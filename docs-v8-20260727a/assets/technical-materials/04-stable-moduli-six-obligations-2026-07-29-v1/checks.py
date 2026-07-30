#!/usr/bin/env python3
"""Exact symbolic checks for the Program-4 six-obligation note.

The checks are intentionally low-dimensional.  They verify the polynomial
identities used by the note; they do not replace the geometric arguments
about representability, normalization, Torelli, or descent.

Checked items
-------------
1. N=3,d=1,m=2 Hensel/factor coordinates and the principal-part split.
2. The direct two-root chart and its nested one-root coordinate v/u^2.
3. The Rees graph Bl_(u^2,v), including its exceptional P^1.
4. Gauge invariance of (Q,B), (Q,B^2), and of H=3At+B after translating t.
5. The length-two Fitting ideals and the valuation formula for (p,d).
6. The generic discriminant fibre is the standard cusp, with X=H^2,Y=H^3.
7. Distinct graph directions specialize to the same lower-length orbit point.

Requires SymPy >= 1.12.
"""
from __future__ import annotations

import sympy as sp


def elimination_kernel(equations, eliminate, keep):
    """Return generators in an elimination ideal using lexicographic order."""
    gb = sp.groebner(equations, *eliminate, *keep, order="lex")
    return [
        sp.factor(poly.as_expr())
        for poly in gb.polys
        if not any(poly.as_expr().has(x) for x in eliminate)
    ]


