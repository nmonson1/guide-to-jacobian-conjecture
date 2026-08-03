#!/usr/bin/env python3
"""Validate the graph-native Living Guide source and publication boundary."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader

from generate_living_guide_v2 import (
    CLAIM_GRAPH_DATA_DIR,
    LITERAL_MANUSCRIPT_LINK_RE,
    MANUSCRIPTS_DATA_DIR,
    MANUSCRIPT_SOURCES_DATA_DIR,
    MODEL_BRIEFS_DATA_DIR,
    PUBLICATION_DATA_DIR,
    PUBLIC_DOCS_DIR,
    SITE_STATE,
    TECHNICAL_MATERIALS_DATA_DIR,
    _protect_formula_like_markdown,
    build_release_metadata,
    load_manuscript_sources,
    load_retained_math,
    load_retained_math_v2,
    proof_source_route,
    retained_corrections,
    retained_v2_compatibility,
    retained_v2_graph,
    retained_v2_is_full,
    resolve_manuscript_links,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / PUBLIC_DOCS_DIR
GRAPH_DATA = ROOT / "data" / CLAIM_GRAPH_DATA_DIR
PUBLICATION_DATA = ROOT / "data" / PUBLICATION_DATA_DIR
MODEL_BRIEF_DATA = ROOT / "data" / MODEL_BRIEFS_DATA_DIR
TEXT_SUFFIXES = {
    ".md", ".yml", ".yaml", ".json", ".css", ".js", ".txt", ".tex", ".bib"
}
FORBIDDEN = (
    "/fss/",
    "/home/",
    "file://",
    "chatgpt.com/share",
    "JC-CAN-",
    "JC-PKG-",
    "conversation_id",
    "message_id",
    "occurrence_id",
    "private_locator",
    "artifact_group_id",
    "INTAKE-",
    "github.com/nmonson1/jacobian-research",
)
FORBIDDEN_PATTERNS = (
    re.compile(
        r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-"
        r"[0-9a-f]{4}-[0-9a-f]{12}\b",
        re.IGNORECASE,
    ),
)
TEMPLATE_PHRASES = (
    "The theorem-level package is centered on the following mechanism",
    "Begin with the precise statement, then use the component statements",
    "A proof is present in the working research record",
)
REQUIRED_NAV = ("Start", "Understand", "Results", "Research", "Evidence", "About")
CLAIM_TAG_PATTERN = re.compile(r"JCG-[0-9A-F]{8}")
HANDOFF_STRUCTURE = (
    "## Current mathematical corpus",
    "## Current research entrypoints",
    "## Strategy and connections",
)
HANDOFF_STATUS_BUREAUCRACY = (
    "review status",
    "audit status",
    "last audited",
    "independent review",
    "independent specialist review",
    "specialist review",
    "specialist-review",
    "review gate",
)
STATE_LANE_LINKS = tuple(
    f"]({slug}.md)" for _, slug in (
        (1, "cubic-flatness-normalization-defects"),
        (2, "boundary-completeness-torelli-at-infinity"),
        (3, "bounded-degree-deformation-modulus-onset"),
        (4, "quartic-endgame"),
        (5, "intrinsic-degree-valuative-budgets"),
        (6, "homogeneous-realization-compression"),
        (7, "five-dimensional-collision-geometry"),
        (8, "plane-newton-queue-terminal-certificates"),
        (9, "plane-chart-correspondence-global-attachment"),
    )
)
LANE_HANDOFF_STRUCTURE = (
    "## Scope",
    "## Setup and definitions",
    "## Results to use",
    "## Live problem",
    "## Tasks",
    "## Limits",
    "## Direct sources",
)
LANE_HANDOFF_V7C_SEMANTIC_GROUPS = (
    ("purpose", ("## Scope", "## Why this lane matters")),
    (
        "setup",
        (
            "## Setup and definitions",
            "## Setup and notation",
            "## Newton-root conventions",
            "## Fixed \\(F_2\\) chart and support",
        ),
    ),
    (
        "reusable mathematics",
        (
            "## Results to use",
            "## Reusable mathematics",
            "## Closed mathematics below 125",
        ),
    ),
    ("live problem", ("## Live problem",)),
    ("ready task", ("## Tasks", "## Ready task ", "## Interface-ready task ")),
    (
        "scope boundary",
        (
            "## Limits",
            "## Non-ready follow-up",
            "## Optional exact-CAS route",
            "## Non-ready \\(F_2\\) integrations",
        ),
    ),
    ("sources", ("## Direct sources", "## Exact sources")),
)
PORTFOLIO_V7C_SEMANTIC_GROUPS = (
    ("lane entrypoints", ("## Choose a lane", "## Lane entrypoints")),
    ("connections", ("## Connections worth testing",)),
)
HANDOFF_OPENING_BUREAUCRACY = (
    "handoff source v",
    "site release living-guide-",
    "public claim records",
    "grouped packages",
    "retained working graph",
    "current proof sources — preferred",
)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _sensitive(text: str, label: str, failures: list[str]) -> None:
    lowered = text.casefold()
    for value in FORBIDDEN:
        if value.casefold() in lowered:
            failures.append(f"{label}: forbidden publication marker {value!r}")
    uuid_text = re.sub(r"https?://[^\s)\]}>\"']+", "", text)
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(uuid_text):
            failures.append(f"{label}: forbidden UUID")


def _local_links(path: Path, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    link_text = re.sub(r"~~~.*?~~~|```.*?```", "", text, flags=re.DOTALL)
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", link_text)
    targets += re.findall(r'href="([^"]+)"', link_text)
    for raw in targets:
        target = raw.split("#", 1)[0]
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        candidate = (path.parent / target).resolve()
        if target.endswith("/") and not candidate.exists():
            candidate = (path.parent / target.rstrip("/")).with_suffix(".md").resolve()
        if not candidate.exists():
            failures.append(f"{path.relative_to(ROOT)}: missing link {target!r}")


def main() -> int:
    failures: list[str] = []
    graph = json.loads((GRAPH_DATA / "claim-graph.json").read_text())
    graph_manifest = json.loads((GRAPH_DATA / "manifest.json").read_text())
    publication = json.loads(
        (PUBLICATION_DATA / "public-export.json").read_text()
    )
    expected = SITE_STATE["expected_counts"]
    expected_graph = {
        "claims": expected["technical_records"],
        "collections": expected["grouped_pages"],
        "programs": expected["research_programs"],
        "memberships": expected["memberships"],
    }
    if graph["counts"] != expected_graph:
        failures.append("claim graph counts disagree with site state")
    if publication["counts"] != expected:
        failures.append("sanitized publication counts disagree with site state")
    graph_file = GRAPH_DATA / graph_manifest["files"][0]["path"]
    if _sha(graph_file) != graph_manifest["files"][0]["sha256"]:
        failures.append("claim graph manifest digest mismatch")

    claims = {item["tag"]: item for item in graph["claims"]}
    collections = {item["slug"]: item for item in graph["collections"]}
    if len(claims) != expected["technical_records"]:
        failures.append("duplicate or missing stable claim tags")
    if len(collections) != expected["grouped_pages"]:
        failures.append("duplicate or missing collection slugs")
    for tag, claim in claims.items():
        if not re.fullmatch(r"JCG-[0-9A-F]{8}", tag):
            failures.append(f"invalid stable public tag: {tag}")
        if "…" in claim["title"] or claim["title"].endswith("..."):
            failures.append(f"{tag}: truncated title remains")
        if not claim.get("statement_version"):
            failures.append(f"{tag}: missing statement version")
        for field in (
            "prominence",
            "status",
            "provenance",
            "verification",
            "proof_access",
            "memberships",
            "public",
        ):
            if field not in claim:
                failures.append(f"{tag}: missing graph field {field}")

    claim_files = sorted((DOCS / "claims").glob("*.md"))
    collection_files = sorted((DOCS / "collections").glob("*.md"))
    program_files = sorted((DOCS / "research/programs").glob("*.md"))
    if len(claim_files) != expected["technical_records"]:
        failures.append(f"expected {expected['technical_records']} claim pages")
    if len(collection_files) != expected["grouped_pages"]:
        failures.append(f"expected {expected['grouped_pages']} collection pages")
    if len(program_files) != expected["research_programs"]:
        failures.append(f"expected {expected['research_programs']} program pages")
    retained_v2 = load_retained_math_v2(ROOT)
    full_v2_payload = (
        retained_v2[1]
        if retained_v2 is not None and retained_v2_is_full(retained_v2[1])
        else None
    )
    full_v2_graph = (
        retained_v2_graph(full_v2_payload)
        if full_v2_payload is not None
        else None
    )
    full_compatibility = (
        retained_v2_compatibility(full_v2_payload)
        if full_v2_payload is not None
        else None
    )
    compatibility_routes = (
        {
            item["legacy_unit_id"]: item
            for item in full_compatibility["routes"]
        }
        if full_compatibility is not None
        else {}
    )
    retained = load_retained_math(ROOT)
    corrections: dict[str, dict[str, object]] = {}
    retained_unit_ids: set[str] = set()
    if retained is None:
        failures.append("selected release does not pin retained mathematics")
    else:
        retained_manifest, retained_graph = retained
        if full_v2_payload is None:
            corrections = retained_corrections(retained)
        retained_unit_ids = {
            unit["unit_id"] for unit in retained_graph["units"]
        }
        retained_state = SITE_STATE["retained_math"]
        retained_units = sorted(
            (DOCS / "research/working-mathematics/units").glob("*.md")
        )
        retained_programs = sorted(
            (DOCS / "research/working-mathematics/programs").glob("*.md")
        )
        if retained_graph["counts"]["units"] != retained_state["expected_units"]:
            failures.append("retained-math unit count disagrees with site state")
        if (
            retained_graph["counts"]["programs"]
            != retained_state["expected_programs"]
        ):
            failures.append("retained-math program count disagrees with site state")
        expected_retained_units = (
            full_v2_graph["counts"]["units"]
            if full_v2_graph is not None
            else retained_state["expected_units"]
        )
        expected_retained_programs = (
            full_v2_graph["counts"]["programs"]
            if full_v2_graph is not None
            else retained_state["expected_programs"]
        )
        if len(retained_units) != expected_retained_units:
            failures.append("retained working-unit page count changed")
        if len(retained_programs) != expected_retained_programs:
            failures.append("retained program-view page count changed")
        if retained_manifest["source_registry_id"] != retained_graph["registry_id"]:
            failures.append("retained registry identity disagrees")
    v2_selection: dict[str, object] | None = None
    if retained_v2 is None:
        failures.append("selected release does not pin retained-math v2")
    else:
        _, v2_selection = retained_v2
        if retained_v2_is_full(v2_selection):
            graph = retained_v2_graph(v2_selection)
            compatibility = retained_v2_compatibility(v2_selection)
            assert compatibility is not None
            if compatibility["counts"]["routes"] != len(claims):
                failures.append("full retained-math compatibility is not total")
            for relative, value in (
                ("research/working-mathematics/graph.json", graph),
                (
                    "research/working-mathematics/legacy-compatibility.json",
                    compatibility,
                ),
            ):
                machine = DOCS / relative
                if not machine.is_file():
                    failures.append(f"missing machine-readable retained math: {relative}")
                elif json.loads(machine.read_text(encoding="utf-8")) != value:
                    failures.append(f"rendered retained math disagrees: {relative}")
        else:
            expected_v2_ids = {
                "arguments": ["ARG-RMU5D8E0003-FINITE-PLANE"],
                "evidence": [
                    "EVD-RMU5D8E0003-EXCEPTIONAL-CUBIC",
                    "EVD-RMU5D8E0003-GENERIC-CUBIC",
                    "EVD-RMU5D8E0003-QUARTIC-SEPARATOR",
                ],
                "obligations": ["OBL-P5-FULL-FINITE-ROW-BASE"],
                "tasks": ["TSK-P5-FULL-FINITE-ROW-BASE"],
                "units": ["RMU-5D8E0001", "RMU-5D8E0002", "RMU-5D8E0003"],
            }
            if v2_selection["selected_ids"] != expected_v2_ids:
                failures.append("retained-math v2 pilot selection changed")
            machine_selection = (
                DOCS / "research/handoffs/retained-math-v2-pilot.json"
            )
            if not machine_selection.is_file():
                failures.append("machine-readable retained-math v2 selection is missing")
            elif json.loads(machine_selection.read_text(encoding="utf-8")) != v2_selection:
                failures.append("rendered retained-math v2 selection disagrees")
    source_manifest = load_manuscript_sources(ROOT)
    source_files: dict[str, dict[str, object]] = {}
    if source_manifest is None:
        failures.append("selected release does not pin manuscript sources")
    else:
        source_files = {item["path"]: item for item in source_manifest["files"]}
        source_state = SITE_STATE["manuscript_sources"]
        source_pages = sorted(
            (DOCS / "research/proof-sources").rglob("*.md")
        )
        if len(source_files) != source_state["expected_files"]:
            failures.append("manuscript-source file count disagrees with site state")
        if len(source_manifest["labels"]) != source_state["expected_labels"]:
            failures.append("manuscript-source label count disagrees with site state")
        if len(source_pages) != source_state["expected_files"] + 1:
            failures.append("text-proof source page count changed")
        if retained is not None and (
            source_manifest["retained_registry"]["registry_id"]
            != retained[1]["registry_id"]
        ):
            failures.append("manuscript sources pin the wrong retained registry")
        for item in source_manifest["files"]:
            page = DOCS / proof_source_route(str(item["path"]))
            if not page.is_file():
                failures.append(f"missing text-proof source page: {item['path']}")
                continue
            text = page.read_text(encoding="utf-8")
            for marker in (str(item["path"]), str(item["sha256"]), "## Complete source"):
                if marker not in text:
                    failures.append(
                        f"{page.relative_to(ROOT)}: missing source marker {marker!r}"
                    )
        if retained is not None:
            for unit in retained[1]["units"]:
                for support in unit.get("support", []):
                    for key in ("locator", "source_locator"):
                        locator = support.get(key)
                        if not isinstance(locator, dict):
                            continue
                        repo_path = str(locator.get("repo_path", ""))
                        if locator.get("kind") != "repo" or not repo_path.startswith(
                            "manuscripts/"
                        ):
                            continue
                        relative = repo_path.removeprefix("manuscripts/")
                        item = source_files.get(relative)
                        if item is None:
                            failures.append(
                                f"{unit['unit_id']}: unpublished manuscript source {relative}"
                            )
                            continue
                        anchor = locator.get("anchor")
                        labels = {label["label"] for label in item["labels"]}
                        if anchor and anchor not in labels:
                            failures.append(
                                f"{unit['unit_id']}: missing source label {relative}#{anchor}"
                            )
    locator_pages = 0
    for path in claim_files:
        text = path.read_text(encoding="utf-8")
        if path.stem not in claims:
            failures.append(f"{path.relative_to(ROOT)}: unknown public tag")
        disposition = compatibility_routes.get(path.stem, {}).get("disposition")
        required_headings = (
            ()
            if disposition in {"replacement", "split_replacement", "archival"}
            else ("## Exact statement", "## Appears in", "## Proof access and evidence boundary")
        )
        for heading in required_headings:
            if heading not in text:
                failures.append(f"{path.relative_to(ROOT)}: missing {heading}")
        if "## Proof locators" in text:
            locator_pages += 1
        _local_links(path, failures)
    for tag, correction in corrections.items():
        unit_id = str(correction["unit_id"])
        relation = str(correction["_forward_relation"])
        historical = relation in {"corrects", "supersedes"}
        if tag not in claims:
            failures.append(f"retained correction targets unknown claim {tag}")
            continue
        if historical and tag in retained_unit_ids:
            failures.append(f"superseded legacy claim remains in working graph: {tag}")
        page = DOCS / "claims" / f"{tag}.md"
        text = page.read_text(encoding="utf-8")
        relation_markers = (
            (
                '!!! warning "Replaced by current working mathematics"',
                "## Current replacement",
            )
            if historical
            else ('!!! info "A stronger current result is available"',)
        )
        expected_markers = (*relation_markers, unit_id)
        if historical:
            expected_markers = (*expected_markers, str(correction["statement"]))
        for marker in expected_markers:
            if marker not in text:
                failures.append(
                    f"{page.relative_to(ROOT)}: missing correction marker {marker!r}"
                )
        unit_page = (
            DOCS
            / "research/working-mathematics/units"
            / f"{unit_id}.md"
        )
        if not unit_page.is_file():
            failures.append(f"retained correction page is missing: {unit_id}")
    # Proof locators are the reason the coverage sidecar ships; losing them
    # from the graph or the renderer should fail loudly, not silently.
    expected_locator_pages = sum(
        1
        for tag, claim in claims.items()
        if claim.get("locators")
        and compatibility_routes.get(tag, {}).get("disposition")
        not in {"replacement", "split_replacement", "archival"}
    )
    if locator_pages != expected_locator_pages:
        failures.append(
            f"claim pages with a Proof locators section: expected "
            f"{expected_locator_pages}, found {locator_pages}"
        )
    if locator_pages < 300:
        failures.append(
            f"fewer than 300 claim pages carry proof locators: {locator_pages}"
        )
    for path in collection_files:
        text = path.read_text(encoding="utf-8")
        if path.stem not in collections:
            failures.append(f"{path.relative_to(ROOT)}: unknown collection")
        for heading in ("## Precise statement", "## Claims in this result package", "## Evidence and manuscript boundary"):
            if heading not in text:
                failures.append(f"{path.relative_to(ROOT)}: missing {heading}")
        _local_links(path, failures)
    for tag, correction in corrections.items():
        unit_id = str(correction["unit_id"])
        relation = str(correction["_forward_relation"])
        claim_page = DOCS / "claims" / f"{tag}.md"
        claim_text = claim_page.read_text(encoding="utf-8")
        expected_label = (
            "Replaced by current working mathematics"
            if relation in {"corrects", "supersedes"}
            else "A stronger current result is available"
        )
        if unit_id not in claim_text or expected_label not in claim_text:
            failures.append(
                f"{claim_page.relative_to(ROOT)}: missing {relation} forward link "
                f"to {unit_id}"
            )
        for membership in claims[tag]["memberships"]:
            collection = DOCS / "collections" / f"{membership['collection_slug']}.md"
            collection_text = collection.read_text(encoding="utf-8")
            if unit_id not in collection_text:
                failures.append(
                    f"{collection.relative_to(ROOT)}: corrected legacy member "
                    f"does not link {unit_id}"
                )
            if relation in {"corrects", "supersedes"}:
                heading = f"### [{tag} · Replaced historical record]"
                start = collection_text.find(heading)
                end = collection_text.find("\n### ", start + len(heading))
                block = collection_text[start : end if end >= 0 else None]
                if start < 0 or claims[tag]["statement"] in block:
                    failures.append(
                        f"{collection.relative_to(ROOT)}: replaced statement {tag} "
                        "is still rendered as collection mathematics"
                    )
        corrections_page = DOCS / "results/corrections.md"
        if unit_id not in corrections_page.read_text(encoding="utf-8"):
            failures.append(
                f"results/corrections.md omits retained correction {unit_id}"
            )

    if full_v2_graph is not None:
        v2_units = {item["unit_id"]: item for item in full_v2_graph["units"]}
        for tag, route in compatibility_routes.items():
            page = DOCS / "claims" / f"{tag}.md"
            text = page.read_text(encoding="utf-8")
            disposition = route["disposition"]
            if disposition in {"replacement", "split_replacement", "archival"}:
                if claims[tag]["statement"] in text:
                    failures.append(
                        f"{page.relative_to(ROOT)}: stale historical statement is rendered"
                    )
            if disposition in {"exact_current", "valid_weaker"}:
                target = next(
                    item
                    for item in route["targets"]
                    if item["role"] == "current_statement"
                )
                current_statement = _protect_formula_like_markdown(
                    v2_units[target["unit_id"]]["statement"]
                )
                if current_statement not in text:
                    failures.append(
                        f"{page.relative_to(ROOT)}: current mathematics is missing"
                    )
            if disposition == "valid_weaker" and (
                "A stronger current result is available" not in text
            ):
                failures.append(
                    f"{page.relative_to(ROOT)}: valid weaker route lacks stronger link"
                )
            if disposition in {"replacement", "split_replacement"}:
                for target in route["targets"]:
                    if target["unit_id"] not in text:
                        failures.append(
                            f"{page.relative_to(ROOT)}: replacement target is missing"
                        )
            if disposition == "archival":
                if "Historical claim" not in text:
                    failures.append(
                        f"{page.relative_to(ROOT)}: archival status is unclear"
                    )
                for membership in claims[tag]["memberships"]:
                    collection = (
                        DOCS
                        / "collections"
                        / f"{membership['collection_slug']}.md"
                    )
                    if tag in collection.read_text(encoding="utf-8"):
                        failures.append(
                            f"{collection.relative_to(ROOT)}: archival route remains in current collection"
                        )
        for unit in full_v2_graph["units"]:
            page = (
                DOCS
                / "research/working-mathematics/units"
                / f"{unit['unit_id']}.md"
            )
            text = page.read_text(encoding="utf-8")
            for relation in ("corrects", "strengthens", "supersedes"):
                if f"- `{relation}`" in text:
                    failures.append(
                        f"{page.relative_to(ROOT)}: backward compatibility relation is rendered"
                    )
            for marker in ("review_state", "audit_current", "last audited"):
                if marker in text.casefold():
                    failures.append(
                        f"{page.relative_to(ROOT)}: internal workflow marker {marker!r}"
                    )

    for path in DOCS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for phrase in TEMPLATE_PHRASES:
            if phrase in text:
                failures.append(f"{path.relative_to(ROOT)}: legacy template prose remains")
        # Privacy backstop for the locator sidecar: even a partial private
        # canonical id must never appear on a rendered page.
        if "JC-CAN" in text:
            failures.append(f"{path.relative_to(ROOT)}: private canonical id marker")
        _local_links(path, failures)

    for public_subtree in ("claims", "collections"):
        for path in sorted((DOCS / public_subtree).glob("*.md")):
            text = path.read_text(encoding="utf-8").casefold()
            for editorial_marker in (
                "review pending",
                "independent review",
                "locator audit incomplete",
                "locator audit needed",
            ):
                if editorial_marker in text:
                    failures.append(
                        f"{path.relative_to(ROOT)}: public mathematical page "
                        f"exposes editorial workflow marker {editorial_marker!r}"
                    )

    brief_manifest = json.loads(
        (MODEL_BRIEF_DATA / "manifest.json").read_text(encoding="utf-8")
    )
    manuscript_manifest = json.loads(
        (ROOT / "data" / MANUSCRIPTS_DATA_DIR / "manifest.json").read_text()
    )
    manuscripts_by_sequence = {
        item["filename"][:2]: item for item in manuscript_manifest["manuscripts"]
    }
    if brief_manifest["brief_count"] != SITE_STATE["model_briefs"]["expected_count"]:
        failures.append("model brief count changed")
    if brief_manifest["brief_count"] != len(brief_manifest["briefs"]):
        failures.append("model brief manifest count mismatch")
    if brief_manifest.get("primary_entrypoint_count") != 10:
        failures.append("primary model-entrypoint count is not ten")
    task_inputs = brief_manifest.get("task_inputs", [])
    is_v7_handoff = (
        brief_manifest.get("schema_version") == 7
        and brief_manifest.get("source_handoff", {}).get("handoff_version")
        in {"7c", "7d", "7e", "7f", "7g", "7h", "7i"}
    )
    if brief_manifest.get("task_input_count", 0) != len(task_inputs):
        failures.append("model task-input count mismatch")
    if brief_manifest.get("schema_version") == 5 and {
        item.get("input_id") for item in task_inputs
    } != {
        "LANE7-COLLISION-CHART-V1",
        "LANE8-RAW-SUPPORT-RECONSTRUCTION-V1",
    }:
        failures.append("handoff v5 must expose the exact Lane 7 and Lane 8 inputs")
    if brief_manifest.get("schema_version") == 6:
        expected_source_packets = {
            f"LANE{sequence}-RESEARCH-SOURCE-PACKET-V1"
            for sequence in range(1, 10)
        }
        expected_inputs = expected_source_packets | {
            "LANE7-COLLISION-CHART-V1",
            "LANE8-RAW-SUPPORT-RECONSTRUCTION-V1",
        }
        if {item.get("input_id") for item in task_inputs} != expected_inputs:
            failures.append(
                "handoff v6 must expose nine research packets and the exact "
                "Lane 7 and Lane 8 inputs"
            )
    if brief_manifest.get("schema_version") == 7:
        expected_source_packets = {
            f"LANE{sequence}-RESEARCH-SOURCE-PACKET-V2"
            for sequence in range(1, 10)
        }
        expected_inputs = expected_source_packets | {
            "LANE7-COLLISION-CHART-V1",
            "LANE8-RAW-SUPPORT-RECONSTRUCTION-V1",
        }
        if {item.get("input_id") for item in task_inputs} != expected_inputs:
            failures.append(
                "handoff v7 must expose nine research packets and the exact "
                "Lane 7 and Lane 8 inputs"
            )
    for item in task_inputs:
        source = MODEL_BRIEF_DATA / item["source"]
        rendered = DOCS / item["route"]
        if not source.is_file() or _sha(source) != item["sha256"]:
            failures.append(f"model task-input source mismatch: {item['source']}")
            continue
        if len(source.read_bytes()) != item["bytes"]:
            failures.append(f"model task-input byte count mismatch: {item['source']}")
        if not rendered.is_file() or _sha(rendered) != item["sha256"]:
            failures.append(f"model task-input render mismatch: {item['route']}")
        text = source.read_text(encoding="utf-8")
        markers_by_id = {
            "LANE7-COLLISION-CHART-V1": (
                "# Lane 7 exact collision-chart input",
                "15 primitive integer quintics",
                "det(T)*(u3-u4*v3) != 0",
                "## Complete Macaulay2 input",
                "## Exact evidence boundary",
            ),
            "LANE8-RAW-SUPPORT-RECONSTRUCTION-V1": (
                "# Lane 8 exact raw-support reconstruction input",
                "## Mathematical contract",
                "## Exact quintic-field relations",
                "## Exact quintic-field helper",
                "quintic_field_fast.py",
                "## Complete reconstruction program",
            ),
        }
        input_id = str(item.get("input_id", ""))
        source_packet_match = re.fullmatch(
            r"LANE(?P<sequence>[1-9])-RESEARCH-SOURCE-PACKET-V[12]",
            input_id,
        )
        source_packet_markers: tuple[str, ...] = ()
        if source_packet_match is not None:
            sequence = source_packet_match.group("sequence")
            source_packet_markers = (
                f"# Lane {sequence} exact research source packet",
                "## Included files",
            )
            if sequence == "8":
                source_packet_markers += (
                    "lane8-full-root-closure-20260803-v1/FULL_ROOT_CLOSURE_PROOF.md",
                    "lane8-full-root-closure-20260803-v1/verify_lane8_packet.py",
                    "F2_degree125_boundary_seed.md",
                    "terminal_primary_belyi.py",
                    "terminal_face_rigidity.py",
                    "planar-descent-no-go-20260802-v1/README.md",
                    "Status: incomplete proof strategy",
                    "hc4_square_correction_no_go.py",
                )
            elif sequence == "4":
                source_packet_markers += (
                    "lane4-f4-contract-20260803-v1/F4_INPUT_CONTRACT.md",
                    "lane4-f4-contract-20260803-v1/f4-contract.schema.json",
                    "lane4-f4-contract-20260803-v1/verify_contract_and_routing.py",
                )
            elif sequence == "7":
                source_packet_markers += (
                    "lane7-projective-kernel-20260803-v1/generate_macaulay2_input.py",
                    "lane7-projective-kernel-20260803-v1/generate_kernel_chart_singular.py",
                    "lane7-projective-kernel-20260803-v1/test_plucker_transport.py",
                )
            if is_v7_handoff:
                records = item.get("source_packet", {}).get("files", [])
                packet_anchors = [record.get("packet_anchor") for record in records]
                if len(packet_anchors) != len(set(packet_anchors)):
                    failures.append(f"{item['source']}: duplicate source anchors")
                for record in records:
                    anchor = record.get("packet_anchor")
                    repo_path = record.get("repo_path")
                    if not isinstance(anchor, str) or re.fullmatch(
                        r"source-[0-9a-f]{16}", anchor
                    ) is None:
                        failures.append(
                            f"{item['source']}: invalid source anchor for {repo_path}"
                        )
                        continue
                    if text.count(f'id="{anchor}"') != 1:
                        failures.append(
                            f"{item['source']}: source anchor {anchor!r} is not unique"
                        )
                    if f"](#{anchor})" not in text:
                        failures.append(
                            f"{item['source']}: source index omits {anchor!r}"
                        )
        for marker in (*markers_by_id.get(input_id, ()), *source_packet_markers):
            if marker not in text:
                failures.append(f"{item['source']}: missing {marker!r}")
    brief_routes: set[str] = set()
    found_v2_markers: list[dict[str, str]] = []
    for brief in brief_manifest["briefs"]:
        kind = brief.get("kind")
        source = MODEL_BRIEF_DATA / brief["source"]
        rendered = DOCS / brief["route"]
        if not source.is_file() or _sha(source) != brief["sha256"]:
            failures.append(f"model brief source mismatch: {brief['source']}")
            continue
        source_text = source.read_text(encoding="utf-8")
        rendered_text = rendered.read_text(encoding="utf-8")
        front_matter_end = rendered_text.find("\n---\n", 4)
        visible_lines = [
            line.strip()
            for line in rendered_text[front_matter_end + 5 :].splitlines()
            if line.strip()
        ] if front_matter_end >= 0 else []
        if not visible_lines or not visible_lines[0].startswith("# "):
            failures.append(
                f"{brief['route']}: mathematical title is not the first visible content"
            )
        title_position = rendered_text.find("\n# ", front_matter_end)
        identity_position = rendered_text.find('class="claim-tag"', front_matter_end)
        if title_position < 0 or identity_position <= title_position:
            failures.append(f"{brief['route']}: lane identity does not follow the title")
        opening = "\n".join(visible_lines[:8]).casefold()
        for marker in HANDOFF_OPENING_BUREAUCRACY:
            if marker in opening:
                failures.append(
                    f"{brief['route']}: opening contains repository plumbing {marker!r}"
                )
        literal_links = LITERAL_MANUSCRIPT_LINK_RE.findall(source_text)
        if literal_links:
            failures.append(
                f"{brief['source']}: literal manuscript filename(s) bypass "
                f"the active manifest: {', '.join(sorted(set(literal_links)))}"
            )
        try:
            resolve_manuscript_links(source_text, manuscripts_by_sequence)
        except ValueError as exc:
            failures.append(f"{brief['source']}: {exc}")
        if kind == "lane":
            if is_v7_handoff:
                for name, alternatives in LANE_HANDOFF_V7C_SEMANTIC_GROUPS:
                    if not any(
                        heading.casefold() in source_text.casefold()
                        for heading in alternatives
                    ):
                        failures.append(
                            f"{brief['source']}: missing v7c lane semantic "
                            f"group {name!r}"
                        )
            else:
                for marker in LANE_HANDOFF_STRUCTURE:
                    if marker.casefold() not in source_text.casefold():
                        failures.append(
                            f"{brief['source']}: missing lane semantic "
                            f"marker {marker!r}"
                        )
            if ".md)" not in source_text:
                failures.append(f"{brief['source']}: lane has no deeper route")
            if brief_manifest.get("schema_version") in {6, 7}:
                expected_packet = (
                    f"lane-{brief['lane_sequence']}-source-packet.md"
                )
                if expected_packet not in source_text:
                    failures.append(
                        f"{brief['source']}: lane does not link its public "
                        "research source packet"
                    )
                if (
                    brief_manifest.get("schema_version") == 6
                    and brief.get("lane_sequence") == 8
                ):
                    for marker in (
                        "idea for a proof, but not fully proved",
                        "RMU-6D8E0011",
                        "not a theorem and not a proof",
                    ):
                        if marker not in source_text:
                            failures.append(
                                f"{brief['source']}: incomplete strategy lacks "
                                f"explicit boundary {marker!r}"
                            )
                scoped_markers = {
                    3: (
                        "rmu-3fef0011",
                        "rmu-9075e072",
                        "sharp stable-equivalence complexity",
                        "03-direct-order-five-recovery-2026-08-03-v1.zip",
                        "recovered order-five row spaces are exact",
                    ),
                    4: (
                        "rmu-2d4e0011",
                        "rmu-2d4e0012",
                        "rmu-2d4e0013",
                        "rmu-2d4e0014",
                        "q4-f4",
                        "not a missing quartic case-tree edge",
                    ),
                    7: (
                        "rmu-5c7e0011",
                        "rmu-5c7e0012",
                        "five affine charts",
                        "characteristic-zero dimensions",
                        r"\eta_{ij}",
                        "pluecker-open",
                    ),
                    8: (
                        "rmu-6d8e0013",
                        "rmu-6d8e0014",
                        "complete-chain refinement",
                        "maximal newton-bounded",
                        "06-f2-support-windows-order-520-2026-08-03-v1.zip",
                        "order-530 value is not an obstruction",
                        "strictly below `125`",
                    ),
                    9: ("rmu-6d8e0012", "begins at layer seven, not four"),
                }
                if brief_manifest.get("schema_version") == 6:
                    source_casefold = source_text.casefold()
                    for marker in scoped_markers.get(
                        brief.get("lane_sequence"), ()
                    ):
                        if marker not in source_casefold:
                            failures.append(
                                f"{brief['source']}: scoped repair lacks {marker!r}"
                            )
                    if brief.get("lane_sequence") == 8 and (
                        "after the canonical `k=4` rechart" in source_text
                    ):
                        failures.append(
                            f"{brief['source']}: superseded canonical k=4 bridge survived"
                        )
            marker_ids = re.findall(
                r"<!-- retained-math-v2-selection:([A-Z0-9-]+) -->",
                source_text,
            )
            found_v2_markers.extend(
                {
                    "program_slug": brief["program_slug"],
                    "argument_id": argument_id,
                }
                for argument_id in marker_ids
            )
        elif kind == "program":
            for marker in HANDOFF_STRUCTURE:
                if marker.casefold() not in source_text.casefold():
                    failures.append(
                        f"{brief['source']}: missing handoff semantic marker {marker!r}"
                    )
        elif kind == "cross_program":
            if is_v7_handoff:
                for name, alternatives in PORTFOLIO_V7C_SEMANTIC_GROUPS:
                    if not any(
                        heading.casefold() in source_text.casefold()
                        for heading in alternatives
                    ):
                        failures.append(
                            f"{brief['source']}: missing v7c portfolio "
                            f"semantic group {name!r}"
                        )
            else:
                for marker in (
                    "## Lane entrypoints",
                    "## Connections worth testing",
                ):
                    if marker.casefold() not in source_text.casefold():
                        failures.append(
                            f"{brief['source']}: missing portfolio marker "
                            f"{marker!r}"
                        )
        for tag in CLAIM_TAG_PATTERN.findall(source_text):
            if tag not in claims:
                failures.append(f"{brief['source']}: unknown claim tag {tag}")
        source_lower = source_text.casefold()
        for marker in HANDOFF_STATUS_BUREAUCRACY:
            if marker in source_lower:
                failures.append(
                    f"{brief['source']}: handoff carries non-research status "
                    f"bureaucracy {marker!r}"
                )
        if kind == "cross_program":
            lane_positions = [
                source_text.find(link) for link in STATE_LANE_LINKS
            ]
            if any(position < 0 for position in lane_positions) or (
                lane_positions != sorted(lane_positions)
            ):
                failures.append(
                    f"{brief['source']}: missing or unordered nine-lane anchors"
                )
            autonomy_phrases = (
                ("invitations",),
                (
                    "rather than dependencies",
                    "not prerequisites",
                )
                if is_v7_handoff
                else ("not prerequisites",),
            )
            for alternatives in autonomy_phrases:
                if any(phrase in source_text for phrase in alternatives):
                    continue
                failures.append(
                    f"{brief['source']}: missing research-autonomy "
                    f"language {' or '.join(repr(value) for value in alternatives)}"
                )
        elif kind == "program":
            graph_route = (
                "../working-mathematics/programs/"
                f"{brief['program_slug']}.md"
            )
            if graph_route not in source_text:
                failures.append(
                    f"{brief['source']}: program overlay lacks its graph view"
                )
            for stale_heading in ("Reusable inputs", "Proof-signature index"):
                if stale_heading in source_text:
                    failures.append(
                        f"{brief['source']}: duplicated dossier mathematics remains"
                    )
        if len(source.read_bytes()) != brief["bytes"]:
            failures.append(f"model brief byte count mismatch: {brief['source']}")
        if len(source_text.split()) != brief["words"]:
            failures.append(f"model brief word count mismatch: {brief['source']}")
        if brief["route"] in brief_routes:
            failures.append(f"duplicate model brief route: {brief['route']}")
        brief_routes.add(brief["route"])
        if kind == "lane":
            lower, upper = 350, 2000
        elif kind == "program":
            lower, upper = 100, 800
        else:
            lower, upper = 150, 1500
        if not lower <= brief["words"] <= upper:
            failures.append(
                f"model brief word count outside {lower}-{upper}: {brief['source']}"
            )
        if not rendered.is_file():
            failures.append(f"missing rendered model brief: {brief['route']}")
            continue
        rendered_text = rendered.read_text(encoding="utf-8")
        if "{{MANUSCRIPT_" in rendered_text:
            failures.append(f"{brief['route']}: unresolved manuscript token")
        for marker in (
            'class="handoff-snapshot"',
            f"site release {SITE_STATE['release_id']}",
        ):
            if marker in rendered_text:
                failures.append(f"{brief['route']}: obsolete release plumbing remains")
        for marker in (
            "## Sources and release",
            "[Retained working mathematics]",
            "[Current proof sources]",
            "[Machine-readable release metadata](release.json)",
        ):
            if marker not in rendered_text:
                failures.append(f"{brief['route']}: missing footer marker {marker!r}")
        if kind == "lane" and is_v7_handoff:
            expected_heading_groups = LANE_HANDOFF_V7C_SEMANTIC_GROUPS
            expected_headings: tuple[str, ...] = ()
        elif kind == "lane":
            expected_heading_groups = ()
            expected_headings = LANE_HANDOFF_STRUCTURE
        elif kind == "program":
            expected_heading_groups = ()
            expected_headings = HANDOFF_STRUCTURE
        elif is_v7_handoff:
            expected_heading_groups = PORTFOLIO_V7C_SEMANTIC_GROUPS
            expected_headings = ()
        else:
            expected_heading_groups = ()
            expected_headings = (
                "## Lane entrypoints",
                "## Connections worth testing",
            )
        for name, alternatives in expected_heading_groups:
            if not any(heading in rendered_text for heading in alternatives):
                failures.append(
                    f"{brief['route']}: missing v7c lane semantic group {name!r}"
                )
        for heading in expected_headings:
            if heading not in rendered_text:
                failures.append(f"{brief['route']}: missing {heading}")
        if is_v7_handoff and kind in {"lane", "cross_program"}:
            if kind == "lane":
                redundant_identity = (
                    f"Lane {brief['lane_sequence']} · 2026-08-03"
                )
            else:
                redundant_identity = "\nUpdated 3 August 2026\n"
            if redundant_identity in rendered_text:
                failures.append(
                    f"{brief['route']}: duplicate source identity remains"
                )
            if rendered_text.count("## Sources and release") != 1:
                failures.append(
                    f"{brief['route']}: expected one rendered release footer"
                )
            if "\n---\n[Portfolio](state-of-the-program.md)" in rendered_text:
                failures.append(
                    f"{brief['route']}: duplicate compact footer remains"
                )
        if (
            brief_manifest.get("schema_version") < 7
            and brief["program_slug"] == "minimum-degree-and-quartic-exclusions"
        ):
            required_conic = (
                "JCG-24A6190A",
                "JCG-80F5587E",
                "JCG-244F8A2E",
                "all seven quadratic-factor orbits",
            )
            for marker in required_conic:
                if marker not in source_text:
                    failures.append(
                        f"{brief['source']}: incomplete full-conic handoff; "
                        f"missing {marker!r}"
                    )
        if (
            brief_manifest.get("schema_version") < 7
            and brief["program_slug"] == "plane-boundary-obstructions"
        ):
            if "JCG-9D0BE662" in source_text and (
                "Open dependency—not an accepted result" not in source_text
            ):
                failures.append(
                    f"{brief['source']}: open lower-bound dependency is not "
                    "distinguished from accepted inputs"
                )
        if brief.get("primary_entrypoint", False):
            index_page = DOCS / "research/index.md"
            if brief["route"].split("/")[-1] not in index_page.read_text(encoding="utf-8"):
                failures.append(
                    f"research index does not link primary brief: {brief['program_slug']}"
                )
        elif kind == "program":
            program_page = DOCS / "research/programs" / f"{brief['program_slug']}.md"
            if brief["route"].split("/")[-1] not in program_page.read_text(encoding="utf-8"):
                failures.append(f"program page does not link model brief: {brief['program_slug']}")

        if (
            full_v2_payload is None
            and brief["program_slug"] == "homogeneous-realization-compression"
        ):
            if source_text.count(
                "<!-- retained-math-v2-selection:ARG-RMU5D8E0003-FINITE-PLANE -->"
            ) != 1:
                failures.append("Lane 6 does not contain exactly one v2 marker")
            for marker in (
                "\n### Compiler-owned retained result\n",
                "ARG-RMU5D8E0003-FINITE-PLANE",
                "g(r)=(r-4)(r^2-8r+64)",
                "-1152",
                "retained-math-v2-pilot.json",
            ):
                if marker not in rendered_text:
                    failures.append(f"Lane 6 v2 rendering lacks {marker!r}")
        elif "retained-math-v2-selection:" in source_text:
            failures.append(f"unexpected v2 marker in {brief['source']}")

    if found_v2_markers != brief_manifest.get("retained_math_v2_markers"):
        failures.append("handoff v2 markers disagree with their manifest")

    retained_graph = load_retained_math(ROOT)
    if retained_graph is not None:
        exposed_ids = {
            unit["unit_id"]
            for unit in retained_graph[1]["units"]
            if unit.get("exposure") == "exposed"
        }
        for unit_id in exposed_ids:
            unit_page = DOCS / "research/working-mathematics/units" / f"{unit_id}.md"
            unit_text = unit_page.read_text(encoding="utf-8")
            if "This page is generated from the retained graph" in unit_text:
                failures.append(
                    f"{unit_page.relative_to(ROOT)}: generated-page boilerplate remains"
                )
            for relation in ("supersedes", "corrects"):
                if f"- {relation} " in unit_text:
                    failures.append(
                        f"{unit_page.relative_to(ROOT)}: backward historical "
                        f"{relation} relation is rendered"
                    )

    scan_roots = (
        DOCS,
        GRAPH_DATA,
        PUBLICATION_DATA,
        MODEL_BRIEF_DATA,
        ROOT / "data" / SITE_STATE["retained_math_v2"]["data_dir"],
        ROOT / "data" / MANUSCRIPT_SOURCES_DATA_DIR,
        ROOT / "overrides",
    )
    scanned = 0
    for scan_root in scan_roots:
        for path in scan_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            scanned += 1
            _sensitive(path.read_text(encoding="utf-8"), str(path.relative_to(ROOT)), failures)

    if manuscript_manifest["manuscript_count"] != SITE_STATE["manuscripts"]["expected_count"]:
        failures.append("manuscript count changed")
    for item in manuscript_manifest["manuscripts"]:
        source = ROOT / "data" / MANUSCRIPTS_DATA_DIR / item["filename"]
        public = DOCS / "assets/manuscripts" / item["filename"]
        for path in (source, public):
            if not path.is_file() or _sha(path) != item["sha256"]:
                failures.append(f"manuscript digest mismatch: {path}")
        if public.is_file() and len(PdfReader(public).pages) != item["pages"]:
            failures.append(f"manuscript page count mismatch: {item['filename']}")

    release_path = DOCS / "research/handoffs/release.json"
    expected_release = build_release_metadata(ROOT)
    if not release_path.is_file():
        failures.append("machine-readable handoff release is missing")
    else:
        try:
            found_release = json.loads(release_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            failures.append("machine-readable handoff release is invalid JSON")
        else:
            if found_release != expected_release:
                failures.append(
                    "machine-readable handoff release disagrees with site state"
                )

    manuscript_versions = {
        item["version"] for item in manuscript_manifest["manuscripts"]
    }
    if len(manuscript_versions) != 1:
        failures.append("selected manuscript release mixes versions")
        manuscript_version = "mixed"
    else:
        manuscript_version = str(next(iter(manuscript_versions)))
    home_text = (DOCS / "index.md").read_text(encoding="utf-8")
    home_summary = (
        f"Browse six working research programs, {expected['results']} result "
        f"collections, {expected['open_problems']} open-problem collections, "
        f"{expected['technical_records']} tagged claims, and seven dated "
        "manuscripts."
    )
    if home_summary not in home_text:
        failures.append("homepage summary counts disagree with site state")
    home_update = (
        f"sanitized {expected['technical_records']}-claim public graph, "
        f"organizes it into {expected['grouped_pages']} grouped packages and "
        f"{expected['memberships']} memberships, and publishes version "
        f"{manuscript_version} of the six reader manuscripts and companion "
        "register."
    )
    if home_update not in home_text:
        failures.append("homepage update counts or manuscript version are stale")
    about_text = (DOCS / "about.md").read_text(encoding="utf-8")
    about_summary = (
        f"six working research programs, {expected['results']} result "
        f"collections, and {expected['open_problems']} open-problem collections."
    )
    if about_summary not in about_text:
        failures.append("About-page counts disagree with site state")
    if re.search(r"canonical registry version \d+", about_text):
        failures.append("About page hard-codes a supersedable registry version")

    materials = json.loads(
        (
            ROOT
            / "data"
            / TECHNICAL_MATERIALS_DATA_DIR
            / "manifest.json"
        ).read_text()
    )
    if materials["artifact_count"] != SITE_STATE["technical_materials"]["expected_count"]:
        failures.append("technical material count changed")
    materials_text = (DOCS / "evidence/materials.md").read_text(encoding="utf-8")
    for program in materials["programs"]:
        for item in program["artifacts"]:
            path = DOCS / "assets/technical-materials" / item["filename"]
            if not path.is_file() or _sha(path) != item["sha256"]:
                failures.append(f"technical material mismatch: {item['filename']}")
            if item["filename"] not in materials_text:
                failures.append(f"technical materials page omits {item['filename']}")

    mkdocs = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    if f"docs_dir: {PUBLIC_DOCS_DIR}" not in mkdocs:
        failures.append("mkdocs.yml selects the wrong docs tree")
    for label in REQUIRED_NAV:
        if not re.search(rf"^\s*-\s+{re.escape(label)}\s*:", mkdocs, re.MULTILINE):
            failures.append(f"mkdocs.yml is missing {label!r}")
    expected_date = (
        datetime.fromisoformat(SITE_STATE["updated_at"])
        .strftime("%d %B %Y")
        .lstrip("0")
        + ", Pacific time"
    )
    if expected_date not in mkdocs:
        failures.append("mkdocs.yml lacks the release date")
    override = (ROOT / "overrides/main.html").read_text(encoding="utf-8")
    if '<meta name="robots" content="noindex, nofollow">' not in override:
        failures.append("global noindex is missing")
    css = (DOCS / "assets/stylesheets/extra.css").read_text(encoding="utf-8")
    for marker in (
        '[data-md-color-scheme="jacobian-dark"]',
        ":focus-visible",
        "@media (prefers-reduced-motion: reduce)",
        "@media screen and (max-width: 620px)",
        ".claim-tag",
        ".metric-grid",
    ):
        if marker not in css:
            failures.append(f"stylesheet lacks {marker!r}")

    if failures:
        print("Graph-native public-site checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(
        f"Graph-native checks passed: {len(claims)} claims, "
        f"{len(collections)} collections, {len(program_files)} programs, "
        f"{scanned} text files scanned."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
