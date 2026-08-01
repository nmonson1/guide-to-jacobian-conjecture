---
title: "Text proof source — 02-low-degree/main.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/02-low-degree/main.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `1c6ab2cf0f37502cff7f541c0800b41ccaf51fc0822a75784dc47af3f94ab7b7` · 42,308 bytes

## Exact label anchors

<a id="label-sec-introduction"></a>
- `sec:introduction` — source line 60
<a id="label-eq-homogeneous"></a>
- `eq:homogeneous` — source line 86
<a id="label-eq-rho"></a>
- `eq:rho` — source line 99
<a id="label-thm-rank-one"></a>
- `thm:rank-one` — source line 127
<a id="label-thm-conic"></a>
- `thm:conic` — source line 147
<a id="label-sec-jets-at-infinity"></a>
- `sec:jets-at-infinity` — source line 164
<a id="label-eq-maximal-contact"></a>
- `eq:maximal-contact` — source line 175
<a id="label-sec-coordinates"></a>
- `sec:coordinates` — source line 202
<a id="label-lem-quadratic-coordinate"></a>
- `lem:quadratic-coordinate` — source line 209
<a id="label-lem-cubic-coordinate"></a>
- `lem:cubic-coordinate` — source line 243
<a id="label-prop-easy-branches"></a>
- `prop:easy-branches` — source line 277
<a id="label-sec-pencil"></a>
- `sec:pencil` — source line 316
<a id="label-eq-highest"></a>
- `eq:highest` — source line 321
<a id="label-lem-weighted-field"></a>
- `lem:weighted-field` — source line 328
<a id="label-prop-cubic-pencils"></a>
- `prop:cubic-pencils` — source line 384
<a id="label-sec-rank-one-proof"></a>
- `sec:rank-one-proof` — source line 446
<a id="label-eq-lower-terms"></a>
- `eq:lower-terms` — source line 465
<a id="label-eq-id1"></a>
- `eq:id1` — source line 483
<a id="label-eq-id2"></a>
- `eq:id2` — source line 484
<a id="label-eq-id3"></a>
- `eq:id3` — source line 485
<a id="label-eq-id4"></a>
- `eq:id4` — source line 486
<a id="label-eq-id5"></a>
- `eq:id5` — source line 492
<a id="label-eq-id6"></a>
- `eq:id6` — source line 493
<a id="label-eq-id7"></a>
- `eq:id7` — source line 494
<a id="label-lem-first-syzygy"></a>
- `lem:first-syzygy` — source line 498
<a id="label-lem-second-syzygy"></a>
- `lem:second-syzygy` — source line 525
<a id="label-sec-span-two"></a>
- `sec:span-two` — source line 587
<a id="label-lem-leading-image"></a>
- `lem:leading-image` — source line 594
<a id="label-prop-four-loci"></a>
- `prop:four-loci` — source line 652
<a id="label-rem-r-zero"></a>
- `rem:r-zero` — source line 699
<a id="label-sec-conic"></a>
- `sec:conic` — source line 724
<a id="label-eq-conic-form"></a>
- `eq:conic-form` — source line 728
<a id="label-lem-orbits"></a>
- `lem:orbits` — source line 734
<a id="label-lem-invariants"></a>
- `lem:invariants` — source line 774
<a id="label-eq-tab"></a>
- `eq:TAB` — source line 829
<a id="label-eq-chain"></a>
- `eq:chain` — source line 842
<a id="label-eq-divisibility"></a>
- `eq:divisibility` — source line 870
<a id="label-prop-terminal-conic"></a>
- `prop:terminal-conic` — source line 897
<a id="label-sec-degree-seven-escape"></a>
- `sec:degree-seven-escape` — source line 965
<a id="label-sec-computation"></a>
- `sec:computation` — source line 989
<a id="label-sec-open-degree-four"></a>
- `sec:open-degree-four` — source line 1069
<a id="label-rem-leaf-accounting"></a>
- `rem:leaf-accounting` — source line 1078

## Complete source

~~~tex
\documentclass[11pt,reqno]{amsart}
\input{../common/preamble}

\title[Quartic Keller maps and leading curves]{Quartic Keller Maps and
Leading Curves at Infinity}
\author{Nathaniel Monson}
\date{July 22, 2026}

\begin{document}

\begin{abstract}
The known three-dimensional counterexample to the Jacobian conjecture has
ordinary coordinate degree seven, while degree at most three is classically
known to be invertible.  This leaves ordinary degrees four, five, and six.
For \(F=LX+H_2+H_3+H_4\), the rescaling
\[
K_\epsilon(X)=\epsilon^4F(X/\epsilon)
\]
satisfies \(\det JK_\epsilon=\epsilon^9\det JF\).  Thus the Keller
condition is a maximal-contact condition along the determinantal
hypersurface, and the leading map collapses the projective boundary to a
point or a rational curve.

Our first result excludes one-dimensional leading target span: if the three
coordinate forms of \(F_4\) span a line, then a degree-at-most-four Keller map
\(\A^3_{\C}\to\A^3_{\C}\) is a polynomial automorphism.  The proof reduces
the transverse cubic pencil to a cube-containing or binary pencil and then
uses two universal determinant syzygies.

This excludes in ordinary degree four the rank-one leading mechanism visible
in the known degree-seven example.  We also treat a conic-image stratum, in
which
\[
F_4=G(x,y,z)(x^2,xy,y^2).
\]
If the quadratic \(G\) is reduced and the base point
\([0:0:1]\) is outside \(G=0\) or is a nonsingular point of it, then the
Keller equations are inconsistent.  The final step is an exact symbolic
calculation in four parabolic orbits.

A continuation appendix closes the two proper rational-quartic frontier
strata.  It follows that a quartic counterexample, if one exists, has leading
target span exactly two.  In that locus we exclude the genuinely nonbinary
quadratic-source case and prove that every coprime binary-pencil map with
common ramification divisor of degree at most two is an automorphism.  The
surviving quartic problem is concentrated in triple-or-higher binary
ramification and fixed-component boundary cases.
\end{abstract}

\maketitle

\begin{center}
\small\emph{Working manuscript.  The exact symbolic calculations have been
reproduced from the recovered sources.  The pencil reductions and
computer-assisted conic argument still require independent specialist
review.}
\end{center}

\section{Introduction}
\label{sec:introduction}

For a polynomial map \(F=(F_1,F_2,F_3)\), its \emph{ordinary degree} is
\[
\deg F=\max_i\deg F_i.
\]
This convention matters: generic fiber degree and ordinary coordinate degree
are different invariants.

