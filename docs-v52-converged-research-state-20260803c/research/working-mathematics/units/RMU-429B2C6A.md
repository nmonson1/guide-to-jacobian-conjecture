---
title: "Basepoint-free fixed-factor conic exclusion"
description: "Under the preceding hypotheses, assume in addition that\n\\[\nV_{\\mathbf P^2}(G,A,B)=\\varnothing.\n\\]\nThen no nonautomorphic Keller map has one of the following leading-form\ntypes:\n\\[\n\\begin{array}{c|c}\nD=5&(g,e)=(1,2),(3,1)\\\\\nD=6&(g,e)=(2,2),(4,1).\n\\end{array}\n\\]"
---

# Basepoint-free fixed-factor conic exclusion

`RMU-429B2C6A` · `theorem` · statement version `1`

## Exact statement

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

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU429B2C6A-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

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

[Machine-readable graph](../graph.json)
