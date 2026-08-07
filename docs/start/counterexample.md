---
title: "Alpöge and Fable (July 2026): a three-dimensional counterexample"
description: "The explicit map, the two checks that refute the conjecture, its geometric mechanism, provenance, and limits."
---

# Alpöge and Fable (July 2026): a three-dimensional counterexample

<p class="byline">Question suggested by Akhil Mathew · construction produced
by Fable · map announced by Levent Alpöge</p>

<p class="dek">An explicit polynomial map has nonzero constant Jacobian
determinant but sends three distinct points to one point.</p>

## What is true and why

The example is best understood as a three-sheeted cover, not as a lucky
cancellation in a long formula. Begin with a binary cubic and choose one of
its simple roots. Forgetting the choice generically identifies three marked
cubics, while requiring the chosen root to stay simple makes the forgetful
map locally invertible. A special affine chart turns both spaces into affine
three-space and makes the forgetful map polynomial.

## Precise result

Set \(u=1+xy\) and define
\(F=(P,Q,R)\colon\mathbf C^3\to\mathbf C^3\) by

\[
\begin{aligned}
P&=u^3z+y^2u(4+3xy),\\
Q&=y+3xu^2z+3xy^2(4+3xy),\\
R&=2x-3x^2y-x^3z.
\end{aligned}
\]

Direct differentiation gives

\[
\det DF=-2.
\]

The three distinct points

\[
(0,0,-1/4),\qquad (1,-3/2,13/2),\qquad (-1,3/2,13/2)
\]

all map to \((-1/4,0,0)\). Thus \(F\) is locally invertible everywhere but
not injective, and therefore is not a polynomial automorphism. For every
\(n>3\), the product \(F\times\operatorname{id}_{\mathbf C^{n-3}}\) gives a
counterexample in dimension \(n\).

## What the calculation does—and does not—show

The determinant and collision are short, exact calculations. The geometric
construction explains why they occur together and why the generic fiber has
three points. It also reveals the missing sheets at exceptional target
values as points escaping to infinity, rather than as finite ramification.

The result does **not** settle the plane Jacobian conjecture, classify
three-dimensional counterexamples, or prove that the displayed degree is
minimal. Restricting a locally invertible three-dimensional map to a plane
does not usually produce a polynomial self-map of that plane with constant
Jacobian.

[See the marked-root geometry](../background/marked-root-geometry.md){ .md-button .md-button--primary }
[Read the plane case](../background/plane-case.md){ .md-button }

## Credit and sources

The provenance recorded in the technical note is: **Akhil Mathew suggested the
question to Levent Alpöge; Alpöge asked Fable; Fable produced the work leading
to the example; Alpöge announced the map.** Later explanations and formal
checks are distinct contributions.

- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
- [Alpöge's announcement](https://x.com/__alpoge__/status/2079028340955197566)
- [Terence Tao, “A digestion of the Jacobian conjecture counterexample” (21 July 2026)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [Alejandro Radisic, Lean verification, pinned revision](https://github.com/alerad/alpoge-lean/tree/b39e3bf3493939db11b0f78c5b369dd028093f0f)
- [Paul Lezeau, Formal Conjectures PR 4474](https://github.com/google-deepmind/formal-conjectures/pull/4474)
- [Dean Cureton, all-characteristics Lean development, pinned revision](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88)
- [Pablo Nogueira Grossi, independent Lean 4 verification](https://doi.org/10.5281/zenodo.21514514)
