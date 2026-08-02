#!/usr/bin/env python3
"""Verify the numerical and fiber-witness claims in the reduced-word theorem."""

from __future__ import annotations

import json
from fractions import Fraction

D = 6
WIDTH = 3 * D


def map_f(point: tuple[Fraction, Fraction, Fraction]):
    x, y, z = point
    a = 1 + x * y
    p = a**3 * z + y**2 * a * (4 + 3 * x * y)
    q = y + 3 * x * a**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    r = 2 * x - 3 * x**2 * y - x**3 * z
    return p, q, r


def derivatives(point: tuple[Fraction, Fraction, Fraction]):
    x, y, z = point
    qx = 3 * z + 12 * x * y * z + 9 * x**2 * y**2 * z + 12 * y**2 + 18 * x * y**3
    qy = 1 + 6 * x**2 * z + 6 * x**3 * y * z + 24 * x * y + 27 * x**2 * y**2
    rx = 2 - 6 * x * y - 3 * x**2 * z
    ry = -3 * x**2
    return qx, qy, rx, ry


def check_nested(N: int, M: int) -> dict[str, int]:
    if N < 18 or M < 3 * N + 13:
        raise AssertionError("nested-family hypotheses are not satisfied")
    d1 = N + 1
    d2 = 2 * M - 1
    if not (d1 > WIDTH and d2 > D * d1 + WIDTH):
        raise AssertionError("nested-family shift inequalities failed")
    minimum = None
    for a1 in range(D + 1):
        for a2 in range(D + 1):
            for b1 in range(D + 1):
                for b2 in range(D + 1):
                    if (a1, a2) == (b1, b2):
                        continue
                    value = abs((a1 - b1) * d1 + (a2 - b2) * d2)
                    minimum = value if minimum is None else min(minimum, value)
    if minimum is None or minimum <= WIDTH:
        raise AssertionError("nested-family support is not separated")
    return {"N": N, "M": M, "d1": d1, "d2": d2, "minimum_shift_gap": minimum}


def superincreasing_shifts(length: int) -> list[int]:
    shifts = [19]
    while len(shifts) < length:
        shifts.append(12 * sum(shifts) + 19)
    return shifts


def check_superincreasing(length: int) -> dict[str, object]:
    shifts = superincreasing_shifts(length)
    for index, shift in enumerate(shifts):
        if index == 0:
            if shift <= WIDTH:
                raise AssertionError("first shift is too small")
        elif shift <= 2 * D * sum(shifts[:index]) + WIDTH:
            raise AssertionError("superincreasing recurrence failed")
    return {
        "length": length,
        "shifts": shifts,
        "x_exponents_for_z_shear": [shift - 2 for shift in shifts],
    }


def main() -> int:
    u = (Fraction(1), Fraction(-4, 3), Fraction(3))
    v = (Fraction(2), Fraction(1, 6), Fraction(-1, 8))
    if map_f(u) != map_f(v):
        raise AssertionError("common-fiber witness changed")
    qxu, qyu, rxu, ryu = derivatives(u)
    qxv, qyv, rxv, ryv = derivatives(v)

    N, M = 18, 67
    values = {
        "y^N*dQdx": (u[1] ** N * qxu, v[1] ** N * qxv),
        "y^N*dRdx": (u[1] ** N * rxu, v[1] ** N * rxv),
        "z^M*dQdy": (u[2] ** M * qyu, v[2] ** M * qyv),
        "z^M*dRdy": (u[2] ** M * ryu, v[2] ** M * ryv),
    }
    if any(left == right for left, right in values.values()):
        raise AssertionError("a derivative witness unexpectedly became fiber-constant")

    result = {
        "status": "pass",
        "degree_bound": D,
        "weight_width": WIDTH,
        "nested_example": check_nested(N, M),
        "arbitrary_length_example": check_superincreasing(4),
        "fiber_witness_target": [str(value) for value in map_f(u)],
        "derivative_witnesses_distinct": list(values),
        "conclusion": (
            "Reduced words with separated Taylor shifts have constant degree-six "
            "intersection; this includes arbitrary-length commuting words and "
            "an explicit noncommuting nested triangular family."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
