---
title: "Text proof source — 04-stable-moduli/appendices/categorical-boundary-quotient.tex"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `321abf955167e0d80004fcd28a08d0c1ee714a5dcc1eeaeefdf6e82d63d02a1a` · 8,903 bytes

## Exact label anchors

<a id="label-app-categorical-boundary-quotient"></a>
- `app:categorical-boundary-quotient` — source line 2
<a id="label-prop-bounded-root-translation-groupoid"></a>
- `prop:bounded-root-translation-groupoid` — source line 29
<a id="label-thm-categorical-differential-kernel"></a>
- `thm:categorical-differential-kernel` — source line 79
<a id="label-thm-one-wall-control"></a>
- `thm:one-wall-control` — source line 122
<a id="label-thm-fppf-wall-nonalgebraic"></a>
- `thm:fppf-wall-nonalgebraic` — source line 171
<a id="label-subsec-separated-degeneration-spaces"></a>
- `subsec:separated-degeneration-spaces` — source line 223

## Complete source

~~~tex
\section{The bounded coefficient groupoid and its quotients}
\label{app:categorical-boundary-quotient}

This appendix separates three objects that coincide on the generic
finite-root locus but behave differently on the boundary: the affine
categorical quotient, the fppf orbit sheaf, and a separated space retaining
degeneration directions.

For a ring \(R\) and a finite projective \(R\)-module \(E\), we write
\(\mathbf V(E)=\Spec\operatorname{Sym}_R(E^\vee)\).  Kernels below are
scheme-theoretic kernels of affine group schemes over \(\Spec R\).  The
affine categorical quotient is \(\Spec(A^K)\); the orbit sheaf is the fppf
sheafification of the presheaf of pointwise orbits; and \([X/K]\) denotes
the fppf quotient stack.  These are distinct functors on \(R\)-algebras and
are not silently identified at the boundary.

\subsection{A single bounded orbit map}

Fix an ambient degree bound \(N\), and write
\[
\widehat Q(z)=z^N+q_1z^{N-1}+\cdots+q_N,\qquad
P\in\mathbb C[z]/(\widehat Q).
\]
Let \(E_N\) be the tautological rank-\(N\) bundle on
\(\operatorname{Hilb}^N(\mathbb A^1)\), and let \(Z\) denote multiplication by
\(z\).

\begin{proposition}[Bounded orbit map]
\label{prop:bounded-root-translation-groupoid}
The degree-preserving root translations form the kernel pair of the map
\[
\Theta_N\colon\operatorname{Tot}(E_N)\longrightarrow
\operatorname{Tot}(E_N),
\qquad
(\widehat Q,P)\longmapsto(\widehat Q,Z^NP).
\]
If \(\widehat Q=z^mQ_d\), with \(Q_d(0)\ne0\), then uniquely
\[
P=z^mP_d+Q_dS,\qquad \deg P_d<d,\quad\deg S<m.
\]
The finite-root decoration is \(P_d\); root translation removes precisely
the principal part \(S/z^m\) supported at infinity.
\end{proposition}

