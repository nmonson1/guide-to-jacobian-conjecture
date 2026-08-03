#!/usr/bin/env python3
"""Validation helpers for the public retained-math v2 site contract."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

OBJECTS = (
    ("programs", "slug"),
    ("units", "unit_id"),
    ("arguments", "argument_id"),
    ("evidence", "evidence_id"),
    ("obligations", "obligation_id"),
    ("tasks", "task_id"),
)
COMPATIBILITY_DISPOSITIONS = {
    "exact_current",
    "valid_weaker",
    "replacement",
    "split_replacement",
    "archival",
}
FORWARD_RELATIONS = {"corrects", "strengthens", "supersedes"}
INTERNAL_KEYS = {
    "admission",
    "audit_current",
    "collision_check",
    "dependency_closure_sha256",
    "novelty_claim",
    "provenance",
    "publication",
    "receipt_id",
    "review_state",
    "verification",
}
PRIVATE_PATTERNS = {
    "private filesystem path": re.compile(r"(?:/fss/|/home/|file://)"),
    "conversation locator": re.compile(
        r"(?:chatgpt\.com/share|conversation_id|message_id|artifact_id)",
        re.IGNORECASE,
    ),
    "private workflow identifier": re.compile(r"(?:INTAKE-|JC-CAN-|JC-PKG-)"),
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _index(
    items: list[dict[str, Any]], key: str, *, label: str
) -> dict[str, dict[str, Any]]:
    try:
        indexed = {item[key]: item for item in items}
    except (KeyError, TypeError) as exc:
        raise ValueError(f"malformed {label} collection") from exc
    if len(indexed) != len(items):
        raise ValueError(f"duplicate {key} in retained-math v2 {label}")
    return indexed


def _walk(value: Any, *, path: str = "<root>") -> Iterable[tuple[str, Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from _walk(child, path=f"{path}/{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk(child, path=f"{path}/{index}")


def validate_public_v2_graph(graph: dict[str, Any]) -> dict[str, int]:
    """Validate the privacy-pruned, research-facing v2 materialization."""
    if graph.get("schema_version") != 2:
        raise ValueError("retained-math v2 public graph has wrong schema version")
    registry_id = graph.get("registry_id")
    if not isinstance(registry_id, str) or not registry_id.startswith("RETAINED2-"):
        raise ValueError("retained-math v2 public graph has invalid registry ID")

    indexes: dict[str, dict[str, dict[str, Any]]] = {}
    counts: dict[str, int] = {}
    for plural, key in OBJECTS:
        items = graph.get(plural)
        if not isinstance(items, list):
            raise ValueError(f"retained-math v2 public graph lacks {plural}")
        indexes[plural] = _index(items, key, label=plural)
        counts[plural] = len(items)
    if graph.get("counts") != counts:
        raise ValueError("retained-math v2 public graph counts disagree")

    rendered = json.dumps(graph, ensure_ascii=False, sort_keys=True)
    for label, pattern in PRIVATE_PATTERNS.items():
        if pattern.search(rendered):
            raise ValueError(f"{label} leaked into retained-math v2 public graph")
    for object_path, value in _walk(graph):
        if isinstance(value, dict):
            if value.get("kind") == "private_source":
                raise ValueError(
                    f"private source locator leaked at {object_path}"
                )
            leaked = sorted(INTERNAL_KEYS & value.keys())
            if leaked:
                raise ValueError(
                    f"internal workflow fields leaked at {object_path}: {leaked}"
                )

    unit_ids = set(indexes["units"])
    argument_ids = set(indexes["arguments"])
    evidence_ids = set(indexes["evidence"])
    obligation_ids = set(indexes["obligations"])
    program_ids = set(indexes["programs"])
    for unit_id, unit in indexes["units"].items():
        unknown_programs = set(unit["memberships"]["programs"]) - program_ids
        if unknown_programs:
            raise ValueError(f"{unit_id}: unknown program memberships")
        for field, known in (
            ("argument_ids", argument_ids),
            ("evidence_ids", evidence_ids),
            ("obligation_ids", obligation_ids),
        ):
            unknown = set(unit.get(field, [])) - known
            if unknown:
                raise ValueError(f"{unit_id}: unresolved {field} {sorted(unknown)}")
    for argument_id, argument in indexes["arguments"].items():
        unknown_conclusions = set(argument["conclusion_unit_ids"]) - unit_ids
        unknown_evidence = set(argument["evidence_ids"]) - evidence_ids
        unknown_dependencies = (
            set(argument["depends_on_argument_ids"]) - argument_ids
        )
        if unknown_conclusions or unknown_evidence or unknown_dependencies:
            raise ValueError(f"{argument_id}: unresolved public graph edge")
    for evidence_id, evidence in indexes["evidence"].items():
        if not evidence["target_unit_ids"] and not evidence["target_argument_ids"]:
            raise ValueError(f"{evidence_id}: evidence has no target")
        if set(evidence["target_argument_ids"]) - argument_ids:
            raise ValueError(f"{evidence_id}: unresolved argument target")
    return counts


def validate_legacy_compatibility(
    compatibility: dict[str, Any],
    *,
    graph: dict[str, Any],
    expected_legacy_ids: set[str],
    schema_path: Path | None = None,
) -> dict[str, int]:
    """Validate total stable-route coverage and forward target semantics."""
    if schema_path is not None:
        try:
            from jsonschema import Draft202012Validator
        except ImportError as exc:
            raise ValueError(
                "jsonschema is required to validate a full compatibility map"
            ) from exc
        schema = load_json(schema_path)
        errors = sorted(
            Draft202012Validator(schema).iter_errors(compatibility),
            key=lambda error: list(error.path),
        )
        if errors:
            rendered = "; ".join(
                f"{'/'.join(str(part) for part in error.path) or '<root>'}: "
                f"{error.message}"
                for error in errors
            )
            raise ValueError(f"legacy compatibility schema failure: {rendered}")

    if compatibility.get("source_registry", {}).get("registry_id") != graph.get(
        "registry_id"
    ):
        raise ValueError("legacy compatibility map targets the wrong v2 registry")
    routes = compatibility.get("routes")
    if not isinstance(routes, list):
        raise ValueError("legacy compatibility map lacks routes")
    indexed = _index(routes, "legacy_unit_id", label="compatibility routes")
    found = set(indexed)
    if found != expected_legacy_ids:
        missing = sorted(expected_legacy_ids - found)
        extra = sorted(found - expected_legacy_ids)
        raise ValueError(
            f"legacy compatibility map is not total: missing={missing}, extra={extra}"
        )
    units = _index(graph["units"], "unit_id", label="units")

    for legacy_id, route in indexed.items():
        disposition = route.get("disposition")
        targets = route.get("targets")
        if disposition not in COMPATIBILITY_DISPOSITIONS or not isinstance(
            targets, list
        ):
            raise ValueError(f"{legacy_id}: invalid compatibility disposition")
        if route.get("route") != f"claims/{legacy_id}/":
            raise ValueError(f"{legacy_id}: unstable compatibility route")
        roles = [target.get("role") for target in targets]
        if disposition == "archival":
            if targets:
                raise ValueError(f"{legacy_id}: archival route has targets")
            continue
        if not targets:
            raise ValueError(f"{legacy_id}: current route has no target")
        target_ids = [target.get("unit_id") for target in targets]
        if len(target_ids) != len(set(target_ids)):
            raise ValueError(f"{legacy_id}: duplicate compatibility target")
        if disposition == "exact_current" and roles != ["current_statement"]:
            raise ValueError(f"{legacy_id}: malformed exact-current targets")
        if disposition == "valid_weaker" and (
            not roles
            or roles[0] != "current_statement"
            or any(role != "stronger_result" for role in roles[1:])
            or len(roles) < 2
        ):
            raise ValueError(f"{legacy_id}: malformed valid-weaker targets")
        if disposition == "replacement" and roles != ["replacement"]:
            raise ValueError(f"{legacy_id}: malformed replacement targets")
        if disposition == "split_replacement" and (
            len(roles) < 2 or any(role != "replacement" for role in roles)
        ):
            raise ValueError(f"{legacy_id}: malformed split replacement targets")

        for target in targets:
            unit_id = target.get("unit_id")
            if unit_id not in units:
                raise ValueError(f"{legacy_id}: unknown current target {unit_id}")
            unit = units[unit_id]
            if target.get("statement_version") != unit.get("statement_version"):
                raise ValueError(f"{legacy_id}: stale statement version for {unit_id}")
            role = target["role"]
            if role == "current_statement":
                if unit_id != legacy_id:
                    raise ValueError(
                        f"{legacy_id}: current statement changes stable ID"
                    )
                if "relation_type" in target:
                    raise ValueError(
                        f"{legacy_id}: current statement has a forward relation"
                    )
            if role == "stronger_result":
                expected_relation = "strengthens"
            elif role == "replacement":
                expected_relation = target.get("relation_type")
                if expected_relation not in {"corrects", "supersedes"}:
                    raise ValueError(f"{legacy_id}: replacement is not forward")
            else:
                continue
            if target.get("relation_type") != expected_relation:
                raise ValueError(f"{legacy_id}: incompatible forward relation")
            if not any(
                relation.get("relation_type") == expected_relation
                and relation.get("target_unit_id") == legacy_id
                for relation in unit.get("relations", [])
            ):
                raise ValueError(
                    f"{legacy_id}: target {unit_id} lacks its forward relation edge"
                )

    measured = Counter(route["disposition"] for route in routes)
    expected_counts = {"routes": len(routes), **dict(sorted(measured.items()))}
    if compatibility.get("counts") != expected_counts:
        raise ValueError("legacy compatibility counts do not match routes")
    return expected_counts


def compatibility_by_id(
    compatibility: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    return _index(
        compatibility["routes"],
        "legacy_unit_id",
        label="compatibility routes",
    )