The counterexample has ordered coordinate-degree profile \((7,6,4)\), and
hence ordinary degree seven
\cite{alpoge2026announcement,tao2026digestion}.  We credit Akhil Mathew as
the primary human source of the problem: Mathew prompted Levent Alp\"oge,
Alp\"oge prompted Fable, Fable produced the example, and Alp\"oge announced
it publicly \cite{ulam2026counterexample}.  Vistoli proved that every
three-dimensional Keller map of ordinary degree at most three is an
automorphism \cite{vistoli1999}.  Thus, if \(D_{\min}\) denotes the least
ordinary degree of a three-dimensional counterexample, the presently known
endpoints give
\[
4\le D_{\min}\le7.
\]
The interval is background, not a novelty claim.

Write an affine-normalized degree-four map as
\begin{equation}
\label{eq:homogeneous}
F=LX+H_2+H_3+H_4,
\qquad L\in\operatorname{GL}_3(\C),
\end{equation}
with \(H_i\) homogeneous of degree \(i\).  Throughout, the base field is
algebraically closed of characteristic zero; theorem statements fix
\(\C\), and every argument uses only those two properties.  The constant
term is removed by a target translation, which changes neither the Keller
condition nor invertibility, and no separate hypothesis on \(L\) is
needed: \(L=JF(0)\), so the Keller condition itself makes \(L\)
invertible.  Define the \emph{leading target
span}
\begin{equation}
\label{eq:rho}
\rho_4(F)=
\dim_{\C}\angles{(H_4)_1,(H_4)_2,(H_4)_3}
\subset \Sym^4((\C^3)^\vee).
\end{equation}
This is not the generic rank of \(JH_4\), Waring rank, or tensor rank.

There is a complementary geometric invariant.  The projectivized leading
map
\[
\phi_4\colon\PP^2\dashrightarrow\PP^2,\qquad
[x:y:z]\longmapsto[H_{4,1}:H_{4,2}:H_{4,3}]
\]
has image closure \(C_4(F)\).  The determinant equation implies that this
image has dimension at most one.  Subject to base-locus degeneracies, the
cases \(\rho_4=1,2,3\) correspond to point, line, and nondegenerate
rational-curve image.  We use \(\rho_4\) for exact linear algebra and
\(C_4(F)\) to organize the geometry at infinity.

Our main theorem excludes \(\rho_4(F)=1\).  The continuation in
\cref{app:quartic-frontier-and-ramification} then excludes the remaining
proper nondegenerate rational leading curves and begins the resulting
target-span-two endgame.  The further continuation in
\cref{app:quartic-high-ramification-fixed-components} closes the primitive
ramification-four/five strata and the fixed-component leaves, conditional
on the recorded upstream routing.

\begin{theorem}[One-dimensional leading target span]
\label{thm:rank-one}
Let \(F\colon\A^3_{\C}\to\A^3_{\C}\) be a Keller map of ordinary degree at
most four.  If \(\rho_4(F)=1\), then \(F\) is a polynomial automorphism.
\end{theorem}

The theorem allows arbitrary mixed quadratic and cubic layers.  It assumes
neither that \(F-X\) is homogeneous nor that its Jacobian is nilpotent.  This
distinguishes it from the homogeneous three-dimensional theorem of de
Bondt--van den Essen \cite{deBondtVanDenEssen2005}.  General invariant theory
of binary quartic pencils is classical \cite{wall1998}; our claim concerns
the restrictions imposed by the mixed homogeneous Keller equations.

Recent work restricts graded Keller maps \cite{shaska2026graded}.  We impose
no torus action.  As of July 23, 2026, we know no public theorem excluding
every ordinary-degree-four three-dimensional Keller map.

Our second theorem concerns a conic-image leading form rather than linear
target span two.

\begin{theorem}[Four reduced conic orbits]
\label{thm:conic}
Suppose a degree-four Keller map has, after independent linear source and
target changes,
\[
H_4=G(x,y,z)(x^2,xy,y^2),
\]
where \(G\) is a reduced quadratic form.  Put \(p=[0:0:1]\).  If \(p\notin
V(G)\), or if \(p\) is a nonsingular point of \(V(G)\), then no such Keller
map exists.
\end{theorem}

The final coefficient elimination in \cref{thm:conic} is computer-assisted.
The calculation keeps an arbitrary invertible linear part and never divides
by a parameter.  The exact scope is described in
\cref{sec:computation}.

\section{Keller jets at infinity}
\label{sec:jets-at-infinity}

The homogeneous determinant identities have a compact geometric source.
Define
\[
K_\epsilon(X)
=\epsilon^4F(X/\epsilon)
=H_4+\epsilon H_3+\epsilon^2H_2+\epsilon^3LX.
\]
Since \(JK_\epsilon=\epsilon^3JF(X/\epsilon)\),
\begin{equation}
\label{eq:maximal-contact}
\det JK_\epsilon=\epsilon^9\det JF.
\end{equation}
In particular, \(\det JH_4=0\).  More strongly, every coefficient below
the maximum possible order nine in the determinant arc
\[
JH_4+\epsilon JH_3+\epsilon^2JH_2+\epsilon^3L
\]
vanishes.  Thus a quartic Keller map is a maximally volume-preserving
deformation of a singular leading map at infinity.

The rank-one theorem treats the case in which \(C_4(F)\) is a point.  The
span-two reduction treats line image.  The conic theorem begins the first
nonlinear case.  This explains why the cases belong in one paper: they are
successive image geometries of the same boundary jet, rather than unrelated
coefficient ansatzes.

\begin{remark}[Determinantal arcs]
Equation \eqref{eq:maximal-contact} says that the matrix arc \(JK_\epsilon\)
has maximal contact with the determinant hypersurface in
\(\operatorname{Mat}_{3\times3}\).  Our matrices are not arbitrary arcs:
each coefficient is the Jacobian of a homogeneous polynomial map.  The
integrability constraint is what turns a coarse determinantal problem into
the pencil, coordinate, and first-integral geometry used below.
\end{remark}

\section{Two coordinate lemmas}
\label{sec:coordinates}

We work over an algebraically closed field \(k\) of characteristic
zero, as fixed in the introduction; the lemmas here are stated over
\(k\) for later reuse.

\begin{lemma}[Quadratic coordinate]
\label{lem:quadratic-coordinate}
If \(f\in k[X_1,X_2,X_3]\) has degree at most two and no critical point, then
some constant directional derivative of \(f\) is nonzero.  In particular,
\(f\) is a coordinate.
\end{lemma}

\begin{remark}[Sharpness of low-degree coordinate rigidity]
The quadratic hypothesis is essential.  The polynomial
\[
f=x+x^2y
\]
has no critical point, but its zero fiber is reducible, so it is not a
coordinate.  Likewise \(x^4+x+x^2y\) has pure-power quartic top part, no
critical point, and a reducible zero fiber.  The coordinate lemmas therefore
encode a genuine low-degree threshold rather than an unrestricted
submersion principle.
\end{remark}

