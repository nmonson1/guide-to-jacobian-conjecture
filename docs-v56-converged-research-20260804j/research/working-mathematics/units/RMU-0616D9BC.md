---
title: "Rational-quartic frontier exclusion"
description: "Assume the preceding frontier reduction: every proper rational-quartic\nleading image not already excluded has either\n\\[\n(\\deg q,\\textup{ tangent-syzygy type})=(3,(1,2))\n\\quad\\text{or}\\quad\n(2,(2,2)).\n\\]\nNeither stratum occurs as the projective leading image of a quartic Keller\nmap."
---

# Rational-quartic frontier exclusion

`RMU-0616D9BC` · `theorem` · statement version `1`

## Exact statement

Assume the preceding frontier reduction: every proper rational-quartic
leading image not already excluded has either
\[
(\deg q,\textup{ tangent-syzygy type})=(3,(1,2))
\quad\text{or}\quad
(2,(2,2)).
\]
Neither stratum occurs as the projective leading image of a quartic Keller
map.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU0616D9BC-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

For type \((3,(1,2))\), use the tricuspidal parametrization
\[
h=(x^2y^2,\ y^2(x-y)^2,\ x^2(x-y)^2).
\]
Its derivative has the factorization
\[
h_x\times h_y=8xy(x-y)n,\qquad
n=(-(x-y)^3,x^3,-y^3),
\]
and a Hilbert--Burch basis
\[
a=(x+y,x-2y,-2x+y),\qquad
b=(x^2,x^2-3xy+3y^2,x^2).
\]
Thus the most general first normal cubic layer is
\[
z\bigl((px+qy)a+\mu b\bigr)+\rho z^2a.
\]
The \(z^3\)-coefficient of the second jet is
\[
24\rho^2(x^2-xy+y^2)^2,
\]
so \(\rho=0\).  The next coefficient is
\[
12\kappa^2+16xy(x-y)(n\cdot u),
\]
where
\[
\kappa=(\mu+p)x^3+(-2\mu-p+q)x^2y+(p-q)xy^2+qy^3.
\]
Divisibility by the squarefree cubic \(xy(x-y)\) forces
\(\kappa=cxy(x-y)\); comparison of coefficients gives
\[
p=q=\mu=c=0.
\]
The remaining low-degree syzygy is a scalar multiple of \(a\), and a later
coefficient is \(12\sigma^2(x^2-xy+y^2)^2\).  Hence the quadratic layer is
binary as well.  The terminal equation then gives \(L_z=0\), contrary to
\(L\in\operatorname{GL}_3\).

For type \((2,(2,2))\), the ramification divisor has either two distinct
roots or one double root.  In the first case every proper parametrization
is equivalent to
\[
h_m=(x^4+mx^3y,\ x^2y^2,\ y^4+xy^3).
\]
The exceptional values \(m=4\) and \(m=16\) are respectively the
tricuspidal stratum and the previously excluded \((1,3)\) stratum.  Away
from them, explicit quadratic syzygies \(a_m,b_m\) form a Hilbert--Burch
basis.  If \(V=\alpha a_m+\beta b_m\), evaluation of
\eqref{eq:frontier-second-jet} at the two ramification points gives
\[
-216\beta^2x^6,\qquad
-24m\bigl(4\alpha+(m-16)\beta\bigr)^2y^6.
\]
They kill \(\alpha,\beta\); the endpoint \(m=0\) is killed by the next
three coefficient equations without dividing by \(m\).

In the double-root case every proper parametrization is equivalent to
\[
h_{A,B}=(x^4+Ax^3y+Bx^2y^2,\ xy^3,\ y^4).
\]
The \((2,2)\) condition is precisely \(3A^2-8B\ne0\).  For an explicit
quadratic Hilbert--Burch basis \(a,b\), the first two coefficients of
\(Q_h(\alpha a+\beta b)\) are
\[
-12288\alpha^2x^6,\qquad
-6144\alpha(2A\alpha+\beta)x^5.
\]
Thus \(\alpha=0\).  The following three equations yield
\[
u_2=32\beta^2,\qquad
u_1=-8A\beta^2,\qquad
(8B-3A^2)\beta^2=0,
\]
and hence \(\beta=0\).  In both root types the quadratic layer is then
binary and the terminal equation again forces \(L_z=0\).

All displayed identities, the exceptional-parameter identifications, and
the birational inverse formulas are checked both in SymPy and in an
independent sparse-polynomial implementation over \(\mathbb Q\).

[Machine-readable graph](../graph.json)
