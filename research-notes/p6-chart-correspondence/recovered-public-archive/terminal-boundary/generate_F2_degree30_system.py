#!/usr/bin/env python3
"""Generate the ambient F2 uniformizing-cover coefficient scheme.

Normalize p(0)=1 and q(0)=1/5.  The ODE

    5 p q - 3 z p q' + 5 z p' q = 1

recursively determines q from p.  Polynomial termination at deg(q)=10 is
exactly b_11=...=b_15=0.  The output records five primitive integer
polynomials in a1,...,a5, weighted homogeneous of weights 11,...,15 for
wt(ai)=i.  A polynomial complete-chain face has lattice gap five, hence lies
on the sublocus a1=a2=a3=a4=0.  This sublocus is one nonzero scaling orbit;
a5=-1 is the displayed representative.
"""
from __future__ import annotations

import argparse
from functools import reduce
from math import gcd
import json
from pathlib import Path

import sympy as sp

z = sp.symbols("z")
a = sp.symbols("a1:6")
vars_ = a


def primitive_integer_poly(expr: sp.Expr) -> sp.Poly:
    poly = sp.Poly(expr, *vars_, domain=sp.QQ)
    den, cleared = poly.clear_denoms()
    coeffs = [int(c) for c in cleared.coeffs()]
    content = reduce(gcd, (abs(c) for c in coeffs if c), 0) or 1
    cleared = sp.Poly(cleared.as_expr() / content, *vars_, domain=sp.ZZ)
    if cleared.LC() < 0:
        cleared = -cleared
    return cleared


def build() -> tuple[list[sp.Expr], list[sp.Poly]]:
    A = [sp.Integer(1), *a]
    b: list[sp.Expr] = []
    for k in range(16):
        rhs = sp.Integer(1) if k == 0 else sp.Integer(0)
        previous = sum(
            (5 - 3 * k + 8 * i) * A[i] * b[k - i]
            for i in range(1, min(5, k) + 1)
        )
        b_k = sp.cancel((rhs - previous) / sp.Integer(5 - 3 * k))
        b.append(b_k)

    equations = [primitive_integer_poly(sp.together(b[k]).as_numer_denom()[0]) for k in range(11, 16)]
    return b, equations


def weighted_degree(monom: tuple[int, ...]) -> int:
    return sum((i + 1) * exponent for i, exponent in enumerate(monom))


def serialize_poly(poly: sp.Poly) -> dict:
    terms = []
    for monom, coeff in poly.terms():
        terms.append({"exp": list(monom), "coeff": int(coeff)})
    weights = sorted({weighted_degree(m) for m, _ in poly.terms()})
    assert len(weights) == 1
    return {
        "weighted_degree": weights[0],
        "total_degree": poly.total_degree(),
        "term_count": len(terms),
        "terms": terms,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=Path("F2_degree30_coefficient_system.json"))
    args = parser.parse_args()

    b, equations = build()
    assert sp.cancel(b[0] - sp.Rational(1, 5)) == 0

    # Lattice-compatible C5-pullback locus: a1=...=a4=0.
    c5 = {a[0]: 0, a[1]: 0, a[2]: 0, a[3]: 0, a[4]: -1}
    assert all(poly.as_expr().subs({a[0]: 0, a[1]: 0, a[2]: 0, a[3]: 0}) == 0 for poly in equations)
    assert all(poly.as_expr().subs(c5) == 0 for poly in equations)
    q = sp.expand(sum(b[k].subs(c5) * z**k for k in range(11)))
    q_expected = sp.Rational(1, 5) - sp.Rational(3, 5) * z**5 + sp.Rational(9, 25) * z**10
    assert sp.expand(q - q_expected) == 0

    payload = {
        "normalization": {"p0": "1", "q0": "1/5"},
        "variables": [str(v) for v in vars_],
        "variable_weights": [1, 2, 3, 4, 5],
        "recurrence": "b_k = -(sum_{i=1}^{min(5,k)} (5-3k+8i) a_i b_{k-i})/(5-3k), k>0",
        "termination_conditions": [f"b_{k}=0" for k in range(11, 16)],
        "equations": [serialize_poly(p) for p in equations],
        "interpretation": "ambient uniformizing scheme; polynomial lattice support imposes a1=a2=a3=a4=0",
        "lattice_compatible_scaling_orbit": {
            "conditions": ["a1=0", "a2=0", "a3=0", "a4=0", "a5!=0"],
            "representative_a5": "-1",
        },
        "explicit_C5_solution": {
            "p": "1-z^5",
            "q": "1/5-(3/5)z^5+(9/25)z^10",
        },
    }
    args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print("wrote", args.json)
    for k, poly in zip(range(11, 16), equations):
        print(
            f"b_{k}: weighted degree {weighted_degree(poly.monoms()[0])}, "
            f"total degree {poly.total_degree()}, terms {len(poly.terms())}"
        )
    print("ambient equations and the lattice-compatible C5 scaling orbit verified")


if __name__ == "__main__":
    main()
