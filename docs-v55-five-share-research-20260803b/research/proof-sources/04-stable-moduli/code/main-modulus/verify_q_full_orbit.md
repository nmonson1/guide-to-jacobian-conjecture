---
title: "Text proof source — 04-stable-moduli/code/main-modulus/verify_q_full_orbit.py"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/04-stable-moduli/code/main-modulus/verify_q_full_orbit.py`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `4877184b95f52a574cf37c8234d4110fe9d6d5bb14f1a05f6de890379715b1f0` · 5,593 bytes

## Complete source

~~~python
#!/usr/bin/env python3
"""Exact checks for full/stable rigidity of q in the quadratic cubic-frame slice."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

# Target cubic and discriminant geometry.
c, t, u, v, q, qp = sp.symbols("c t u v q qp")
A = c * (c + 1)
B = q*c**2 - 4*c - 2
poly = A*sp.Symbol('T')**3 + B*sp.Symbol('T')**2 + v*sp.Symbol('T') - 2*u
Delta = sp.expand(B**2*v**2 - 4*A*v**3 + 8*B**3*u - 108*A**2*u**2 - 36*A*B*u*v)
assert sp.factor(sp.discriminant(Delta, u) + 64*(3*A*v - B**2)**3) == 0

# Normalization of the discriminant surface by the repeated root t.
vnu = sp.expand(-3*A*t**2 - 2*B*t)
unu = sp.expand(-A*t**3 - sp.Rational(1,2)*B*t**2)
H = sp.expand(3*A*t + B)
assert sp.factor(Delta.subs({u: unu, v: vnu})) == 0
assert sp.factor((B**2 - 3*A*v).subs(v, vnu)) == H**2
assert sp.factor((-18*A*u - B*v).subs({u: unu, v: vnu})) == 2*t*H**2

# The gradient vanishes exactly over the triple-root conductor H=0.
grad_factors = {
    'du': sp.factor(sp.diff(Delta, u).subs({u: unu, v: vnu})),
    'dv': sp.factor(sp.diff(Delta, v).subs({u: unu, v: vnu})),
    'dc': sp.factor(sp.diff(Delta, c).subs({u: unu, v: vnu})),
}
assert sp.factor(grad_factors['du'] - 8*H**3) == 0
assert sp.factor(grad_factors['dv'] + 4*t*H**3) == 0
assert sp.factor(grad_factors['dc']/H**3) == -4*t**2*(2*c*q + 2*c*t + t - 4)

# The marked nonproperness plane c=-1 lifts to a line M in the normalization.
d = q + 2
assert sp.factor(unu.subs(c, -1) + d*t**2/2) == 0
assert sp.factor(vnu.subs(c, -1) + 2*d*t) == 0
assert sp.factor(H.subs(c, -1) - d) == 0

# q=-2 is exceptional: the discriminant acquires the plane factor c+1.
Delta_m2 = sp.factor(Delta.subs(q, -2))
assert sp.rem(Delta_m2, c+1, c) == 0
assert sp.factor(B.subs(q, -2)) == -2*(c+1)**2

# At q=-2 the residual discriminant component is singular where it meets the plane.
Delta_res_m2 = sp.factor(Delta_m2/(c+1))
assert sp.factor(Delta_res_m2.subs(c,-1)) == 4*v**3
assert sp.factor(sp.diff(Delta_res_m2,u).subs({c:-1,u:0,v:0})) == 0
assert sp.factor(sp.diff(Delta_res_m2,v).subs({c:-1,u:0,v:0})) == 0
assert sp.factor(sp.diff(Delta_res_m2,c).subs({c:-1,u:0,v:0})) == 0
# For q != -2, the discriminant component is smooth along its intersection with c=-1.
assert sp.factor(sp.diff(Delta,u).subs(c,-1) - 8*(q+2)**3) == 0

# Triple-root component tends to (u,v,c)=(0,0,-1) at q=-2.
ug_m2 = sp.factor((-B**3/(54*A**2)).subs(q, -2))
vg_m2 = sp.factor((B**2/(3*A)).subs(q, -2))
assert ug_m2 == 4*(c+1)**4/(27*c**2)
assert vg_m2 == 4*(c+1)**3/(3*c)
assert sp.limit(ug_m2, c, -1) == 0
assert sp.limit(vg_m2, c, -1) == 0

# Symbolic coefficient comparison in the marked-normalization rigidity lemma.
lam, mu, kap = sp.symbols('lam mu kap', nonzero=True)
h0, h1 = sp.symbols('h0 h1')
C = lam*(c+1)-1
# T is forced to be mu*t+h(c); for coefficient checks a generic polynomial h is represented symbolically.
h = sp.Function('h')(c)
BqpC = qp*C**2 - 4*C - 2
Hpull = sp.expand(3*C*(C+1)*(mu*t+h) + BqpC)
Hq = sp.expand(3*c*(c+1)*t + B)
coeff_t = sp.factor(sp.diff(Hpull - kap*Hq, t))
# The coefficient is exactly the expression used in the proof.
assert sp.factor(coeff_t - 3*(c + 1)*(c*lam**2*mu - c*kap + lam**2*mu - lam*mu)) == 0

# Exact equivalence of the alpha=0 line to the base via an LND flow.
x, y, z, s = sp.symbols('x y z s')
T, Csym = sp.symbols('T C')
r = sp.Rational(2)/x
source_c = sp.expand(2*x - 3*x**2*y - x**3*z)
source_t = y + 1/x

def frame_map(Aexpr: sp.Expr, Bexpr: sp.Expr) -> sp.Matrix:
    h_expr = Aexpr*T**3 + Bexpr*T**2
    b_expr = sp.expand(sp.cancel(r - sp.diff(h_expr, T).subs({T: source_t, Csym: source_c})))
    a_expr = sp.expand(sp.cancel((h_expr.subs({T: source_t, Csym: source_c}) + source_t*b_expr)/2))
    return sp.Matrix([a_expr, b_expr, source_c])

Fbase = frame_map(Csym, -2)
beta = 3*s
Fbeta = frame_map(Csym, -2 + beta*Csym**2)
source_c_over_x = sp.expand(source_c/x)
Theta = sp.Matrix([
    x,
    y + s*source_c,
    z - 3*s*source_c_over_x,
])
theta_sub = {x: Theta[0], y: Theta[1], z: Theta[2]}
assert sp.factor(source_c.subs(theta_sub, simultaneous=True) - source_c) == 0
assert sp.factor(Theta.jacobian((x,y,z)).det()) == 1
Fbase_theta = sp.Matrix([
    sp.expand(sp.cancel(e.subs(theta_sub, simultaneous=True))) for e in Fbase
])
L = 3*s**2*Csym**3 - 4*s*Csym
D = s**3*Csym**4 - 2*s**2*Csym**2
# K o Fbeta = Fbase o Theta.
a_b, b_b, c_b = Fbeta
K_Fbeta = sp.Matrix([
    sp.expand(a_b + D.subs(Csym,c_b)/2 + s*c_b*(b_b - L.subs(Csym,c_b))/2),
    sp.expand(b_b - L.subs(Csym,c_b)),
    c_b,
])
for i in range(3):
    assert sp.factor(sp.expand(Fbase_theta[i] - K_Fbeta[i])) == 0

# Save a compact audit.
out = {
    'normalized_slice': {
        'A': str(A),
        'B_q': str(B),
        'discriminant': str(Delta),
        'normalization_u': str(unu),
        'normalization_v': str(vnu),
        'conductor_H': str(H),
        'marked_line': 'c + 1 = 0',
    },
    'key_identities': {
        'disc_u_Delta': str(sp.factor(sp.discriminant(Delta,u))),
        'B2_minus_3Av_on_normalization': str(H**2),
        'repeated_root_inverse_numerator': str(2*t*H**2),
        'gradient_factors': {k: str(val) for k,val in grad_factors.items()},
        'q_minus_2_factorization': str(Delta_m2),
    },
    'alpha_zero_equivalence': {
        'beta': '3*s',
        'source_Theta': [str(e) for e in Theta],
        'L': str(L),
        'D': str(D),
    },
}
Path(__file__).with_name('data').mkdir(exist_ok=True)
Path(__file__).with_name('data').joinpath('q_full_orbit.json').write_text(json.dumps(out, indent=2)+'\n')
print('ALL q-ORBIT CHECKS PASSED')
~~~

[Back to the text-source index](../../../index.md)
