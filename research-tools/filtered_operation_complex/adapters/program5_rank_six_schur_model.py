"""Shared exact Schur-complement model for the Program 5 rank-six locus.

This module reconstructs the public 115-dimensional quadratic source-field
space, the rank-six base coefficient matrix, its fixed invertible 6-by-6
minor, the rank-93 tangent operator, and the adapted 20+2 tangent splitting.
It is intentionally internal research infrastructure for the higher Kuranishi
audits; it does not add a new mathematical claim by itself.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement
from pathlib import Path
from typing import Any, Sequence

import sympy as sp

from .program5_compression_export import (
    DEFAULT_SOURCE,
    _load_source,
    _monomial_label,
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


@dataclass
class Program5RankSixSchurModel:
    source_path: Path
    source_sha256: str
    V: tuple[sp.Symbol, ...]
    labels: list[str]
    cubic_monomials: list[sp.Expr]
    variation_matrices: list[sp.Matrix]
    base_rows: list[int]
    zero_rows: list[int]
    pivot_columns: list[int]
    nonpivot_columns: list[int]
    G0: sp.Matrix
    B0: sp.Matrix
    L: sp.Matrix
    pivot_rows: tuple[int, ...]
    pivot_operation_columns: tuple[int, ...]
    minor_inverse: sp.Matrix
    tangent_basis: list[sp.Matrix]
    row_basis: list[sp.Matrix]
    eta0: sp.Matrix
    eta1: sp.Matrix
    theta_u: sp.Matrix
    theta_v: sp.Matrix

    @property
    def ambient_operation_dimension(self) -> int:
        return len(self.labels)

    @property
    def residual_dimension(self) -> int:
        return self.L.rows

    def variation(self, vector: sp.Matrix) -> sp.Matrix:
        result = sp.zeros(len(self.V), len(self.cubic_monomials))
        for coefficient, matrix in zip(vector, self.variation_matrices):
            if coefficient:
                result += coefficient * matrix
        return result

    def blocks(self, vector: sp.Matrix) -> dict[str, sp.Matrix]:
        matrix = self.variation(vector)
        return {
            "A": matrix[self.base_rows, self.pivot_columns],
            "B": matrix[self.base_rows, self.nonpivot_columns],
            "C": matrix[self.zero_rows, self.pivot_columns],
            "D": matrix[self.zero_rows, self.nonpivot_columns],
        }

    def project(self, forcing: sp.Matrix) -> sp.Matrix:
        return _project_to_cokernel(
            forcing,
            self.L,
            pivot_rows=self.pivot_rows,
            pivot_columns=self.pivot_operation_columns,
            inverse_minor=self.minor_inverse,
        )

    def solve_image(self, forcing_matrix: sp.Matrix) -> sp.Matrix:
        forcing = _flatten(forcing_matrix)
        residual = self.project(forcing)
        if any(sp.factor(value) != 0 for value in residual):
            raise AssertionError("forcing is not in the tangent image")
        coefficients = self.minor_inverse * forcing[list(self.pivot_rows), :]
        correction = sp.zeros(self.ambient_operation_dimension, 1)
        for index, column in enumerate(self.pivot_operation_columns):
            correction[column, 0] = coefficients[index, 0]
        if self.L * correction != forcing:
            raise AssertionError("deterministic image solution failed")
        return correction

    def quadratic_forcing(
        self,
        theta_block: dict[str, sp.Matrix],
    ) -> sp.Matrix:
        G1 = -self.G0 * theta_block["A"] * self.G0
        return (
            theta_block["C"] * self.G0 * theta_block["B"]
            + theta_block["C"] * G1 * self.B0
        )

    def cubic_forcing(
        self,
        theta_block: dict[str, sp.Matrix],
        p2_block: dict[str, sp.Matrix],
    ) -> sp.Matrix:
        G1 = -self.G0 * theta_block["A"] * self.G0
        G2 = -self.G0 * (
            theta_block["A"] * G1 + p2_block["A"] * self.G0
        )
        return (
            theta_block["C"] * self.G0 * p2_block["B"]
            + theta_block["C"] * G1 * theta_block["B"]
            + theta_block["C"] * G2 * self.B0
            + p2_block["C"] * self.G0 * theta_block["B"]
            + p2_block["C"] * G1 * self.B0
        )

    def bilinear_effect(
        self,
        tangent_block: dict[str, sp.Matrix],
        theta_block: dict[str, sp.Matrix],
    ) -> sp.Matrix:
        return (
            tangent_block["C"] * self.G0 * theta_block["B"]
            - tangent_block["C"]
            * self.G0
            * theta_block["A"]
            * self.G0
            * self.B0
            + theta_block["C"] * self.G0 * tangent_block["B"]
            - theta_block["C"]
            * self.G0
            * tangent_block["A"]
            * self.G0
            * self.B0
        )

    def residual_coordinate(self, residual_row: int) -> dict[str, str]:
        schur_row, schur_column = divmod(
            residual_row,
            len(self.nonpivot_columns),
        )
        return {
            "schur_row_variable": str(self.V[self.zero_rows[schur_row]]),
            "schur_column_monomial": _monomial_label(
                self.cubic_monomials[
                    self.nonpivot_columns[schur_column]
                ]
            ),
        }


def build_schur_model(
    source_path: Path = DEFAULT_SOURCE,
) -> Program5RankSixSchurModel:
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
    for vector in adapted:
        if L * vector != sp.zeros(L.rows, 1):
            raise AssertionError("adapted tangent basis left ker(L)")
    pivot_rows, pivot_operation_columns = _independent_rows_and_columns(L)
    minor = L[pivot_rows, pivot_operation_columns]
    minor_inverse = minor.inv()

    return Program5RankSixSchurModel(
        source_path=source_path,
        source_sha256=exported["summary"]["source_sha256"],
        V=V,
        labels=labels,
        cubic_monomials=cubic_monomials,
        variation_matrices=variation_matrices,
        base_rows=base_rows,
        zero_rows=zero_rows,
        pivot_columns=pivot_columns,
        nonpivot_columns=nonpivot_columns,
        G0=G0,
        B0=B0,
        L=L,
        pivot_rows=pivot_rows,
        pivot_operation_columns=pivot_operation_columns,
        minor_inverse=minor_inverse,
        tangent_basis=adapted,
        row_basis=row_columns,
        eta0=eta0,
        eta1=eta1,
        theta_u=theta_u,
        theta_v=theta_v,
    )
