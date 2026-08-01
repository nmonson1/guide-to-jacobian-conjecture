# Stable boundary Torelli on the squarefree locus

`RMU-47B48FBA` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-47B48FBA` · `theorem`

Let \((A,B)\) and \((\widetilde A,\widetilde B)\) be admissible squarefree
coprime pairs.  The following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item \(G_{A,B}\) and \(G_{\widetilde A,\widetilde B}\) are stably
polynomially left--right equivalent;
\item they are ordinarily polynomially left--right equivalent;
\item there is \(u\in\C^*\) such that
\[
\widetilde A(uc)=uA(c),\qquad
\widetilde B(uc)-B(c)\in cA(c)\C[c];
\]
\item multiplication by \(u\) identifies the decorated finite schemes
\[
(Z_A^\circ,\sigma_B)
\quad\text{and}\quad
(Z_{\widetilde A}^\circ,\sigma_{\widetilde B}).
\]
\end{enumerate}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

A stable equivalence preserves the reduced nonproperness divisor.  Its
unique singular nonplane component is the discriminant component, while its
other components are the planes \(c=s\), \(s\in Z_A^\circ\).  Passing to
normalizations gives an automorphism of a cylinder over \(\A^2_{c,t}\)
preserving \(L_{A,B}\) and the union of the vertical lines.

Write \(Q_A=A/c\), and let \(C,T\) be the pullbacks of the normalization
coordinates.  Unique factorization gives
\[
Q_{\widetilde A}(C)=\lambda Q_A(c).
\]
Hence \(C\) is algebraic over \(\C(c)\).  Since \(\C(c)\) is algebraically
closed in the purely transcendental cylinder function field, \(C\in\C(c)\).
Polynomiality of the automorphism and its inverse then force
\[
C=uc+v.
\]
The omitted vertical roots account for every root except the distinguished
retained root, so the latter is preserved and \(v=0\).  The normalization
\(A'(0)=\widetilde A'(0)=1\) yields
\[
\widetilde A(uc)=uA(c).
\]

Preservation of the irreducible singular-preimage curve gives
\[
3\widetilde A(C)T+\widetilde B(C)
=\kappa(3A(c)t+B(c)).
\]
The value at \(c=0\) gives \(\kappa=1\), and the admissibility jets imply
\[
\widetilde B(uc)-B(c)\in cA(c)\C[c].
\]
This proves (i)\(\Rightarrow\)(iii); (iii) and (iv) are equivalent by
squarefreeness.

Conversely, after the diagonal change
\[
(x,y,z)\mapsto(ux,y/u,z/u^2),\qquad
(a,b,c)\mapsto(a/u^2,b/u,uc),
\]
condition (iii) reduces to
\[
\widetilde B-B=3A\phi,\qquad \phi\in c\C[c].
\]
The source root translation
\[
(x,y,z)\mapsto
\left(x,y+\phi(c),z-3\frac{\phi(c)}x\right)
\]
is polynomial, preserves \(c\), and shifts \(t\) by \(\phi(c)\).
Expanding the cubic supplies a triangular target automorphism, proving
ordinary left--right equivalence.

  - Does not establish: Presence in the manuscript is not an independent proof audit.
