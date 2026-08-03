#!/usr/bin/env python3
"""Prepare a write-once public selection from a retained-math v2 graph."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from retained_math_v2_public import (
    load_json,
    validate_legacy_compatibility,
    validate_public_v2_graph,
)
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


def _prepare_full_materialization(
    *,
    graph: dict[str, Any],
    graph_payload: bytes,
    source_manifest_payload: bytes,
    compatibility_path: Path,
    legacy_claim_graph_path: Path,
    output: Path,
    release_id: str,
    updated_at: str,
) -> dict[str, Any]:
    """Write a pinned, complete public v2 graph and total route map."""
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    graph_counts = validate_public_v2_graph(graph)
    compatibility = load_json(compatibility_path)
    compatibility_payload = compatibility_path.read_bytes()
    claim_graph = load_json(legacy_claim_graph_path)
    legacy_ids = {
        item["tag"] for item in claim_graph.get("claims", [])
    }
    if len(legacy_ids) != len(claim_graph.get("claims", [])):
        raise ValueError("legacy public claim graph has duplicate stable tags")
    compatibility_counts = validate_legacy_compatibility(
        compatibility,
        graph=graph,
        expected_legacy_ids=legacy_ids,
        schema_path=ROOT / "schemas/legacy-compatibility-v1.schema.json",
    )

    files = []
    for relative, payload in (
        ("public-graph.json", graph_payload),
        ("legacy-compatibility.json", compatibility_payload),
    ):
        _write_once(output / relative, payload)
        files.append(
            {
                "path": relative,
                "sha256": _sha256(payload),
                "size_bytes": len(payload),
            }
        )
    manifest = {
        "schema_version": 2,
        "kind": "retained-math-v2-full-public",
        "release_id": release_id,
        "updated_at": updated_at,
        "source_registry_id": graph["registry_id"],
        "source_manifest_sha256": _sha256(source_manifest_payload),
        "source_public_graph_sha256": _sha256(graph_payload),
        "source_compatibility_sha256": _sha256(compatibility_payload),
        "compatibility_map_id": compatibility["map_id"],
        "graph_counts": graph_counts,
        "compatibility_counts": compatibility_counts,
        "files": files,
    }
    manifest_payload = (
        json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    ).encode("utf-8")
    _write_once(output / "manifest.json", manifest_payload)
    return {
        "output_dir": str(output),
        "release_id": release_id,
        "registry_id": graph["registry_id"],
        "compatibility_map_id": compatibility["map_id"],
        "graph_counts": graph_counts,
        "compatibility_counts": compatibility_counts,
        "manifest_sha256": _sha256(manifest_payload),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    parser.add_argument("--argument-id")
    parser.add_argument("--task-id")
    parser.add_argument(
        "--compatibility-map",
        type=Path,
        help=(
            "Build a full materialization using this total legacy-route map; "
            "omit to retain the bounded pilot-selection mode"
        ),
    )
    parser.add_argument(
        "--legacy-claim-graph",
        type=Path,
        help=(
            "Claim graph whose stable tags define compatibility totality; "
            "defaults to the release selected by site-state.json"
        ),
    )
    parser.add_argument(
        "--base-v1-source",
        type=Path,
        help=(
            "Public v1 graph used to validate the selection; defaults to the "
            "v1 release selected by site-state.json"
        ),
    )
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

    if args.compatibility_map is not None:
        if args.argument_id is not None or args.task_id is not None:
            raise ValueError(
                "full materialization cannot also select one argument or task"
            )
        if args.legacy_claim_graph is None:
            state = load_site_state(ROOT)
            legacy_claim_graph_path = (
                ROOT
                / "data"
                / state["claim_graph"]["data_dir"]
                / "claim-graph.json"
            )
        else:
            legacy_claim_graph_path = args.legacy_claim_graph.resolve()
        result = _prepare_full_materialization(
            graph=graph,
            graph_payload=source_graph_payload,
            source_manifest_payload=source_manifest_payload,
            compatibility_path=args.compatibility_map.resolve(),
            legacy_claim_graph_path=legacy_claim_graph_path,
            output=output,
            release_id=args.release_id,
            updated_at=args.updated_at,
        )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    if args.argument_id is None or args.task_id is None:
        raise ValueError(
            "pilot-selection mode requires both --argument-id and --task-id"
        )

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

    if args.base_v1_source is None:
        state = load_site_state(ROOT)
        legacy_data = ROOT / "data" / state["retained_math"]["data_dir"]
    else:
        legacy_data = args.base_v1_source.resolve()
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
