---
title: "Text proof source — 01-cubic-incidence/main.tex"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/01-cubic-incidence/main.tex`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `852a6b001bf1b5c50f58b1760cecbccc9ea7ba1dd5771b13e9d1adca197dc7b0` · 36,956 bytes

## Exact label anchors

<a id="label-sec-introduction"></a>
- `sec:introduction` — source line 52
<a id="label-sec-frame"></a>
- `sec:frame` — source line 127
<a id="label-eq-frame"></a>
- `eq:frame` — source line 132
<a id="label-eq-ab-map"></a>
- `eq:ab-map` — source line 137
<a id="label-eq-inverse-cubic"></a>
- `eq:inverse-cubic` — source line 143
<a id="label-eq-root-identities"></a>
- `eq:root-identities` — source line 151
<a id="label-eq-reconstruction"></a>
- `eq:reconstruction` — source line 158
<a id="label-sec-ab-family"></a>
- `sec:AB-family` — source line 171
<a id="label-thm-pole-cancellation"></a>
- `thm:pole-cancellation` — source line 176
<a id="label-eq-admissibility"></a>
- `eq:admissibility` — source line 180
<a id="label-eq-w-jet"></a>
- `eq:w-jet` — source line 185
<a id="label-eq-b-cleared"></a>
- `eq:b-cleared` — source line 200
<a id="label-eq-a-cleared"></a>
- `eq:a-cleared` — source line 201
<a id="label-def-admissible"></a>
- `def:admissible` — source line 227
<a id="label-prop-keller-degree"></a>
- `prop:keller-degree` — source line 239
<a id="label-eq-coprime"></a>
- `eq:coprime` — source line 284
<a id="label-eq-completion"></a>
- `eq:completion` — source line 289
<a id="label-thm-ab-global"></a>
- `thm:AB-global` — source line 304
<a id="label-eq-source-open"></a>
- `eq:source-open` — source line 312
<a id="label-eq-discriminant"></a>
- `eq:discriminant` — source line 319
<a id="label-eq-nonproperness"></a>
- `eq:nonproperness` — source line 326
<a id="label-eq-omitted"></a>
- `eq:omitted` — source line 343
<a id="label-eq-disc-pullback"></a>
- `eq:disc-pullback` — source line 384
<a id="label-cor-fiber-table"></a>
- `cor:fiber-table` — source line 421
<a id="label-rem-lost-sheet-types"></a>
- `rem:lost-sheet-types` — source line 429
<a id="label-sec-equivalence"></a>
- `sec:equivalence` — source line 441
<a id="label-thm-equivalence"></a>
- `thm:equivalence` — source line 452
<a id="label-eq-eq-a"></a>
- `eq:eq-A` — source line 458
<a id="label-eq-eq-b"></a>
- `eq:eq-B` — source line 459
<a id="label-eq-eq-alpha"></a>
- `eq:eq-alpha` — source line 460
<a id="label-lem-primitive-disc"></a>
- `lem:primitive-disc` — source line 488
<a id="label-lem-nonproper-general"></a>
- `lem:nonproper-general` — source line 506
<a id="label-eq-general-nonproper"></a>
- `eq:general-nonproper` — source line 509
<a id="label-eq-c-affine"></a>
- `eq:c-affine` — source line 554
<a id="label-eq-cusp-covariant"></a>
- `eq:cusp-covariant` — source line 571
<a id="label-eq-cusp-scaling"></a>
- `eq:cusp-scaling` — source line 579
<a id="label-eq-target-c"></a>
- `eq:target-c` — source line 641
<a id="label-eq-target-b"></a>
- `eq:target-b` — source line 642
<a id="label-eq-target-a"></a>
- `eq:target-a` — source line 645
<a id="label-eq-cubic-transform"></a>
- `eq:cubic-transform` — source line 649
<a id="label-eq-source-transform"></a>
- `eq:source-transform` — source line 656
<a id="label-cor-moduli-data"></a>
- `cor:moduli-data` — source line 697
<a id="label-sec-stable-uniqueness"></a>
- `sec:stable-uniqueness` — source line 714
<a id="label-eq-tangent-functional"></a>
- `eq:tangent-functional` — source line 734
<a id="label-eq-uab"></a>
- `eq:Uab` — source line 739
<a id="label-thm-stable-uniqueness"></a>
- `thm:stable-uniqueness` — source line 746
<a id="label-eq-class-group"></a>
- `eq:class-group` — source line 776
<a id="label-eq-coprime-class"></a>
- `eq:coprime-class` — source line 810
<a id="label-eq-dh-class"></a>
- `eq:DH-class` — source line 829
<a id="label-eq-ztilde"></a>
- `eq:Ztilde` — source line 849
<a id="label-eq-z-class"></a>
- `eq:Z-class` — source line 883
<a id="label-eq-deficit"></a>
- `eq:deficit` — source line 893
<a id="label-sec-universal"></a>
- `sec:universal` — source line 926
<a id="label-prop-conditional-master"></a>
- `prop:conditional-master` — source line 943
<a id="label-q-flatness"></a>
- `q:flatness` — source line 963
<a id="label-q-boundary-torelli"></a>
- `q:boundary-torelli` — source line 976
<a id="label-sec-computation"></a>
- `sec:computation` — source line 990

## Complete source

~~~tex
\documentclass[11pt,reqno]{amsart}
\input{../common/preamble}

\title[Cubic marked-root covers]{Cubic Marked-Root Covers:\\
Normal Forms, Equivalence, and Stable Uniqueness}
\author{Nathaniel Monson}
\date{July 22, 2026}

\begin{document}

\begin{abstract}
The recent counterexample to the Jacobian conjecture is governed by a binary
cubic together with a marked simple root.  We study two classification
questions suggested by that description.

First, we classify a normalized determinant-neutral family in which the
inverse cubic has the form
\[
 A(c)T^3+B(c)T^2+bT-2a.
\]
Polynomiality is equivalent to a finite set of jet conditions at a
distinguished simple zero of \(A\).  When \(A\) and \(B\) are coprime, the
projective root-incidence completion is a smooth finite flat cubic cover, and
we determine its boundary, discriminant, nonproperness set, omitted locus, and
fiber stratification.  Without a squarefreeness or coprimality hypothesis, we
classify the resulting maps up to arbitrary polynomial left--right
equivalence: the invariant is an affine orbit of the divisor of \(A\), its
marked simple point, and the residue class of \(B\) modulo \(A\).
The coordinate frame is governed by a universal root--slope identity: the
root-forgetting Jacobian is \(P'(t)/2\), while the affine chart contributes
its reciprocal.  This gives generic \(S_3\) monodromy and a product
description of the principal discriminant complement.

Second, we consider the larger binary multiplication-incidence construction
obtained from
\(\PP(V_a)\times\PP(V_b)\to\PP(V_{a+b})\).  After removing the resultant and
the pullback of any tangent but nonosculating hyperplane, the resulting open
is stably affine space only in the cubic case
\(\{a,b\}=\{1,2\}\).  The obstruction combines the public class-group
reduction to adjacent degrees with a codimension-two Hodge--Deligne deficit.
\end{abstract}

\maketitle

\begin{center}
\small\emph{Working manuscript.  The computer checks described in
\cref{sec:computation} are exact, but they do not replace independent review
of the geometric arguments.}
\end{center}

\section{Introduction}
\label{sec:introduction}

A polynomial map \(F\colon\C^n\to\C^n\) is a \emph{Keller map} if its
Jacobian determinant is a nonzero constant.  The Jacobian conjecture asserted
that every Keller map is a polynomial automorphism.  The explicit
three-dimensional counterexample disproved the conjecture in dimensions at
least three.

\emph{Discovery attribution.}  We credit Akhil Mathew as the primary human
source of the problem: Mathew prompted Levent Alp\"oge, Alp\"oge prompted
Fable, Fable produced the example, and Alp\"oge announced it publicly
\cite{ulam2026counterexample,alpoge2026announcement}.

The feature relevant here is not the original coordinate formula but its
root-incidence geometry.  The public projective formulation due to Jiang
\cite{jiang2026markedroot} regards a source point as a binary cubic together
with a marked simple root; the map forgets the mark.  Lou gave a
resultant-normalized affine chart \cite{lou2026derivation}, and Litt described
the source through affine-line bundles and pencils \cite{litt2026bundle}.
Speyer's discussion \cite{speyer2026seminar}, Tao's exposition
\cite{tao2026digestion}, and Naskr\k ecki's audit
\cite{naskrecki2026audit} contain further covering, boundary, and orbit
interpretations.

Our first question is what remains after fixing the determinant-neutral
coordinates but allowing the cubic coefficients to vary with one target
coordinate.  This produces the normalized \(A,B\) family of
\cref{sec:AB-family}.  Pole cancellation is rigid enough to classify every
member of the family, while flexible enough to retain arbitrarily complicated
one-variable data.  The main results are the global description in the
coprime case, \cref{thm:AB-global}, and the unrestricted left--right
classification, \cref{thm:equivalence}.

Our second question is whether the cubic marked-root construction is one
member of a higher binary multiplication family with affine-space source.
The class-group obstruction in this direction was already observed publicly
by Skooi and Shubhodip Mondal; Mondal also reported the first
\((a,b)=(2,3)\) point-count failure in the Secret Blogging Seminar discussion
\cite{speyer2026seminar}.  We take that reduction as the starting point.
\Cref{thm:stable-uniqueness} proves that every adjacent higher pair has a
universal codimension-two Hodge--Deligne deficit.  Thus the cubic is the
unique stably affine case throughout the two-block construction.

\subsection*{Novelty boundary}

We do not claim the counterexample, its marked-root interpretation, the
resultant chart, the basic \(3/1/0\) fiber count, or the initial class-group
obstruction.  Our candidate contributions are:

\begin{enumerate}[label=(\roman*)]
\item the complete pole-cancellation and coprime global-geometry theorem for
the normalized \(A,B\) family;
\item the all-multiplicity left--right classification in that family; and
\item the codimension-two argument proving stable uniqueness in the full
two-block incidence family.
\end{enumerate}

For orientation we also record the root--slope identity, generic monodromy,
and discriminant-complement geometry of the normalized frame.  These organize
the classification but are not used to enlarge the novelty claim.

The first two results concern a deliberately restricted normal form; they do
not classify arbitrary degree-three Keller maps.  The last result concerns a
specific binary multiplication construction; it is not a universality
theorem for counterexamples.

\subsection*{Conventions}

We work over \(\C\).  Varieties are reduced and separated.  We write
\(\Lef=[\A^1]\) in the Grothendieck ring
\(K_0(\operatorname{Var}_{\C})\), and \(F_dK_0\) for the subgroup generated
by varieties of dimension at most \(d\).  Compactly supported
Hodge--Deligne polynomials are denoted by \(\cE(-;u,v)\).

\section{The marked-root coordinate frame}
\label{sec:frame}

Let \(A,B\in\C[c]\), with \(A\ne0\), and initially work on the chart
\(x\ne0\).  Put
\begin{equation}
\label{eq:frame}
t=y+\frac1x,\qquad r=\frac2x,\qquad c=w(x,y)-x^3z,
\end{equation}
where \(w\in\C[x,y]\).  Define
\begin{equation}
\label{eq:ab-map}
b=r-3A(c)t^2-2B(c)t,\qquad
2a=\frac{2t}{x}-2A(c)t^3-B(c)t^2.
\end{equation}
The associated inverse polynomial is
\begin{equation}
\label{eq:inverse-cubic}
P_{a,b,c}(T)=A(c)T^3+B(c)T^2+bT-2a.
\end{equation}
Whenever \((a,b,c)\) extends polynomially across \(x=0\), we denote the
resulting map by \(F\colon\A^3_{x,y,z}\to\A^3_{a,b,c}\).

The coordinates are designed so that
\begin{equation}
\label{eq:root-identities}
P_{F(x,y,z)}(t)=0,\qquad
P'_{F(x,y,z)}(t)=\frac2x
\end{equation}
on \(x\ne0\).  Consequently each finite simple root \(t\) reconstructs a
source point by
\begin{equation}
\label{eq:reconstruction}
x=\frac2{P'(t)},\qquad
y=t-\frac{P'(t)}2,\qquad
z=\frac{w(x,y)-c}{x^3}.
\end{equation}

Terms in the inverse polynomial of degrees at most one in \(T\) introduce no
new geometry here: a term \(C(c)T+D(c)\) is removed by a triangular target
automorphism.  Likewise, replacing \(w\) by \(w+x^3u(x,y)\) is the source
shear \(z\mapsto z-u(x,y)\).

\section{Classification and geometry of the
\texorpdfstring{\(A,B\)}{A,B} family}
\label{sec:AB-family}

\subsection{Pole cancellation}

\begin{theorem}[Pole-cancellation theorem]
\label{thm:pole-cancellation}
Let \(A\ne0\).  The rational expressions in \eqref{eq:ab-map} are
polynomials if and only if there is \(\alpha\in\C\) such that
\begin{equation}
\label{eq:admissibility}
A(\alpha)=0,\qquad A'(\alpha)\ne0,\qquad B(\alpha)=-2,
\end{equation}
and, modulo \(x^3\C[x,y]\),
\begin{equation}
\label{eq:w-jet}
w(x,y)\equiv
\alpha+\frac{2}{A'(\alpha)}x
+x^2\left(
-\frac{3}{A'(\alpha)}y
-\frac{2A''(\alpha)}{A'(\alpha)^3}
-\frac{B'(\alpha)}{A'(\alpha)^2}
\right).
\end{equation}
The \(x^3\)-remainder is removed by a source shear.
\end{theorem}

\begin{proof}
Write \(q=1+xy\).  Clearing the possible poles gives
\begin{align}
x^2b&=2x-3A(c)q^2-2xB(c)q,\label{eq:b-cleared}\\
2x^3a&=2xq-2A(c)q^3-xB(c)q^2.\label{eq:a-cleared}
\end{align}
Polynomiality first gives \(A(w(0,y))=0\).  Since \(A\) has finitely many
roots, \(w(0,y)\) is constant; call it \(\alpha\).  Write
\[
w=\alpha+xp(y)+x^2s(y)+O(x^3),
\]
and abbreviate \(A_i=A^{(i)}(\alpha)\), \(B_i=B^{(i)}(\alpha)\).
The coefficients of \(x\) in \eqref{eq:b-cleared} and
\eqref{eq:a-cleared} are respectively
\[
2-3A_1p-2B_0,\qquad 2-2A_1p-B_0.
\]
Their vanishing gives \(A_1p=2\) and \(B_0=-2\).  In particular
\(A_1\ne0\) and \(p=2/A_1\) is constant.  The coefficient of \(x^2\) in
\eqref{eq:a-cleared} then gives
\[
s(y)=-\frac3{A_1}y-\frac{2A_2}{A_1^3}-\frac{B_1}{A_1^2}.
\]
These conditions are also sufficient: substitution makes the right sides of
\eqref{eq:b-cleared} and \eqref{eq:a-cleared} divisible by \(x^2\) and
\(x^3\), respectively.  Finally, an \(x^3u(x,y)\) term in \(w\) is absorbed
by the stated source shear.
\end{proof}

\begin{definition}
\label{def:admissible}
An \emph{admissible triple} is
\[
(A,B,\alpha),\qquad
A,B\in\C[c],\quad A\ne0,
\]
satisfying \eqref{eq:admissibility}.  We use the representative
\(w=w_{A,B,\alpha}\) displayed in \eqref{eq:w-jet}, with no \(x^3\)
remainder, and write \(F_{A,B,\alpha}\) for the resulting polynomial map.
\end{definition}

\begin{proposition}
\label{prop:keller-degree}
Every admissible triple defines a Keller map with
\[
\det D F_{A,B,\alpha}=-2.
\]
Its generic degree is three.  The source plane \(x=0\) maps isomorphically
onto the target plane \(c=\alpha\).
\end{proposition}

\begin{proof}
On \(x\ne0\), direct differentiation gives
\[
\det\frac{\partial(a,b,c)}{\partial(t,r,c)}=\frac r2,
\qquad
\det\frac{\partial(t,r,c)}{\partial(x,y,z)}=-2x.
\]
Since \(r=2/x\), their product is \(-2\), and polynomiality extends the
identity to all of \(\A^3\).

For a general target point, \eqref{eq:inverse-cubic} has three finite simple
roots, and \eqref{eq:reconstruction} gives three distinct source points.
Thus the generic degree is three.

For completeness, restriction of the canonical representative to \(x=0\)
gives
\[
b=y-\frac{B'(\alpha)}{A'(\alpha)}
\]
and
\[
a=A'(\alpha)z+4y^2+
\left(
\frac{5B'(\alpha)}{2A'(\alpha)}
+\frac{6A''(\alpha)}{A'(\alpha)^2}
\right)y+\kappa,
\]
where \(\kappa\in\C\) depends only on the first three derivatives of \(A\)
and the first two derivatives of \(B\) at \(\alpha\).  This is a triangular
polynomial isomorphism from \(\A^2_{y,z}\) to \(\A^2_{a,b}\).
\end{proof}

\subsection{The coprime completion}

Assume for the remainder of this subsection that
\begin{equation}
\label{eq:coprime}
\gcd(A,B)=1.
\end{equation}
Let
\begin{equation}
\label{eq:completion}
\widetilde X=
V\left(
A(c)T^3+B(c)ST^2+bS^2T-2aS^3
\right)
\subset
\A^3_{a,b,c}\times\PP^1_{[S:T]}.
\end{equation}
For a distinct zero \(\beta\) of \(A\), let
\[
E_\beta=\set{c=\beta,\ [S:T]=[0:1]}\simeq\A^2.
\]
Let \(R\) be the repeated-root divisor in \(\widetilde X\).

\begin{theorem}[Global geometry of the coprime family]
\label{thm:AB-global}
For an admissible triple satisfying \eqref{eq:coprime}:

\begin{enumerate}[label=(\roman*)]
\item the total space \(\widetilde X\) is smooth, and the projection
\(\pi\colon\widetilde X\to\A^3_{a,b,c}\) is finite flat of degree three;
\item there is an isomorphism
\begin{equation}
\label{eq:source-open}
\A^3_{x,y,z}\simeq
\widetilde X\setminus
\left(R\cup\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}E_\beta\right);
\end{equation}
\item the branch discriminant is
\begin{equation}
\label{eq:discriminant}
\mathcal D=
B(c)^2b^2-4A(c)b^3+8aB(c)^3
-36aA(c)B(c)b-108a^2A(c)^2;
\end{equation}
\item the nonproperness set is
\begin{equation}
\label{eq:nonproperness}
S_F=V(\mathcal D)\cup
\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}V(c-\beta);
\end{equation}
\item if
\[
T_3=
V\left(3A(c)b-B(c)^2,\,
54A(c)^2a+B(c)^3\right)
\]
and
\[
C_\beta=
V\left(c-\beta,\ b^2+8aB(\beta)\right),
\]
then
\begin{equation}
\label{eq:omitted}
\A^3\setminus F(\A^3)=
T_3\cup\bigcup_{\beta\ne\alpha}C_\beta
=\Sing(S_F)_{\mathrm{red}}.
\end{equation}
\end{enumerate}
\end{theorem}

\begin{proof}
The equation in \eqref{eq:completion} is a nonzero binary cubic on every
geometric target fiber: at a common zero of \(A\) and \(B\) this could fail,
but \eqref{eq:coprime} excludes such a point.  It therefore defines a
relative effective Cartier divisor of degree three in the trivial
\(\PP^1\)-bundle.  The divisor is proper with zero-dimensional fibers and
hence finite; the constant relative Hilbert polynomial makes it flat of
degree three.

The total space is smooth.  On \(S\ne0\), the partial derivative with
respect to \(a\) is \(-2S^3\).  If \(S=0\), then \(T\ne0\), \(A(c)=0\),
and \(B(c)\ne0\); the partial derivative with respect to \(S\) is
\(B(c)T^2\).

On the chart of finite simple roots, \eqref{eq:reconstruction} identifies
the incidence with the source.  The root at infinity over \(c=\alpha\) is
also simple because \(B(\alpha)=-2\), and
\cref{prop:keller-degree} identifies it with the plane \(x=0\).  At every
other zero \(\beta\) of \(A\), the simple infinity section \(E_\beta\) has
no affine source point.  The explicit inverse and its regular gluing along
the retained infinity section are proved in
\cref{lem:retained-infinity-gluing}; removing the other sections and the
repeated-root divisor gives \eqref{eq:source-open}.

The discriminant of \eqref{eq:inverse-cubic} is
\eqref{eq:discriminant}.  On the chosen-root incidence chart, put
\[
r=P'(t),\qquad
b=r-3A(c)t^2-2B(c)t,\qquad
a=-A(c)t^3-\frac12B(c)t^2+\frac12rt.
\]
Then
\begin{equation}
\label{eq:disc-pullback}
\pi^*\mathcal D
=r^2\left((3A(c)t+B(c))^2-4A(c)r\right).
\end{equation}
Thus \(R=\{r=0\}\simeq\A^2_{t,c}\), and its image is the branch
hypersurface \(V(\mathcal D)\).  Each deleted \(E_\beta\) maps
isomorphically to the plane \(c=\beta\), giving
\eqref{eq:nonproperness}.

A cubic on the branch hypersurface has one double and one simple root away
from \(T_3\); the double root lies in \(R\), while the simple root remains.
At \(T_3\) all three roots coincide and none remains in
\eqref{eq:source-open}.  On \(c=\beta\ne\alpha\), the infinity root is
deleted.  The remaining quadratic has a double root precisely on
\[
b^2+8aB(\beta)=0,
\]
because
\[
\mathcal D|_{c=\beta}
=B(\beta)^2\bigl(b^2+8aB(\beta)\bigr).
\]
This proves the first equality in \eqref{eq:omitted}.

Where \(A(c)\ne0\), depressing the cubic identifies its branch equation
transversely with a cusp; its singular locus is \(T_3\).  Along
\(c=\beta\), the branch hypersurface is smooth because
\[
\left.\frac{\partial\mathcal D}{\partial a}\right|_{A=0}
=8B(\beta)^3\ne0,
\]
and it meets the plane \(c=\beta\) transversely exactly along \(C_\beta\).
The reduced singular locus of the union \eqref{eq:nonproperness} is
therefore the right side of \eqref{eq:omitted}.
\end{proof}

\begin{corollary}[Fiber table]
\label{cor:fiber-table}
The affine fiber size is three off \(S_F\), one on
\(V(\mathcal D)\setminus(T_3\cup\bigcup C_\beta)\), two on a deleted
plane away from \(V(\mathcal D)\), and zero on \(T_3\) and on every
\(C_\beta\).
\end{corollary}

\begin{remark}
\label{rem:lost-sheet-types}
The generic local behavior of an arbitrary cubic normalization is more
finely divided than the slogan ``ramified, unramified, or boundary.''  Relative
to the finite completion, the generic divisor types are \(U_0,U_1,U_2,B\):
three unramified sheets with respectively zero, one, or two deleted, or a
\(2+1\) ramified fiber with the ramified point deleted and the unramified
point retained.  A generic three-cycle is excluded.  The proof and scope of
this divisorial classification are given in
\cref{prop:corrected-divisorial-types}.
\end{remark}

\section{Polynomial left--right equivalence}
\label{sec:equivalence}

We now drop the coprimality and squarefreeness assumptions.  Two maps
\(F_i\colon\A^3\to\A^3\) are \emph{left--right equivalent} if there are
polynomial automorphisms \(\Phi\) of the source and \(\Psi\) of the target
such that
\[
F_2\circ\Phi=\Psi\circ F_1.
\]

\begin{theorem}[All-multiplicity equivalence criterion]
\label{thm:equivalence}
Let \((A_i,B_i,\alpha_i)\) be admissible triples.  Then
\(F_{A_1,B_1,\alpha_1}\) and \(F_{A_2,B_2,\alpha_2}\) are polynomially
left--right equivalent if and only if there are an affine map
\(\phi(c)=uc+v\), \(u\ne0\), and a scalar \(\kappa\in\C^*\) such that
\begin{align}
A_2(\phi(c))&=\kappa A_1(c),\label{eq:eq-A}\\
B_2(\phi(c))&\equiv B_1(c)\pmod{A_1(c)},\label{eq:eq-B}\\
\phi(\alpha_1)&=\alpha_2.\label{eq:eq-alpha}
\end{align}
No squarefreeness hypothesis is required.

When \(A_1\) has at least two distinct roots, every equivalence induces the
root-affine data above.  When \(A_1\) is linear, all members lie in one
equivalence class; we do not assert that the construction below describes
the full self-equivalence group of that class.
\end{theorem}

\subsection{The reduced nonproperness divisor}

Let
\[
\Delta=B^2b^2-4Ab^3+8aB^3-36aABb-108a^2A^2.
\]
Regard \(\Delta\) as a polynomial in \(a,b\) over \(\C[c]\).  Let \(g(c)\)
be the gcd of its coefficients and put
\[
\Delta_{\mathrm{prim}}=\Delta/g(c).
\]
At a zero \(\beta\) of \(A\), if
\(m_\beta=\ord_\beta A\) and \(n_\beta=\ord_\beta B\), then
\[
\ord_\beta g=\min(m_\beta,2n_\beta).
\]

\begin{lemma}
\label{lem:primitive-disc}
The polynomial \(\Delta_{\mathrm{prim}}\) is irreducible in
\(\C[a,b,c]\).
\end{lemma}

\begin{proof}
Over \(\C(b,c)\), the discriminant is quadratic in \(a\), and the
discriminant of that quadratic is
\[
-64\bigl(3A(c)b-B(c)^2\bigr)^3.
\]
The factor \(3Ab-B^2\) has a simple zero as a rational function of \(b\),
so it is not a square in \(\C(b,c)\).  The quadratic is irreducible over
that field.  Dividing by coefficient content and applying Gauss's lemma
proves the assertion.
\end{proof}

\begin{lemma}
\label{lem:nonproper-general}
As a reduced set,
\begin{equation}
\label{eq:general-nonproper}
S_F=V(\Delta_{\mathrm{prim}})
\cup\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}V(c-\beta).
\end{equation}
The first component is the unique nonplane irreducible component.
\end{lemma}

\begin{proof}
At a general point of \(V(\Delta_{\mathrm{prim}})\) with \(A(c)\ne0\),
the inverse cubic has one double finite root.  Splitting that root makes
\(P'(t)\to0\), so \(x=2/P'(t)\to\infty\).  Thus a dense open subset of
the irreducible hypersurface is nonproper, and closedness of the
nonproperness set gives the entire component.

If \(A(\beta)=0\) with \(\beta\ne\alpha\), then the limiting degree drops
by one when \(B(\beta)\ne0\), and by two when \(B(\beta)=0\).  The lost
roots tend to infinity.  Their source reconstructions cannot remain bounded:
otherwise \(t\to\infty\) would force \(x\to0\), and
\(c=w(x,y)-x^3z\) would tend to the distinguished value \(\alpha\), contrary
to \(\beta\ne\alpha\).  Hence every indicated plane is a nonproperness
component.

Conversely, away from the displayed set, all roots are finite and simple,
and \eqref{eq:reconstruction} is regular.  At \(c=\alpha\), the projective
infinity root is simple and retained by the plane \(x=0\), so the same
conclusion holds.

Finally, over \(\C(c)\) the primitive discriminant is a cusp in affine
coordinates, hence singular.  The remaining components in
\eqref{eq:general-nonproper} are smooth planes.  This proves uniqueness.
\end{proof}

\subsection{Necessity}

\begin{proof}[Proof of necessity in \cref{thm:equivalence}]
Suppose
\[
F_2\circ\Phi=\Psi\circ F_1.
\]
Polynomial automorphisms preserve nonproperness sets.  Assume first that
\(A_1\) has at least two distinct roots.  By
\cref{lem:nonproper-general}, a plane component cannot map to the singular
primitive-discriminant component.  The pullback of the prime ideal of a
target plane is therefore the prime ideal of a source plane, giving
\begin{equation}
\label{eq:c-affine}
c_2\circ\Psi=uc+v=\phi(c),\qquad u\ne0.
\end{equation}

Put \(K=\C(c)\),
\[
\widetilde A_2=A_2(\phi(c)),\qquad
\widetilde B_2=B_2(\phi(c)),
\]
and define the cubic covariants
\[
p_i=3A_i b_i-B_i^2,\qquad
Q_i=2B_i^3-9A_iB_i b_i-54A_i^2a_i.
\]
The affine change \((a_i,b_i)\leftrightarrow(p_i,Q_i)\) has determinant
\(162A_i^3\) over \(K\), and
\begin{equation}
\label{eq:cusp-covariant}
Q_i^2+4p_i^3=-27A_i^2\Delta_i.
\end{equation}
Thus the generic nonplane component is the monomial cusp
\(Q^2+4p^3=0\).  By the classification of plane automorphisms preserving
a monomial cusp \cite[Theorem~2(ii)]{blancStampfli2015}, applied over the
perfect field \(K\), there is \(\rho\in K^*\) such that
\begin{equation}
\label{eq:cusp-scaling}
p_2\circ\Psi=\rho^2p_1,\qquad
Q_2\circ\Psi=\rho^3Q_1.
\end{equation}

Write \(\widehat a=\Psi^*(a_2)\) and
\(\widehat b=\Psi^*(b_2)\).  Comparing coefficients in
\eqref{eq:cusp-scaling} gives
\[
\widehat b=\lambda_b(c)b+f(c),\qquad
\lambda_b=\frac{\rho^2A_1}{\widetilde A_2},
\]
and
\[
\widehat a=\lambda_a(c)a+g(c)b+h(c),\qquad
\lambda_a=\frac{\rho^3A_1^2}{\widetilde A_2^2}.
\]
Polynomiality puts the displayed coefficients in \(\C[c]\).  Since
\[
\det D\Psi=u\lambda_a\lambda_b\in\C^*,
\]
both \(\lambda_a\) and \(\lambda_b\) are constants.  It follows that
\(\rho=\lambda_b^2/\lambda_a\in\C^*\) and that
\(\widetilde A_2/A_1=\kappa\in\C^*\), proving
\eqref{eq:eq-A} with multiplicities.

The plane components are indexed by all distinct zeros of \(A_i\) except
the marked zero.  Their permutation under \(\phi\), together with
\eqref{eq:eq-A}, identifies the omitted root and proves
\eqref{eq:eq-alpha}.  On the marked plane one has identically
\[
p_i=-4,\qquad Q_i=-16.
\]
Specializing \eqref{eq:cusp-scaling} gives
\(\rho^2=\rho^3=1\), hence \(\rho=1\).  Solving the first relation in
\eqref{eq:cusp-scaling} for \(\widehat b\), and the second for
\(\widehat a\), shows that the coefficient of \(b\) in
\(\widehat a\) is
\[
\frac{B_1-\widetilde B_2}{6\kappa^2A_1}.
\]
Its polynomiality gives \(A_1\mid B_1-\widetilde B_2\), which is
\eqref{eq:eq-B}, including the residue jets at repeated roots.

If \(A_1\) is linear, \eqref{eq:general-nonproper} has no plane component;
the same is true of \(A_2\).  An affine \(\phi\) matches the marked roots
and gives \eqref{eq:eq-A}; \eqref{eq:eq-B} follows from
\(B_i(\alpha_i)=-2\).
\end{proof}

\subsection{Sufficiency and an explicit lift}

\begin{proof}[Proof of sufficiency in \cref{thm:equivalence}]
Assume \eqref{eq:eq-A}--\eqref{eq:eq-alpha}.  Put
\[
\lambda=\kappa^{-1},\qquad
q(c)=
\frac{\lambda\bigl(B_1(c)-B_2(\phi(c))\bigr)}{3A_1(c)}
\in\C[c].
\]
Define the triangular target automorphism
\begin{align}
c_2&=\phi(c),\label{eq:target-c}\\
b_2&=\lambda b+\frac{3A_1q^2}{\lambda}-2B_1q,\label{eq:target-b}\\
a_2&=\lambda^2a+\frac{\lambda q}{2}b
+\frac{A_1q^3}{2\lambda}-\frac{B_1q^2}{2}.
\label{eq:target-a}
\end{align}
Direct coefficient comparison gives
\begin{equation}
\label{eq:cubic-transform}
P_2(\lambda T+q;\,a_2,b_2,\phi(c))
=\lambda^2P_1(T;\,a,b,c).
\end{equation}

Let \(w_i=w_{A_i,B_i,\alpha_i}\) and define
\begin{equation}
\label{eq:source-transform}
X=\frac{x}{\lambda},\qquad
Y=\lambda y+q(c),\qquad
Z=\frac{\lambda^3}{x^3}
\left(w_2(X,Y)-\phi(c)\right).
\end{equation}
This is polynomial.  Indeed, if \(q_0=q(\alpha_1)\), differentiating
\eqref{eq:eq-A} and
\[
B_2(\phi(c))=B_1(c)-\frac{3A_1(c)q(c)}{\lambda}
\]
at \(c=\alpha_1\) gives the two-jet identity
\[
w_2\left(\frac{x}{\lambda},\lambda y+q_0\right)
=\phi(w_1(x,y)).
\]
Moreover \(c-\alpha_1\in(x)\), so \(q(c)-q_0\in(x)\); the variable \(Y\)
occurs in \(w_2\) multiplied by \(X^2\), and replacing \(q_0\) by \(q(c)\)
therefore changes the left side by a multiple of \(x^3\).  Finally
\(w_1-c=x^3z\), proving divisibility of the numerator in
\eqref{eq:source-transform}.

The same construction with
\[
\phi^{-1},\qquad \lambda^{-1},\qquad
q_{\mathrm{inv}}(c_2)
=-\lambda^{-1}q(\phi^{-1}(c_2))
\]
is a polynomial inverse.  Thus \eqref{eq:source-transform} is a source
automorphism.  Since
\[
Y+\frac1X=\lambda\left(y+\frac1x\right)+q(c),
\]
\eqref{eq:cubic-transform} and its derivative give
\[
F_2(X,Y,Z)=\Psi(F_1(x,y,z))
\]
on \(x\ne0\), hence everywhere.
\end{proof}

\begin{corollary}
\label{cor:moduli-data}
The equivalence classes are the
\(\operatorname{Aff}_1(\C)\)-orbits of triples
\[
(D,\alpha,\overline B),
\]
where \(D=\operatorname{div}(A)\) is an effective divisor on \(\A^1\),
\(\alpha\) is a marked multiplicity-one point of \(D\), and
\[
\overline B\in\C[c]/(A),\qquad \overline B(\alpha)=-2.
\]
For degree \(d\) in a multiplicity stratum with \(r\ge2\) distinct roots,
the generic dimension is \(d+r-3\); in the squarefree stratum it is
\(2d-3\).
\end{corollary}

\section{Stable uniqueness in the two-block incidence family}
\label{sec:stable-uniqueness}

Let
\[
V_d=H^0(\PP^1,\mathcal O(d))
\]
and consider multiplication of binary forms
\[
\mu_{a,b}\colon
\PP(V_a)\times\PP(V_b)\longrightarrow\PP(V_{a+b}),
\qquad ([f],[g])\longmapsto[fg].
\]
Let \(R_{a,b}\) be the resultant divisor.  Fix the point
\([Y^{a+b}]\) on the rational normal curve, and let \(H\) be any hyperplane
tangent but not osculating there.  In coefficient coordinates
\[
h=\sum_{i=0}^{a+b}h_iX^iY^{a+b-i},
\]
its functional can be normalized to
\begin{equation}
\label{eq:tangent-functional}
\lambda(h)=h_2+\lambda_3h_3+\cdots+\lambda_{a+b}h_{a+b}.
\end{equation}
Define
\begin{equation}
\label{eq:Uab}
U_{a,b,H}=
\bigl(\PP(V_a)\times\PP(V_b)\bigr)
\setminus\left(R_{a,b}\cup\mu_{a,b}^{-1}(H)\right).
\end{equation}

\begin{theorem}[Stable uniqueness]
\label{thm:stable-uniqueness}
Let \(a,b\ge1\) and \(a+b\ge3\).  For every hyperplane \(H\) tangent but
not osculating at the chosen point,
\[
U_{a,b,H}\simeq\A^{a+b}
\quad\Longleftrightarrow\quad
\{a,b\}=\{1,2\}.
\]
More strongly, outside the cubic case,
\[
U_{a,b,H}\times\A^r
\not\simeq\A^{a+b+r}
\qquad\text{for every }r\ge0.
\]
\end{theorem}

\subsection{The class-group reduction}

Put \(D_H=\mu_{a,b}^{-1}(H)\).  The matrix of the bilinear form
\((f,g)\mapsto\lambda(fg)\) has rank at least two, so \(D_H\) is
irreducible.  The two removed prime divisors have classes
\[
[R_{a,b}]=(b,a),\qquad [D_H]=(1,1)
\]
in
\[
\Cl(\PP^a\times\PP^b)=\mathbb Z^2.
\]
Divisor localization gives
\begin{equation}
\label{eq:class-group}
\Cl(U_{a,b,H})
\simeq\mathbb Z^2/\angles{(b,a),(1,1)}.
\end{equation}
Thus a trivial class group forces \(\abs{a-b}=1\).  Since the class group
of these smooth varieties is unchanged by adjoining polynomial variables,
\eqref{eq:class-group} also obstructs stable affine space unless the degrees
are adjacent.

It remains to take \(b=a+1\), \(a\ge2\), and put
\[
n=2a+1,\qquad
X=\PP^a\times\PP^{a+1},\qquad
C=X\setminus R_{a,a+1}.
\]
Here we have interchanged the two factors if necessary.

\subsection{The coprime-pair locus}

Write
\[
P_m=[\PP^m]=1+\Lef+\cdots+\Lef^m.
\]
Stratifying pairs of effective divisors on \(\PP^1\) by the degree of their
gcd gives motivic M\"obius inversion.  Since
\[
\sum_{d\ge0}P_dT^d=\frac1{(1-T)(1-\Lef T)},
\]
we obtain
\begin{align}
[C]
&=P_aP_{a+1}-(1+\Lef)P_{a-1}P_a
+\Lef P_{a-2}P_{a-1}\notag\\
&=\Lef^n+\Lef^{n-1}.
\label{eq:coprime-class}
\end{align}

\subsection{The hyperplane divisor}

Let \(r\) be the rank of the matrix of
\((f,g)\mapsto\lambda(fg)\).  It contains the minor
\[
\begin{pmatrix}
0&0&1\\
0&1&\lambda_3\\
1&\lambda_3&\lambda_4
\end{pmatrix},
\qquad\det=-1,
\]
so \(r\ge3\).  Projecting \(D_H\) to \(\PP^a\), its fiber is \(\PP^a\)
away from the left radical and \(\PP^{a+1}\) on the radical
\(\PP^{a-r}\).  Therefore
\begin{equation}
\label{eq:DH-class}
[D_H]=P_a^2+\Lef^{a+1}P_{a-r}
\equiv
\Lef^{n-1}+2\Lef^{n-2}
\pmod{F_{n-3}K_0}.
\end{equation}
We use the convention \(P_m=0\) for \(m<0\).

\subsection{The codimension-two intersection}

Resolve the resultant by marking a common linear factor:
\[
\widetilde R=
\PP^1\times\PP^{a-1}\times\PP^a
\longrightarrow R_{a,a+1},
\qquad
(\ell,[f_1],[g_1])\longmapsto([\ell f_1],[\ell g_1]).
\]
The inverse image of \(D_H\) is
\begin{equation}
\label{eq:Ztilde}
\widetilde Z=
\set{\lambda(\ell^2f_1g_1)=0}.
\end{equation}
At \(\ell=Y\), the residual bilinear matrix contains
\[
\begin{pmatrix}0&1\\1&\lambda_3\end{pmatrix},
\]
so its generic rank is at least two and its generic defining polynomial is
irreducible.

There are no vertical components.  Write \(\ell=vY+uX\).  The coefficients
of the restricted functional are
\[
\rho_j=v^2\lambda_j+2uv\lambda_{j+1}+u^2\lambda_{j+2}.
\]
If all \(\rho_j\) vanished, then
\(\rho_0=u^2\lambda_2=0\) would give \(u=0\), while
\(\rho_2=v^2\lambda_2\ne0\), a contradiction.  Gauss's lemma therefore
shows that \(\widetilde Z\) is geometrically irreducible.

On a generic affine chart, its bilinear equation can be solved for one
residual coefficient, so its function field is rational.  The locus where
\(f_1\) and \(g_1\) have an additional common factor is the residual
resultant divisor.  On the generic \(\PP^{a-1}\times\PP^a\) fiber it has
class \((a,a-1)\), whereas \(\widetilde Z\) has class \((1,1)\).  The two
irreducible divisors therefore differ, so the additional-common-factor locus
does not contain \(\widetilde Z\).  Hence the map to
\[
Z=R_{a,a+1}\cap D_H
\]
is generically one-to-one.  Consequently \(Z\) is irreducible and rational
of dimension \(n-2\), and
\begin{equation}
\label{eq:Z-class}
[Z]\equiv\Lef^{n-2}\pmod{F_{n-3}K_0}.
\end{equation}

\subsection{Proof of stable uniqueness}

\begin{proof}[Proof of \cref{thm:stable-uniqueness}]
For the adjacent higher pairs, inclusion--exclusion and
\eqref{eq:coprime-class}, \eqref{eq:DH-class}, and \eqref{eq:Z-class} give
\begin{equation}
\label{eq:deficit}
[U_{a,a+1,H}]
\equiv\Lef^n-\Lef^{n-2}
\pmod{F_{n-3}K_0}.
\end{equation}
Applying the compactly supported Hodge--Deligne polynomial, terms in
\(F_{n-3}K_0\) cannot change the coefficient of \((uv)^{n-2}\).  Hence
\[
\cE(U_{a,a+1,H};u,v)\ne(uv)^n
=\cE(\A^n;u,v).
\]
Multiplication by \(\A^r\) multiplies the polynomial by \((uv)^r\), so the
same deficit rules out every stable affine-space isomorphism.

For nonadjacent pairs the class-group obstruction already applies.  In the
cubic case \(\{a,b\}=\{1,2\}\),
\cref{prop:cubic-positive-internal} gives an explicit normalization of the
tangent nonosculating hyperplane and identifies the resulting marked-root
incidence open with \(\A^3\).
\end{proof}

\begin{remark}[Why the cubic is the knife edge]
For \(a=1\), the residual product in \eqref{eq:Ztilde} has degree one.  At
the tangent point, the restricted functional vanishes on an entire residual
fiber, giving a second top-dimensional component of \(R\cap D_H\).  Its
extra \(\Lef^{n-2}\) contribution cancels the deficit in
\eqref{eq:deficit}.  For \(a\ge2\), the coefficient
\(\rho_2=v^2\lambda_2\) prevents that vertical component.  The geometric
transition is therefore a codimension-two component count, not merely the
special solvability of cubic equations.
\end{remark}

\section{The conditional universal cover and the remaining defect}
\label{sec:universal}

These results do not show that every generic-degree-three Keller map belongs
to the normalized family.  There is, however, a useful conditional universal
statement.

Let \(V=\Sym^3(\C^2)^\vee\).  The space of a linear form \(L\), a quadratic
form \(Q\), and the normalization \(\Res(L,Q)=1\) is isomorphic to
\[
\operatorname{SL}_2\times\A^1.
\]
Multiplication \((L,Q)\mapsto LQ\) is the universal marked-simple-root map
over the simple-root locus.  This description is compatible with the
classical binary-form and flat-triple-cover frameworks
\cite{miranda1985,wood2011}.

\begin{proposition}[Conditional master-cover statement]
\label{prop:conditional-master}
Let \(F\colon\A^3\to\A^3\) be a generic-degree-three Keller map, and let
\(\overline X\to\A^3\) be the normalization of the target in its function
field.  If \(\overline X\to\A^3\) is finite flat of degree three, then over
the simple-root locus it is a pullback of the universal
resultant-one marked-root cover.  Recovering the original affine source from
\(\overline X\) additionally requires a theorem identifying the entire
deleted boundary.
\end{proposition}

\begin{proof}
The classifying morphism and Cartesian pullback square are constructed in
\cref{prop:master-cover-cartesian}.  That proposition works over the full
simple-root locus, where the residual quadratic also has nonzero
discriminant.  Its boundary-scope remark proves the final qualification:
the finite-cover identification supplies no automatic description of the
open affine source.
\end{proof}

\begin{question}[Cubic flatness]
\label{q:flatness}
Does the Keller condition force the finite cubic normalization
\(\overline X\to\A^3\) to be flat?
\end{question}

The trace-zero summand is a rank-two reflexive module, so a possible defect
is confined to finitely many target points.  General normal \(S_3\)-covers
need not be flat.  We know no argument that rules out this defect using only
the Keller condition.  Thus \cref{q:flatness}, rather than the already
understood universal marked-root algebra, is the current obstruction to a
general cubic classification.

\begin{question}[Boundary Torelli]
\label{q:boundary-torelli}
To what extent is a marked-root cover determined, up to polynomial
left--right equivalence, by its deleted boundary together with the induced
normalization, conductor, and incidence data?  In particular, which
hypotheses make the boundary-completeness problem in
\cref{prop:conditional-master} a reconstruction theorem?
\end{question}

A positive answer would turn the nonproperness boundary from a defect of the
affine map into usable classification data.  The normalized \(A,B\) family
and the stable-uniqueness calculation provide test cases, but no general
boundary Torelli theorem is claimed here.

\section{Exact computations and reproducibility}
\label{sec:computation}

Five exact Python/SymPy programs accompany the reader proof record.
They use rational or finite-field arithmetic only.

\begin{enumerate}[label=(\arabic*)]
\item The normalized-family verifier checks the forced jets in
\cref{thm:pole-cancellation}, the restriction to \(x=0\), the determinant,
the universal discriminant, \eqref{eq:disc-pullback}, and a multi-root
example with explicit collisions and two deleted infinity planes.
\item The equivalence stress verifier checks
\eqref{eq:cubic-transform}, the cusp identity
\eqref{eq:cusp-covariant}, and the complete source--target conjugacy for a
repeated-root example.  It does not prove the Blanc--Stampfli input or the
necessity argument.
\item The stable-uniqueness verifier checks the motivic polynomial
identities and exact point counts for all tangent hyperplanes in the tested
\((2,3)\) and \((3,4)\) finite-field cases.  It does not prove the
class-group, irreducibility, rationality, or Hodge--Deligne steps.
\item The root--slope verifier checks the universal Jacobian,
the marked discriminant factorization, monodromy examples, and the product
description of the discriminant complement in the root--slope appendix.
\item The audit-repair verifier checks the displayed infinity-chart,
retained infinity jet, tangent hyperplane, resultant scaling, and residual
discriminant identities.  It does not prove normalization, purity, descent,
or the binary-cubic correspondence.
\end{enumerate}

The reviewed source files are included in
\texttt{code/core/}; the root-slope and repair checks are in
\path{code/verify_root_slope_extensions.py} and
\path{code/verify_audit_repairs.py}.  The accompanying
\texttt{COMPUTATION.md} gives a claim-to-file index and exact run commands.
Fresh logs and a hash manifest are distributed in the versioned
computational supplement.  These calculations expose the algebra behind the
normal forms: pole cancellation fixes the first two transverse jets, the
cubic discriminant factors on the chosen-root chart, and the same covariants
control source--target equivalence.  They do not replace the geometric
arguments about normalization, boundary components, or automorphism groups.

\appendix
\input{appendices/root-slope-geometry}
\input{appendices/audit-repairs}
\input{appendices/omitted-values}
\input{appendices/cubic-resolvent-defects}
\input{../common/companion-register-note}

\section*{Acknowledgments and disclosure}

The author thanks the participants in the Secret Blogging Seminar and the
subsequent public discussions for rapidly clarifying the geometry of the
counterexample.  In particular, the marked-root and resultant
interpretations and the initial class-group obstruction are credited in
\cref{sec:introduction}.

AI systems were used extensively for exploration, proof drafting, symbolic
code, literature triage, and manuscript editing.  They are not authors.  The
human author is responsible for every mathematical claim.  Exact symbolic
checks are identified in \cref{sec:computation}; the remaining arguments
require ordinary mathematical review.

\bibliographystyle{alpha}
\bibliography{../common/references}

\end{document}
~~~

[Back to the text-source index](../index.md)
