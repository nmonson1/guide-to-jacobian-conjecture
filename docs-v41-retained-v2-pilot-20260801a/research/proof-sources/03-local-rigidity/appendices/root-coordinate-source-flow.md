---
title: "Text proof source — 03-local-rigidity/appendices/root-coordinate-source-flow.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/03-local-rigidity/appendices/root-coordinate-source-flow.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `e9de0ba66ac1c51da3613ed5156ef6f14c4cfb5d353a42fd378f39ee0383dca2` · 1,915 bytes

## Exact label anchors

<a id="label-app-root-coordinate-source-flow"></a>
- `app:root-coordinate-source-flow` — source line 2
<a id="label-prop-root-coordinate-divergence"></a>
- `prop:root-coordinate-divergence` — source line 17
<a id="label-q-different-filtered-reconstruction"></a>
- `q:different-filtered-reconstruction` — source line 54

## Complete source

~~~tex
\section{Root coordinates and the source-flow complex}
\label{app:root-coordinate-source-flow}

The marked-root coordinates make the volume-preserving source action much
sparser than it appears in coefficient coordinates.  Write the target cubic
as
\[
As^3+Bs^2+bs-2a=0
\]
and use \((A,B,s)\) as source coordinates.  Solving for the remaining source
coordinates in the standard marked-root frame gives the Jacobian factor
\[
\delta=1-Bs+3As^2.
\]

\begin{proposition}[Weighted divergence in root coordinates]
\label{prop:root-coordinate-divergence}
In the marked-root chart,
\[
dx\wedge dy\wedge dz
=-\delta\,dA\wedge dB\wedge ds.
\]
Consequently a vector field
\[
X=a\,\partial_A+b\,\partial_B+c\,\partial_s
\]
preserves source volume if and only if
\[
\partial_A(\delta a)+\partial_B(\delta b)+\partial_s(\delta c)=0.
\]
\end{proposition}

\begin{proof}
The first identity is the determinant of the explicit triangular change
from \((x,y,z)\) to the marked-root variables.  Cartan's formula gives
\[
\mathcal L_X(\delta\,dA\wedge dB\wedge ds)
=
\bigl(
\partial_A(\delta a)+\partial_B(\delta b)+\partial_s(\delta c)
\bigr)dA\wedge dB\wedge ds,
\]
which proves the second assertion.
\end{proof}

The same factor \(\delta\) is the derivative of the cubic in the marked
root.  Thus the different of the cubic cover is exactly the weight in the
source divergence equation.  This suggests filtering the volume-preserving
Lie algebra by powers of the different, transferring it to the finite
overflow complex, and comparing the resulting higher brackets with the
Kuranishi equations computed in the body.

\begin{question}[Different-filtered reconstruction]
\label{q:different-filtered-reconstruction}
Can a different-filtered source-flow complex, or an equivalent transferred
\(L_\infty\)-model, recover the bounded-degree Kuranishi ideal and its
length \(584\) independently of coefficient elimination?
\end{question}
~~~

[Back to the text-source index](../../index.md)
