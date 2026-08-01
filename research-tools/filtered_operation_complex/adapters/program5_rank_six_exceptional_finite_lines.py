#!/usr/bin/env python3
"""Audit the exceptional finite slopes left by the symbolic pairing ideal.

For the selected second-order-compatible plane, the generic cubic left-null
pairing is

    (r - 4) * (r^2 - 8*r + 64).

Thus the symbolic Q(r) certificate leaves only

    r = 4,  4 + 4*sqrt(-3),  4 - 4*sqrt(-3)

for specialized analysis.  This module recomputes the exact cubic tangent
system at those three ratios.  The rational point is checked over Q and the
conjugate pair over Q(sqrt(-3)).

A rank mismatch at all three points, together with the generic pairing
certificate, closes every finite algebraic slope in this selected plane.  The
point at infinity is a separate quartic-order calculation.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from .program5_compression_export import DEFAULT_SOURCE
from .program5_rank_six_schur_model import build_schur_model
from .program5_rank_six_second_order import _flatten


def _rank_over_domain(
    matrix: sp.Matrix,
    rhs: sp.Matrix,
    domain: Any,
) -> tuple[int, int]:
    matrix_domain = DomainMatrix.from_Matrix(
        matrix,
        fmt="sparse",
    ).convert_to(domain)
    augmented_domain = DomainMatrix.from_Matrix(
        matrix.row_join(rhs),
        fmt="sparse",
    ).convert_to(domain)
    return matrix_domain.rank(), augmented_domain.rank()


def _cubic_system(model: Any, ratio: sp.Expr) -> tuple[sp.Matrix, sp.Matrix]:
    theta = model.theta_v + ratio * model.theta_u
    theta_block = model.blocks(theta)
    H2 = model.quadratic_forcing(theta_block)
    residual2 = model.project(_flatten(H2))
    if any(sp.factor(sp.cancel(value)) != 0 for value in residual2):
        raise AssertionError(f"ratio {ratio} is not second-order compatible")
    P2 = model.solve_image(H2)
    cubic_residual = model.project(
        _flatten(model.cubic_forcing(theta_block, model.blocks(P2)))
    )
    tangent_blocks = [model.blocks(vector) for vector in model.tangent_basis]
    effect_columns = [
        model.project(
            _flatten(model.bilinear_effect(tangent_block, theta_block))
        )
        for tangent_block in tangent_blocks
    ]
    active_rows = sorted(
        {
            row
            for row, value in enumerate(cubic_residual)
            if sp.factor(sp.cancel(value)) != 0
        }
        | {
            row
            for column in effect_columns
            for row, value in enumerate(column)
            if sp.factor(sp.cancel(value)) != 0
        }
    )
    matrix = sp.Matrix(
        [
            [sp.factor(sp.cancel(column[row, 0])) for column in effect_columns]
            for row in active_rows
        ]
    )
    rhs = sp.Matrix(
        [-sp.factor(sp.cancel(cubic_residual[row, 0])) for row in active_rows]
    )
    return matrix, rhs


def analyze_exceptional_finite_lines(
    source_path: Path = DEFAULT_SOURCE,
) -> dict[str, Any]:
    model = build_schur_model(source_path)
    r = sp.symbols("r")
    exceptional_polynomial = sp.expand(
        (r - 4) * (r**2 - 8 * r + 64)
    )
    sqrt_minus_three = sp.sqrt(-3)
    field = sp.QQ.algebraic_field(sqrt_minus_three)
    ratios = [
        {
            "label": "r=4",
            "value": sp.Integer(4),
            "field": sp.QQ,
            "field_label": "Q",
            "minimal_factor": r - 4,
        },
        {
            "label": "r=4+4*sqrt(-3)",
            "value": 4 + 4 * sqrt_minus_three,
            "field": field,
            "field_label": "Q(sqrt(-3))",
            "minimal_factor": r**2 - 8 * r + 64,
        },
        {
            "label": "r=4-4*sqrt(-3)",
            "value": 4 - 4 * sqrt_minus_three,
            "field": field,
            "field_label": "Q(sqrt(-3))",
            "minimal_factor": r**2 - 8 * r + 64,
        },
    ]

    results = []
    for packet in ratios:
        value = packet["value"]
        if sp.factor(packet["minimal_factor"].subs(r, value)) != 0:
            raise AssertionError(f"{packet['label']} is not a root of its factor")
        matrix, rhs = _cubic_system(model, value)
        rank, augmented_rank = _rank_over_domain(
            matrix,
            rhs,
            packet["field"],
        )
        results.append(
            {
                "label": packet["label"],
                "ratio": str(value),
                "field": packet["field_label"],
                "minimal_factor": str(sp.factor(packet["minimal_factor"])),
                "compressed_cubic_equation_count": matrix.rows,
                "cubic_effect_rank": rank,
                "cubic_augmented_rank": augmented_rank,
                "cubic_lift_solvable": rank == augmented_rank,
            }
        )

    conjugate_profiles_equal = (
        results[1]["cubic_effect_rank"]
        == results[2]["cubic_effect_rank"]
        and results[1]["cubic_augmented_rank"]
        == results[2]["cubic_augmented_rank"]
    )
    all_obstructed = all(
        not item["cubic_lift_solvable"]
        for item in results
    )
    return {
        "schema_version": 1,
        "name": "Program 5 exceptional finite-slope cubic audit",
        "source_file": str(source_path),
        "source_sha256": model.source_sha256,
        "generic_pairing_polynomial": str(sp.factor(exceptional_polynomial)),
        "exceptional_ratio_count": len(results),
        "exceptional_ratios": results,
        "conjugate_rank_profiles_equal": conjugate_profiles_equal,
        "all_exceptional_finite_ratios_obstructed": all_obstructed,
        "finite_selected_plane_closed_at_cubic_order": all_obstructed,
        "interpretation_boundary": (
            "This closes the finite projective chart only for the selected "
            "second-order-compatible transverse plane. It does not classify "
            "the full 15-dimensional finite row-base fibre."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_exceptional_finite_lines(args.source)
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(
            f"program5_rank_six_exceptional_finite_lines: {exc}",
            file=sys.stderr,
        )
        return 2
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