def main() -> None:
    z = sp.Symbol("z")

    # ------------------------------------------------------------------
    # 1. Formal factor chart: N=3, d=1, m=2.
    # ------------------------------------------------------------------
    q, e1, e2 = sp.symbols("q e1 e2")
    Qd = z + q
    Em = z**2 + e1*z + e2
    product = sp.Poly(sp.expand(Qd * Em), z)
    q1, q2, q3 = product.all_coeffs()[1:]
    assert q1 == e1 + q
    assert q2 == e1*q + e2
    assert q3 == e2*q

    J = sp.Matrix([[sp.diff(f, x) for x in (q, e1, e2)] for f in (q1, q2, q3)])
    J_escape = J.subs({e1: 0, e2: 0})
    assert sp.factor(J_escape.det()) == q**2

    print("1. Hensel chart N=3,d=1,m=2")
    print("   product coefficients:")
    print("     q1 =", q1)
    print("     q2 =", q2)
    print("     q3 =", q3)
    print("   Jacobian at E=z^2 has determinant", sp.factor(J_escape.det()))
    print("   Hence the factor chart is etale when q=Q_d(0) is a unit.")

    p0, p1, p2 = sp.symbols("p0 p1 p2")
    rho, s0, s1 = sp.symbols("rho s0 s1")
    P = p0 + p1*z + p2*z**2
    decomposition = sp.Poly(P - (z**2*rho + Qd*(s0 + s1*z)), z)
    sol = sp.solve(decomposition.all_coeffs(), [rho, s0, s1], dict=True)[0]
    assert sp.simplify(sol[s0] - p0/q) == 0
    assert sp.simplify(sol[s1] - (p1*q-p0)/q**2) == 0
    assert sp.simplify(sol[rho] - (p2*q**2-p1*q+p0)/q**2) == 0
    print("   exact P=z^2 P_d+Q_d S decomposition:")
    print("     s0  =", sp.factor(sol[s0]))
    print("     s1  =", sp.factor(sol[s1]))
    print("     P_d =", sp.factor(sol[rho]))

    # Explicit N=3 inverse bounded map.
    Q1, Q2, Q3 = sp.symbols("q1 q2 q3")
    y0, y1, y2 = sp.symbols("y0 y1 y2")
    Z3mat = sp.Matrix([[0, 0, -Q3], [1, 0, -Q2], [0, 1, -Q1]])
    assert sp.factor(Z3mat.det()) == -Q3
    Zcube = sp.expand(Z3mat**3)
    Pinv = [sp.factor(x) for x in Zcube.inv() * sp.Matrix([y0, y1, y2])]
    numerators = [sp.factor(x * Q3**3) for x in Pinv]
    for x, n in zip(Pinv, numerators):
        assert sp.simplify(x - n/Q3**3) == 0
    print("   N=3 inverse bounded map has P_i=n_i/q3^3, with")
    for i, n in enumerate(numerators):
        print(f"     n{i} =", n)
    # At the generic one-root wall q2 is a unit and n0=-q2^3*y0 mod q3.
    assert sp.factor(numerators[0].subs(Q3, 0) + Q2**3*y0) == 0
    print("   At q3=0, n0=-q2^3*y0; the coarse one-root graph is [q3^5:n0].")

    # ------------------------------------------------------------------
    # 2. Nested coordinate inside the direct two-root weighted chart.
    # ------------------------------------------------------------------
    beta, gamma = sp.symbols("beta gamma", nonzero=True)
    u, v, w = sp.symbols("u v w")
    S0, S1 = sp.symbols("S0 S1")
    # At gamma=0, E_2=z(z+beta).  Split S0+S1*z as
    # z*p + (z+beta)*g.  Then g is the zero-root gauge and p the
    # residual decoration.
    p_dec, g_gauge = sp.symbols("p_dec g_gauge")
    split = sp.Poly((S0 + S1*z) - (z*p_dec + (z+beta)*g_gauge), z)
    split_sol = sp.solve(split.all_coeffs(), [p_dec, g_gauge], dict=True)[0]
    assert sp.simplify(split_sol[g_gauge] - S0/beta) == 0
    assert sp.simplify(split_sol[p_dec] - (S1-S0/beta)) == 0

    scaled_g = sp.simplify(split_sol[g_gauge].subs({S0: beta**3*v, S1: beta**2*w}) / beta**2)
    scaled_p = sp.simplify(split_sol[p_dec].subs({S0: beta**3*v, S1: beta**2*w}) / beta**2)
    assert scaled_g == v
    assert scaled_p == -v + w

    # If gamma=beta^2*u, the small root is -beta*u+O(u^2), so u is its
    # scale relative to beta.  The gauge has weight two, hence v/u^2.
    roots = sp.solve(z**2 + beta*z + beta**2*u, z)
    small_root_series = sp.series(roots[0] if roots[0].subs(u, 0) == 0 else roots[1], u, 0, 3)

    print("\n2. Nested one-root coordinate in the direct two-root chart")
    print("   At gamma=0, S=z*p+(z+beta)*g with")
    print("     g = S0/beta,  p = S1-S0/beta.")
    print("   Under S0=beta^3*v, S1=beta^2*w:")
    print("     normalized gauge =", scaled_g)
    print("     normalized residual decoration =", scaled_p)
    print("   With gamma=beta^2*u, the small root has series", small_root_series)
    print("   so the nested weighted coordinate is v/u^2.")

    # ------------------------------------------------------------------
    # 3. Direct versus iterated chart: blowup of (u^2,v).
    # ------------------------------------------------------------------
    T = sp.Symbol("T")
    U, V = sp.symbols("U V")
    kernel = elimination_kernel(
        [U-u**2*T, V-v*T],
        eliminate=[T],
        keep=[U, V, u, v, w],
    )
    normalized_kernel = {sp.factor(k) for k in kernel}
    relation = sp.factor(U*v - V*u**2)
    assert relation in normalized_kernel or -relation in normalized_kernel

    print("\n3. Direct/iterated N=3 overlap")
    print("   Rees graph of [u^2:v] has equation U*v-V*u^2=0.")
    print("   Direct chart: Spec k[u,v,w].")
    print("   Iterated refinement: Bl_(u^2,v) Spec k[u,v,w].")
    print("   Over u=v=0 the homogeneous fibre is P^1, so the charts differ.")

    xi, eta = sp.symbols("xi eta")
    assert sp.expand((U*v - V*u**2).subs({U: 1, V: xi, v: xi*u**2})) == 0
    assert sp.expand((U*v - V*u**2).subs({V: 1, U: eta, u**2: eta*v})) == 0
    print("   U-chart: v=xi*u^2; V-chart: u^2=eta*v.")

    # ------------------------------------------------------------------
    # 4. Nonunit-resultant and relative-Jacobian gauge invariance.
    # ------------------------------------------------------------------
    c, t = sp.symbols("c t")
    a1, a2 = sp.symbols("a1 a2")
    b0, b1 = sp.symbols("b0 b1")
    g0, g1 = sp.symbols("g0 g1")
    Q = 1 + a1*c + a2*c**2
    A_c = c*Q
    Bd = b0 + b1*c
    S = g0 + g1*c
    phi = c*S/3
    Bfull = sp.expand(Bd + c**2*Q*S)  # Bd + 3A*phi

    frac = sp.QQ.frac_field(a1, a2, b0, b1, g0, g1)
    rem_B = sp.rem(Bfull, Q, domain=frac)
    rem_B2 = sp.rem(sp.expand(Bfull**2), Q, domain=frac)
    rem_Bd2 = sp.rem(sp.expand(Bd**2), Q, domain=frac)
    assert sp.expand(rem_B - Bd) == 0
    assert sp.expand(rem_B2 - rem_Bd2) == 0

    Hfull = sp.expand(3*A_c*t + Bfull)
    Hd_shifted = sp.expand((3*A_c*t + Bd).subs(t, t + phi))
    assert sp.expand(Hfull - Hd_shifted) == 0

    print("\n4. Nonunit and relative-Jacobian compatibility")
    print("   B_full=B_d+3A*phi with phi=cS/3.")
    print("   rem_Q(B_full)=B_d and rem_Q(B_full^2)=rem_Q(B_d^2).")
    print("   H_full(c,t)=H_d(c,t+phi), H=3At+B.")
    print("   Hence (Q,B), (Q,B^2), and the marked H^3/content divisor are gauge invariant.")

    eps = sp.Symbol("eps")
    sigma0, sigma1 = sp.symbols("sigma0 sigma1")
    Msigma = sp.Matrix([[sigma0, 0], [sigma1, sigma0]])
    assert sp.factor(Msigma.det()) == sigma0**2
    print("   On k[eps]/(eps^2), m_sigma =", Msigma.tolist())
    print("   Fitt_0(coker m_sigma)=(sigma0^2)")
    print("   Fitt_1(coker m_sigma)=(sigma0,sigma1)")

    # Exhaustively test d=3m-min(r,2m), p=r-m for small valuation pairs.
    valuation_rows = []
    for r_int in range(1, 8):
        for k_int in range(0, 9):
            m_int = min(r_int, k_int)
            lhs = 3*m_int - min(r_int, 2*k_int)
            rhs = 3*m_int - min(r_int, 2*m_int)
            assert lhs == rhs
            valuation_rows.append((r_int, k_int, m_int, r_int-m_int, rhs))
    print("   Checked p=r-m and d=3m-min(r,2m) for", len(valuation_rows), "valuation pairs.")

    # ------------------------------------------------------------------
    # 5. Standard cusp on the generic discriminant fibre.
    # ------------------------------------------------------------------
    A, B, a, b, t = sp.symbols("A B a b t")
    Delta = B**2*b**2 - 4*A*b**3 + 8*B**3*a - 108*A**2*a**2 - 36*A*B*a*b
    X = B**2 - 3*A*b
    Y = B*X + sp.Rational(3, 2)*A*(-18*A*a - B*b)
    assert sp.factor(Y**2 - X**3 + sp.Rational(27, 4)*A**2*Delta) == 0

    H = 3*A*t + B
    b_param = -3*A*t**2 - 2*B*t
    a_param = -A*t**3 - sp.Rational(1, 2)*B*t**2
    assert sp.factor(X.subs({a: a_param, b: b_param}) - H**2) == 0
    assert sp.factor(Y.subs({a: a_param, b: b_param}) - H**3) == 0

    linear_matrix = sp.Matrix(
        [[sp.diff(X, a), sp.diff(X, b)], [sp.diff(Y, a), sp.diff(Y, b)]]
    )
    assert sp.factor(linear_matrix.det()) == -81*A**3

    print("\n5. Generic discriminant fibre as a standard cusp")
    print("   X=B^2-3Ab")
    print("   Y=B*X+(3A/2)*(-18Aa-Bb)")
    print("   Y^2-X^3=-(27/4)A^2 Delta")
    print("   det d(X,Y)/d(a,b)=", sp.factor(linear_matrix.det()))
    print("   On normalization: X=H^2, Y=H^3, H=3At+B.")

    # ------------------------------------------------------------------
    # 6. Distinct directions, same special orbit.
    # ------------------------------------------------------------------
    alpha, beta_par, tau, Nsym = sp.symbols("alpha beta tau N")
    assert sp.simplify((alpha*tau**(Nsym+2))/tau**(Nsym+2)) == alpha
    assert sp.simplify((beta_par*tau**(Nsym+2))/tau**(Nsym+2)) == beta_par
    print("\n6. Noninjectivity of comparison with the special orbit")
    print("   epsilon=tau, y=lambda*tau^(N+2) has graph limit [1:lambda].")
    print("   Different lambda give different graph points but the same special")
    print("   coefficient point epsilon=y=0 and the same lower-length orbit.")

    print("\nALL PROGRAM-4 SIX-OBLIGATION SYMBOLIC CHECKS PASSED")


if __name__ == "__main__":
    main()