\begin{proof}
Write
\[
f=\frac12X^TAX+b^TX+c
\]
with \(A\) symmetric.  If \(b\in\operatorname{im}A\), the equation
\(AX+b=0\) has a solution, contrary to the hypothesis.  Hence
\[
b\notin\operatorname{im}A=(\ker A)^\perp.
\]
There is \(u\in\ker A\) with \(b^Tu\ne0\), and \(D_uf=b^Tu\).  After making
\(u\) a coordinate direction, a triangular change replaces that coordinate
by \(f\).
\end{proof}

\begin{lemma}[Cubic-cube coordinate]
\label{lem:cubic-coordinate}
Suppose that \(\deg f\le3\), \(f\) has no critical point, and its cubic
homogeneous part is \(\lambda\ell^3\) with \(\lambda\ne0\).  Then \(f\) has
a nonzero constant directional derivative and is a coordinate.  The
straightening and its inverse can be chosen of degree at most three.
\end{lemma}

\begin{proof}
Take \(\ell=x\), write the remaining variables as \(w\in k^2\), and express
\[
\nabla_wf=Mw+ax+b
\]
with \(M\) symmetric.  Project this affine expression to
\(\operatorname{coker}M=(\ker M)^\vee\).

If it never vanishes, the two projected vectors \(a,b\) do not span an
affine line through the origin.  Hence some \(u\in\ker M\) satisfies
\(u^Ta=0\) and \(u^Tb\ne0\), so \(D_uf\) is a nonzero constant.

Otherwise fix a solution of \(Mw+ax+b=0\).  If \(a\) pairs nontrivially with
\(\ker M\), variation within the solution space makes \(f_x\) vanish.  If it
does not, then \(a\in\operatorname{im}M\); solvability for one \(x\) also
puts \(b\) in \(\operatorname{im}M\), so the system is solvable for every
\(x\).  Substitution of a linear solution \(w=w(x)\) makes \(f_x\) a
quadratic polynomial in \(x\) with leading coefficient \(3\lambda\).  It
has a root over \(k\), again producing a critical point.  Both alternatives
contradict the hypothesis, so the constant-direction case is forced.

In suitable linear coordinates \(f=cw_2+\psi(x,w_1)\), with \(c\ne0\) and
\(\deg\psi\le3\).  Replacing \(w_2\) by \(f\) gives the asserted
straightening and degree bound.
\end{proof}

\begin{proposition}[The easy transverse branches]
\label{prop:easy-branches}
In \eqref{eq:homogeneous}, suppose
\[
H_4=(0,0,h),\qquad H_3=(P,Q,R).
\]
If \(P,Q\) are linearly dependent, or if their pencil contains the cube of a
linear form, then \(F\) is an automorphism.
\end{proposition}

\begin{proof}
A row of \(JF\) cannot vanish, so every target combination of the
coordinates of \(F\) has no critical point.  In the dependent case a target
combination of the first two components has degree at most two, and
\cref{lem:quadratic-coordinate} applies.  In the cube-containing case a
combination has degree at most three with cubic part a cube, and
\cref{lem:cubic-coordinate} applies.

After straightening this component to a variable \(t\), choose the other
target combination among the first two original components.  Over
\(\overline{k(t)}\), the remaining two coordinates form a plane Keller map.
In the quadratic case one component has degree at most six.  In the cubic
case it has degree in
\[
\set{1,2,3,4,5,6,7,9}.
\]
Indeed, substituting \(w_2=c^{-1}(t-\psi)\) into a cubic gives degree at most
seven unless the \(w_2^3\) term and the cubic part of \(\psi\) are both
nonzero, in which case the unique top term has degree nine.  Every displayed
integer is a product of at most two primes, counted with multiplicity.
The corrected Appelgate--Onishi plane theorem, in the form completed by
Nagata, therefore makes the plane map an automorphism
\cite{appelgateOnishi1985,nagata1988two}.  Its inverse over
\(\overline{k(t)}\) is unique, hence fixed by every automorphism over
\(k(t)\), and therefore descends to \(k(t)\).  It follows that \(F\) is
birational over \(k\).  A birational Keller self-map is injective by
Zariski's Main Theorem and hence an automorphism by Ax--Grothendieck.
\end{proof}

\section{The rational-composite pencil lemma}
\label{sec:pencil}

The highest nonautomatic homogeneous Keller equation for the normalization
in \cref{prop:easy-branches} is
\begin{equation}
\label{eq:highest}
dP\wedge dQ\wedge dh=0.
\end{equation}
If \(P,Q\) are independent, they are algebraically independent and
\eqref{eq:highest} makes \(h\) algebraic over \(k(P,Q)\).

\begin{lemma}[Weighted one-variable field]
\label{lem:weighted-field}
Let \(P,Q\) be homogeneous forms of the same degree \(a>0\).  Write
\[
P=GA,\qquad Q=GB,\qquad \gcd(A,B)=1,
\qquad n=\deg A=\deg B,
\]
and let \(h\) be homogeneous of degree \(b>0\).  Put
\[
  \begin{aligned}
  t&=P/Q=A/B, & g&=\gcd(a,b),\\
  p&=a/g, & q&=b/g, & w&=h^p/Q^q,
  \end{aligned}
\]
and suppose that \(h\) is algebraic over \(k(P,Q)\).  Then \(w\) is
algebraic over \(k(t)\).

If \(K_1=k(t,w)\), there are coprime homogeneous forms \(A_0,B_0\) of a
common degree \(d\) and a rational function \(\mathcal R\) of degree \(e\)
such that
\[
K_1=k(A_0/B_0),\qquad t=\mathcal R(A_0/B_0),
\qquad n=ed.
\]
\end{lemma}

\begin{proof}
Choose a polynomial relation among \(P,Q,h\) and retain a nonzero
source-homogeneous part.  Every monomial \(P^iQ^jh^k\) in that part
satisfies
\[
a(i+j)+bk=M.
\]
It follows that all exponents \(k\) are congruent modulo \(p=a/g\).
After removing their common residual power of \(h\), the relation has the
form
\[
\sum_i C_i(P,Q)h^{pi}=0,
\qquad \deg C_i=N-qi
\]
for a suitable integer \(N\).  Division by \(Q^N\) gives a polynomial
relation for \(w\) over \(k(t)\).

The one-variable field \(K_1\subset k(\PP^2)\) is the function field of a
curve dominated by \(\PP^2\).  Restriction to a suitable line makes that
curve unirational, hence rational in characteristic zero.  Thus
\(K_1=k(s)\), and \(s\) can be written \(A_0/B_0\) with \(A_0,B_0\)
coprime homogeneous forms of the same degree \(d\).

