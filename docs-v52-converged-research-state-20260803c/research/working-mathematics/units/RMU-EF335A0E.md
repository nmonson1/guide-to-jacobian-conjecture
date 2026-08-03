---
title: "Cubic-cube coordinate"
description: "Suppose that \\(\\deg f\\le3\\), \\(f\\) has no critical point, and its cubic\nhomogeneous part is \\(\\lambda\\ell^3\\) with \\(\\lambda\\ne0\\).  Then \\(f\\) has\na nonzero constant directional derivative and is a coordinate.  The\nstraightening and its inverse can be chosen of degree at most three."
---

# Cubic-cube coordinate

`RMU-EF335A0E` · `lemma` · statement version `1`

## Exact statement

Suppose that \(\deg f\le3\), \(f\) has no critical point, and its cubic
homogeneous part is \(\lambda\ell^3\) with \(\lambda\ne0\).  Then \(f\) has
a nonzero constant directional derivative and is a coordinate.  The
straightening and its inverse can be chosen of degree at most three.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMUEF335A0E-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Take \(\ell=x\), write the remaining variables as \(w\in k^2\), and express
\[
\nabla_wf=Mw+ax+b
\]
with \(M\) symmetric.  Project this affine expression to
\(\operatorname{coker}M=(\ker M)^\vee\).

If it never vanishes, the two projected vectors \(a,b\) do not span an
affine line through the origin.  Hence some \(u\in\ker M\) satisfies
\(u^Ta=0\) and \(u^Tb\ne0\), so \(D_uf\) is a nonzero constant.

Otherwise fix a solution of \(Mw+ax+b=0\).  If \(a\) pairs nontrivially with
\(\ker M\), variation within the solution space makes \(f_x\) vanish.  If it
does not, then \(a\in\operatorname{im}M\); solvability for one \(x\) also
puts \(b\) in \(\operatorname{im}M\), so the system is solvable for every
\(x\).  Substitution of a linear solution \(w=w(x)\) makes \(f_x\) a
quadratic polynomial in \(x\) with leading coefficient \(3\lambda\).  It
has a root over \(k\), again producing a critical point.  Both alternatives
contradict the hypothesis, so the constant-direction case is forced.

In suitable linear coordinates \(f=cw_2+\psi(x,w_1)\), with \(c\ne0\) and
\(\deg\psi\le3\).  Replacing \(w_2\) by \(f\) gives the asserted
straightening and degree bound.

[Machine-readable graph](../graph.json)
