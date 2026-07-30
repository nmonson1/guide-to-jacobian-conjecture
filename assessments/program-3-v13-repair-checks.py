#!/usr/bin/env python3
"""Exact symbolic checks supporting the Program 3 v13 corrigendum.

This script checks only the displayed shear identities and the corrected
conjugation argument for Theorem C.2. It does not verify the large Kuranishi,
radical, inverse-system, or border-basis certificates.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    reduced = sp.factor(sp.expand(expr))
    if reduced != 0:
        raise AssertionError(f"{label}: expected 0, got {reduced}")


def main() -> None:
    x, y, z, tau = sp.symbols("x y z tau", nonzero=True)
    a, b, c = sp.symbols("a b c")
    A, B, C = sp.symbols("A B C")

    u = 1 + x * y
    P = u**3 * z + y**2 * u * (4 + 3 * x * y)
    Q = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    R = 2 * x - 3 * x**2 * y - x**3 * z
    G = (R / 2, Q, P)

    f = a * x**2 + b * x * y + c * y**2
    g = A * x**2 + B * x * y + C * y**2

    # Proposition C.1: substitute z -> z + f.
    Gf = tuple(sp.expand(component.subs(z, z + f)) for component in G)
    delta_expected = (-x**3 * f / 2, 3 * x * u**2 * f, u**3 * f)
    for i, (actual, base, delta) in enumerate(zip(Gf, G, delta_expected), 1):
        assert_zero(actual - base - delta, f"quadratic shear identity, component {i}")

    # The unique degree-eight term is in the third component.
    p = sp.Poly(sp.expand(Gf[2]), x, y, z)
    degree_eight_terms = []
    for monom, coeff in p.terms():
        if sum(monom) == 8:
            degree_eight_terms.append(
                coeff * x**monom[0] * y**monom[1] * z**monom[2]
            )
    assert_zero(
        sum(degree_eight_terms) - x**3 * y**3 * f,
        "degree-eight leading term",
    )

    # With A_tau = diag(tau^-1, tau, tau^2), the source map forced by a
    # target torus symmetry is alpha = phi_f^{-1} A_tau phi_g.
    normal_term = sp.expand(
        tau**2 * g
        - f.subs({x: tau**-1 * x, y: tau * y}, simultaneous=True)
    )
    equations = [sp.Eq(coef, 0) for coef in sp.Poly(normal_term, x, y).coeffs()]
    solution = sp.solve(equations, (A, B, C), dict=True)
    expected = [{A: a * tau**-4, B: b * tau**-2, C: c}]
    if solution != expected:
        raise AssertionError(
            f"affineness equations: expected {expected}, got {solution}"
        )

    # Renaming sigma=tau^-1 gives the theorem's action.
    sigma = sp.symbols("sigma", nonzero=True)
    theorem_action = sp.expand(
        sigma**2
        * f.subs({x: sigma * x, y: sigma**-1 * y}, simultaneous=True)
    )
    theorem_coefficients = sp.Poly(theorem_action, x, y)
    if theorem_coefficients.coeff_monomial(x**2) != a * sigma**4:
        raise AssertionError("x^2 weight is not 4")
    if theorem_coefficients.coeff_monomial(x * y) != b * sigma**2:
        raise AssertionError("xy weight is not 2")
    if theorem_coefficients.coeff_monomial(y**2) != c:
        raise AssertionError("y^2 weight is not 0")

    print("PASS: Proposition C.1 shear identity")
    print("PASS: unique degree-eight leading term x^3 y^3 f")
    print("PASS: corrected Theorem C.2 affineness equations")
    print("PASS: torus weights (4, 2, 0) on (x^2, xy, y^2)")
    print("BOUNDARY: no degree-eight residual Kuranishi claim is checked here")


if __name__ == "__main__":
    main()
