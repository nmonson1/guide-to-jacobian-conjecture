#!/usr/bin/env python3
"""Attack 8: a 13-term exact functional detecting the quartic obstruction.

For the normalized 11D degree-three map K=I+Q+C, the unique scalar
monomial triangular quadratic shift lowering the cubic-coordinate span
from seven to six is P2=-d^2 e_a.  Its exact conjugate has quartic error D4.

This script verifies a compact linear functional Lambda_4 such that
    Lambda_4([Q,P3]) = 0 for every cubic vector field P3,
    Lambda_4(D4) = 1.
Thus D4 is not in the image of the quartic homological operator.
"""
from __future__ import annotations
import itertools
import sympy as sp
import base19_data as B

X = B.X
Q = sp.Matrix(B.K2)
n = len(X)
assert n == 11
x, y, z, a, b, c, d, q, s, h, k = X
JQ = Q.jacobian(X)

D4 = sp.zeros(n, 1)
D4[2] = d**3*z + 3*d**2*y**2
D4[3] = x**2*y**2
D4[5] = -2*d**3*z - 6*d**2*y**2

# (output row, quartic monomial, coefficient in Lambda_4)
terms = [
    (3, x**2*y**2, sp.Rational(1)),
    (3, x**2*a*c, sp.Rational(4)),
    (3, x**2*a*s, -sp.Rational(20, 3)),
    (3, x**2*q*k, sp.Rational(9)),
    (3, x*c*h*k, sp.Rational(3)),
    (3, x*d**2*q, -sp.Rational(1, 2)),
    (3, x*s*h*k, sp.Rational(-7)),
    (3, y**2*a*h, sp.Rational(4, 3)),
    (3, y*b*c*h, -sp.Rational(1, 2)),
    (3, y*d*h*k, sp.Rational(-1)),
    (3, z*a**2*h, sp.Rational(8, 3)),
    (3, a*q*h*k, sp.Rational(25)),
    (6, d*q*h*k, sp.Rational(-2)),
]
support = [(row, sp.Poly(mon, *X).monoms()[0]) for row, mon, _ in terms]
lam = sp.Matrix([[co for _, _, co in terms]])

def functional(R: sp.Matrix) -> sp.Expr:
    ans = 0
    for row, mon, co in terms:
        ans += co * sp.Poly(R[row], *X, domain=sp.QQ).coeff_monomial(mon)
    return sp.factor(ans)

assert functional(D4) == 1

mons3 = []
for comb in itertools.combinations_with_replacement(range(n), 3):
    mon = sp.Integer(1)
    for i in comb:
        mon *= X[i]
    mons3.append(mon)
assert len(mons3) == 286

# Restricted matrix of the homological operator on the 13 support rows.
columns = []
for row in range(n):
    for mon in mons3:
        P = sp.zeros(n, 1)
        P[row] = mon
        delta = (JQ*P - P.jacobian(X)*Q).applyfunc(sp.expand)
        col = [
            sp.Poly(delta[out], *X, domain=sp.QQ).coeff_monomial(exp)
            for out, exp in support
        ]
        columns.append(col)
        assert sum(co*v for (_, _, co), v in zip(terms, col)) == 0

R = sp.Matrix(13, len(columns), lambda i, j: columns[j][i])
dvec = sp.Matrix([
    sp.Poly(D4[out], *X, domain=sp.QQ).coeff_monomial(exp)
    for out, exp in support
])

assert R.rank() == 12
assert R.row_join(dvec).rank() == 13
assert lam*R == sp.zeros(1, R.cols)
assert (lam*dvec)[0] == 1

# The support is a circuit: every proper 12-row subset already has rank 12.
for omitted in range(13):
    keep = [i for i in range(13) if i != omitted]
    assert R[keep, :].rank() == 12

print("[ok] Lambda_4 annihilates [Q,P3] for all 3146 cubic monomial vector fields")
print("[result] Lambda_4(D4)=1, so D4 is not in im(delta_Q)")
print("[ok] the 13 support rows form a minimal circuit: ranks 12 vs 13 augmented")
