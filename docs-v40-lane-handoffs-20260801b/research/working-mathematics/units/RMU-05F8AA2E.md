# Invariant fields

`RMU-05F8AA2E` · `lemma`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-05F8AA2E` · `lemma`

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

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

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

  - Full source and surrounding context: [`manuscripts/02-low-degree/main.tex#lem:invariants`](../../proof-sources/02-low-degree/main.md#label-lem-invariants)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
