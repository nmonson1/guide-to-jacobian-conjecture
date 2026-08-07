---
title: "Every generic degree—and prime examples in every degree"
description: "Every number of generic sheets at least three occurs, and one can arrange full symmetric monodromy so the map does not decompose nontrivially."
---

# Every generic degree—and prime examples in every degree

<p class="byline">Every-degree constructions by Alexis Gallagher and in the
unbylined Ulam technical note · later geometric generalization by Shuhong Gao
· full-symmetric-monodromy strengthening from this project</p>

!!! info "Reading level"
    The first section needs only the idea of counting generic preimages. The
    strengthening uses monodromy: how those preimages permute as the target
    moves around loops.

## What is true and why

The original counterexample is generically three-to-one, but the number
three is not rigid. Two sources published on 20 July 2026 give different ways
to alter the hidden one-variable inverse equation without losing the
constant-Jacobian identity. Its degree becomes the number of generic sheets.
Together they show that every integer at least three occurs already for a
Keller map of three-dimensional affine space.

## The every-degree theorem

For every integer \(d\ge3\), there is a polynomial map

\[
F_d\colon\mathbf C^3\longrightarrow\mathbf C^3
\]

with constant nonzero Jacobian determinant, generic degree \(d\), and no
polynomial inverse. Generic degree is invariant under polynomial changes of
coordinates, so maps with different \(d\) are inequivalent.

Gallagher chooses a polynomial \(p(w)\) satisfying endpoint and integral
conditions. Those conditions cancel apparent denominators, while inversion
reduces to

\[
\int_0^w p(s)\,ds=wP-cQ.
\]

Choosing \(p\) of degree \(d-1\) gives a degree-\(d\) equation for the hidden
parameter \(w\).

The Ulam technical note uses a separate family \(F_\eta\). It adds terms
that preserve both the determinant calculation and the original three-point
collision. Theorem 5.2 derives a hidden-root equation whose degree is
prescribed by the added polynomial; Corollary 5.3 obtains every \(d\ge3\).

Shuhong Gao subsequently recast this and related examples as **tangent
sweeps** and generalized the mechanism to direction fields on hypersurfaces.
Gao obtains arbitrarily large generic degree in every dimension greater than
two, including five new explicit maps.

## Project strengthening: prime examples in every degree

Counting sheets does not tell us whether a map was assembled by composing
simpler Keller maps. Call \(F\) **composition-prime** if every factorization

\[
F=G\circ H
\]

has \(G\) or \(H\) a polynomial automorphism.

A nontrivial factorization forces the generic fiber of \(F\) to split into
blocks: first choose a preimage under \(G\), then choose a point in the
corresponding fiber of \(H\). Monodromy must preserve those blocks. Therefore
primitive monodromy—and in particular the full symmetric group \(S_d\)—rules
out a nontrivial factorization.

The weighted-lift construction can be chosen so that its hidden inverse
polynomial is a Morse polynomial: all critical points are simple and their
critical values are distinct. The local branch permutations are then
transpositions. Connectedness makes those transpositions generate the full
symmetric group.

Consequently, for every \(d\ge3\), there is a three-dimensional Keller map
with

\[
\operatorname{Mon}(F_d)=S_d.
\]

In particular, there is a composition-prime counterexample of every generic
degree \(d\ge3\).

## What the strengthening does and does not say

This shows that higher-sheeted examples need not be iterates or composites of
the three-sheeted map. It is an existence theorem: it chooses one suitable
seed in each degree. It does not claim that the convenient rational seed used
for the simplest every-degree formula has full symmetric monodromy for every
\(d\), nor does it classify all Keller maps of a fixed generic degree.

An imprimitive monodromy group is also not enough, by itself, to produce a
polynomial factorization. It gives an intermediate normal finite cover, but
one must still recognize an affine-space opening on that cover.

## Sources and status

- [Alexis Gallagher, explanatory article](https://alexisgallagher.com/posts/2026/jacobianfun/)
- [Gallagher's pinned construction and exact code](https://github.com/algal/jacobianfun/tree/0a73d4c75bed60660c6e91a56f1595be756cbd59)
- [Unbylined Ulam technical note, Theorem 5.2 and Corollary 5.3](https://www.ulam.ai/research/jacobian.pdf)
- [Shuhong Gao, arXiv:2608.00222](https://arxiv.org/abs/2608.00222)

The full-symmetric-monodromy proof is recorded in the current project
contribution `contributions/composition-monodromy-boundary.md`. Its exact seed
construction should be linked from a pinned public source bundle before final
editorial approval.

[Learn how monodromy detects composition](../ideas/monodromy.md){ .md-button }
