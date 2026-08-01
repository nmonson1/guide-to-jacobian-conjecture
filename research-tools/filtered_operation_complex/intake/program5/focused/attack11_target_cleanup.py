#!/usr/bin/env python3
"""Attack 11: independent target cleanup cannot promote the rank-six jet
within the natural low-degree quadratic target model.

After the unique quadratic conjugacy a -> a-d^2, the exact map has cubic
coordinate-span rank six and a rank-two quartic error:
    D4_z = d^2(dz+3y^2),  D4_a=x^2y^2,  D4_c=-2D4_z.

The output coordinates d,q,h,k have degree at most two.  Therefore a
quadratic target automorphism built only from these coordinates creates no
terms above degree four.  This script checks the full ten-dimensional space
of such corrections.

D4_z (and hence D4_c) is not in its quartic image.  D4_a has a unique
preimage, -Y_d^2, but that correction raises the cubic-coordinate span back
from six to seven.
"""
from __future__ import annotations
import itertools
import sympy as sp
import base19_data as B

X = B.X
K = sp.Matrix(B.K)
n = len(X)
x,y,z,a,b,c,d,q,s,h,k = X

def homogeneous_part(expr, degree):
    P = sp.Poly(sp.expand(expr), *X, domain=sp.QQ)
    ans = 0
    for mon, coeff in P.terms():
        if sum(mon) == degree:
            term = coeff
            for v,e in zip(X,mon):
                term *= v**e
            ans += term
    return sp.expand(ans)

def coefficient_matrix(vec, degree):
    exps = []
    for comb in itertools.combinations_with_replacement(range(n), degree):
        e=[0]*n
        for i in comb:
            e[i]+=1
        exps.append(tuple(e))
    return sp.Matrix([
        [sp.Poly(f,*X,domain=sp.QQ).coeff_monomial(e) for e in exps]
        for f in vec
    ]), exps

# Exact conjugacy S(a)=a-d^2, S^{-1}(a)=a+d^2.
S = sp.Matrix(X)
S[3] = a-d**2
KS = K.subs({X[i]:S[i] for i in range(n)}, simultaneous=True).applyfunc(sp.expand)
Kc = KS.copy()
Kc[3] = sp.expand(KS[3] + KS[6]**2)

C3 = sp.Matrix([homogeneous_part(f,3) for f in Kc])
D4 = sp.Matrix([homogeneous_part(f,4) for f in Kc])
Ccoef,_ = coefficient_matrix(C3,3)
assert Ccoef.rank() == 6
assert sp.expand(D4[2]-d**2*(d*z+3*y**2)) == 0
assert sp.expand(D4[3]-x**2*y**2) == 0
assert sp.expand(D4[5]+2*d**2*(d*z+3*y**2)) == 0
assert all(D4[i] == 0 for i in range(n) if i not in (2,3,5))

# All quadratic products of the exact low-degree output coordinates d,q,h,k.
low = [6,7,9,10]
products = [
    sp.expand(Kc[i]*Kc[j])
    for i,j in itertools.combinations_with_replacement(low,2)
]
assert len(products) == 10
P3vec = sp.Matrix([homogeneous_part(f,3) for f in products])
P4vec = sp.Matrix([homogeneous_part(f,4) for f in products])
P4coef, exps4 = coefficient_matrix(P4vec,4)
P4map = P4coef.T
assert P4map.rank() == 10

def rhs(poly):
    P=sp.Poly(poly,*X,domain=sp.QQ)
    return sp.Matrix([P.coeff_monomial(e) for e in exps4])

# z and c quartics cannot be removed in this entire target-correction space.
for row in (2,5):
    target = rhs(-D4[row])
    assert P4map.row_join(target).rank() == 11

# The a quartic has exactly one correction: -Y_d^2.
target_a = rhs(-D4[3])
assert P4map.row_join(target_a).rank() == 10
sol = next(iter(sp.linsolve((P4map,target_a))))
assert sol == (-1,0,0,0,0,0,0,0,0,0)

Kclean = Kc.copy()
Kclean[3] = sp.expand(Kc[3]-Kc[6]**2)
Cclean = sp.Matrix([homogeneous_part(f,3) for f in Kclean])
Cclean_coef,_ = coefficient_matrix(Cclean,3)
assert Cclean_coef.rank() == 7

print("[ok] the exact conjugate has cubic span 6 and quartic span 2")
print("[ok] ten low-output quadratic target corrections have independent quartic images")
print("[result] D4_z and D4_c are outside that image")
print("[result] D4_a is uniquely killed by -Y_d^2, which restores cubic span 7")
