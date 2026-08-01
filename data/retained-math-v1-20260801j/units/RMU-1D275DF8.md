# If \(q,q'\ne-2\), then \(G_q\) and \(G_{q'}\) are stably polynomially left--right equivalent…

`RMU-1D275DF8` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-1D275DF8` · `theorem`

If \(q,q'\ne-2\), then \(G_q\) and \(G_{q'}\) are stably polynomially
left--right equivalent if and only if \(q=q'\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

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

  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#thm:stable-nonexceptional`](../../proof-sources/04-stable-moduli/main.md#label-thm-stable-nonexceptional)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
