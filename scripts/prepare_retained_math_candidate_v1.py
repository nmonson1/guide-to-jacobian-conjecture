#!/usr/bin/env python3
"""Prepare a non-published site candidate from a retained-math public graph."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_PATTERNS = {
    "private filesystem path": re.compile(r"(?:/fss/|/home/|file://)"),
    "conversation locator": re.compile(
        r"(?:chatgpt\.com/share|conversation_id|message_id|artifact_id)",
        re.IGNORECASE,
    ),
}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def _write_once(path: Path, payload: bytes) -> None:
    if path.exists():
        raise ValueError(f"refusing to overwrite candidate output: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(payload)


def _verify_source(source: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    manifest_path = source / "manifest.json"
    graph_path = source / "public-graph.json"
    if not manifest_path.is_file() or not graph_path.is_file():
        raise ValueError("retained-math source lacks manifest or public graph")
    manifest = _load(manifest_path)
    graph = _load(graph_path)
    if graph.get("registry_id") != manifest.get("registry_id"):
        raise ValueError("retained-math public graph and manifest disagree")
    pinned = {item["path"]: item for item in manifest.get("files", [])}
    for relative, item in pinned.items():
        path = source / relative
        if not path.is_file() or _sha256(path) != item["sha256"]:
            raise ValueError(f"retained-math source pin failed: {relative}")
    rendered = graph_path.read_text(encoding="utf-8")
    for label, pattern in PRIVATE_PATTERNS.items():
        if pattern.search(rendered):
            raise ValueError(f"{label} leaked into retained-math public graph")
    return manifest, graph


def _candidate_config(
    base: Path, docs_name: str, programs: list[dict[str, Any]]
) -> str:
    text = base.read_text(encoding="utf-8")
    text = re.sub(r"^docs_dir: .+$", f"docs_dir: {docs_name}", text, count=1, flags=re.M)
    text = re.sub(r"^edit_uri: .+$", "edit_uri: ''", text, count=1, flags=re.M)
    marker = "  - Research:\n"
    if text.count(marker) != 1:
        raise ValueError("could not locate unique Research navigation section")
    retained_nav = (
        "    - Retained working mathematics:\n"
        "      - Overview: research/working-mathematics/index.md\n"
        + "".join(
            "      - "
            + program["title"]
            + ": research/working-mathematics/programs/"
            + program["slug"]
            + ".md\n"
            for program in programs
        )
    )
    return text.replace(marker, marker + retained_nav, 1)


def prepare(
    *,
    source: Path,
    base_docs: Path,
    docs_output: Path,
    data_output: Path,
    config_output: Path,
) -> dict[str, Any]:
    for path in (docs_output, data_output, config_output):
        if path.exists():
            raise ValueError(f"refusing to overwrite candidate output: {path}")
    manifest, graph = _verify_source(source)
    programs = graph.get("programs", [])
    if not programs:
        raise ValueError("retained-math source has no program views")
    dossiers = {
        program["slug"]: source / "programs" / f"{program['slug']}.md"
        for program in programs
    }
    units = sorted((source / "units").glob("*.md"))
    if (
        not all(path.is_file() for path in dossiers.values())
        or len(units) != graph["counts"]["units"]
    ):
        raise ValueError("retained-math source lacks expected generated pages")

    shutil.copytree(base_docs, docs_output)
    graph_target = data_output / "public-graph.json"
    _write_once(graph_target, (source / "public-graph.json").read_bytes())
    program_targets = []
    for program in programs:
        slug = program["slug"]
        target = (
            docs_output
            / "research"
            / "working-mathematics"
            / "programs"
            / f"{slug}.md"
        )
        _write_once(target, dossiers[slug].read_bytes())
        program_targets.append(target)
    unit_targets = []
    for unit in units:
        target = (
            docs_output
            / "research"
            / "working-mathematics"
            / "units"
            / unit.name
        )
        _write_once(target, unit.read_bytes())
        unit_targets.append(target)

    program_links = "\n".join(
        f"- [{program['title']}](programs/{program['slug']}.md)"
        for program in programs
    )
    overview = (
        "# Retained working mathematics\n\n"
        "This candidate view is generated from the retained mathematical graph. "
        "It exposes exact reusable units, supplied support, dependencies, and "
        "scope without private source locators or editorial workflow labels.\n\n"
        f"The current graph contains **{graph['counts']['units']} working units** "
        f"across {len(programs)} overlapping program views, with "
        f"{graph['counts']['support_objects']} support objects and "
        f"{graph['counts']['relations']} typed relations.\n\n"
        + program_links
        + "\n\n"
        "This is not the publication-ready subset. Verification, attribution, "
        "deduplication, and dependency repair proceed asynchronously.\n"
    )
    overview_path = docs_output / "research/working-mathematics/index.md"
    _write_once(overview_path, overview.encode("utf-8"))

    for program in programs:
        slug = program["slug"]
        handoff = docs_output / "research/handoffs" / f"{slug}.md"
        handoff_text = handoff.read_text(encoding="utf-8")
        handoff_note = (
            "\n!!! info \"Retained working graph\"\n"
            "    Exact reusable units and their deeper support pages are "
            f"available in the [retained working mathematics view](../working-mathematics/programs/{slug}.md).\n"
        )
        first_break = handoff_text.find("\n")
        if first_break < 0:
            raise ValueError(f"handoff lacks a title line: {handoff}")
        handoff.write_text(
            handoff_text[: first_break + 1]
            + handoff_note
            + handoff_text[first_break + 1 :],
            encoding="utf-8",
        )

    config_text = _candidate_config(
        ROOT / "mkdocs.yml", docs_output.name, programs
    )
    _write_once(config_output, config_text.encode("utf-8"))
    materialized = [graph_target, overview_path, *program_targets, *unit_targets]
    candidate_manifest = {
        "schema_version": 1,
        "kind": "retained-math-site-candidate",
        "source_registry_id": graph["registry_id"],
        "source_manifest_sha256": _sha256(source / "manifest.json"),
        "counts": graph["counts"],
        "docs_dir": docs_output.name,
        "config": config_output.name,
        "files": [
            {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": _sha256(path),
                "size_bytes": path.stat().st_size,
            }
            for path in materialized
        ],
    }
    manifest_target = data_output / "manifest.json"
    _write_once(manifest_target, _json_bytes(candidate_manifest))
    return {**candidate_manifest, "manifest_sha256": _sha256(manifest_target)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--base-docs", type=Path, required=True)
    parser.add_argument("--docs-output", type=Path, required=True)
    parser.add_argument("--data-output", type=Path, required=True)
    parser.add_argument("--config-output", type=Path, required=True)
    args = parser.parse_args()
    result = prepare(
        source=args.source.resolve(),
        base_docs=args.base_docs.resolve(),
        docs_output=args.docs_output.resolve(),
        data_output=args.data_output.resolve(),
        config_output=args.config_output.resolve(),
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
