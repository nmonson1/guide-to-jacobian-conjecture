#!/usr/bin/env python3
"""Exact symbolic checks for the Lane 7 Pluecker marking transport."""

from __future__ import annotations

import itertools

import sympy as sp

u = sp.symbols("u0:5")
v = sp.symbols("v0:5")
d = sp.symbols("d", nonzero=True)
b = sp.symbols("b0:25")
B = sp.Matrix(5, 5, b)


def eta(i: int, j: int, second: tuple[sp.Expr, ...] | list[sp.Expr] = v) -> sp.Expr:
    return sp.expand(u[i] * second[j] - u[j] * second[i])


def main() -> int:
    # The five quadratic equations for Gr(2,5).
    for i, j, k, ell in itertools.combinations(range(5), 4):
        relation = (
            eta(i, j) * eta(k, ell)
            - eta(i, k) * eta(j, ell)
            + eta(i, ell) * eta(j, k)
        )
        assert sp.expand(relation) == 0

    # Every independent pair lies in one of these ten normalized charts.
    for i, j in itertools.combinations(range(5), 2):
        denominator = eta(i, j)
        p = [sp.cancel(eta(r, j) / denominator) for r in range(5)]
        q = [sp.cancel(eta(i, r) / denominator) for r in range(5)]
        assert sp.cancel(p[i] - 1) == 0
        assert sp.cancel(p[j]) == 0
        assert sp.cancel(q[i]) == 0
        assert sp.cancel(q[j] - 1) == 0

        expected_p = [
            sp.cancel((v[j] * u[r] - u[j] * v[r]) / denominator)
            for r in range(5)
        ]
        expected_q = [
            sp.cancel((-v[i] * u[r] + u[i] * v[r]) / denominator)
            for r in range(5)
        ]
        assert all(sp.cancel(x - y) == 0 for x, y in zip(p, expected_p))
        assert all(sp.cancel(x - y) == 0 for x, y in zip(q, expected_q))

    # On D(d), Theorem C reconstructs v=-d^{-1}Bu. Thus
    # d*eta_ij=-(u_i(Bu)_j-u_j(Bu)_i) for every Pluecker coordinate.
    Bu = B * sp.Matrix(u)
    reconstructed_v = tuple(sp.cancel(-entry / d) for entry in Bu)
    for i, j in itertools.combinations(range(5), 2):
        phi = sp.expand(u[i] * Bu[j] - u[j] * Bu[i])
        transported = sp.cancel(d * eta(i, j, reconstructed_v) + phi)
        assert transported == 0

    # The formerly normalized affine open is precisely eta_34 on v4=1.
    assert sp.expand(eta(3, 4).subs(v[4], 1) - (u[3] - u[4] * v[3])) == 0

    print(
        "verified 5 Pluecker relations, all 10 normalized charts, "
        "and d*eta_ij=-Phi_ij for the projective-kernel reconstruction"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
