#!/usr/bin/env python3
"""Resolve the Program 5 cubic rank-six obstruction modulo tangent freedom.

The deterministic formal lift in ``program5_rank_six_formal_arc.py`` sets the
22-dimensional homogeneous freedom in each quadratic correction equal to
zero.  Its order-three forcing has a nonzero cokernel projection.  That is not
an intrinsic obstruction: every order-two correction is defined only modulo
the rank-six tangent kernel.

This script introduces all 66 free coefficients

    K_rank tensor Sym^2<u,v>

in the three quadratic corrections, computes their exact effect on the four
cubic forcing coefficients, and solves the resulting linear system over Q.
It then verifies the adjusted order-two lift and constructs deterministic
order-three corrections.

The result decides compatibility through cubic parameter order for the chosen
two-dimensional first-order plane. It does not decide fourth order, all-order
integration, convergence, or the true operation-group quotient.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from itertools import combinations_with_replacement
from pathlib import Path
from typing import Any, Sequence

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from .program5_compression_export import (
    DEFAULT_SOURCE,
    _load_source,
    _monomial_label,
    _q,
    build_export,
)
from .program5_rank_six_second_order import (
    _flatten,
    _independent_rows_and_columns,
    _matrix_rank,
    _project_to_cokernel,
    _sympy_matrix,
)
from .program5_tangent_bridge import _extend_basis


def _sparse_vector(
    vector: sp.Matrix,
    labels: Sequence[str],
) -> list[dict[str, Any]]:
    return [
        {"coordinate": labels[index], "coefficient": _q(vector[index, 0])}
        for index in range(vector.rows)
        if vector[index, 0] != 0
    ]


def _digest(vector: sp.Matrix) -> str:
    return hashlib.sha256(
        json.dumps(
            [str(sp.Rational(value)) for value in vector],
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _deterministic_linear_solution(
    matrix: sp.Matrix,
    rhs: sp.Matrix,
) -> tuple[bool, sp.Matrix | None, int, int, int]:
    rank = DomainMatrix.from_Matrix(matrix, fmt="sparse").rank()
    augmented_rank = DomainMatrix.from_Matrix(
        matrix.row_join(rhs),
        fmt="sparse",
    ).rank()
    if rank != augmented_rank:
        return False, None, rank, augmented_rank, matrix.cols - rank
    solution_tuple = next(iter(sp.linsolve((matrix, rhs))))
    free_symbols = sorted(
        set().union(*(entry.free_symbols for entry in solution_tuple)),
        key=str,
    )
    substitution = {symbol: 0 for symbol in free_symbols}
    solution = sp.Matrix(
        [sp.factor(entry.subs(substitution)) for entry in solution_tuple]
    )
    if matrix * solution != rhs:
        raise AssertionError("deterministic cubic-lift solution failed")
    return True, solution, rank, augmented_rank, len(free_symbols)


def analyze_third_order(source_path: Path = DEFAULT_SOURCE) -> dict[str, Any]:
    contract, exported = build_export(source_path)
    row_layer, rank_layer = contract["layers"]
    operation_labels = list(row_layer["deformation_basis"])
    row_kernel = _sympy_matrix(row_layer["actions"][0]["action_matrix"])
    rank_kernel = _sympy_matrix(rank_layer["actions"][0]["action_matrix"])
    row_columns = [row_kernel[:, index] for index in range(row_kernel.cols)]
    rank_columns = [rank_kernel[:, index] for index in range(rank_kernel.cols)]
    adapted, complement = _extend_basis(row_columns, rank_columns)
    if len(adapted) != 22 or len(complement) != 2:
        raise AssertionError("the 20+2 tangent splitting changed")
    tangent_basis = adapted
    eta0, eta1 = complement
    theta_u = eta0 + row_columns[4]
    theta_v = eta1 + 4 * row_columns[0] - 24 * row_columns[1] - 4 * row_columns[4]

    source, _ = _load_source(source_path)
    V = tuple(source.V)
    Q = sp.Matrix(source.Q)
    C = sp.Matrix(source.C)
    weights = source.weights
    n = len(V)
    cubic_monomials = [
        sp.prod(V[index] for index in indices)
        for indices in combinations_with_replacement(range(n), 3)
    ]
    quadratic_monomials = [
        sp.prod(V[index] for index in indices)
        for indices in combinations_with_replacement(range(n), 2)
    ]

    def weight(monomial: sp.Expr) -> int:
        exponents = sp.Poly(monomial, *V).monoms()[0]
        return sum(exponents[index] * weights[V[index]] for index in range(n))

    operation_basis: list[tuple[int, sp.Expr]] = []
    for row, variable in enumerate(V):
        for monomial in quadratic_monomials:
            if weight(monomial) == weights[variable]:
                operation_basis.append((row, monomial))
    labels = [
        f"e_{V[row]}*{_monomial_label(monomial)}"
        for row, monomial in operation_basis
    ]
    if len(operation_basis) != 115 or labels != operation_labels:
        raise AssertionError("operation basis changed")

    JQ = Q.jacobian(V)
    variation_matrices: list[sp.Matrix] = []
    for operation_row, monomial in operation_basis:
        field = sp.zeros(n, 1)
        field[operation_row, 0] = monomial
        bracket = sp.Matrix(
            [
                sp.expand(value)
                for value in JQ * field - field.jacobian(V) * Q
            ]
        )
        coefficient_matrix = sp.zeros(n, len(cubic_monomials))
        for row, expression in enumerate(bracket):
            polynomial = sp.Poly(expression, *V)
            for column, cubic_monomial in enumerate(cubic_monomials):
                coefficient_matrix[row, column] = polynomial.coeff_monomial(
                    cubic_monomial
                )
        variation_matrices.append(coefficient_matrix)

    def variation(vector: sp.Matrix) -> sp.Matrix:
        result = sp.zeros(n, len(cubic_monomials))
        for coefficient, matrix in zip(vector, variation_matrices):
            if coefficient:
                result += coefficient * matrix
        return result

    p0 = sp.zeros(115, 1)
    p0_index = next(
        index
        for index, (row, monomial) in enumerate(operation_basis)
        if row == 3 and sp.expand(monomial - source.d**2) == 0
    )
    p0[p0_index, 0] = -1
    M0 = sp.zeros(n, len(cubic_monomials))
    for row, expression in enumerate(C):
        polynomial = sp.Poly(expression, *V)
        for column, monomial in enumerate(cubic_monomials):
            M0[row, column] = polynomial.coeff_monomial(monomial)
    M0 += variation(p0)

    base_rows = [0, 1, 2, 4, 5, 8]
    zero_rows = [3, 6, 7, 9, 10]
    base_matrix = M0[base_rows, :]
    _, pivot_tuple = base_matrix.rref()
    pivot_columns = list(pivot_tuple)
    nonpivot_columns = [
        column for column in range(len(cubic_monomials))
        if column not in pivot_columns
    ]
    A0 = M0[base_rows, pivot_columns]
    B0 = M0[base_rows, nonpivot_columns]
    G0 = A0.inv()

    def blocks(vector: sp.Matrix) -> dict[str, sp.Matrix]:
        matrix = variation(vector)
        return {
            "A": matrix[base_rows, pivot_columns],
            "B": matrix[base_rows, nonpivot_columns],
            "C": matrix[zero_rows, pivot_columns],
            "D": matrix[zero_rows, nonpivot_columns],
        }

    ambient_blocks = [blocks(sp.eye(115)[:, index]) for index in range(115)]
    L_columns = [
        _flatten(block["D"] - block["C"] * G0 * B0)
        for block in ambient_blocks
    ]
    L = sp.Matrix.hstack(*L_columns)
    if _matrix_rank(L) != 93:
        raise AssertionError("tangent map rank changed")
    for vector in tangent_basis:
        if L * vector != sp.zeros(L.rows, 1):
            raise AssertionError("exported tangent basis left ker(L)")
    pivot_rows, pivot_operation_columns = _independent_rows_and_columns(L)
    minor = L[pivot_rows, pivot_operation_columns]
    minor_inverse = minor.inv()

    def solve_image(forcing: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
        residual = _project_to_cokernel(
            forcing,
            L,
            pivot_rows=pivot_rows,
            pivot_columns=pivot_operation_columns,
            inverse_minor=minor_inverse,
        )
        if any(residual):
            raise AssertionError("forcing is not in the tangent image")
        coefficients = minor_inverse * forcing[list(pivot_rows), :]
        correction = sp.zeros(115, 1)
        for index, column in enumerate(pivot_operation_columns):
            correction[column, 0] = coefficients[index, 0]
        if L * correction != forcing:
            raise AssertionError("deterministic image solution failed")
        return correction, residual

    theta_blocks = [blocks(theta_v), blocks(theta_u)]
    G1 = [
        -G0 * theta_blocks[index]["A"] * G0
        for index in range(2)
    ]

    # H2 coefficients in order v^2, u*v, u^2.
    H2 = []
    for total_u in range(3):
        value = sp.zeros(len(zero_rows), len(nonpivot_columns))
        for left_u in range(2):
            right_u = total_u - left_u
            if 0 <= right_u < 2:
                value += (
                    theta_blocks[left_u]["C"]
                    * G0
                    * theta_blocks[right_u]["B"]
                )
        for c_u in range(2):
            g_u = total_u - c_u
            if 0 <= g_u < 2:
                value += theta_blocks[c_u]["C"] * G1[g_u] * B0
        H2.append(value)

    P2_particular = []
    for value in H2:
        correction, _ = solve_image(_flatten(value))
        P2_particular.append(correction)

    def inverse_order_two(P2: Sequence[sp.Matrix]) -> list[sp.Matrix]:
        A2 = [blocks(vector)["A"] for vector in P2]
        result = []
        for total_u in range(3):
            convolution = sp.zeros(6, 6)
            for left_u in range(2):
                right_u = total_u - left_u
                if 0 <= right_u < 2:
                    convolution += theta_blocks[left_u]["A"] * G1[right_u]
            convolution += A2[total_u] * G0
            result.append(-G0 * convolution)
        return result

    def cubic_forcing(P2: Sequence[sp.Matrix]) -> list[sp.Matrix]:
        P2_blocks = [blocks(vector) for vector in P2]
        G2 = inverse_order_two(P2)
        values = []
        for total_u in range(4):
            value = sp.zeros(len(zero_rows), len(nonpivot_columns))
            # Sum C_i G_j B_k for i+j+k=3, i>=1, using orders 1 and 2.
            for i_order in (1, 2):
                C_list = theta_blocks if i_order == 1 else P2_blocks
                for j_order in (0, 1, 2):
                    k_order = 3 - i_order - j_order
                    if k_order not in (0, 1, 2):
                        continue
                    G_list = [G0] if j_order == 0 else (G1 if j_order == 1 else G2)
                    if k_order == 0:
                        B_list = [B0]
                    elif k_order == 1:
                        B_list = [block["B"] for block in theta_blocks]
                    else:
                        B_list = [block["B"] for block in P2_blocks]
                    for c_u, C_value in enumerate(C_list):
                        for g_u, G_value in enumerate(G_list):
                            b_u = total_u - c_u - g_u
                            if 0 <= b_u < len(B_list):
                                value += C_value * G_value * B_list[b_u]
            values.append(value)
        return values

    base_H3 = cubic_forcing(P2_particular)
    base_residuals = [
        _project_to_cokernel(
            _flatten(value),
            L,
            pivot_rows=pivot_rows,
            pivot_columns=pivot_operation_columns,
            inverse_minor=minor_inverse,
        )
        for value in base_H3
    ]
    if sum(any(vector) for vector in base_residuals) != 4:
        raise AssertionError("the deterministic cubic obstruction changed")

    # Exact linear effect of a tangent-kernel addition to P2.
    tangent_blocks = [blocks(vector) for vector in tangent_basis]

    def bilinear_h(
        left: dict[str, sp.Matrix],
        right: dict[str, sp.Matrix],
    ) -> sp.Matrix:
        return (
            left["C"] * G0 * right["B"]
            - left["C"] * G0 * right["A"] * G0 * B0
            + right["C"] * G0 * left["B"]
            - right["C"] * G0 * left["A"] * G0 * B0
        )

    effect_v = []
    effect_u = []
    for tangent_block in tangent_blocks:
        effect_v.append(
            _project_to_cokernel(
                _flatten(bilinear_h(tangent_block, theta_blocks[0])),
                L,
                pivot_rows=pivot_rows,
                pivot_columns=pivot_operation_columns,
                inverse_minor=minor_inverse,
            )
        )
        effect_u.append(
            _project_to_cokernel(
                _flatten(bilinear_h(tangent_block, theta_blocks[1])),
                L,
                pivot_rows=pivot_rows,
                pivot_columns=pivot_operation_columns,
                inverse_minor=minor_inverse,
            )
        )

    # Compress the 4*1400 equations to the rows that can be nonzero.
    row_keys: set[tuple[int, int]] = set()
    for output_u, residual in enumerate(base_residuals):
        row_keys.update(
            (output_u, row)
            for row, value in enumerate(residual)
            if value
        )
    for input_u in range(3):
        for effect in effect_v:
            row_keys.update(
                (input_u, row)
                for row, value in enumerate(effect)
                if value
            )
        for effect in effect_u:
            row_keys.update(
                (input_u + 1, row)
                for row, value in enumerate(effect)
                if value
            )
    ordered_rows = sorted(row_keys)
    row_index = {key: index for index, key in enumerate(ordered_rows)}
    effect_matrix = sp.zeros(len(ordered_rows), 66)
    rhs = sp.zeros(len(ordered_rows), 1)
    for output_u, residual in enumerate(base_residuals):
        for row, value in enumerate(residual):
            if value:
                rhs[row_index[(output_u, row)], 0] = -value
    for input_u in range(3):
        for tangent_index in range(22):
            column = 22 * input_u + tangent_index
            for row, value in enumerate(effect_v[tangent_index]):
                if value:
                    effect_matrix[row_index[(input_u, row)], column] += value
            for row, value in enumerate(effect_u[tangent_index]):
                if value:
                    effect_matrix[row_index[(input_u + 1, row)], column] += value

    solvable, solution, effect_rank, augmented_rank, free_dimension = (
        _deterministic_linear_solution(effect_matrix, rhs)
    )
    result: dict[str, Any] = {
        "schema_version": 1,
        "name": "Program 5 cubic lift modulo quadratic tangent freedom",
        "source_file": str(source_path),
        "source_sha256": exported["summary"]["source_sha256"],
        "ambient_operation_dimension": 115,
        "rank_six_tangent_dimension": 22,
        "quadratic_coefficient_count": 3,
        "quadratic_tangent_freedom_dimension": 66,
        "compressed_cubic_equation_count": len(ordered_rows),
        "cubic_effect_rank": effect_rank,
        "cubic_augmented_rank": augmented_rank,
        "cubic_lift_solvable": solvable,
        "cubic_lift_solution_free_dimension": free_dimension if solvable else None,
        "deterministic_base_obstructed_monomials": [
            "v^3",
            "u*v^2",
            "u^2*v",
            "u^3",
        ],
    }
    if not solvable or solution is None:
        result["interpretation"] = (
            "The cubic obstruction survives every tangent-kernel choice in "
            "the quadratic correction, so it is intrinsic for the chosen "
            "first-order plane."
        )
        return result

    adjusted_P2 = [vector.copy() for vector in P2_particular]
    tangent_adjustments = []
    for input_u in range(3):
        adjustment = sp.zeros(115, 1)
        coefficients = []
        for tangent_index, tangent_vector in enumerate(tangent_basis):
            coefficient = solution[22 * input_u + tangent_index, 0]
            if coefficient:
                adjustment += coefficient * tangent_vector
                coefficients.append(
                    {
                        "tangent_basis_index": tangent_index,
                        "coefficient": _q(coefficient),
                    }
                )
        adjusted_P2[input_u] += adjustment
        tangent_adjustments.append(
            {
                "monomial": ("v^2", "u*v", "u^2")[input_u],
                "coefficient_count": len(coefficients),
                "coefficients": coefficients,
                "adjustment_nonzero_count": len(_sparse_vector(adjustment, labels)),
                "adjustment_sha256": _digest(adjustment),
            }
        )

    adjusted_H3 = cubic_forcing(adjusted_P2)
    adjusted_residuals = [
        _project_to_cokernel(
            _flatten(value),
            L,
            pivot_rows=pivot_rows,
            pivot_columns=pivot_operation_columns,
            inverse_minor=minor_inverse,
        )
        for value in adjusted_H3
    ]
    if any(any(vector) for vector in adjusted_residuals):
        raise AssertionError("the solved tangent adjustment did not kill the cubic obstruction")
    P3 = []
    for value in adjusted_H3:
        correction, _ = solve_image(_flatten(value))
        P3.append(correction)

    result.update(
        {
            "quadratic_tangent_adjustments": tangent_adjustments,
            "adjusted_quadratic_corrections": [
                {
                    "monomial": ("v^2", "u*v", "u^2")[index],
                    "nonzero_count": len(_sparse_vector(vector, labels)),
                    "sha256": _digest(vector),
                    "vector": _sparse_vector(vector, labels),
                }
                for index, vector in enumerate(adjusted_P2)
            ],
            "cubic_obstruction_after_adjustment": 0,
            "cubic_corrections": [
                {
                    "monomial": (
                        "v^3",
                        "u*v^2",
                        "u^2*v",
                        "u^3",
                    )[index],
                    "nonzero_count": len(_sparse_vector(vector, labels)),
                    "sha256": _digest(vector),
                    "vector": _sparse_vector(vector, labels),
                }
                for index, vector in enumerate(P3)
            ],
            "interpretation": (
                "The deterministic cubic obstruction is removable by the "
                "22-dimensional tangent freedom in the quadratic correction. "
                "The chosen two-dimensional branch therefore survives through "
                "cubic parameter order."
            ),
        }
    )
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_third_order(args.source)
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(f"program5_rank_six_third_order_lift: {exc}", file=sys.stderr)
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
