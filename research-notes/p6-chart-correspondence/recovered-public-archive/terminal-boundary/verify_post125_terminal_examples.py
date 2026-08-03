#!/usr/bin/env python3
"""Exact lattice-gap terminal checks for the first post-125 complete chains.

The script distinguishes the ambient fractional uniformizing cover from the
lattice-compatible quotient u=z^gap.  It verifies exact quotient ODEs and
explicit maps for the degree-125 F2 case and the first three post-125 cases.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
from fractions import Fraction
import json
from pathlib import Path

import sympy as sp

from terminal_primary_belyi import terminal_reduction, verify_explicit_f2_solution
from count_F2_terminal_dessins import weighted_hurwitz

u, z = sp.symbols("u z")


def _weighted_count(rec) -> Fraction:
    return weighted_hurwitz(rec.lattice_quotient.degree, rec.lattice_quotient.cycle_types)[1]


def _check_basic_polynomials(pbar: sp.Expr, qbar: sp.Expr) -> None:
    pp = sp.Poly(pbar, u, extension=True)
    qq = sp.Poly(qbar, u, extension=True)
    assert pp.eval(0) != 0 and qq.eval(0) != 0
    assert sp.gcd(pp, qq).degree() == 0
    assert sp.gcd(pp, pp.diff()).degree() == 0
    assert sp.gcd(qq, qq.diff()).degree() == 0


def _verify_quotient_and_lift(
    *, pbar: sp.Expr, qbar: sp.Expr, m: int, n: int, gap: int
) -> tuple[sp.Expr, sp.Expr]:
    N = n // gap
    qode = sp.cancel(
        N * pbar * qbar
        - m * u * pbar * sp.diff(qbar, u)
        + n * u * sp.diff(pbar, u) * qbar
    )
    assert qode == sp.Rational(1, gap)
    taubar = sp.cancel(u**N * pbar**n / qbar**m)
    assert sp.cancel(
        sp.diff(taubar, u)
        - sp.Rational(1, gap) * u ** (N - 1) * pbar ** (n - 1) / qbar ** (m + 1)
    ) == 0

    p = sp.expand(pbar.subs(u, z**gap))
    q = sp.expand(qbar.subs(u, z**gap))
    ode = sp.cancel(n * p * q - m * z * p * sp.diff(q, z) + n * z * sp.diff(p, z) * q)
    assert ode == 1
    tau = sp.cancel(z**n * p**n / q**m)
    assert sp.cancel(tau - taubar.subs(u, z**gap)) == 0
    assert sp.cancel(sp.diff(tau, z) - z ** (n - 1) * p ** (n - 1) / q ** (m + 1)) == 0
    _check_basic_polynomials(pbar, qbar)
    return p, q


def one_step_max126_map() -> dict[str, str]:
    """Unique quotient passport (3^3 1),(2^5),(8 1^2), degree 10."""
    P = u**3 + u**2 + sp.Rational(5, 12) * u + sp.Rational(1, 18)
    Q = (
        u**5
        + sp.Rational(3, 2) * u**4
        + u**3
        + sp.Rational(1, 3) * u**2
        + sp.Rational(5, 96) * u
        + sp.Rational(1, 576)
    )
    assert sp.simplify(u * P**3 - Q**2 + (36 * u**2 + 28 * u + 9) / sp.Integer(2985984)) == 0
    assert sp.discriminant(P, u) == -sp.Rational(1, 216)
    assert sp.discriminant(Q, u) == sp.Rational(1, 859963392)
    assert sp.discriminant(36 * u**2 + 28 * u + 9, u) == -512

    pbar, qbar = 18 * P, 192 * Q
    p, q = _verify_quotient_and_lift(pbar=pbar, qbar=qbar, m=2, n=3, gap=3)
    return {
        "pbar": str(sp.expand(pbar)),
        "qbar": str(sp.expand(qbar)),
        "p": str(p),
        "q": str(q),
        "quotient_identity": "u P(u)^3-Q(u)^2=-(36u^2+28u+9)/2985984",
    }


def two_step_max126_map() -> dict[str, str]:
    """Unique quotient passport (2^4 1),(3^3),(7 1^2), degree 9."""
    pbar = (
        1
        + sp.Rational(20, 3) * u
        + 24 * u**2
        + sp.Rational(288, 7) * u**3
        + sp.Rational(288, 7) * u**4
    )
    qbar = sp.Rational(1, 2) + 5 * u + 12 * u**2 + 18 * u**3
    p, q = _verify_quotient_and_lift(pbar=pbar, qbar=qbar, m=3, n=2, gap=2)

    P = u**4 + u**3 + sp.Rational(7, 12) * u**2 + sp.Rational(35, 216) * u + sp.Rational(7, 288)
    Q = u**3 + sp.Rational(2, 3) * u**2 + sp.Rational(5, 18) * u + sp.Rational(1, 36)
    assert sp.simplify(u * P**2 - Q**3 + (72 * u**2 + 39 * u + 16) / sp.Integer(746496)) == 0
    assert sp.discriminant(P, u) != 0
    assert sp.discriminant(Q, u) != 0
    assert sp.discriminant(72 * u**2 + 39 * u + 16, u) != 0
    return {
        "pbar": str(sp.expand(pbar)),
        "qbar": str(sp.expand(qbar)),
        "p": str(p),
        "q": str(q),
        "quotient_identity": "u P(u)^2-Q(u)^3=-(72u^2+39u+16)/746496",
    }


def F24_maps() -> dict[str, object]:
    """The two quotient passport (4^2 1),(3^3),(5 1^4) maps over Q(sqrt(6))."""
    records: list[dict[str, str]] = []
    sqrt6 = sp.sqrt(6)
    for sign in (-1, 1):
        eps = sp.Rational(17, 160) + sign * sp.Rational(11, 480) * sqrt6
        b2 = sp.Rational(1, 3) + sign * sqrt6 / 18
        d2 = sp.Rational(2, 5) + sign * sqrt6 / 40
        pbar = 1 + u + b2 * u**2
        qbar = sp.Rational(1, 4) + sp.Rational(5, 8) * u + d2 * u**2 + eps * u**3
        p, q = _verify_quotient_and_lift(pbar=pbar, qbar=qbar, m=3, n=4, gap=4)

        # The third fiber has one ramification point of index five and four
        # unramified points.  This is visible from the degree-four remainder.
        L = sp.cancel(sp.LC(sp.Poly(pbar, u, extension=sqrt6)) ** 4 / sp.LC(sp.Poly(qbar, u, extension=sqrt6)) ** 3)
        remainder = sp.cancel(u * pbar**4 - L * qbar**3)
        assert sp.Poly(remainder, u, extension=sqrt6).degree() == 4
        assert sp.gcd(
            sp.Poly(remainder, u, extension=sqrt6),
            sp.Poly(sp.diff(remainder, u), u, extension=sqrt6),
        ).degree() == 0
        records.append(
            {
                "sign": "+" if sign == 1 else "-",
                "pbar": str(sp.expand(pbar)),
                "qbar": str(sp.expand(qbar)),
                "p": str(p),
                "q": str(q),
                "coefficient_field": "Q(sqrt(6))",
            }
        )
    return {"maps": records, "Galois_relation": "the two maps are conjugate under sqrt(6) -> -sqrt(6)"}


def _serialize_reduction(rec) -> dict[str, object]:
    return {
        "corner": {
            "a": rec.a,
            "ell": rec.ell,
            "b": rec.b,
            "k": rec.k,
            "m": rec.m,
            "n": rec.n,
            "direction": [rec.rho, rec.sigma],
            "gap": rec.gap,
            "N": rec.N,
        },
        "uniformizing_degree": rec.uniformizing.degree,
        "uniformizing_passport": list(rec.uniformizing.display),
        "lattice_quotient_degree": rec.lattice_quotient.degree,
        "lattice_quotient_passport": list(rec.lattice_quotient.display),
        "quotient_polynomial_degrees": [rec.deg_p_bar, rec.deg_q_bar],
        "uniformizing_ode": rec.uniformizing_ode,
        "quotient_ode": rec.quotient_ode,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    definitions = {
        "F2_max125": dict(a=7, ell=5, b=2, k=1, m=3, n=5),
        "one_step_max126": dict(a=19, ell=7, b=5, k=2, m=2, n=3),
        "two_step_max126": dict(a=11, ell=6, b=3, k=1, m=3, n=2),
        "F24_max128": dict(a=19, ell=8, b=3, k=1, m=3, n=4),
        "one_step_max132": dict(a=19, ell=4, b=8, k=1, m=2, n=3),
    }
    reductions = {name: terminal_reduction(**data) for name, data in definitions.items()}

    expected_counts = {
        "F2_max125": Fraction(1),
        "one_step_max126": Fraction(1),
        "two_step_max126": Fraction(1),
        "F24_max128": Fraction(2),
        "one_step_max132": Fraction(2),
    }
    payload: dict[str, object] = {}
    for name, rec in reductions.items():
        count = _weighted_count(rec)
        assert count == expected_counts[name]
        # In all five cases the first branch partition has a unique fixed
        # sheet.  A deck transformation centralizing a transitive monodromy
        # group is semiregular, hence must be trivial if it fixes that sheet.
        assert rec.N == 1
        item = _serialize_reduction(rec)
        item.update(
            {
                "weighted_connected_Hurwitz_count": str(count),
                "connected_dessin_classes": int(count),
                "deck_group": "trivial (unique fixed sheet in the first branch partition)",
            }
        )
        payload[name] = item

    payload["F2_max125"]["explicit_map"] = verify_explicit_f2_solution()
    payload["one_step_max126"]["explicit_map"] = one_step_max126_map()
    payload["two_step_max126"]["explicit_map"] = two_step_max126_map()
    payload["F24_max128"]["explicit_maps"] = F24_maps()

    # Spot checks against the complete-chain directions.
    assert reductions["F2_max125"].rho == 25 and reductions["F2_max125"].sigma == -17
    assert reductions["one_step_max126"].rho == 21 and reductions["one_step_max126"].sigma == -11
    assert reductions["two_step_max126"].rho == 12 and reductions["two_step_max126"].sigma == -7
    assert reductions["F24_max128"].rho == 32 and reductions["F24_max128"].sigma == -25
    assert reductions["one_step_max132"].rho == 12 and reductions["one_step_max132"].sigma == -7

    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    print("all lattice-gap passports, Hurwitz counts, explicit quotient maps, and cyclic lifts verified")


if __name__ == "__main__":
    main()
