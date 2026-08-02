---
title: "Text proof source — 02-low-degree/appendices/quartic-frontier-and-ramification.tex"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/02-low-degree/appendices/quartic-frontier-and-ramification.tex`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `22aaf8d83e0351d580159c10b8dbbe8a19075a736f24fb360e254e244643757a` · 13,123 bytes

## Exact label anchors

<a id="label-app-quartic-frontier-and-ramification"></a>
- `app:quartic-frontier-and-ramification` — source line 2
<a id="label-eq-frontier-first-jet"></a>
- `eq:frontier-first-jet` — source line 32
<a id="label-eq-frontier-second-jet"></a>
- `eq:frontier-second-jet` — source line 33
<a id="label-thm-rational-quartic-frontier-exclusion"></a>
- `thm:rational-quartic-frontier-exclusion` — source line 48
<a id="label-cor-quartic-target-span-two"></a>
- `cor:quartic-target-span-two` — source line 145
<a id="label-prop-plucker-fixed-component"></a>
- `prop:plucker-fixed-component` — source line 173
<a id="label-thm-target-span-two-ramification-two"></a>
- `thm:target-span-two-ramification-two` — source line 226
<a id="label-subsec-degree-three-ramification-frontier"></a>
- `subsec:degree-three-ramification-frontier` — source line 330

## Complete source

~~~tex
\section{Closing the rational-quartic frontier}
\label{app:quartic-frontier-and-ramification}

This appendix records a continuation of the leading-curve analysis.  It has
two purposes.  First, it closes the two proper rational-quartic strata left
by the frontier theorem.  Second, once the leading target span has thereby
been reduced to two, it eliminates the regular, simple-ramification, and
double-ramification parts of the coprime binary-pencil locus, together with
the genuinely nonbinary quadratic-source locus.  The complete proof notes
and exact checkers are preserved in
\begin{center}
\texttt{code/program-2-2026-07-27-v1/}.
\end{center}

\subsection{The two proper rational-quartic strata}

Let
\[
h=(h_0,h_1,h_2)\in\C[x,y]_4^3
\]
be a basepoint-free proper parametrization of a plane quartic.  Write
\[
h_x\times h_y=q\,n
\]
with \(n\) primitive.  If
\[
H_3=C_3(x,y)+zV(x,y),\qquad
H_2=D_2(x,y)+zW_1(x,y)+z^2u,
\]
the first two determinant-jet equations are
\begin{align}
(h_x\times h_y)\cdot V&=0, \label{eq:frontier-first-jet}\\
[z]E_2&=Q_h(V)+2(h_x\times h_y)\cdot u=0, \label{eq:frontier-second-jet}
\end{align}
where
\[
Q_h(V)=\det(V_x,h_y,V)+\det(h_x,V_y,V).
\]
If \(V=0\), the same equations make \(W_1+2zu\) a low-degree
syzygy of \(n\).  If both lower nonlinear layers are binary, the next
equation is
\[
E_3=(h_x\times h_y)\cdot L_z,
\]
where \(L_z\) is the third column of \(L\).

\begin{theorem}[Rational-quartic frontier exclusion]
\label{thm:rational-quartic-frontier-exclusion}
Assume the preceding frontier reduction: every proper rational-quartic
leading image not already excluded has either
\[
(\deg q,\textup{ tangent-syzygy type})=(3,(1,2))
\quad\text{or}\quad
(2,(2,2)).
\]
Neither stratum occurs as the projective leading image of a quartic Keller
map.
\end{theorem}

\begin{proof}
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
\end{proof}

\begin{corollary}[Exact leading target span in degree four]
\label{cor:quartic-target-span-two}
Subject to the leading-image routing of \cref{lem:leading-image} and
\cref{rem:leaf-accounting}, every nonautomorphic quartic Keller map has
leading target span exactly two.
\end{corollary}

\begin{proof}
By \cref{lem:leading-image} the leading image is a point, a line, or a
proper rational curve of degree two, three, or four, with leaf table
\((e,k,\deg G)\in\{(2,1,2),(2,2,0),(3,1,1),(4,1,0)\}\).  The point
case is \cref{thm:rank-one}, and the line case is target span two.  The
conic, quadratic-Veronese, and cubic-image leaves are closed by
\cref{thm:conic} together with the register results cited leaf by leaf
in \cref{rem:leaf-accounting}; the quartic leaf is closed by
\cref{thm:rational-quartic-frontier-exclusion} above, whose frontier
pre-classification is likewise recorded there.  The register legs carry
certificate or proof-offered evidence rather than reader-manuscript
proofs, which is the precise content of the qualifier in the statement.
\end{proof}

\subsection{An independent fixed-component check}

The next calculation belongs to the rank-one route, not to the
target-span-two theorem.  We retain it because it closes the sole
fixed-component chart left by the earlier \(2+2\) calculation and supplies
an independently implemented coefficient proof of that special case.

\begin{proposition}[Fixed-component Pl\"ucker boundary]
\label{prop:plucker-fixed-component}
In the normalized chart
\[
H_4=(0,0,x^2y^2),\qquad
(H_3)_1=x^2y,\qquad (H_3)_2=xy^2,
\]
the Keller equations force the third column of \(L\) to vanish.  Hence this
chart cannot occur for a Keller map with invertible linear part.
\end{proposition}

\begin{proof}[Computer-assisted coefficient proof]
The complete high-syzygy solution has parameters
\(t_1,t_2,u_1,\ldots,u_4,c\).  Selected degree-five coefficients first give
\[
t_1=t_2=u_2=u_3=0,\qquad
9c+u_1^2-4u_1u_4+u_4^2=0.
\]
The \(xyz^2\)-coefficient of \(D_4\) and the \(z^3\)-coefficient of \(D_3\)
then give
\[
(u_1-2u_4)(u_1+u_4)(2u_1-u_4)=0,
\]
\[
u_1u_4(u_1^2-4u_1u_4+u_4^2)=0.
\]
Their only common zero is \(u_1=u_4=0\), so \(c=0\).

Writing the third column of \(L\) as
\((\alpha,\beta,\gamma)^T\), two further coefficients determine the
\(xz,yz\) terms of \((H_2)_3\) from \(\alpha,\beta\).  Three square
coefficients then give \(\alpha=\beta=0\), and the remaining degree-four
coefficient is \(3\gamma\).  Hence \(\gamma=0\).  Both a SymPy construction
of the full determinant and an independent standard-library sparse
implementation verify this chain with every unrestricted lower coefficient
present.
\end{proof}

\subsection{The target-span-two ramification filtration}

In the binary-pencil locus write
\[
H_4=(P,Q,0),\qquad P,Q\in S_4,\qquad
R=(H_3)_3\in S_3,\qquad S=\C[x,y].
\]
Set
\[
U=J(Q,R),\qquad V=J(P,R),\qquad W=J(P,Q),
\qquad \Delta=\gcd(U,V,W).
\]
The divisor \(\Delta\) measures common ramification of the weighted binary
map \([x:y]\mapsto[P:Q:R]\).

\begin{theorem}[Target-span-two exclusions through double ramification]
\label{thm:target-span-two-ramification-two}
Assume \cref{prop:four-loci}, the low-degree plane theorem, the cubic-cube
coordinate reduction, and the primitive fourth-power exclusion used in
this manuscript.
\begin{enumerate}[label=(\roman*)]
\item If the binary pencil is regular, \(\Delta=1\), then \(F\) is a
polynomial automorphism.
\item No quartic Keller map lies in the genuinely nonbinary,
no-fixed-component quadratic-source locus.
\item If \(P,Q\) are coprime and \(\deg\Delta\le2\), then \(F\) is a
polynomial automorphism.
\end{enumerate}
Consequently a nonautomorphic map in the coprime binary locus must satisfy
\[
\deg\Delta\ge3.
\]
\end{theorem}

\begin{proof}
For (i), the maximal minors \((U,-V,W)\) of the two-row gradient matrix have
height two.  Hilbert--Burch gives two minimal syzygies of total degree
eight.  The coefficients of \(D_7\) have total degrees five, six, and seven,
so every \(z\)-dependent normal term in
\((H_3)_1,(H_3)_2,(H_2)_3\) vanishes.  The equation \(D_6=0\) similarly
kills the remaining nonlinear \(z\)-terms and the relevant entry of \(L\).
The map is triangular over a plane Keller map of degree at most four.

For (ii), write
\[
P=U_0(a,b),\qquad Q=V_0(a,b)
\]
with \(a,b\) coprime quadrics and \([U_0:V_0]\) of degree two.  A valuation
argument on the generic conic of the pencil shows that a nonbinary survivor
must have a double-line fiber \(a=x^2\) and
\[
R=xb.
\]
There are three nonbinary conic-pencil normal forms
\[
b=x^2+yz,\qquad b=yz,\qquad b=y^2+xz,
\]
and three relative normal forms for the outer double cover.  Exact
elimination in all nine charts, with arbitrary \(H_3,H_2,L\), makes columns
two and three of \(L\) proportional.

It remains to prove (iii) for \(\deg\Delta=1,2\).  At a simple
ramification point, a source shear gives
\[
\begin{aligned}
P&=p_0x^4+p_2x^2y^2+p_3xy^3+p_4y^4,\\
Q&=q_0x^4+q_2x^2y^2+q_3xy^3+q_4y^4,\\
R&=r_0x^3+r_2xy^2+r_3y^3.
\end{aligned}
\]
The first residual normal parameter is supported on the vanishing of the
weighted-inflection determinant
\[
\Omega=
\det\begin{pmatrix}
4p_0&4q_0&3r_0\\
p_2&q_2&r_2\\
p_3&q_3&r_3
\end{pmatrix}.
\]
Classifying \(\Omega=0\) leaves two even families and one special orbit.
The special orbit has the unavoidable coefficient
\[
[xy^4z]D_6=[y^5z]D_6=\frac{104}{3}.
\]
In each even family the remaining equations make
\(\operatorname{col}_2(L)\) proportional to
\(\operatorname{col}_3(L)\).  Thus simple ramification is impossible.

For \(\deg\Delta=2\), the primitive Hilbert--Burch shifts are
\[
(3,7),\qquad(4,6),\qquad(5,5).
\]
The first type enters the cubic-cube/fourth-power boundary.  In type
\((4,6)\), a constant source vector field reduces the nonboundary chart to
\[
R_y=\Delta,\qquad P_y=x\Delta,\qquad Q_y=y\Delta.
\]
The four relative orbits of the quadratic divisor are checked exactly.
They are inconsistent, acquire a fixed component or extra ramification, or
leave the parameter-free obstruction
\[
[y^3z^2]D_5=-\frac13.
\]
In type \((5,5)\), a double root of \(\Delta\) gives a fixed component.
For squarefree \(\Delta\), the normalized forms are
\[
\begin{aligned}
P&=p_0x^4+p_2x^2y^2+p_4y^4,\\
Q&=q_0x^4+q_2x^2y^2+q_4y^4,\\
R&=r_0x^3+r_3y^3.
\end{aligned}
\]
The two extreme coefficients of \(D_6\) show that every nonzero normal
direction produces a fourth-power pencil member.  If the normal direction
vanishes, lower syzygy degrees make the map triangular.  This exhausts
\(\deg\Delta=2\).
\end{proof}

\subsection{What remains in degree four}
\label{subsec:degree-three-ramification-frontier}

The next binary stratum is \(\deg\Delta=3\).  Its primitive
Hilbert--Burch types are \((2,5)\) and \((3,4)\).  The first again enters
the cubic-cube/fourth-power boundary.  In the generic \((3,4)\) chart, the
first transverse normal branch has exact determinant
\[
9216\tau^3(\tau^2+2\tau+3)(3\tau^2+2\tau+1);
\]
the exceptional kernels have dependent \(P,Q\), a cubic cube, or a common
factor.  A later calculation reduces the remaining generic normal
deformations to an explicit weighted-inflection family \(F_4\).

An independent exact verifier over \(\mathbb Q(a,b,\tau)\) reconstructs the
generic \((3,4)\) Hilbert--Burch chart, checks the gradient factorization and
determinantal normal-form identities, and proves that the six next Keller
equations have generic rank six and a two-dimensional kernel with the two
recorded basis vectors.  Over the algebraic closure, intersecting that kernel
plane with the quadratic Veronese image forces the generic transverse
parameters to vanish away from the displayed denominator, rank-drop, and
weighted-inflection divisors.  This exact calculation narrows the remaining
work but does not check the exceptional divisors or the later \(F_4\)
compatibility problem.

We do not promote the complete \(\deg\Delta=3\) exclusion to a theorem.
The conversation calculation leaves one precise compatibility check:
after solving all of \(D_6=0\) over
\[
\mathbb Q(\tau)[d]/(q_4(d,\tau)),
\]
one must prove uniformly that arbitrary lower binary terms cannot cancel
the displayed \(D_5\) obstruction on \(F_4\).  The pure obstruction and
exact sample parameters were checked, but no auditable attached program
completes this extension-field solve.

The continuation in
\cref{app:quartic-high-ramification-fixed-components} closes
\(\deg\Delta=4,5\), the zero-minor boundary, the primitive fourth-power
boundary, and the fixed-component leaves, subject to the upstream routing
used here.  It leaves the exceptional \(\deg\Delta=3\) \(F_4\) system and
a global exhaustiveness audit.  This remains a reduction of the quartic
problem, not a proof that ordinary degree four is impossible.
~~~

[Back to the text-source index](../../index.md)
