#!/usr/bin/env python3
"""Construct a two-parameter rank-six formal arc order by order.

The second-order Kuranishi equations for the two tangent directions outside the
row-zero chart admit the uniform linear section

    s0=4v, s1=-24v, s3=0, s4=u-4v, s5=0,

with all other displayed row-zero coordinates set to zero.  Equivalently, if
``xi_i`` is the exported row-zero tangent basis and ``eta_0,eta_1`` the two
complement directions, use

    theta_u = eta_0 + xi_4,
    theta_v = eta_1 + 4 xi_0 - 24 xi_1 - 4 xi_4.

This script seeks a formal solution of the local Schur-complement equations

    F(P)=0

of the form

    P(u,v)=P0 + sum_{n>=1} P_n(u,v),

where ``P_n`` is homogeneous of degree ``n``.  At each order it computes the
complete forcing, projects it to the cokernel of the rank-93 tangent map, and,
when compatible, chooses the deterministic correction supported on a fixed
invertible 93-by-93 tangent minor.

The result is a formal local rank calculation.  It does not impose the
quartic compression equation, identify the true operation-group quotient, or
prove convergence/algebraization.
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


MatrixPolynomial = list[sp.Matrix]
VectorPolynomial = list[sp.Matrix]


def _zero_matrices(count: int, rows: int, columns: int) -> MatrixPolynomial:
    return [sp.zeros(rows, columns) for _ in range(count)]


def _sparse_vector(
    vector: sp.Matrix,
    labels: Sequence[str],
) -> list[dict[str, Any]]:
    return [
        {"coordinate": labels[index], "coefficient": _q(vector[index, 0])}
        for index in range(vector.rows)
        if vector[index, 0] != 0
    ]


def _vector_digest(vector: sp.Matrix) -> str:
    payload = [str(sp.Rational(value)) for value in vector]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _coefficient_convolution(
    left: MatrixPolynomial,
    right: MatrixPolynomial,
    *,
    total_u_degree: int,
) -> sp.Matrix:
    if not left or not right:
        raise ValueError("empty polynomial coefficient list")
    rows = left[0].rows
    columns = right[0].cols
    result = sp.zeros(rows, columns)
    for left_u, left_matrix in enumerate(left):
        right_u = total_u_degree - left_u
        if 0 <= right_u < len(right):
            result += left_matrix * right[right_u]
    return result


def analyze_formal_arc(
    source_path: Path = DEFAULT_SOURCE,
    *,
    max_order: int = 6,
) -> dict[str, Any]:
    if max_order < 2:
        raise ValueError("max_order must be at least two")

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

    p0 = sp.zeros(115, 1)
    p0_index = next(
        index
        for index, (row, monomial) in enumerate(operation_basis)
        if row == 3 and sp.expand(monomial - source.d**2) == 0
    )
    p0[p0_index, 0] = -1

    def variation(vector: sp.Matrix) -> sp.Matrix:
        result = sp.zeros(n, len(cubic_monomials))
        for coefficient, matrix in zip(vector, variation_matrices):
            if coefficient:
                result += coefficient * matrix
        return result

    M0 = sp.zeros(n, len(cubic_monomials))
    for row, expression in enumerate(C):
        polynomial = sp.Poly(expression, *V)
        for column, monomial in enumerate(cubic_monomials):
            M0[row, column] = polynomial.coeff_monomial(monomial)
    M0 += variation(p0)
    if M0.rank() != 6:
        raise AssertionError("base cubic-coordinate matrix lost rank six")

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
        raise AssertionError("tangent map no longer has rank 93")
    pivot_rows, pivot_operation_columns = _independent_rows_and_columns(L)
    minor = L[pivot_rows, pivot_operation_columns]
    minor_inverse = minor.inv()

    def solve_image(forcing: sp.Matrix) -> tuple[bool, sp.Matrix, sp.Matrix]:
        residual = _project_to_cokernel(
            forcing,
            L,
            pivot_rows=pivot_rows,
            pivot_columns=pivot_operation_columns,
            inverse_minor=minor_inverse,
        )
        correction = sp.zeros(115, 1)
        if not any(residual):
            coefficients = minor_inverse * forcing[list(pivot_rows), :]
            for index, column in enumerate(pivot_operation_columns):
                correction[column, 0] = coefficients[index, 0]
            if L * correction != forcing:
                raise AssertionError("deterministic correction failed")
            return True, correction, residual
        return False, correction, residual

    # P_series[n][k] is the coefficient of u^k v^(n-k).
    P_series: dict[int, VectorPolynomial] = {
        1: [theta_v, theta_u]
    }
    A_series: dict[int, MatrixPolynomial] = {}
    B_series: dict[int, MatrixPolynomial] = {0: [B0]}
    C_series: dict[int, MatrixPolynomial] = {}
    D_series: dict[int, MatrixPolynomial] = {}
    G_series: dict[int, MatrixPolynomial] = {0: [G0]}

    def record_blocks(order: int) -> None:
        A_series[order] = []
        B_series[order] = []
        C_series[order] = []
        D_series[order] = []
        for vector in P_series[order]:
            block = blocks(vector)
            A_series[order].append(block["A"])
            B_series[order].append(block["B"])
            C_series[order].append(block["C"])
            D_series[order].append(block["D"])

    def compute_inverse_order(order: int) -> None:
        coefficients = _zero_matrices(order + 1, 6, 6)
        for u_degree in range(order + 1):
            total = sp.zeros(6, 6)
            for left_order in range(1, order + 1):
                right_order = order - left_order
                for left_u, A_value in enumerate(A_series[left_order]):
                    right_u = u_degree - left_u
                    if 0 <= right_u < len(G_series[right_order]):
                        total += A_value * G_series[right_order][right_u]
            coefficients[u_degree] = -G0 * total
        G_series[order] = coefficients

    record_blocks(1)
    compute_inverse_order(1)

    orders: list[dict[str, Any]] = [
        {
            "order": 1,
            "compatible": True,
            "coefficient_count": 2,
            "corrections": [
                {
                    "monomial": "v",
                    "nonzero_count": len(_sparse_vector(theta_v, labels)),
                    "sha256": _vector_digest(theta_v),
                    "vector": _sparse_vector(theta_v, labels),
                },
                {
                    "monomial": "u",
                    "nonzero_count": len(_sparse_vector(theta_u, labels)),
                    "sha256": _vector_digest(theta_u),
                    "vector": _sparse_vector(theta_u, labels),
                },
            ],
        }
    ]

    first_obstructed_order: int | None = None
    for order in range(2, max_order + 1):
        forcing_coefficients = _zero_matrices(
            order + 1,
            len(zero_rows),
            len(nonpivot_columns),
        )
        # H_n = sum C_i G_j B_k with i>=1 and i+j+k=n.
        # The term C_n G_0 B_0 is the linear part and is omitted.
        for i in range(1, order):
            for j in range(0, order - i + 1):
                k = order - i - j
                if j not in G_series or k not in B_series:
                    continue
                for c_u, C_value in enumerate(C_series[i]):
                    for g_u, G_value in enumerate(G_series[j]):
                        b_u = None
                        for candidate_b_u, B_value in enumerate(B_series[k]):
                            total_u = c_u + g_u + candidate_b_u
                            if total_u <= order:
                                forcing_coefficients[total_u] += (
                                    C_value * G_value * B_value
                                )

        corrections: VectorPolynomial = []
        obstruction_vectors = []
        compatible = True
        for forcing_matrix in forcing_coefficients:
            forcing = _flatten(forcing_matrix)
            solvable, correction, residual = solve_image(forcing)
            corrections.append(correction)
            obstruction_vectors.append(residual)
            compatible = compatible and solvable

        obstruction_rank = _matrix_rank(
            sp.Matrix.hstack(*obstruction_vectors)
        ) if obstruction_vectors else 0
        record = {
            "order": order,
            "compatible": compatible,
            "coefficient_count": order + 1,
            "obstruction_rank": obstruction_rank,
            "obstructed_monomials": [
                (
                    f"u^{u_degree}*v^{order-u_degree}"
                    if 0 < u_degree < order
                    else (f"v^{order}" if u_degree == 0 else f"u^{order}")
                )
                for u_degree, residual in enumerate(obstruction_vectors)
                if any(residual)
            ],
        }
        if compatible:
            P_series[order] = corrections
            record_blocks(order)
            compute_inverse_order(order)
            record["corrections"] = []
            for u_degree, vector in enumerate(corrections):
                monomial = (
                    f"u^{u_degree}*v^{order-u_degree}"
                    if 0 < u_degree < order
                    else (f"v^{order}" if u_degree == 0 else f"u^{order}")
                )
                sparse = _sparse_vector(vector, labels)
                record["corrections"].append(
                    {
                        "monomial": monomial,
                        "nonzero_count": len(sparse),
                        "sha256": _vector_digest(vector),
                        "vector": sparse,
                    }
                )
        else:
            first_obstructed_order = order
        orders.append(record)
        if not compatible:
            break

    return {
        "schema_version": 1,
        "name": "Program 5 two-parameter formal rank-six arc",
        "source_file": str(source_path),
        "source_sha256": exported["summary"]["source_sha256"],
        "ambient_operation_dimension": 115,
        "tangent_map_rank": 93,
        "tangent_dimension": 22,
        "row_zero_tangent_dimension": 20,
        "chosen_first_order_plane": {
            "coordinate_section": {
                "s0": "4*v",
                "s1": "-24*v",
                "s3": "0",
                "s4": "u-4*v",
                "s5": "0",
                "other_s_coordinates": "0",
            },
            "theta_u": "eta_0 + xi_4",
            "theta_v": "eta_1 + 4*xi_0 - 24*xi_1 - 4*xi_4",
        },
        "maximum_requested_order": max_order,
        "maximum_compatible_order": max(
            record["order"] for record in orders if record["compatible"]
        ),
        "first_obstructed_order": first_obstructed_order,
        "orders": orders,
        "interpretation_boundary": (
            "Compatibility through order N gives a formal rank-six arc only "
            "to that order in the chosen local Schur-complement chart. It does "
            "not impose Lambda_4=0, prove all-order algebraization, or quotient "
            "by every admissible operation."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--max-order", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_formal_arc(
            args.source,
            max_order=args.max_order,
        )
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(f"program5_rank_six_formal_arc: {exc}", file=sys.stderr)
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
