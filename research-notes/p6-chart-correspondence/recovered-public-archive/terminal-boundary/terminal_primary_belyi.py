#!/usr/bin/env python3
"""Exact terminal-primary Belyi formulas for type-I.b complete-chain corners.

There are two distinct covers.

1. On the fractional uniformizing coordinate z=x^{-sigma/rho}y, the final
   face equation is

       n*p*q - m*z*p*q' + n*z*p'*q = 1,

   with deg(p)=m*b-1 and deg(q)=n*b.  It defines an ambient Belyi map

       tau(z)=z**n*p(z)**n/q(z)**m

   of degree m*n*b.

2. Polynomial lattice support forces p(z)=pbar(z**g), q(z)=qbar(z**g), where

       g=gap(rho,ell)=rho/gcd(rho,ell).

   Put N=n/g and u=z**g.  The lattice-compatible quotient satisfies

       N*pbar*qbar - m*u*pbar*qbar' + n*u*pbar'*qbar = 1/g

   and defines

       taubar(u)=u**N*pbar(u)**n/qbar(u)**m

   of degree m*n*b/g.  This quotient, not the ambient cyclic pullback, is the
   finite Hurwitz problem attached to the polynomial complete-chain corner.

The script checks the final-corner arithmetic, divisibility, passports,
Riemann--Hurwitz identities, and the explicit F2 quotient/lift.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from fractions import Fraction
from math import gcd
import json
from pathlib import Path
from typing import Iterable

import sympy as sp

z, u = sp.symbols("z u")


def _partition_text(parts: Iterable[int]) -> str:
    counts: dict[int, int] = {}
    for part in sorted(parts, reverse=True):
        counts[part] = counts.get(part, 0) + 1
    pieces: list[str] = []
    for part in sorted(counts, reverse=True):
        mult = counts[part]
        pieces.append(str(part) if mult == 1 else f"{part}^{mult}")
    return "(" + ",".join(pieces) + ")"


@dataclass(frozen=True)
class Passport:
    degree: int
    cycle_types: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]
    display: tuple[str, str, str]
    ramification_total: int


@dataclass(frozen=True)
class TerminalReduction:
    a: int
    ell: int
    b: int
    k: int
    m: int
    n: int
    rho: int
    sigma: int
    gap: int
    N: int
    deg_p: int
    deg_q: int
    deg_p_bar: int
    deg_q_bar: int
    uniformizing: Passport
    lattice_quotient: Passport
    terminal_coordinate_exponent_r: str
    uniformizing_ode: str
    quotient_ode: str


def _passport(parts0: tuple[int, ...], parts1: tuple[int, ...], parts2: tuple[int, ...]) -> Passport:
    degree = sum(parts0)
    assert sum(parts1) == degree and sum(parts2) == degree
    rh = sum(x - 1 for parts in (parts0, parts1, parts2) for x in parts)
    assert rh == 2 * degree - 2
    return Passport(
        degree=degree,
        cycle_types=(parts0, parts1, parts2),
        display=tuple(_partition_text(parts) for parts in (parts0, parts1, parts2)),
        ramification_total=rh,
    )


def terminal_passport(m: int, n: int, b: int) -> Passport:
    """Ambient passport on the fractional uniformizing z-line.

    Kept under the historical function name for compatibility with earlier
    scripts.  For the polynomial/lattice-compatible passport use
    ``terminal_reduction(...).lattice_quotient``.
    """
    if min(m, n, b) <= 0:
        raise ValueError("m,n,b must be positive")
    if gcd(m, n) != 1 or min(m, n) <= 1:
        raise ValueError("standard-pair application assumes coprime m,n>1")
    D = m * n * b
    H = (m + n) * b - 1
    return _passport(
        tuple([n] * (m * b)),
        tuple([m] * (n * b)),
        tuple([H] + [1] * (D - H)),
    )


def primitive_direction(*, a: int, ell: int, b: int, k: int, n: int) -> tuple[int, int]:
    """Primitive (rho,sigma) from sigma/rho=(k-na)/(n ell b)."""
    numerator = k - n * a
    denominator = n * ell * b
    d = gcd(abs(numerator), denominator)
    rho, sigma = denominator // d, numerator // d
    assert rho > 0 and gcd(rho, abs(sigma)) == 1
    return rho, sigma


def terminal_reduction(
    *, a: int, ell: int, b: int, k: int, m: int, n: int
) -> TerminalReduction:
    if min(a, ell, b, k, m, n) <= 0:
        raise ValueError("all corner parameters must be positive")
    if gcd(m, n) != 1 or min(m, n) <= 1:
        raise ValueError("m,n must be coprime and >1")

    # Equation (3.17), in the orientation st(Q)=(k/ell,0).
    assert (m + n) * b * k - n * (b * ell - a) == k

    rho, sigma = primitive_direction(a=a, ell=ell, b=b, k=k, n=n)
    r = Fraction(-sigma, rho)
    assert r == Fraction(n * a - k, n * ell * b)
    gap = rho // gcd(rho, ell)

    A, B = Fraction(ell - k, ell), Fraction(1)
    C, D = Fraction(k, ell), Fraction(0)
    c_pq = A * D - B * C
    c_pqprime = A - B * r
    c_pprimeq = r * D - C
    scale = -Fraction(n * ell, k)
    assert (scale * c_pq, scale * c_pqprime, scale * c_pprimeq) == (n, -m, n)

    deg_p, deg_q = m * b - 1, n * b
    assert A + r * deg_p == Fraction(m * a, ell)
    assert B + deg_p == m * b
    assert C + r * deg_q == Fraction(n * a, ell)
    assert D + deg_q == n * b

    # Lattice support: only powers z^gap occur.  The degree divisibilities
    # are therefore necessary for a genuine complete-chain corner.
    assert deg_p % gap == 0
    assert deg_q % gap == 0
    assert gcd(gap, b) == 1
    assert n % gap == 0

    N = n // gap
    Abar, Bbar = deg_p // gap, deg_q // gap
    Dbar = m * n * b // gap
    Hbar_num = (m + n) * b - 1
    assert Hbar_num % gap == 0
    Hbar = Hbar_num // gap
    quotient = _passport(
        tuple(sorted([n] * Abar + [N], reverse=True)),
        tuple([m] * Bbar),
        tuple([Hbar] + [1] * (Dbar - Hbar)),
    )

    return TerminalReduction(
        a=a,
        ell=ell,
        b=b,
        k=k,
        m=m,
        n=n,
        rho=rho,
        sigma=sigma,
        gap=gap,
        N=N,
        deg_p=deg_p,
        deg_q=deg_q,
        deg_p_bar=Abar,
        deg_q_bar=Bbar,
        uniformizing=terminal_passport(m, n, b),
        lattice_quotient=quotient,
        terminal_coordinate_exponent_r=str(r),
        uniformizing_ode=f"{n}*p*q - {m}*z*p*q' + {n}*z*p'*q = 1",
        quotient_ode=f"{N}*pbar*qbar - {m}*u*pbar*qbar' + {n}*u*pbar'*qbar = 1/{gap}",
    )


def verify_final_corner_arithmetic(
    *, a: int, ell: int, b: int, k: int, m: int, n: int
) -> dict[str, object]:
    """Backward-compatible JSON-style wrapper around :func:`terminal_reduction`."""
    rec = terminal_reduction(a=a, ell=ell, b=b, k=k, m=m, n=n)
    return {
        "direction": [rec.rho, rec.sigma],
        "direction_ratio_sigma_over_rho": str(Fraction(rec.sigma, rec.rho)),
        "terminal_coordinate_exponent_r": rec.terminal_coordinate_exponent_r,
        "gap": rec.gap,
        "N": rec.N,
        "deg_p": str(rec.deg_p),
        "deg_q": str(rec.deg_q),
        "deg_p_bar": str(rec.deg_p_bar),
        "deg_q_bar": str(rec.deg_q_bar),
        "normalized_ode": rec.uniformizing_ode,
        "quotient_ode": rec.quotient_ode,
        "uniformizing_passport": rec.uniformizing.display,
        "lattice_quotient_passport": rec.lattice_quotient.display,
        "uniformizing_degree": rec.uniformizing.degree,
        "lattice_quotient_degree": rec.lattice_quotient.degree,
    }


def verify_explicit_f2_solution() -> dict[str, str]:
    """Verify the unique lattice-compatible F2 quotient and its C5 pullback."""
    pbar = 1 - u
    qbar = sp.Rational(1, 5) - sp.Rational(3, 5) * u + sp.Rational(9, 25) * u**2
    qode = sp.expand(
        pbar * qbar
        - 3 * u * pbar * sp.diff(qbar, u)
        + 5 * u * sp.diff(pbar, u) * qbar
    )
    assert qode == sp.Rational(1, 5)
    taubar = sp.cancel(u * pbar**5 / qbar**3)
    assert sp.cancel(sp.diff(taubar, u) - sp.Rational(1, 5) * pbar**4 / qbar**4) == 0

    p = sp.expand(pbar.subs(u, z**5))
    q = sp.expand(qbar.subs(u, z**5))
    ode = sp.expand(5 * p * q - 3 * z * p * sp.diff(q, z) + 5 * z * sp.diff(p, z) * q)
    assert ode == 1
    tau = sp.cancel(z**5 * p**5 / q**3)
    assert sp.cancel(tau - taubar.subs(u, z**5)) == 0
    assert sp.cancel(sp.diff(tau, z) - z**4 * p**4 / q**4) == 0

    return {
        "pbar": str(sp.expand(pbar)),
        "qbar": str(sp.expand(qbar)),
        "taubar": "u*pbar(u)^5/qbar(u)^3",
        "p": str(p),
        "q": str(q),
        "tau": "taubar(z^5)",
    }


def _serialize(obj: object) -> object:
    if isinstance(obj, Passport):
        data = asdict(obj)
        data["cycle_types"] = [list(x) for x in obj.cycle_types]
        data["display"] = list(obj.display)
        return data
    if isinstance(obj, TerminalReduction):
        return {
            **{k: v for k, v in asdict(obj).items() if k not in {"uniformizing", "lattice_quotient"}},
            "uniformizing": _serialize(obj.uniformizing),
            "lattice_quotient": _serialize(obj.lattice_quotient),
        }
    return obj


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int, default=7)
    parser.add_argument("--ell", type=int, default=5)
    parser.add_argument("--b", type=int, default=2)
    parser.add_argument("--k", type=int, default=1)
    parser.add_argument("--m", type=int, default=3)
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rec = terminal_reduction(a=args.a, ell=args.ell, b=args.b, k=args.k, m=args.m, n=args.n)
    payload: dict[str, object] = {"terminal_reduction": _serialize(rec)}
    if (args.a, args.ell, args.b, args.k, args.m, args.n) == (7, 5, 2, 1, 3, 5):
        payload["explicit_F2_solution"] = verify_explicit_f2_solution()
        assert rec.gap == 5
        assert rec.lattice_quotient.degree == 6
        assert rec.lattice_quotient.display == ("(5,1)", "(3^2)", "(3,1^3)")

    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    print("all terminal-face, lattice-gap, quotient, passport, derivative, and RH checks passed")


if __name__ == "__main__":
    main()
