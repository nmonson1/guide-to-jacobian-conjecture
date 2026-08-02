#!/usr/bin/env python3
"""Verify the all-exponent elementary-monomial-source-shear theorem.

The finite part replays exact rational common-fiber certificates for every
exponent not covered by the torus-weight separation lemma.  The infinite tail
is certified structurally from the source torus grading and one explicit
three-point fiber.  The resonant coefficient family z -> z + c*y^2 is delegated
to resonant_weight_certificate.py.

This verifies a theorem for single elementary shears.  It does not cover
arbitrary compositions of shears or wild source automorphisms.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from elementary_shear_scan import BOUND, PRIME, candidate_points, verify_case
from resonant_weight_certificate import verify as verify_resonant

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "all_elementary_monomial_shears.json"

SOURCE_WEIGHTS = {"x": -1, "y": 1, "z": 2}
WEIGHT_INTERVAL = (-6, 12)
HIGH_THRESHOLDS = {
    "z+xN": 17,
    "y+xN": 18,
    "x+yN": 18,
    "z+yN": 21,
    "y+zN": 10,
    "x+zN": 9,
}


def map_f(point: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    x, y, z = point
    a = 1 + x * y
    p = a**3 * z + y**2 * a * (4 + 3 * x * y)
    q = y + 3 * x * a**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    r = 2 * x - 3 * x**2 * y - x**3 * z
    return p, q, r


def derivatives(point: tuple[Fraction, Fraction, Fraction]) -> dict[str, Fraction]:
    x, y, z = point
    return {
        "Q_x": 3 * (3*x**2*y**2*z + 6*x*y**3 + 4*x*y*z + 4*y**2 + z),
        "Q_y": 6*x**3*y*z + 27*x**2*y**2 + 6*x**2*z + 24*x*y + 1,
        "Q_z": 3*x*(x*y + 1)**2,
        "R_x": -3*x**2*z - 6*x*y + 2,
        "R_y": -3*x**2,
        "R_z": -x**3,
    }


def verify_weight_tail() -> dict[str, object]:
    low, high = WEIGHT_INTERVAL
    if high - low != 18:
        raise AssertionError("ordinary degree-six torus-weight width changed")

    derivation_weights = {
        "z+xN": lambda n: -n - 2,
        "y+xN": lambda n: -n - 1,
        "x+yN": lambda n: n + 1,
        "z+yN": lambda n: n - 2,
        "y+zN": lambda n: 2*n - 1,
        "x+zN": lambda n: 2*n + 1,
    }
    for kind, threshold in HIGH_THRESHOLDS.items():
        if abs(derivation_weights[kind](threshold)) <= 18:
            raise AssertionError(f"{kind}: threshold does not enter the separated range")
        if threshold > 2 and abs(derivation_weights[kind](threshold - 1)) > 18:
            raise AssertionError(f"{kind}: threshold is not minimal")

    u = (Fraction(-12), Fraction(1, 11), Fraction(-8, 11))
    v = (Fraction(-10), Fraction(1, 11), Fraction(-14, 11))
    w = (Fraction(22), Fraction(-1, 22), Fraction(65, 484))
    target = (Fraction(0), Fraction(1, 11), Fraction(-1320))
    if not (map_f(u) == map_f(v) == map_f(w) == target):
        raise AssertionError("high-weight witness points are not one fiber")

    du, dv, dw = derivatives(u), derivatives(v), derivatives(w)
    expected = {
        "u": {
            "Q_x": Fraction(-684, 1331), "Q_y": Fraction(7753, 121),
            "Q_z": Fraction(-36, 121), "R_x": Fraction(3550, 11),
            "R_y": Fraction(-432), "R_z": Fraction(1728),
        },
        "v": {
            "Q_x": Fraction(750, 1331), "Q_y": Fraction(-8219, 121),
            "Q_z": Fraction(-30, 121), "R_x": Fraction(4282, 11),
            "R_y": Fraction(-300), "R_z": Fraction(1000),
        },
        "w": {
            "Q_x": Fraction(-3, 242), "Q_y": Fraction(4),
            "Q_z": Fraction(0), "R_x": Fraction(-187),
            "R_y": Fraction(-1452), "R_z": Fraction(-10648),
        },
    }
    if du != expected["u"] or dv != expected["v"] or dw != expected["w"]:
        raise AssertionError("derivative witness table changed")

    if du["Q_z"] == 0 or dw["Q_z"] != 0:
        raise AssertionError("z-derivative zero witness changed")
    if abs(u[0]) == abs(v[0]):
        raise AssertionError("x-power witness lost strict magnitude")
    if not (du["Q_y"] > 0 > dv["Q_y"]):
        raise AssertionError("y+x^N Q witness lost opposite signs")
    if not (du["Q_x"] < 0 < dv["Q_x"]):
        raise AssertionError("x+y^N Q witness lost opposite signs")
    if not (u[1] == v[1] != 0):
        raise AssertionError("same-y witness changed")
    if du["Q_z"] == dv["Q_z"] or du["R_z"] == dv["R_z"]:
        raise AssertionError("same-y z-derivative witness changed")
    if not (u[2] < 0 and v[2] < 0 and du["Q_y"] > 0 > dv["Q_y"]):
        raise AssertionError("y+z^N Q sign witness changed")
    if not (
        Fraction(36, 25) * Fraction(4, 7) < 1
        and Fraction(3550, 4282) * Fraction(4, 7) < 1
    ):
        raise AssertionError("z-power strict-ratio witnesses changed")

    return {
        "status": "pass",
        "weight_interval": list(WEIGHT_INTERVAL),
        "weight_width": high - low,
        "high_thresholds": HIGH_THRESHOLDS,
        "common_fiber_target": [str(value) for value in target],
        "conclusion": (
            "For every listed direction, every nonzero shear coefficient, "
            "and every exponent at or above its threshold, the degree-six "
            "intersection is k."
        ),
    }


def main() -> int:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    if certificate["prime"] != PRIME or certificate["degree_bound"] != BOUND:
        raise AssertionError("finite certificate parameters changed")
    candidates = candidate_points()
    finite_results = [
        verify_case(case, candidates) for case in certificate["finite_cases"]
    ]
    tail = verify_weight_tail()
    resonant = verify_resonant()
    result = {
        "status": "pass",
        "finite_case_count": len(finite_results),
        "finite_rank_82_cases": sum(item["rank"] == 82 for item in finite_results),
        "finite_rank_83_cases": sum(item["rank"] == 83 for item in finite_results),
        "tail": tail,
        "resonant": resonant,
        "conclusion": certificate["conclusion"],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