Write \(\mathcal R=U/V\), where \(U,V\) are coprime binary forms of degree
\(e\).  The substituted forms \(U(A_0,B_0)\) and \(V(A_0,B_0)\) remain
coprime: their common divisor would, by the binary resultant identities,
divide powers of both \(A_0\) and \(B_0\).  Comparing degrees in the reduced
ratio \(A/B=\mathcal R(A_0/B_0)\) yields \(n=ed\).
\end{proof}

\begin{proposition}[Cubic pencils]
\label{prop:cubic-pencils}
Let \(P,Q\) be independent homogeneous cubics satisfying
\eqref{eq:highest}.  Then their pencil either contains the cube of a linear
form, or \(P,Q,h\) are polynomials in two independent linear forms.
\end{proposition}

\begin{proof}
First suppose \(\gcd(P,Q)=1\).  Apply
\cref{lem:weighted-field} directly to \(P,Q,h\).
If \(e>1\), then \(3=ed\) gives \(e=3,d=1\), so \(P,Q\) are binary in two
linear forms.

If \(e=1\), write \(w=R(t)\).  For
\(F_\xi=P-\xi Q\), let \(r_\xi=\ord_\xi R\), and set
\[
c_\xi=r_\xi+4\mathbf1_{\xi=\infty}.
\]
If an irreducible component of \(F_\xi\) has multiplicity \(m\), valuation
gives
\[
3\nu(h)=c_\xi m.
\]
Every \(c_\xi\) is nonnegative and
\[
\sum_{\xi\in\PP^1}c_\xi=4.
\]
If no fiber is a cube, every cubic fiber has a component whose multiplicity
is prime to three.  The displayed valuation then makes every \(c_\xi\) a
multiple of three, contradicting their sum.

Now write \(P=GA,Q=GB\) with \(G\ne1\) and \(\gcd(A,B)=1\).
If \(\deg G=2\), then \(A,B\) are independent linear forms.  An irreducible
factor of \(G\), of multiplicity \(m=1\) or \(2\), cannot carry a
nonconstant \(A/B\), since its valuation would give
\[
3\nu(h)=4m.
\]
Every component of \(G\) is therefore a fiber line of the pencil
\(\angles{A,B}\); hence \(G,P,Q\) are binary.

If \(G=\ell\), the reduced pencil \(A/B\) has degree two.  In the composite
case \cref{lem:weighted-field} gives \(e=2,d=1\).  The valuation along
\(\ell\) forces \(\ell\) into the same binary pencil.  In the primitive
case, the same valuation first makes \(A/B\) constant on \(\ell=0\).
After changing the pencil basis, write \(A=\ell m\).  If
\(m\) is proportional to \(\ell\), then \(P=\ell^3\).  Otherwise, with
\(r=\ord_0R\), valuations along \(m=0\) and \(\ell=0\) give
\[
3\nu_m(h)=r,\qquad 3\nu_\ell(h)=r+4,
\]
which is impossible modulo three.

Finally, if \(P,Q\) are binary in linear forms \(a,b\), then
\[
dP\wedge dQ=J_{a,b}(P,Q)\,da\wedge db
\]
with nonzero planar Jacobian.  Equation \eqref{eq:highest} forces the
derivative of \(h\) transverse to \(a,b\) to vanish, so \(h\) is binary in
the same forms.
\end{proof}

\section{Proof of the one-dimensional-span theorem}
\label{sec:rank-one-proof}

By a target change, write \(H_4=(0,0,h)\).  In the branch not already covered
by \cref{prop:easy-branches}, \cref{prop:cubic-pencils} gives coordinates
such that
\[
P,Q\in k[x,y]_3,\qquad h\in k[x,y]_4,
\]
and the pencil \(\angles{P,Q}\) contains no cube.

Put
\[
W=J(P,Q),\qquad U=J(P,h),\qquad V=J(Q,h),
\]
where \(J\) is the planar Jacobian in \(x,y\).  Write every possible
\(z\)-dependent lower term as
\begin{align}
(H_2)_1&=A_0(x,y)+za(x,y)+\alpha z^2,\nonumber\\
(H_2)_2&=B_0(x,y)+zb(x,y)+\beta z^2,\nonumber\\
(H_2)_3&=C_0(x,y)+zr(x,y)+cz^2,\label{eq:lower-terms}\\
(H_3)_3&=R_0(x,y)+zq(x,y)+z^2\ell(x,y)+\rho z^3,\nonumber
\end{align}
where \(a,b,r,\ell\) are linear and \(q\) is quadratic.

Introduce \(T\) and expand
\[
\det(L+T JH_2+T^2JH_3+T^3JH_4)
=\det L+\sum_{j=1}^7T^jE_j.
\]
In terms of \cref{sec:jets-at-infinity}, \(T\) reverses the
\(\epsilon\)-grading: \(E_j\) is the coefficient of
\(\epsilon^{9-j}\) in \(\det JK_\epsilon\) (the \(T^8,T^9\)
coefficients vanish identically here because \(JH_4\) has a single
nonzero row), and the Keller condition is exactly
\(E_1=\dots=E_7=0\).
Exact expansion gives
\begin{align}
[z^2]E_6&=3\rho W,\label{eq:id1}\\
[z]E_6&=2(W\ell+\alpha V-\beta U),\label{eq:id2}\\
[1]E_6&=Wq+Va-Ub,\label{eq:id3}\\
[z^3]E_5&=-2J(\ell,\alpha Q-\beta P),\label{eq:id4}
\end{align}
where the last three identities are read after \(\rho=0\).
After \(\alpha=\beta=\ell=\rho=0\), one also has
\begin{align}
[z]E_5={}&-4J(a,b)h-qJ(a,Q)+3QJ(a,q)\nonumber\\
&+qJ(b,P)-3PJ(b,q)+2cW,\label{eq:id5}\\
[z^2]E_4={}&-J(a,b)q+2c(J(a,Q)-J(b,P)),\label{eq:id6}\\
[z^3]E_3={}&2cJ(a,b).\label{eq:id7}
\end{align}

\begin{lemma}[First binary syzygy]
\label{lem:first-syzygy}
In the cube-free branch,
\[
\rho=\ell=\alpha=\beta=0.
\]
\end{lemma}

\begin{proof}
Equation \eqref{eq:id1} gives \(\rho=0\).  Put
\(S=\alpha Q-\beta P\).  Equations \eqref{eq:id2} and
\eqref{eq:id4} say
\[
W\ell+J(S,h)=0,\qquad J(\ell,S)=0.
\]
If \(\ell\ne0\), the second equation makes
\(S=\lambda\ell^3\).  Cube-freeness gives \(S=0\), whence
\(\alpha=\beta=0\), and the first equation becomes \(W\ell=0\), a
contradiction.