\begin{proof}
For every \(R\)-algebra, two points \(p,p'\) have the same image under a
linear map \(M\) exactly when \(p-p'\in\ker M\).  These are precisely the
equations of the scheme-theoretic fiber product
\(\mathbf V(E)\times_{\mathbf V(E)}\mathbf V(E)\), where both arrows to the
middle copy are \(M\).  This proves the kernel-pair claim for \(M=Z^N\).

For the decomposition, consider the linear map
\[
\{\deg P_d<d\}\oplus\{\deg S<m\}
\longrightarrow \{\deg P<N\},
\qquad (P_d,S)\longmapsto z^mP_d+Q_dS.
\]
If its value is zero, reduction modulo \(Q_d\) gives
\(z^mP_d=0\).  Since \(Q_d(0)\ne0\), \(z\) is a unit modulo \(Q_d\), so
\(P_d=0\); then \(S=0\).  The source and target both have rank \(N=d+m\),
so the map is an isomorphism, proving existence and uniqueness over the
entire monic coefficient base.
\end{proof}

This formulation uses polynomial remainder by the monic polynomial
\(\widehat Q\), and therefore remains defined on the nonunit-resultant and
nonreduced boundary.

\subsection{Affine categorical quotient}

Let \(R\) be a \(\mathbb Q\)-algebra, \(E\) a finite projective \(R\)-module,
\(M\colon E\to E\), and
\[
K=\ker(\mathbf V(M))\curvearrowright X=\mathbf V(E)
\]
the translation action.  Put \(A=\operatorname{Sym}_R(E^\vee)\).

\begin{theorem}[Differential description]
\label{thm:categorical-differential-kernel}
The invariant algebra is
\[
A^K=\ker\left(
A\xrightarrow{d_{X/R}}
A\otimes_R E^\vee
\longrightarrow
A\otimes_R\operatorname{coker}(M^\vee)
\right).
\]
Equivalently, in homogeneous degree \(r\), it is the kernel of one finite
syzygy map
\[
\operatorname{Sym}^r(E^\vee)\longrightarrow
\operatorname{Sym}^{r-1}(E^\vee)\otimes_R\operatorname{coker}(M^\vee).
\]
\end{theorem}

\begin{proof}
If \(f\) is translation-invariant, the linear term of
\(f(p+s)-f(p)\) vanishes modulo the equations \(Ms=0\); this is exactly the
displayed differential-kernel condition.  Conversely, if
\(df=M^\vee h\), work in the coordinate ring of \(X\times_RK\) and put
\(F(t)=f(p+ts)\).  Then
\[
F'(t)=\langle h(p+ts),Ms\rangle.
\]
This vanishes because \(Ms=0\) on \(K\).  Over a \(\mathbb Q\)-algebra a
polynomial with zero derivative is coefficientwise constant, so
\(F(1)=F(0)\) and \(f\) is invariant.  Restricting the differential map to
homogeneous degree \(r\) gives the stated finite syzygy map.
\end{proof}

For the cubic-frame problem \(M=Z^N\), and the only height-one support of
\(\operatorname{coker}(M^\vee)\) is the one-root wall \(q_N=0\).
Put
\[
R_N=\C[q_1,\ldots,q_N],\qquad
A_N=\operatorname{Sym}_{R_N}(E_N^\vee),\qquad
K_N=\ker(\mathbf V(Z^N)).
\]

\begin{theorem}[One-wall control]
\label{thm:one-wall-control}
Inside the generic polynomial algebra,
\[
A_N^{K_N}
=
A_N\cap (A_N^{K_N})_{(q_N)}.
\]
Thus simultaneous escapes impose no additional divisorial conditions on
global invariant functions.
\end{theorem}

\begin{proof}
Put \(R=\C[q_1,\ldots,q_N]\).  The characteristic polynomial of \(Z\) is
\(\widehat Q\), so
\[
\det Z=(-1)^Nq_N,
\qquad
\det(Z^N)=(\pm q_N)^N.
\]
Thus \(M^\vee=(Z^N)^\vee\) is injective and its cokernel \(C\) has a free
resolution
\[
0\longrightarrow R^N\xrightarrow{M^\vee}R^N
\longrightarrow C\longrightarrow0
\]
with support exactly \(V(q_N)\).  At every prime in its support, the module
\(C\) has
projective dimension one.  Since \(R\) is regular, Auslander--Buchsbaum
shows that \(C\) is Cohen--Macaulay of codimension one.  Hence
\[
\operatorname{Ass}_R(C)=\{(q_N)\}.
\]

In homogeneous degree \(r\), the quotient of
\(\operatorname{Sym}^r(E_N^\vee)\) by the invariant kernel is the image of
the differential map, hence a submodule of
\[
\operatorname{Sym}^{r-1}(E_N^\vee)\otimes_R C.
\]
Every associated prime of that image is therefore \((q_N)\), so the image
injects into its localization at \((q_N)\).  An obstruction that vanishes
after this localization already vanishes globally.  Intersecting inside the
generic free module gives the displayed equality in every degree, and then
for the full graded algebra.  No reflexivity assertion is used.
\end{proof}

\subsection{Why the fppf quotient is not algebraic}

\begin{theorem}[Rank-one wall obstruction]
\label{thm:fppf-wall-nonalgebraic}
Let \(R\) be a DVR with uniformizer \(\pi\), let \(e\ge 1\), and let
\[
K_e=\operatorname{Spec} R[s]/(\pi^es)
\]
act on \(\mathbb A^1_R\) by translation.  Its fppf orbit sheaf is not an algebraic
space, and the quotient stack is not an algebraic stack.  Consequently the
bounded cubic-frame fppf quotient has the same failure along its generic
one-root wall.
\end{theorem}

\begin{proof}
For an \(R\)-algebra \(B\), one has
\(K_e(B)=\operatorname{Ann}_B(\pi^e)\), so the orbit presheaf is
\[
B/\operatorname{Ann}_B(\pi^e)\simeq\pi^eB.
\]
The image functor \(B\mapsto\pi^eB\) is already an fppf sheaf: faithful
flatness detects membership in the submodule \(\pi^eB\).

Set
\[
A'=A''=R/(\pi^{e+1}),\qquad A=R/(\pi^e),
\]
and form the standard Rim--Schlessinger pushout ring
\[
B=A'\times_AA''.
\]
Then \(F(A')=F(A'')\simeq k\), while \(F(A)=0\).  An element of \(B\) has
components congruent modulo \(\pi^e\); because \(e\ge1\), their residues
agree.  Consequently
\[
F(B)=\pi^eB\longrightarrow
F(A')\times_{F(A)}F(A'')\simeq k\oplus k
\]
has diagonal image and is not surjective.  Thus \(F\) fails the strong
Rim--Schlessinger condition, which algebraic stacks satisfy by
\cite[Lemma 98.18.2, Tag 0CXN]{stacks0CXN}.
The translation action is free, so its fppf quotient stack has trivial
inertia; if it were algebraic, it would be an algebraic space and would
coincide with the orbit sheaf, a contradiction.

For the cubic-frame consequence, restrict to a DVR at the generic point of
the one-root wall and, if needed, pass to an étale splitting extension.
Multiplication by \(z\) has one elementary divisor \(\pi\) and all others
units, so \(Z^N\) has Smith form
\(\operatorname{diag}(1,\ldots,1,\pi^N)\) up to units.  This gives the
rank-one action above with \(e=N\ge1\), times an unaffected affine factor;
the conclusion is only asserted on this generic wall neighborhood.
\end{proof}

\subsection{Separated degeneration spaces}
\label{subsec:separated-degeneration-spaces}

The following are candidate local models, not proved constructions in this
appendix.  To turn either assertion into a theorem one must specify the base
ring, the generic quotient coordinate, the map whose graph is closed, and
the relevant family-valued functor.

For a simple wall, the expected graph closure of the generic quotient
coordinate is
the blowup
\[
\operatorname{Bl}_{(\epsilon^{N+2},y)}
\operatorname{Spec} B[\epsilon,y].
\]
For a simultaneous escape of length \(m\), the unique decomposition in
\cref{prop:bounded-root-translation-groupoid} supplies weighted principal
part coordinates.  The proposed projectivization has weights
\[
(1,2,\ldots,m,m+1,m,\ldots,2)
\]
and is a candidate finite-type projective separated model of degeneration
directions.

These graph closures do not represent the orbit sheaf and do not by
themselves prove that stable left--right equivalence is intrinsically
reconstructed at infinity.  A global complete-weighted-collineation space is
a concrete candidate for that last compactification, not a theorem of this
appendix.
~~~

[Back to the text-source index](../../index.md)
