---
title: "The Jacobian conjecture and its counterexample"
description: "What the conjecture said, the explicit three-dimensional map that disproved it, why the construction works, and what remains open."
---

# The Jacobian conjecture and its counterexample

<p class="dek">An everywhere-invertible derivative does not force a
polynomial map to be globally invertible.</p>

Let

\[
F=(F_1,\ldots,F_n)\colon \mathbf C^n\longrightarrow\mathbf C^n
\]

be a polynomial map. Its Jacobian matrix \(DF\) records the first-order
change of the output when the input moves. If \(\det DF\) never vanishes,
the inverse-function theorem gives a local inverse near every point.

The classical conjecture asked whether this local condition forces a single
global polynomial inverse:

> **Classical Jacobian conjecture.** If \(\det DF\) is a nonzero constant,
> then \(F\) is a polynomial automorphism.

Note that if the determinant of a polynomial Jacobian never vanishes, it is
already a nonzero constant.

## Why the question was plausible

An everywhere-invertible derivative rules out ordinary folding and
ramification. In one variable it settles the problem immediately: a
polynomial with nonzero constant derivative is linear. Many important
special classes in higher dimensions are also known to be invertible.

What the derivative does **not** control is behavior at infinity. Distinct
points can have the same image without a finite critical point if sheets of
the map separate and reconnect through infinity. That is the loophole used
by the three-dimensional counterexample.

## The status now

- As of **8 August 2026**, we know that the Jacobian conjecture is false.[^announcement]
  For the explicit map below, the target point \((-1/4,0,0)\) has three
  distinct preimages.
- We still do not know whether there is a three-variable counterexample of
  ordinary degree below seven, or whether there is any characteristic-zero
  plane counterexample.

The conjecture is therefore false in every dimension at least three: add
unused coordinates to the three-dimensional example. It remains open in
dimension two and is true in dimension one. Cubic counterexamples are known
in higher dimension, so “lower degree” above refers specifically to maps of
three variables.

[^announcement]: [Levent Alpöge's announcement of the counterexample](https://x.com/__alpoge__/status/2079028340955197566).

## The explicit map

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
not injective, and therefore is not a polynomial automorphism.

These two finite checks—the determinant and the collision—are already a
complete refutation of the conjecture in dimension three. The construction
behind them explains why such an unlikely-looking formula exists.

## Why the map works

Begin with a binary cubic and choose one of its simple roots. Forgetting the
choice generically identifies three marked cubics, while requiring the chosen
root to remain simple makes the forgetful map locally invertible. A special
affine chart turns both spaces into affine three-space and makes the
forgetful map polynomial.

In this picture, the three colliding source points are three choices of a
marked root of the same cubic. At exceptional target values, sheets disappear
through the deleted boundary at infinity rather than merging at a finite
critical point. The Jacobian detects the absence of finite ramification; it
does not detect the global collision.

[See the marked-root geometry](../background/marked-root-geometry.md){ .md-button .md-button--primary }
[Read the plane case](../background/plane-case.md){ .md-button }

## What the example does not settle

The example does not classify three-dimensional counterexamples or prove
that degree seven is minimal there. It also does not settle the plane
Jacobian conjecture. Restricting a locally invertible three-dimensional map
to a plane does not usually produce a polynomial self-map of that plane with
constant Jacobian.

## Credit and sources

The provenance recorded in the technical note is: **Akhil Mathew suggested
the question to Levent Alpöge; Alpöge asked Fable; Fable produced the work
leading to the example; Alpöge announced the map.** Later explanations and
formal checks are distinct contributions.

- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
- [Alpöge's announcement](https://x.com/__alpoge__/status/2079028340955197566)
- [Terence Tao, “A digestion of the Jacobian conjecture counterexample” (21 July 2026)](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [Alejandro Radisic, Lean verification, pinned revision](https://github.com/alerad/alpoge-lean/tree/b39e3bf3493939db11b0f78c5b369dd028093f0f)
- [Paul Lezeau, Formal Conjectures PR 4474](https://github.com/google-deepmind/formal-conjectures/pull/4474)
- [Dean Cureton, all-characteristics Lean development, pinned revision](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88)
- [Pablo Nogueira Grossi, independent Lean 4 verification](https://doi.org/10.5281/zenodo.21514514)
