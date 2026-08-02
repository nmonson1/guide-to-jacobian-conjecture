#!/usr/bin/env python3
"""Exact symbolic checks for the Pluecker-chart marking transport."""

from __future__ import annotations

import itertools
import sympy as sp

lam = sp.symbols("lambda0:5")
mu = sp.symbols("mu0:5")
ell = sp.symbols("ell0:5")


def eta(i: int, j: int) -> sp.Expr:
    return sp.expand(lam[i] * mu[j] - lam[j] * mu[i])


def main() -> int:
    for i, j, k, l in itertools.combinations(range(5), 4):
        relation = eta(i, j) * eta(k, l) - eta(i, k) * eta(j, l) + eta(i, l) * eta(j, k)
        assert sp.expand(relation) == 0

    for i, j in itertools.combinations(range(5), 2):
        denominator = eta(i, j)
        p = [sp.cancel(eta(r, j) / denominator) for r in range(5)]
        q = [sp.cancel(eta(i, r) / denominator) for r in range(5)]
        assert sp.cancel(p[i] - 1) == 0
        assert sp.cancel(p[j]) == 0
        assert sp.cancel(q[i]) == 0
        assert sp.cancel(q[j] - 1) == 0

        expected_p = [
            sp.cancel((mu[j] * lam[r] - lam[j] * mu[r]) / denominator)
            for r in range(5)
        ]
        expected_q = [
            sp.cancel((-mu[i] * lam[r] + lam[i] * mu[r]) / denominator)
            for r in range(5)
        ]
        assert all(sp.cancel(x - y) == 0 for x, y in zip(p, expected_p))
        assert all(sp.cancel(x - y) == 0 for x, y in zip(q, expected_q))

        zeta = [sum(ell[r] * eta(r, s) for r in range(5)) for s in range(5)]
        ell_p = sum(ell[r] * p[r] for r in range(5))
        ell_q = sum(ell[r] * q[r] for r in range(5))
        assert sp.cancel(ell_p - zeta[j] / denominator) == 0
        assert sp.cancel(ell_q + zeta[i] / denominator) == 0

    print("verified 5 Pluecker relations and all 10 normalized charts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
