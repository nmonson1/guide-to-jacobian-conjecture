#!/usr/bin/env python3
"""Second-order Kuranishi test for the Program 5 rank-six condition.

Let ``M(P)`` be the 11-by-286 cubic-coordinate coefficient matrix of

    C + [Q,P]

inside the 115-dimensional space of weight-preserving quadratic source
fields.  At ``P0=-d^2 e_a``, ``M(P0)`` has rank six.  Choose the six nonzero
base rows and a nonzero six-by-six pivot minor.  In this chart the rank-at-most
six equations are the Schur complement

    F(P) = D(P) - C(P) A(P)^(-1) B(P) = 0.

The first derivative has a 22-dimensional kernel.  This script computes the
quadratic forcing

    L(zeta) + Q2(xi) = 0

for an arbitrary tangent vector ``xi`` in that kernel, projects ``Q2`` exactly
to the cokernel of ``L``, and reports the resulting homogeneous quadratic
Kuranishi equations.

The calculation decides second-order formal compatibility only.  It is not an
all-order algebraization theorem and does not quotient by every source,
target, or stable-presentation operation.
"""
from __future__ import annotations

import argparse
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
from .program5_tangent_bridge import _extend_basis


def _sympy_matrix(values: Sequence[Sequence[Any]]) -> sp.Matrix:
    return sp.Matrix(
        [[sp.Rational(value) for value in row] for row in values]
    )


def _polynomial_terms(
    expression: sp.Expr,
    variables: Sequence[sp.Symbol],
) -> list[dict[str, Any]]:
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    result = []
    for exponents, coefficient in polynomial.terms():
        parts = []
        for variable, exponent in zip(variables, exponents):
            if not exponent:
                continue
            parts.append(
                str(variable) if exponent == 1 else f"{variable}^{exponent}"
            )
        result.append(
            {
                "exponents": list(exponents),
                "monomial": "*".join(parts) or "1",
                "coefficient": _q(coefficient),
            }
        )
    return result


def _matrix_rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(matrix, fmt="sparse").rank()