Thus \(\ell=0\), and \(J(S,h)=0\).  Algebraically dependent homogeneous
binary forms of coprime degrees three and four are powers of a common linear
form.  A nonzero \(S\) would therefore be a cube in
\(\angles{P,Q}\).  Hence \(S=0\), and independence of \(P,Q\) gives
\(\alpha=\beta=0\).
\end{proof}

\begin{lemma}[Second binary syzygy]
\label{lem:second-syzygy}
In the cube-free branch,
\[
a=b=q=c=0.
\]
\end{lemma}

\begin{proof}
Let \(D=J(a,b)\).  If \(D\ne0\), equations
\eqref{eq:id7}, \eqref{eq:id6}, and \eqref{eq:id5}, in that order, give
\(c=0,q=0,h=0\), a contradiction.  Thus \(D=0\).

If \(a=b=0\), equations \eqref{eq:id3} and \eqref{eq:id5} give
\(q=c=0\).  Otherwise a row operation on the first two target coordinates
makes \(b=0,a\ne0\).  If \(c\ne0\), \eqref{eq:id6} makes
\(J(a,Q)=0\), so \(Q\) is a cube.  Hence \(c=0\).

Equation \eqref{eq:id5} is now
\[
-qJ(a,Q)+3QJ(a,q)=0.
\]
If \(q=0\), equation \eqref{eq:id3} gives \(J(Q,h)=0\), again making
\(Q\) a cube.  Otherwise take \(a=x\); then
\[
qQ_y-3Qq_y=0,
\qquad
\partial_y(Q/q^3)=0.
\]
Homogeneity gives \(x^3Q=\lambda q^3\).  Unique factorization makes \(Q\)
a cube, the final contradiction.
\end{proof}

\begin{proof}[Proof of \cref{thm:rank-one}]
The two syzygy lemmas reduce the map to
\[
F_1=f_1(x,y)+\gamma z,\qquad
F_2=f_2(x,y)+\phi z,\qquad
F_3=f_3(x,y)+(\mu+r(x,y))z,
\]
with \(r\) linear.  The coefficient of \(z\) in the determinant is
\[
J(r,\phi f_1-\gamma f_2).
\]
If \((\gamma,\phi)\ne(0,0)\) and \(r\ne0\), its vanishing makes the
nonzero cubic \(\phi P-\gamma Q\) a polynomial in the single linear form
\(r\), hence a cube.  Therefore \(r=0\).  A target linear change sends the
nonzero vector \((\gamma,\phi,\mu)\) to \(e_3\), and the map becomes
\[
(G_1(x,y),G_2(x,y),z+G_3(x,y)).
\]
The plane pair is Keller and one coordinate has degree at most four, so
\cite{appelgateOnishi1985} makes it an automorphism.

If \(\gamma=\phi=0\), then
\[
\det JF=J(f_1,f_2)(\mu+r).
\]
Both factors are units, so \(r=0\), and the same triangular conclusion
holds.
\end{proof}

\section{A leading-target-span-two reduction}
\label{sec:span-two}

The strata of this section and of the appendices are organized by the
following factorization, which promotes the register entry
\hyperref[supp-note-02-010]{supp-note 02-010} to a proved statement.

\begin{lemma}[Leading-image factorization]
\label{lem:leading-image}
Suppose \(H_4\ne0\) and the image closure \(C_4(F)\) is a curve of
degree \(e\ge1\).  Then there are coprime forms \(A,B\) of a common
degree \(k\ge1\), binary forms \(h=(h_0,h_1,h_2)\) of degree \(e\)
with no common root giving a proper parametrization of \(C_4(F)\), and a
form \(G\), such that
\[
H_4=G\cdot h(A,B),\qquad \deg G+ek=4.
\]
The possible leaves with a nondegenerate image are
\[
(e,k,\deg G)\in\{(2,1,2),\ (2,2,0),\ (3,1,1),\ (4,1,0)\},
\]
and \(e=1\) is the leading-target-span-two locus.
\end{lemma}

\begin{proof}
Let \(K\) be the relative algebraic closure of
\(\phi_4^*k(C_4(F))\) in \(k(\PP^2)\).  It has transcendence degree
one and is unirational, hence rational by L\"uroth: \(K=k(A/B)\) with
\(A,B\) coprime forms of a common degree \(k\).  The ratios
\(H_{4,i}/H_{4,j}\) lie in \(K\), so
\([H_{4,1}:H_{4,2}:H_{4,3}]=[h_0(A,B):h_1(A,B):h_2(A,B)]\) for binary
forms \(h_i\) without common root, and the induced map
\(\PP^1\to C_4(F)\) is birational because \(K\) is relatively
algebraically closed; hence the parametrization is proper and
\(e=\deg C_4(F)\).  The substituted forms \(h_i(A,B)\) have no common
factor: a common root of the \(h_i\) does not exist, so a common factor
would force the coprime pencil \((A,B)\) to have a base divisor.  Hence
\(G=\gcd(H_{4,1},H_{4,2},H_{4,3})\) satisfies
\(H_{4,i}=G\,h_i(A,B)\) up to one common scalar, and the degree
relation follows.
\end{proof}

For context, suppose instead that
\[
H_4=(P,Q,0)
\]
with \(P,Q\) algebraically independent quartics, and let \(R\) be the third
cubic component of \(H_3\).  The highest Keller equation is
\[
\operatorname{Jac}(P,Q,R)=0.
\]
Write \(P=GA,Q=GB\), with \(\gcd(A,B)=1\), and set
\[
n=\deg A=\deg B=4-\deg G,\qquad
t=A/B,\qquad w=R^4/Q^3.
\]
The proof of \cref{lem:weighted-field}, with weights \(4,4,3\), gives a
rational intermediate field and a factorization \(n=ed\).

Assume \(R\ne0\) here and for \cref{prop:four-loci}; the vanishing
case is \cref{rem:r-zero}.  Here and below, a reduced pencil \(A/B\) is
\emph{composition-primitive} if this factorization has \(e=1\).  This is
distinct both from coprimality of \(A,B\) and from the period-primitivity
used for homogeneous invariant fields.

\begin{proposition}[Four structural loci]
\label{prop:four-loci}
Every such leading pair belongs to at least one of the following loci:
\begin{enumerate}[label=(\roman*)]
\item a binary quartic pencil, with \(R\) binary in the same two linear
forms;
\item a quadratic-source pencil
\[
P=U(a_2,b_2),\qquad Q=V(a_2,b_2),
\]
where \(a_2,b_2\) are coprime quadrics and \(U,V\) are binary quadratics;
\item a composition-primitive coprime pencil containing a fourth power
\(\ell^4\);
\item a composition-primitive reduced pencil \(A/B\) with a nontrivial
common factor \(G\), every irreducible component of \(G\) not already binary
being supported on a special fiber of \(A/B\).
\end{enumerate}
The loci need not be disjoint.
\end{proposition}

