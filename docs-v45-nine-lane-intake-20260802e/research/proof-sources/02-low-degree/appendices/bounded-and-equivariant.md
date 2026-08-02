---
title: "Text proof source — 02-low-degree/appendices/bounded-and-equivariant.tex"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/02-low-degree/appendices/bounded-and-equivariant.tex`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `d3e8ecba4716dac6af3f61069a1e0104561c95fa71dcf7bb08cf51c230c5f4a1` · 9,832 bytes

## Exact label anchors

<a id="label-app-bounded-equivariant"></a>
- `app:bounded-equivariant` — source line 2
<a id="label-eq-equivariant-keller"></a>
- `eq:equivariant-keller` — source line 50
<a id="label-lem-equivariant-boundary"></a>
- `lem:equivariant-boundary` — source line 56
<a id="label-thm-equivariant-threshold"></a>
- `thm:equivariant-threshold` — source line 80
<a id="label-rem-equivariant-sharpness"></a>
- `rem:equivariant-sharpness` — source line 87
<a id="label-q-degree-five-six-bridge"></a>
- `q:degree-five-six-bridge` — source line 249

## Complete source

~~~tex
\section{Bounded-degree schemes and the sharp equivariant threshold}
\label{app:bounded-equivariant}

This appendix fixes the finite-algebra framework.  It also records the exact
classification for weights \((-1,1,2)\).  These calculations originally
motivated the unrestricted quartic analysis in the body of the paper.

\subsection{The coefficient scheme and collision slice}

Fix \(n,D\).  After translating the source and target and normalizing the
linear part, write
\[
F=X+\sum_{d=2}^{D}H_d.
\]
Equating the nonconstant coefficients of \(\det JF-1\) defines a finite-type
coefficient scheme \(K_{n,D}\).  At a Keller map \(F\), its tangent equation
in the direction \(H\) is
\[
\operatorname{tr}\bigl((JF)^{-1}JH\bigr)=0
\]
coefficientwise.

If a Keller map has a collision, affine source and target transformations
place the two source points at \(0,e_1\), their common image at \(0\), and
the first Jacobian at the identity, without increasing ordinary degree.
Thus a fixed-degree counterexample search can be conducted in the finite
closed incidence slice
\[
F(0)=F(e_1)=0,\qquad JF(0)=I,\qquad \det JF=1.
\]
This is an implementation framework rather than a novelty claim about
finite coefficient loci themselves.

\subsection{Equivariant quotient equation}

Let
\[
\lambda\cdot(x,y,z)=(\lambda^{-1}x,\lambda y,\lambda^2z),
\qquad u=xy,\quad v=x^2z.
\]
Every normalized equivariant map has a unique Laurent presentation
\[
X=xf(u,v),\qquad
Y=x^{-1}g(u,v),\qquad
Z=x^{-2}h(u,v).
\]
Polynomiality imposes finite support conditions on \(f,g,h\).  The Keller
equation is the planar identity
\begin{equation}
\label{eq:equivariant-keller}
gJ(f,h)-2hJ(f,g)+fJ(g,h)=1,
\end{equation}
where \(J\) denotes the Jacobian in \(u,v\).

\begin{lemma}[Boundary equation]
\label{lem:equivariant-boundary}
Let \(C_f=V(f)\).  Then \(C_f\) is smooth and
\[
gD_fh-2hD_fg=1
\quad\text{on }C_f,
\qquad D_f=J(f,-).
\]
On an affine-line component, if this is written
\[
g_0h_0'-2h_0g_0'=\kappa\ne0,
\]
then \(\deg g_0\le1\).
\end{lemma}

\begin{proof}
At a singular point of \(f=0\), the left side of
\eqref{eq:equivariant-keller} would vanish.  For the degree assertion,
compare the leading term.  If cancellation occurs because
\(\deg h_0=2\deg g_0\), subtract a multiple of \(g_0^2\) from \(h_0\);
this preserves the equation and lowers the degree.  Iteration leaves
\(\deg g_0\le1\).
\end{proof}

\begin{theorem}[Equivariant threshold]
\label{thm:equivariant-threshold}
Every normalized \((-1,1,2)\)-equivariant Keller map of ordinary degree at
most six is a polynomial automorphism.  Equivalently, no counterexample of
ordinary degree at most six exists in this equivariant class.
\end{theorem}

\begin{remark}[Sharpness rests on an external input]
\label{rem:equivariant-sharpness}
The announced degree-seven counterexample \cite{alpoge2026announcement}
appears to carry exactly this \((-1,1,2)\)-symmetry; that equivariance is
read off the displayed public formulas and is neither proved nor certified
in this appendix.  Granting that external identification,
\cref{thm:equivariant-threshold} is sharp and the exact minimum ordinary
degree in this equivariant class is seven; the theorem itself supplies
only the unconditional half of that statement.
\end{remark}

\begin{proof}[Proof and certificate structure]
For degree at most five, the exhaustive support is
\[
\begin{aligned}
f&=1+au+bv+cu^2,\\
g&=u+pv+qu^2+ruv+su^3+tv^2,\\
h&=v+Au^2+Buv+Cu^3+Dv^2+Eu^2v.
\end{aligned}
\]
\Cref{lem:equivariant-boundary} reduces the nonconstant-\(f\) locus to four
exact coefficient ideals.  After the necessary saturations, their
Gr\"obner bases over \(\mathbb Q\) are all \((1)\).  Thus \(f=1\), and
\eqref{eq:equivariant-keller} reduces to \(J(g,h)=1\) for a plane map
\(\psi=(g,h)\) of degree at most three, which is a plane automorphism by
the low-degree plane Jacobian theorem
\cite{appelgateOnishi1985,nagata1988two}.  The
plane automorphism lifts to three variables because the linear part of
\(\psi\) is \(\bigl(\begin{smallmatrix}1&p\\0&1\end{smallmatrix}\bigr)\):
then \(\psi^{-1}\) has no constant terms and the linear \(u\)-coefficient
of its second component vanishes, which is exactly what makes
\((x,y,z)\mapsto
(x,\;x^{-1}\psi^{-1}_1(xy,x^2z),\;x^{-2}\psi^{-1}_2(xy,x^2z))\)
a polynomial inverse of the three-dimensional map.

For degree at most six, the exhaustive support is
\[
\begin{aligned}
f={}&1+au+bv+cu^2+duv,\\
g={}&u+pv+qu^2+ruv+su^3+tv^2+ku^2v,\\
h={}&v+Au^2+Buv+Cu^3+Dv^2+Eu^2v+Fu^4+Guv^2.
\end{aligned}
\]
When \(d\ne0\), normalize \(d=1\) and \(b\in\{0,1\}\).  Smoothness is the
nonvanishing of
\[
\Delta=1-ab+cb^2,
\]
and both ideals saturated by \(\Delta\) are unit ideals over
\(\mathbb Q\).

When \(d=0,b\ne0\), normalize \(b=1\).  The boundary lemma gives the
necessary relations among \(q,r,s,t,k\); the five resulting charts,
including the previously easy-to-miss \(c=0,k\ne0\) chart, all have unit
Gr\"obner ideals.

Finally suppose \(b=d=0\), so \(f=f(u)\), and suppose \(f\) is
nonconstant.  The support of \(g\) still allows the monomial \(tv^2\),
and we first rule it out.  Since \(f_v=0\), a multiple root of \(f\)
would be a singular point of \(C_f\), contradicting
\Cref{lem:equivariant-boundary}; so every root \(u_0\) of \(f\) (over
the algebraic closure) is simple, and the vertical line \(u=u_0\) is an
affine-line component of \(C_f\) on which \(D_f=f'(u_0)\,\partial_v\)
with \(f'(u_0)\ne0\).  There the boundary equation takes the normalized
form \(g_0h_0'-2h_0g_0'=\kappa\ne0\) of \Cref{lem:equivariant-boundary}
with \(g_0=g(u_0,\cdot)\), so \(\deg_v g(u_0,\cdot)\le1\); a nonzero
\(t\) would give \(\deg_v g(u_0,\cdot)=2\) at every root.  Hence
\(t=0\), and we may write
\[
g=n(u)+m(u)v,\qquad
h=L(u)+j(u)v+N(u)v^2,
\]
where the displayed support gives \(f(0)=1\), \(n(0)=0\), \(n'(0)=1\),
\(j(0)=1\), \(\deg N\le1\), and \(L\) without constant or linear term.
With
\[
U=fg,\qquad V=f^2h,
\]
equation \eqref{eq:equivariant-keller} becomes
\[
J(U,V)=f^2.
\]
If \(m\ne0\), eliminate \(v\) using \(v=(U/f-n)/m\).  As a polynomial
in \(U\) over \(\C(u)\), one obtains
\[
[U^2]V=\frac{N}{m^2},\qquad
[U]V=\frac{fj}{m}-\frac{2fNn}{m^2},\qquad
\left.\frac{dV}{du}\right|_U=-\frac{f}{m}.
\]
The right side is independent of \(U\), so the two displayed coefficients
are constant.

Suppose first that \(m\) is nonconstant.  The degree bounds
\(\deg N\le1\) and \(\deg m\ge1\) force the constant \(N/m^2\) to be zero.
The \(U\)-coefficient then gives \(fj=\lambda m\) for some
\(\lambda\ne0\).  If \(A_0(u)\) is the constant coefficient of \(V\) as a
polynomial in \(U\), the fixed-\(U\) derivative gives
\(A_0'=-f/m=-\lambda/j\).  Since \(A_0\) is a polynomial, \(j\) divides the
nonzero constant \(\lambda\); hence \(j\) is constant, and \(j(0)=1\) gives
\(j=1\).  Thus \(m=f/\lambda\).  Integrating the remaining constant-term
identity gives
\[
fn=u+\rho f^2L
\]
for a constant \(\rho\).  Modulo \(f\) this says \(u\equiv0\pmod f\),
which is impossible for a nonconstant \(f\) with \(f(0)=1\).

If \(m\) is a nonzero constant, then \(N/m^2\) constant makes \(N\)
constant.  The constant \(U\)-coefficient has value \(1/m\) at \(u=0\),
so
\[
f(jm-2Nn)=m.
\]
This makes the nonconstant polynomial \(f\) divide the nonzero constant
\(m\), again impossible.  Finally, if \(m=0\), direct substitution gives
\[
J(U,V)=(fn)'f^2(j+2Nv)=f^2.
\]
Thus \(N=0\) and \((fn)'j=1\).  Polynomial units are constant, and the
normalizations \(n'(0)=1\), \(f(0)=j(0)=1\) give \((fn)'=j=1\), hence
\(fn=u\), the same contradiction modulo \(f\).

Therefore \(f=1\).  The remaining plane map \(\psi=(g,h)\) has Jacobian
one and degree at most four, so it is an automorphism by the corrected
low-degree plane theorem \cite{appelgateOnishi1985,nagata1988two}.  Its
linear part is again
\(\bigl(\begin{smallmatrix}1&p\\0&1\end{smallmatrix}\bigr)\), so the same
support argument used in degree five shows that
\[
(x,y,z)\longmapsto
\left(x,\;x^{-1}\psi^{-1}_1(xy,x^2z),\;
x^{-2}\psi^{-1}_2(xy,x^2z)\right)
\]
is polynomial and is the inverse of the original threefold map.  All
normalizations used above are invertible diagonal source/target torus
changes; undoing them transports this inverse back to the original map.

The finite branches and unit-ideal certificates were generated over
\(\mathbb Q\) and rerun from the recovered exact scripts.  Finite-field
scans were useful diagnostics but are not logical inputs to the theorem.
\end{proof}

\begin{remark}[A corrected boundary warning]
The Laurent boundary equation alone does not force a monomial solution.
There are explicit nonmonomial Laurent pairs satisfying it.  The proof above
uses the complete lifted Keller identity, not that false intermediate
shortcut.
\end{remark}

\subsection{The unrestricted quartic coefficient problem}

For normalized maps \(\A^3\to\A^3\) of ordinary degree at most four, the
unrestricted collision coefficient system has \(93\) variables and \(219\)
nonconstant determinant-coefficient equations.  This count is exact, but it
does not by itself make the system tractable.

Inside the weight-\((-1,1,2)\) quartic subfamily, exact coefficient
elimination makes every Keller map tame.  The calculation is a useful
negative result for that symmetry class; it is not a classification of
unrestricted quartic Keller maps.  In particular, no lower bound for a
general counterexample follows merely from this computation.

\begin{question}[Degrees five and six]
\label{q:degree-five-six-bridge}
Can the unrestricted degree-five and degree-six collision schemes be reduced
to finitely many invariant leading-form strata with certificates comparable
to those above?  More specifically, which parts of the leading-curve,
maximal-contact, and Keller-jet analysis used in degree four persist before
the degree-seven example appears?
\end{question}
~~~

[Back to the text-source index](../../index.md)
