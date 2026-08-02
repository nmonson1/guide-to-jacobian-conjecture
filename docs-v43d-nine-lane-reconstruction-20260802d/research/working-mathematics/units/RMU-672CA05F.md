# Degree-fifteen stable moduli

`RMU-672CA05F` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-672CA05F` · `theorem`

The associated maps are polynomial Keller maps of component degrees
\((15,14,4)\), generic degree three, and generic monodromy \(S_3\).
Their stable equivalence relation is exactly
\[
(s,d_1,d_2)\sim(1/s,d_2,d_1).
\]
Consequently degree fifteen contains a three-dimensional stable-moduli
family, modulo this finite involution.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

The jet conditions at \(c=0\) are precisely the pole-cancellation
conditions in the cubic frame, so \cref{prop:general-frame} gives a Keller
map of generic degree three.  Since \(\deg A=\deg B=3\), the leading-term
formulas give component degrees \((15,14,4)\).

The inverse cubic is irreducible over the target function field because it
generates the degree-three source extension.  Its discriminant has valuation
one along the irreducible primitive discriminant divisor, so it is not a
square in that field.  A transitive subgroup of \(S_3\) arising from an
irreducible cubic is \(A_3\) or \(S_3\); the nonsquare discriminant excludes
\(A_3\).  Thus the generic monodromy is \(S_3\).

The represented root is \(0\), while the
two missing roots are \(-1,-s\).  By
\cref{thm:conductor-arrangement-classification}, an equivalence must fix the
represented root and either fix or interchange the missing roots.  This
gives the identity or the displayed involution.  The involution is realized
by
\[
(x,y,z)\longmapsto(x/s,sy,s^2z)
\]
and
\[
(a,b,c)\longmapsto(s^2a,sb,c/s).
\]

  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/conductor-arrangements.tex#thm:degree-fifteen-moduli`](../../proof-sources/04-stable-moduli/appendices/conductor-arrangements.md#label-thm-degree-fifteen-moduli)
