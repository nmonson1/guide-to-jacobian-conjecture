#!/usr/bin/env python3
"""Exact checks for the formal-effectivity theorem of the cubic-frame q-modulus.

The script verifies finite polynomial identities underlying the proof:

1. the general root-translation left-right identity;
2. the exact residual formula for every tested degree D;
3. the annihilator/degree law over C[s]/(s^M) for several ramification orders;
4. compatibility of the optimal Artin gauges under truncation;
5. exact source and target degree formulas in the unramified case;
6. the residual affine-frame equations and their inability to lower degree;
7. unbounded c-degree of the compatible formal limit.

The nonexistence of a stable equivalence over C[[s]] uses the published
stable q-classification on the generic fiber and is recorded as a theorem
input rather than a CAS assertion.
"""
from __future__ import annotations

import json
from math import ceil
from pathlib import Path

import sympy as sp


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def truncate_s(expr: sp.Expr, s: sp.Symbol, c: sp.Symbol, modulus: int) -> sp.Expr:
    """Reduce a polynomial in s,c modulo s**modulus."""
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    result = sp.Integer(0)
    for (se, ce), coeff in sp.Poly(expr, s, c).terms():
        if se < modulus:
            result += coeff * s**se * c**ce
    return sp.expand(result)


def c_degree(expr: sp.Expr, c: sp.Symbol) -> int:
    expr = sp.expand(expr)
    if expr == 0:
        return -1
    return int(sp.Poly(expr, c).degree())


