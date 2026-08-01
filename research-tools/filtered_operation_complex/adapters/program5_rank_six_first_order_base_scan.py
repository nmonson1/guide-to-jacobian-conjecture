#!/usr/bin/env python3
"""Probe the full first-order row-base freedom at cubic order.

The previously audited two-plane is a section of the quadratic Kuranishi
locus, not the whole locus.  For finite slope r=u/v, v=1, the displayed six
quadratic equations reduce to

    s3 = 0,  s4 = r-4,  s5 = 0,
    s1 = -24,
    3*s0 + 2*s2 - 12*s19 = 12,

with thirteen further row-zero coordinates free.  Relative to the chosen
section this gives the fifteen homogeneous row directions

    xi_2 - (2/3) xi_0,
    xi_19 + 4 xi_0,
    xi_6, ..., xi_18.

At the point at infinity v=0, u=1, every row direction except xi_3 and xi_4
is first-order quadratic-compatible.  This adapter tests coordinate and a few
deterministic mixed points in those row-base fibres.  For each direction it
allows the complete 22-dimensional tangent freedom in the quadratic
correction before testing the cubic equations.

The scan is exploratory.  A finite sample does not classify either fibre.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from .program5_compression_export import DEFAULT_SOURCE, _q
from .program5_rank_six_schur_model import build_schur_model
from .program5_rank_six_second_order import _flatten


def _rank_pair(matrix: sp.Matrix, rhs: sp.Matrix) -> tuple[int, int]:
    return (
        DomainMatrix.from_Matrix(matrix, fmt="sparse").rank(),
        DomainMatrix.from_Matrix(
            matrix.row_join(rhs),
            fmt="sparse",
        ).rank(),
    )


def analyze_first_order_base_scan(
    source_path: Path = DEFAULT_SOURCE,
) -> dict[str, Any]:
    model = build_schur_model(source_path)
    tangent_blocks = [model.blocks(vector) for vector in model.tangent_basis]

    def analyze_direction(
        name: str,
        theta: sp.Matrix,
        metadata: dict[str, Any],
    ) -> dict[str, Any]:
        theta_block = model.blocks(theta)
        H2 = model.quadratic_forcing(theta_block)
        residual2 = model.project(_flatten(H2))
        compatible2 = not any(value != 0 for value in residual2)
        result: dict[str, Any] = {
            "name": name,
            **metadata,
            "second_order_compatible": compatible2,
        }
        if not compatible2:
            result["second_order_residual_rank"] = DomainMatrix.from_Matrix(
                residual2,
                fmt="sparse",
            ).rank()
            return result

        P2 = model.solve_image(H2)
        cubic_residual = model.project(
            _flatten(model.cubic_forcing(theta_block, model.blocks(P2)))
        )
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
                if value != 0
            }
            | {
                row
                for column in effect_columns
                for row, value in enumerate(column)
                if value != 0
            }
        )
        matrix = sp.Matrix(
            [
                [column[row, 0] for column in effect_columns]
                for row in active_rows
            ]
        )
        rhs = sp.Matrix([-cubic_residual[row, 0] for row in active_rows])
        rank, augmented_rank = _rank_pair(matrix, rhs)
        result.update(
            {
                "compressed_cubic_equation_count": len(active_rows),
                "cubic_effect_rank": rank,
                "cubic_augmented_rank": augmented_rank,
                "cubic_lift_solvable": rank == augmented_rank,
                "cubic_solution_free_dimension": (
                    matrix.cols - rank if rank == augmented_rank else None
                ),
            }
        )
        return result

    row = model.row_basis
    finite_fibre_basis: list[tuple[str, sp.Matrix]] = [
        ("rho_s2", row[2] - sp.Rational(2, 3) * row[0]),
        ("rho_s19", row[19] + 4 * row[0]),
    ] + [(f"xi_{index}", row[index]) for index in range(6, 19)]
    infinity_fibre_basis = [
        (f"xi_{index}", row[index])
        for index in range(20)
        if index not in (3, 4)
    ]

    samples: list[tuple[str, sp.Matrix, dict[str, Any]]] = []
    for ratio in (sp.Rational(0), sp.Rational(1)):
        base = model.theta_v + ratio * model.theta_u
        samples.append(
            (
                f"finite:r={ratio}:base",
                base,
                {
                    "chart": "finite",
                    "u_over_v": _q(ratio),
                    "row_adjustments": [],
                },
            )
        )
        if ratio == 0:
            for basis_name, basis_vector in finite_fibre_basis:
                samples.append(
                    (
                        f"finite:r=0:+{basis_name}",
                        base + basis_vector,
                        {
                            "chart": "finite",
                            "u_over_v": 0,
                            "row_adjustments": [
                                {"name": basis_name, "coefficient": 1}
                            ],
                        },
                    )
                )
            all_sum = sp.zeros(model.ambient_operation_dimension, 1)
            alternating = sp.zeros(model.ambient_operation_dimension, 1)
            for index, (_, basis_vector) in enumerate(finite_fibre_basis):
                all_sum += basis_vector
                alternating += (-1) ** index * basis_vector
            samples.extend(
                [
                    (
                        "finite:r=0:all-plus-one",
                        base + all_sum,
                        {
                            "chart": "finite",
                            "u_over_v": 0,
                            "row_adjustments": [
                                {"name": name, "coefficient": 1}
                                for name, _ in finite_fibre_basis
                            ],
                        },
                    ),
                    (
                        "finite:r=0:alternating",
                        base + alternating,
                        {
                            "chart": "finite",
                            "u_over_v": 0,
                            "row_adjustments": [
                                {
                                    "name": name,
                                    "coefficient": (-1) ** index,
                                }
                                for index, (name, _) in enumerate(
                                    finite_fibre_basis
                                )
                            ],
                        },
                    ),
                ]
            )

    infinity_base = model.theta_u
    samples.append(
        (
            "infinity:base",
            infinity_base,
            {
                "chart": "infinity",
                "u_over_v": "infinity",
                "row_adjustments": [],
            },
        )
    )
    for basis_name, basis_vector in infinity_fibre_basis:
        samples.append(
            (
                f"infinity:+{basis_name}",
                infinity_base + basis_vector,
                {
                    "chart": "infinity",
                    "u_over_v": "infinity",
                    "row_adjustments": [
                        {"name": basis_name, "coefficient": 1}
                    ],
                },
            )
        )

    results = [
        analyze_direction(name, theta, metadata)
        for name, theta, metadata in samples
    ]
    compatible = [item for item in results if item["second_order_compatible"]]
    cubic_solvable = [
        item
        for item in compatible
        if item.get("cubic_lift_solvable")
    ]
    return {
        "schema_version": 1,
        "name": "Program 5 first-order row-base cubic scan",
        "source_file": str(source_path),
        "source_sha256": model.source_sha256,
        "ambient_operation_dimension": model.ambient_operation_dimension,
        "rank_six_tangent_dimension": len(model.tangent_basis),
        "finite_fibre_basis": [name for name, _ in finite_fibre_basis],
        "finite_fibre_dimension": len(finite_fibre_basis),
        "infinity_fibre_basis": [name for name, _ in infinity_fibre_basis],
        "infinity_fibre_dimension": len(infinity_fibre_basis),
        "sample_count": len(results),
        "second_order_compatible_count": len(compatible),
        "cubic_solvable_count": len(cubic_solvable),
        "cubic_solvable_samples": [item["name"] for item in cubic_solvable],
        "samples": results,
        "interpretation_boundary": (
            "This finite coordinate scan only tests selected points of the "
            "15- and 18-dimensional first-order row-base fibres. A solvable "
            "sample supplies a branch candidate; absence of one is not a "
            "classification theorem."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_first_order_base_scan(args.source)
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(f"program5_rank_six_first_order_base_scan: {exc}", file=sys.stderr)
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
