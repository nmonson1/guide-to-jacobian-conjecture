#!/usr/bin/env python3
"""Compute the full support-admissible Laurent fixed-chart gauge space.

This refines ``degree21_lower_face_replay.py``.  Instead of retaining only
individual Laurent monomials whose images already fit the Newton windows, it
allows arbitrary finite Laurent combinations and imposes all outside-window
coefficient equations simultaneously over the exact quintic field.

For ``r != 5`` and ``Psi=z^2``, weighted divergence determines

    g = -(f' + 2f/z)/(r-5).

The coefficient search is finite for the degree-21 face.  If ``k`` is the
lowest exponent of ``f``, the lowest coefficients of the two components of
``Theta_r`` are proportional to

    2k+r-1,       3k+2r-4.

They vanish simultaneously only at ``r=5``.  If ``k`` is the highest exponent,
the two top coefficients are both proportional to

    k+4r-18.

Consequently, for ``r != 5`` every support-admissible source field is contained
in the finite exponent interval computed below, including the one exceptional
top-cancellation exponent ``18-4r``.

This program computes the largest weighted-divergence-free Laurent source
space whose linearized action lies in the archived coefficient windows.  A
smaller fixed-chart automorphism group may impose additional integrability,
normalization, or chart-preservation conditions; those are not inferred here.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

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
    serialized_matrix_digest,
    theta,
    vector_image,
)


def linear_combination(
    field: QuinticField,
    columns: Sequence[Poly],
    coefficients: Sequence[FieldElement],
) -> Poly:
    if len(columns) != len(coefficients):
        raise ValueError("column count does not match coefficient count")
    result: Poly = {}
    for column, scalar in zip(columns, coefficients):
        if not scalar:
            continue
        for exponent, coefficient in column.items():
            result[exponent] = result.get(exponent, field.zero) + scalar * coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def exact_source_bounds(
    r: int,
    a_support: Sequence[int],
    b_support: Sequence[int],
) -> tuple[int, int, int, int]:
    if r == 5:
        raise ValueError("the r=5 resonance requires a separate source parametrization")
    if not a_support or not b_support:
        raise ValueError("the endpoint proof requires nonempty a and b windows")

    # A0 has exponents 1..8 and B0 has exponents 2..12.
    lower = min(min(a_support), min(b_support) - 1)
    ordinary_upper = max(max(a_support) - 7, max(b_support) - 11)
    exceptional_upper = 18 - 4 * r
    upper = max(ordinary_upper, exceptional_upper)
    return lower, upper, ordinary_upper, exceptional_upper


def source_column(
    field: QuinticField,
    r: int,
    k: int,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
) -> tuple[Poly, Poly]:
    f = monomial(field, k)
    g_coefficient = field.element(-(k + 2)) / field.element(r - 5)
    g = monomial(field, k - 1, g_coefficient)
    return theta(field, A0, B0, f, g)


def vector_terms(
    exponents: Sequence[int], vector: Sequence[FieldElement]
) -> list[dict[str, Any]]:
    return [
        {"k": exponent, "coefficient": coefficient.as_json()}
        for exponent, coefficient in zip(exponents, vector)
        if coefficient
    ]


def output_terms(
    a_support: Sequence[int],
    b_support: Sequence[int],
    vector: Sequence[FieldElement],
) -> dict[str, list[dict[str, Any]]]:
    split = len(a_support)
    return {
        "a": [
            {"exponent": exponent, "coefficient": coefficient.as_json()}
            for exponent, coefficient in zip(a_support, vector[:split])
            if coefficient
        ],
        "b": [
            {"exponent": exponent, "coefficient": coefficient.as_json()}
            for exponent, coefficient in zip(b_support, vector[split:])
            if coefficient
        ],
    }


def independent_extension(
    field: QuinticField,
    initial: Sequence[Vector],
    candidates: Sequence[Vector],
    ambient_dimension: int,
) -> tuple[list[Vector], list[Vector]]:
    basis = independent_columns(field, initial, ambient_dimension)
    rank = len(basis)
    added: list[Vector] = []
    for candidate in candidates:
        trial = basis + [candidate]
        trial_basis = independent_columns(field, trial, ambient_dimension)
        if len(trial_basis) > rank:
            basis.append(candidate)
            added.append(candidate)
            rank += 1
    return basis, added


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


def analyze_layer(
    field: QuinticField,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    layer: Mapping[str, Any],
) -> dict[str, Any]:
    r = int(layer["r"])
    a_support = list(layer["a_support"])
    b_support = list(layer["b_support"])
    ambient_dimension = len(a_support) + len(b_support)

    operator, target_exponents = determinant_operator(
        field, r, A0, B0, a_support, b_support
    )
    operator_rank = matrix_rank(
        operator, columns=ambient_dimension, field=field
    )
    kernel_basis = nullspace(
        operator, columns=ambient_dimension, field=field
    )
    kernel_dimension = len(kernel_basis)

    lower, upper, ordinary_upper, exceptional_upper = exact_source_bounds(
        r, a_support, b_support
    )
    source_exponents = list(range(lower, upper + 1))
    a_columns: list[Poly] = []
    b_columns: list[Poly] = []
    individually_admissible: list[int] = []
    allowed_a = set(a_support)
    allowed_b = set(b_support)
    for k in source_exponents:
        a, b = source_column(field, r, k, A0, B0)
        a_columns.append(a)
        b_columns.append(b)
        if all(exponent in allowed_a for exponent in a) and all(
            exponent in allowed_b for exponent in b
        ):
            individually_admissible.append(k)

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
    constraint_rows: list[tuple[str, int]] = [
        *(("a", exponent) for exponent in forbidden_a),
        *(("b", exponent) for exponent in forbidden_b),
    ]
    constraint_matrix: Matrix = []
    for kind, exponent in constraint_rows:
        columns = a_columns if kind == "a" else b_columns
        constraint_matrix.append(
            [column.get(exponent, field.zero) for column in columns]
        )

    source_basis = nullspace(
        constraint_matrix,
        columns=len(source_exponents),
        field=field,
    )
    gauge_candidates: list[Vector] = []
    for source_vector in source_basis:
        a = linear_combination(field, a_columns, source_vector)
        b = linear_combination(field, b_columns, source_vector)
        if any(exponent not in allowed_a for exponent in a):
            raise AssertionError(f"layer {r}: an a-support constraint was lost")
        if any(exponent not in allowed_b for exponent in b):
            raise AssertionError(f"layer {r}: a b-support constraint was lost")
        output = output_vector(field, a, b, a_support, b_support)
        if any(vector_image(operator, output, field)):
            raise AssertionError(f"layer {r}: a source image is not in ker D_r")
        gauge_candidates.append(output)

    gauge_basis = independent_columns(
        field, gauge_candidates, ambient_dimension
    )
    explained, residual_representatives = independent_extension(
        field, gauge_basis, kernel_basis, ambient_dimension
    )
    gauge_dimension = len(gauge_basis)
    residual_dimension = len(residual_representatives)
    if len(explained) != kernel_dimension:
        raise AssertionError(f"layer {r}: gauge plus residuals do not span the kernel")

    return {
        "r": r,
        "a_support": a_support,
        "b_support": b_support,
        "domain_dimension": ambient_dimension,
        "target_dimension": len(target_exponents),
        "target_exponents": target_exponents,
        "rank": operator_rank,
        "kernel_dimension": kernel_dimension,
        "cokernel_dimension": len(target_exponents) - operator_rank,
        "source_exponent_interval": [lower, upper],
        "ordinary_upper_bound": ordinary_upper,
        "exceptional_top_cancellation_exponent": exceptional_upper,
        "source_candidate_dimension": len(source_exponents),
        "outside_constraint_count": len(constraint_rows),
        "outside_constraints": [
            {"component": kind, "exponent": exponent}
            for kind, exponent in constraint_rows
        ],
        "individually_admissible_exponents": individually_admissible,
        "support_admissible_source_dimension": len(source_basis),
        "source_stabilizer_dimension": len(source_basis) - gauge_dimension,
        "source_basis": [
            vector_terms(source_exponents, vector) for vector in source_basis
        ],
        "gauge_dimension": gauge_dimension,
        "residual_dimension": residual_dimension,
        "residual_representatives": [
            output_terms(a_support, b_support, vector)
            for vector in residual_representatives
        ],
        "operator_sha256": serialized_matrix_digest(
            operator, columns=ambient_dimension
        ),
        "constraint_sha256": serialized_matrix_digest(
            constraint_matrix, columns=len(source_exponents)
        ),
    }


def analyze(
    face_path: Path,
    support_path: Path,
    layers: Sequence[int],
) -> dict[str, Any]:
    field, A0, B0 = parse_face(face_path)
    if (min(A0), max(A0), min(B0), max(B0)) != (1, 8, 2, 12):
        raise ValueError("unexpected leading-face endpoint exponents")
    if face_equation(field, A0, B0) != {2: field.one}:
        raise ValueError("the reconstructed leading face does not satisfy Psi=z^2")
    results = [
        analyze_layer(field, A0, B0, layer)
        for layer in load_full_layers(support_path, layers)
    ]
    return {
        "schema_version": 1,
        "name": "degree-21 full Laurent fixed-chart gauge replay",
        "coefficient_field_degree": 5,
        "face_identity_verified": True,
        "identity": "D_r Theta_r(f,g)=(f z^2)' +(r-5)g z^2",
        "source_model": (
            "all finite Laurent f with g=-(f'+2f/z)/(r-5) whose combined "
            "Theta_r image lies in the exact full Newton coefficient windows"
        ),
        "scope_limitation": (
            "This is the maximal linear support-admissible weighted-divergence "
            "space. It does not impose nonlinear integrability, normalization, "
            "or preservation of the complete fixed-chart presentation."
        ),
        "layers": results,
        "gauge_sequence": [result["gauge_dimension"] for result in results],
        "residual_sequence": [result["residual_dimension"] for result in results],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("face", type=Path)
    parser.add_argument("supports", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument(
        "--layers",
        default="1,2,3,4",
        help="comma-separated normal layers (default: 1,2,3,4)",
    )
    args = parser.parse_args(argv)
    try:
        layers = [int(value) for value in args.layers.split(",") if value]
        report = analyze(args.face, args.supports, layers)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"degree21_lower_face_full_gauge: {exc}", file=sys.stderr)
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