\begin{proof}
If the intermediate extension has degree \(e>1\), the possibilities
\(n=ed\) are
\[
\begin{array}{c|c|c}
\deg G&n&(e,d)\\ \hline
0&4&(4,1),(2,2)\\
1&3&(3,1)\\
2&2&(2,1).
\end{array}
\]
The \(d=1\) cases are binary after valuation along every component of \(G\);
the only nonbinary composite case is \((e,d)=(2,2)\).

In the composition-primitive coprime case \(w=\rho(t)\).  If a component of
multiplicity \(m\) lies in the fiber \(P-\xi Q\), then
\[
4\nu(R)=c_\xi m,\qquad c_\xi\ge0,\qquad
\sum_{\xi\in\PP^1}c_\xi=3,
\]
with the denominator contribution incorporated at infinity.  Some
\(c_\xi\) is odd, so every component multiplicity in that fiber is divisible
by four.  The quartic fiber is therefore \(\ell^4\).  With fixed
components, the same valuation argument places every component not already
binary over a special fiber, giving (iv).
\end{proof}

\begin{remark}[The vanishing-\(R\) leaf]
\label{rem:r-zero}
If \(R=0\), the equation \(\operatorname{Jac}(P,Q,R)=0\) is vacuous.
The determinant arc supplies the replacement: the third rows of
\(JH_3\) and \(JH_4\) then vanish, so the top surviving
\(T\)-coefficient is
\(E_7=\operatorname{Jac}(P,Q,(H_2)_3)=0\); if \((H_2)_3=0\) as well,
\(E_6=\operatorname{Jac}(P,Q,(LX)_3)=0\); and if the entire third
component were constant, the third row of \(JF\) would vanish against
the Keller condition.  Thus \cref{lem:weighted-field} applies with
\(b=2\) or \(b=1\) in place of \(b=3\).  The register entry
\hyperref[supp-note-02-016]{supp-note 02-016} records the resolution:
a first normal layer of degree one or two makes a coordinate linear or
quadratic and reduces the map to an excluded low-degree plane Keller
map.  That entry is proof-offered research-lead evidence, not a
reader-manuscript theorem; it is part of the routing audit below.
\end{remark}

\begin{remark}
\Cref{prop:four-loci} is a structural reduction, not an exclusion theorem.
Its relation to the classical stratification of binary quartic pencils
\cite{wall1998} is that the Keller equation supplies the cubic \(R\) and the
valuation restrictions; it does not make the ambient pencil theory new.
\end{remark}

\section{The four reduced conic orbits}
\label{sec:conic}

We now turn to the separate conic-image form
\begin{equation}
\label{eq:conic-form}
H_4=G(x,y,z)(x^2,xy,y^2).
\end{equation}
Put \(p=[0:0:1]\).

\begin{lemma}[Parabolic orbit list]
\label{lem:orbits}
Up to a source transformation fixing \(p\) and rescaling \(G\), the seven
orbits of pairs consisting of a plane conic and \(p\) have representatives
\[
\begin{array}{c|c}
\text{geometry}&G\\ \hline
\text{smooth, }p\notin V(G)&z^2+xy\\
\text{smooth, }p\in V(G)&xz+y^2\\
\text{two lines, }p\notin V(G)&z^2+x^2\\
\text{two lines, }p\text{ nonsingular on the union}&xz\\
\text{two lines, }p\text{ the node}&xy\\
\text{double line, }p\notin V(G)&z^2\\
\text{double line, }p\in V(G)&x^2.
\end{array}
\]
\end{lemma}

\begin{proof}
The subgroup preserving the pencil \(\angles{x,y}\) is the projective
stabilizer of \(p\).  Over \(\C\), plane conics are classified by rank.
For rank three, the stabilizer is transitive on points on the conic and on
points off it.  For rank two, a point is off the union, on exactly one
component, or at the node.  For rank one, it is on or off the doubled line.
Elementary linear changes give the displayed representatives.
\end{proof}

For \eqref{eq:conic-form}, define
\[
\delta_G=xG_z\partial_x+yG_z\partial_y+(zG_z-4G)\partial_z.
\]
This is a right-kernel derivation for \(JH_4\).  Let
\[
n=(y^2,-2xy,x^2)^T.
\]
Then \(n\) is a left-kernel vector, and
\[
\delta_G(n)=2G_z n.
\]

\begin{lemma}[Invariant fields]
\label{lem:invariants}
For each of
\[
G=z^2+xy,\quad xz+y^2,\quad z^2+x^2,\quad xz,
\]
one has
\[
\ker_{\C(x,y,z)}\delta_G
=\C\left(\frac{x}{y},Gy^2\right).
\]
Consequently a homogeneous invariant rational function has scalar degree
divisible by four.
\end{lemma}

\begin{proof}
Put \(r=x/y\) and \(s=Gy^2\).  Direct differentiation gives
\(\delta_G(r)=\delta_G(s)=0\).

For \(G=xz+\epsilon y^2\), the full field is
\(\C(r,s)(y)\), since
\[
z=\frac{s-\epsilon y^4}{ry^3}.
\]
The induced nonzero derivation on this one-variable rational field has
constant field \(\C(r,s)\).

For \(G=z^2+xy\) and \(z^2+x^2\), put \(w=yz\).  Over
\(\C(r,s)\), the full field is the function field of
\[
w^2+r y^4=s
\quad\text{or}\quad
w^2+r^2y^4=s.
\]
Each generic curve is geometrically integral.  Thus \(\C(r,s)\) is
relatively algebraically closed in the one-variable function field, and a
nonzero \(\C(r,s)\)-derivation has no further constants.

Under scalar dilation, \(r\) has degree zero and \(s\) degree four.  The
rational eigenvectors in \(\C(r,s)\) therefore have degrees in
\(4\mathbb Z\).
\end{proof}

Write \(H_3=(P,Q,R)\) and \(M=n\cdot H_3\).  The first normal Keller
equation is
\[
n^TJH_3\,\delta_G=0,
\]
or
\[
\delta_G(M)=2G_zM.
\]
Hence \(M/y^2\) is invariant of degree three.  By
\cref{lem:invariants}, \(M=0\), and the syzygies of
\((y^2,-2xy,x^2)\) give
\begin{equation}
\label{eq:TAB}
H_3=T(A,B):=(2xA,yA+xB,2yB)
\end{equation}
for quadratic forms \(A,B\).

