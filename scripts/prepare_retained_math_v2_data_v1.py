#!/usr/bin/env python3
"""Prepare a write-once public selection from a retained-math v2 graph."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from site_state import load_site_state


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_PATTERNS = {
    "private filesystem path": re.compile(r"(?:/fss/|/home/|file://)"),
    "conversation locator": re.compile(
        r"(?:chatgpt\.com/share|conversation_id|message_id|artifact_id)",
        re.IGNORECASE,
    ),
    "private workflow identifier": re.compile(r"(?:INTAKE-|JC-CAN-|JC-PKG-)"),
}
LEGACY_UNIT_FIELDS = (
    "unit_id",
    "unit_type",
    "title",
    "statement",
    "statement_version",
    "hypotheses",
    "exact_scope",
    "memberships",
    "relations",
    "attribution",
)


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _write_once(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(payload)


def _index(items: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    indexed = {item[key]: item for item in items}
    if len(indexed) != len(items):
        raise ValueError(f"duplicate {key} in retained-math v2 graph")
    return indexed


def _selected(
    indexed: dict[str, dict[str, Any]], ids: set[str], label: str
) -> list[dict[str, Any]]:
    missing = sorted(ids - indexed.keys())
    if missing:
        raise ValueError(f"missing selected {label}: {', '.join(missing)}")
    return [indexed[item_id] for item_id in sorted(ids)]


def _validate_legacy_units(
    selected_units: list[dict[str, Any]], legacy_graph: dict[str, Any]
) -> None:
    legacy_units = _index(legacy_graph["units"], "unit_id")
    for unit in selected_units:
        unit_id = unit["unit_id"]
        if unit_id not in legacy_units:
            raise ValueError(f"v2 selection has no v1 public unit: {unit_id}")
        legacy = legacy_units[unit_id]
        for field in LEGACY_UNIT_FIELDS:
            if unit.get(field) != legacy.get(field):
                raise ValueError(f"v2/v1 unit drift for {unit_id}: {field}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    parser.add_argument("--argument-id", required=True)
    parser.add_argument("--task-id", required=True)
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    source_manifest_path = source / "manifest.json"
    source_graph_path = source / "public-graph.json"
    source_manifest_payload = source_manifest_path.read_bytes()
    source_graph_payload = source_graph_path.read_bytes()
    source_manifest = _load(source_manifest_path)
    graph = _load(source_graph_path)
    pinned = {
        item["path"]: item for item in source_manifest.get("files", [])
    }
    graph_pin = pinned.get("public-graph.json")
    if graph_pin is None or _sha256(source_graph_payload) != graph_pin["sha256"]:
        raise ValueError("source manifest does not pin public-graph.json")
    if graph.get("registry_id") != source_manifest.get("registry_id"):
        raise ValueError("source manifest and public graph registry disagree")

    units = _index(graph["units"], "unit_id")
    arguments = _index(graph["arguments"], "argument_id")
    evidence = _index(graph["evidence"], "evidence_id")
    obligations = _index(graph["obligations"], "obligation_id")
    tasks = _index(graph["tasks"], "task_id")
    if args.argument_id not in arguments:
        raise ValueError(f"unknown argument: {args.argument_id}")
    if args.task_id not in tasks:
        raise ValueError(f"unknown task: {args.task_id}")

    argument_ids = {args.argument_id}
    pending_arguments = [args.argument_id]
    while pending_arguments:
        current = arguments[pending_arguments.pop()]
        for dependency in current.get("depends_on_argument_ids", []):
            if dependency not in argument_ids:
                argument_ids.add(dependency)
                pending_arguments.append(dependency)

    selected_arguments = _selected(arguments, argument_ids, "arguments")
    selected_task = tasks[args.task_id]
    unit_ids: set[str] = set()
    evidence_ids: set[str] = set()
    obligation_ids = set(selected_task.get("obligation_ids", []))
    for argument in selected_arguments:
        unit_ids.update(argument.get("premise_unit_ids", []))
        unit_ids.update(argument.get("conclusion_unit_ids", []))
        evidence_ids.update(argument.get("evidence_ids", []))
    for item in selected_task.get("inputs", []):
        kind = item.get("kind")
        if kind == "unit":
            unit_ids.add(item["unit_id"])
        elif kind == "argument":
            if item["argument_id"] not in argument_ids:
                raise ValueError("task references an argument outside its closure")
        elif kind == "evidence":
            evidence_ids.add(item["evidence_id"])
        else:
            raise ValueError(f"unsupported task input kind: {kind!r}")
    selected_units = _selected(units, unit_ids, "units")
    for unit in selected_units:
        obligation_ids.update(unit.get("obligation_ids", []))
    selected_evidence = _selected(evidence, evidence_ids, "evidence")
    selected_obligations = _selected(
        obligations, obligation_ids, "obligations"
    )

    state = load_site_state(ROOT)
    legacy_data = ROOT / "data" / state["retained_math"]["data_dir"]
    legacy_graph = _load(legacy_data / "public-graph.json")
    if graph.get("base_registry", {}).get("registry_id") != legacy_graph.get(
        "registry_id"
    ):
        raise ValueError("v2 graph does not extend the selected v1 registry")
    _validate_legacy_units(selected_units, legacy_graph)

    excluded_evidence_ids = sorted(
        {
            evidence_id
            for unit in selected_units
            for evidence_id in unit.get("evidence_ids", [])
            if evidence_id not in evidence_ids
        }
    )
    external_relation_unit_ids = sorted(
        {
            relation["target_unit_id"]
            for unit in selected_units
            for relation in unit.get("relations", [])
            if relation["target_unit_id"] not in unit_ids
        }
    )
    selection = {
        "schema_version": 1,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "selection_id": f"SEL-{args.argument_id}",
        "source": {
            "registry_id": graph["registry_id"],
            "source_manifest_sha256": _sha256(source_manifest_payload),
            "public_graph_sha256": _sha256(source_graph_payload),
            "base_registry": graph["base_registry"],
        },
        "selected_ids": {
            "units": sorted(unit_ids),
            "arguments": sorted(argument_ids),
            "evidence": sorted(evidence_ids),
            "obligations": sorted(obligation_ids),
            "tasks": [args.task_id],
        },
        "counts": {
            "units": len(selected_units),
            "arguments": len(selected_arguments),
            "evidence": len(selected_evidence),
            "obligations": len(selected_obligations),
            "tasks": 1,
        },
        "units": selected_units,
        "arguments": selected_arguments,
        "evidence": selected_evidence,
        "obligations": selected_obligations,
        "tasks": [selected_task],
        "references_outside_selection": {
            "unit_evidence_ids": excluded_evidence_ids,
            "relation_unit_ids": external_relation_unit_ids,
        },
    }
    selection_payload = (
        json.dumps(selection, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    ).encode("utf-8")
    text = selection_payload.decode("utf-8")
    for label, pattern in PRIVATE_PATTERNS.items():
        if pattern.search(text):
            raise ValueError(f"{label} leaked into retained-math v2 selection")

    _write_once(output / "selection.json", selection_payload)
    manifest = {
        "schema_version": 1,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "source_registry_id": graph["registry_id"],
        "source_manifest_sha256": _sha256(source_manifest_payload),
        "source_public_graph_sha256": _sha256(source_graph_payload),
        "selection_id": selection["selection_id"],
        "counts": selection["counts"],
        "files": [
            {
                "path": "selection.json",
                "sha256": _sha256(selection_payload),
                "size_bytes": len(selection_payload),
            }
        ],
    }
    manifest_payload = (
        json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    ).encode("utf-8")
    _write_once(output / "manifest.json", manifest_payload)
    print(
        json.dumps(
            {
                "output_dir": str(output),
                "release_id": args.release_id,
                "selection_id": selection["selection_id"],
                "counts": selection["counts"],
                "manifest_sha256": _sha256(manifest_payload),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
