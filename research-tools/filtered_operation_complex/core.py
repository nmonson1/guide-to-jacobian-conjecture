#!/usr/bin/env python3
"""CLI and document-level orchestration for filtered operation complexes."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from .fields import (
    ContractError,
    NumberField,
    NumberFieldElement,
    RationalField,
    build_field,
)
from .layer import LayerAudit, parse_layer
from .linear import dot, serialize_vector, solve_affine
from .transition import audit_transition


def _audit_affine_forcing(
    audit: LayerAudit,
    *,
    field: Any,
    include_vectors: bool,
) -> None:
    """Augment one layer report with the exact equation ``D*x=-Phi``."""

    data = audit.data
    if data.forcing is None:
        return

    rhs = [-value for value in data.forcing]
    solvable, particular = solve_affine(
        data.operator,
        rhs,
        rows=data.equation_dimension,
        columns=data.deformation_dimension,
        field=field,
    )
    complete_pairings = [
        dot(functional, data.forcing, field)
        for functional in data.left_kernel_basis
    ]
    pairing_compatible = all(not value for value in complete_pairings)
    if pairing_compatible != solvable:
        raise ContractError(
            f"{data.identifier}: affine solvability disagrees with the "
            "complete left-null pairing test"
        )

    audit.result.update(
        {
            "affine_equation": "D*x=-forcing",
            "forcing_solvable": solvable,
            "forcing_compatibility_verified": True,
            "complete_left_null_forcing_pairings": [
                field.serialize(value) for value in complete_pairings
            ],
            "affine_solution_dimension": (
                len(data.kernel_basis) if solvable else None
            ),
        }
    )
    if include_vectors and particular is not None:
        audit.result["particular_solution"] = serialize_vector(
            field,
            particular,
        )


def analyze_document(document: Mapping[str, Any]) -> dict[str, Any]:
    if document.get("schema_version") != 1:
        raise ContractError("schema_version must equal 1")
    field = build_field(document.get("field"))
    report_options = document.get("report_options", {})
    if not isinstance(report_options, Mapping):
        raise ContractError("report_options must be an object")
    include_vectors = bool(report_options.get("include_vectors", False))

    raw_layers = document.get("layers")
    if not isinstance(raw_layers, list) or not raw_layers:
        raise ContractError("layers must be a nonempty list")
    audits = [
        parse_layer(field, raw, include_vectors=include_vectors)
        for raw in raw_layers
    ]
    for audit in audits:
        _audit_affine_forcing(
            audit,
            field=field,
            include_vectors=include_vectors,
        )

    by_identifier: dict[str, LayerAudit] = {}
    for audit in audits:
        if audit.data.identifier in by_identifier:
            raise ContractError(
                f"duplicate layer id {audit.data.identifier!r}"
            )
        by_identifier[audit.data.identifier] = audit

    raw_transitions = document.get("transitions", [])
    if not isinstance(raw_transitions, list):
        raise ContractError("transitions must be a list")
    transitions = [
        audit_transition(field, raw, by_identifier)
        for raw in raw_transitions
    ]

    forced_layers = [
        audit for audit in audits if audit.data.forcing is not None
    ]
    return {
        "schema_version": 1,
        "name": str(document.get("name", "filtered operation complex")),
        "field": {
            "kind": field.kind,
            **(
                {
                    "modulus": [str(value) for value in field.modulus],
                    "symbol": field.symbol,
                }
                if isinstance(field, NumberField)
                else {}
            ),
        },
        "layers": [audit.result for audit in audits],
        "transitions": transitions,
        "all_true_quotients_zero": all(
            audit.result["unexplained_dimension"] == 0
            for audit in audits
        ),
        "all_transitions_verified": all(
            transition["chain_map_verified"] for transition in transitions
        ),
        "all_forcing_equations_solvable": (
            all(audit.result["forcing_solvable"] for audit in forced_layers)
            if forced_layers
            else None
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        type=Path,
        help="filtered-operation JSON contract",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="write report as JSON",
    )
    args = parser.parse_args(argv)
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(document, Mapping):
            raise ContractError("top-level JSON value must be an object")
        report = analyze_document(document)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"filtered_operation_complex: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