def _flatten(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(
        [matrix[row, column] for row in range(matrix.rows) for column in range(matrix.cols)]
    )


def _independent_rows_and_columns(matrix: sp.Matrix) -> tuple[list[int], list[int]]:
    column_pivots = list(
        DomainMatrix.from_Matrix(matrix, fmt="sparse").rref()[1]
    )
    row_pivots = list(
        DomainMatrix.from_Matrix(matrix.T, fmt="sparse").rref()[1]
    )
    if len(column_pivots) != len(row_pivots):
        raise AssertionError("row and column ranks disagree")
    return row_pivots, column_pivots


def _project_to_cokernel(
    vector: sp.Matrix,
    image_matrix: sp.Matrix,
    *,
    pivot_rows: Sequence[int],
    pivot_columns: Sequence[int],
    inverse_minor: sp.Matrix,
) -> sp.Matrix:
    selected_rhs = vector[list(pivot_rows), :]
    coefficients = inverse_minor * selected_rhs
    residual = vector - image_matrix[:, list(pivot_columns)] * coefficients
    if any(residual[row, 0] for row in pivot_rows):
        raise AssertionError("cokernel projection did not kill pivot rows")
    return sp.Matrix([sp.factor(value) for value in residual])


def _rank_pair(matrix: sp.Matrix, rhs: sp.Matrix) -> tuple[int, int]:
    return _matrix_rank(matrix), _matrix_rank(matrix.row_join(rhs))


def analyze_second_order(source_path: Path = DEFAULT_SOURCE) -> dict[str, Any]:
    contract, exported = build_export(source_path)
    row_layer, rank_layer = contract["layers"]
    operation_labels = list(row_layer["deformation_basis"])
    row_kernel = _sympy_matrix(row_layer["actions"][0]["action_matrix"])
    rank_kernel = _sympy_matrix(rank_layer["actions"][0]["action_matrix"])
    row_columns = [row_kernel[:, index] for index in range(row_kernel.cols)]
    rank_columns = [rank_kernel[:, index] for index in range(rank_kernel.cols)]
    adapted, complement = _extend_basis(row_columns, rank_columns)
    if len(adapted) != 22 or len(complement) != 2:
        raise AssertionError("the 20+2 adapted tangent splitting changed")
    tangent_basis = adapted

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
    if len(operation_basis) != 115:
        raise AssertionError("the operation space no longer has dimension 115")
    labels = [
        f"e_{V[row]}*{_monomial_label(monomial)}"
        for row, monomial in operation_basis
    ]
    if labels != operation_labels:
        raise AssertionError("operation basis order changed")

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
    M0 = sp.zeros(n, len(cubic_monomials))
    for row, expression in enumerate(C):
        polynomial = sp.Poly(expression, *V)
        for column, monomial in enumerate(cubic_monomials):
            M0[row, column] = polynomial.coeff_monomial(monomial)
    for coefficient, variation in zip(p0, variation_matrices):
        if coefficient:
            M0 += coefficient * variation
    if M0.rank() != 6:
        raise AssertionError("base cubic-coordinate matrix lost rank six")

    base_rows = [0, 1, 2, 4, 5, 8]
    zero_rows = [3, 6, 7, 9, 10]
    base_matrix = M0[base_rows, :]
    _, pivot_columns_tuple = base_matrix.rref()
    pivot_columns = list(pivot_columns_tuple)
    if len(pivot_columns) != 6:
        raise AssertionError("base row matrix lost rank six")
    nonpivot_columns = [
        column for column in range(len(cubic_monomials))
        if column not in pivot_columns
    ]
    A0 = M0[base_rows, pivot_columns]
    B0 = M0[base_rows, nonpivot_columns]
    A0_inverse = A0.inv()

    def variation(vector: sp.Matrix) -> sp.Matrix:
        result = sp.zeros(n, len(cubic_monomials))
        for coefficient, matrix in zip(vector, variation_matrices):
            if coefficient:
                result += coefficient * matrix
        return result

    tangent_variations = [variation(vector) for vector in tangent_basis]
    blocks = []
    for matrix in tangent_variations:
        blocks.append(
            {
                "a": matrix[base_rows, pivot_columns],
                "b": matrix[base_rows, nonpivot_columns],
                "c": matrix[zero_rows, pivot_columns],
                "d": matrix[zero_rows, nonpivot_columns],
            }
        )

    ambient_tangent_columns = []
    ambient_blocks = []
    for matrix in variation_matrices:
        block = {
            "a": matrix[base_rows, pivot_columns],
            "b": matrix[base_rows, nonpivot_columns],
            "c": matrix[zero_rows, pivot_columns],
            "d": matrix[zero_rows, nonpivot_columns],
        }
        ambient_blocks.append(block)
        linear = block["d"] - block["c"] * A0_inverse * B0
        ambient_tangent_columns.append(_flatten(linear))
    L = sp.Matrix.hstack(*ambient_tangent_columns)
    if _matrix_rank(L) != 93:
        raise AssertionError("rank-six tangent map no longer has rank 93")
    for vector in tangent_basis:
        if L * vector != sp.zeros(L.rows, 1):
            raise AssertionError("adapted vector left the rank-six tangent kernel")

    pivot_rows, pivot_operation_columns = _independent_rows_and_columns(L)
    if len(pivot_rows) != 93:
        raise AssertionError("failed to find a rank-93 tangent minor")
    tangent_minor = L[pivot_rows, pivot_operation_columns]
    if tangent_minor.det() == 0:
        raise AssertionError("selected tangent minor is singular")
    tangent_minor_inverse = tangent_minor.inv()

    parameter_names = [f"s{index}" for index in range(20)] + ["u", "v"]
    parameters = sp.symbols(" ".join(parameter_names))
    monomial_pairs = list(combinations_with_replacement(range(22), 2))
    monomial_labels = [
        (
            parameter_names[left] + "^2"
            if left == right
            else parameter_names[left] + "*" + parameter_names[right]
        )
        for left, right in monomial_pairs
    ]

    obstruction_columns: list[sp.Matrix] = []
    nonzero_monomials: list[str] = []
    raw_quadratic_columns: list[sp.Matrix] = []
    for (left, right), label in zip(monomial_pairs, monomial_labels):
        left_block = blocks[left]
        right_block = blocks[right]

        def ordered(first: dict[str, sp.Matrix], second: dict[str, sp.Matrix]) -> sp.Matrix:
            return (
                -first["c"] * A0_inverse * second["b"]
                + first["c"]
                * A0_inverse
                * second["a"]
                * A0_inverse
                * B0
            )

        quadratic = ordered(left_block, right_block)
        if left != right:
            quadratic += ordered(right_block, left_block)
        raw_vector = _flatten(quadratic)
        residual = _project_to_cokernel(
            raw_vector,
            L,
            pivot_rows=pivot_rows,
            pivot_columns=pivot_operation_columns,
            inverse_minor=tangent_minor_inverse,
        )
        raw_quadratic_columns.append(raw_vector)
        obstruction_columns.append(residual)
        if any(residual):
            nonzero_monomials.append(label)

    obstruction_matrix = sp.Matrix.hstack(*obstruction_columns)
    obstruction_rank = _matrix_rank(obstruction_matrix)
    obstruction_row_pivots = list(
        DomainMatrix.from_Matrix(obstruction_matrix.T, fmt="sparse").rref()[1]
    )
    if len(obstruction_row_pivots) != obstruction_rank:
        raise AssertionError("failed to select independent Kuranishi equations")

    equations = []
    equation_matrix = obstruction_matrix[obstruction_row_pivots, :]
    for equation_index in range(equation_matrix.rows):
        expression = sp.expand(
            sum(
                equation_matrix[equation_index, monomial_index]
                * parameters[left]
                * parameters[right]
                for monomial_index, (left, right) in enumerate(monomial_pairs)
            )
        )
        equations.append(expression)

    pure_row_equations = [
        expression.subs({parameters[20]: 0, parameters[21]: 0})
        for expression in equations
    ]
    if any(sp.expand(expression) != 0 for expression in pure_row_equations):
        raise AssertionError("row-zero tangent directions acquired a quadratic obstruction")

    u, v = parameters[20], parameters[21]
    A = sp.zeros(len(equations), 20)
    B = sp.zeros(len(equations), 20)
    c_u2 = sp.zeros(len(equations), 1)
    c_uv = sp.zeros(len(equations), 1)
    c_v2 = sp.zeros(len(equations), 1)
    for row, expression in enumerate(equations):
        polynomial = sp.Poly(expression, *parameters, domain=sp.QQ)
        for index in range(20):
            A[row, index] = polynomial.coeff_monomial(parameters[index] * u)
            B[row, index] = polynomial.coeff_monomial(parameters[index] * v)
        c_u2[row, 0] = polynomial.coeff_monomial(u**2)
        c_uv[row, 0] = polynomial.coeff_monomial(u * v)
        c_v2[row, 0] = polynomial.coeff_monomial(v**2)

    axis_u_ranks = _rank_pair(A, -c_u2)
    axis_v_ranks = _rank_pair(B, -c_v2)

    t = sp.symbols("t")
    generic_matrix = t * A + B
    generic_rhs = -(t**2 * c_u2 + t * c_uv + c_v2)
    generic_rank = DomainMatrix.from_Matrix(
        generic_matrix,
        fmt="sparse",
    ).to_field().rank()
    generic_augmented_rank = DomainMatrix.from_Matrix(
        generic_matrix.row_join(generic_rhs),
        fmt="sparse",
    ).to_field().rank()

    sample_ratios = []
    for ratio in (-3, -2, -1, 0, 1, 2, 3):
        matrix = ratio * A + B
        rhs = -(ratio**2 * c_u2 + ratio * c_uv + c_v2)
        ranks = _rank_pair(matrix, rhs)
        sample_ratios.append(
            {
                "u_over_v": ratio,
                "matrix_rank": ranks[0],
                "augmented_rank": ranks[1],
                "second_order_solvable": ranks[0] == ranks[1],
            }
        )

    compact_equations = []
    for index, expression in enumerate(equations):
        compact_equations.append(
            {
                "index": index,
                "source_target_row": obstruction_row_pivots[index],
                "terms": _polynomial_terms(expression, parameters),
            }
        )

    return {
        "schema_version": 1,
        "name": "Program 5 rank-six second-order Kuranishi audit",
        "source_file": str(source_path),
        "source_sha256": exported["summary"]["source_sha256"],
        "ambient_operation_dimension": 115,
        "tangent_map_rank": 93,
        "tangent_dimension": 22,
        "row_zero_subspace_dimension": 20,
        "tangent_excess_dimension": 2,
        "local_rank_chart": {
            "base_rows": [str(V[index]) for index in base_rows],
            "zero_rows": [str(V[index]) for index in zero_rows],
            "pivot_cubic_monomials": [
                _monomial_label(cubic_monomials[index]) for index in pivot_columns
            ],
            "nonpivot_column_count": len(nonpivot_columns),
            "schur_complement_equation_count": L.rows,
        },
        "quadratic_kuranishi": {
            "parameter_order": parameter_names,
            "candidate_monomial_count": len(monomial_pairs),
            "nonzero_obstruction_monomials": nonzero_monomials,
            "obstruction_coefficient_rank": obstruction_rank,
            "independent_equation_count": len(equations),
            "equations": compact_equations,
        },
        "projective_eta_ratio_analysis": {
            "u_axis": {
                "matrix_rank": axis_u_ranks[0],
                "augmented_rank": axis_u_ranks[1],
                "second_order_solvable": axis_u_ranks[0] == axis_u_ranks[1],
            },
            "v_axis": {
                "matrix_rank": axis_v_ranks[0],
                "augmented_rank": axis_v_ranks[1],
                "second_order_solvable": axis_v_ranks[0] == axis_v_ranks[1],
            },
            "generic_v_nonzero": {
                "coefficient_field": "Q(t), t=u/v",
                "matrix_rank": generic_rank,
                "augmented_rank": generic_augmented_rank,
                "second_order_solvable_generically": (
                    generic_rank == generic_augmented_rank
                ),
            },
            "rational_samples": sample_ratios,
        },
        "interpretation_boundary": (
            "Vanishing of the quadratic Kuranishi equations is necessary and "
            "sufficient for a rank-six arc through second order in the chosen "
            "Schur-complement chart. It does not establish all-order "
            "integration, polynomial realization, or the true operation-group "
            "quotient."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_second_order(args.source)
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(f"program5_rank_six_second_order: {exc}", file=sys.stderr)
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
