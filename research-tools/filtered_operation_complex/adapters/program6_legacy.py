#!/usr/bin/env python3
"""Adapt the original Program 6 chart-correspondence JSON contract.

The legacy contract has one operator together with ``gauge_vectors`` and
``rechart_vectors`` per layer.  This adapter interprets the supplied gauge
vectors as the declared filtered fixed-chart operation space and the supplied
rechart vectors as adjacent-presentation directions.  It does not infer the
formal, polynomial, or approximate-root subgroup hierarchy.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..core import ContractError, analyze_document


def transport_support(k: int, monomials: Sequence[Sequence[int]]) -> list[list[int]]:
    transported: set[tuple[int, int]] = set()
    for monomial in monomials:
        if len(monomial) != 2:
            raise ContractError(f"invalid Program 6 monomial {monomial!r}")
        i, j = monomial
        if not isinstance(i, int) or not isinstance(j, int) or j < 0:
            raise ContractError("Program 6 support exponents must be integers with j>=0")
        for t in range(j + 1):
            transported.add((i - k * t, j - t))
    return [
        [i, j]
        for i, j in sorted(transported, key=lambda pair: (-pair[1], pair[0]))
    ]


def adapt_document(legacy: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    if legacy.get("schema_version") != 1:
        raise ContractError("legacy Program 6 schema_version must equal 1")
    raw_layers = legacy.get("layers")
    if not isinstance(raw_layers, list) or not raw_layers:
        raise ContractError("legacy Program 6 contract has no layers")

    layers: list[dict[str, Any]] = []
    support_closures: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_layers):
        if not isinstance(raw, Mapping):
            raise ContractError(f"legacy layer {index} is not an object")
        identifier = str(raw.get("label", raw.get("r", f"layer-{index}")))
        operator = raw.get("operator")
        if not isinstance(operator, list):
            raise ContractError(f"{identifier}: operator must be a list")
        deformation_dimension = len(operator[0]) if operator else raw.get("ambient_dimension")
        if not isinstance(deformation_dimension, int):
            raise ContractError(
                f"{identifier}: ambient_dimension is required for an empty operator"
            )
        gauge_vectors = raw.get("gauge_vectors", [])
        rechart_vectors = raw.get("rechart_vectors", [])
        if not isinstance(gauge_vectors, list) or not isinstance(rechart_vectors, list):
            raise ContractError(f"{identifier}: legacy vectors must be lists")
        layer = {
            "id": identifier,
            "deformation_dimension": deformation_dimension,
            "equation_dimension": len(operator),
            "operator": operator,
            "actions": [
                {
                    "name": "filtered_fixed_chart",
                    "role": "filtered",
                    "generators": gauge_vectors,
                }
            ],
            "gauge_actions": ["filtered_fixed_chart"],
            "recharts": [
                {
                    "name": "adjacent_chart_tangents",
                    "generators": rechart_vectors,
                }
            ],
            "metadata": {
                "legacy_label": identifier,
                "legacy_contract": True,
            },
        }
        layers.append(layer)

        support = raw.get("support_transport")
        if support is not None:
            if not isinstance(support, Mapping):
                raise ContractError(f"{identifier}: support_transport must be an object")
            k = support.get("k")
            monomials = support.get("monomials")
            if not isinstance(k, int) or not isinstance(monomials, list):
                raise ContractError(
                    f"{identifier}: support_transport requires integer k and monomials"
                )
            support_closures.append(
                {
                    "layer": identifier,
                    "k": k,
                    "input": monomials,
                    "closure": transport_support(k, monomials),
                }
            )

    contract = {
        "schema_version": 1,
        "name": f"Program 6 adapter: {legacy.get('name', 'legacy chart contract')}",
        "field": {"kind": "rational"},
        "layers": layers,
        "transitions": [],
    }
    adapter_metadata = {
        "adapter": "program6_legacy",
        "limitations": [
            "The legacy gauge vectors are treated as the declared filtered subgroup.",
            "The adapter does not discover adjacent charts or the approximate-root subgroup.",
            *[str(value) for value in legacy.get("limitations", [])],
        ],
        "support_closures": support_closures,
    }
    return contract, adapter_metadata


def analyze_legacy_document(legacy: Mapping[str, Any]) -> dict[str, Any]:
    contract, metadata = adapt_document(legacy)
    report = analyze_document(contract)
    report["adapter_metadata"] = metadata
    return report


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="legacy Program 6 JSON contract")
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument(
        "--emit-contract",
        type=Path,
        help="also write the converted generic contract",
    )
    args = parser.parse_args(argv)
    try:
        legacy = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(legacy, Mapping):
            raise ContractError("top-level legacy value must be an object")
        contract, metadata = adapt_document(legacy)
        report = analyze_document(contract)
        report["adapter_metadata"] = metadata
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"program6_legacy: {exc}", file=sys.stderr)
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
