# Stable conductor-arrangement classification

`RMU-A7F1B713` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-A7F1B713` · `theorem`

Assume \(A,A'\) are squarefree and
\[
\gcd(A,B)=\gcd(A',B')=1.
\]
Two marked arrangements
\[
\left(\A^2,L_{A,B},\{M_\rho\}_{\rho\in S}\right)
\quad\text{and}\quad
\left(\A^2,L_{A',B'},\{M_{\rho'}\}_{\rho'\in S'}\right)
\]
become isomorphic after multiplication by an affine space if and only if
there exist
\[
\gamma(c)=\lambda c+\mu,\quad \lambda\ne0,\qquad
\nu,\kappa\in\C^*,\qquad h(c)\in\C[c],
\]
such that \(\gamma\) carries the marked roots to the marked roots and
\[
A'(\gamma(c))\nu=\kappa A(c),
\]
\[
B'(\gamma(c))+3A'(\gamma(c))h(c)=\kappa B(c).
\]
Stabilization introduces no additional transformations.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

If a cylinder automorphism has first coordinate \(C\), mapping one marked
line to another gives equality of principal prime ideals and hence
\[
C-\rho'=\lambda(c-\rho).
\]
Thus \(C=\lambda c+\mu\), independent of \(t\) and of all stabilization
variables.  The conductor curves are irreducible principal divisors, so
\[
3A'(C)T+B'(C)=\kappa(3A(c)t+B(c)).
\]
Solving this identity shows that \(T\) is independent of all stabilization
variables and has the form \(T=\nu(c)t+h(c)\).  In the full cylinder
Jacobian, the determinant factors as \(\lambda\nu(c)\) times the determinant
of the stabilization-coordinate block.  Since the product is a nonzero
constant, \(\nu(c)\) is a unit, hence constant.
Coefficient comparison gives the two equations.  Conversely, they define
the required triangular automorphism without using any stabilization
variable.

  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/conductor-arrangements.tex#thm:conductor-arrangement-classification`](../../proof-sources/04-stable-moduli/appendices/conductor-arrangements.md#label-thm-conductor-arrangement-classification)
