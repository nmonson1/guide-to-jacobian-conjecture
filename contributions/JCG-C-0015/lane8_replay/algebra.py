"""Small exact polynomial-linear-algebra layer for the Lane 8 replay."""
from __future__ import annotations

from fractions import Fraction
import os
from pathlib import Path
import sys
from typing import Any

PACKAGE_DIR = Path(__file__).resolve().parent
FIELD_DIR = Path(
    os.environ.get(
        "LANE8_FIELD_DIR",
        PACKAGE_DIR.parent / "fixtures",
    )
).resolve()
sys.path.insert(0, str(FIELD_DIR))
from quintic_field_fast import K, K5  # noqa: E402

ZERO = K.zero
ONE = K.one
U = K.unit
KElement = K5
Monomial = tuple[int, ...]
ParamPoly = dict[Monomial, KElement]
NVAR = 0
ZEXP: Monomial = ()


def set_parameter_count(count: int) -> None:
    global NVAR, ZEXP
    NVAR = count
    ZEXP = (0,) * count


def k_vector(value: KElement) -> list[str]:
    return [str(q) for q in value.coeffs]


def k_expr(value: KElement, symbol: str = "u") -> str:
    pieces: list[str] = []
    for degree, coefficient in enumerate(value.coeffs):
        if coefficient == 0:
            continue
        c = str(coefficient)
        if degree == 0:
            pieces.append(f"({c})")
        elif degree == 1:
            pieces.append(f"({c})*{symbol}")
        else:
            pieces.append(f"({c})*{symbol}^{degree}")
    return " + ".join(pieces) if pieces else "0"


def clean(poly: ParamPoly) -> ParamPoly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient != ZERO}


def constant(coefficient: KElement) -> ParamPoly:
    return {} if coefficient == ZERO else {ZEXP: coefficient}


def variable(index: int) -> ParamPoly:
    exponent = [0] * NVAR
    exponent[index] = 1
    return {tuple(exponent): ONE}


def add(left: ParamPoly, right: ParamPoly) -> ParamPoly:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, ZERO) + coefficient
    return clean(out)


def negate(poly: ParamPoly) -> ParamPoly:
    return {monomial: -coefficient for monomial, coefficient in poly.items()}


def scale(coefficient: KElement | int | Fraction, poly: ParamPoly) -> ParamPoly:
    coefficient = K.convert(coefficient)
    if coefficient == ZERO:
        return {}
    return clean({monomial: coefficient * value for monomial, value in poly.items()})


def multiply(left: ParamPoly, right: ParamPoly) -> ParamPoly:
    out: ParamPoly = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            out[monomial] = out.get(monomial, ZERO) + left_coefficient * right_coefficient
    return clean(out)


def weighted_degree(poly: ParamPoly, weights: tuple[int, ...]) -> int:
    values = {sum(exponent * weight for exponent, weight in zip(monomial, weights)) for monomial in poly}
    if len(values) != 1:
        raise AssertionError(values)
    return next(iter(values))


def normalized(poly: ParamPoly) -> tuple[KElement, ParamPoly]:
    first = min(poly)
    coefficient = ONE / poly[first]
    return coefficient, {monomial: coefficient * value for monomial, value in poly.items()}


def polynomial_json(poly: ParamPoly) -> list[dict[str, Any]]:
    return [
        {"exp": list(monomial), "coeff_basis": k_vector(coefficient), "coeff_expr": k_expr(coefficient)}
        for monomial, coefficient in sorted(poly.items())
    ]


def rref_transform_details(matrix: list[list[KElement]]) -> tuple[list[list[KElement]], list[list[KElement]], list[int], list[KElement]]:
    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    augmented = [
        list(matrix[row]) + [ONE if row == identity_column else ZERO for identity_column in range(row_count)]
        for row in range(row_count)
    ]
    pivot_row = 0
    pivots: list[int] = []
    pivot_units: list[KElement] = []
    for column in range(column_count):
        source = next((row for row in range(pivot_row, row_count) if augmented[row][column] != ZERO), None)
        if source is None:
            continue
        augmented[pivot_row], augmented[source] = augmented[source], augmented[pivot_row]
        pivot_units.append(augmented[pivot_row][column])
        inverse = ONE / augmented[pivot_row][column]
        augmented[pivot_row] = [inverse * value for value in augmented[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or augmented[row][column] == ZERO:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                augmented[row][index] - factor * augmented[pivot_row][index]
                for index in range(column_count + row_count)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return (
        [row[:column_count] for row in augmented],
        [row[column_count:] for row in augmented],
        pivots,
        pivot_units,
    )


def rref_transform(matrix: list[list[KElement]]) -> tuple[list[list[KElement]], list[list[KElement]], list[int]]:
    reduced, transform, pivots, _ = rref_transform_details(matrix)
    return reduced, transform, pivots


def transform_polynomials(transform: list[list[KElement]], vector: list[ParamPoly]) -> list[ParamPoly]:
    out: list[ParamPoly] = []
    for row in transform:
        value: ParamPoly = {}
        for coefficient, poly in zip(row, vector):
            value = add(value, scale(coefficient, poly))
        out.append(value)
    return out


def determinant(matrix: list[list[KElement]]) -> KElement:
    work = [list(row) for row in matrix]
    size = len(work)
    value = ONE
    sign = 1
    for column in range(size):
        source = next(row for row in range(column, size) if work[row][column] != ZERO)
        if source != column:
            work[column], work[source] = work[source], work[column]
            sign = -sign
        pivot = work[column][column]
        value *= pivot
        inverse = ONE / pivot
        for row in range(column + 1, size):
            if work[row][column] == ZERO:
                continue
            factor = work[row][column] * inverse
            for index in range(column, size):
                work[row][index] -= factor * work[column][index]
    return -value if sign < 0 else value
