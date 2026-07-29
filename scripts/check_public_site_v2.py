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
    MANUSCRIPTS_DATA_DIR,
    MODEL_BRIEFS_DATA_DIR,
    PUBLICATION_DATA_DIR,
    PUBLIC_DOCS_DIR,
    SITE_STATE,
    TECHNICAL_MATERIALS_DATA_DIR,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / PUBLIC_DOCS_DIR
GRAPH_DATA = ROOT / "data" / CLAIM_GRAPH_DATA_DIR
PUBLICATION_DATA = ROOT / "data" / PUBLICATION_DATA_DIR
MODEL_BRIEF_DATA = ROOT / "data" / MODEL_BRIEFS_DATA_DIR
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".css", ".js", ".txt"}
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
    "### Coverage rule",
    "### Compact glossary",
    "### Case and dependency map",
    "Proof signature",
    "Boundary exit",
)
HANDOFF_PROOF_LINK = re.compile(
    r"(?P<path>\.\./\.\./assets/(?:manuscripts|proof-archives)/"
    r"[^)\s]+\.pdf)#page=(?P<page>\d+)"
)
HANDOFF_STATUS_BUREAUCRACY = (
    "review status",
    "audit status",
    "last audited",
    "independent review",
    "independent specialist review",
)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _sensitive(text: str, label: str, failures: list[str]) -> None:
    lowered = text.casefold()
    for value in FORBIDDEN:
        if value.casefold() in lowered:
            failures.append(f"{label}: forbidden publication marker {value!r}")
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(text):
            failures.append(f"{label}: forbidden UUID")


def _local_links(path: Path, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    targets += re.findall(r'href="([^"]+)"', text)
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
    for path in claim_files:
        text = path.read_text(encoding="utf-8")
        if path.stem not in claims:
            failures.append(f"{path.relative_to(ROOT)}: unknown public tag")
        for heading in ("## Exact statement", "## Appears in", "## Proof access and evidence boundary"):
            if heading not in text:
                failures.append(f"{path.relative_to(ROOT)}: missing {heading}")
        _local_links(path, failures)
    for path in collection_files:
        text = path.read_text(encoding="utf-8")
        if path.stem not in collections:
            failures.append(f"{path.relative_to(ROOT)}: unknown collection")
        for heading in ("## Precise statement", "## Claims in this result package", "## Evidence and manuscript boundary"):
            if heading not in text:
                failures.append(f"{path.relative_to(ROOT)}: missing {heading}")
        _local_links(path, failures)

    for path in DOCS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for phrase in TEMPLATE_PHRASES:
            if phrase in text:
                failures.append(f"{path.relative_to(ROOT)}: legacy template prose remains")
        _local_links(path, failures)

    brief_manifest = json.loads(
        (MODEL_BRIEF_DATA / "manifest.json").read_text(encoding="utf-8")
    )
    if brief_manifest["brief_count"] != SITE_STATE["model_briefs"]["expected_count"]:
        failures.append("model brief count changed")
    if brief_manifest["brief_count"] != len(brief_manifest["briefs"]):
        failures.append("model brief manifest count mismatch")
    brief_routes: set[str] = set()
    for brief in brief_manifest["briefs"]:
        source = MODEL_BRIEF_DATA / brief["source"]
        rendered = DOCS / brief["route"]
        if not source.is_file() or _sha(source) != brief["sha256"]:
            failures.append(f"model brief source mismatch: {brief['source']}")
            continue
        source_text = source.read_text(encoding="utf-8")
        for marker in HANDOFF_STRUCTURE:
            if marker.casefold() not in source_text.casefold():
                failures.append(
                    f"{brief['source']}: missing handoff semantic marker {marker!r}"
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
        if brief.get("kind") == "cross_program":
            if source_text.count("#3-reusable-inputs-exact-scope-and-proof-access") < 6:
                failures.append(
                    f"{brief['source']}: cross-program proof routes do not "
                    "reach all six handoffs"
                )
        else:
            proof_links = list(HANDOFF_PROOF_LINK.finditer(source_text))
            if len(proof_links) < 8:
                failures.append(
                    f"{brief['source']}: too few direct page-level proof links"
                )
            for match in proof_links:
                proof_pdf = (rendered.parent / match.group("path")).resolve()
                page = int(match.group("page"))
                if not proof_pdf.is_file():
                    failures.append(
                        f"{brief['source']}: missing direct proof PDF "
                        f"{match.group('path')!r}"
                    )
                    continue
                pages = len(PdfReader(proof_pdf).pages)
                if page < 1 or page > pages:
                    failures.append(
                        f"{brief['source']}: proof page {page} is outside "
                        f"the {pages}-page PDF {proof_pdf.name}"
                    )
        if len(source.read_bytes()) != brief["bytes"]:
            failures.append(f"model brief byte count mismatch: {brief['source']}")
        if len(source_text.split()) != brief["words"]:
            failures.append(f"model brief word count mismatch: {brief['source']}")
        if brief["route"] in brief_routes:
            failures.append(f"duplicate model brief route: {brief['route']}")
        brief_routes.add(brief["route"])
        lower, upper = ((1500, 2500) if brief.get("kind") == "cross_program" else (2000, 4000))
        if not lower <= brief["words"] <= upper:
            failures.append(
                f"model brief word count outside {lower}-{upper}: {brief['source']}"
            )
        if not rendered.is_file():
            failures.append(f"missing rendered model brief: {brief['route']}")
            continue
        rendered_text = rendered.read_text(encoding="utf-8")
        for heading in (
            "## 1. Setup and notation",
            "## 2. Goal and payoff",
            "## 4. The live frontier",
            "## 5. Graveyard",
            "## 6. Tasks",
            "## 7. Evidence and replay index",
            "## 8. Do not do",
        ):
            if heading not in rendered_text:
                failures.append(f"{brief['route']}: missing {heading}")
        section_three = (
            "## 3. Reusable anchors and proof routes"
            if brief.get("kind") == "cross_program"
            else "## 3. Reusable inputs, exact scope, and proof access"
        )
        if section_three not in rendered_text:
            failures.append(f"{brief['route']}: missing {section_three}")
        if brief["program_slug"] == "minimum-degree-and-quartic-exclusions":
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
        if brief["program_slug"] == "plane-boundary-obstructions":
            if "JCG-9D0BE662" in source_text and (
                "Open dependency—not an accepted result" not in source_text
            ):
                failures.append(
                    f"{brief['source']}: open lower-bound dependency is not "
                    "distinguished from accepted inputs"
                )
        if brief.get("kind") == "cross_program":
            index_page = DOCS / "research/index.md"
            if brief["route"].split("/")[-1] not in index_page.read_text(encoding="utf-8"):
                failures.append("research index does not link cross-program brief")
        else:
            program_page = DOCS / "research/programs" / f"{brief['program_slug']}.md"
            if brief["route"].split("/")[-1] not in program_page.read_text(encoding="utf-8"):
                failures.append(f"program page does not link model brief: {brief['program_slug']}")

    scan_roots = (
        DOCS,
        GRAPH_DATA,
        PUBLICATION_DATA,
        MODEL_BRIEF_DATA,
        ROOT / "overrides",
    )
    scanned = 0
    for scan_root in scan_roots:
        for path in scan_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            scanned += 1
            _sensitive(path.read_text(encoding="utf-8"), str(path.relative_to(ROOT)), failures)

    manuscript_manifest = json.loads(
        (ROOT / "data" / MANUSCRIPTS_DATA_DIR / "manifest.json").read_text()
    )
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
