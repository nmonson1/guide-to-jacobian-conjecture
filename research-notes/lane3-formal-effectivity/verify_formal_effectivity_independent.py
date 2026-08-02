#!/usr/bin/env python3
"""Independent finite-support checker for the effectivity staircase.

This checker deliberately uses no CAS.  Polynomials in (s,c) are sparse
Python dictionaries with rational coefficients.  It verifies the exact
residual and sharp ramification law for a grid of Artin quotients.
"""
from __future__ import annotations

from fractions import Fraction
from math import ceil
from pathlib import Path
import json

Monomial = tuple[int, int]
Poly = dict[Monomial, Fraction]


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for poly in polys:
        for mon, coeff in poly.items():
            out[mon] = out.get(mon, Fraction(0)) + coeff
            if out[mon] == 0:
                del out[mon]
    return out


def scale(poly: Poly, scalar: Fraction) -> Poly:
    return {m: scalar * a for m, a in poly.items() if scalar * a}


def mul(left: Poly, right: Poly, modulus: int | None = None) -> Poly:
    out: Poly = {}
    for (si, ci), ai in left.items():
        for (sj, cj), aj in right.items():
            se = si + sj
            if modulus is not None and se >= modulus:
                continue
            mon = (se, ci + cj)
            out[mon] = out.get(mon, Fraction(0)) + ai * aj
            if out[mon] == 0:
                del out[mon]
    return out


def monomial(s_exp: int, c_exp: int, coeff: Fraction = Fraction(1)) -> Poly:
    return {} if coeff == 0 else {(s_exp, c_exp): coeff}


def c_degree(poly: Poly) -> int:
    return max((c for _, c in poly), default=-1)


def phi_for(M: int, e: int, D: int) -> Poly:
    # delta is normalized to 1; the factor 1/3 is retained exactly.
    out: Poly = {}
    for j in range(D):
        out = add(
            out,
            monomial(e * (j + 2), j + 1, Fraction((-1) ** j, 3)),
        )
    return {m: a for m, a in out.items() if m[0] < M}


def residual(M: int, e: int, D: int) -> Poly:
    # delta*alpha^2*c^2 - 3*c*(1+alpha*c)*phi_D
    difference = {} if 2 * e >= M else monomial(2 * e, 2)
    A = add(monomial(0, 1), monomial(e, 2))
    correction = scale(mul(A, phi_for(M, e, D), modulus=M), Fraction(3))
    return add(difference, scale(correction, Fraction(-1)))


def main() -> None:
    samples: list[dict[str, int | bool]] = []
    for M in range(2, 31):
        for e in range(1, min(M, 8)):
            D = max(0, ceil(M / e) - 2)
            r = residual(M, e, D)
            if r:
                raise AssertionError(f"existence failed M={M}, e={e}: {r}")
            deg = c_degree(phi_for(M, e, D))
            expected = -1 if D == 0 else D
            if deg != expected:
                raise AssertionError((M, e, deg, expected))
            sharp = True
            if D > 0:
                previous = residual(M, e, D - 1)
                sharp = bool(previous)
                if not sharp:
                    raise AssertionError(f"sharpness failed M={M}, e={e}")
            samples.append(
                {
                    "M": M,
                    "e": e,
                    "D": D,
                    "sharp": sharp,
                }
            )

    # Compatibility in the unramified tower.
    for M in range(1, 30):
        current_D = max(0, M - 2)
        next_D = max(0, M - 1)
        current = {m: a for m, a in phi_for(M, 1, current_D).items() if m[0] < M}
        reduced_next = {
            m: a for m, a in phi_for(M + 1, 1, next_D).items() if m[0] < M
        }
        if current != reduced_next:
            raise AssertionError(f"compatibility failed at M={M}")

    report = {
        "status": "INDEPENDENT EFFECTIVITY STAIRCASE CHECKS PASSED",
        "engine": "pure Python sparse dictionaries with Fraction coefficients",
        "sample_count": len(samples),
        "max_modulus": 30,
        "max_ramification_order": 7,
        "samples": samples,
    }
    path = Path(__file__).with_name("formal_effectivity_independent_report.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report["status"])


if __name__ == "__main__":
    main()
