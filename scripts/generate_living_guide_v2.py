#!/usr/bin/env python3
"""Render the Living Guide from the stable-tag claim graph."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from retained_math_v2_public import (
    FORWARD_RELATIONS,
    compatibility_by_id,
    validate_legacy_compatibility,
    validate_public_v2_graph,
)
from site_state import load_site_state


ROOT = Path(__file__).resolve().parents[1]
SITE_STATE = load_site_state(ROOT)
PUBLIC_DOCS_DIR = SITE_STATE["docs_dir"]
CLAIM_GRAPH_DATA_DIR = SITE_STATE["claim_graph"]["data_dir"]
PUBLICATION_DATA_DIR = SITE_STATE["publication"]["data_dir"]
MANUSCRIPTS_DATA_DIR = SITE_STATE["manuscripts"]["data_dir"]
TECHNICAL_MATERIALS_DATA_DIR = SITE_STATE["technical_materials"]["data_dir"]
MODEL_BRIEFS_DATA_DIR = SITE_STATE["model_briefs"]["data_dir"]
RETAINED_MATH_DATA_DIR = (
    SITE_STATE.get("retained_math", {}).get("data_dir")
)
MANUSCRIPT_SOURCES_DATA_DIR = (
    SITE_STATE.get("manuscript_sources", {}).get("data_dir")
)

MANUSCRIPT_TOKEN_RE = re.compile(r"\{\{MANUSCRIPT_(?P<sequence>[0-9]{2})\}\}")
LITERAL_MANUSCRIPT_LINK_RE = re.compile(
    r"assets/manuscripts/(?P<filename>[^)\s]+\.pdf)"
)
RETAINED_MATH_V2_MARKER_RE = re.compile(
    r"<!-- retained-math-v2-selection:(?P<argument_id>[A-Z0-9-]+) -->"
)

NEW_COLLECTIONS = (
    "cubic-resolvent-defect-exclusions",
    "quartic-target-span-two-ramification-filtration",
    "triple-ramification-and-fixed-component-endgame",
    "marked-root-source-flow-reconstruction",
    "categorical-cubic-frame-quotient",
    "full-kernel-regular-pencil-geometry",
    "nineteen-to-eighteen-compression-obstructions",
    "stored-degree-twenty-one-terminal-no-gluing",
)


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_retained_math(root: Path) -> tuple[dict[str, Any], dict[str, Any]] | None:
    state = load_site_state(root)
    component = state.get("retained_math")
    if component is None:
        return None
    data = root / "data" / component["data_dir"]
    manifest = _load(data / "manifest.json")
    graph = _load(data / "public-graph.json")
    if manifest.get("source_registry_id") != graph.get("registry_id"):
        raise ValueError("retained-math manifest and public graph disagree")
    if manifest.get("counts") != graph.get("counts"):
        raise ValueError("retained-math manifest and public counts disagree")
    files = manifest.get("files", [])
    if manifest.get("file_count") != len(files):
        raise ValueError("retained-math manifest file count disagrees")
    for item in files:
        path = data / item["path"]
        if not path.is_file():
            raise ValueError(f"missing retained-math source: {item['path']}")
        payload = path.read_bytes()
        if len(payload) != item["size_bytes"]:
            raise ValueError(f"retained-math byte count mismatch: {item['path']}")
        if hashlib.sha256(payload).hexdigest() != item["sha256"]:
            raise ValueError(f"retained-math digest mismatch: {item['path']}")
    return manifest, graph


def load_retained_math_v2(
    root: Path,
) -> tuple[dict[str, Any], dict[str, Any]] | None:
    state = load_site_state(root)
    component = state.get("retained_math_v2")
    if component is None:
        return None
    data = root / "data" / component["data_dir"]
    manifest = _load(data / "manifest.json")
    if manifest.get("kind") == "retained-math-v2-full-public":
        graph_path = data / "public-graph.json"
        compatibility_path = data / "legacy-compatibility.json"
        graph = _load(graph_path)
        compatibility = _load(compatibility_path)
        pinned = {item["path"]: item for item in manifest.get("files", [])}
        if set(pinned) != {"public-graph.json", "legacy-compatibility.json"}:
            raise ValueError(
                "full retained-math v2 manifest must pin graph and compatibility map"
            )
        for path in (graph_path, compatibility_path):
            item = pinned[path.name]
            payload = path.read_bytes()
            if len(payload) != item["size_bytes"]:
                raise ValueError(f"retained-math v2 byte count mismatch: {path.name}")
            if hashlib.sha256(payload).hexdigest() != item["sha256"]:
                raise ValueError(f"retained-math v2 digest mismatch: {path.name}")
        graph_counts = validate_public_v2_graph(graph)
        state = load_site_state(root)
        claim_graph = _load(
            root
            / "data"
            / state["claim_graph"]["data_dir"]
            / "claim-graph.json"
        )
        legacy_ids = {item["tag"] for item in claim_graph["claims"]}
        compatibility_counts = validate_legacy_compatibility(
            compatibility,
            graph=graph,
            expected_legacy_ids=legacy_ids,
            schema_path=root / "schemas/legacy-compatibility-v1.schema.json",
        )
        if manifest.get("source_registry_id") != graph.get("registry_id"):
            raise ValueError("retained-math v2 source registry disagrees")
        if manifest.get("compatibility_map_id") != compatibility.get("map_id"):
            raise ValueError("retained-math v2 compatibility identity disagrees")
        if manifest.get("graph_counts") != graph_counts:
            raise ValueError("retained-math v2 graph counts disagree")
        if manifest.get("compatibility_counts") != compatibility_counts:
            raise ValueError("retained-math v2 compatibility counts disagree")
        return manifest, {
            "format": "full",
            "graph": graph,
            "compatibility": compatibility,
        }
    selection = _load(data / "selection.json")
    if manifest.get("selection_id") != selection.get("selection_id"):
        raise ValueError("retained-math v2 manifest and selection disagree")
    if manifest.get("source_registry_id") != selection.get("source", {}).get(
        "registry_id"
    ):
        raise ValueError("retained-math v2 source registry disagrees")
    if manifest.get("counts") != selection.get("counts"):
        raise ValueError("retained-math v2 manifest and counts disagree")
    files = manifest.get("files", [])
    if len(files) != 1 or files[0].get("path") != "selection.json":
        raise ValueError("retained-math v2 must pin exactly selection.json")
    for item in files:
        path = data / item["path"]
        payload = path.read_bytes()
        if len(payload) != item["size_bytes"]:
            raise ValueError(f"retained-math v2 byte count mismatch: {item['path']}")
        if hashlib.sha256(payload).hexdigest() != item["sha256"]:
            raise ValueError(f"retained-math v2 digest mismatch: {item['path']}")
    expected = {
        key.removeprefix("expected_"): value
        for key, value in component.items()
        if key.startswith("expected_")
    }
    if selection["counts"] != expected:
        raise ValueError("retained-math v2 counts disagree with site state")
    selected_ids = selection["selected_ids"]
    for plural, key in (
        ("units", "unit_id"),
        ("arguments", "argument_id"),
        ("evidence", "evidence_id"),
        ("obligations", "obligation_id"),
        ("tasks", "task_id"),
    ):
        found = [item[key] for item in selection[plural]]
        if found != selected_ids[plural] or len(found) != len(set(found)):
            raise ValueError(f"retained-math v2 {plural} selection disagrees")
    retained = load_retained_math(root)
    if retained is None:
        raise ValueError("retained-math v2 requires the v1 working graph")
    if selection["source"]["base_registry"]["registry_id"] != retained[1][
        "registry_id"
    ]:
        raise ValueError("retained-math v2 and v1 registries disagree")
    return manifest, selection


def retained_v2_is_full(payload: dict[str, Any]) -> bool:
    return payload.get("format") == "full"


def retained_v2_graph(payload: dict[str, Any]) -> dict[str, Any]:
    """Return the renderable object arrays from either public package format."""
    return payload["graph"] if retained_v2_is_full(payload) else payload


def retained_v2_compatibility(
    payload: dict[str, Any],
) -> dict[str, Any] | None:
    if not retained_v2_is_full(payload):
        return None
    return payload["compatibility"]


def load_manuscript_sources(root: Path) -> dict[str, Any] | None:
    state = load_site_state(root)
    component = state.get("manuscript_sources")
    if component is None:
        return None
    data = root / "data" / component["data_dir"]
    manifest = _load(data / "manifest.json")
    files = manifest.get("files", [])
    if manifest["counts"]["files"] != len(files):
        raise ValueError("manuscript-source file count disagrees")
    if manifest["counts"]["labels"] != len(manifest.get("labels", [])):
        raise ValueError("manuscript-source label count disagrees")
    if len(files) != component["expected_files"]:
        raise ValueError("manuscript-source file count disagrees with site state")
    if len(manifest["labels"]) != component["expected_labels"]:
        raise ValueError("manuscript-source label count disagrees with site state")
    indexed_labels = []
    for item in files:
        path = data / "sources" / item["path"]
        payload = path.read_bytes()
        if len(payload) != item["size_bytes"]:
            raise ValueError(f"manuscript-source byte count mismatch: {item['path']}")
        if hashlib.sha256(payload).hexdigest() != item["sha256"]:
            raise ValueError(f"manuscript-source digest mismatch: {item['path']}")
        indexed_labels.extend(item["labels"])
    def label_key(item: dict[str, Any]) -> tuple[str, int, str]:
        return item["path"], item["line"], item["label"]

    if sorted(indexed_labels, key=label_key) != sorted(
        manifest["labels"], key=label_key
    ):
        raise ValueError("manuscript-source file labels disagree with global index")
    return manifest


def proof_source_route(path: str) -> Path:
    return Path("research/proof-sources") / Path(path).with_suffix(".md")


def _proof_entrypoint(
    manifest: dict[str, Any], program_sequence: int
) -> dict[str, Any]:
    entry_id = f"program-{program_sequence}"
    return next(
        item for item in manifest["entrypoints"] if item["entrypoint_id"] == entry_id
    )


def render_proof_source_page(item: dict[str, Any], source: str) -> str:
    relative = item["path"]
    language = {
        ".bib": "bibtex",
        ".py": "python",
    }.get(Path(relative).suffix, "tex")
    back = "../" * len(Path(relative).parent.parts) + "index.md"
    lines = [
        "---",
        f"title: {_yaml('Text proof source — ' + relative)}",
            f"description: {_yaml('Sanitized current source with exact labels when present.')}",
        "---",
        "",
        "# Text proof source",
        "",
        f"`manuscripts/{relative}`",
        "",
        "This is the current sanitized source text used by the retained working "
        "graph. TeX comments and private locators are omitted; mathematical "
        "content and line numbering are preserved. PDFs are optional reading "
        "copies.",
        "",
        f"Published SHA-256: `{item['sha256']}` · {item['size_bytes']:,} bytes",
        "",
    ]
    if item["labels"]:
        lines.extend(["## Exact label anchors", ""])
        for label in item["labels"]:
            lines.extend(
                [
                    f'<a id="{label["anchor"]}"></a>',
                    f"- `{label['label']}` — source line {label['line']}",
                ]
            )
        lines.append("")
    lines.extend(
        [
            "## Complete source",
            "",
            f"~~~{language}",
            source.rstrip(),
            "~~~",
            "",
            f"[Back to the text-source index]({back})",
            "",
        ]
    )
    return "\n".join(lines)


def render_proof_source_index(manifest: dict[str, Any]) -> str:
    files = {item["path"]: item for item in manifest["files"]}
    lines = [
        "---",
        'title: "Current text proof sources"',
        'description: "Model-friendly TeX sources for the current retained mathematics."',
        "---",
        "",
        "# Current text proof sources",
        "",
        "Give a research model the relevant program entrypoint below. It can "
        "follow `\\input` links, retained-unit source anchors, and technical "
        "records without downloading a PDF.",
        "",
        f"This pinned release contains **{manifest['counts']['files']} files**, "
        f"**{manifest['counts']['labels']} exact label anchors**, and "
        f"{manifest['counts']['size_bytes']:,} bytes of sanitized TeX/BibTeX.",
        "",
        "## Program entrypoints",
        "",
    ]
    for entry in manifest["entrypoints"]:
        path = entry["path"].removeprefix("manuscripts/")
        item = files[path]
        title = entry["entrypoint_id"].replace("-", " ").title()
        route = proof_source_route(path).relative_to("research/proof-sources")
        lines.append(
            f"- [{title}]({route.as_posix()}) — "
            f"{len(entry['selected_files'])} transitive source files, "
            f"{len(item['labels'])} labels in the entrypoint"
        )
    lines.extend(["", "## All published source files", ""])
    for item in manifest["files"]:
        route = proof_source_route(item["path"]).relative_to(
            "research/proof-sources"
        )
        lines.append(
            f"- [`{item['path']}`]({route.as_posix()}) — "
            f"{len(item['labels'])} labels · {item['size_bytes']:,} bytes"
        )
    lines.append("")
    return "\n".join(lines)


def retained_corrections(
    retained: tuple[dict[str, Any], dict[str, Any]] | None,
) -> dict[str, dict[str, Any]]:
    """Map legacy claim tags to the strongest current forward relation."""
    if retained is None:
        return {}
    _, graph = retained
    corrections: dict[str, dict[str, Any]] = {}
    relation_priority = {"strengthens": 1, "supersedes": 2, "corrects": 3}
    for unit in graph["units"]:
        for relation in unit.get("relations", []):
            target = relation.get("target_unit_id", "")
            relation_type = relation.get("relation_type")
            if relation_type not in relation_priority or not target.startswith("JCG-"):
                continue
            candidate = {**unit, "_forward_relation": relation_type}
            existing = corrections.get(target)
            if existing is not None and existing["unit_id"] != unit["unit_id"]:
                raise ValueError(
                    f"legacy claim has multiple current forward units: {target}"
                )
            if existing is None or relation_priority[relation_type] > relation_priority[
                existing["_forward_relation"]
            ]:
                corrections[target] = candidate
    return corrections


def _yaml(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _human(value: str) -> str:
    return value.replace("_", " ").strip()


def _status_label(value: str) -> str:
    return {
        "proof offered": "Proof supplied",
        "certificate offered": "Certificate supplied",
        "open": "Open",
        "recorded": "Recorded",
    }.get(value, value.title())


def _coverage_label(value: str) -> str:
    return {
        "complete": "Exact manuscript location",
        "partial": "Partial manuscript locator",
        "manuscript_attached": "Manuscript attached",
        "not_applicable": "No program manuscript claimed",
        "not_in_manuscript": "Not in program manuscript",
        "locator_audit_needed": "No exact manuscript locator supplied",
    }.get(value, _human(value).title())


def _source_lines(sources: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    seen: set[str] = set()
    for source in sources:
        url = source.get("url")
        citation = source.get("citation")
        key = url or citation or source.get("title", "")
        if not key or key in seen:
            continue
        seen.add(key)
        title = source.get("title", "Public source")
        authors = source.get("authors", [])
        if authors:
            title += " — " + ", ".join(authors)
        if url:
            lines.append(f"- [{title}]({url})")
        elif citation:
            lines.append(f"- {title}: {citation}")
    return lines


def _credit_lines(credits: list[dict[str, Any]]) -> list[str]:
    lines = []
    for credit in credits:
        roles = ", ".join(_human(role) for role in credit.get("roles", []))
        basis = _human(
            credit.get("attribution_basis", credit.get("basis", "recorded"))
        )
        scope = f" — {credit['scope']}" if credit.get("scope") else ""
        lines.append(f"- {credit['name']}: {roles}; {basis}{scope}")
    return lines


def load(root: Path) -> tuple[
    dict[str, Any],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, Any],
    dict[str, dict[str, Any]],
]:
    state = load_site_state(root)
    graph = _load(
        root / "data" / state["claim_graph"]["data_dir"] / "claim-graph.json"
    )
    claims = {item["tag"]: item for item in graph["claims"]}
    collections = {item["slug"]: item for item in graph["collections"]}
    programs = {item["slug"]: item for item in graph["programs"]}
    manuscript_manifest = _load(
        root / "data" / state["manuscripts"]["data_dir"] / "manifest.json"
    )
    manuscripts = {
        item["filename"][:2]: item for item in manuscript_manifest["manuscripts"]
    }
    materials = _load(
        root
        / "data"
        / state["technical_materials"]["data_dir"]
        / "manifest.json"
    )
    brief_manifest = _load(
        root / "data" / state["model_briefs"]["data_dir"] / "manifest.json"
    )
    source_manifest = load_manuscript_sources(root)
    if source_manifest is None:
        raise ValueError("selected release does not pin manuscript sources")
    if brief_manifest["brief_count"] != len(brief_manifest["briefs"]):
        raise ValueError("model brief manifest count mismatch")
    briefs = {item["program_slug"]: item for item in brief_manifest["briefs"]}
    if len(briefs) != state["model_briefs"]["expected_count"]:
        raise ValueError("model brief count disagrees with site-state.json")
    for brief in briefs.values():
        source = root / "data" / state["model_briefs"]["data_dir"] / brief["source"]
        if not source.is_file():
            raise ValueError(f"missing model brief source: {source}")
        payload = source.read_bytes()
        if len(payload) != brief["bytes"]:
            raise ValueError(f"model brief byte count mismatch: {source}")
        if hashlib.sha256(payload).hexdigest() != brief["sha256"]:
            raise ValueError(f"model brief digest mismatch: {source}")
    task_inputs = brief_manifest.get("task_inputs", [])
    if brief_manifest.get("task_input_count", 0) != len(task_inputs):
        raise ValueError("model brief task-input count mismatch")
    brief_routes = {item["route"] for item in brief_manifest["briefs"]}
    for item in task_inputs:
        source = root / "data" / state["model_briefs"]["data_dir"] / item["source"]
        if not source.is_file():
            raise ValueError(f"missing model task input: {source}")
        payload = source.read_bytes()
        if len(payload) != item["bytes"]:
            raise ValueError(f"model task-input byte count mismatch: {source}")
        if hashlib.sha256(payload).hexdigest() != item["sha256"]:
            raise ValueError(f"model task-input digest mismatch: {source}")
        if item["route"] in brief_routes:
            raise ValueError(f"model task-input route collides with brief: {item['route']}")
    task_roadmap = brief_manifest.get("task_roadmap")
    if not isinstance(task_roadmap, dict):
        raise ValueError("model handoff package does not define a task roadmap")
    roadmap_source = (
        root
        / "data"
        / state["model_briefs"]["data_dir"]
        / task_roadmap["source"]
    )
    if not roadmap_source.is_file():
        raise ValueError(f"missing research-task roadmap: {roadmap_source}")
    roadmap_payload = roadmap_source.read_bytes()
    if (
        len(roadmap_payload) != task_roadmap["bytes"]
        or hashlib.sha256(roadmap_payload).hexdigest()
        != task_roadmap["sha256"]
    ):
        raise ValueError("research-task roadmap differs from its manifest")
    if task_roadmap["route"] in brief_routes or task_roadmap["route"] in {
        item["route"] for item in task_inputs
    }:
        raise ValueError("research-task roadmap route collides with handoff data")
    expected = state["expected_counts"]
    if graph["counts"] != {
        "claims": expected["technical_records"],
        "collections": expected["grouped_pages"],
        "programs": expected["research_programs"],
        "memberships": expected["memberships"],
    }:
        raise ValueError("claim graph counts disagree with site-state.json")
    if len(claims) != len(graph["claims"]):
        raise ValueError("duplicate public claim tag")
    return graph, claims, collections, programs, manuscripts, materials, briefs


def source_packet_routes(brief_manifest: dict[str, Any]) -> dict[str, str]:
    """Map canonical repository locators to their public source packet."""
    routes: dict[str, str] = {}
    for task_input in brief_manifest.get("task_inputs", []):
        packet = task_input.get("source_packet")
        if not isinstance(packet, dict):
            continue
        route = Path(task_input["route"])
        public_route = f"../../handoffs/{route.name}"
        for item in packet.get("files", []):
            raw = item.get("repo_path") or item.get("path")
            if not isinstance(raw, str) or not raw:
                continue
            candidates = {raw}
            if not raw.startswith(
                (
                    "manuscripts/",
                    "papers-release-",
                    "research-notes/",
                    "research-tools/",
                )
            ):
                candidates.add(f"research-notes/{raw}")
            for candidate in candidates:
                # A shared source can support more than one lane. The manifest
                # order supplies one stable public locator; every copy is
                # hash-pinned to the same repository payload.
                routes.setdefault(candidate, public_route)
    return routes


def task_input_is_binary(item: dict[str, Any]) -> bool:
    """Return whether a task input is copied byte-for-byte instead of rendered."""
    media_type = item.get("media_type")
    return isinstance(media_type, str) and not media_type.startswith("text/")


def resolve_manuscript_links(
    source: str, manuscripts: dict[str, dict[str, Any]]
) -> str:
    literal = LITERAL_MANUSCRIPT_LINK_RE.search(source)
    if literal:
        raise ValueError(
            "model brief source must use a logical manuscript token, not "
            f"{literal.group('filename')}"
        )

    def replace(match: re.Match[str]) -> str:
        sequence = match.group("sequence")
        if sequence not in manuscripts:
            raise ValueError(f"unknown model-brief manuscript token: {sequence}")
        return manuscripts[sequence]["filename"]

    rendered = MANUSCRIPT_TOKEN_RE.sub(replace, source)
    if "{{MANUSCRIPT_" in rendered:
        raise ValueError("malformed model-brief manuscript token")
    return rendered


def _version_label(release_id: str) -> str:
    match = re.search(r"-v(?P<version>[0-9]+[a-z]?)-", release_id)
    if not match:
        raise ValueError(f"release ID has no version label: {release_id}")
    return f"v{match.group('version')}"


def build_release_metadata(root: Path) -> dict[str, Any]:
    state = load_site_state(root)
    manuscript_manifest = _load(
        root / "data" / state["manuscripts"]["data_dir"] / "manifest.json"
    )
    brief_manifest = _load(
        root / "data" / state["model_briefs"]["data_dir"] / "manifest.json"
    )
    source_manifest = load_manuscript_sources(root)
    if source_manifest is None:
        raise ValueError("selected release does not pin manuscript sources")
    versions = {item["version"] for item in manuscript_manifest["manuscripts"]}
    if len(versions) != 1:
        raise ValueError("selected manuscripts do not share one release version")
    manuscripts = []
    for item in manuscript_manifest["manuscripts"]:
        manuscripts.append(
            {
                "sequence": item["filename"][:2],
                "title": item["title"],
                "filename": item["filename"],
                "version": item["version"],
                "pages": item["pages"],
                "sha256": item["sha256"],
            }
        )
    handoffs = []
    for item in sorted(
        brief_manifest["briefs"],
        key=lambda brief: brief.get(
            "display_sequence", brief["program_sequence"]
        ),
    ):
        handoffs.append(
            {
                "kind": item["kind"],
                "program_sequence": item["program_sequence"],
                "program_slug": item["program_slug"],
                "title": item["title"],
                "route": item["route"].removesuffix(".md") + "/",
                "source_sha256": item["sha256"],
                "source_words": item["words"],
                "primary_entrypoint": item.get("primary_entrypoint", False),
                "related_programs": item.get("related_programs", []),
                "lane_sequence": item.get("lane_sequence"),
            }
        )
    release = {
        "schema_version": 1,
        "site_release_id": state["release_id"],
        "updated_at": state["updated_at"],
        "timezone": state["timezone"],
        "components": {
            "claim_graph_manifest_sha256": state["claim_graph"]["manifest_sha256"],
            "manuscript_manifest_sha256": state["manuscripts"]["manifest_sha256"],
            "model_brief_manifest_sha256": state["model_briefs"]["manifest_sha256"],
            "manuscript_source_manifest_sha256": state["manuscript_sources"]["manifest_sha256"],
        },
        "counts": state["expected_counts"],
        "manuscript_version": next(iter(versions)),
        "manuscripts": manuscripts,
        "handoff_source": {
            "release_id": brief_manifest["release_id"],
            "version": _version_label(brief_manifest["release_id"]),
            "count": brief_manifest["brief_count"],
            "task_input_count": brief_manifest.get("task_input_count", 0),
            "task_inputs": [
                {
                    "input_id": item["input_id"],
                    "route": (
                        item["route"]
                        if task_input_is_binary(item)
                        else item["route"].removesuffix(".md") + "/"
                    ),
                    "source_sha256": item["sha256"],
                }
                for item in brief_manifest.get("task_inputs", [])
            ],
            "task_roadmap": {
                "route": brief_manifest["task_roadmap"]["route"].removesuffix(
                    ".md"
                )
                + "/",
                "source_sha256": brief_manifest["task_roadmap"]["sha256"],
            },
        },
        "handoffs": handoffs,
        "manuscript_sources": {
            "release_id": source_manifest["release_id"],
            "source_repository_commit": source_manifest["source_repository_commit"],
            "counts": source_manifest["counts"],
            "index_route": "research/proof-sources/",
        },
    }
    retained = load_retained_math(root)
    if retained is not None:
        manifest, graph = retained
        release["retained_math"] = {
            "release_id": manifest["release_id"],
            "registry_id": graph["registry_id"],
            "counts": graph["counts"],
        }
    retained_v2 = load_retained_math_v2(root)
    if retained_v2 is not None:
        manifest, payload = retained_v2
        release["components"]["retained_math_v2_manifest_sha256"] = state[
            "retained_math_v2"
        ]["manifest_sha256"]
        if retained_v2_is_full(payload):
            graph = retained_v2_graph(payload)
            compatibility = retained_v2_compatibility(payload)
            assert compatibility is not None
            release["retained_math_v2"] = {
                "release_id": manifest["release_id"],
                "source_registry_id": manifest["source_registry_id"],
                "counts": graph["counts"],
                "compatibility_map_id": compatibility["map_id"],
                "compatibility_counts": compatibility["counts"],
                "machine_routes": {
                    "graph": "research/working-mathematics/graph.json",
                    "legacy_compatibility": (
                        "research/working-mathematics/legacy-compatibility.json"
                    ),
                },
            }
        else:
            release["retained_math_v2"] = {
                "release_id": manifest["release_id"],
                "source_registry_id": manifest["source_registry_id"],
                "selection_id": payload["selection_id"],
                "selected_ids": payload["selected_ids"],
                "counts": payload["counts"],
                "machine_route": "research/handoffs/retained-math-v2-pilot.json",
            }
    return release


def _bullet_lines(items: list[str]) -> list[str]:
    return [f"- {item}" for item in items]


def _retained_v2_locator(evidence: dict[str, Any]) -> str | None:
    locator = evidence.get("locator")
    if not locator:
        return None
    if locator.get("kind") == "external":
        return f"[Pinned source]({locator['url']})"
    if locator.get("kind") == "repo":
        anchor = f"#{locator['anchor']}" if locator.get("anchor") else ""
        return f"`{locator['repo_path']}{anchor}`"
    raise ValueError(f"unsupported retained-math v2 locator: {locator}")


def render_retained_math_v2_selection(
    argument_id: str, selection: dict[str, Any]
) -> str:
    arguments = {item["argument_id"]: item for item in selection["arguments"]}
    if argument_id not in arguments:
        raise ValueError(f"handoff requests unselected argument: {argument_id}")
    argument = arguments[argument_id]
    if len(argument["conclusion_unit_ids"]) != 1:
        raise ValueError("v2 handoff pilot requires one conclusion unit")
    units = {item["unit_id"]: item for item in selection["units"]}
    evidence = {item["evidence_id"]: item for item in selection["evidence"]}
    unit = units[argument["conclusion_unit_ids"][0]]

    if "selection_id" in selection:
        provenance_lines = [
            "    rendered from one retained-math v2 selection. The",
            "    [machine-readable selection](retained-math-v2-pilot.json) is pinned",
            "    by the handoff release metadata.",
        ]
    else:
        provenance_lines = [
            "    rendered from the complete retained-math v2 graph. The",
            "    [machine-readable graph](../working-mathematics/graph.json) preserves",
            "    its argument, evidence, and relation edges.",
        ]

    lines = [
        "### Compiler-owned retained result",
        "",
        '!!! info "First-class retained mathematics"',
        "    This result, its exact argument, and its evidence boundary are",
        *provenance_lines,
        "",
        f"#### {unit['title']}",
        "",
        f"`{unit['unit_id']}` · `{unit['unit_type']}` · statement version "
        f"`{unit['statement_version']}`",
        "",
        unit["statement"],
        "",
        "**Hypotheses**",
        "",
        *_bullet_lines(unit["hypotheses"]),
        "",
        "**Applies to**",
        "",
        *_bullet_lines(unit["exact_scope"]["applies_to"]),
        "",
        "**Limitations**",
        "",
        *_bullet_lines(unit["exact_scope"]["limitations"]),
        "",
        "#### Exact argument",
        "",
        f"**{argument['title']}** · `{argument['argument_id']}` · "
        f"`{argument['argument_type']}`",
        "",
        argument["summary"],
        "",
        argument["body"],
        "",
        "**This argument does not establish**",
        "",
        *_bullet_lines(argument["does_not_establish"]),
        "",
        "#### Evidence and exact source links",
        "",
    ]
    for evidence_id in argument["evidence_ids"]:
        item = evidence[evidence_id]
        lines.extend(
            [
                f"##### {item['title']}",
                "",
                item["summary"],
                "",
                f"**Establishes:** {item['establishes']}",
                "",
            ]
        )
        locator = _retained_v2_locator(item)
        if locator is not None:
            lines.extend([f"**Locator:** {locator}", ""])
        lines.extend(
            [
                "**Does not establish**",
                "",
                *_bullet_lines(item["does_not_establish"]),
                "",
            ]
        )

    return "\n".join(lines)


def expand_retained_math_v2_markers(
    source: str, selection: dict[str, Any]
) -> str:
    found = RETAINED_MATH_V2_MARKER_RE.findall(source)

    def replace(match: re.Match[str]) -> str:
        return render_retained_math_v2_selection(
            match.group("argument_id"), selection
        )

    rendered = RETAINED_MATH_V2_MARKER_RE.sub(replace, source)
    if "retained-math-v2-selection:" in rendered:
        raise ValueError("malformed retained-math v2 marker")
    if len(found) != len(set(found)):
        raise ValueError("duplicate retained-math v2 marker")
    return rendered


def _compatibility_targets(
    route: dict[str, Any], units: dict[str, dict[str, Any]], role: str
) -> list[dict[str, Any]]:
    return [
        units[target["unit_id"]]
        for target in route["targets"]
        if target["role"] == role
    ]


def _append_before_browse(page: str, lines: list[str]) -> str:
    marker = "\n[Browse all claims](../results/all-claims.md)\n"
    if marker not in page:
        raise ValueError("claim renderer lacks all-claims footer")
    return page.replace(marker, "\n" + "\n".join(lines) + marker, 1)


def _protect_formula_like_markdown(text: str) -> str:
    """Keep bracketed formulas from being parsed as relative Markdown links."""
    pattern = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")

    def replace(match: re.Match[str]) -> str:
        target = match.group(2).strip()
        if (
            "://" in target
            or "/" in target
            or "#" in target
            or target.endswith((".md", ".json", ".pdf", ".zip"))
        ):
            return match.group(0)
        return f"[{match.group(1)}&#93;({match.group(2)})"

    return pattern.sub(replace, text)


def render_compatible_claim(
    claim: dict[str, Any],
    collections: dict[str, dict[str, Any]],
    route: dict[str, Any],
    units: dict[str, dict[str, Any]],
) -> str:
    """Render one stable claim URL according to the total forward map."""
    disposition = route["disposition"]
    if disposition in {"exact_current", "valid_weaker"}:
        current = _compatibility_targets(route, units, "current_statement")[0]
        rendered_claim = {
            **claim,
            "title": current["title"],
            "statement": current["statement"],
            "statement_version": current["statement_version"],
        }
        stronger = _compatibility_targets(route, units, "stronger_result")
        correction = None
        if stronger:
            correction = {**stronger[0], "_forward_relation": "strengthens"}
        page = render_claim(rendered_claim, collections, correction)
        extra = [
            "## Current retained record",
            "",
            f"[Open the full mathematical unit](../research/working-mathematics/units/{current['unit_id']}.md)",
            "",
            "The linked unit carries its first-class arguments, evidence, source locators, and machine-readable relations.",
            "",
        ]
        if len(stronger) > 1:
            extra.extend(["Other stronger current formulations:", ""])
            extra.extend(
                f"- [{unit['title']}](../research/working-mathematics/units/{unit['unit_id']}.md)"
                for unit in stronger[1:]
            )
            extra.append("")
        return _protect_formula_like_markdown(_append_before_browse(page, extra))

    if disposition in {"replacement", "split_replacement"}:
        replacements = _compatibility_targets(route, units, "replacement")
        lines = [
            "---",
            f"title: {_yaml('Replaced claim ' + claim['tag'])}",
            f"description: {_yaml('This stable claim route points to current replacement mathematics.')}",
            "---",
            "",
            f'<p class="claim-tag">{claim["tag"]}</p>',
            "# Replaced claim",
            "",
            '!!! warning "Use the current replacement mathematics"',
            "    This stable URL is preserved for continuity, but its earlier",
            "    statement is superseded and is intentionally not reproduced here.",
            "",
            "## Current replacement" if len(replacements) == 1 else "## Current replacements",
            "",
        ]
        for unit in replacements:
            lines.extend(
                [
                    f"### [{unit['title']}](../research/working-mathematics/units/{unit['unit_id']}.md)",
                    "",
                    f"`{unit['unit_id']}` · statement version `{unit['statement_version']}`",
                    "",
                    unit["statement"],
                    "",
                ]
            )
        lines.extend(
            [
                "## Historical status",
                "",
                "This route records that an earlier public statement existed. It is not part of the current result collections.",
                "",
                "[Browse all claims](../results/all-claims.md)",
                "",
            ]
        )
        return _protect_formula_like_markdown("\n".join(lines))

    if disposition != "archival":
        raise ValueError(f"unknown compatibility disposition: {disposition}")
    return _protect_formula_like_markdown("\n".join(
        [
            "---",
            f"title: {_yaml('Historical claim ' + claim['tag'])}",
            f"description: {_yaml('A preserved historical claim route with no current mathematical target.')}",
            "robots: noindex, nofollow",
            "---",
            "",
            f'<p class="claim-tag">{claim["tag"]}</p>',
            "# Historical claim",
            "",
            '!!! warning "Historical record"',
            "    This stable URL is preserved as publication history. The earlier",
            "    wording is intentionally not reproduced, and the current retained",
            "    graph supplies no forward replacement.",
            "",
            "This record is excluded from current result and open-problem collections.",
            "",
            "[Browse all claims](../results/all-claims.md)",
            "",
        ]
    ))


def render_compatible_collection(
    page: dict[str, Any],
    claims: dict[str, dict[str, Any]],
    collections: dict[str, dict[str, Any]],
    routes: dict[str, dict[str, Any]],
    units: dict[str, dict[str, Any]],
) -> str:
    """Render a current collection without reviving archival mathematics."""
    coverage = page["manuscript_coverage"]["status"]
    has_historical_members = any(
        routes[tag]["disposition"]
        in {"replacement", "split_replacement", "archival"}
        for tag in page["member_tags"]
    )
    visible_description = (
        "This current collection omits historical wording. Replaced records "
        "point to their current retained mathematics."
        if has_historical_members
        else page["description"]
    )
    precise_statement = (
        "Current mathematical statements are listed unit by unit below; "
        "superseded and archival wording is not reproduced."
        if has_historical_members
        else page["statement"]
    )
    lines = [
        "---",
        f"title: {_yaml(page['title'])}",
        f"description: {_yaml(visible_description)}",
        "---",
        "",
        f"# {page['title']}",
        "",
        f'<p class="dek">{visible_description}</p>',
        "",
        f'<span class="status status-kind">{_human(page["kind"]).title()}</span> '
        f'<span class="status coverage-{coverage}">{_coverage_label(coverage)}</span>',
        "",
        "## Precise statement",
        "",
        precise_statement,
        "",
        "## Claims in this result package",
        "",
    ]
    for tag in page["member_tags"]:
        route = routes[tag]
        disposition = route["disposition"]
        if disposition == "archival":
            continue
        claim = claims[tag]
        membership = next(
            item
            for item in claim["memberships"]
            if item["collection_slug"] == page["slug"]
        )
        if disposition in {"replacement", "split_replacement"}:
            replacements = _compatibility_targets(route, units, "replacement")
            lines.extend(
                [
                    f"### [{tag} · Replaced historical record](../claims/{tag}.md)",
                    "",
                    '!!! warning "Replaced working statement"',
                    "    The earlier wording is suppressed. Continue with the current replacement mathematics below.",
                    "",
                ]
            )
            for unit in replacements:
                lines.extend(
                    [
                        f"- [{unit['title']}](../research/working-mathematics/units/{unit['unit_id']}.md): {unit['statement']}",
                        "",
                    ]
                )
        else:
            current = _compatibility_targets(
                route, units, "current_statement"
            )[0]
            lines.extend(
                [
                    f"### [{tag} · {current['title']}](../claims/{tag}.md)",
                    "",
                    current["statement"],
                    "",
                ]
            )
            stronger = _compatibility_targets(route, units, "stronger_result")
            if stronger:
                lines.extend(
                    [
                        '!!! info "Stronger current result available"',
                        "    The statement above remains valid. A stronger current formulation is available:",
                        "",
                        *[
                            f"    - [{unit['title']}](../research/working-mathematics/units/{unit['unit_id']}.md)"
                            for unit in stronger
                        ],
                        "",
                    ]
                )
        lines.extend(
            [
                f"*{_human(membership['inclusion']).title()} · "
                f"{_human(membership['role']).title()} · {_status_label(claim['status'])}*",
                "",
            ]
        )
    lines.extend(
        [
            "## Evidence and manuscript boundary",
            "",
            page["source_treatment"],
            "",
            page["manuscript_coverage"]["coverage_rule"],
            "",
        ]
    )
    if page["source"]:
        lines.extend(["### Public sources", "", *_source_lines(page["source"]), ""])
    if page["credited_to"]:
        lines.extend(
            ["## Credit", "", *_credit_lines(page["credited_to"]), ""]
        )
    connected = sorted(
        set(page["connections"].get("depends_on", []))
        | set(page["connections"].get("shares_claims_with", []))
    )
    if connected:
        lines.extend(["## Connections", ""])
        for slug in connected:
            if slug in collections:
                lines.append(
                    f"- [{collections[slug]['title']}](../collections/{slug}.md)"
                )
        lines.append("")
    lines.extend(["[Back to Results](../results/index.md)", ""])
    return _protect_formula_like_markdown("\n".join(lines))


def render_all_claims_compatible(
    claims: dict[str, dict[str, Any]],
    routes: dict[str, dict[str, Any]],
    units: dict[str, dict[str, Any]],
) -> str:
    lines = [
        "---",
        'title: "All claims"',
        'description: "The complete stable-route claim catalogue."',
        "---",
        "",
        "# All claims",
        "",
        '<p class="dek">Every legacy public claim URL remains resolvable. Current, replaced, and archival dispositions are stated explicitly.</p>',
        "",
        '<div class="claim-list" markdown>',
        "",
    ]
    for tag in sorted(claims):
        route = routes[tag]
        disposition = route["disposition"]
        if disposition in {"exact_current", "valid_weaker"}:
            current = _compatibility_targets(
                route, units, "current_statement"
            )[0]
            title = current["title"]
        elif disposition in {"replacement", "split_replacement"}:
            title = "Replaced historical claim"
        else:
            title = "Historical claim"
        lines.append(
            f"- [`{tag}`](../claims/{tag}.md) **{title}** — "
            f"{_human(disposition)}"
        )
    lines.extend(["", "</div>", ""])
    return _protect_formula_like_markdown("\n".join(lines))


def render_corrections_compatible(
    routes: dict[str, dict[str, Any]], units: dict[str, dict[str, Any]]
) -> str:
    lines = [
        "---",
        'title: "Corrections and scope changes"',
        'description: "Stable routes whose current mathematical disposition points forward."',
        "---",
        "",
        "# Corrections and scope changes",
        "",
        '<p class="dek">Earlier wording is suppressed when it has been corrected or superseded.</p>',
        "",
    ]
    for tag, route in sorted(routes.items()):
        if route["disposition"] not in {
            "valid_weaker",
            "replacement",
            "split_replacement",
        }:
            continue
        lines.extend([f"## [{tag}](../claims/{tag}.md)", ""])
        role = (
            "stronger_result"
            if route["disposition"] == "valid_weaker"
            else "replacement"
        )
        for unit in _compatibility_targets(route, units, role):
            lines.extend(
                [
                    f"- [{unit['title']}](../research/working-mathematics/units/{unit['unit_id']}.md)",
                    "",
                    unit["statement"],
                    "",
                ]
            )
    return _protect_formula_like_markdown("\n".join(lines))


def _published_evidence_locator(
    locator: dict[str, Any] | None,
    proof_sources: dict[str, Any],
    source_packet_routes: dict[str, str] | None = None,
) -> tuple[str | None, str | None]:
    """Return a reader link and optional inline body for a public locator."""
    if locator is None:
        return None, None
    kind = locator.get("kind")
    if kind == "external":
        return f"[Open the pinned source]({locator['url']})", None
    if kind == "inline":
        return "Inline evidence is reproduced below.", locator["body"]
    if kind != "repo":
        return None, None
    source_packet_routes = source_packet_routes or {}
    public_packet = source_packet_routes.get(locator["repo_path"])
    if public_packet is not None:
        return f"[Open the published source]({public_packet})", None
    repo_path = Path(locator["repo_path"])
    parts = repo_path.parts
    if parts and parts[0] == "manuscripts":
        relative = Path(*parts[1:])
    elif parts and parts[0].startswith("papers-release-"):
        relative = Path(*parts[1:])
    else:
        relative = None
    if relative is not None:
        sources = {item["path"]: item for item in proof_sources["files"]}
        item = sources.get(relative.as_posix())
        if item is not None:
            route = proof_source_route(relative.as_posix()).relative_to(
                "research/proof-sources"
            )
            anchor = locator.get("anchor")
            fragment = ""
            if anchor:
                label = next(
                    (
                        value
                        for value in item["labels"]
                        if value["label"] == anchor or value["anchor"] == anchor
                    ),
                    None,
                )
                if label is not None:
                    fragment = f"#{label['anchor']}"
            return (
                f"[Open the published source](../../proof-sources/{route.as_posix()}{fragment})",
                None,
            )
    suffix = f"#{locator['anchor']}" if locator.get("anchor") else ""
    return f"Source path: `{locator['repo_path']}{suffix}`", None


def render_retained_v2_unit(
    unit: dict[str, Any],
    graph: dict[str, Any],
    proof_sources: dict[str, Any],
    source_packet_routes: dict[str, str] | None = None,
) -> str:
    """Render a current unit with math-facing edges and no audit workflow."""
    graph_unit_ids = {item["unit_id"] for item in graph["units"]}
    arguments = {item["argument_id"]: item for item in graph["arguments"]}
    evidence = {item["evidence_id"]: item for item in graph["evidence"]}
    lines = [
        "---",
        f"title: {_yaml(unit['title'])}",
        f"description: {_yaml(unit['statement'])}",
        "---",
        "",
        f"# {unit['title']}",
        "",
        f"`{unit['unit_id']}` · `{unit['unit_type']}` · statement version `{unit['statement_version']}`",
        "",
        "## Exact statement",
        "",
        unit["statement"],
        "",
    ]
    for heading, values in (
        ("Hypotheses", unit["hypotheses"]),
        ("Applies to", unit["exact_scope"]["applies_to"]),
        ("Limitations", unit["exact_scope"]["limitations"]),
    ):
        if values:
            lines.extend([f"## {heading}", "", *_bullet_lines(values), ""])
    selected_arguments = [
        arguments[argument_id] for argument_id in unit.get("argument_ids", [])
    ]
    if selected_arguments:
        lines.extend(["## Arguments", ""])
        for argument in selected_arguments:
            lines.extend(
                [
                    f"### {argument['title']}",
                    "",
                    f"`{argument['argument_id']}` · `{argument['argument_type']}`",
                    "",
                    argument["summary"],
                    "",
                    argument["body"],
                    "",
                ]
            )
            if argument["premise_unit_ids"]:
                lines.extend(
                    [
                        "Premise units:",
                        "",
                        *[
                            (
                                f"- [`{unit_id}`]({unit_id}.md)"
                                if unit_id in graph_unit_ids
                                else f"- `{unit_id}` (external graph reference)"
                            )
                            for unit_id in argument["premise_unit_ids"]
                        ],
                        "",
                    ]
                )
            if argument["depends_on_argument_ids"]:
                lines.extend(
                    [
                        "Argument dependencies:",
                        "",
                        *[
                            f"- `{argument_id}`"
                            for argument_id in argument["depends_on_argument_ids"]
                        ],
                        "",
                    ]
                )
            if argument["does_not_establish"]:
                lines.extend(
                    [
                        "Does not establish:",
                        "",
                        *_bullet_lines(argument["does_not_establish"]),
                        "",
                    ]
                )
    evidence_ids = list(unit.get("evidence_ids", []))
    for argument in selected_arguments:
        evidence_ids.extend(argument["evidence_ids"])
    selected_evidence = [
        evidence[evidence_id]
        for evidence_id in dict.fromkeys(evidence_ids)
        if evidence_id in evidence
    ]
    if selected_evidence:
        lines.extend(["## Evidence and source access", ""])
        for item in selected_evidence:
            lines.extend(
                [
                    f"### {item['title']}",
                    "",
                    f"`{item['evidence_id']}` · `{item['kind']}`",
                    "",
                    item["summary"],
                    "",
                    f"**Establishes:** {item['establishes']}",
                    "",
                ]
            )
            locator, inline = _published_evidence_locator(
                item.get("locator"), proof_sources, source_packet_routes
            )
            if locator:
                lines.extend([f"**Source:** {locator}", ""])
            if inline:
                lines.extend([inline, ""])
            replay = item.get("replay")
            if replay:
                lines.extend(["Replay commands:", ""])
                lines.extend(f"- `{command}`" for command in replay["commands"])
                lines.append("")
            if item["does_not_establish"]:
                lines.extend(
                    [
                        "Does not establish:",
                        "",
                        *_bullet_lines(item["does_not_establish"]),
                        "",
                    ]
                )
    visible_relations = [
        relation
        for relation in unit.get("relations", [])
        if relation.get("relation_type") not in FORWARD_RELATIONS
    ]
    if visible_relations:
        lines.extend(["## Mathematical connections", ""])
        for relation in visible_relations:
            target = relation["target_unit_id"]
            note = f" — {relation['note']}" if relation.get("note") else ""
            target_label = (
                f"[`{target}`]({target}.md)"
                if target in graph_unit_ids
                else f"`{target}` (external graph reference)"
            )
            lines.append(
                f"- `{relation['relation_type']}` {target_label}{note}"
            )
        lines.append("")
    attribution = unit.get("attribution", {})
    if attribution.get("credited_to") or attribution.get("citations"):
        lines.extend(["## Attribution and citations", ""])
        lines.extend(
            f"- Credit: {value}" for value in attribution.get("credited_to", [])
        )
        lines.extend(
            f"- Citation: {value}" for value in attribution.get("citations", [])
        )
        lines.append("")
    lines.extend(
        [
            "[Machine-readable graph](../graph.json)",
            "",
        ]
    )
    return _protect_formula_like_markdown("\n".join(lines))


def render_retained_v2_program(
    program: dict[str, Any], graph: dict[str, Any]
) -> str:
    units = [
        unit
        for unit in graph["units"]
        if program["slug"] in unit["memberships"]["programs"]
    ]
    lines = [
        "---",
        f"title: {_yaml(program['title'])}",
        f"description: {_yaml(program['summary'])}",
        "---",
        "",
        f"# {program['title']}",
        "",
        program["summary"],
        "",
        f"This current view contains **{len(units)} retained units**.",
        "",
    ]
    for unit in sorted(units, key=lambda item: item["title"].casefold()):
        lines.extend(
            [
                f"## [{unit['title']}](../units/{unit['unit_id']}.md)",
                "",
                unit["statement"],
                "",
                f"`{unit['unit_id']}` · `{unit['unit_type']}`",
                "",
            ]
        )
    return _protect_formula_like_markdown("\n".join(lines))


def render_model_brief(
    brief: dict[str, Any],
    source: str,
    manuscripts: dict[str, dict[str, Any]],
    release: dict[str, Any],
    proof_sources: dict[str, Any],
    retained_v2_selection: dict[str, Any],
) -> str:
    source = resolve_manuscript_links(source, manuscripts)
    source = expand_retained_math_v2_markers(source, retained_v2_selection)
    kind = brief.get("kind")
    cross_program = kind == "cross_program"
    lane = kind == "lane"
    if cross_program:
        label = "Model research brief · Portfolio hub"
        back_link = "[Back to the research overview](../index.md)"
    elif lane:
        label = f'Model research brief · Lane {brief["lane_sequence"]}'
        back_link = "[Back to the portfolio hub](state-of-the-program.md)"
    else:
        label = f'Model research brief · Program {brief["program_sequence"]}'
        back_link = (
            f'[Back to the Program {brief["program_sequence"]} overview]'
            f'(../programs/{brief["program_slug"]}.md)'
        )
    retained_target: str | None = None
    if "retained_math" in release:
        retained_target = (
            "../working-mathematics/index.md"
            if cross_program or lane
            else "../working-mathematics/programs/"
            f"{brief['program_slug']}.md"
        )
    if cross_program or lane:
        source_target = "../proof-sources/index.md"
    else:
        entry = _proof_entrypoint(proof_sources, brief["program_sequence"])
        source_path = entry["path"].removeprefix("manuscripts/")
        source_target = "../proof-sources/" + proof_source_route(
            source_path
        ).relative_to("research/proof-sources").as_posix()
    source_lines = source.rstrip().splitlines()
    if source_lines and source_lines[0].startswith("# "):
        title_line = source_lines[0]
        body = "\n".join(source_lines[1:]).lstrip()
    else:
        title_index = next(
            (index for index, line in enumerate(source_lines) if line.startswith("# ")),
            None,
        )
        if title_index is None:
            title_line = f"# {brief['title']}"
            body_lines = source_lines
        else:
            title_line = source_lines[title_index]
            body_lines = source_lines[:title_index] + source_lines[title_index + 1 :]
        body = "\n".join(body_lines).lstrip()
    if cross_program or lane:
        body_lines = body.splitlines()
        if body_lines:
            leading = body_lines[0].strip()
            redundant_identity = (
                lane
                and re.fullmatch(
                    rf"Lane {brief['lane_sequence']} · [0-9]{{4}}-[0-9]{{2}}-[0-9]{{2}}",
                    leading,
                )
            ) or (
                cross_program
                and re.fullmatch(r"Updated [0-9]{1,2} [A-Za-z]+ [0-9]{4}", leading)
            )
            if redundant_identity:
                body_lines = body_lines[1:]
                if body_lines and not body_lines[0].strip():
                    body_lines = body_lines[1:]
                body = "\n".join(body_lines)
        body_head, separator, compact_footer = body.rpartition("\n---\n")
        if (
            separator
            and "[Release metadata](release.json)" in compact_footer
            and "[Current proof sources]" in compact_footer
        ):
            body = body_head.rstrip()
    updated = datetime.fromisoformat(release["updated_at"]).strftime("%-d %B %Y")
    identity = f"{label.removeprefix('Model research brief · ')} · Updated {updated}"
    footer_links = []
    if retained_target is not None:
        footer_links.append(f"[Retained working mathematics]({retained_target})")
    if lane:
        footer_links.append(
            "[Optional runnable source ZIP]"
            f"(../inputs/lane-{brief['lane_sequence']}-source-files.zip)"
        )
    footer_links.extend(
        [
            f"[Current proof sources]({source_target})",
            "[Machine-readable release metadata](release.json)",
        ]
    )
    return "\n".join(
        [
            "---",
            f"title: {_yaml('Model research brief — ' + brief['title'])}",
            "description: \"A self-contained mathematical handoff for a research model.\"",
            "---",
            "",
            title_line,
            "",
            f'<p class="claim-tag">{identity}</p>',
            "",
            body,
            "",
            "## Sources and release",
            "",
            " · ".join(footer_links),
            "",
            "The linked source text is preferred for full proof context; PDFs are optional archival copies.",
            "",
            back_link,
            "",
        ]
    )


def render_claim(
    claim: dict[str, Any],
    collections: dict[str, dict[str, Any]],
    correction: dict[str, Any] | None = None,
) -> str:
    correction_block = []
    historical = False
    if correction is not None:
        unit_id = correction["unit_id"]
        historical = correction["_forward_relation"] in {"corrects", "supersedes"}
        if historical:
            correction_block = [
                '!!! warning "Replaced by current working mathematics"',
                "    This stable-tag statement is retained as publication history. Use the",
                f"    [current replacement](../research/working-mathematics/units/{unit_id}.md)",
                "    for research and model handoffs.",
                "",
                "## Current replacement",
                "",
                correction["statement"],
                "",
            ]
        else:
            correction_block = [
                '!!! info "A stronger current result is available"',
                "    The statement below remains valid, and the",
                f"    [stronger current unit](../research/working-mathematics/units/{unit_id}.md)",
                "    gives the improved formulation.",
                "",
            ]
    lines = [
        "---",
        f"title: {_yaml(claim['title'])}",
        f"description: {_yaml(claim['statement'])}",
        "---",
        "",
        f'<p class="claim-tag">{claim["tag"]}</p>',
        f"# {claim['title']}",
        "",
        *correction_block,
        *(
            []
            if historical
            or claim["statement"].strip() == claim["title"].strip()
            else [f'<p class="dek">{claim["statement"]}</p>', ""]
        ),
        f'<span class="status status-kind">{_human(claim["kind"]).title()}</span> '
        f'<span class="status status-draft">{_status_label(claim["status"])}</span> '
        f'<span class="status">{claim["prominence"].title()}</span>',
        "",
        "## Exact statement",
        "",
        *(
            ["**Superseded legacy wording:**", ""]
            if historical
            else []
        ),
        claim["statement"],
        "",
        f"Statement version `{claim['statement_version']}`. The public tag is stable; "
        "statement revisions increment the version rather than replacing the tag.",
        "",
        "## Appears in",
        "",
    ]
    for membership in claim["memberships"]:
        collection = collections[membership["collection_slug"]]
        lines.append(
            f"- [{collection['title']}](../collections/{collection['slug']}.md) — "
            f"{_human(membership['inclusion'])}, {_human(membership['role'])}"
        )
    if not claim["memberships"]:
        lines.append("- No grouped public page currently contains this record.")
    lines.extend(["", "## Proof access and evidence boundary", ""])
    for access in claim["proof_access"]:
        collection = collections[access["collection_slug"]]
        lines.append(
            f"- [{collection['title']}](../collections/{collection['slug']}.md): "
            f"**{_coverage_label(access['status'])}**"
        )
    if not claim["proof_access"]:
        lines.append("- No program-manuscript location is claimed for this record.")
    locators = claim.get("locators", [])
    if locators:
        # Manuscript-source anchors from the private coverage audit; plain
        # text only, so no private path or identifier can become a link.
        lines.extend(["", "## Proof locators", ""])
        for locator in locators:
            role = locator["role"].strip()
            suffix = f" ({role})" if role else ""
            lines.append(
                f"- `{locator['anchor']}` in `{locator['repo_path']}`{suffix}"
            )
    evidence = claim["verification"].get("evidence", [])
    precise_evidence = [
        item
        for item in evidence
        if isinstance(item, dict)
        and (
            item.get("links")
            or not item.get("scope", "").startswith(
                ("A proof is present", "Supporting checks are present")
            )
        )
    ]
    if precise_evidence:
        lines.extend(["", "**Recorded evidence**", ""])
        for item in precise_evidence:
            lines.append(f"- {_human(item['kind']).title()}: {item['scope']}")
    provenance = claim["provenance"]
    sources = _source_lines(provenance.get("sources", []))
    if sources:
        lines.extend(["", "## Public sources", "", *sources])
    credits = _credit_lines(provenance.get("credited_to", []))
    if credits:
        lines.extend(["", "## Credit", "", *credits])
    assistance = provenance.get("ai_assistance", {})
    if assistance.get("present"):
        lines.extend(["", "## AI assistance", ""])
        for item in assistance.get("systems", []):
            lines.append(
                f"- {item['system']}: {', '.join(_human(role) for role in item['roles'])}; "
                f"{item['purpose']}"
            )
        humans = assistance.get("responsible_humans", [])
        if humans:
            lines.append(f"- Responsible human(s): {', '.join(humans)}")
    lines.extend(["", "[Browse all claims](../results/all-claims.md)", ""])
    return "\n".join(lines)


def render_collection(
    page: dict[str, Any],
    claims: dict[str, dict[str, Any]],
    collections: dict[str, dict[str, Any]],
    corrections: dict[str, dict[str, Any]],
) -> str:
    coverage = page["manuscript_coverage"]["status"]
    historical_updates = [
        corrections[tag]
        for tag in page["member_tags"]
        if tag in corrections
        and corrections[tag]["_forward_relation"] in {"corrects", "supersedes"}
    ]
    visible_description = (
        "This historical package includes replaced atomic statements. Follow "
        "the current-unit links below for reusable mathematics."
        if historical_updates
        else page["description"]
    )
    lines = [
        "---",
        f"title: {_yaml(page['title'])}",
        f"description: {_yaml(page['description'])}",
        "---",
        "",
        f"# {page['title']}",
        "",
        f'<p class="dek">{visible_description}</p>',
        "",
        f'<span class="status status-kind">{_human(page["kind"]).title()}</span> '
        f'<span class="status coverage-{coverage}">{_coverage_label(coverage)}</span>',
        "",
        "## Precise statement",
        "",
        *(
            [
                "This package contains one or more replaced atomic statements. "
                "The current mathematical statements and forward links are listed below."
            ]
            if historical_updates
            else [page["statement"]]
        ),
        "",
        "## Claims in this result package",
        "",
    ]
    for tag in page["member_tags"]:
        claim = claims[tag]
        correction = corrections.get(tag)
        historical = correction is not None and correction[
            "_forward_relation"
        ] in {"corrects", "supersedes"}
        member_title = "Replaced historical record" if historical else claim["title"]
        membership = next(
            item
            for item in claim["memberships"]
            if item["collection_slug"] == page["slug"]
        )
        lines.extend(
            [
                f"### [{claim['tag']} · {member_title}](../claims/{claim['tag']}.md)",
                "",
                *(
                    (
                        [
                            '!!! warning "Replaced working statement"',
                            "    The historical wording is suppressed here. Use the "
                            f"[current replacement](../research/working-mathematics/units/{correction['unit_id']}.md).",
                            "",
                        ]
                        if historical
                        else [
                            '!!! info "Stronger current result"',
                            "    A "
                            f"[stronger current unit](../research/working-mathematics/units/{correction['unit_id']}.md) "
                            "is available.",
                            "",
                        ]
                    )
                    if correction is not None
                    else []
                ),
                correction["statement"] if historical else claim["statement"],
                "",
                f"*{_human(membership['inclusion']).title()} · "
                f"{_human(membership['role']).title()} · {_status_label(claim['status'])}*",
                "",
            ]
        )
    lines.extend(
        [
            "## Evidence and manuscript boundary",
            "",
            page["source_treatment"],
            "",
            page["manuscript_coverage"]["coverage_rule"],
            "",
        ]
    )
    if page["source"]:
        lines.extend(["### Public sources", "", *_source_lines(page["source"]), ""])
    if page["credited_to"]:
        lines.extend(["", "## Credit", "", *_credit_lines(page["credited_to"]), ""])
    connected = sorted(
        set(page["connections"].get("depends_on", []))
        | set(page["connections"].get("shares_claims_with", []))
    )
    if connected:
        lines.extend(["## Connections", ""])
        for slug in connected:
            if slug in collections:
                lines.append(
                    f"- [{collections[slug]['title']}](../collections/{slug}.md)"
                )
        lines.append("")
    lines.extend(["[Back to Results](../results/index.md)", ""])
    return "\n".join(lines)


def render_results_index(
    collections: dict[str, dict[str, Any]],
    claims: dict[str, dict[str, Any]],
) -> str:
    highlights = [
        page
        for page in collections.values()
        if page["public"]["release_state"] == "public" or page["slug"] in NEW_COLLECTIONS
    ]
    lines = [
        "---",
        'title: "Results and open problems"',
        'description: "A reader-facing map into the complete tagged claim graph."',
        "---",
        "",
        "# Results and open problems",
        "",
        '<p class="dek">Start with landmark results and the newest research packages, '
        "then move into the complete stable-tag claim graph.</p>",
        "",
        '<div class="metric-grid" markdown>',
        "",
        f"- **{sum(p['kind'] == 'result' for p in collections.values())}** grouped results",
        f"- **{sum(p['kind'] == 'open_problem' for p in collections.values())}** open-problem packages",
        f"- **{len(claims)}** stable-tag atomic claims",
        "",
        "</div>",
        "",
        "[Browse every tagged claim](all-claims.md){ .md-button .md-button--primary }",
        "[See open problems](open-problems.md){ .md-button }",
        "[Open the proof index](../evidence/index.md){ .md-button }",
        "",
        "## Highlights",
        "",
        '<div class="record-grid" markdown>',
        "",
    ]
    for page in sorted(highlights, key=lambda item: item["title"].casefold()):
        lines.extend(
            [
                f"### [{page['title']}](../collections/{page['slug']}.md)",
                "",
                page["description"],
                "",
                f"*{_human(page['kind'])} · {_coverage_label(page['manuscript_coverage']['status'])}*",
                "",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines)


def render_all_claims(
    claims: dict[str, dict[str, Any]],
    corrections: dict[str, dict[str, Any]],
) -> str:
    counts = Counter(claim["prominence"] for claim in claims.values())
    lines = [
        "---",
        'title: "All claims"',
        'description: "The complete searchable stable-tag claim catalogue."',
        "---",
        "",
        "# All claims",
        "",
        '<p class="dek">Every public atomic statement has one stable tag. Tags remain fixed when wording evolves; statement versions record revisions.</p>',
        "",
        f"{counts['headline']} headline · {counts['core']} core · {counts['supporting']} supporting",
        "",
        '<div class="claim-list" markdown>',
        "",
    ]
    for claim in sorted(claims.values(), key=lambda item: item["tag"]):
        correction = corrections.get(claim["tag"])
        suffix = ""
        if correction is not None:
            if correction["_forward_relation"] in {"corrects", "supersedes"}:
                suffix = f"; replaced by `{correction['unit_id']}`"
            else:
                suffix = f"; strengthened by `{correction['unit_id']}`"
        lines.append(
            f"- [`{claim['tag']}`](../claims/{claim['tag']}.md) "
            f"**{claim['title']}** — {_status_label(claim['status'])}{suffix}"
        )
    lines.extend(["", "</div>", ""])
    return "\n".join(lines)


def render_open_problems(
    collections: dict[str, dict[str, Any]], claims: dict[str, dict[str, Any]]
) -> str:
    pages = sorted(
        (p for p in collections.values() if p["kind"] == "open_problem"),
        key=lambda item: item["title"].casefold(),
    )
    atomic = sorted(
        (c for c in claims.values() if c["kind"] == "open_problem"),
        key=lambda item: item["tag"],
    )
    lines = [
        "---",
        'title: "Open problems"',
        'description: "Unresolved questions separated from proved reductions and computational evidence."',
        "---",
        "",
        "# Open problems",
        "",
        f'<p class="dek">{len(pages)} grouped frontiers and {len(atomic)} atomic open-question records. Each page separates what is known from the step that remains.</p>',
        "",
    ]
    for page in pages:
        lines.extend(
            [
                f"## [{page['title']}](../collections/{page['slug']}.md)",
                "",
                page["description"],
                "",
                f"**Open statement:** {page['statement']}",
                "",
            ]
        )
    return "\n".join(lines)


def render_corrections(
    claims: dict[str, dict[str, Any]],
    corrections: dict[str, dict[str, Any]],
) -> str:
    selected = [
        claim
        for claim in claims.values()
        if claim["tag"] in corrections
        or any(
            word in (claim["title"] + " " + claim["statement"]).casefold()
            for word in ("correction", "corrected", "proof gap", "failed extension")
        )
    ]
    lines = [
        "---",
        'title: "Corrections and scope changes"',
        'description: "Tagged records that correct, narrow, or explicitly retire an earlier line of argument."',
        "---",
        "",
        "# Corrections and scope changes",
        "",
        '<p class="dek">Corrections live in the same claim graph as results. They are not buried in release notes.</p>',
        "",
    ]
    for claim in sorted(selected, key=lambda item: item["tag"]):
        correction = corrections.get(claim["tag"])
        lines.extend(
            [
                f"## [{claim['tag']} · {claim['title']}](../claims/{claim['tag']}.md)",
                "",
                claim["statement"],
                "",
                *(
                    [
                        (
                            "**Current replacement:** "
                            if correction["_forward_relation"]
                            in {"corrects", "supersedes"}
                            else "**Stronger current result:** "
                        )
                        + f"[{correction['unit_id']}](../research/working-mathematics/units/{correction['unit_id']}.md)",
                        "",
                        correction["statement"],
                        "",
                    ]
                    if correction is not None
                    else []
                ),
            ]
        )
    return "\n".join(lines)


def _manuscript(program: dict[str, Any], manuscripts: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return manuscripts[program["manuscript"][:2]]


def render_program(
    program: dict[str, Any],
    collections: dict[str, dict[str, Any]],
    manuscripts: dict[str, dict[str, Any]],
    briefs: dict[str, dict[str, Any]],
    proof_sources: dict[str, Any],
) -> str:
    pages = [collections[slug] for slug in program["collection_slugs"]]
    results = [page for page in pages if page["kind"] == "result"]
    problems = [page for page in pages if page["kind"] == "open_problem"]
    coverage = Counter(page["manuscript_coverage"]["status"] for page in pages)
    manuscript = _manuscript(program, manuscripts)
    entry = _proof_entrypoint(proof_sources, program["sequence"])
    source_path = entry["path"].removeprefix("manuscripts/")
    source_route = proof_source_route(source_path).relative_to("research")
    lines = [
        "---",
        f"title: {_yaml(program['title'])}",
        f"description: {_yaml(program['question'])}",
        "---",
        "",
        f'<p class="claim-tag">Program {program["sequence"]}</p>',
        f"# {program['title']}",
        "",
        f'<p class="dek">{program["question"]}</p>',
        "",
        program["summary"],
        "",
        '<div class="metric-grid" markdown>',
        "",
        f"- **{len(results)}** result packages",
        f"- **{len(problems)}** open-problem packages",
        f"- **{coverage.get('complete', 0)}** exact-coverage pages",
        "",
        "</div>",
        "",
    ]
    if program["slug"] in briefs:
        brief = briefs[program["slug"]]
        lines.extend(
            [
                "## Model research brief",
                "",
                f"[Give a research model this one page](../handoffs/{program['slug']}.md)"
                "{ .md-button .md-button--primary }",
                "",
                "The brief is self-contained: setup, proved results with stable claim links, live frontier, failed approaches, tasks, evidence boundaries, and scope fences. No ZIP or private replay access is required.",
                "",
                f"Research state {brief['updated_at'] if brief.get('updated_at') else '29 July 2026'} · {brief['words']} words",
                "",
            ]
        )
    lines.extend(
        [
            "## Current text proof sources",
            "",
            f"[Open the complete Program {program['sequence']} TeX source]"
            f"(../{source_route.as_posix()})"
            "{ .md-button .md-button--primary }",
            "",
            "The text source is the current model-friendly authority: exact "
            "definitions, statements, proofs, dependencies, and label anchors.",
            "",
            "## Optional PDF reading copy",
            "",
            f"[{manuscript['title']}, v{manuscript['version']}](../../assets/manuscripts/{manuscript['filename']})"
            "{ .md-button }",
            "",
            f"Nathaniel Monson · {manuscript['pages']} pages · dated {manuscript['manuscript_date']} · SHA-256 `{manuscript['sha256']}`",
            "",
            "This PDF predates some August 1 source repairs. Use it for reading, "
            "not as the authority when it differs from the retained graph or text source.",
            "",
        ]
    )
    for heading, selected in (("Results", results), ("Open problems", problems)):
        if not selected:
            continue
        lines.extend([f"## {heading}", ""])
        for page in sorted(selected, key=lambda item: item["title"].casefold()):
            lines.extend(
                [
                    f"### [{page['title']}](../../collections/{page['slug']}.md)",
                    "",
                    page["description"],
                    "",
                    f"*{_coverage_label(page['manuscript_coverage']['status'])}*",
                    "",
                ]
            )
    lines.extend(["[Back to research state](../index.md)", ""])
    return "\n".join(lines)


def render_research_index(
    programs: dict[str, dict[str, Any]],
    collections: dict[str, dict[str, Any]],
    claims: dict[str, dict[str, Any]],
    briefs: dict[str, dict[str, Any]],
) -> str:
    lines = [
        "---",
        'title: "State of the research program"',
        'description: "Six working programs, their strongest reductions, and their exact open boundaries."',
        "---",
        "",
        "# State of the research program",
        "",
        '<p class="dek">The counterexample is settled; the surrounding classification, minimality, moduli, homogeneous reduction, and plane-boundary questions are not.</p>',
        "",
        f"The current candidate incorporates {len(collections)} grouped "
        f"result/problem packages and {len(claims)} stable-tag atomic claims. "
        "Manuscript coverage and independent verification are displayed "
        "separately from mathematical status.",
        "",
        "## Model-ready handoffs",
        "",
        "A model-ready handoff is a single self-contained web page. Optional source-tree archives support local execution, but no download is required to read the setup, known results, tasks, and evidence boundaries.",
        "",
        "[Open the current research-task roadmap](tasks/index.md) for every ready and blocked task, its effort profile, dependencies, and exact missing inputs.",
        "",
    ]
    primary = sorted(
        (
            brief
            for brief in briefs.values()
            if brief.get("primary_entrypoint", False)
        ),
        key=lambda item: item.get("display_sequence", item["program_sequence"]),
    )
    secondary = sorted(
        (
            brief
            for brief in briefs.values()
            if not brief.get("primary_entrypoint", False)
        ),
        key=lambda item: item.get("display_sequence", item["program_sequence"]),
    )
    for brief in primary:
        label = (
            brief["title"]
            if brief.get("kind") != "lane"
            else f"Lane {brief['lane_sequence']}: {brief['title']}"
        )
        lines.extend(
            [
                f"- [{label}](handoffs/{brief['program_slug']}.md) — {brief['words']} words.",
                "",
            ]
        )
    lines.extend(
        [
            "### Deeper program dossiers",
            "",
            "The six program dossiers are durable subject views over the same mathematics; use them for broader context and proof navigation.",
            "",
        ]
    )
    for brief in secondary:
        lines.extend(
            [
                f"- [Program {brief['program_sequence']}: {brief['title']}](handoffs/{brief['program_slug']}.md) — {brief['words']} words.",
                "",
            ]
        )
    lines.extend(
        [
            "## Six programs",
            "",
            '<div class="record-grid" markdown>',
            "",
        ]
    )
    for program in sorted(programs.values(), key=lambda item: item["sequence"]):
        pages = [collections[slug] for slug in program["collection_slugs"]]
        open_count = sum(page["kind"] == "open_problem" for page in pages)
        lines.extend(
            [
                f"### [{program['sequence']}. {program['title']}](programs/{program['slug']}.md)",
                "",
                f"**{program['question']}**",
                "",
                program["summary"],
                "",
                f"*{len(pages)} packages · {open_count} open*",
                "",
            ]
        )
    lines.extend(["</div>", "", "## New in this candidate", ""])
    for slug in NEW_COLLECTIONS:
        page = collections[slug]
        lines.append(f"- [{page['title']}](../collections/{slug}.md) — {page['description']}")
    lines.extend(["", "[Browse the papers](papers.md){ .md-button }", ""])
    return "\n".join(lines)


def render_papers(manuscripts: dict[str, dict[str, Any]]) -> str:
    version = max(int(item["version"]) for item in manuscripts.values())
    lines = [
        "---",
        'title: "Working papers"',
        'description: "Six reader manuscripts and the companion results-and-research register."',
        "---",
        "",
        "# Working papers",
        "",
        f'<p class="dek">Version {version} of the six-program reader set. These are working manuscripts.</p>',
        "",
    ]
    for key, item in sorted(manuscripts.items()):
        lines.extend(
            [
                f"## [{item['title']}](../assets/manuscripts/{item['filename']})",
                "",
                f"Version {item['version']} · {item['pages']} pages · {item['manuscript_date']} · `{item['kind']}`",
                "",
                f"SHA-256 `{item['sha256']}`",
                "",
            ]
        )
    return "\n".join(lines)


def render_evidence_index(collections: dict[str, dict[str, Any]]) -> str:
    counts = Counter(page["manuscript_coverage"]["status"] for page in collections.values())
    lines = [
        "---",
        'title: "Proof and evidence index"',
        'description: "Claim-by-claim manuscript coverage and review boundaries."',
        "---",
        "",
        "# Proof and evidence index",
        "",
        '<p class="dek">Where a statement is written down is not the same as whether it has been independently checked.</p>',
        "",
        '<div class="metric-grid" markdown>',
        "",
        f"- **{counts['complete']}** exact manuscript coverage",
        f"- **{counts['partial']}** locator audits incomplete",
        f"- **{counts['not_applicable']}** no program manuscript claimed",
        "",
        "</div>",
        "",
        "| Result or problem package | Kind | Manuscript coverage |",
        "| --- | --- | --- |",
    ]
    for page in sorted(collections.values(), key=lambda item: item["title"].casefold()):
        lines.append(
            f"| [{page['title']}](../collections/{page['slug']}.md) | "
            f"{_human(page['kind'])} | {_coverage_label(page['manuscript_coverage']['status'])} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_materials(materials: dict[str, Any]) -> str:
    lines = [
        "---",
        'title: "Technical materials"',
        'description: "Hash-pinned public computations, source bundles, and technical notes."',
        "---",
        "",
        "# Technical materials",
        "",
        f'<p class="dek">{materials["artifact_count"]} sanitized artifacts across {materials["program_count"]} programs.</p>',
        "",
        "Artifacts document exact calculations and reproducibility boundaries. They are not substitutes for proof or independent review.",
        "",
    ]
    for program in sorted(materials["programs"], key=lambda item: item["sequence"]):
        lines.extend([f"## {program['sequence']}. {program['title']}", "", program["scope"], ""])
        for item in program["artifacts"]:
            lines.extend(
                [
                    f"### [{item['title']}](../assets/technical-materials/{item['filename']})",
                    "",
                    item["scope"],
                    "",
                    f"**Boundary:** {item['limitations']}",
                    "",
                    f"SHA-256 `{item['sha256']}`",
                    "",
                ]
            )
    return "\n".join(lines)


def expected_outputs(root: Path) -> dict[Path, str | bytes]:
    _, claims, collections, programs, manuscripts, materials, briefs = load(root)
    release = build_release_metadata(root)
    docs = root / PUBLIC_DOCS_DIR
    outputs: dict[Path, str] = {}
    retained = load_retained_math(root)
    retained_v2 = load_retained_math_v2(root)
    proof_sources = load_manuscript_sources(root)
    if proof_sources is None:
        raise ValueError("selected release does not pin manuscript sources")
    if retained is None:
        raise ValueError("selected release does not pin retained mathematics")
    if retained_v2 is None:
        raise ValueError("selected release does not pin retained-math v2")
    if (
        proof_sources["retained_registry"]["registry_id"]
        != retained[1]["registry_id"]
    ):
        raise ValueError("manuscript sources and retained graph disagree")
    corrections = retained_corrections(retained)
    v2_payload = retained_v2[1]
    full_v2 = retained_v2_is_full(v2_payload)
    v2_graph = retained_v2_graph(v2_payload)
    compatibility_routes: dict[str, dict[str, Any]] = {}
    v2_units: dict[str, dict[str, Any]] = {}
    if full_v2:
        compatibility = retained_v2_compatibility(v2_payload)
        assert compatibility is not None
        compatibility_routes = compatibility_by_id(compatibility)
        v2_units = {item["unit_id"]: item for item in v2_graph["units"]}
    for claim in claims.values():
        if full_v2:
            outputs[docs / "claims" / f"{claim['tag']}.md"] = (
                render_compatible_claim(
                    claim,
                    collections,
                    compatibility_routes[claim["tag"]],
                    v2_units,
                )
            )
        else:
            outputs[docs / "claims" / f"{claim['tag']}.md"] = render_claim(
                claim, collections, corrections.get(claim["tag"])
            )
    for page in collections.values():
        if full_v2:
            outputs[docs / "collections" / f"{page['slug']}.md"] = (
                render_compatible_collection(
                    page,
                    claims,
                    collections,
                    compatibility_routes,
                    v2_units,
                )
            )
        else:
            outputs[docs / "collections" / f"{page['slug']}.md"] = render_collection(
                page, claims, collections, corrections
            )
    for program in programs.values():
        outputs[
            docs / "research/programs" / f"{program['slug']}.md"
        ] = render_program(
            program, collections, manuscripts, briefs, proof_sources
        )
    for brief in briefs.values():
        source_path = root / "data" / MODEL_BRIEFS_DATA_DIR / brief["source"]
        outputs[docs / brief["route"]] = render_model_brief(
            brief,
            source_path.read_text(encoding="utf-8"),
            manuscripts,
            release,
            proof_sources,
            v2_graph,
        )
    brief_manifest = _load(root / "data" / MODEL_BRIEFS_DATA_DIR / "manifest.json")
    for item in brief_manifest.get("task_inputs", []):
        source_path = root / "data" / MODEL_BRIEFS_DATA_DIR / item["source"]
        outputs[docs / item["route"]] = (
            source_path.read_bytes()
            if task_input_is_binary(item)
            else source_path.read_text(encoding="utf-8")
        )
    task_roadmap = brief_manifest["task_roadmap"]
    roadmap_source = (
        root / "data" / MODEL_BRIEFS_DATA_DIR / task_roadmap["source"]
    )
    outputs[docs / task_roadmap["route"]] = roadmap_source.read_text(
        encoding="utf-8"
    )
    public_source_packets = source_packet_routes(brief_manifest)
    outputs[docs / "research/handoffs/release.json"] = (
        json.dumps(release, indent=2, sort_keys=True) + "\n"
    )
    if full_v2:
        compatibility = retained_v2_compatibility(v2_payload)
        assert compatibility is not None
        outputs[docs / "research/working-mathematics/graph.json"] = (
            json.dumps(v2_graph, indent=2, ensure_ascii=False, sort_keys=True)
            + "\n"
        )
        outputs[
            docs / "research/working-mathematics/legacy-compatibility.json"
        ] = (
            json.dumps(
                compatibility, indent=2, ensure_ascii=False, sort_keys=True
            )
            + "\n"
        )
    else:
        outputs[docs / "research/handoffs/retained-math-v2-pilot.json"] = (
            json.dumps(v2_payload, indent=2, ensure_ascii=False, sort_keys=True)
            + "\n"
        )
    outputs[docs / "results/index.md"] = render_results_index(
        collections, claims
    )
    outputs[docs / "results/all-claims.md"] = (
        render_all_claims_compatible(claims, compatibility_routes, v2_units)
        if full_v2
        else render_all_claims(claims, corrections)
    )
    outputs[docs / "results/open-problems.md"] = render_open_problems(
        collections, claims
    )
    outputs[docs / "results/corrections.md"] = (
        render_corrections_compatible(compatibility_routes, v2_units)
        if full_v2
        else render_corrections(claims, corrections)
    )
    outputs[docs / "research/index.md"] = render_research_index(
        programs, collections, claims, briefs
    )
    outputs[docs / "research/papers.md"] = render_papers(manuscripts)
    outputs[docs / "evidence/index.md"] = render_evidence_index(collections)
    outputs[docs / "evidence/materials.md"] = render_materials(materials)
    source_data = root / "data" / SITE_STATE["manuscript_sources"]["data_dir"]
    outputs[docs / "research/proof-sources/index.md"] = (
        render_proof_source_index(proof_sources)
    )
    for item in proof_sources["files"]:
        source_path = source_data / "sources" / item["path"]
        outputs[docs / proof_source_route(item["path"])] = (
            render_proof_source_page(
                item, source_path.read_text(encoding="utf-8")
            )
        )
    if full_v2:
        program_links = "\n".join(
            f"- [{program['title']}](programs/{program['slug']}.md)"
            for program in v2_graph["programs"]
        )
        counts = v2_graph["counts"]
        outputs[docs / "research/working-mathematics/index.md"] = (
            "# Retained working mathematics\n\n"
            "This current view is compiled from first-class mathematical units, "
            "arguments, evidence, and typed relations. Historical route mapping "
            "is kept separate from the progress-facing mathematics.\n\n"
            f"The graph contains **{counts['units']} current units**, "
            f"**{counts['arguments']} arguments**, and "
            f"**{counts['evidence']} evidence objects** across "
            f"{counts['programs']} overlapping program views.\n\n"
            f"{program_links}\n\n"
            "[Machine-readable graph](graph.json) · "
            "[Legacy route compatibility](legacy-compatibility.json)\n"
        )
        for program in v2_graph["programs"]:
            outputs[
                docs
                / "research/working-mathematics/programs"
                / f"{program['slug']}.md"
            ] = render_retained_v2_program(program, v2_graph)
        for unit in v2_graph["units"]:
            outputs[
                docs
                / "research/working-mathematics/units"
                / f"{unit['unit_id']}.md"
            ] = render_retained_v2_unit(
                unit,
                v2_graph,
                proof_sources,
                public_source_packets,
            )
    elif retained is not None:
        _, retained_graph = retained
        retained_data = root / "data" / SITE_STATE["retained_math"]["data_dir"]
        retained_programs = retained_graph["programs"]
        program_links = "\n".join(
            f"- [{program['title']}](programs/{program['slug']}.md)"
            for program in retained_programs
        )
        retained_counts = retained_graph["counts"]
        outputs[docs / "research/working-mathematics/index.md"] = (
            "# Retained working mathematics\n\n"
            "This view is generated from the retained mathematical graph. It "
            "exposes exact reusable units, supplied support, dependencies, and "
            "scope without private source locators or editorial workflow labels.\n\n"
            f"The current graph contains **{retained_counts['units']} working units** "
            f"across {len(retained_programs)} overlapping program views, with "
            f"{retained_counts['support_objects']} support objects and "
            f"{retained_counts['relations']} typed relations.\n\n"
            f"{program_links}\n\n"
            "This is not the publication-ready subset. Verification, attribution, "
            "deduplication, and dependency repair proceed asynchronously.\n"
        )
        for program in retained_programs:
            relative = Path("programs") / f"{program['slug']}.md"
            outputs[
                docs / "research/working-mathematics" / relative
            ] = (retained_data / relative).read_text(encoding="utf-8")
        for source in sorted((retained_data / "units").glob("*.md")):
            outputs[
                docs / "research/working-mathematics/units" / source.name
            ] = source.read_text(encoding="utf-8")
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        outputs = expected_outputs(root)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if args.write:
        for path, content in sorted(outputs.items()):
            if path.exists():
                raise FileExistsError(f"refusing to overwrite generated page: {path}")
            path.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(content, bytes):
                path.write_bytes(content)
            else:
                path.write_text(content, encoding="utf-8")
        print(f"Generated {len(outputs)} graph-native pages.")
        return 0
    failures = []
    for path, expected in sorted(outputs.items()):
        if not path.is_file():
            failures.append(f"missing generated file: {path.relative_to(root)}")
        elif isinstance(expected, bytes):
            if path.read_bytes() != expected:
                failures.append(f"stale generated file: {path.relative_to(root)}")
        elif path.read_text(encoding="utf-8") != expected:
            failures.append(f"stale generated file: {path.relative_to(root)}")
    expected_paths = set(outputs)
    for directory in (
        root / PUBLIC_DOCS_DIR / "claims",
        root / PUBLIC_DOCS_DIR / "collections",
        root / PUBLIC_DOCS_DIR / "research/programs",
        root / PUBLIC_DOCS_DIR / "research/handoffs",
        root / PUBLIC_DOCS_DIR / "research/tasks",
        root / PUBLIC_DOCS_DIR / "research/proof-sources",
        root / PUBLIC_DOCS_DIR / "research/working-mathematics/programs",
        root / PUBLIC_DOCS_DIR / "research/working-mathematics/units",
    ):
        for path in directory.rglob("*.md"):
            if path not in expected_paths:
                failures.append(f"unexpected generated file: {path.relative_to(root)}")
    if failures:
        print("Living-guide v2 generation check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Living-guide v2 generation check passed for {len(outputs)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