def total_degree(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> int:
    expr = sp.expand(expr)
    if expr == 0:
        return -1
    return int(sp.Poly(expr, *variables).total_degree())


def main() -> None:
    # ------------------------------------------------------------------
    # 1. General frame-coordinate identity.
    # ------------------------------------------------------------------
    A, B, phi, t, b_target = sp.symbols("A B phi t b_target")
    B_shifted = B + 3 * A * phi
    ell = 3 * A * phi**2 + 2 * B * phi
    eta = A * phi**3 + B * phi**2

    # Source shift t -> t+phi produces b_source=b_target-ell.
    b_source = b_target - ell
    two_a_source = sp.expand(
        A * (t + phi) ** 3
        + B * (t + phi) ** 2
        + (t + phi) * b_source
    )
    two_a_after_target = sp.expand(two_a_source - phi * b_source - eta)
    two_a_desired = sp.expand(A * t**3 + B_shifted * t**2 + t * b_target)
    check(two_a_after_target == two_a_desired, "root-translation LR identity")

    # Source invariant c is fixed.
    x, y, z, P = sp.symbols("x y z P")
    c_xyz = 2 * x - 3 * x**2 * y - x**3 * z
    c_transformed = sp.expand(
        2 * x - 3 * x**2 * (y + P) - x**3 * (z - 3 * P / x)
    )
    check(sp.expand(c_transformed - c_xyz) == 0, "source transformation fixes c")

    # ------------------------------------------------------------------
    # 2. Universal residual formula.
    # ------------------------------------------------------------------
    alpha, delta, c = sp.symbols("alpha delta c")
    A_alpha = c * (1 + alpha * c)
    residual_checks: list[dict[str, object]] = []
    for D in range(0, 11):
        if D == 0:
            phi_D = sp.Integer(0)
        else:
            phi_D = sp.expand(
                delta
                * alpha**2
                * c
                * sum((-alpha * c) ** j for j in range(D))
                / 3
            )
        residual = sp.expand(delta * alpha**2 * c**2 - 3 * A_alpha * phi_D)
        expected = sp.expand((-1) ** D * delta * alpha ** (D + 2) * c ** (D + 2))
        check(residual == expected, f"universal residual formula D={D}")
        residual_checks.append(
            {
                "D": D,
                "phi_c_degree": c_degree(phi_D, c),
                "residual": str(sp.factor(residual)),
            }
        )

    # ------------------------------------------------------------------
    # 3. Ramification law over C[s]/(s^M).
    # ------------------------------------------------------------------
    s, q, qp, lam = sp.symbols("s q qp lam")
    dq = qp - q

    # Exact orbit-cokernel relation for alpha=s: in the quotient by
    # 1+s*c, multiplication by s has inverse -c.
    orbit_relation = sp.expand(s * (-c) - 1)
    orbit_denominator_basic = sp.Poly(
        1 + s * c,
        c,
        domain=sp.QQ.frac_field(s),
    )
    orbit_remainder = sp.rem(
        sp.Poly(orbit_relation, c, domain=sp.QQ.frac_field(s)),
        orbit_denominator_basic,
    )
    check(orbit_remainder.as_expr() == 0, "s is invertible in orbit cokernel")
    obstruction_numerator = sp.Poly(
        dq * s**2,
        c,
        domain=sp.QQ.frac_field(s, q, qp),
    )
    orbit_denominator = sp.Poly(
        1 + s * c,
        c,
        domain=sp.QQ.frac_field(s, q, qp),
    )
    _, obstruction_remainder = sp.div(obstruction_numerator, orbit_denominator)
    check(
        sp.expand(obstruction_remainder.as_expr() - dq * s**2) == 0,
        "q obstruction is nonzero in generic orbit cokernel",
    )

    ramification_table: list[dict[str, object]] = []

    for M in range(2, 15):
        for e in range(1, min(5, M)):
            nilpotence_index = ceil(M / e)
            D_min = max(0, nilpotence_index - 2)
            alpha_me = s**e
            A_me = c * (1 + alpha_me * c)

            if D_min == 0:
                phi_min = sp.Integer(0)
            else:
                phi_min = sp.expand(
                    dq
                    * alpha_me**2
                    * c
                    * sum((-alpha_me * c) ** j for j in range(D_min))
                    / 3
                )

            residual_min = truncate_s(
                dq * alpha_me**2 * c**2 - 3 * A_me * phi_min,
                s,
                c,
                M,
            )
            check(residual_min == 0, f"ramified existence M={M}, e={e}")

            actual_degree = c_degree(truncate_s(phi_min, s, c, M), c)
            expected_degree = -1 if D_min == 0 else D_min
            check(actual_degree == expected_degree, f"ramified degree M={M}, e={e}")

            if D_min > 0:
                phi_prev = (
                    sp.Integer(0)
                    if D_min == 1
                    else sp.expand(
                        dq
                        * alpha_me**2
                        * c
                        * sum((-alpha_me * c) ** j for j in range(D_min - 1))
                        / 3
                    )
                )
                residual_prev = truncate_s(
                    dq * alpha_me**2 * c**2 - 3 * A_me * phi_prev,
                    s,
                    c,
                    M,
                )
                check(residual_prev != 0, f"ramified sharpness M={M}, e={e}")

            ramification_table.append(
                {
                    "M": M,
                    "e": e,
                    "nilpotence_index": nilpotence_index,
                    "minimal_c_degree": max(0, actual_degree),
                    "frames_already_equal": D_min == 0,
                }
            )

    # ------------------------------------------------------------------
    # 4. Unramified compatibility and exact degree staircase.
    # ------------------------------------------------------------------
    compatibility_table: list[dict[str, object]] = []
    phi_by_M: dict[int, sp.Expr] = {}
    for M in range(1, 15):
        if M <= 2:
            phi_M = sp.Integer(0)
        else:
            phi_M = sp.expand(
                dq * s**2 * c * sum((-s * c) ** j for j in range(M - 2)) / 3
            )
        phi_by_M[M] = phi_M

        A_s = c * (1 + s * c)
        residual = truncate_s(
            dq * s**2 * c**2 - 3 * A_s * phi_M,
            s,
            c,
            M,
        )
        check(residual == 0, f"unramified equivalence mod s^{M}")

        if M >= 3:
            check(c_degree(phi_M, c) == M - 2, f"unramified exact degree M={M}")
            top = sp.expand(phi_M).coeff(c, M - 2)
            expected_top = dq * (-1) ** (M - 3) * s ** (M - 1) / 3
            check(sp.expand(top - expected_top) == 0, f"unramified top term M={M}")

        compatibility_table.append(
            {
                "M": M,
                "c_degree": max(0, c_degree(phi_M, c)),
                "source_degree": 1 if M <= 2 else 4 * (M - 2),
                "target_degree": 1 if M <= 2 else M - 1,
            }
        )

    for M in range(1, 14):
        reduced_next = truncate_s(phi_by_M[M + 1], s, c, M)
        current = truncate_s(phi_by_M[M], s, c, M)
        check(reduced_next == current, f"compatibility M={M+1}->M={M}")

    # ------------------------------------------------------------------
    # 5. Exact source and target coordinate degrees.
    # ------------------------------------------------------------------
    d = 2 - 3 * x * y - x**2 * z
    c_source = x * d
    degree_table: list[dict[str, object]] = []
    bvar, avar, cvar = sp.symbols("b a c")

    for M in range(3, 11):
        D = M - 2
        phi_M_source = sp.expand(phi_by_M[M].subs(c, c_source))
        theta_y = sp.expand(y + phi_M_source)
        theta_z = sp.expand(z - 3 * phi_M_source / x)
        source_degree = max(
            total_degree(x, (x, y, z)),
            total_degree(theta_y, (x, y, z)),
            total_degree(theta_z, (x, y, z)),
        )
        check(source_degree == 4 * D, f"source degree M={M}")

        # Target corrections over R_M; use B_q and reduce in s.
        phi_target = phi_by_M[M].subs(c, cvar)
        A_target = cvar * (1 + s * cvar)
        B_target = -2 - 4 * s * cvar + q * s**2 * cvar**2
        ell_target = truncate_s(
            3 * A_target * phi_target**2 + 2 * B_target * phi_target,
            s,
            cvar,
            M,
        )
        eta_target = truncate_s(
            A_target * phi_target**3 + B_target * phi_target**2,
            s,
            cvar,
            M,
        )
        xi_a = sp.expand(avar - phi_target * bvar / 2 - eta_target / 2)
        xi_b = sp.expand(bvar + ell_target)
        target_degree = max(
            total_degree(xi_a, (avar, bvar, cvar)),
            total_degree(xi_b, (avar, bvar, cvar)),
            1,
        )
        # The inverse is triangular.  Equivalently it is the target map for
        # the reverse root translation from B+3Aphi back to B.
        xi_inv_a = sp.expand(
            avar
            + phi_target * bvar / 2
            - truncate_s(phi_target * ell_target, s, cvar, M) / 2
            + eta_target / 2
        )
        xi_inv_b = sp.expand(bvar - ell_target)
        target_inverse_degree = max(
            total_degree(xi_inv_a, (avar, bvar, cvar)),
            total_degree(xi_inv_b, (avar, bvar, cvar)),
            1,
        )
        check(target_degree == D + 1, f"target degree M={M}")
        check(target_inverse_degree == D + 1, f"target inverse degree M={M}")
        check(c_degree(ell_target, cvar) <= D, f"ell c-degree M={M}")
        check(c_degree(eta_target, cvar) <= D - 1, f"eta c-degree M={M}")

        degree_table.append(
            {
                "M": M,
                "D": D,
                "source_degree": source_degree,
                "target_degree": target_degree,
                "target_inverse_degree": target_inverse_degree,
                "ell_c_degree": c_degree(ell_target, cvar),
                "eta_c_degree": c_degree(eta_target, cvar),
            }
        )

    # ------------------------------------------------------------------
    # 6. Residual affine framed transformations.
    # ------------------------------------------------------------------
    affine_table: list[dict[str, object]] = []
    for M in range(3, 13):
        D = M - 2
        u = 1 + lam * s ** (M - 1)
        u_inv = 1 - lam * s ** (M - 1)
        h = truncate_s(-u_inv * phi_by_M[M], s, c, M)

        A_s = c * (1 + s * c)
        B_q = -2 - 4 * s * c + q * s**2 * c**2
        B_qp = -2 - 4 * s * c + qp * s**2 * c**2

        A_relation = truncate_s(
            A_s.subs(c, u * c) * u_inv - A_s,
            s,
            c,
            M,
        )
        B_relation = truncate_s(
            B_qp.subs(c, u * c)
            + 3 * A_s.subs(c, u * c) * h
            - B_q,
            s,
            c,
            M,
        )
        check(A_relation == 0, f"affine A relation M={M}")
        check(B_relation == 0, f"affine B relation M={M}")
        check(c_degree(h, c) == D, f"affine degree unchanged M={M}")
        affine_table.append(
            {
                "M": M,
                "residual_scaling": f"u=1+lambda*s^{M-1}",
                "h_c_degree": D,
            }
        )

    # ------------------------------------------------------------------
    # 7. The formal limit has unbounded c-degree.
    # ------------------------------------------------------------------
    formal_coefficients: list[dict[str, object]] = []
    for n in range(2, 13):
        coeff = dq * (-1) ** (n - 2) * c ** (n - 1) / 3
        check(c_degree(coeff, c) == n - 1, f"formal coefficient degree n={n}")
        formal_coefficients.append(
            {
                "s_power": n,
                "coefficient": str(coeff),
                "c_degree": n - 1,
                "source_y_degree": 4 * (n - 1),
            }
        )

    report = {
        "status": "ALL FORMAL-EFFECTIVITY CHECKS PASSED",
        "theorem_inputs_not_cas_checked": [
            "stable q-classification on the generic fiber: Program 4, thm:main / cor:q-classification",
            "constant generic-combination lemma for an empty affine generic fiber",
            "D'Andrea-Krick-Sombra parametric effective Nullstellensatz (Theorem 0.5)",
        ],
        "universal_residual_checks": residual_checks,
        "ramification_samples": ramification_table,
        "unramified_compatibility": compatibility_table,
        "canonical_degree_checks": degree_table,
        "affine_frame_checks": affine_table,
        "formal_limit_coefficients": formal_coefficients,
        "orbit_cokernel": "C[[s]][c]/(1+s*c) = C((s))",
        "orbit_obstruction_class": "(q'-q)/3 * s^2",
        "orbit_cokernel_s_inverse": "-c",
        "formal_limit_ring": "C[c][[s]]",
        "polynomial_complete_base_ring": "C[[s]][c]",
        "noncommutation": (
            "lim_M colim_D Isom_D(R_M) is nonempty, "
            "while colim_D lim_M Isom_D(R_M) is empty"
        ),
    }

    output = Path(__file__).with_name("formal_effectivity_report.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(report["status"])
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