Introduce
\[
K_\epsilon=H_4+\epsilon H_3+\epsilon^2H_2+\epsilon^3LX,
\qquad
\Phi(Y)=Y_1Y_3-Y_2^2.
\]
The chain rule gives
\begin{equation}
\label{eq:chain}
\operatorname{Jac}(K_{\epsilon,1},K_{\epsilon,2},
\Phi(K_\epsilon))
=K_{\epsilon,1}\det JK_\epsilon.
\end{equation}
For a Keller map,
\[
\det JK_\epsilon=\epsilon^9\det L.
\]
Write
\[
\Phi(K_\epsilon)=
\epsilon^2S_2+\epsilon^3S_3+\epsilon^4S_4+
\epsilon^5S_5+\epsilon^6S_6.
\]
The first two coefficients of \eqref{eq:chain} make \(S_2,S_3\)
\(\delta_G\)-invariant.  Their degrees are six and five, so
\cref{lem:invariants} gives
\[
S_2=S_3=0.
\]

Now
\[
S_2=G\,n\cdot H_2-(yA-xB)^2.
\]
Since \(G\) is squarefree,
\begin{equation}
\label{eq:divisibility}
yA-xB=G\ell,\qquad n\cdot H_2=G\ell^2
\end{equation}
for a linear form \(\ell\).  In fact \(\ell\in(x,y)\).  For
\(G=z^2+xy\) or \(z^2+x^2\), reduce the first identity modulo
\((x,y)\): since \(yA-xB\in(x,y)\), one obtains
\(z^2\overline{\ell}=0\) in \(k[z]\).  For \(G=xz+y^2\) or \(xz\), use
the second identity: \(n\cdot H_2\in(x,y)^2\), whereas \(G\) has
\((x,y)\)-order one, so \(\ell\notin(x,y)\) would make
\(G\ell^2\) have order one.  Thus in every case
\(\ell=ax+by\).  Every solution of the second equation is
\[
H_2=G(b^2,-ab,a^2)+T(U,V),
\]
where \(U,V\) are linear.  The first equation has the exhaustive solutions
\[
\begin{array}{c|c|c}
G&A&B\\ \hline
z^2+xy&xC+ax^2+bz^2&yC-az^2-by^2\\
xz+y^2&xC+axy+bG&yC-axz\\
z^2+x^2&xC+bG&yC-aG\\
xz&xC+bG&yC-aG,
\end{array}
\]
with \(C\) linear.

\begin{proposition}[Exact terminal elimination]
\label{prop:terminal-conic}
For each of the four displayed \(G\), the equations
\[
S_3=0,\qquad \delta_G(S_4)=0
\]
and one further coefficient of \eqref{eq:chain} force \(\det L=0\).
\end{proposition}

\begin{proof}[Computer-assisted proof]
Substitute the preceding parametrizations and retain all nine entries of
\(L\).  Solving the linear equation \(S_3=0\) leaves two entries of \(L\)
free.  The coefficients of \(\delta_G(S_4)=0\) are then solved without
inverting a parameter.  The orbit \(G=xz+y^2\) has the exhaustive split
\[
a=0\qquad\text{or}\qquad [z]C=[x]C.
\]
In the resulting five charts, the next nonzero coefficient and the
determinant have the form
\[
\begin{array}{c|c|c}
G&\text{required zero coefficient}&\det L\\ \hline
z^2+xy&
x^2zG(A_0x+2B_0y)^2&
c_2(-bA_0+2aB_0)^2\\
xz+y^2,\ c_2=c_0&
\frac12x^3G(A_0x-2my)^2&
c_2(bA_0+2am)^2\\
xz+y^2,\ a=0&
\frac12x^3G(nx+(4b^2(c_2-c_0)-2m)y)^2&
b^2c_2n^2\\
z^2+x^2&
x^2zG(A_0x+B_0y)^2&
c_2(bA_0-aB_0)^2\\
xz&
\frac12x^3G(A_0x+B_0y)^2&
c_2(bA_0-aB_0)^2.
\end{array}
\]
Here the displayed letters are the residual scalar parameters after the
linear solves.  In every row, vanishing of the middle polynomial forces the
squared linear form to vanish coefficientwise, and the last column then
vanishes.

The accompanying assertion-based checker constructs the parametrizations,
performs the linear solves, verifies the exhaustive branch equation, expands
\eqref{eq:chain}, and asserts each factorization exactly over \(\mathbb Q\).
The evidence boundary is stated in
\cref{sec:computation}.
\end{proof}

\begin{proof}[Proof of \cref{thm:conic}]
\Cref{lem:orbits} reduces the hypothesis to the four forms treated in
\cref{prop:terminal-conic}.  That proposition contradicts the required
invertibility of \(L\).
\end{proof}

\begin{remark}[The three untreated conic orbits]
The remaining representatives are
\[
G=xy,\qquad G=z^2,\qquad G=x^2.
\]
For \(G=xy\) and \(G=x^2\), the characteristic derivation has odd-degree
polynomial invariants, so the first normal deformation need not vanish.  For
\(G=z^2\), degree-six invariants survive, so \(S_2\) need not vanish.
The proof above does not specialize to these cases.
\end{remark}

\section{Why the degree-seven example escapes}
\label{sec:degree-seven-escape}

The public degree-seven map has a rank-one top layer, so it is important to
say exactly why \cref{thm:rank-one} does not continue formally to degree
seven.  In the displayed coordinates, one transverse component is
\[
R=2x-3x^2y-x^3z=x(2-3xy-x^2z).
\]
It is a polynomial submersion:
\[
R_y=-3x^2,\qquad R_z=-x^3,
\]
so a critical point would have \(x=0\), where \(R_x=2\).  Nevertheless
\(R\) is not a coordinate, because the fiber \(R^{-1}(0)\) is reducible.

In ordinary degree four, the dependent transverse branch in the rank-one
argument produces a quadratic polynomial submersion, and
\cref{lem:quadratic-coordinate} forces it to be a coordinate.  The known
counterexample reaches a quartic submersion that is smooth but globally
nontrivial.  Thus the degree gap is not an artifact of the proof:
low-degree differential regularity still forces algebraic triviality,
whereas degree seven has enough room for nontrivial behavior at infinity.

\section{Exact computations and remaining proof obligations}
\label{sec:computation}

The recovered supplement contains one universal rank-one script and nine
conic-orbit scripts.  All ten programs were rerun with Python 3.12.11 and
SymPy 1.14.0.  Every new log is byte-for-byte identical to the stored output.
The reviewed copies, stored outputs, and integrity manifests are in
\texttt{code/rank-one/} and \texttt{code/recovered-conic/}.

For the conic theorem, the standalone checker
\begin{center}
\texttt{code/verify\_conic\_certificates.py}
\end{center}
reconstructs the five terminal charts from the normal equations.  It asserts
the cubic and quadratic normal forms, \(S_2=S_3=0\),
\(\delta_G(S_4)=0\), the set-theoretically exhaustive split \(a=0\) or
\([z]C=[x]C\), and all five pairs of factorizations in
\cref{prop:terminal-conic}.  It uses exact rational arithmetic, makes no
random specializations, and divides by no parameter.

