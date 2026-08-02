#!/usr/bin/env python3
"""Verify bounded elementary-source-shear Lane 5 certificates.

For each coefficient-one monomial shear in six coordinate directions and each
exponent 2 through 8, the script constructs rational common-fiber pairs for
the sheared map, finds a nonzero modular minor on B_{<=6}, and checks the exact
kernel vectors that identify the filtered intersection.

The result is a finite exact family, not a classification of arbitrary source
automorphisms.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from standard_filtration_certificate import (
    dot,
    evaluate_monomials,
    fraction_mod,
    monomials_degree_at_most,
    split_target,
)

HERE = Path(__file__).resolve().parent
EXPECTED = HERE / "elementary_shear_scan.json"
PRIME = 1_000_003
BOUND = 6
MONOMIALS = monomials_degree_at_most(BOUND)
INDEX = {monomial: index for index, monomial in enumerate(MONOMIALS)}


def transform_inverse(
    kind: str,
    exponent: int,
    point: tuple[Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction]:
    x, y, z = point
    if kind == "z+xN":
        return x, y, z - x**exponent
    if kind == "y+xN":
        return x, y - x**exponent, z
    if kind == "x+yN":
        return x - y**exponent, y, z
    if kind == "z+yN":
        return x, y, z - y**exponent
    if kind == "y+zN":
        return x, y - z**exponent, z
    if kind == "x+zN":
        return x - z**exponent, y, z
    raise ValueError(f"unknown shear kind: {kind}")


def add_row_echelon(row: list[int], basis: dict[int, list[int]]) -> bool:
    work = row[:]
    for pivot in sorted(basis):
        factor = work[pivot]
        if not factor:
            continue
        basis_row = basis[pivot]
        for column in range(pivot, len(work)):
            work[column] = (
                work[column] - factor * basis_row[column]
            ) % PRIME
    pivot = next((i for i, entry in enumerate(work) if entry), None)
    if pivot is None:
        return False
    inverse = pow(work[pivot], PRIME - 2, PRIME)
    for column in range(pivot, len(work)):
        work[column] = work[column] * inverse % PRIME
    basis[pivot] = work
    return True


def determinant_mod(matrix: list[list[int]]) -> int:
    work = [[entry % PRIME for entry in row] for row in matrix]
    size = len(work)
    determinant = 1
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            determinant = -determinant
        pivot = work[column][column] % PRIME
        determinant = determinant * pivot % PRIME
        inverse = pow(pivot, PRIME - 2, PRIME)
        for row in range(column + 1, size):
            if not work[row][column]:
                continue
            factor = work[row][column] * inverse % PRIME
            for offset in range(column, size):
                work[row][offset] = (
                    work[row][offset] - factor * work[column][offset]
                ) % PRIME
    return determinant % PRIME


def constant_vector() -> list[Fraction]:
    vector = [Fraction(0)] * len(MONOMIALS)
    vector[INDEX[(0, 0, 0)]] = 1
    return vector


def sheared_r_vector(kind: str, exponent: int) -> list[Fraction] | None:
    """Coefficient vector of sigma(R), when its total degree is at most six."""
    coefficients: dict[tuple[int, int, int], Fraction] = {
        (1, 0, 0): Fraction(2),
        (2, 1, 0): Fraction(-3),
        (3, 0, 1): Fraction(-1),
    }
    if kind == "z+xN":
        monomial, coefficient = (exponent + 3, 0, 0), Fraction(-1)
    elif kind == "y+xN":
        monomial, coefficient = (exponent + 2, 0, 0), Fraction(-3)
    elif kind == "z+yN":
        monomial, coefficient = (3, exponent, 0), Fraction(-1)
    elif kind == "y+zN":
        monomial, coefficient = (2, 0, exponent), Fraction(-3)
    else:
        return None
    coefficients[monomial] = coefficients.get(monomial, Fraction(0)) + coefficient
    if any(
        sum(monomial) > BOUND and coefficient
        for monomial, coefficient in coefficients.items()
    ):
        return None
    vector = [Fraction(0)] * len(MONOMIALS)
    for monomial, coefficient in coefficients.items():
        if coefficient:
            vector[INDEX[monomial]] = coefficient
    return vector


def candidate_points() -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for h in (Fraction(1), Fraction(2), Fraction(3)):
        for a in range(-12, 1):
            for b in range(-12, 2):
                for sign in (1, -1):
                    try:
                        _, points = split_target(
                            Fraction(a), Fraction(b), h, sign
                        )
                    except (ValueError, ZeroDivisionError):
                        continue
                    candidates.append(
                        {
                            "a": str(a),
                            "b": str(b),
                            "h": str(h),
                            "sign": sign,
                            "points": points,
                        }
                    )
    return candidates


def verify_case(
    expected: dict[str, object],
    candidates: list[dict[str, object]],
) -> dict[str, object]:
    kind = str(expected["kind"])
    exponent = int(expected["exponent"])
    target_rank = int(expected["rank"])
    basis: dict[int, list[int]] = {}
    exact_rows: list[list[Fraction]] = []

    for candidate in candidates:
        points = [
            transform_inverse(kind, exponent, point)
            for point in candidate["points"]  # type: ignore[index]
        ]
        first = evaluate_monomials(points[0], MONOMIALS, BOUND)
        for pair in (1, 2):
            second = evaluate_monomials(points[pair], MONOMIALS, BOUND)
            exact_row = [left - right for left, right in zip(first, second)]
            modular_row = [fraction_mod(entry, PRIME) for entry in exact_row]
            if not add_row_echelon(modular_row, basis):
                continue
            exact_rows.append(exact_row)
            if len(basis) == target_rank:
                break
        if len(basis) == target_rank:
            break

    if len(basis) != target_rank:
        raise AssertionError(f"{kind}, N={exponent}: target rank not reached")
    pivots = sorted(basis)
    nonpivots = [
        column for column in range(len(MONOMIALS)) if column not in set(pivots)
    ]
    if nonpivots != [int(value) for value in expected["nonpivot_columns"]]:
        raise AssertionError(f"{kind}, N={exponent}: pivot columns changed")

    modular_rows = [
        [fraction_mod(entry, PRIME) for entry in row] for row in exact_rows
    ]
    determinant = determinant_mod(
        [[row[column] for column in pivots] for row in modular_rows]
    )
    if determinant != int(expected["pivot_minor_determinant_mod_prime"]):
        raise AssertionError(f"{kind}, N={exponent}: determinant changed")

    vectors = {"1": constant_vector()}
    sheared_r = sheared_r_vector(kind, exponent)
    if sheared_r is not None:
        vectors["sigma(R)"] = sheared_r
    expected_basis = [str(value) for value in expected["intersection_basis"]]
    if list(vectors) != expected_basis:
        raise AssertionError(f"{kind}, N={exponent}: kernel basis changed")
    for name, vector in vectors.items():
        if any(dot(row, vector) != 0 for row in exact_rows):
            raise AssertionError(
                f"{kind}, N={exponent}: {name} is not in the exact kernel"
            )

    kernel_dimension = len(MONOMIALS) - target_rank
    if kernel_dimension != len(vectors):
        raise AssertionError(f"{kind}, N={exponent}: kernel dimension changed")

    return {
        "kind": kind,
        "exponent": exponent,
        "rank": target_rank,
        "kernel_dimension": kernel_dimension,
        "intersection_basis": expected_basis,
        "pivot_minor_determinant_mod_prime": determinant,
        "status": "pass",
    }


def main() -> int:
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    if int(expected["prime"]) != PRIME or int(expected["degree_bound"]) != BOUND:
        raise AssertionError("global certificate parameters changed")
    candidates = candidate_points()
    results = [verify_case(case, candidates) for case in expected["cases"]]
    summary = {
        "status": "pass",
        "case_count": len(results),
        "prime": PRIME,
        "degree_bound": BOUND,
        "rank_82_cases": sum(result["rank"] == 82 for result in results),
        "rank_83_cases": sum(result["rank"] == 83 for result in results),
        "conclusion": expected["conclusion"],
        "cases": results,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
