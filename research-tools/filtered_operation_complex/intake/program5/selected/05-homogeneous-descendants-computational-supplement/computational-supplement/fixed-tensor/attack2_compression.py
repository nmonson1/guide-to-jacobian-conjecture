#!/usr/bin/env python3
"""Attack 2: rank-compressed suspension and a cubic-jet obstruction."""
from __future__ import annotations
import itertools
import sympy as sp
import base19_data as M

# K = X + Q + C with C=Bq and rank of the cubic-coordinate span equal to 7.
assert M.K1 == sp.Matrix(M.X)
assert M.K3 == M.B*M.q
cubic_mons = sorted(set().union(*[
    set(sp.Poly(e, *M.X).monoms()) for e in M.K3
]))
coef = sp.Matrix([[sp.Poly(e, *M.X).coeff_monomial(mon) for mon in cubic_mons]
                  for e in M.K3])
assert coef.rank() == 7

# Exact stable equivalence of the 18D suspension.
W = sp.Matrix(M.w)
q = M.q
Q = M.K2
B = M.B
# S(X,w)=(X,w-q), then K x id, then T(U,V)=(U+B V,V).
source_after_S = sp.Matrix(M.X).col_join(W-q)
after_K = M.K.col_join(W-q)
after_T = (M.K + B*(W-q)).col_join(W-q)
expected = (sp.Matrix(M.X)+Q+B*W).col_join(W-q)
assert (after_T-expected).applyfunc(sp.expand) == sp.zeros(18, 1)

# Homogeneous 19D map and the small determinant certificate.
t = M.t
Jsmall = sp.eye(11) + t*Q.jacobian(M.X) + t**2*B*q.jacobian(M.X)
JK_scaled = M.K.jacobian(M.X).subs({M.X[i]: t*M.X[i] for i in range(11)})
assert (Jsmall-JK_scaled).applyfunc(sp.expand) == sp.zeros(11)
# The Schur complement of the w-block in JG is exactly Jsmall.
Jtop_left = sp.eye(11)+t*Q.jacobian(M.X)
Jtop_w = t**2*B
Jbot_x = -q.jacobian(M.X)
assert (Jtop_left-Jtop_w*Jbot_x-Jsmall).applyfunc(sp.expand) == sp.zeros(11)

# Cubic jet under quadratic conjugacy: C -> C + [Q,P],
# [Q,P]=JQ P-JP Q.  The b-coordinate Q_5 is zero.
assert Q[4] == 0
pairs = [(i, j) for i in range(11) for j in range(i, 11)]
u = sp.symbols(f"u0:{len(pairs)}")
Pb = sum(a*M.X[i]*M.X[j] for a, (i, j) in zip(u, pairs))
bracket_b = -sum(sp.diff(Pb, M.X[k])*Q[k] for k in range(11))
poly = sp.Poly(sp.expand(bracket_b), *M.X)

def cc(mon):
    return poly.coeff_monomial(mon)

# Lambda(f)=[x^2 y]f + 1/3[x^2 k]f + 1/3[x z h]f -2[d h k]f.
Lambda_bracket = (cc(M.x**2*M.y) + sp.Rational(1, 3)*cc(M.x**2*M.k)
                  + sp.Rational(1, 3)*cc(M.x*M.z*M.h)
                  - 2*cc(M.d*M.h*M.k))
assert sp.expand(Lambda_bracket) == 0
Cb = M.K3[4]
Cp = sp.Poly(Cb, *M.X)
Lambda_C = (Cp.coeff_monomial(M.x**2*M.y)
            + sp.Rational(1, 3)*Cp.coeff_monomial(M.x**2*M.k)
            + sp.Rational(1, 3)*Cp.coeff_monomial(M.x*M.z*M.h)
            - 2*Cp.coeff_monomial(M.d*M.h*M.k))
assert Lambda_C == 3

print("[ok] cubic-coordinate span rank r=7")
print("[ok] 18D stable-equivalence identity")
print("[ok] determinant reduces to det JK(tX) by an 11x11 Schur complement")
print("[ok] exact cubic-jet obstruction Lambda([Q,P]_b)=0, Lambda(C_b)=3")
print("[result] mu(F0) <= 11+7=18, hence N_cubic <= 19")
