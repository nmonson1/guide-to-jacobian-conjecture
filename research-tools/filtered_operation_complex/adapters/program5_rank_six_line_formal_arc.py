#!/usr/bin/env python3
"""Lift a one-parameter Program 5 rank-six tangent line order by order.

The projective line scan shows that the selected finite directions are
intrinsically obstructed at cubic parameter order, while the point at infinity

    theta_u = eta_0 + xi_4

survives after the complete 22-dimensional tangent freedom in the quadratic
correction is used.  This adapter continues that line recursively.

For a one-parameter expansion

    P(t) = P0 + sum_{n>=1} P_n t^n,

it solves the Schur-complement equation at order n, then uses the full tangent
kernel in P_n to kill the order-(n+1) cokernel class.  The linear effect of
that tangent adjustment is the same bilinear map at every order, namely the
polarization of the quadratic Kuranishi map with the fixed first-order
direction.

The output is an exact formal local rank-at-most-six audit.  It does not impose
the quartic compression equation, identify the true operation-group quotient,
or prove convergence or algebraization.
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


def _digest(vector: sp.Matrix) -> str:
    payload = [str(sp.Rational(value)) for value in vector]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _sparse_vector(
    vector: sp.Matrix,
    labels: Sequence[str],
) -> list[dict[str, Any]]:
    return [
        {"coordinate": labels[index], "coefficient": _q(vector[index, 0])}
        for index in range(vector.rows)
        if vector[index, 0] != 0
    ]


def _deterministic_solution(
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
        raise AssertionError("deterministic tangent solution failed")
    return True, solution, rank, augmented_rank, len(free_symbols)


def analyze_line_formal_arc(
    source_path: Path = DEFAULT_SOURCE,
    *,
    ratio: int | sp.Rational | None = None,
    max_order: int = 8,
    verify_effect: bool = True,
) -> dict[str, Any]:
    if max_order < 3:
        raise ValueError("max_order must be at least three")

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
    if ratio is None:
        theta = theta_u
        direction_label = "theta_u"
        projective_ratio: Any = "infinity"
    else:
        rational_ratio = sp.Rational(ratio)
        theta = theta_v + rational_ratio * theta_u
        direction_label = f"theta_v + ({rational_ratio}) theta_u"
        projective_ratio = _q(rational_ratio)

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
    if M0.rank() != 6:
        raise AssertionError("base cubic-coordinate matrix lost rank six")

    base_rows = [0, 1, 2, 4, 5, 8]
    zero_rows = [3, 6, 7, 9, 10]
    base_matrix = M0[base_rows, :]
    _, pivot_tuple = base_matrix.rref()
    pivot_columns = list(pivot_tuple)
    if len(pivot_columns) != 6:
        raise AssertionError("the fixed Schur minor lost rank six")
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
    L = sp.Matrix.hstack(
        *[
            _flatten(block["D"] - block["C"] * G0 * B0)
            for block in ambient_blocks
        ]
    )
    if _matrix_rank(L) != 93:
        raise AssertionError("rank-six tangent map changed")
    for vector in tangent_basis:
        if L * vector != sp.zeros(L.rows, 1):
            raise AssertionError("adapted tangent basis left ker(L)")
    pivot_rows, pivot_operation_columns = _independent_rows_and_columns(L)
    minor = L[pivot_rows, pivot_operation_columns]
    minor_inverse = minor.inv()

    def project(forcing: sp.Matrix) -> sp.Matrix:
        return _project_to_cokernel(
            forcing,
            L,
            pivot_rows=pivot_rows,
            pivot_columns=pivot_operation_columns,
            inverse_minor=minor_inverse,
        )

    def solve_image(forcing_matrix: sp.Matrix) -> sp.Matrix:
        forcing = _flatten(forcing_matrix)
        residual = project(forcing)
        if any(residual):
            raise AssertionError("forcing is not in the tangent image")
        coefficients = minor_inverse * forcing[list(pivot_rows), :]
        correction = sp.zeros(115, 1)
        for index, column in enumerate(pivot_operation_columns):
            correction[column, 0] = coefficients[index, 0]
        if L * correction != forcing:
            raise AssertionError("deterministic image solution failed")
        return correction

    theta_block = blocks(theta)
    tangent_blocks = [blocks(vector) for vector in tangent_basis]

    def bilinear_effect(tangent_block: dict[str, sp.Matrix]) -> sp.Matrix:
        return (
            tangent_block["C"] * G0 * theta_block["B"]
            - tangent_block["C"]
            * G0
            * theta_block["A"]
            * G0
            * B0
            + theta_block["C"] * G0 * tangent_block["B"]
            - theta_block["C"]
            * G0
            * tangent_block["A"]
            * G0
            * B0
        )

    effect_columns = [
        project(_flatten(bilinear_effect(tangent_block)))
        for tangent_block in tangent_blocks
    ]
    effect_rows = sorted(
        {
            row
            for column in effect_columns
            for row, value in enumerate(column)
            if value
        }
    )
    base_effect_matrix = sp.Matrix(
        [
            [column[row, 0] for column in effect_columns]
            for row in effect_rows
        ]
    )
    effect_rank = DomainMatrix.from_Matrix(
        base_effect_matrix,
        fmt="sparse",
    ).rank()

    P_series: dict[int, sp.Matrix] = {1: theta}
    A_series: dict[int, sp.Matrix] = {}
    B_series: dict[int, sp.Matrix] = {0: B0}
    C_series: dict[int, sp.Matrix] = {}
    D_series: dict[int, sp.Matrix] = {}
    G_series: dict[int, sp.Matrix] = {0: G0}

    def record_blocks(order: int) -> None:
        block = blocks(P_series[order])
        A_series[order] = block["A"]
        B_series[order] = block["B"]
        C_series[order] = block["C"]
        D_series[order] = block["D"]

    def compute_inverse_order(order: int) -> None:
        total = sp.zeros(6, 6)
        for left_order in range(1, order + 1):
            total += A_series[left_order] * G_series[order - left_order]
        G_series[order] = -G0 * total

    def forcing(order: int) -> sp.Matrix:
        value = sp.zeros(len(zero_rows), len(nonpivot_columns))
        for i_order in range(1, order):
            for j_order in range(0, order - i_order + 1):
                k_order = order - i_order - j_order
                if (
                    i_order in C_series
                    and j_order in G_series
                    and k_order in B_series
                ):
                    value += (
                        C_series[i_order]
                        * G_series[j_order]
                        * B_series[k_order]
                    )
        return value

    def solve_tangent_adjustment(
        residual: sp.Matrix,
    ) -> tuple[
        bool,
        sp.Matrix | None,
        int,
        int,
        int,
        list[int],
        sp.Matrix,
        sp.Matrix,
    ]:
        active_rows = sorted(
            set(effect_rows)
            | {row for row, value in enumerate(residual) if value}
        )
        matrix = sp.Matrix(
            [
                [column[row, 0] for column in effect_columns]
                for row in active_rows
            ]
        )
        rhs = sp.Matrix([-residual[row, 0] for row in active_rows])
        solvable, solution, rank, augmented_rank, free_dimension = (
            _deterministic_solution(matrix, rhs)
        )
        return (
            solvable,
            solution,
            rank,
            augmented_rank,
            free_dimension,
            active_rows,
            matrix,
            rhs,
        )

    def obstruction_certificate(
        matrix: sp.Matrix,
        rhs: sp.Matrix,
        active_rows: Sequence[int],
        *,
        order: int,
    ) -> dict[str, Any]:
        witness = next(
            (
                vector
                for vector in matrix.T.nullspace()
                if (vector.T * rhs)[0, 0] != 0
            ),
            None,
        )
        if witness is None:
            raise AssertionError("rank mismatch has no left-null witness")
        first_nonzero = next(value for value in witness if value != 0)
        witness = sp.Matrix([sp.factor(value / first_nonzero) for value in witness])
        pairing = sp.factor((witness.T * rhs)[0, 0])
        if witness.T * matrix != sp.zeros(1, matrix.cols) or pairing == 0:
            raise AssertionError("invalid higher-order obstruction witness")
        coordinates = []
        for local_row, coefficient in enumerate(witness):
            if coefficient == 0:
                continue
            residual_row = active_rows[local_row]
            schur_row, schur_column = divmod(
                residual_row,
                len(nonpivot_columns),
            )
            coordinates.append(
                {
                    "parameter_monomial": f"t^{order}",
                    "schur_row_variable": str(V[zero_rows[schur_row]]),
                    "schur_column_monomial": _monomial_label(
                        cubic_monomials[nonpivot_columns[schur_column]]
                    ),
                    "coefficient": _q(coefficient),
                }
            )
        return {
            "kind": "exact left-null witness",
            "order": order,
            "pairing_with_rhs": _q(pairing),
            "nonzero_count": len(coordinates),
            "witness_sha256": _digest(witness),
            "coordinates": coordinates,
        }

    record_blocks(1)
    compute_inverse_order(1)

    H2 = forcing(2)
    residual2 = project(_flatten(H2))
    if any(residual2):
        return {
            "schema_version": 1,
            "name": "Program 5 one-parameter formal rank-six arc",
            "source_file": str(source_path),
            "source_sha256": exported["summary"]["source_sha256"],
            "direction": direction_label,
            "u_over_v": projective_ratio,
            "maximum_requested_order": max_order,
            "maximum_compatible_order": 1,
            "first_obstructed_order": 2,
            "second_order_obstruction_rank": _matrix_rank(residual2),
        }
    P_series[2] = solve_image(H2)
    record_blocks(2)
    compute_inverse_order(2)

    if verify_effect:
        base_H3 = forcing(3)
        base_residual3 = project(_flatten(base_H3))
        original = P_series[2]
        original_block = {
            "A": A_series[2].copy(),
            "B": B_series[2].copy(),
            "C": C_series[2].copy(),
            "D": D_series[2].copy(),
        }
        original_G2 = G_series[2].copy()
        for tangent_index, tangent_vector in enumerate(tangent_basis):
            P_series[2] = original + tangent_vector
            record_blocks(2)
            compute_inverse_order(2)
            observed = project(_flatten(forcing(3))) - base_residual3
            if observed != effect_columns[tangent_index]:
                raise AssertionError(
                    "direct recursive effect replay disagrees in tangent "
                    f"column {tangent_index}"
                )
        P_series[2] = original
        A_series[2] = original_block["A"]
        B_series[2] = original_block["B"]
        C_series[2] = original_block["C"]
        D_series[2] = original_block["D"]
        G_series[2] = original_G2

    orders: list[dict[str, Any]] = [
        {
            "order": 1,
            "compatible": True,
            "correction": {
                "nonzero_count": len(_sparse_vector(theta, labels)),
                "sha256": _digest(theta),
                "vector": _sparse_vector(theta, labels),
            },
        },
        {
            "order": 2,
            "compatible": True,
            "provisional_correction": {
                "nonzero_count": len(_sparse_vector(P_series[2], labels)),
                "sha256": _digest(P_series[2]),
            },
        },
    ]
    first_obstructed_order: int | None = None
    obstruction: dict[str, Any] | None = None

    for order in range(3, max_order + 1):
        H_order = forcing(order)
        residual = project(_flatten(H_order))
        (
            solvable,
            solution,
            rank,
            augmented_rank,
            free_dimension,
            active_rows,
            matrix,
            rhs,
        ) = solve_tangent_adjustment(residual)
        if not solvable or solution is None:
            first_obstructed_order = order
            obstruction = obstruction_certificate(
                matrix,
                rhs,
                active_rows,
                order=order,
            )
            orders.append(
                {
                    "order": order,
                    "compatible": False,
                    "effect_rank": rank,
                    "augmented_rank": augmented_rank,
                    "obstruction_certificate": obstruction,
                }
            )
            break

        adjustment = sp.zeros(115, 1)
        adjustment_coefficients = []
        for tangent_index, tangent_vector in enumerate(tangent_basis):
            coefficient = solution[tangent_index, 0]
            if coefficient:
                adjustment += coefficient * tangent_vector
                adjustment_coefficients.append(
                    {
                        "tangent_basis_index": tangent_index,
                        "coefficient": _q(coefficient),
                    }
                )
        P_series[order - 1] += adjustment
        record_blocks(order - 1)
        compute_inverse_order(order - 1)

        adjusted_H = forcing(order)
        adjusted_residual = project(_flatten(adjusted_H))
        if any(adjusted_residual):
            raise AssertionError(
                f"the order-{order} tangent adjustment left a residual"
            )
        P_series[order] = solve_image(adjusted_H)
        record_blocks(order)
        compute_inverse_order(order)

        orders[-1]["finalized_correction"] = {
            "nonzero_count": len(_sparse_vector(P_series[order - 1], labels)),
            "sha256": _digest(P_series[order - 1]),
        }
        orders[-1]["tangent_adjustment"] = {
            "coefficient_count": len(adjustment_coefficients),
            "coefficients": adjustment_coefficients,
            "nonzero_count": len(_sparse_vector(adjustment, labels)),
            "sha256": _digest(adjustment),
        }
        orders.append(
            {
                "order": order,
                "compatible": True,
                "effect_rank": rank,
                "augmented_rank": augmented_rank,
                "tangent_solution_free_dimension": free_dimension,
                "provisional_correction": {
                    "nonzero_count": len(_sparse_vector(P_series[order], labels)),
                    "sha256": _digest(P_series[order]),
                },
            }
        )

    compatible_orders = [item["order"] for item in orders if item["compatible"]]
    result: dict[str, Any] = {
        "schema_version": 1,
        "name": "Program 5 one-parameter formal rank-six arc",
        "source_file": str(source_path),
        "source_sha256": exported["summary"]["source_sha256"],
        "ambient_operation_dimension": 115,
        "rank_six_tangent_dimension": 22,
        "direction": direction_label,
        "u_over_v": projective_ratio,
        "fixed_tangent_effect_rank": effect_rank,
        "direct_effect_columns_verified": 22 if verify_effect else 0,
        "maximum_requested_order": max_order,
        "maximum_compatible_order": max(compatible_orders),
        "first_obstructed_order": first_obstructed_order,
        "orders": orders,
        "interpretation_boundary": (
            "Compatibility through order N is formal and local in the fixed "
            "rank-six Schur chart. It does not impose Lambda_4=0, classify the "
            "true operation quotient, or prove convergence/algebraization."
        ),
    }
    if obstruction is not None:
        result["obstruction_certificate"] = obstruction
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument(
        "--ratio",
        help="finite rational u/v; omit for the point at infinity theta_u",
    )
    parser.add_argument("--max-order", type=int, default=8)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--skip-direct-effect-check", action="store_true")
    args = parser.parse_args(argv)
    try:
        ratio = None if args.ratio is None else sp.Rational(args.ratio)
        result = analyze_line_formal_arc(
            args.source,
            ratio=ratio,
            max_order=args.max_order,
            verify_effect=not args.skip_direct_effect_check,
        )
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(f"program5_rank_six_line_formal_arc: {exc}", file=sys.stderr)
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
