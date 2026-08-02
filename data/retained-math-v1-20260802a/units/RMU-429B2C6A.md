# Basepoint-free fixed-factor conic exclusion

`RMU-429B2C6A` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-429B2C6A` · `theorem`

Under the preceding hypotheses, assume in addition that
\[
V_{\mathbf P^2}(G,A,B)=\varnothing.
\]
Then no nonautomorphic Keller map has one of the following leading-form
types:
\[
\begin{array}{c|c}
D=5&(g,e)=(1,2),(3,1)\\
D=6&(g,e)=(2,2),(4,1).
\end{array}
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

The additional projective basepoint-free hypothesis is used here: it says
that \(A,B\) form a regular sequence in the homogeneous coordinate ring
\(\C[x,y,z]/(G)\).  The vanishings \(S_1,\ldots,S_{D-1}\) combine with the
Koszul syzygies of \((A,B)\) and the Hilbert--Burch syzygies of
\((A,B)^2\).  They lift the
deformed rank-one symmetric matrix to
\[
\widehat{\mathsf M}_\varepsilon
=a_\varepsilon P_\varepsilon P_\varepsilon^T
+\varepsilon^3\operatorname{sym}(P_\varepsilon,Q_\varepsilon)
\]
after a source-independent target correction.  Consequently
\[
\Phi(\widehat K_\varepsilon)
=-\varepsilon^6(P_\varepsilon\wedge Q_\varepsilon)^2.
\]
The chain-rule identity forces every non-\(\varepsilon\) irreducible factor
of \(P_\varepsilon\wedge Q_\varepsilon\) to divide both of the first two
coordinates and then the Keller determinant.  This is impossible.  The
remaining possibility is a pure power of \(\varepsilon\); comparison of the
lowest coefficients makes the wedge vanish and again forces the linear
determinant to be zero.

Under \texttt{code/degree-five-six/}, the file
\path{conic_fixed_factor_d5_d6_proof_note.md} writes out the four
graded lift identities.  The script
\path{verify_conic_hensel_d5_d6.py} replays them exactly.

  - Full source and surrounding context: [`manuscripts/02-low-degree/appendices/degree-five-six-fixed-factor.tex#thm:degree-five-six-fixed-factor`](../../proof-sources/02-low-degree/appendices/degree-five-six-fixed-factor.md#label-thm-degree-five-six-fixed-factor)
