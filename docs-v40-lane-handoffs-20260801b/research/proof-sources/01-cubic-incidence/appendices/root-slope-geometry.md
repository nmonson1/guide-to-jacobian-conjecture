---
title: "Text proof source — 01-cubic-incidence/appendices/root-slope-geometry.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/01-cubic-incidence/appendices/root-slope-geometry.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `6202ee36bf3ba17c7343c8dfc68c0c8f7063c0164b7e2ee73d930a396d6e8f07` · 4,154 bytes

## Exact label anchors

<a id="label-app-root-slope"></a>
- `app:root-slope` — source line 2
<a id="label-prop-root-slope-transform"></a>
- `prop:root-slope-transform` — source line 9
<a id="label-prop-marked-vandermonde"></a>
- `prop:marked-vandermonde` — source line 67
<a id="label-thm-generic-s3"></a>
- `thm:generic-S3` — source line 97

## Complete source

~~~tex
\section{Root--slope geometry and monodromy}
\label{app:root-slope}

This appendix isolates the mechanism behind the coordinate frame.  It also
records two consequences that complete the generic covering picture.  The
calculations are independent of the pole-cancellation classification.

\begin{proposition}[Universal root--slope transform]
\label{prop:root-slope-transform}
Let \(H(T,c)\in k[T,c]\), where \(2\in k^*\), and define
\[
b=r-H_T(t,c),\qquad
2a=H(t,c)+tb.
\]
Then, for
\[
P_{a,b,c}(T)=H(T,c)+bT-2a,
\]
one has
\[
P_{a,b,c}(t)=0,\qquad P'_{a,b,c}(t)=r,
\]
and
\[
2\,da-t\,db-H_c(t,c)\,dc=r\,dt.
\]
Consequently
\[
\det\frac{\partial(a,b,c)}{\partial(t,r,c)}=\frac r2.
\]
\end{proposition}

\begin{proof}
The root and derivative identities are immediate from the definitions.
Differentiating \(2a=H(t,c)+tb\) and substituting
\(H_T(t,c)+b=r\) gives the one-form identity.  Wedge it with
\(db\wedge dc\); since
\[
db=dr-H_{TT}\,dt-H_{Tc}\,dc,
\]
the stated determinant follows.
\end{proof}

For the reciprocal chart
\[
t=y+\frac1x,\qquad r=\frac2x,\qquad c=w(x,y)-x^3z,
\]
direct expansion gives
\[
\det\frac{\partial(t,r,c)}{\partial(x,y,z)}
=-2x=-\frac4r.
\]
Thus the composite has determinant \(-2\) wherever it is defined.  If pole
cancellation makes it polynomial across \(x=0\), it is a Keller map on all
of affine space.

\begin{remark}[The mechanism]
The finite root-forgetting map contributes the vanishing factor
\(r=P'(t)\).  The affine chart contributes its reciprocal.  When two roots
collide, \(P'(t)\) tends to zero and \(x=2/P'(t)\) tends to infinity.  The
ramification point is not canceled inside the affine source; it is deleted
from the affine chart.  This is the precise gap between an everywhere
\'{e}tale affine map and a finite \'{e}tale cover.
\end{remark}

\begin{proposition}[Marked Vandermonde factorization]
\label{prop:marked-vandermonde}
If \(P(T)=(T-t)Q(T)\), then
\[
\Disc(P)=P'(t)^2\Disc(Q).
\]
For
\[
P(T)=A(c)T^3+B(c)T^2+bT-2a,\qquad r=P'(t),
\]
this becomes
\[
\Disc(P)
=r^2\bigl((3A(c)t+B(c))^2-4A(c)r\bigr).
\]
\end{proposition}

\begin{proof}
Use the product formula
\[
\Disc((T-t)Q)=\Disc(T-t)\Disc(Q)\Res(T-t,Q)^2
\]
and \(\Res(T-t,Q)=Q(t)=P'(t)\).  Dividing the cubic by \(T-t\)
gives a quadratic whose discriminant is the displayed residual factor.
\end{proof}

The two factors represent different collisions.  The first records a
collision involving the marked root; the second records collision of the
two unmarked roots.  Only the first ramifies the chosen sheet.

\begin{theorem}[Generic \(S_3\) monodromy]
\label{thm:generic-S3}
Assume characteristic zero and generic degree three.  The normal closure of
the normalized cubic extension has Galois group \(S_3\).  Over \(\C\), the
geometric monodromy of the three-sheeted \'{e}tale locus is therefore
\(S_3\).
\end{theorem}

\begin{proof}
Generic degree three makes the inverse cubic irreducible over
\(\overline k(a,b,c)\).  Its discriminant is
\[
\Delta=B^2b^2-4Ab^3+8aB^3-36aABb-108a^2A^2.
\]
As a quadratic in \(a\),
\[
\Disc_a(\Delta)=-64(3Ab-B^2)^3.
\]
The right side is not a square in \(\overline k(b,c)\), so \(\Delta\) is
not a square in the rational function field.  An irreducible cubic with
nonsquare discriminant has Galois group \(S_3\).
\end{proof}

On \(A(c)\ne0\), depressing the cubic gives coordinates
\[
p=\frac{3Ab-B^2}{3A^2},\qquad
q=\frac{2B^3-9ABb-54A^2a}{27A^3}
\]
for which
\[
\Delta=A(c)^4(-4p^3-27q^2).
\]
Hence
\[
\{A(c)\ne0,\Delta\ne0\}
\cong
\bigl(\A^1_c\setminus V(A)\bigr)
\times
\{(p,q):4p^3+27q^2\ne0\}.
\]
If \(A\) has \(s\) distinct complex roots, the fundamental group is
\[
F_s\times B_3.
\]
The \(F_s\)-factor records deleted infinity levels; the braid factor gives
the standard permutation quotient \(B_3\twoheadrightarrow S_3\).

\paragraph{Verification boundary.}
The accompanying verifier checks the root--slope Jacobian, reciprocal
chart, discriminant identities, and the finite motivic identities in the
companion research note.  The full companion source and its generated PDF
are retained under \path{supplements/}; the present appendix includes only
the results integrated into this manuscript.
~~~

[Back to the text-source index](../../index.md)
