# For every \(q\in\C\), \[ S_{G_q}=D_q\cup P. \] These are the two irreducible…

`RMU-FF941A1E` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-FF941A1E` · `proposition`

For every \(q\in\C\),
\[
S_{G_q}=D_q\cup P.
\]
These are the two irreducible components.  For \(q\ne-2\), the component
\(D_q\) is singular and \(P\) is smooth.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

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

  - Does not establish: Presence in the manuscript is not an independent proof audit.
