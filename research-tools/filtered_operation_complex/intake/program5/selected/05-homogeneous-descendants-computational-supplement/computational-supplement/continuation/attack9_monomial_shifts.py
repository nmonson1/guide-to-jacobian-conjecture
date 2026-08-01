#!/usr/bin/env python3
"""Attack 9: exhaustive scalar-monomial triangular quadratic shifts.

For P2=lambda*m*e_r, with m a quadratic monomial not involving X_r,
test whether the cubic jet C+[Q,P2] can have coordinate-span rank <=6.

There are 11*C(11,2)=605 such triangular monomial directions.
A fixed nonzero 7x7 minor of C gives a univariate exceptional polynomial.
Only 22 directions have a nonconstant exceptional polynomial; all 27 roots
are rational and are checked by full exact rank.
"""
from __future__ import annotations
import itertools
import sympy as sp
import base19_data as B

X = B.X
Q = sp.Matrix(B.K2)
C = sp.Matrix(B.K3)
n = len(X)
JQ = Q.jacobian(X)
lam = sp.symbols("lambda")

mons3_exp = []
for comb in itertools.combinations_with_replacement(range(n), 3):
    e = [0]*n
    for i in comb:
        e[i] += 1
    mons3_exp.append(tuple(e))
assert len(mons3_exp) == 286

Ccoef = sp.Matrix([
    [sp.Poly(f, *X, domain=sp.QQ).coeff_monomial(e) for e in mons3_exp]
    for f in C
])
active = [i for i in range(n) if any(Ccoef.row(i))]
assert active == [0, 1, 2, 3, 4, 5, 8]
_, piv = Ccoef[active, :].rref()
piv = list(piv[:7])
Cminor = Ccoef.extract(active, piv)
assert Cminor.det() == -36

def monomial(exp):
    ans = sp.Integer(1)
    for v, e in zip(X, exp):
        if e:
            ans *= v**e
    return ans

directions = []
for r in range(n):
    allowed = [i for i in range(n) if i != r]
    for i0, j0 in itertools.combinations_with_replacement(allowed, 2):
        e = [0]*n
        e[i0] += 1
        e[j0] += 1
        directions.append((r, tuple(e)))
assert len(directions) == 605

constant = 0
exceptional = []
for r, exp in directions:
    m = monomial(exp)
    delta = [sp.expand(JQ[i, r]*m) for i in range(n)]
    delta[r] = sp.expand(delta[r] - sum(sp.diff(m, X[j])*Q[j] for j in range(n)))

    dsmall = sp.zeros(7, 7)
    for ii, out in enumerate(active):
        p = sp.Poly(delta[out], *X, domain=sp.QQ)
        for jj, col in enumerate(piv):
            dsmall[ii, jj] = p.coeff_monomial(mons3_exp[col])
    determinant = sp.factor((Cminor + lam*dsmall).det())
    if sp.Poly(determinant, lam).degree() == 0:
        constant += 1
    else:
        exceptional.append((r, exp, delta, determinant))

assert constant == 583
assert len(exceptional) == 22

checks = []
drops = []
for r, exp, delta, determinant in exceptional:
    roots = sp.roots(determinant, lam)
    assert sum(roots.values()) == sp.Poly(determinant, lam).degree()
    dcoef = sp.Matrix([
        [sp.Poly(delta[i], *X, domain=sp.QQ).coeff_monomial(e)
         for e in mons3_exp]
        for i in range(n)
    ])
    for root, multiplicity in roots.items():
        assert root.is_Rational
        rank = (Ccoef + root*dcoef).rank()
        checks.append((r, exp, root, multiplicity, rank))
        if rank <= 6:
            drops.append((r, exp, root, rank))

assert len(checks) == 27
expected_exp = [0]*n
expected_exp[6] = 2
assert drops == [(3, tuple(expected_exp), sp.Rational(-1), 6)]

print("[ok] 605 scalar monomial triangular quadratic shifts checked exactly")
print("[ok] 583 have no exceptional parameter; 22 give 27 rational roots")
print("[result] the unique rank-six shift is P2=-d^2 e_a")
