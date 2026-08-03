---
title: "Text proof source — 03-local-rigidity/appendices/degree-eight.tex"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/03-local-rigidity/appendices/degree-eight.tex`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `b2659948aa902d287701c53ca4a744fcfe09b0455d699e651c6860dde092a20b` · 5,433 bytes

## Exact label anchors

<a id="label-app-degree-eight"></a>
- `app:degree-eight` — source line 2
<a id="label-prop-quadratic-shears"></a>
- `prop:quadratic-shears` — source line 22
<a id="label-thm-shear-classification"></a>
- `thm:shear-classification` — source line 57
<a id="label-thm-degree-eight-transverse"></a>
- `thm:degree-eight-transverse` — source line 117

## Complete source

~~~tex
\section{The first degree-eight families}
\label{app:degree-eight}

The degree-seven theorem in the body is sharp as a statement about reduced
affine rigidity.  This appendix records what happens when the degree bound is
raised by one.  The explicit family is an exact theorem.  The final residual
calculation is reported with its mixed exact and modular evidentiary status.

\subsection{A three-parameter shear family}

For a polynomial \(f\in\C[x,y]\), let
\[
\phi_f(x,y,z)=(x,y,z+f(x,y))
\qquad\text{and}\qquad
G_f=G\circ\phi_f.
\]
The map \(\phi_f\) is a polynomial automorphism with Jacobian determinant
one.  Hence every \(G_f\) is a Keller map and has the same generic degree and
the same failure of injectivity as \(G\).

\begin{proposition}[Quadratic shear family]
\label{prop:quadratic-shears}
If \(f\) is a nonzero homogeneous quadratic, then \(G_f\) has ordinary degree
eight.  More explicitly,
\[
G_f
=G+f\left(-\frac{x^3}{2},\,
          3x(1+xy)^2,\,
          (1+xy)^3\right),
\]
and its degree-eight homogeneous part is
\[
\bigl(0,0,x^3y^3f(x,y)\bigr).
\]
In particular, \(G_f\) is not affinely equivalent to the degree-seven map
\(G\).
\end{proposition}

\begin{proof}
Only the variable \(z\) is changed.  Substitution into the three formulas
\eqref{eq:P}--\eqref{eq:R}, followed by the normalization
\eqref{eq:G}, gives the displayed identity.  If \(f\) is quadratic, the only
term of degree eight is \(x^3y^3f\) in the final coordinate.  Affine
left--right equivalence preserves ordinary degree.
\end{proof}

The stabilizer torus \eqref{eq:torus} acts on the space
\[
\Sym^2\angles{x,y}
=\angles{x^2,xy,y^2}
\]
with weights \(4,2,0\) after the common normalization induced by the
\(z\)-shear.  The following statement classifies the displayed family; it
does not classify the full degree-eight Keller germ.

\begin{theorem}[Affine classification inside the shear family]
\label{thm:shear-classification}
For nonzero homogeneous quadratics \(f,g\),
\[
G_f\sim_{\mathrm{aff}}G_g
\quad\Longleftrightarrow\quad
g(x,y)=\tau^2f(\tau x,\tau^{-1}y)
\quad\text{for some }\tau\in\C^\times .
\]
Consequently the generic affine quotient of the three-parameter quadratic
shear family has dimension two.
\end{theorem}

\begin{proof}
The displayed change of \(f\) is induced by the stabilizer
\eqref{eq:torus}, so it gives affine equivalence.  Conversely, suppose
affine automorphisms \(\alpha\) of the source and \(\beta\) of the target
satisfy
\[
G_f\circ\alpha=\beta\circ G_g.
\]
The maps \(G_f\), \(G_g\), and \(G\) have the same image and omitted curve
\(\Gamma\), because \(\phi_f\) and \(\phi_g\) are source automorphisms.
Hence \(\beta(\Gamma)=\Gamma\).  The target part of
\cref{prop:stabilizer} gives \(\beta=A_\mu\) for some \(\mu\in\C^\times\).
Using equivariance,
\[
G\circ\phi_f\circ\alpha=G\circ A_\mu\circ\phi_g.
\]
The generic cubic extension of \(G\) has trivial deck group by
\cref{prop:stabilizer}, so
\[
\phi_f\circ\alpha=A_\mu\circ\phi_g.
\]
Consequently
\[
\alpha(x,y,z)=
\left(\mu^{-1}x,\mu y,
\mu^2z+\mu^2g(x,y)-f(\mu^{-1}x,\mu y)\right).
\]
The last two terms are homogeneous quadratic, so \(\alpha\) is affine
exactly when
\[
\mu^2g(x,y)=f(\mu^{-1}x,\mu y).
\]
Putting \(\tau=\mu^{-1}\) gives the displayed action.  Conversely, this
identity makes the source lift affine and gives the required equivalence.
On the coefficient basis \((x^2,xy,y^2)\), the torus weights are
\((4,2,0)\), so the generic orbit is one-dimensional and the generic
quotient is two-dimensional.
\end{proof}

\subsection{What remains after known shears}

The unrestricted formally \'{e}tale lifting principle does not disappear in
degree eight: it produces many formal coordinate directions.  After
removing the affine orbit and the explicit source and target shear
directions, the recovered exact calculation leaves a \(28\)-variable
residual Kuranishi problem.  Its only tangent weights are \(-2\) and \(-1\).

\begin{proposition}[Current residual evidence boundary]
\label{thm:degree-eight-transverse}
In the named \(28\)-variable residual Kuranishi calculation, only tangent
weights \(-2\) and \(-1\) occur.  In weight \(-2\), exact rational
elimination yields at successive orders the
incompatible conditions
\[
u_0u_1=0,\qquad 100u_0u_1+9=0.
\]
Thus no nonzero weight-\(-2\) initial direction lifts.  The weight \(-1\)
sector survives through parameter order four over \(\mathbb Q\).  Later
death calculations are modular evidence only: they do not establish over
characteristic zero that every first-normal direction is obstructed, and
they do not prove that the reduced residual germ is the union of the known
affine, source-shear, and target-shear components.
\end{proposition}

\begin{question}
Is the radical of the completed residual ideal exactly the union of the
known affine, source-shear, and target-shear components?  This requires a
characteristic-zero treatment of the surviving weight-\(-1\) sector,
including branches tangent to a known component before leaving it.
\end{question}

\begin{remark}[Scope]
\Cref{prop:quadratic-shears,thm:shear-classification} are conventional exact
statements.  In \cref{thm:degree-eight-transverse}, only the weight-\(-2\)
elimination and survival of weight \(-1\) through order four are exact over
\(\mathbb Q\); later weight-\(-1\) death is modular evidence.  No stronger
characteristic-zero or scheme-theoretic description of the residual germ is
asserted.
\end{remark}
~~~

[Back to the text-source index](../../index.md)
