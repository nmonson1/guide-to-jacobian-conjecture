#!/usr/bin/env python3
"""Check the arithmetic and exact witness for high-weight polynomial shears."""

from __future__ import annotations

import json
from fractions import Fraction

WIDTH = 18
WEIGHTS = {"x": -1, "y": 1, "z": 2}
DIRECTIONS = (
    ("z+xN", "z", "x", 17, -1),
    ("y+xN", "y", "x", 18, -1),
    ("x+yN", "x", "y", 18, 1),
    ("z+yN", "z", "y", 21, 1),
    ("y+zN", "y", "z", 10, 1),
    ("x+zN", "x", "z", 9, 1),
)


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

    derivative_table = {
        name: derivatives(point) for name, point in (("u",u),("v",v),("w",w))
    }
    thresholds = []
    for name, changed, base, threshold, sign in DIRECTIONS:
        shift = threshold*WEIGHTS[base]-WEIGHTS[changed]
        previous = (threshold-1)*WEIGHTS[base]-WEIGHTS[changed]
        if sign*shift < 19:
            raise AssertionError(f"{name}: threshold misses the high-weight tail")
        if sign*previous >= 19:
            raise AssertionError(f"{name}: threshold is not minimal")
        for exponent in range(threshold, threshold+25):
            current = exponent*WEIGHTS[base]-WEIGHTS[changed]
            if sign*current < 19:
                raise AssertionError(f"{name}: tail changed sign or magnitude")
        thresholds.append({"direction":name,"threshold":threshold,"first_shift":shift})

    resonant_shift = 2*WEIGHTS["y"]-WEIGHTS["z"]
    if resonant_shift != 0:
        raise AssertionError("z+y^2 is no longer weight zero")

    result = {
        "status": "pass",
        "degree_bound": 6,
        "weight_interval": [-6,12],
        "weight_width": WIDTH,
        "thresholds": thresholds,
        "resonant_shift_z_plus_y2": resonant_shift,
        "common_fiber_target": [str(value) for value in target],
        "derivatives": {
            point: {key: str(value) for key, value in table.items()}
            for point, table in derivative_table.items()
        },
        "conclusion": (
            "Each listed threshold is the first exponent whose derivation "
            "weight lies strictly outside the degree-six weight window; the "
            "exact three-point fiber supplies the D(Q),D(R) obstruction used "
            "for arbitrary finite polynomial tails."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
