#!/usr/bin/env python3
"""Adapt a Program 5 row-killing packet to the generic operation complex.

The expected packet exports the exact linear operator together with candidate
row-killers, proved source and target automorphism images, stable-presentation
changes, and optional obstruction functionals.  Stable-presentation changes
are represented as recharts rather than fixed-presentation gauge.

This adapter is an interface, not a Program 5 theorem: it cannot decide which
row-killing directions are genuine automorphisms or discover missing stable
presentation changes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..core import ContractError, analyze_document


def _vectors(packet: Mapping[str, Any], key: str) -> list[Any]:
    values = packet.get(key, [])
    if not isinstance(values, list):
        raise ContractError(f"Program 5 field {key!r} must be a list")
    return values


def adapt_document(packet: Mapping[str, Any]) -> dict[str, Any]:
    if packet.get("schema_version") != 1:
        raise ContractError("Program 5 adapter schema_version must equal 1")
    operator = packet.get("operator")
    if not isinstance(operator, list):
        raise ContractError("Program 5 packet requires operator rows")
    deformation_dimension = packet.get("deformation_dimension")
    if not isinstance(deformation_dimension, int):
        deformation_dimension = len(operator[0]) if operator else None
    equation_dimension = packet.get("equation_dimension")
    if not isinstance(equation_dimension, int):
        equation_dimension = len(operator)
    if not isinstance(deformation_dimension, int):
        raise ContractError("deformation_dimension is required for an empty operator")

    candidates = _vectors(packet, "candidate_row_killers")
    source = _vectors(packet, "source_automorphisms")
    target = _vectors(packet, "target_automorphisms")
    stable = _vectors(packet, "stable_presentation_changes")
    extra_gauge = packet.get("extra_gauge_spaces", [])
    if not isinstance(extra_gauge, list):
        raise ContractError("extra_gauge_spaces must be a list")

    actions: list[dict[str, Any]] = [
        {
            "name": "row_killing_candidates",
            "role": "formal",
            "generators": candidates,
        },
        {
            "name": "source_automorphisms",
            "role": "source_automorphism",
            "parent": "row_killing_candidates" if candidates else None,
            "generators": source,
        },
        {
            "name": "target_automorphisms",
            "role": "target_automorphism",
            "parent": "row_killing_candidates" if candidates else None,
            "generators": target,
        },
    ]
    gauge_actions = ["source_automorphisms", "target_automorphisms"]
    for index, space in enumerate(extra_gauge):
        if not isinstance(space, Mapping):
            raise ContractError(f"extra_gauge_spaces[{index}] must be an object")
        name = str(space.get("name", f"extra-gauge-{index}"))
        actions.append(
            {
                "name": name,
                "role": str(space.get("role", "gauge")),
                "parent": space.get("parent"),
                "generators": space.get("generators", []),
            }
        )
        gauge_actions.append(name)

    layer: dict[str, Any] = {
        "id": str(packet.get("layer_id", "program5-row-killing")),
        "deformation_dimension": deformation_dimension,
        "equation_dimension": equation_dimension,
        "deformation_basis": packet.get("deformation_basis"),
        "equation_basis": packet.get("equation_basis"),
        "operator": operator,
        "actions": actions,
        "gauge_actions": gauge_actions,
        "recharts": [
            {
                "name": "stable_presentation_changes",
                "generators": stable,
            }
        ],
        "obstruction_functionals": packet.get("obstruction_functionals", []),
        "metadata": {
            "adapter": "program5_row_killing",
            "scope": packet.get(
                "scope",
                "Exact tangent-space quotient only; nonlinear coupling is not audited.",
            ),
        },
    }
    if "forcing" in packet:
        layer["forcing"] = packet["forcing"]
    if layer["deformation_basis"] is None:
        layer.pop("deformation_basis")
    if layer["equation_basis"] is None:
        layer.pop("equation_basis")

    return {
        "schema_version": 1,
        "name": str(packet.get("name", "Program 5 row-killing quotient")),
        "field": packet.get("field", {"kind": "rational"}),
        "report_options": packet.get("report_options", {}),
        "layers": [layer],
        "transitions": packet.get("transitions", []),
    }


def analyze_packet(packet: Mapping[str, Any]) -> dict[str, Any]:
    return analyze_document(adapt_document(packet))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Program 5 row-killing packet")
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--emit-contract", type=Path)
    args = parser.parse_args(argv)
    try:
        packet = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(packet, Mapping):
            raise ContractError("top-level Program 5 packet must be an object")
        contract = adapt_document(packet)
        report = analyze_document(contract)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"program5_row_killing: {exc}", file=sys.stderr)
        return 2
    if args.emit_contract:
        args.emit_contract.parent.mkdir(parents=True, exist_ok=True)
        args.emit_contract.write_text(
            json.dumps(contract, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
