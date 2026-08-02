#!/usr/bin/env python3
"""Check the arithmetic and exact witness for the lacunary composition theorem."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction

WIDTH = 18
ORDER = 6
WEIGHTS = {"x": -1, "y": 1, "z": 2}
DIRECTIONS = (
    ("z+xN", "z", "x"),
    ("y+xN", "y", "x"),
    ("x+yN", "x", "y"),
    ("z+yN", "z", "y"),
    ("y+zN", "y", "z"),
    ("x+zN", "x", "z"),
)
EXAMPLES = {
    "z+xN": [17, 131],
    "y+xN": [18, 132],
    "x+yN": [18, 132],
    "z+yN": [21, 135],
    "y+zN": [10, 67],
    "x+zN": [9, 66],
}


def multiindices(length: int, total: int = ORDER):
    for values in itertools.product(range(total + 1), repeat=length):
        if sum(values) <= total:
            yield values


def six_step_separated(shifts: list[int]) -> bool:
    seen: list[int] = []
    for alpha in multiindices(len(shifts)):
        value = sum(a * e for a, e in zip(alpha, shifts))
        if any(abs(value - previous) <= WIDTH for previous in seen):
            return False
        seen.append(value)
    return True


def map_f(point: tuple[Fraction, Fraction, Fraction]):
    x, y, z = point
    a = 1 + x*y
    return (
        a**3*z + y**2*a*(4+3*x*y),
        y + 3*x*a**2*z + 3*x*y**2*(4+3*x*y),
        2*x - 3*x**2*y - x**3*z,
    )


def derivatives(point: tuple[Fraction, Fraction, Fraction]):
    x, y, z = point
    return {
        "Q_x": 3*(3*x**2*y**2*z + 6*x*y**3 + 4*x*y*z + 4*y**2 + z),
        "Q_y": 6*x**3*y*z + 27*x**2*y**2 + 6*x**2*z + 24*x*y + 1,
        "Q_z": 3*x*(x*y+1)**2,
        "R_x": -3*x**2*z - 6*x*y + 2,
        "R_y": -3*x**2,
        "R_z": -x**3,
    }


def main() -> int:
    u = (Fraction(-12), Fraction(1, 11), Fraction(-8, 11))
    v = (Fraction(-10), Fraction(1, 11), Fraction(-14, 11))
    w = (Fraction(22), Fraction(-1, 22), Fraction(65, 484))
    target = (Fraction(0), Fraction(1, 11), Fraction(-1320))
    if not (map_f(u) == map_f(v) == map_f(w) == target):
        raise AssertionError("common-fiber witness changed")

    derivative_table = {name: derivatives(point) for name, point in (("u",u),("v",v),("w",w))}
    examples = []
    for name, changed, base in DIRECTIONS:
        exponents = EXAMPLES[name]
        shifts = [N*WEIGHTS[base]-WEIGHTS[changed] for N in exponents]
        if not six_step_separated(shifts):
            raise AssertionError(f"{name}: example is not separated")
        if not (
            abs(shifts[0]) > WIDTH
            and abs(shifts[1]) > WIDTH + ORDER*abs(shifts[0])
        ):
            raise AssertionError(f"{name}: recursive bound changed")
        examples.append({"direction":name,"exponents":exponents,"shifts":shifts})

    result = {
        "status": "pass",
        "degree_bound": ORDER,
        "weight_interval": [-6, 12],
        "weight_width": WIDTH,
        "common_fiber_target": [str(value) for value in target],
        "derivatives": {
            point: {key: str(value) for key, value in table.items()}
            for point, table in derivative_table.items()
        },
        "two_term_examples": examples,
        "conclusion": (
            "The exact common-fiber witness and one superlacunary two-term "
            "example in every coordinate direction satisfy the hypotheses "
            "of the weight-separated composition theorem."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
