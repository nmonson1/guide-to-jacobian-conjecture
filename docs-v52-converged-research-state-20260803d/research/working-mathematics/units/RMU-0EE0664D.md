---
title: "Universal cubic frame"
description: "For every admissible pair, \\(G_{A,B}\\) is polynomial and\n\\[\n\\det DG_{A,B}=-2.\n\\]\nIf \\(A\\ne0\\), its generic degree is three."
---

# Universal cubic frame

`RMU-0EE0664D` · `proposition` · statement version `1`

## Exact statement

For every admissible pair, \(G_{A,B}\) is polynomial and
\[
\det DG_{A,B}=-2.
\]
If \(A\ne0\), its generic degree is three.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU0EE0664D-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Write
\[
A=c+a_2c^2+c^3A_3(c),\qquad
B=-2-4a_2c+c^2B_2(c),
\]
which is equivalent to the four admissibility conditions.  With
\(\xi=1+xy\), \(d=2-3xy-x^2z\), \(c=xd\), and \(t=\xi/x\), the only
terms that can have poles are
\[
\frac{2+4\xi-3d\xi^2}{x}
\quad\text{and}\quad
\frac{2\xi-2d\xi^3+2\xi^2}{x^2}
+\frac{2a_2d\xi^2(2-d\xi)}{x}.
\]
The three factorizations displayed in the proof of \cref{prop:basic} show
that these are polynomial.  Every term involving \(c^3A_3\) or \(c^2B_2\)
is already polynomial after substituting \(c=xd\) and \(t=\xi/x\).

On \(x\ne0\),
the change \((x,y,z)\mapsto(t,r,c)\) has determinant \(-2x\), while
\((t,r,c)\mapsto(a,b,c)\) has determinant \(r/2\).  Since \(r=2/x\),
the product is \(-2\), and polynomiality extends it across \(x=0\).
Finite simple roots of
\[
A(c)T^3+B(c)T^2+bT-2a
\]
recover the source, giving generic degree three.

[Machine-readable graph](../graph.json)
