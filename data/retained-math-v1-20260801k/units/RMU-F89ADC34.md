# Every vector-Waring decomposition of \(H\) has length at least 52.

`RMU-F89ADC34` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-F89ADC34` · `proposition`

Every vector-Waring decomposition of \(H\) has length at least 52.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Suppose a decomposition has length at most 51.  Every preceding inequality is
then an equality:
\[
R=\dim U=51,\qquad W=\ker\bigl(U\to\Sym^2(\mathcal A^*)\bigr).
\]
Choose a basis
\(\alpha_1,\ldots,\alpha_{12}\) of \(\mathcal A^*\) among the restricted
forms.  If
\(\alpha=\sum c_j\alpha_j\) and
\(\alpha^2\) lies in the span of the \(\alpha_j^2\), then all
\(c_ic_j\) for \(i\ne j\) vanish.  Hence every restricted form is
proportional to one \(\alpha_j\).

Choose a complement \(V=\mathcal B\oplus\mathcal A\), with
\(\dim\mathcal B=7\), and let
\[
\mathcal C=
\operatorname{pr}_{\mathcal B^*\otimes\mathcal A^*}(W).
\]
The equality description forces \(\mathcal C\) to be invariant under the
twelve coordinate projectors in the \(\alpha_j\)-basis.  Therefore its right
stabilizer algebra
\[
\mathcal E=
\set{T\in\operatorname{End}(\mathcal A^*):
(I\otimes T)\mathcal C\subset\mathcal C}
\]
contains a conjugate of the full diagonal algebra.  Its commutant can then
contain no nonzero nilpotent.

Exact rational computation gives
\[
\dim\mathcal C=24,\qquad
\dim\mathcal E=62,\qquad
\dim\mathcal E'=7,
\]
and \(\mathcal E'\) contains the matrix unit \(E_{5,0}\), with indices
numbered \(0,\ldots,11\).  This element is nonzero and square-zero, a
contradiction.

  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#prop:waring52`](../../proof-sources/05-homogeneous-descendants/main.md#label-prop-waring52)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
