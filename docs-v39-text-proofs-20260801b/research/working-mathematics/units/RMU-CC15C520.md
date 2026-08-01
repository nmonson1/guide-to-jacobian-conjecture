# Fourth-power and zero-minor boundaries

`RMU-CC15C520` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-CC15C520` · `proposition`

Subject to the same structural inputs:
\begin{enumerate}[label=(\roman*)]
\item if a primitive coprime leading pencil contains a fourth power, then
its cubic and quadratic normal layers route it to the binary,
quadratic-source, or aligned pure-power branch, so it creates no additional
open leaf;
\item if one of \(U,V,W\) vanishes, including the separate case \(R=0\),
then the map is a polynomial automorphism.
\end{enumerate}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

For (i), normalize \(H_4=(x^4,Q,0)\), \(x\nmid Q\).  The highest
determinant equation makes \(Q(1,u,v)\) and \(R(1,u,v)\) algebraically
dependent.  Their common polynomial generator has degree one or two,
routing respectively to the binary or quadratic-source branch; a constant
generator gives an aligned pure power.  If \(R=0\), the same argument
applies to \(E=(H_2)_3\).

For (ii), if \(J(Q,R)=0\) with \(Q,R\ne0\), Euler's identity gives
\[
 3R\,dQ-4Q\,dR=0,
\]
and hence \(Q=\alpha L^4,R=\beta L^3\).  The other one-minor case is
symmetric, and two vanishing minors with \(R\ne0\) contradict target span
two.  When \(R=0\), the next determinant equation is
\[
 J(P,Q)E_z=0,
\]
so \(F_3=e(x,y)+\mu z\), \(\deg e\le2\).  Straightening this coordinate
reduces the remaining two coordinates to a plane Keller map with a
coordinate of degree at most seven; the corrected low-degree plane theorem
applies.

  - Full source and surrounding context: [`manuscripts/02-low-degree/appendices/quartic-high-ramification-and-fixed-components.tex#prop:quartic-fourth-power-zero-minor`](../../proof-sources/02-low-degree/appendices/quartic-high-ramification-and-fixed-components.md#label-prop-quartic-fourth-power-zero-minor)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
