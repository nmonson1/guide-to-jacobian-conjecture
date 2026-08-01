#!/usr/bin/env python3
"""Scan one-parameter Program 5 rank-six tangent directions through order three.

The selected second-order-compatible plane from
``program5_rank_six_formal_arc.py`` has basis

    theta_u = eta_0 + xi_4,
    theta_v = eta_1 + 4 xi_0 - 24 xi_1 - 4 xi_4.

The full two-parameter plane has a certified cubic obstruction, but that does
not by itself classify its projective tangent lines.  For each finite ratio
``r=u/v`` this adapter studies the one-parameter direction

    theta(r) = theta_v + r theta_u,

and separately studies the point at infinity ``theta_u``.  It solves the
second-order equation, permits every element of the 22-dimensional rank-six
tangent kernel in the quadratic correction, and tests the resulting cubic
linear system exactly over Q.

This is a formal local rank-at-most-six calculation in the fixed Schur chart.
It does not impose the quartic compression equation, identify the true
operation-group quotient, or prove convergence/algebraization.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from itertools import combinations_with_replacement
from pathlib import Path
from typing import Any, Iterable, Sequence

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


def _rank_pair(matrix: sp.Matrix, rhs: sp.Matrix) -> tuple[int, int]:
    return (
        DomainMatrix.from_Matrix(matrix, fmt="sparse").rank(),
        DomainMatrix.from_Matrix(matrix.row_join(rhs), fmt="sparse").rank(),
    )


def _deterministic_solution(
    matrix: sp.Matrix,
    rhs: sp.Matrix,
) -> tuple[bool, sp.Matrix | None, int, int, int]:
    rank, augmented_rank = _rank_pair(matrix, rhs)
    if rank != augmented_rank:
        return False, None, rank, augmented_rank, matrix.cols - rank
    solution_tuple = next(iter(sp.linsolve((matrix, rhs))))
    free_symbols = sorted(
        set().union(*(entry.free_symbols for entry in solution_tuple)),
        key=str,
    )
    solution = sp.Matrix(
        [
            sp.factor(entry.subs({symbol: 0 for symbol in free_symbols}))
            for entry in solution_tuple
        ]
    )
    if matrix * solution != rhs:
        raise AssertionError("deterministic tangent solution failed")
    return True, solution, rank, augmented_rank, len(free_symbols)


def analyze_line_scan(
    source_path: Path = DEFAULT_SOURCE,
    *,
    ratios: Iterable[int | sp.Rational] = (-3, -2, -1, 0, 1, 2, 3),
    verify_axes: bool = True,
) -> dict[str, Any]:
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

    tangent_blocks = [blocks(vector) for vector in tangent_basis]

    def quadratic_forcing(theta_block: dict[str, sp.Matrix]) -> sp.Matrix:
        G1 = -G0 * theta_block["A"] * G0
        return (
            theta_block["C"] * G0 * theta_block["B"]
            + theta_block["C"] * G1 * B0
        )

    def cubic_forcing(
        theta_block: dict[str, sp.Matrix],
        p2_block: dict[str, sp.Matrix],
    ) -> sp.Matrix:
        G1 = -G0 * theta_block["A"] * G0
        G2 = -G0 * (
            theta_block["A"] * G1 + p2_block["A"] * G0
        )
        return (
            theta_block["C"] * G0 * p2_block["B"]
            + theta_block["C"] * G1 * theta_block["B"]
            + theta_block["C"] * G2 * B0
            + p2_block["C"] * G0 * theta_block["B"]
            + p2_block["C"] * G1 * B0
        )

    def bilinear_effect(
        tangent_block: dict[str, sp.Matrix],
        theta_block: dict[str, sp.Matrix],
    ) -> sp.Matrix:
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
            raise AssertionError("invalid line obstruction witness")
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
            "pairing_with_rhs": _q(pairing),
            "nonzero_count": len(coordinates),
            "witness_sha256": _digest(witness),
            "coordinates": coordinates,
        }

    def analyze_direction(
        name: str,
        theta: sp.Matrix,
        *,
        ratio: int | sp.Rational | None,
        verify_effect: bool,
    ) -> dict[str, Any]:
        theta_block = blocks(theta)
        H2 = quadratic_forcing(theta_block)
        second_residual = project(_flatten(H2))
        second_order_compatible = not any(second_residual)
        result: dict[str, Any] = {
            "name": name,
            "u_over_v": ratio if ratio is not None else "infinity",
            "first_order_nonzero_count": len(_sparse_vector(theta, labels)),
            "first_order_sha256": _digest(theta),
            "second_order_compatible": second_order_compatible,
        }
        if not second_order_compatible:
            result["first_obstructed_order"] = 2
            result["second_order_obstruction_rank"] = _matrix_rank(second_residual)
            return result

        P2 = solve_image(H2)
        P2_block = blocks(P2)
        H3 = cubic_forcing(theta_block, P2_block)
        cubic_residual = project(_flatten(H3))
        effect_columns = [
            project(_flatten(bilinear_effect(tangent_block, theta_block)))
            for tangent_block in tangent_blocks
        ]
        if verify_effect:
            for tangent_index, tangent_block in enumerate(tangent_blocks):
                perturbed_block = {
                    key: P2_block[key] + tangent_block[key]
                    for key in P2_block
                }
                observed = project(
                    _flatten(cubic_forcing(theta_block, perturbed_block))
                ) - cubic_residual
                if observed != effect_columns[tangent_index]:
                    raise AssertionError(
                        "direct line-effect replay disagrees in tangent column "
                        f"{tangent_index} for {name}"
                    )

        active_rows = sorted(
            {
                row
                for row, value in enumerate(cubic_residual)
                if value
            }
            | {
                row
                for column in effect_columns
                for row, value in enumerate(column)
                if value
            }
        )
        effect_matrix = sp.Matrix(
            [
                [column[row, 0] for column in effect_columns]
                for row in active_rows
            ]
        )
        rhs = sp.Matrix([-cubic_residual[row, 0] for row in active_rows])
        solvable, solution, rank, augmented_rank, free_dimension = (
            _deterministic_solution(effect_matrix, rhs)
        )
        result.update(
            {
                "quadratic_tangent_freedom_dimension": 22,
                "compressed_cubic_equation_count": len(active_rows),
                "cubic_effect_rank": rank,
                "cubic_augmented_rank": augmented_rank,
                "cubic_lift_solvable": solvable,
                "cubic_lift_solution_free_dimension": (
                    free_dimension if solvable else None
                ),
                "direct_effect_columns_verified": 22 if verify_effect else 0,
            }
        )
        if not solvable or solution is None:
            result["first_obstructed_order"] = 3
            result["cubic_obstruction_certificate"] = obstruction_certificate(
                effect_matrix,
                rhs,
                active_rows,
                order=3,
            )
            return result

        tangent_adjustment = sp.zeros(115, 1)
        coefficients = []
        for index, tangent_vector in enumerate(tangent_basis):
            coefficient = solution[index, 0]
            if coefficient:
                tangent_adjustment += coefficient * tangent_vector
                coefficients.append(
                    {
                        "tangent_basis_index": index,
                        "coefficient": _q(coefficient),
                    }
                )
        adjusted_P2 = P2 + tangent_adjustment
        adjusted_H3 = cubic_forcing(theta_block, blocks(adjusted_P2))
        adjusted_residual = project(_flatten(adjusted_H3))
        if any(adjusted_residual):
            raise AssertionError("solved tangent adjustment left a cubic residual")
        P3 = solve_image(adjusted_H3)
        result.update(
            {
                "maximum_compatible_order": 3,
                "quadratic_tangent_adjustment": {
                    "coefficient_count": len(coefficients),
                    "coefficients": coefficients,
                    "nonzero_count": len(_sparse_vector(tangent_adjustment, labels)),
                    "sha256": _digest(tangent_adjustment),
                },
                "adjusted_quadratic_correction": {
                    "nonzero_count": len(_sparse_vector(adjusted_P2, labels)),
                    "sha256": _digest(adjusted_P2),
                },
                "cubic_correction": {
                    "nonzero_count": len(_sparse_vector(P3, labels)),
                    "sha256": _digest(P3),
                },
            }
        )
        return result

    finite_results = []
    normalized_ratios = [sp.Rational(value) for value in ratios]
    for ratio in normalized_ratios:
        finite_results.append(
            analyze_direction(
                f"theta_v + ({ratio}) theta_u",
                theta_v + ratio * theta_u,
                ratio=ratio,
                verify_effect=verify_axes and ratio == 0,
            )
        )
    infinity_result = analyze_direction(
        "theta_u",
        theta_u,
        ratio=None,
        verify_effect=verify_axes,
    )

    return {
        "schema_version": 1,
        "name": "Program 5 projective rank-six line scan through cubic order",
        "source_file": str(source_path),
        "source_sha256": exported["summary"]["source_sha256"],
        "ambient_operation_dimension": 115,
        "rank_six_tangent_dimension": 22,
        "selected_plane": {
            "theta_u": "eta_0 + xi_4",
            "theta_v": "eta_1 + 4*xi_0 - 24*xi_1 - 4*xi_4",
        },
        "finite_ratio_results": finite_results,
        "infinity_result": infinity_result,
        "interpretation_boundary": (
            "Each entry decides formal compatibility through cubic parameter "
            "order for one selected projective tangent direction after all "
            "quadratic tangent freedom is allowed. The finite sample is not a "
            "classification of every rational or algebraic ratio."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--ratios",
        default="-3,-2,-1,0,1,2,3",
        help="comma-separated rational values u/v",
    )
    parser.add_argument(
        "--skip-direct-effect-checks",
        action="store_true",
    )
    args = parser.parse_args(argv)
    try:
        ratios = [sp.Rational(value.strip()) for value in args.ratios.split(",")]
        result = analyze_line_scan(
            args.source,
            ratios=ratios,
            verify_axes=not args.skip_direct_effect_checks,
        )
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(f"program5_rank_six_line_scan: {exc}", file=sys.stderr)
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
