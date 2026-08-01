---
title: "Text proof source — 01-cubic-incidence/appendices/audit-repairs.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/01-cubic-incidence/appendices/audit-repairs.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `aa16e7adb4eb6025d2ca3c0735dcab8f64e3574fc987fa24b9e890c7bc1e8e4f` · 9,469 bytes

## Exact label anchors

<a id="label-app-audit-repairs"></a>
- `app:audit-repairs` — source line 2
<a id="label-lem-retained-infinity-gluing"></a>
- `lem:retained-infinity-gluing` — source line 14
<a id="label-eq-infinity-incidence"></a>
- `eq:infinity-incidence` — source line 44
<a id="label-eq-infinity-inverse"></a>
- `eq:infinity-inverse` — source line 57
<a id="label-prop-cubic-positive-internal"></a>
- `prop:cubic-positive-internal` — source line 109
<a id="label-prop-master-cover-cartesian"></a>
- `prop:master-cover-cartesian` — source line 180

## Complete source

~~~tex
\section{Completed arguments and corrections}
\label{app:audit-repairs}

This appendix is part of the proof record.  It supplies the scheme-theoretic
gluing omitted from \cref{thm:AB-global}, gives an internal proof of the
positive cubic case in \cref{thm:stable-uniqueness}, and replaces the proof
sketch in \cref{prop:conditional-master} by a classifying morphism and a
Cartesian pullback statement.  It also records the correction to the list of
divisorial sheet types used in earlier versions.

\subsection{The retained infinity section}

\begin{lemma}[Explicit gluing at the marked infinity section]
\label{lem:retained-infinity-gluing}
For an admissible coprime triple, the morphism
\[
\jmath\colon\A^3_{x,y,z}\longrightarrow\widetilde X,
\qquad
(x,y,z)\longmapsto
\bigl(F(x,y,z),[x:1+xy]\bigr)
\]
is an isomorphism onto
\[
\widetilde X\setminus
\left(R\cup\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}E_\beta\right).
\]
In particular, this proves the gluing assertion in
\cref{thm:AB-global}(ii), including a neighborhood of \(x=0\).
\end{lemma}

\begin{proof}
On \(x\ne0\), the marked point has affine coordinate
\[
t=\frac{T}{S}=\frac{1+xy}{x}=y+\frac1x.
\]
Multiplying \(P_{F(x,y,z)}(t)=0\) by \(x^3\) gives the homogeneous incidence
equation, so \(\jmath\) is a morphism; at \(x=0\) its marked point is
\([0:1]\).  On the finite-root chart \(S\ne0\), the inverse is exactly
\eqref{eq:reconstruction}.  It remains to check the neighborhood of the
infinity section \(E_\alpha\).

