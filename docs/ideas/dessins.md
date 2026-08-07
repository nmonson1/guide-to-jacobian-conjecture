---
title: "Dessins d'enfants: turning boundary equations into permutations"
description: "Why Belyi maps and dessins give finite combinatorial models for Newton faces."
---

# Dessins d'enfants: turning boundary equations into permutations

A **Belyi map** is a map from an algebraic curve to the projective line that
branches only over \(0\), \(1\), and \(\infty\). Its inverse image of the
interval \([0,1]\) is a bipartite graph embedded in the curve—a *dessin
d'enfant*.

For a map of degree \(d\), loops around \(0\), \(1\), and \(\infty\) give
three permutations of \(d\) sheets. Their cycle lengths record the
ramification, their product is the identity, and transitivity says the cover
is connected. A ramification **passport** therefore turns a geometric
classification into a finite permutation problem.

For a degree-two toy example, \(z\mapsto z^2\) is branched only over \(0\)
and \(\infty\), which is allowed because those points are a subset of
\(\{0,1,\infty\}\). The sheet permutations around \(0,1,\infty\) are a
transposition, the identity, and a transposition. This tiny permutation
triple already records the whole connected cover.

## Why dessins arise here

On a Newton face of a hypothetical plane Keller map, the constant-Jacobian
equation can force a rational function whose derivative has zeros and poles
in exactly three fibers. That function is a Belyi map. The allowable face is
then constrained by a passport, and one can enumerate the corresponding
dessins before reconstructing exact coefficients.

In the degree-21 boundary calculation, the forced passport has exactly five
connected dessins. They form one arithmetic orbit and have monodromy
\(A_{21}\). This is a substantial exact classification of the face data.

## What a dessin does not prove

A dessin controls one boundary layer. It does not guarantee that the layer
extends to a global polynomial Keller pair. Later compatibility equations
must still be solved, and the logical route from a global candidate to the
chosen face must be explicit.

[Read the degree-21 result](../results/degree-21-dessins.md){ .md-button }

## Sources

- [Guccione–Guccione–Horruitiner–Valqui, arXiv:2204.14178](https://arxiv.org/abs/2204.14178)
- [Public working manuscript and certificates in this repository's history](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/06-plane-boundary/appendices/degree-twenty-one-certificates.tex)
