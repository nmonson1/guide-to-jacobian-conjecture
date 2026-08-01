#!/usr/bin/env python3
"""Compute the intrinsic order-four map at the exceptional algebraic slope.

The symbolic finite-slope cubic certificate leaves the conjugate pair

    r = 4 +/- 4*sqrt(-3).

At either slope the cubic tangent system has rank five and is solvable, so the
quadratic correction has a 17-dimensional affine freedom.  This adapter works
at

    r_plus = 4 + 4*sqrt(-3)

inside K = Q(sqrt(-3)), retains the complete 17-dimensional cubic-lift fibre,
and computes the degree-at-most-two order-four Kuranishi map.  Since all input
data are rational, the result at the other slope is its exact Galois
conjugate.

The strongest cheap invariant is the coefficient-span test.  If the constant
term of the order-four map is outside the K-span of every nonconstant
coefficient, a K-linear target functional annihilates all dependence on the
17 fibre parameters while pairing nontrivially with the constant term.  This
is an intrinsic order-four obstruction for both conjugate slopes.

This is a formal local rank-at-most-six calculation.  It does not classify the
full 15-dimensional finite row-base fibre, impose the compression functional,
or prove convergence/algebraization.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Sequence

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from .program5_compression_export import DEFAULT_SOURCE
from .program5_rank_six_schur_model import build_schur_model
from .program5_rank_six_second_order import (
    _flatten,
    _independent_rows_and_columns,
)


def _normal(value: sp.Expr) -> sp.Expr:
    return sp.factor(sp.cancel(value))


def _normal_matrix(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.applyfunc(_normal)


def _digest(vector: sp.Matrix) -> str:
    payload = [str(_normal(value)) for value in vector]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _rank_over_field(matrix: sp.Matrix, field: Any) -> int:
    return DomainMatrix.from_Matrix(
        matrix,
        fmt="sparse",
    ).convert_to(field).rank()


def _deterministic_solution(
    matrix: sp.Matrix,
    rhs: sp.Matrix,
) -> tuple[sp.Matrix, int]:
    solution_tuple = next(iter(sp.linsolve((matrix, rhs))))
    free_symbols = sorted(
        set().union(*(entry.free_symbols for entry in solution_tuple)),
        key=str,
    )
    substitution = {symbol: 0 for symbol in free_symbols}
    solution = sp.Matrix(
        [_normal(entry.subs(substitution)) for entry in solution_tuple]
    )
    error = _normal_matrix(matrix * solution - rhs)
    if any(value != 0 for value in error):
        raise AssertionError("deterministic algebraic solution failed")
    return solution, len(free_symbols)


def _support_union(vectors: Sequence[sp.Matrix]) -> list[int]:
    return sorted(
        {
            row
            for vector in vectors
            for row, value in enumerate(vector)
            if _normal(value) != 0
        }
    )


def analyze_algebraic_fourth_order_kuranishi(
    source_path: Path = DEFAULT_SOURCE,
) -> dict[str, Any]:
    model = build_schur_model(source_path)
    alpha = sp.sqrt(-3)
    field = sp.QQ.algebraic_field(alpha)
    ratio = 4 + 4 * alpha
    conjugate_ratio = 4 - 4 * alpha
    if _normal(ratio**2 - 8 * ratio + 64) != 0:
        raise AssertionError("selected algebraic ratio left its minimal factor")

    theta = model.theta_v + ratio * model.theta_u
    theta_block = model.blocks(theta)
    tangent_matrix = sp.Matrix.hstack(*model.tangent_basis)
    tangent_blocks = [model.blocks(vector) for vector in model.tangent_basis]

    H2 = model.quadratic_forcing(theta_block)
    residual2 = model.project(_flatten(H2))
    if any(_normal(value) != 0 for value in residual2):
        raise AssertionError("exceptional algebraic direction lost order two")
    P2_image_particular = model.solve_image(H2)

    cubic_residual = model.project(
        _flatten(
            model.cubic_forcing(
                theta_block,
                model.blocks(P2_image_particular),
            )
        )
    )
    effect_columns = [
        model.project(
            _flatten(model.bilinear_effect(tangent_block, theta_block))
        )
        for tangent_block in tangent_blocks
    ]
    effect_full = sp.Matrix.hstack(*effect_columns)
    effect_active_rows = _support_union([cubic_residual, *effect_columns])
    effect_matrix = effect_full[effect_active_rows, :]
    cubic_rhs = sp.Matrix(
        [-cubic_residual[row, 0] for row in effect_active_rows]
    )
    effect_rank = _rank_over_field(effect_matrix, field)
    effect_augmented_rank = _rank_over_field(
        effect_matrix.row_join(cubic_rhs),
        field,
    )
    if effect_rank != effect_augmented_rank:
        raise AssertionError("exceptional algebraic cubic lift became obstructed")
    tangent_coordinates, reported_free_dimension = _deterministic_solution(
        effect_matrix,
        cubic_rhs,
    )
    tangent_particular = tangent_matrix * tangent_coordinates
    P2_base = P2_image_particular + tangent_particular
    cubic_check = model.project(
        _flatten(model.cubic_forcing(theta_block, model.blocks(P2_base)))
    )
    if any(_normal(value) != 0 for value in cubic_check):
        raise AssertionError("algebraic quadratic correction left cubic forcing")

    kernel_coordinates = effect_matrix.nullspace()
    expected_free_dimension = len(model.tangent_basis) - effect_rank
    if len(kernel_coordinates) != expected_free_dimension:
        raise AssertionError("algebraic cubic-effect nullity changed")
    if reported_free_dimension != expected_free_dimension:
        raise AssertionError("algebraic linsolve free dimension disagrees")
    for coordinates in kernel_coordinates:
        if any(
            _normal(value) != 0
            for value in effect_matrix * coordinates
        ):
            raise AssertionError("algebraic nullspace vector is invalid")
    homogeneous_directions = [
        tangent_matrix * coordinates
        for coordinates in kernel_coordinates
    ]

    local_pivot_rows, effect_pivot_columns = _independent_rows_and_columns(
        effect_matrix
    )
    effect_minor = effect_matrix[local_pivot_rows, effect_pivot_columns]
    effect_minor_inverse = effect_minor.inv()
    global_pivot_rows = [effect_active_rows[row] for row in local_pivot_rows]

    def project_effect(vector: sp.Matrix) -> sp.Matrix:
        coefficients = effect_minor_inverse * vector[global_pivot_rows, :]
        residual = _normal_matrix(
            vector
            - effect_full[:, list(effect_pivot_columns)] * coefficients
        )
        if any(residual[row, 0] != 0 for row in global_pivot_rows):
            raise AssertionError("algebraic order-three projection kept pivots")
        return residual

    def forcing_through_four(P2: sp.Matrix) -> sp.Matrix:
        block1 = theta_block
        block2 = model.blocks(P2)
        G0 = model.G0
        G1 = -G0 * block1["A"] * G0
        G2 = -G0 * (
            block1["A"] * G1 + block2["A"] * G0
        )
        H3 = _normal_matrix(
            block1["C"] * G0 * block2["B"]
            + block1["C"] * G1 * block1["B"]
            + block1["C"] * G2 * model.B0
            + block2["C"] * G0 * block1["B"]
            + block2["C"] * G1 * model.B0
        )
        if any(
            _normal(value) != 0
            for value in model.project(_flatten(H3))
        ):
            raise AssertionError("algebraic quadratic fibre left cubic forcing")
        P3 = model.solve_image(H3)
        block3 = model.blocks(P3)
        G3 = -G0 * (
            block1["A"] * G2
            + block2["A"] * G1
            + block3["A"] * G0
        )

        blocks = {1: block1, 2: block2, 3: block3}
        inverses = {0: G0, 1: G1, 2: G2, 3: G3}
        B_series = {
            0: model.B0,
            1: block1["B"],
            2: block2["B"],
            3: block3["B"],
        }
        H4 = sp.zeros(len(model.zero_rows), len(model.nonpivot_columns))
        for i_order in range(1, 4):
            for j_order in range(0, 4 - i_order + 1):
                k_order = 4 - i_order - j_order
                if k_order in B_series:
                    H4 += (
                        blocks[i_order]["C"]
                        * inverses[j_order]
                        * B_series[k_order]
                    )
        return project_effect(model.project(_flatten(H4)))

    q0 = forcing_through_four(P2_base)
    plus_values: list[sp.Matrix] = []
    linear_coefficients: list[sp.Matrix] = []
    diagonal_coefficients: list[sp.Matrix] = []
    for direction in homogeneous_directions:
        plus = forcing_through_four(P2_base + direction)
        minus = forcing_through_four(P2_base - direction)
        plus_values.append(plus)
        linear_coefficients.append(
            _normal_matrix((plus - minus) / 2)
        )
        diagonal_coefficients.append(
            _normal_matrix((plus + minus - 2 * q0) / 2)
        )

    off_diagonal_coefficients: list[sp.Matrix] = []
    for left in range(len(homogeneous_directions)):
        for right in range(left + 1, len(homogeneous_directions)):
            value = forcing_through_four(
                P2_base
                + homogeneous_directions[left]
                + homogeneous_directions[right]
            )
            off_diagonal_coefficients.append(
                _normal_matrix(
                    value
                    - plus_values[left]
                    - plus_values[right]
                    + q0
                )
            )

    variable_vectors = [
        *linear_coefficients,
        *diagonal_coefficients,
        *off_diagonal_coefficients,
    ]
    coefficient_active_rows = _support_union([q0, *variable_vectors])
    variable_matrix = sp.Matrix.hstack(*variable_vectors)[
        coefficient_active_rows,
        :,
    ]
    constant_vector = q0[coefficient_active_rows, :]
    variable_rank = _rank_over_field(variable_matrix, field)
    augmented_rank = _rank_over_field(
        variable_matrix.row_join(constant_vector),
        field,
    )
    constant_obstruction = augmented_rank > variable_rank

    certificate = None
    if constant_obstruction:
        witness = next(
            (
                vector
                for vector in variable_matrix.T.nullspace()
                if _normal((vector.T * constant_vector)[0, 0]) != 0
            ),
            None,
        )
        if witness is None:
            raise AssertionError("rank jump has no algebraic left-null witness")
        first_nonzero = next(value for value in witness if value != 0)
        witness = sp.Matrix(
            [_normal(value / first_nonzero) for value in witness]
        )
        annihilation = _normal_matrix(witness.T * variable_matrix)
        pairing = _normal((witness.T * constant_vector)[0, 0])
        if any(value != 0 for value in annihilation) or pairing == 0:
            raise AssertionError("invalid algebraic fourth-order certificate")
        coordinates = []
        for local_row, coefficient in enumerate(witness):
            if coefficient == 0:
                continue
            coordinates.append(
                {
                    **model.residual_coordinate(
                        coefficient_active_rows[local_row]
                    ),
                    "coefficient": str(_normal(coefficient)),
                }
            )
        certificate = {
            "kind": "K-linear constant-term separator",
            "field": "Q(sqrt(-3))",
            "pairing_with_constant_term": str(pairing),
            "nonzero_count": len(coordinates),
            "witness_sha256": _digest(witness),
            "coordinates": coordinates,
        }

    return {
        "schema_version": 1,
        "name": "Program 5 exceptional algebraic order-four Kuranishi audit",
        "source_file": str(source_path),
        "source_sha256": model.source_sha256,
        "coefficient_field": "Q(sqrt(-3))",
        "minimal_polynomial": "u^2 + 3",
        "audited_ratio": str(ratio),
        "conjugate_ratio": str(conjugate_ratio),
        "conjugate_result_follows_by_Q_galois_symmetry": True,
        "ambient_operation_dimension": model.ambient_operation_dimension,
        "rank_six_tangent_dimension": len(model.tangent_basis),
        "cubic_effect_rank": effect_rank,
        "cubic_augmented_rank": effect_augmented_rank,
        "cubic_lift_affine_dimension": expected_free_dimension,
        "order_four_map": {
            "source_dimension": expected_free_dimension,
            "constant_nonzero_count": sum(
                _normal(value) != 0 for value in q0
            ),
            "linear_coefficient_count": len(linear_coefficients),
            "diagonal_quadratic_coefficient_count": len(
                diagonal_coefficients
            ),
            "off_diagonal_quadratic_coefficient_count": len(
                off_diagonal_coefficients
            ),
            "active_target_coordinate_count": len(coefficient_active_rows),
            "variable_coefficient_rank": variable_rank,
            "constant_augmented_rank": augmented_rank,
            "constant_term_outside_variable_coefficient_span": (
                constant_obstruction
            ),
        },
        "intrinsic_order_four_obstruction": constant_obstruction,
        "obstruction_certificate": certificate,
        "interpretation_boundary": (
            "A constant-term separator is decisive for this conjugate pair. "
            "If none is found, the order-four zero locus still requires a "
            "nonlinear solve; equality of coefficient spans is not a lift."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_algebraic_fourth_order_kuranishi(args.source)
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(
            f"program5_rank_six_algebraic_fourth_order_kuranishi: {exc}",
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