Work on the chart \(T=1\), and put \(u=S/T\).  The incidence equation is
\begin{equation}
\label{eq:infinity-incidence}
A(c)+B(c)u+bu^2-2au^3=0.
\end{equation}
Set
\[
\delta=-B(c)-2bu+6au^2.
\]
Using \eqref{eq:infinity-incidence} to eliminate \(A(c)\) gives
\[
P'(1/u)=\frac{\delta}{u}.
\]
Consequently the finite-root inverse rewrites as
\begin{equation}
\label{eq:infinity-inverse}
x=\frac{2u}{\delta},\qquad
y=\frac{2+B(c)+2bu-6au^2}{2u}.
\end{equation}
At \(E_\alpha\) one has \(u=0\), \(c=\alpha\), and
\(\delta=-B(\alpha)=2\), so \(\delta\) is a unit.  Moreover,
\eqref{eq:infinity-incidence} says
\[
A(c)=-u\bigl(B(c)+bu-2au^2\bigr).
\]
Since \(A(c)=(c-\alpha)A_\alpha(c)\) with
\(A_\alpha(\alpha)=A'(\alpha)\ne0\), it follows that
\(c-\alpha\in(u)\).  The numerator in the formula for \(y\) is therefore
divisible by \(u\), because \(B(\alpha)=-2\).  Thus both \(x\) and \(y\)
are regular near \(E_\alpha\), and \(x/u\) is a unit.

It remains only to verify regularity of
\[
z=\frac{w(x,y)-c}{x^3}.
\]
Write
\[
A_1=A'(\alpha),\qquad A_2=A''(\alpha),\qquad B_1=B'(\alpha).
\]
Expansion of \eqref{eq:infinity-incidence} modulo \(u^3\), followed by
\eqref{eq:infinity-inverse}, gives in the local ring along \(E_\alpha\)
\begin{align*}
c&\equiv \alpha+\frac{2}{A_1}u+
\left(-\frac b{A_1}-\frac{2A_2}{A_1^3}
-\frac{2B_1}{A_1^2}\right)u^2\pmod{u^3},\\
x&\equiv u+\left(b+\frac{B_1}{A_1}\right)u^2\pmod{u^3},\\
y&\equiv b+\frac{B_1}{A_1}\pmod u.
\end{align*}
Substituting these congruences into the canonical jet
\eqref{eq:w-jet} yields
\[
w(x,y)\equiv c\pmod{u^3}.
\]
Since \(x/u\) is a unit, this is equivalent to
\(w(x,y)-c\in(x^3)\), so \(z\) is regular.

The formulas above define an inverse near \(E_\alpha\), and they agree with
\eqref{eq:reconstruction} on the dense overlap \(u\ne0\).  The finite-root
chart together with this neighborhood covers the claimed open: every point
with \(S=0\) lies on some \(E_\beta\), and all such sections except
\(E_\alpha\) have been removed.  Hence \(\jmath\) is the required
isomorphism.
\end{proof}

\subsection{The positive cubic case}

\begin{proposition}[The cubic incidence open is affine three-space]
\label{prop:cubic-positive-internal}
For every tangent but nonosculating hyperplane \(H\) in the case
\(\{a,b\}=\{1,2\}\), one has
\[
U_{a,b,H}\simeq\A^3.
\]
This supplies the positive direction of \cref{thm:stable-uniqueness} without
an appeal to an unspecified public construction.
\end{proposition}

\begin{proof}
Interchanging the two factors reduces to \((a,b)=(1,2)\).  Write a binary
cubic as
\[
f=A T^3+B S T^2+C S^2T+D S^3.
\]
At the point \([S^3]\) of the rational normal cubic, the tangent line is
spanned by \(S^3,S^2T\), and the osculating plane is spanned by
\(S^3,S^2T,ST^2\).  Hence a tangent nonosculating hyperplane has equation
\[
B+\lambda A=0
\]
after scaling.  The change \(T\mapsto T+\tau S\), which fixes \([S^3]\),
replaces \(B\) by \(B+3\tau A\).  Choosing \(\tau\) appropriately sends
\(H\) to \(V(B)\).  This proves the required transitivity directly.

On the complement of \(V(B)\), a projective product cubic \([LQ]\) has a
unique scalar representative with \(B=-2\).  Thus a point of
\(U_{1,2,H}\) is equivalently a cubic
\[
cT^3-2ST^2+bS^2T-2aS^3
\]
together with a marked linear factor \(L\), such that the residual quadratic
factor \(Q\) is coprime to \(L\).  Coprimality is exactly simplicity of the
marked root.  Therefore \(U_{1,2,H}\) is the marked-simple-root incidence
open \(\widetilde X\setminus R\) for the admissible triple
\[
A(c)=c,\qquad B(c)=-2,\qquad\alpha=0.
\]
Here \(A\) has no zero other than the marked one, so there are no deleted
sections \(E_\beta\) with \(\beta\ne\alpha\).  Applying
\cref{lem:retained-infinity-gluing} gives
\[
U_{1,2,H}=\widetilde X\setminus R\simeq\A^3.
\]
\end{proof}

\subsection{The finite-flat master cover}

Let \(W=\C^2\), let \(V=\Sym^3(W^\vee)\), and let
\(V^{\mathrm{sm}}\subset V\) be the nonzero-discriminant locus.  Define
\[
\mathcal M=
\set{(L,Q)\in W^\vee\times\Sym^2(W^\vee):\Res(L,Q)=1}
\]
and
\[
m\colon\mathcal M\longrightarrow V,\qquad (L,Q)\longmapsto LQ.
\]
The full simple-root part is
\[
\mathcal M^{\mathrm{sm}}=m^{-1}(V^{\mathrm{sm}})
=\set{(L,Q)\in\mathcal M:\Disc(Q)\ne0},
\]
because
\[
\Disc(LQ)=\Res(L,Q)^2\Disc(Q)=\Disc(Q)
\]
on \(\mathcal M\).

\begin{proposition}[Classifying map and Cartesian pullback]
\label{prop:master-cover-cartesian}
Let \(F\colon\A^3\to\A^3\) be a generic-degree-three Keller map, and let
\(\pi\colon\overline X\to Y=\A^3\) be the normalization of the target in its
function field.  Assume that \(\pi\) is finite flat of degree three.  Then,
after choosing a frame of the trace-zero bundle, there is a morphism
\[
\gamma\colon Y\longrightarrow V
\]
such that, for \(Y^\circ=\gamma^{-1}(V^{\mathrm{sm}})\), the square
\[
\begin{array}{ccc}
\overline X^\circ&\longrightarrow&\mathcal M^{\mathrm{sm}}\\
\big\downarrow&&\big\downarrow m\\
Y^\circ&\xrightarrow{\ \gamma\ }&V^{\mathrm{sm}}
\end{array}
\]
is Cartesian.  In particular, \(\overline X^\circ\to Y^\circ\) is the
pullback of the universal resultant-one marked-root cover over the full
simple-root locus.  This proves the finite-cover assertion of
\cref{prop:conditional-master}; identifying the original affine source still
requires separate boundary data.
\end{proposition}

\begin{proof}
Put \(\mathcal B=\pi_*\mathcal O_{\overline X}\).  Since \(3\) is invertible,
the trace map splits the unit inclusion and gives
\[
\mathcal B\simeq\mathcal O_Y\oplus\mathcal E,
\qquad
\mathcal E=\ker(\operatorname{tr}_{\mathcal B/\mathcal O_Y}),
\]
where \(\mathcal E\) is locally free of rank two.  Every algebraic vector
bundle on affine space is trivial by the Quillen--Suslin theorem, so choose a
global frame of \(\mathcal E\).

The functorial cubic-algebra/binary-cubic correspondence over an arbitrary
base \cite{miranda1985,wood2011} associates to \(\mathcal B\), with this
frame, a binary cubic and hence the morphism \(\gamma\colon Y\to V\).  On the
nonzero-discriminant locus it identifies \(\Spec_Y\mathcal B\) with the
finite étale scheme of roots of that cubic.

It remains to identify that root scheme with \(\mathcal M^{\mathrm{sm}}\).
Let \(f\in V^{\mathrm{sm}}\), and choose one of its three projective linear
factors \([L]\).  Writing \(f=LQ\), the residual quadratic \(Q\) has two
distinct roots and is coprime to \(L\).  Replacing \((L,Q)\) by
\((sL,s^{-1}Q)\) preserves the product and changes the resultant by
\[
\Res(sL,s^{-1}Q)=s\Res(L,Q).
\]
There is therefore a unique \(s\in\C^*\) for which the resultant is one.
This construction is algebraic in families and is inverse to forgetting the
normalized factorization.  Hence
\(m\colon\mathcal M^{\mathrm{sm}}\to V^{\mathrm{sm}}\) is the universal
three-sheeted root-incidence cover, and the displayed square is Cartesian.
\end{proof}

\begin{remark}[Boundary scope]
The Cartesian square concerns the finite normalization.  It does not imply
that the original open immersion \(\A^3\hookrightarrow\overline X\) deletes
only ramification divisors: unramified sheets may also be absent over the
nonproperness boundary.  Thus the boundary-completeness qualification in
\cref{prop:conditional-master} remains necessary.
\end{remark}

\subsection{Correction to the divisorial type list}

The list in \cref{rem:lost-sheet-types} omitted the ordinary case in which
all three unramified sheets are retained.  The complete list at the geometric
generic point of a target prime divisor is
\[
U_0,\quad U_1,\quad U_2,\quad B,
\]
where \(U_i\) means trivial inertia with exactly \(i\) of the three sheets
deleted, and \(B\) means transposition inertia with the ramified point deleted
and the unramified point retained.  Outside \(S_F\) only \(U_0\) occurs; at a
prime divisor contained in \(S_F\), only \(U_1,U_2,B\) occur.  The excluded
three-cycle case remains impossible.  A proof, together with the monodromy
consequence, is given in \cref{prop:corrected-divisorial-types}.
~~~

[Back to the text-source index](../../index.md)
