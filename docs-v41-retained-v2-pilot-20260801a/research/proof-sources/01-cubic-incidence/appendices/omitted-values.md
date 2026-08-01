---
title: "Text proof source — 01-cubic-incidence/appendices/omitted-values.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/01-cubic-incidence/appendices/omitted-values.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `86c992f926e2502e56b1541ff80febd88b0ffcd9819924e5cd66b77f9f403d7d` · 4,476 bytes

## Exact label anchors

<a id="label-app-omitted-values"></a>
- `app:omitted-values` — source line 2
<a id="label-thm-omitted-singular"></a>
- `thm:omitted-singular` — source line 21
<a id="label-cor-smooth-nonproper-surjective"></a>
- `cor:smooth-nonproper-surjective` — source line 86

## Complete source

~~~tex
\section{Omitted values and the singular nonproperness locus}
\label{app:omitted-values}

This appendix records a general consequence that arose from the cubic
incidence calculation but does not depend on generic degree three.  The proof
below makes explicit the two geometric inputs used in earlier versions:
purity of the boundary of a dense affine open and the tame local form along a
regular branch divisor.

Let
\[
F\colon X=\A^n_{\C}\longrightarrow Y=\A^n_{\C}
\]
be a Keller map.  Write
\[
O_F=Y\setminus F(X)
\]
and let \(S_F\) be the nonproperness set, with its reduced structure.

\begin{theorem}[Omitted values are singular]
\label{thm:omitted-singular}
For every complex polynomial Keller map,
\[
O_F\subseteq\Sing(S_F).
\]
\end{theorem}

\begin{proof}
The map \(F\) is étale and hence open, so \(O_F\) is closed.  It has
codimension at least two.  Indeed, if an irreducible divisor
\(V(h)\subset Y\) were contained in \(O_F\), then \(h\circ F\) would be a
nowhere-zero polynomial on affine space and hence a nonzero constant.
Dominance makes \(F^*\) injective, forcing \(h\) itself to be constant.

Let
\[
\pi\colon\widetilde X\longrightarrow Y
\]
be the normalization of \(Y\) in \(\C(X)\).  Zariski's Main Theorem factors
\(F\) as an open immersion \(j\colon X\hookrightarrow\widetilde X\) followed
by the finite map \(\pi\).  Put \(D=\widetilde X\setminus X\).  Every
irreducible component of \(D\) has codimension one: this is the purity of the
complement of a dense affine open in a separated locally Noetherian scheme
(Stacks Project, Lemma 31.17.5, Tag
\href{https://stacks.math.columbia.edu/tag/0BCQ}{0BCQ}).  Moreover
\[
S_F=\pi(D).
\]

Take \(y\in S_F^{\mathrm{reg}}\).  After shrinking around \(y\), the reduced
nonproperness set is a regular effective Cartier divisor \(V(f)\).  Over its
complement the finite normalization equals \(X\), so it is a finite
étale cover.  Characteristic zero makes every codimension-one
ramification index tame.  Abhyankar's lemma for a regular divisor (Stacks
Project, Lemma 58.31.5, Tag
\href{https://stacks.math.columbia.edu/tag/0EYG}{0EYG}) therefore gives, after
an étale base change \(\Spec A\to Y\), a disjoint union of standard
normalizations
\[
\Spec A[u_i]/(u_i^{e_i}-f)\longrightarrow\Spec A,
\]
The unique prime divisor over \(V(f)\) in the \(i\)-th piece is
\(E_i=V(u_i)\).

If \(e_i>1\), then \(E_i\) is ramified for \(\pi\), so its generic point
cannot lie in \(X\): otherwise the restriction \(F=\pi|_X\) would ramify.
Thus every ramified \(E_i\) is a boundary component.  Conversely, after
shrinking once more, purity of \(D\) implies that the boundary in each
standard piece is either all of \(E_i\) or none of it.  There is no additional
codimension-two deletion on a retained \(E_i\), because every boundary
divisor in this neighborhood maps into \(V(f)\), and \(E_i\) is the unique
prime over \(f\) in its piece.

Not all \(E_i\) can be deleted.  If they were, an étale-open dense
subset of the divisor \(V(f)\) would be omitted, contradicting
\(\operatorname{codim}O_F\ge2\).  Hence some \(E_i\) is retained.  It must
have \(e_i=1\), and then its point over the chosen lift of \(y\) lies in the
base change of \(X\).  Existence of that point descends through the
surjective étale neighborhood, so \(y\in F(X)\).

Thus every smooth point of \(S_F\) belongs to the image, which is equivalent
to \(O_F\subseteq\Sing(S_F)\).
\end{proof}

\begin{corollary}
\label{cor:smooth-nonproper-surjective}
If \(S_F\) is smooth, then \(F\) is surjective.
\end{corollary}

\begin{proof}
The singular locus is empty, so \cref{thm:omitted-singular} gives
\(O_F=\varnothing\).
\end{proof}

For the normalized cubic family of this paper, singularity is visible
directly.  At any \(c_0\) with \(A(c_0)\ne0\), the cubic
\[
P_{a,b,c_0}(T)=A(c_0)T^3+B(c_0)T^2+bT-2a
\]
has a unique triple-root specialization
\[
t_0=-\frac{B(c_0)}{3A(c_0)},\qquad
b_0=\frac{B(c_0)^2}{3A(c_0)},\qquad
a_0=-\frac{B(c_0)^3}{54A(c_0)^2}.
\]
After translating \(T=t_0+W\), the local discriminant is the cusp
\(-4p^3-27q^2\).  Consequently the reduced nonproperness hypersurface of
every admissible member of the \(A,B\) family is singular along its
triple-root curve.

\begin{remark}[Scope]
The theorem concerns the reduced nonproperness set, not the critical-value
locus: a Keller map has no critical points.  The local input is now stated
precisely, but the theorem should still be read independently of any priority
claim.
\end{remark}
~~~

[Back to the text-source index](../../index.md)
