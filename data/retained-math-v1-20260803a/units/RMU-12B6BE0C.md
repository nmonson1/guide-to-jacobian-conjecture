# Bounded orbit map

`RMU-12B6BE0C` · `proposition`

## Mathematical record

`RMU-12B6BE0C` · `proposition`

The degree-preserving root translations form the kernel pair of the map
\[
\Theta_N\colon\operatorname{Tot}(E_N)\longrightarrow
\operatorname{Tot}(E_N),
\qquad
(\widehat Q,P)\longmapsto(\widehat Q,Z^NP).
\]
If \(\widehat Q=z^mQ_d\), with \(Q_d(0)\ne0\), then uniquely
\[
P=z^mP_d+Q_dS,\qquad \deg P_d<d,\quad\deg S<m.
\]
The finite-root decoration is \(P_d\); root translation removes precisely
the principal part \(S/z^m\) supported at infinity.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

For every \(R\)-algebra, two points \(p,p'\) have the same image under a
linear map \(M\) exactly when \(p-p'\in\ker M\).  These are precisely the
equations of the scheme-theoretic fiber product
\(\mathbf V(E)\times_{\mathbf V(E)}\mathbf V(E)\), where both arrows to the
middle copy are \(M\).  This proves the kernel-pair claim for \(M=Z^N\).

For the decomposition, consider the linear map
\[
\{\deg P_d<d\}\oplus\{\deg S<m\}
\longrightarrow \{\deg P<N\},
\qquad (P_d,S)\longmapsto z^mP_d+Q_dS.
\]
If its value is zero, reduction modulo \(Q_d\) gives
\(z^mP_d=0\).  Since \(Q_d(0)\ne0\), \(z\) is a unit modulo \(Q_d\), so
\(P_d=0\); then \(S=0\).  The source and target both have rank \(N=d+m\),
so the map is an isomorphism, proving existence and uniqueness over the
entire monic coefficient base.

  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#prop:bounded-root-translation-groupoid`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-prop-bounded-root-translation-groupoid)
