# Order-nine integrability certificate

`RMU-EC26BB3F` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-EC26BB3F` · `proposition`

One has
\[
\mathfrak m^9=0.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Let \(\Lambda^{(9)}\) be a hypothetical nonzero top-degree-nine dual class of
torus weight \(W\).  Every contraction \(\partial_i\Lambda^{(9)}\) lies in the
three-dimensional top degree-eight dual space.  Hence
\[
\partial_i\Lambda^{(9)}
=a_i\Lambda_{W-w_i}^{(8)}
\]
when \(W-w_i\in\{-1,0,1\}\), and it is zero otherwise.  Equality of mixed
contractions produces a homogeneous linear system in the active scalars
\(a_i\).

For each possible weight \(W=-4,\ldots,4\), an exact square subsystem has the
following determinant.
\[
\begin{array}{c|r|r}
W&\text{active scalars}&\text{determinant}\\ \hline
-4&1&248832\\
-3&2&23219011584\\
-2&4&159739999685311463424\\
-1&4&59902499881991798784\\
0&5&4416491511299491340746752\\
1&5&-14905658850635783275020288\\
2&5&-1656184316737309251780032\\
3&3&-71328803586048\\
4&1&-27648
\end{array}
\]
All are nonzero.  For \(|W|>4\), there are no active contractions.  Thus every
\(a_i\) is zero and all contractions of \(\Lambda^{(9)}\) vanish, which forces
\(\Lambda^{(9)}=0\).  Therefore
\(\mathfrak m^9/\mathfrak m^{10}=0\).  Nakayama's lemma applied to the
finitely generated module \(\mathfrak m^9\) gives \(\mathfrak m^9=0\).

  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#prop:order-nine`](../../proof-sources/03-local-rigidity/main.md#label-prop-order-nine)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
