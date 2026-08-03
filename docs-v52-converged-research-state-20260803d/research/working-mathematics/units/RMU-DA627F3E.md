---
title: "All-order formal-local versus stable separation"
description: "For every \\(q\\), there is a coefficientwise formal source automorphism\n\\[\n\\Phi_s=\\id+\\sum_{n\\ge1}s^nV_n,\n\\qquad V_n\\in\\C[x,y,z]^3,\n\\]\nsuch that \\(F_s\\circ\\Phi_s=F_0\\) in \\(\\C[x,y,z][[s]]^3\\).  Thus all\n\\(q\\)-arcs are source-trivial to every formal order, while fibers with\nnonzero complex \\(s\\) and different \\(q\\) remain pairwise stably\ninequivalent."
---

# All-order formal-local versus stable separation

`RMU-DA627F3E` · `proposition` · statement version `2`

## Exact statement

For every \(q\), there is a coefficientwise formal source automorphism
\[
\Phi_s=\id+\sum_{n\ge1}s^nV_n,
\qquad V_n\in\C[x,y,z]^3,
\]
such that \(F_s\circ\Phi_s=F_0\) in \(\C[x,y,z][[s]]^3\).  Thus all
\(q\)-arcs are source-trivial to every formal order, while fibers with
nonzero complex \(s\) and different \(q\) remain pairwise stably
inequivalent.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMUDA627F3E-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Write \(F_s=F_0+sF_1+s^2F_2\), as checked directly from the frame.  Suppose
\(V_1,\ldots,V_{n-1}\) have been chosen so that the identity holds modulo
\(s^n\).  At order \(n\), the new coefficient occurs linearly and the
equation is
\[
DF_0\,V_n=-R_n,
\]
where \(R_n\) is a polynomial vector determined by the earlier
coefficients.  The determinant of \(DF_0\) is \(-2\), so its adjugate divided
by \(-2\) is a polynomial inverse.  Therefore
\[
V_n=-(DF_0)^{-1}R_n
\]
is polynomial, and induction constructs \(\Phi_s\) to all orders.  A map
congruent to the identity modulo
\(s\) has a continuous compositional inverse in the \(s\)-adic ring, so this
is a formal source automorphism.

Stable inequivalence of the nonzero complex fibers follows from the
intrinsic ratio of conductor values.  There is no contradiction: the
coefficientwise formal automorphism need not have bounded polynomial degree
in \((x,y,z)\), algebraize over \(\C[s]\), or specialize at \(s\ne0\).

[Machine-readable graph](../graph.json)
