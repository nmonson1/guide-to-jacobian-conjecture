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
    qz = 3 * x * (1 + x * y) ** 2
    rx = 2 - 6 * x * y - 3 * x**2 * z
    ry = -3 * x**2
    rz = -x**3
    return qx, qy, qz, rx, ry, rz


def check_nested(N: int, M: int) -> dict[str, int]:
    if M < 21 or N < 6 * M + 6:
        raise AssertionError("mixed-sign nested-family hypotheses are not satisfied")
    d1 = -N - 1
    d2 = M - 2
    if not (d2 > WIDTH and abs(d1) > D * d2 + WIDTH):
        raise AssertionError("mixed-sign nested-family shift inequalities failed")
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
    signed = [shift if index % 2 == 0 else -shift for index, shift in enumerate(shifts)]
    terms = []
    for shift in signed:
        if shift > 0:
            terms.append({"monomial": f"z^{(shift + 1) // 2}", "shift": shift})
        else:
            terms.append({"monomial": f"x^{-shift - 1}", "shift": shift})
    return {
        "length": length,
        "absolute_shifts": shifts,
        "signed_shifts": signed,
        "terms_for_y_shear": terms,
    }


def main() -> int:
    u = (Fraction(1), Fraction(-4, 3), Fraction(3))
    v = (Fraction(2), Fraction(1, 6), Fraction(-1, 8))
    if map_f(u) != map_f(v):
        raise AssertionError("common-fiber witness changed")
    qxu, qyu, qzu, rxu, ryu, rzu = derivatives(u)
    qxv, qyv, qzv, rxv, ryv, rzv = derivatives(v)

    M, N = 21, 132
    values = {
        "x^N*dQdy": (u[0] ** N * qyu, v[0] ** N * qyv),
        "x^N*dRdy": (u[0] ** N * ryu, v[0] ** N * ryv),
        "y^M*dQdz": (u[1] ** M * qzu, v[1] ** M * qzv),
        "y^M*dRdz": (u[1] ** M * rzu, v[1] ** M * rzv),
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
            "intersection; this includes arbitrary-length mixed-sign commuting "
            "words and an explicit mixed-sign noncommuting triangular family."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
