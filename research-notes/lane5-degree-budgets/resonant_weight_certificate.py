#!/usr/bin/env python3
"""Verify the resonant Lane 5 family z -> z + c*y^2 exactly over Q[c].

The source torus weights are wt(x)=-1, wt(y)=1, wt(z)=2, so this shear is
weight preserving.  The degree-at-most-six source space splits into 19 small
weight spaces.  For each weight, the certificate supplies one or two exact
rational collision minors.  Their gcd over Q[c] is 1, except in weight 1 where
it is c.  This proves that the only degree-six fiber-constant polynomials are

    span{1,Q,R}                  when c = 0,
    span{1, sigma_c(R)}          when c != 0.

The standard c=0 equality is separately pinned by
standard_filtration_certificate.py.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from standard_filtration_certificate import (
    monomials_degree_at_most,
    split_target,
)

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "resonant_weight_certificate.json"
BOUND = 6
MONOMIALS = monomials_degree_at_most(BOUND)


def candidate_points() -> list[tuple[tuple[Fraction, Fraction, Fraction], ...]]:
    candidates = []
    for h in (Fraction(1), Fraction(2), Fraction(3)):
        for a in range(-12, 1):
            for b in range(-12, 2):
                for sign in (1, -1):
                    try:
                        _, points = split_target(Fraction(a), Fraction(b), h, sign)
                    except (ValueError, ZeroDivisionError):
                        continue
                    candidates.append(points)
    return candidates


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [[Fraction(entry) for entry in row] for row in matrix]
    size = len(work)
    value = Fraction(1)
    sign = 1
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign = -sign
        pivot = work[column][column]
        value *= pivot
        for row in range(column + 1, size):
            if not work[row][column]:
                continue
            factor = work[row][column] / pivot
            for offset in range(column + 1, size):
                work[row][offset] -= factor * work[column][offset]
            work[row][column] = 0
    return sign * value


def evaluate_columns(
    point: tuple[Fraction, Fraction, Fraction],
    columns: list[int],
    parameter: int,
) -> list[Fraction]:
    x, y, z = point
    transformed_z = z - parameter * y**2
    return [
        x**i * y**j * transformed_z**k
        for i, j, k in (MONOMIALS[column] for column in columns)
    ]


def interpolate_consecutive(values: list[Fraction]) -> list[Fraction]:
    """Interpolate f(0),...,f(d) in the monomial basis over Q."""
    differences = [Fraction(value) for value in values]
    leading_differences = []
    while differences:
        leading_differences.append(differences[0])
        differences = [
            differences[index + 1] - differences[index]
            for index in range(len(differences) - 1)
        ]

    coefficients = [Fraction(0)] * len(values)
    falling_factorial = [Fraction(1)]
    factorial = 1
    for degree, difference in enumerate(leading_differences):
        if degree:
            updated = [Fraction(0)] * (len(falling_factorial) + 1)
            for index, coefficient in enumerate(falling_factorial):
                updated[index] -= (degree - 1) * coefficient
                updated[index + 1] += coefficient
            falling_factorial = updated
            factorial *= degree
        scale = difference / factorial
        for index, coefficient in enumerate(falling_factorial):
            coefficients[index] += scale * coefficient
    return trim(coefficients)


def trim(poly: list[Fraction]) -> list[Fraction]:
    result = [Fraction(value) for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def monic(poly: list[Fraction]) -> list[Fraction]:
    result = trim(poly)
    if result == [0]:
        return result
    return [coefficient / result[-1] for coefficient in result]


def divide(
    dividend: list[Fraction], divisor: list[Fraction]
) -> tuple[list[Fraction], list[Fraction]]:
    remainder = trim(dividend)
    divisor = trim(divisor)
    if divisor == [0]:
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(1, len(remainder) - len(divisor) + 1)
    while remainder != [0] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + shift] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def gcd(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = divide(left, right)
        left, right = right, remainder
    return monic(left)


def coefficient_hash(poly: list[Fraction]) -> str:
    payload = json.dumps(
        [str(value) for value in trim(poly)], separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def c_order(poly: list[Fraction]) -> int:
    return next(index for index, value in enumerate(poly) if value)


def expected_gcd(value: str) -> list[Fraction]:
    if value == "1":
        return [Fraction(1)]
    if value == "c":
        return [Fraction(0), Fraction(1)]
    raise ValueError(f"unsupported expected gcd: {value}")


def verify() -> dict[str, object]:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    if certificate["degree_bound"] != BOUND:
        raise AssertionError("degree bound changed")
    candidates = candidate_points()
    weights = []

    for entry in certificate["weights"]:
        weight = int(entry["weight"])
        columns = [int(value) for value in entry["columns"]]
        gcd_poly: list[Fraction] | None = None

        for minor in entry["minors"]:
            local_pivots = [int(value) for value in minor["pivot_local_columns"]]
            selected_columns = [columns[index] for index in local_pivots]
            degree_bound = sum(MONOMIALS[column][2] for column in selected_columns)
            determinant_values = []

            for parameter in range(degree_bound + 1):
                matrix = []
                for candidate_index, pair in minor["rows"]:
                    points = candidates[int(candidate_index)]
                    first = evaluate_columns(points[0], selected_columns, parameter)
                    second = evaluate_columns(
                        points[int(pair)], selected_columns, parameter
                    )
                    matrix.append(
                        [left - right for left, right in zip(first, second)]
                    )
                determinant_values.append(determinant(matrix))

            polynomial = interpolate_consecutive(determinant_values)
            if len(polynomial) - 1 != int(minor["degree"]):
                raise AssertionError(f"weight {weight}: determinant degree changed")
            if c_order(polynomial) != int(minor["c_order"]):
                raise AssertionError(f"weight {weight}: c-order changed")
            if coefficient_hash(polynomial) != minor["coefficient_sha256"]:
                raise AssertionError(f"weight {weight}: determinant changed")
            gcd_poly = (
                monic(polynomial)
                if gcd_poly is None
                else gcd(gcd_poly, polynomial)
            )

        expected = expected_gcd(entry["expected_minor_gcd"])
        if gcd_poly != expected:
            raise AssertionError(f"weight {weight}: minor gcd changed")

        weights.append(
            {
                "weight": weight,
                "dimension": len(columns),
                "target_rank": int(entry["target_rank"]),
                "minor_count": len(entry["minors"]),
                "minor_gcd": entry["expected_minor_gcd"],
            }
        )

    return {
        "status": "pass",
        "weight_count": len(weights),
        "minor_count": sum(item["minor_count"] for item in weights),
        "weights": weights,
        "conclusion": certificate["conclusion"],
    }


def main() -> int:
    print(json.dumps(verify(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
