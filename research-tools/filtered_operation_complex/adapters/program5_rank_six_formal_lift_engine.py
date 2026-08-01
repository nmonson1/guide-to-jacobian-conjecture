"""Reusable one-parameter formal lift engine for the Program 5 Schur model.

Given a first-order tangent vector ``theta`` in the rank-six tangent kernel,
this module recursively constructs

    P(t) = P0 + theta*t + P2*t^2 + P3*t^3 + ...

inside the fixed rank-six Schur chart.  At each order it first solves the
linear image equation, then uses every vector in the 22-dimensional tangent
kernel to remove the next cokernel class.  A failed rank test is accompanied
by an exact left-null certificate.

This is internal research infrastructure.  It audits formal rank-at-most-six
compatibility only; it does not impose the quartic compression equation or
prove convergence/algebraization.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any, Sequence

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from .program5_compression_export import _q
from .program5_rank_six_second_order import _flatten


def _digest(vector: sp.Matrix) -> str:
    payload = [str(sp.factor(sp.cancel(value))) for value in vector]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _nonzero_count(vector: sp.Matrix) -> int:
    return sum(sp.factor(sp.cancel(value)) != 0 for value in vector)


def _rank_pair(matrix: sp.Matrix, rhs: sp.Matrix) -> tuple[int, int]:
    return (
        DomainMatrix.from_Matrix(matrix, fmt="sparse").rank(),
        DomainMatrix.from_Matrix(
            matrix.row_join(rhs),
            fmt="sparse",
        ).rank(),
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
    substitution = {symbol: 0 for symbol in free_symbols}
    solution = sp.Matrix(
        [
            sp.factor(sp.cancel(entry.subs(substitution)))
            for entry in solution_tuple
        ]
    )
    error = (matrix * solution - rhs).applyfunc(
        lambda value: sp.factor(sp.cancel(value))
    )
    if any(value != 0 for value in error):
        raise AssertionError("deterministic tangent solution failed")
    return True, solution, rank, augmented_rank, len(free_symbols)


def _obstruction_certificate(
    matrix: sp.Matrix,
    rhs: sp.Matrix,
    active_rows: Sequence[int],
    model: Any,
    *,
    order: int,
) -> dict[str, Any]:
    witness = next(
        (
            vector
            for vector in matrix.T.nullspace()
            if sp.factor(sp.cancel((vector.T * rhs)[0, 0])) != 0
        ),
        None,
    )
    if witness is None:
        raise AssertionError("rank mismatch has no left-null witness")
    first_nonzero = next(value for value in witness if value != 0)
    witness = sp.Matrix(
        [
            sp.factor(sp.cancel(value / first_nonzero))
            for value in witness
        ]
    )
    annihilation = (witness.T * matrix).applyfunc(
        lambda value: sp.factor(sp.cancel(value))
    )
    pairing = sp.factor(sp.cancel((witness.T * rhs)[0, 0]))
    if any(value != 0 for value in annihilation) or pairing == 0:
        raise AssertionError("invalid formal-lift obstruction witness")
    coordinates = []
    for local_row, coefficient in enumerate(witness):
        if coefficient == 0:
            continue
        coordinates.append(
            {
                "parameter_monomial": f"t^{order}",
                **model.residual_coordinate(active_rows[local_row]),
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


def lift_formal_direction(
    model: Any,
    theta: sp.Matrix,
    *,
    name: str,
    max_order: int = 4,
    verify_effect: bool = False,
) -> dict[str, Any]:
    """Lift one tangent direction or return its first exact obstruction."""
    if max_order < 2:
        raise ValueError("max_order must be at least two")
    if model.L * theta != sp.zeros(model.L.rows, 1):
        raise AssertionError("first-order direction is not in ker(L)")

    tangent_basis = model.tangent_basis
    theta_block = model.blocks(theta)
    tangent_blocks = [model.blocks(vector) for vector in tangent_basis]
    effect_columns = [
        model.project(
            _flatten(model.bilinear_effect(tangent_block, theta_block))
        )
        for tangent_block in tangent_blocks
    ]
    effect_rows = sorted(
        {
            row
            for column in effect_columns
            for row, value in enumerate(column)
            if value != 0
        }
    )
    base_effect_matrix = sp.Matrix(
        [
            [column[row, 0] for column in effect_columns]
            for row in effect_rows
        ]
    )
    fixed_effect_rank = DomainMatrix.from_Matrix(
        base_effect_matrix,
        fmt="sparse",
    ).rank()

    P_series: dict[int, sp.Matrix] = {1: theta}
    A_series: dict[int, sp.Matrix] = {}
    B_series: dict[int, sp.Matrix] = {0: model.B0}
    C_series: dict[int, sp.Matrix] = {}
    D_series: dict[int, sp.Matrix] = {}
    G_series: dict[int, sp.Matrix] = {0: model.G0}

    def record_blocks(order: int) -> None:
        block = model.blocks(P_series[order])
        A_series[order] = block["A"]
        B_series[order] = block["B"]
        C_series[order] = block["C"]
        D_series[order] = block["D"]

    def compute_inverse_order(order: int) -> None:
        total = sp.zeros(6, 6)
        for left_order in range(1, order + 1):
            total += A_series[left_order] * G_series[order - left_order]
        G_series[order] = (-model.G0 * total).applyfunc(
            lambda value: sp.factor(sp.cancel(value))
        )

    def forcing(order: int) -> sp.Matrix:
        value = sp.zeros(len(model.zero_rows), len(model.nonpivot_columns))
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
        return value.applyfunc(lambda entry: sp.factor(sp.cancel(entry)))

    def tangent_system(
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
            | {row for row, value in enumerate(residual) if value != 0}
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

    record_blocks(1)
    compute_inverse_order(1)
    H2 = forcing(2)
    residual2 = model.project(_flatten(H2))
    if any(value != 0 for value in residual2):
        return {
            "name": name,
            "maximum_requested_order": max_order,
            "maximum_compatible_order": 1,
            "first_obstructed_order": 2,
            "fixed_tangent_effect_rank": fixed_effect_rank,
            "direct_effect_columns_verified": 0,
            "orders": [
                {"order": 1, "compatible": True},
                {
                    "order": 2,
                    "compatible": False,
                    "obstruction_rank": DomainMatrix.from_Matrix(
                        residual2,
                        fmt="sparse",
                    ).rank(),
                },
            ],
        }

    P_series[2] = model.solve_image(H2)
    record_blocks(2)
    compute_inverse_order(2)

    verified_columns = 0
    if verify_effect and max_order >= 3:
        base_residual = model.project(_flatten(forcing(3)))
        original = P_series[2]
        original_blocks = {
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
            observed = model.project(_flatten(forcing(3))) - base_residual
            observed = observed.applyfunc(
                lambda value: sp.factor(sp.cancel(value))
            )
            expected = effect_columns[tangent_index]
            if observed != expected:
                raise AssertionError(
                    "direct formal effect replay disagrees in tangent column "
                    f"{tangent_index}"
                )
            verified_columns += 1
        P_series[2] = original
        A_series[2] = original_blocks["A"]
        B_series[2] = original_blocks["B"]
        C_series[2] = original_blocks["C"]
        D_series[2] = original_blocks["D"]
        G_series[2] = original_G2

    orders: list[dict[str, Any]] = [
        {
            "order": 1,
            "compatible": True,
            "correction_nonzero_count": _nonzero_count(theta),
            "correction_sha256": _digest(theta),
        },
        {
            "order": 2,
            "compatible": True,
            "provisional_correction_nonzero_count": _nonzero_count(P_series[2]),
            "provisional_correction_sha256": _digest(P_series[2]),
        },
    ]
    first_obstructed_order: int | None = None
    obstruction: dict[str, Any] | None = None

    for order in range(3, max_order + 1):
        residual = model.project(_flatten(forcing(order)))
        (
            solvable,
            solution,
            rank,
            augmented_rank,
            free_dimension,
            active_rows,
            matrix,
            rhs,
        ) = tangent_system(residual)
        if not solvable or solution is None:
            first_obstructed_order = order
            obstruction = _obstruction_certificate(
                matrix,
                rhs,
                active_rows,
                model,
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

        adjustment = sp.zeros(model.ambient_operation_dimension, 1)
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

        adjusted_forcing = forcing(order)
        adjusted_residual = model.project(_flatten(adjusted_forcing))
        if any(value != 0 for value in adjusted_residual):
            raise AssertionError(
                f"the order-{order} tangent adjustment left a residual"
            )
        P_series[order] = model.solve_image(adjusted_forcing)
        record_blocks(order)
        compute_inverse_order(order)

        orders[-1]["finalized_correction_nonzero_count"] = _nonzero_count(
            P_series[order - 1]
        )
        orders[-1]["finalized_correction_sha256"] = _digest(
            P_series[order - 1]
        )
        orders[-1]["tangent_adjustment_coefficient_count"] = len(
            adjustment_coefficients
        )
        orders[-1]["tangent_adjustment_coefficients"] = adjustment_coefficients
        orders.append(
            {
                "order": order,
                "compatible": True,
                "effect_rank": rank,
                "augmented_rank": augmented_rank,
                "tangent_solution_free_dimension": free_dimension,
                "provisional_correction_nonzero_count": _nonzero_count(
                    P_series[order]
                ),
                "provisional_correction_sha256": _digest(P_series[order]),
            }
        )

    compatible_orders = [item["order"] for item in orders if item["compatible"]]
    result: dict[str, Any] = {
        "name": name,
        "maximum_requested_order": max_order,
        "maximum_compatible_order": max(compatible_orders),
        "first_obstructed_order": first_obstructed_order,
        "fixed_tangent_effect_rank": fixed_effect_rank,
        "direct_effect_columns_verified": verified_columns,
        "orders": orders,
    }
    if obstruction is not None:
        result["obstruction_certificate"] = obstruction
    return result
