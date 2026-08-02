# Binary fixed-factor exclusion

`RMU-D6A4C9D6` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-D6A4C9D6` · `theorem`

Assume the Program~2 reductions reach a binary leading pencil
\[
 H_4=(P,Q,0)
\]
with a nonconstant greatest common divisor \(G\).  If
\(\deg G=1,2,\) or \(3\), then every quartic Keller map in the corresponding
stratum is a polynomial automorphism.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

For \(\deg G=3\), normalize \(H_4=(xG,yG,0)\).  The three multiplicity
types of \(G\) are squarefree, double-plus-simple, and a triple line.  On
the squarefree chart, the first-normal determinant is
\[
 -6^6\operatorname{Disc}(G)\operatorname{Res}(G,R)^2.
\]
The exact root-incidence sweep closes its resultant divisor.  Separate
exact sweeps of the double-line and triple-line types either kill the normal
amplitudes or give a triangular degree drop.

For \(\deg G=1\), the valuation reduction normalizes
\[
 H_4=(x^4,xB,0),\qquad x\nmid B.
\]
There are two affine orbits for the residual cubic:
\[
 B=y^3,\qquad B=y^3+x^2y.
\]
In general coordinates the first-normal determinant is
\[
 248832\,b_3^3r_3^4\Theta,
\]
where
\[
\begin{aligned}
\Theta={}&3b_1^2r_3^2-4b_1b_2r_2r_3-6b_1b_3r_1r_3
+4b_1b_3r_2^2\\
&+4b_2^2r_1r_3-4b_2b_3r_1r_2+3b_3^2r_1^2.
\end{aligned}
\]
The exact exceptional-divisor sweep treats the projective endpoints and
the resonant vertex; the latter reassembles to a plane reduction.

For \(\deg G=2\), the coprime residual quadratic pencil is a secant of the
Veronese conic and can be normalized as
\[
 P=x^2G,\qquad Q=y^2G.
\]
Writing
\[
 G=g_0x^2+g_1xy+g_2y^2,\qquad
 R=r_0x^3+r_1x^2y+r_2xy^2+r_3y^3,
\]
the \(8\)-by-\(8\) first-normal determinant factors exactly as
\begin{equation}
\begin{aligned}
41472&(4g_0g_2-g_1^2)
(-4g_0r_1+3g_1r_0)\\
&\quad\cdot(-3g_1r_3+4g_2r_2)
\operatorname{Res}(G,R)^2.
\end{aligned}
\tag{A.9}
\end{equation}
The four divisors in (A.9), all their intersections, rank jumps,
projective endpoints, and the final aligned resonance are covered by 38
exact replay groups.  No continuity argument across an inverted factor is
used.  Off the divisors the normal matrix is invertible; on every divisor
the determinant arc either produces a unit obstruction or reduces to a
plane automorphism.

  - Full source and surrounding context: [`manuscripts/02-low-degree/appendices/quartic-high-ramification-and-fixed-components.tex#thm:quartic-binary-fixed-factors`](../../proof-sources/02-low-degree/appendices/quartic-high-ramification-and-fixed-components.md#label-thm-quartic-binary-fixed-factors)
