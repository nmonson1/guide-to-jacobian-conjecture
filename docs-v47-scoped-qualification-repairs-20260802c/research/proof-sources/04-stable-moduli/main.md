---
title: "Text proof source — 04-stable-moduli/main.tex"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/04-stable-moduli/main.tex`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `6ad054451c7b0087602be4961ce33102947eb5d53002a8579077784cc1fb0806` · 29,790 bytes

## Exact label anchors

<a id="label-sec-introduction"></a>
- `sec:introduction` — source line 54
<a id="label-eq-ab-general"></a>
- `eq:AB-general` — source line 131
<a id="label-thm-main"></a>
- `thm:main` — source line 141
<a id="label-sec-family"></a>
- `sec:family` — source line 203
<a id="label-eq-frame"></a>
- `eq:frame` — source line 207
<a id="label-eq-g-frame"></a>
- `eq:G-frame` — source line 218
<a id="label-prop-basic"></a>
- `prop:basic` — source line 234
<a id="label-eq-fiber-cubic-general"></a>
- `eq:fiber-cubic-general` — source line 291
<a id="label-eq-reconstruct"></a>
- `eq:reconstruct` — source line 301
<a id="label-eq-diagonal-equivalence"></a>
- `eq:diagonal-equivalence` — source line 328
<a id="label-eq-ab-normalized"></a>
- `eq:AB-normalized` — source line 344
<a id="label-sec-nonproperness"></a>
- `sec:nonproperness` — source line 349
<a id="label-eq-cylinder-np"></a>
- `eq:cylinder-NP` — source line 356
<a id="label-eq-delta"></a>
- `eq:Delta` — source line 368
<a id="label-prop-np"></a>
- `prop:NP` — source line 388
<a id="label-sec-normalization"></a>
- `sec:normalization` — source line 453
<a id="label-eq-normalization-map"></a>
- `eq:normalization-map` — source line 458
<a id="label-eq-hq"></a>
- `eq:Hq` — source line 470
<a id="label-prop-normalization"></a>
- `prop:normalization` — source line 475
<a id="label-eq-t-relation-1"></a>
- `eq:t-relation-1` — source line 486
<a id="label-eq-t-relation-2"></a>
- `eq:t-relation-2` — source line 487
<a id="label-eq-recover-t"></a>
- `eq:recover-t` — source line 502
<a id="label-eq-grad-a"></a>
- `eq:grad-a` — source line 511
<a id="label-eq-grad-b"></a>
- `eq:grad-b` — source line 512
<a id="label-eq-grad-c"></a>
- `eq:grad-c` — source line 514
<a id="label-eq-m-map"></a>
- `eq:M-map` — source line 526
<a id="label-eq-marked-pair"></a>
- `eq:marked-pair` — source line 541
<a id="label-lem-marked-rigidity"></a>
- `lem:marked-rigidity` — source line 547
<a id="label-eq-c-form"></a>
- `eq:C-form` — source line 563
<a id="label-eq-h-pull"></a>
- `eq:H-pull` — source line 570
<a id="label-eq-mu"></a>
- `eq:mu` — source line 586
<a id="label-eq-constant-comparison"></a>
- `eq:constant-comparison` — source line 594
<a id="label-thm-stable-nonexceptional"></a>
- `thm:stable-nonexceptional` — source line 603
<a id="label-sec-exceptional"></a>
- `sec:exceptional` — source line 633
<a id="label-prop-exceptional"></a>
- `prop:exceptional` — source line 647
<a id="label-cor-q-classification"></a>
- `cor:q-classification` — source line 685
<a id="label-sec-alpha-zero"></a>
- `sec:alpha-zero` — source line 699
<a id="label-eq-theta"></a>
- `eq:Theta` — source line 713
<a id="label-eq-ell-delta"></a>
- `eq:ell-delta` — source line 728
<a id="label-eq-xi"></a>
- `eq:Xi` — source line 734
<a id="label-prop-alpha-zero-gauge"></a>
- `prop:alpha-zero-gauge` — source line 744
<a id="label-prop-zero-vs-nonzero"></a>
- `prop:zero-vs-nonzero` — source line 772
<a id="label-sec-verification"></a>
- `sec:verification` — source line 798
<a id="label-sec-questions"></a>
- `sec:questions` — source line 850
<a id="label-q-compactified-stable-moduli"></a>
- `q:compactified-stable-moduli` — source line 877

## Complete source

~~~tex
\documentclass[11pt,reqno]{amsart}
\input{../common/preamble}

\title[Boundary rigidity and stable moduli]{Boundary Rigidity and Stable
Left--Right Moduli at Generic Degree Three}
\author{Nathaniel Monson}
\date{July 22, 2026}

\begin{document}

\begin{abstract}
Building on the public marked-simple-root and cubic-factor construction of
the recent counterexample, we exhibit a one-parameter family of polynomial Keller maps
\(\A^3_{\C}\to\A^3_{\C}\), all of generic degree three, whose members remain
pairwise inequivalent after adjoining arbitrarily many identity variables and
applying arbitrary polynomial changes of source and target coordinates.
The family is obtained from the quadratic cubic-frame data
\[
A_\alpha(c)=c+\alpha c^2,\qquad
B_{\alpha,\beta}(c)=-2-4\alpha c+\beta c^2.
\]
For \(\alpha\ne0\), the complete stable left--right invariant is
\[
q=\beta/\alpha^2.
\]
The line \(\alpha=0\) is a single ordinary left--right orbit, stably distinct
from every \(\alpha\ne0\) orbit.

The invariant is recovered from the nonproperness divisor.  After normalizing
its singular discriminant component, one obtains an affine plane with two
intrinsically marked curves.  A unique-factorization argument
shows that every automorphism of every affine cylinder preserving this marked
pair fixes \(q\).  A separate singular-incidence argument treats the
exceptional value \(q=-2\).  Exact symbolic calculations verify the
discriminant, normalization, conductor, exceptional fiber, and the explicit
gauge transformation on the line \(\alpha=0\).

More generally, on the squarefree coprime cubic-frame locus, the complete
stable invariant is the deleted infinity scheme \(V(A/c)\) decorated by the
transverse derivative \(B|_{V(A/c)}\).  Stable and ordinary left--right
equivalence coincide there.  Within this fixed frame, this yields parameter
families of pairwise stably inequivalent maps of arbitrarily large dimension,
all at generic degree three and, for each family, fixed ordinary degree.
\end{abstract}

\maketitle

\begin{center}
\small\emph{Working manuscript.  The exact symbolic verifier has been rerun
from the recovered source artifact.}
\end{center}

\section{Introduction}
\label{sec:introduction}

The recent counterexample to the Jacobian conjecture gives a polynomial
map \(\A^3_\C\to\A^3_\C\) with nonzero constant Jacobian determinant that
is not an automorphism \cite{alpoge2026announcement,tao2026digestion}.
We credit Akhil Mathew as the primary human source of the problem: Mathew
prompted Levent Alp\"oge, Alp\"oge prompted Fable, Fable produced the
example, and Alp\"oge announced it publicly
\cite{ulam2026counterexample}.
\emph{Constructional provenance.}  The degree-three frame used here is an
adaptation of the public marked-simple-root construction.  Jiang gave its
projective symmetric-product formulation, while Lou independently gave a
factorization--resultant derivation and an explicit affine-three-space chart
\cite{jiang2026markedroot,lou2026derivation}.  Speyer and Tao gave subsequent
geometric expositions, and Ulam developed the inverse-cubic, fiber, image, and
nonproperness descriptions
\cite{speyer2026seminar,tao2026digestion,ulam2026counterexample}.  We use that
construction as input.  The contributions claimed here begin with complete
polynomial left--right classification of the quadratic \(A,B\)-slice,
including stability under adjoining affine variables, and continue with the
decorated-boundary classification in the broader fixed cubic frame.

The construction was quickly placed in larger families.  In particular,
public accounts allow arbitrary one-variable deformation data and produce
counterexamples of every generic degree
\cite{ulam2026counterexample,gallagher2026explained}.  Varying generic
degree already gives inequivalent maps.

Independent exact work of Giannini reports the base map's geometric degree,
exact image, discriminant--Jelonek relation, and full \(S_3\) monodromy
\cite{giannini2026counterexample}.  Santib\'a\~nez-Leal subsequently supplied
another exact validation together with an infinite family and escape-geometry
analysis \cite{santibanezLeal2026validated}.  Shaska independently studied the
graded equivariant structure and its quotient geometry
\cite{shaska2026graded}.  These works overlap the constructional and
base-map background, not the unrestricted stable polynomial left--right
classification treated below.

This paper asks a narrower question:
\begin{quote}
\emph{Can a family of counterexamples of one fixed generic degree carry a
modulus that survives arbitrary polynomial source and target changes, even
after stabilization?}
\end{quote}
The answer is yes already at generic degree three.

Let
\[
F,H\colon\A^n\longrightarrow\A^n
\]
be polynomial maps.  They are \emph{polynomially left--right equivalent} if
there are polynomial automorphisms \(\Phi,\Psi\) of \(\A^n\) such that
\[
H\circ\Phi=\Psi\circ F.
\]
They are \emph{stably polynomially left--right equivalent} if, for some
\(m\ge0\), the maps
\[
F\times\id_{\A^m},\qquad H\times\id_{\A^m}
\]
are polynomially left--right equivalent.  We use this definition throughout;
``stable equivalence'' has other meanings in the Jacobian-conjecture
literature.

Unless a different base is stated explicitly, all schemes, morphisms,
normalizations, and products in this paper are over \(\C\), and every
polynomial automorphism is a \(\C\)-scheme automorphism of affine space.
Nonproperness divisors are taken with their reduced induced structure,
whereas intersections and Fitting ideals retain their scheme structures.
The orbit sets and dimension counts below are set-theoretic or coarse-moduli
statements; no representing moduli scheme or stack for unrestricted stable
left--right equivalence is asserted.  Appendix~D explicitly changes base to
an arbitrary \(\mathbb Q\)-algebra or a DVR and distinguishes affine categorical
quotients, fppf orbit sheaves, and quotient stacks.

For \(\alpha,\beta\in\C\), consider
\begin{equation}
\label{eq:AB-general}
A_\alpha(C)=C+\alpha C^2,\qquad
B_{\alpha,\beta}(C)=-2-4\alpha C+\beta C^2.
\end{equation}
These polynomials define a Keller map \(G_{\alpha,\beta}\) by the cubic-frame
construction in \cref{sec:family}.  Every member has generic degree three
and is nonproper.  Our main theorem classifies the entire two-parameter
family.

\begin{theorem}[Complete stable classification]
\label{thm:main}
The stable polynomial left--right orbit set of the family
\(\set{G_{\alpha,\beta}}\) is
\[
\set{\mathcal O_0}
\ \sqcup\
\set{\mathcal O_q:q\in\C},
\]
where
\[
\mathcal O_0=\set{G_{0,\beta}:\beta\in\C}
\]
and
\[
\mathcal O_q=
\set{G_{\alpha,\beta}:
      \alpha\ne0,\ \beta/\alpha^2=q}.
\]
More explicitly:
\begin{enumerate}[label=(\roman*)]
\item all maps \(G_{0,\beta}\) are ordinarily left--right equivalent;
\item no \(G_{0,\beta}\) is stably equivalent to a member with
      \(\alpha\ne0\); and
\item if \(\alpha,\alpha'\ne0\), then
\[
G_{\alpha,\beta}\sim_{\mathrm{stable}}G_{\alpha',\beta'}
\quad\Longleftrightarrow\quad
\frac{\beta}{\alpha^2}=\frac{\beta'}{\alpha'^2}.
\]
\end{enumerate}
\end{theorem}

The weighted-scaling invariance of \(\beta/\alpha^2\) is immediate.  The
content of \cref{thm:main} is completeness under \emph{arbitrary} polynomial
left--right equivalence and after arbitrary affine stabilization.

Our invariant comes from the set at which the map is not proper.  For a
dominant equidimensional polynomial map this set, if nonempty, is a
hypersurface by Jelonek's theorem \cite{jelonek1993nonproper}.  In our
normalized one-parameter slice it has a singular discriminant component
\(D_q\) and a plane component \(P\).  The normalization of \(D_q\) is an
affine plane containing two intrinsic marked curves:
\[
L_q:
3c(c+1)t+qc^2-4c-2=0,
\qquad
M:c+1=0.
\]
The pair \((L_q,M)\) remembers \(q\), even after taking a product with
affine space.  This gives the necessity in \cref{thm:main}.

The existence of left--right moduli for nonproper étale maps on other affine
varieties has important precedent: Dubouloz and Palka constructed
high-dimensional families on affine pseudo-planes
\cite{duboulozPalka2019}.  Our theorem concerns polynomial self-maps of
affine space arising directly from the new three-dimensional construction.
The general marked-root framework and its unstabilized equivalence criterion
are developed in the companion paper \cite{monson2026markedroot}.  The proof
below includes all of the special geometry needed for stable separation in
the quadratic slice.

\section{The quadratic cubic-frame family}
\label{sec:family}

Put
\begin{equation}
\label{eq:frame}
c=2x-3x^2y-x^3z,\qquad
t=y+\frac1x,\qquad
r=\frac2x.
\end{equation}
For \(A=A_\alpha\) and \(B=B_{\alpha,\beta}\), let
\[
h(T,C)=A(C)T^3+B(C)T^2
\]
and define
\begin{equation}
\label{eq:G-frame}
b=r-\frac{\partial h}{\partial T}(t,c),
\qquad
2a=h(t,c)+tb.
\end{equation}
Although \eqref{eq:frame} uses \(1/x\), the two expressions in
\eqref{eq:G-frame} are polynomials.  We write
\[
G_{\alpha,\beta}=(a,b,c)
\colon\A^3_{x,y,z}\longrightarrow\A^3_{a,b,c}.
\]
The projective root incidence and simple-root reconstruction used below are
adaptations of the marked-root and inverse-cubic descriptions cited in the
introduction.

\begin{proposition}
\label{prop:basic}
For every \(\alpha,\beta\in\C\), the map \(G_{\alpha,\beta}\) is polynomial,
\[
\det DG_{\alpha,\beta}=-2,
\]
and its generic degree is three.
\end{proposition}

\begin{proof}
Set
\[
\xi=1+xy,\qquad d=2-3xy-x^2z,
\]
so that \(t=\xi/x\) and \(c=xd\).  Clearing denominators in \(b\) gives
\[
b=
\frac{2+4\xi-3d\xi^2}{x}
-3\alpha d^2\xi^2+8\alpha d\xi
-2\beta x d^2\xi.
\]
The numerator of the displayed fraction vanishes at \(x=0\), hence is
divisible by \(x\).  More explicitly,
\[
2+4\xi-3d\xi^2
=x\bigl(3x^3y^2z+9x^2y^3+6x^2yz+12xy^2+3xz+y\bigr).
\]
Similarly,
\[
2a=
\frac{2\xi-2d\xi^3+2\xi^2}{x^2}
+\frac{4\alpha d\xi^2-2\alpha d^2\xi^3}{x}
-\beta d^2\xi^2.
\]
Here
\[
2\xi-2d\xi^3+2\xi^2
=2x^2(1+xy)
 \bigl(x^2y^2z+3xy^3+2xyz+4y^2+z\bigr),
\]
while the second numerator is
\[
2\alpha d\xi^2(2-d\xi),\qquad
2-d\xi=x\bigl(x^2yz+3xy^2+xz+y\bigr).
\]
Thus \(a\) and \(b\) are polynomial.

On \(x\ne0\), the coordinate changes in \eqref{eq:frame} give
\[
\det\frac{\partial(a,b,c)}{\partial(t,r,c)}=\frac r2,
\qquad
\det\frac{\partial(t,r,c)}{\partial(x,y,z)}=-2x.
\]
Since \(r=2/x\), their product is \(-2\).  Polynomiality extends this
identity across \(x=0\).

For a target point \((a,b,c)\), introduce
\begin{equation}
\label{eq:fiber-cubic-general}
P_{a,b,c}(T)=A(c)T^3+B(c)T^2+bT-2a.
\end{equation}
The construction gives
\[
P_{G_{\alpha,\beta}(x,y,z)}(t)=0,\qquad
P'_{G_{\alpha,\beta}(x,y,z)}(t)=\frac2x.
\]
Conversely, every finite simple root \(t\) reconstructs
\begin{equation}
\label{eq:reconstruct}
x=\frac2{P'(t)},\qquad
y=t-\frac{P'(t)}2,\qquad
z=\frac{2x-3x^2y-c}{x^3}.
\end{equation}
A general cubic \eqref{eq:fiber-cubic-general} has three finite simple roots,
giving three source points.
\end{proof}

\begin{remark}
The determinant in \cref{prop:basic} is \(-2\), rather than \(1\), only
because of our target normalization.  A linear target rescaling gives the
usual Keller normalization.
\end{remark}

\subsection{The ordinary scaling orbit}

Suppose \(\alpha,\alpha'\ne0\), and put
\[
u=\frac{\alpha}{\alpha'}.
\]
If
\[
\frac{\beta}{\alpha^2}=\frac{\beta'}{\alpha'^2},
\]
then direct substitution gives
\begin{equation}
\label{eq:diagonal-equivalence}
G_{\alpha',\beta'}
\left(ux,\frac yu,\frac z{u^2}\right)
=
\left(\frac a{u^2},\frac bu,uc\right)
\quad\text{when}\quad
(a,b,c)=G_{\alpha,\beta}(x,y,z).
\end{equation}
Thus equality of \(q=\beta/\alpha^2\) is sufficient for ordinary
equivalence.  Every nonzero-\(\alpha\) orbit therefore has the normalized
representative
\[
G_q:=G_{1,q},
\]
with
\begin{equation}
\label{eq:AB-normalized}
A(c)=c(c+1),\qquad B_q(c)=qc^2-4c-2.
\end{equation}

\section{The intrinsic nonproperness divisor}
\label{sec:nonproperness}

For a dominant polynomial map \(F\), write \(S_F\) for its reduced
nonproperness set.  Polynomial source automorphisms leave \(S_F\) unchanged,
target automorphisms carry it isomorphically to the new nonproperness set,
and
\begin{equation}
\label{eq:cylinder-NP}
S_{F\times\id_{\A^m}}=S_F\times\A^m.
\end{equation}
The last identity follows either from the valuative criterion or directly
from sequences escaping to infinity.

The discriminant of the normalized fiber cubic
\[
P_{a,b,c}(T)=A(c)T^3+B_q(c)T^2+bT-2a
\]
is
\begin{equation}
\label{eq:Delta}
\Delta_q=
B_q^2b^2-4Ab^3+8B_q^3a
-108A^2a^2-36AB_qab.
\end{equation}
For \(q\ne-2\), let
\[
D_q=V(\Delta_q).
\]
For \(q=-2\), the polynomial \(\Delta_{-2}\) has content \(c+1\); in that
case put
\[
D_{-2}=V\left(\frac{\Delta_{-2}}{c+1}\right).
\]
In every case let
\[
P=V(c+1).
\]

\begin{proposition}
\label{prop:NP}
For every \(q\in\C\),
\[
S_{G_q}=D_q\cup P.
\]
These are the two irreducible components.  For \(q\ne-2\), the component
\(D_q\) is singular and \(P\) is smooth.
\end{proposition}

\begin{proof}
For \(q\ne-2\), the polynomials \(A\) and \(B_q\) are coprime.  Regarding
\(\Delta_q\) as a quadratic in \(a\), one computes
\[
\Disc_a(\Delta_q)=64(B_q^2-3Ab)^3.
\]
The right side is not a square in \(\C(b,c)\), so Gauss's lemma gives the
irreducibility of \(\Delta_q\).

Use instead the projective root incidence
\[
\overline X_q=
V(AU^3+B_qU^2V+bUV^2-2aV^3)
\subset\A^3\times\PP^1.
\]
The marked-root map sends the source to the simple-root locus.  On the
finite-root chart, the reconstruction formula of
\cref{prop:basic} is a two-sided inverse.  The simple infinity
root over \(c=0\) is retained: it is the image of \(x=0\), and the
restriction there is the triangular isomorphism
\[
(y,z)\longmapsto (b,a)
=\bigl(y+4,\ z+4y^2+2y-2q\bigr).
\]
These formulas
show that the marked-root map is radicial.  It is also étale, since the
incidence projection is étale on the simple-root locus and
\(\det DG_q=-2\).  Hence it is an open immersion, with image exactly the
simple-root locus minus the infinity section over \(c=-1\).

For completeness, if a proper morphism \(\pi:X\to Y\) restricts to
\(f:U\to Y\) on a dense open \(U\subset X\), then the nonproperness locus of
\(f\) is \(\pi(X\setminus U)\).  One inclusion follows because the
complement has been removed.  Conversely, if \(f\) were proper over a
neighborhood of a point in that image, the open immersion
\(U\hookrightarrow X\) would be proper there, hence closed, and density
would force it to be surjective.  Applying this lemma to
\(\overline X_q\) shows that the boundary image is exactly the union of the
projective discriminant and the deleted plane \(P\).  This proves the
assertion for \(q\ne-2\), including the retained infinity-root case.  See
\cref{app:all-multiplicity-relative-jacobian} for the general construction.

At \(q=-2\), one has \(B_{-2}=-2(c+1)^2\).  Dividing the discriminant by
its coefficient content \(c+1\) gives the unique primitive nonplane
component, while the same lost-root argument gives \(P\).  Irreducibility of
the primitive discriminant follows by applying the preceding quadratic
argument over \(\C(c)\) and then Gauss's lemma.  This is also the special
case of the all-multiplicity nonproperness theorem in
\cite{monson2026markedroot}.

Finally, for \(q\ne-2\) the normalization calculation in
\cref{prop:normalization} shows that \(D_q\) is singular, while \(P\) is a
plane.
\end{proof}

\section{Normalization and the marked pair}
\label{sec:normalization}

Assume throughout this section that \(q\ne-2\).  A repeated root \(t\) of
the inverse cubic gives
\begin{equation}
\label{eq:normalization-map}
\begin{aligned}
b&=-3A(c)t^2-2B_q(c)t,\\
a&=-A(c)t^3-\frac12B_q(c)t^2.
\end{aligned}
\end{equation}
Let
\[
\nu_q\colon\A^2_{c,t}\longrightarrow D_q
\]
be the map \eqref{eq:normalization-map}, and put
\begin{equation}
\label{eq:Hq}
H_q(c,t)=3c(c+1)t+qc^2-4c-2.
\end{equation}

\begin{proposition}
\label{prop:normalization}
The map \(\nu_q\) is the normalization of \(D_q\).  Moreover,
\[
\nu_q^{-1}(\Sing D_q)=
L_q:=V(H_q).
\]
\end{proposition}

\begin{proof}
On the parametrization, \(t\) satisfies
\begin{align}
3At^2+2B_qt+b&=0,\label{eq:t-relation-1}\\
B_qt^2+2bt-6a&=0.\label{eq:t-relation-2}
\end{align}
Because \(\gcd(A,B_q)=1\), choose
\(\rho,\sigma\in\C[c]\) with \(\rho A+\sigma B_q=1\).
The sum of \(\rho/3\) times \eqref{eq:t-relation-1} and \(\sigma\) times
\eqref{eq:t-relation-2} is the monic equation
\[
t^2+
\left(\frac23\rho B_q+2\sigma b\right)t
+\frac13\rho b-6\sigma a=0
\]
over \(\C[D_q]\).  Hence \(\nu_q\) is finite.

Direct substitution gives
\begin{equation}
\label{eq:recover-t}
B_q^2-3Ab=H_q^2,\qquad
-18Aa-B_qb=2tH_q^2.
\end{equation}
Thus \(t\) is rationally recovered away from \(H_q=0\), so \(\nu_q\) is
birational.  Since \(\A^2\) is normal, it is the normalization.

The pullbacks of the three partial derivatives of \(\Delta_q\) are
\begin{align}
(\Delta_q)_a\circ\nu_q&=8H_q^3,\label{eq:grad-a}\\
(\Delta_q)_b\circ\nu_q&=-4tH_q^3,\label{eq:grad-b}\\
(\Delta_q)_c\circ\nu_q
&=-4t^2(2cq+2ct+t-4)H_q^3.\label{eq:grad-c}
\end{align}
The first equality shows that all three vanish simultaneously exactly on
\(H_q=0\).
\end{proof}

The plane component \(P\) marks a second curve upstairs.  Write
\[
d=q+2.
\]
On \(c=-1\), formulas \eqref{eq:normalization-map} become
\begin{equation}
\label{eq:M-map}
a=-\frac d2t^2,\qquad b=-2dt.
\end{equation}
Since \(d\ne0\), the inverse image of \(D_q\cap P\) is the line
\[
M:=V(c+1)\subset\A^2_{c,t},
\]
and \(M\to D_q\cap P\) is an isomorphism.  Notice also that
\[
H_q|_M=q+2\ne0,
\]
so \(L_q\cap M=\varnothing\).

The intrinsic data recovered from \(S_{G_q}\) are therefore
\begin{equation}
\label{eq:marked-pair}
(\A^2_{c,t},L_q,M).
\end{equation}
The next lemma is the heart of the stable argument.

\begin{lemma}[Rigidity of the marked cylinder]
\label{lem:marked-rigidity}
Let \(q,q'\ne-2\) and \(m\ge0\).  Suppose a polynomial automorphism of
\(\A^{2+m}\) carries
\[
L_q\times\A^m\ \text{to}\ L_{q'}\times\A^m
\quad\text{and}\quad
M\times\A^m\ \text{to}\ M\times\A^m.
\]
Then \(q=q'\).
\end{lemma}

\begin{proof}
Let \(C,T\) be the pullbacks of the first two coordinates on the target
cylinder.  Since the prime principal divisor \(M\times\A^m\) is preserved,
unique factorization gives
\begin{equation}
\label{eq:C-form}
C+1=\lambda(c+1)
\end{equation}
for some \(\lambda\in\C^*\).  For \(q\ne-2\), the polynomial \(H_q\) is
primitive and linear in \(t\), hence irreducible.  Preservation of the other
prime divisor similarly gives
\begin{equation}
\label{eq:H-pull}
H_{q'}(C,T)=\kappa H_q(c,t)
\end{equation}
for some \(\kappa\in\C^*\).

The right side of \eqref{eq:H-pull} is independent of the stabilization
variables and linear in \(t\).  Since \(C\) is the nonconstant polynomial
in \eqref{eq:C-form}, solving \eqref{eq:H-pull} first shows that \(T\)
belongs to \(\C(c)[t]\), has no stabilization-variable dependence, and has
degree one in \(t\).  Since \(T\) is a polynomial, it follows that
\[
T=\mu(c)t+h(c)
\]
for polynomials \(\mu,h\in\C[c]\).  Comparing the coefficients of \(t\) in
\eqref{eq:H-pull} and cancelling \(c+1\) gives
\begin{equation}
\label{eq:mu}
\lambda\bigl(\lambda(c+1)-1\bigr)\mu(c)=\kappa c.
\end{equation}
The linear polynomial \(\lambda(c+1)-1\) must divide \(c\).  Therefore
\(\lambda=1\), and \eqref{eq:mu} gives \(\mu=\kappa\).

The constant term of \eqref{eq:H-pull} is now
\begin{equation}
\label{eq:constant-comparison}
3c(c+1)h(c)+B_{q'}(c)=\kappa B_q(c).
\end{equation}
At \(c=0\), both \(B_q\) and \(B_{q'}\) equal \(-2\), so
\(\kappa=1\).  At \(c=-1\), equation
\eqref{eq:constant-comparison} gives \(q'+2=q+2\).
\end{proof}

\begin{theorem}
\label{thm:stable-nonexceptional}
If \(q,q'\ne-2\), then \(G_q\) and \(G_{q'}\) are stably polynomially
left--right equivalent if and only if \(q=q'\).
\end{theorem}

\begin{proof}
Sufficiency is immediate.  For necessity, suppose the stabilizations by
\(\A^m\) are left--right equivalent.  By \eqref{eq:cylinder-NP}, the target
automorphism identifies
\[
(D_q\cup P)\times\A^m
\quad\text{with}\quad
(D_{q'}\cup P)\times\A^m.
\]
The plane component is smooth and the discriminant component is singular, so
the two components cannot be exchanged.  We obtain an isomorphism
\[
D_q\times\A^m\simeq D_{q'}\times\A^m
\]
that preserves the intersection with the plane component.

Normalization commutes with adjoining polynomial variables.  The isomorphism
therefore lifts uniquely to an automorphism of
\(\A^2\times\A^m\).  The inverse image of the singular locus is
\(L_q\times\A^m\), and the inverse image of the plane intersection is
\(M\times\A^m\).  The lifted automorphism preserves this marked pair, so
\cref{lem:marked-rigidity} gives \(q=q'\).
\end{proof}

\section{The exceptional value}
\label{sec:exceptional}

At \(q=-2\),
\[
B_{-2}(c)=-2(c+1)^2
\]
and \(\Delta_{-2}\) acquires the factor \(c+1\).  Let
\[
\Delta_{-2}^{\mathrm{res}}=\frac{\Delta_{-2}}{c+1},
\qquad
D_{-2}=V(\Delta_{-2}^{\mathrm{res}}).
\]

\begin{proposition}
\label{prop:exceptional}
The map \(G_{-2}\) is not stably left--right equivalent to \(G_q\) for any
\(q\ne-2\).
\end{proposition}

\begin{proof}
On the plane \(c=-1\), exact substitution gives
\[
\Delta_{-2}^{\mathrm{res}}|_{c=-1}=4b^3.
\]
Thus the reduced intersection \(D_{-2}\cap P\) is the line \(b=0\).
At the point
\[
p=(a,b,c)=(0,0,-1),
\]
all three first partial derivatives of
\(\Delta_{-2}^{\mathrm{res}}\) vanish.  Hence
\[
\Sing(D_{-2})\cap P\ne\varnothing.
\]

For \(q\ne-2\), by contrast,
\[
\left.\frac{\partial\Delta_q}{\partial a}\right|_{c=-1}
=8(q+2)^3\ne0.
\]
Consequently \(D_q\) is smooth along its entire intersection with \(P\), and
\[
\Sing(D_q)\cap P=\varnothing.
\]
Whether the singular locus of the unique nonplane component meets the plane
component is intrinsic to the reduced nonproperness divisor.  The same is
true after taking a product with affine space.  Equation
\eqref{eq:cylinder-NP} therefore separates \(G_{-2}\) from every other
\(G_q\) stably.
\end{proof}

\begin{corollary}
\label{cor:q-classification}
For all \(q,q'\in\C\),
\[
G_q\sim_{\mathrm{stable}}G_{q'}
\quad\Longleftrightarrow\quad
q=q'.
\]
\end{corollary}

\begin{proof}
Combine \cref{thm:stable-nonexceptional,prop:exceptional}.
\end{proof}

\section{The line \texorpdfstring{\(\alpha=0\)}{alpha=0} is gauge}
\label{sec:alpha-zero}

It remains to understand the parameter line not covered by the normalization
\(\alpha=1\).  When \(\alpha=0\),
\[
A(C)=C,\qquad B(C)=-2+\beta C^2.
\]
Put
\[
s=\frac\beta3,\qquad
c(x,y,z)=2x-3x^2y-x^3z,
\]
and define
\begin{equation}
\label{eq:Theta}
\Theta_s(x,y,z)=
\left(
x,\ y+sc,\ z-3s\frac cx
\right).
\end{equation}
This is polynomial because
\[
\frac cx=2-3xy-x^2z.
\]
It preserves \(c\), has Jacobian determinant one, and has inverse
\(\Theta_{-s}\).

Set
\begin{equation}
\label{eq:ell-delta}
\ell_s(c)=3s^2c^3-4sc,\qquad
\delta_s(c)=s^3c^4-2s^2c^2,
\end{equation}
and define the triangular target automorphism
\begin{equation}
\label{eq:Xi}
\Xi_s(a,b,c)=
\left(
a-\frac12\delta_s(c)-\frac{sc}{2}b,\
b+\ell_s(c),\
c
\right).
\end{equation}

\begin{proposition}
\label{prop:alpha-zero-gauge}
For every \(\beta\in\C\),
\[
G_{0,\beta}
=
\Xi_{\beta/3}\circ G_{0,0}\circ\Theta_{\beta/3}.
\]
In particular, the entire line \(\alpha=0\) is one ordinary left--right
orbit.
\end{proposition}

\begin{proof}
Because \(\Theta_s\) fixes \(c\), it sends the framed root
\(t=y+1/x\) to \(t+sc\).  Substitute this translation in
\[
cT^3-2T^2
\]
and compare the coefficients of \(T\) with
\[
cT^3+(-2+3sc^2)T^2.
\]
The residual linear and constant terms are precisely the target shears
\(\ell_s\) and \(\delta_s\) in \eqref{eq:ell-delta}.  Substitution in
\eqref{eq:G-frame} gives the displayed identity.  All expressions are
polynomial, and \(\Theta_s,\Xi_s\) are triangularly invertible.
\end{proof}

\begin{proposition}
\label{prop:zero-vs-nonzero}
No member with \(\alpha=0\) is stably left--right equivalent to a member
with \(\alpha\ne0\).
\end{proposition}

\begin{proof}
For \(\alpha=0\), the polynomial \(A(C)=C\) has only the marked root.
The reduced nonproperness set therefore consists solely of its irreducible
primitive discriminant component.  For \(\alpha\ne0\), the second root
\(-1/\alpha\) contributes a plane component in addition to the primitive
discriminant component, as in \cref{prop:NP}.  Thus the two nonproperness
sets have respectively one and two irreducible components.  Products with
\(\A^m\) preserve this component count, and
\eqref{eq:cylinder-NP} makes it a stable left--right invariant.
\end{proof}

\begin{proof}[Proof of \cref{thm:main}]
The first assertion is \cref{prop:alpha-zero-gauge}; the second is
\cref{prop:zero-vs-nonzero}.  For nonzero \(\alpha,\alpha'\), equality of
\(\beta/\alpha^2\) gives the ordinary equivalence
\eqref{eq:diagonal-equivalence}.  Conversely, normalize both maps to
\(\alpha=1\) using the same formula and apply
\cref{cor:q-classification}.
\end{proof}

\section{Exact verification and proof boundary}
\label{sec:verification}

The accompanying verifier uses exact SymPy arithmetic.  It checks:
\begin{enumerate}[label=(\arabic*)]
\item the discriminant \eqref{eq:Delta} and its discriminant as a quadratic
in \(a\);
\item the normalization formulas \eqref{eq:normalization-map};
\item both rational-recovery identities \eqref{eq:recover-t};
\item all three gradient factorizations
\eqref{eq:grad-a}--\eqref{eq:grad-c};
\item the marked-line formulas \eqref{eq:M-map};
\item the factorization and singular-incidence calculation at \(q=-2\);
\item the coefficient identity used in \cref{lem:marked-rigidity};
\item the identity that gauges away \(\beta\) when \(\alpha=0\); and
\item the Jacobian identity \(\det D\Theta_s=1\).
\end{enumerate}

The unchanged recovered verifier was rerun in a fresh environment with SymPy
declared explicitly.  It printed
\[
\texttt{ALL q-ORBIT CHECKS PASSED},
\]
and regenerated a JSON audit byte-for-byte identical to the recovered
reference output.

The principal verifier is
\texttt{code/main-modulus/verify\_q\_full\_orbit.py}.  The companion source
also includes separate exact checks for the reciprocal family, the
grading-preserving and based moduli problems, conductor arrangements,
weighted-lift critical-root invariants, and boundary-residue constructions.
They are indexed by mathematical role in \texttt{COMPUTATION.md}; their
purpose is to make the displayed invariant formulas reproducible without
conflating the narrower framed equivalence problems with the stable
left--right theorem in the body.

The bounded version-2 audit-repair verifier indexed in
\texttt{COMPUTATION.md}
independently checks the displayed pole factorizations, retained-infinity
formulas, conductor recovery identities, Bezout quadratic, general
discriminant identity, and the finite hypotheses used by the all-order
formal recursion.  It deliberately does not materialize the rapidly growing
fourth formal coefficient: the all-order assertion is proved by induction in
\cref{prop:formal-stable-separation}, not inferred from finite sampling.

These computations verify the displayed polynomial identities.  The
geometric assertions that the nonproperness divisor is intrinsic, that
normalization lifts an isomorphism, and that the two marked curves are
recovered as asserted are proved conventionally in
\cref{sec:nonproperness,sec:normalization}; they are not being inferred from
the symbolic replay.

\section{Consequences and questions}
\label{sec:questions}

\Cref{thm:main} gives an affine line of stable left--right orbits at one fixed
generic degree, together with one additional degenerate orbit.  The modulus
is not imposed as part of a framing: it is reconstructed from the intrinsic
boundary geometry of the map.

The proof deliberately leaves broader claims outside its scope.  In
particular, it does not classify all cubic-frame counterexamples, all
generic-degree-three Keller maps, or the full stable moduli functor.

\begin{question}
Which larger finite-dimensional cubic-frame families admit complete stable
invariants recovered from their normalized nonproperness divisors?
\end{question}

\begin{question}
Can the marked-cylinder rigidity argument be formulated as a general
cancellation theorem for pairs \((\A^2,L,M)\)?
\end{question}

\begin{question}
What scheme or stack represents deformations of the maps in
\cref{thm:main} modulo stable polynomial left--right equivalence?
\end{question}

\begin{question}[Compactification across boundary collisions]
\label{q:compactified-stable-moduli}
Can the all-multiplicity finite-root classification of
\cref{thm:all-multiplicity-torelli} be compactified across strata where
deleted roots escape to \(c=\infty\)?  The elementary one-root transition
on the resultant-open locus is the contracted gauge chart of
\cref{prop:one-root-transition}.  The desired object must also handle
simultaneous escapes and the nonunit resultant boundary while retaining the
weighted relative-Jacobian data as the number of finite marked planes
changes.
\end{question}

\appendix
\input{appendices/general-boundary-residues}
\input{appendices/all-multiplicity-relative-jacobian}
\input{appendices/conductor-arrangements}
\input{appendices/categorical-boundary-quotient}
\input{../common/companion-register-note}

\section*{AI and computational disclosure}

AI systems were used extensively in exploration, proof drafting, symbolic
program development, source organization, and manuscript editing.  They are
not authors.  The mathematical evidence for the computer-checked identities
is the exact verifier and reproducible output described in
\cref{sec:verification}, not the output of a language model.

\bibliographystyle{amsplain}
\bibliography{../common/references}

\end{document}
~~~

[Back to the text-source index](../index.md)