The rank-one script keeps arbitrary binary cubics \(P,Q\), an arbitrary
binary quartic \(h\), every lower term in \eqref{eq:lower-terms}, and an
arbitrary \(3\times3\) linear part.  It asserts
\eqref{eq:id1}--\eqref{eq:id7} and the terminal determinant identity.
It does not prove
\cref{lem:cubic-coordinate,lem:weighted-field,prop:cubic-pencils}.

The bounded equivariant calculation has a separate source directory.  Its
core scripts recompute the degree-four, degree-five, and degree-six
eliminations over \(\mathbb Q\), together with the exact target-orbit minor.
Exploratory finite-field searches are kept in a visibly separate subdirectory
and are not used as characteristic-zero nonexistence proofs.  The computation
index records which script supports each computer-assisted step.

The continuation supplement
\begin{center}
\texttt{code/program-2-2026-07-27-v1/}
\end{center}
contains five proof bundles and eight exact checkers.  They cover the
rational-quartic frontier, the fixed-component Pl\"ucker chart, regular
binary pencils, nine quadratic-source charts, simple ramification, and
degree-two ramification.  All eight scripts were source-reviewed and rerun
successfully.  The rational-quartic and Pl\"ucker calculations each have a
second implementation using only standard-library sparse polynomial
arithmetic.  The file \texttt{SHA256SUMS} pins every imported source.

The later degree-three \(F_4\) calculation has no attached complete checker.
Accordingly, \cref{app:quartic-frontier-and-ramification} records the proved
generic reduction and the remaining compatibility equation, but does not
state a complete degree-three theorem.

The July 29 continuation supplement
\begin{center}
\texttt{code/program-2-2026-07-29-v2/}
\end{center}
contains the proof packets for high ramification, zero minors, fourth powers,
and fixed components.  Every standalone exact program was reviewed and replayed.
The quadratic fixed-factor archive matched its internal hash manifest, and
all 38 replay groups passed from a fresh copy.  These replays certify the
encoded identities and finite charts.  They do not certify the
leading-curve/four-loci case tree or map every proof chart to a program.

The checker makes the computational implication in
\cref{prop:terminal-conic} explicit.  It does not certify
\cref{lem:orbits,lem:invariants}; those are conventional arguments in the
manuscript.  A submission release therefore requires:

\begin{enumerate}[label=(\arabic*)]
\item an independent audit of the rational-composite-pencil argument;
\item a second check of the parabolic orbit list and invariant fields; and
\item specialist review of the computer-assisted implication in
\cref{prop:terminal-conic}; and
\item verification that the cited Appelgate--Onishi/Nagata plane theorem
holds in the per-polynomial form used in \cref{prop:easy-branches},
where the degree bound in \(\{1,\dots,7,9\}\) is imposed on a single
plane coordinate.  (The other invocation, in the proof of
\cref{thm:rank-one}, bounds both coordinates by four and is insensitive
to the citation form.)
\end{enumerate}

\section{Open degree-four strata}
\label{sec:open-degree-four}

\Cref{cor:quartic-target-span-two} shows that an ordinary-degree-four
counterexample must have leading target span exactly two.  Its proof
routes through the leaf table of \cref{lem:leading-image}; the following
accounting records which result closes each leaf and at what evidence
level.

\begin{remark}[Leading-image leaf accounting]
\label{rem:leaf-accounting}
\begin{enumerate}[label=(\alph*)]
\item Point image: \cref{thm:rank-one} (reader-manuscript theorem).
\item Leaf \((2,1,2)\), \(G\) reduced with \(p\) off the node:
\cref{thm:conic} (computer-assisted, checker attached).  Orbits
\(G=xy,x^2\): \hyperref[supp-note-02-020]{supp-note 02-020}
(certificate offered); orbit \(G=z^2\):
\hyperref[supp-note-02-018]{supp-note 02-018} (certificate offered).
\item Leaf \((2,2,0)\):
\hyperref[supp-note-02-019]{supp-note 02-019} (proof offered).
\item Leaf \((3,1,1)\):
\hyperref[supp-note-02-022]{supp-note 02-022} (certificate offered).
\item Leaf \((4,1,0)\): the frontier pre-classification is
\hyperref[supp-note-02-023]{supp-notes 02-023}--026 (proof offered), and
the surviving strata are closed by
\cref{thm:rational-quartic-frontier-exclusion} (computer-assisted).
\item Vanishing \(R\) within the span-two locus: \cref{rem:r-zero}
and \hyperref[supp-note-02-016]{supp-note 02-016} (proof offered).
\end{enumerate}
Register entries are recorded evidence, not reader-manuscript theorems;
promoting (b)--(f) to audited theorems is part of the global routing
audit below.
\end{remark}
\Cref{thm:target-span-two-ramification-two} eliminates the genuinely
nonbinary quadratic-source locus and the coprime binary locus through two
units of common ramification.  Subject to the upstream routing,
\cref{thm:quartic-high-ramification,thm:quartic-nonbinary-fixed-components,thm:quartic-binary-fixed-factors}
also close ramification degrees four and five and all fixed-factor degrees.
These results do not settle ordinary degree four.  The remaining work is:

\begin{itemize}
\item the explicit exceptional degree-three weighted-inflection
compatibility problem described at the end of
\cref{app:quartic-frontier-and-ramification}; and
\item a global audit that the leading-curve and four-loci reductions route
every quartic map into the recorded terminal charts.
\end{itemize}

The natural next calculation is the extension-field \(D_6\)-to-\(D_5\)
compatibility check on the remaining \(F_4\) family.  Even if that
calculation closes, the global audit and independent proof review remain
necessary before claiming \(D_{\min}\ge5\).

\appendix
\input{appendices/quartic-frontier-and-ramification}
\input{appendices/quartic-high-ramification-and-fixed-components}
\input{appendices/degree-five-six-fixed-factor}
\input{appendices/bounded-and-equivariant}
\input{../common/companion-register-note}

\section*{Acknowledgments and disclosure}

The discovery attribution for the counterexample is recorded in the
introduction. The author credits Angelo Vistoli, Harry Appelgate, Hironori
Onishi, Masayoshi Nagata, Michiel de Bondt, Arno van den Essen, and
C. T. C. Wall for the prior results used to delimit and prove the statements
above.

AI systems were used extensively for exploration, proof drafting, symbolic
code, literature triage, and manuscript editing.  They are not authors.  The
human author is responsible for every mathematical claim.  Exact symbolic
checks are identified in \cref{sec:computation}; they do not replace review
of the geometric reductions.

\bibliographystyle{alpha}
\bibliography{../common/references}

\end{document}
~~~

[Back to the text-source index](../index.md)
