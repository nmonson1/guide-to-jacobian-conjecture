#!/usr/bin/env python3
"""Compare natural source-operation subgroups in the degree-21 lower face.

The full support-admissible weighted-divergence space is larger than the
valuation-filtered approximate-root subgroup.  This program inserts one
canonical intermediate condition: the infinitesimal source field must be
polynomial in the original affine coordinates

    x = X^(-1),   y = Y,   z = X Y^2 = y^2/x.

For ``f=z^k`` and

    g=-(k+2)/(r-5) z^(k-1),

the corresponding field is

    V_{r,k}
      = -(2k+r-1)/(r-5) x^(2-k) y^(2k+r-2) partial_x
        -(k+2)/(r-5)    x^(1-k) y^(2k+r-1) partial_y.

Polynomiality is therefore an exact combinatorial condition on ``(r,k)``, with
zero components treated separately.  Arbitrary linear combinations of the
allowed monomials are then subjected to the same exact outside-window
constraints as the full Laurent calculation.

The resulting affine-polynomial subgroup is still not asserted to equal the
complete-chain approximate-root subgroup.  Comparing its rank with the
manuscript's recorded residual dimensions isolates the remaining filtered
realization gap.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from degree21_lower_face_full_gauge import (
    exact_source_bounds,
    independent_extension,
    linear_combination,
    source_column,
)
from degree21_lower_face_replay import (
    FieldElement,
    Matrix,
    Poly,
    QuinticField,
    Vector,
    columns_to_matrix,
    determinant_layer,
    face_equation,
    independent_columns,
    load_full_layers,
    matrix_rank,
    monomial,
    nullspace,
    output_vector,
    parse_face,
    theta,
    vector_image,
)


def affine_polynomial_exponent(r: int, k: int) -> bool:
    if r == 5:
        raise ValueError("r=5 requires a separate divergence parametrization")

    x_numerator = 2 * k + r - 1
    y_numerator = k + 2
    if x_numerator != 0 and (2 - k < 0 or 2 * k + r - 2 < 0):
        return False
    if y_numerator != 0 and (1 - k < 0 or 2 * k + r - 1 < 0):
        return False
    return True


def fixed_boundary_shear_exponent(r: int, k: int) -> bool:
    """The monomial field is an x-Laurent triangular shear h(x) partial_y."""
    return 2 * k + r - 1 == 0


def determinant_operator(
    field: QuinticField,
    r: int,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    a_support: Sequence[int],
    b_support: Sequence[int],
) -> tuple[Matrix, list[int]]:
    columns: list[Poly] = []
    for exponent in a_support:
        columns.append(
            determinant_layer(field, r, A0, B0, monomial(field, exponent), {})
        )
    for exponent in b_support:
        columns.append(
            determinant_layer(field, r, A0, B0, {}, monomial(field, exponent))
        )
    target_exponents = sorted(
        {exponent for column in columns for exponent in column}
    )
    return columns_to_matrix(field, columns, target_exponents), target_exponents


def subgroup_image(
    field: QuinticField,
    r: int,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    a_support: Sequence[int],
    b_support: Sequence[int],
    operator: Matrix,
    source_exponents: Sequence[int],
) -> dict[str, Any]:
    allowed_a = set(a_support)
    allowed_b = set(b_support)
    a_columns: list[Poly] = []
    b_columns: list[Poly] = []
    individually_supported: list[int] = []
    for k in source_exponents:
        a, b = source_column(field, r, k, A0, B0)
        a_columns.append(a)
        b_columns.append(b)
        if all(exponent in allowed_a for exponent in a) and all(
            exponent in allowed_b for exponent in b
        ):
            individually_supported.append(k)

    forbidden_a = sorted(
        {
            exponent
            for column in a_columns
            for exponent in column
            if exponent not in allowed_a
        }
    )
    forbidden_b = sorted(
        {
            exponent
            for column in b_columns
            for exponent in column
            if exponent not in allowed_b
        }
    )
    constraint_matrix: Matrix = []
    for exponent in forbidden_a:
        constraint_matrix.append(
            [column.get(exponent, field.zero) for column in a_columns]
        )
    for exponent in forbidden_b:
        constraint_matrix.append(
            [column.get(exponent, field.zero) for column in b_columns]
        )
    source_basis = nullspace(
        constraint_matrix,
        columns=len(source_exponents),
        field=field,
    )

    ambient_dimension = len(a_support) + len(b_support)
    gauge_candidates: list[Vector] = []
    for source_vector in source_basis:
        a = linear_combination(field, a_columns, source_vector)
        b = linear_combination(field, b_columns, source_vector)
        output = output_vector(field, a, b, a_support, b_support)
        if any(vector_image(operator, output, field)):
            raise AssertionError(f"layer {r}: subgroup image is not in ker D_r")
        gauge_candidates.append(output)
    gauge_basis = independent_columns(field, gauge_candidates, ambient_dimension)
    return {
        "candidate_exponents": list(source_exponents),
        "individually_supported_exponents": individually_supported,
        "support_admissible_source_dimension": len(source_basis),
        "source_stabilizer_dimension": len(source_basis) - len(gauge_basis),
        "gauge_dimension": len(gauge_basis),
    }


def analyze_layer(
    field: QuinticField,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    layer: Mapping[str, Any],
    manuscript_residual: int,
) -> dict[str, Any]:
    r = int(layer["r"])
    a_support = list(layer["a_support"])
    b_support = list(layer["b_support"])
    ambient_dimension = len(a_support) + len(b_support)
    operator, target_exponents = determinant_operator(
        field, r, A0, B0, a_support, b_support
    )
    kernel_dimension = ambient_dimension - matrix_rank(
        operator, columns=ambient_dimension, field=field
    )

    lower, upper, _, _ = exact_source_bounds(r, a_support, b_support)
    formal_exponents = list(range(lower, upper + 1))
    polynomial_exponents = [
        k for k in formal_exponents if affine_polynomial_exponent(r, k)
    ]
    boundary_shear_exponents = [
        k for k in formal_exponents if fixed_boundary_shear_exponent(r, k)
    ]

    formal = subgroup_image(
        field,
        r,
        A0,
        B0,
        a_support,
        b_support,
        operator,
        formal_exponents,
    )
    polynomial = subgroup_image(
        field,
        r,
        A0,
        B0,
        a_support,
        b_support,
        operator,
        polynomial_exponents,
    )
    boundary_shears = subgroup_image(
        field,
        r,
        A0,
        B0,
        a_support,
        b_support,
        operator,
        boundary_shear_exponents,
    )

    manuscript_gauge = kernel_dimension - manuscript_residual
    return {
        "r": r,
        "kernel_dimension": kernel_dimension,
        "target_dimension": len(target_exponents),
        "formal_laurent": formal,
        "affine_polynomial": polynomial,
        "fixed_boundary_shears": boundary_shears,
        "manuscript_recorded_residual_dimension": manuscript_residual,
        "manuscript_inferred_gauge_dimension": manuscript_gauge,
        "polynomial_minus_manuscript_rank": (
            polynomial["gauge_dimension"] - manuscript_gauge
        ),
    }


def analyze(face_path: Path, support_path: Path) -> dict[str, Any]:
    field, A0, B0 = parse_face(face_path)
    if face_equation(field, A0, B0) != {2: field.one}:
        raise ValueError("the reconstructed leading face does not satisfy Psi=z^2")
    recorded_residuals = [1, 2, 1, 1]
    layers = load_full_layers(support_path, [1, 2, 3, 4])
    results = [
        analyze_layer(field, A0, B0, layer, residual)
        for layer, residual in zip(layers, recorded_residuals)
    ]
    return {
        "schema_version": 1,
        "name": "degree-21 source-subgroup ladder",
        "coordinate_change": "x=X^(-1), y=Y, z=XY^2=y^2/x",
        "scope": (
            "The manuscript residual sequence is recorded input for comparison, "
            "not independently proved by this report."
        ),
        "layers": results,
        "kernel_sequence": [item["kernel_dimension"] for item in results],
        "formal_gauge_sequence": [
            item["formal_laurent"]["gauge_dimension"] for item in results
        ],
        "affine_polynomial_gauge_sequence": [
            item["affine_polynomial"]["gauge_dimension"] for item in results
        ],
        "fixed_boundary_shear_gauge_sequence": [
            item["fixed_boundary_shears"]["gauge_dimension"] for item in results
        ],
        "manuscript_inferred_gauge_sequence": [
            item["manuscript_inferred_gauge_dimension"] for item in results
        ],
        "remaining_polynomial_rank_excess": [
            item["polynomial_minus_manuscript_rank"] for item in results
        ],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("face", type=Path)
    parser.add_argument("supports", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    try:
        report = analyze(args.face, args.supports)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"degree21_subgroup_ladder: {exc}", file=sys.stderr)
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
