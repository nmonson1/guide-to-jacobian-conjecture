---
title: "The Jacobian conjecture, after the counterexample"
description: "A reader's guide to the counterexample in three variables, the surviving plane problem, and the mathematics opened by it."
---

<div class="hero" markdown>
<div class="hero-copy" markdown>

<p class="eyebrow">A mathematical guide</p>

# The conjecture failed in three dimensions. The plane case did not.

For nearly a century, the Jacobian conjecture asked whether a polynomial map
with nonzero constant Jacobian determinant must have a polynomial inverse. An
explicit counterexample announced in July 2026 answers **no** in every
dimension at least three. The two-dimensional problem remains open.

[See the counterexample](start/counterexample.md){ .md-button .md-button--primary }
[Start with the conjecture](start/conjecture.md){ .md-button }

</div>
<div class="hero-panel" markdown>

## The shortest version

There is an explicit polynomial map
\(F\colon \mathbf C^3\to\mathbf C^3\) with

\[
\det DF=-2,
\]

and three distinct points have the same image. Every derivative is invertible.
A generic target value still has three preimages.

The construction uses the third variable in an essential way. The plane
problem asks for new geometry.

</div>
</div>

## Where the story turns

The Jacobian determinant controls the map near each finite source point. The
counterexample exploits what that local calculation cannot see: several
separate sheets can cover the same target region, and some sheets can escape
through infinity without creating a finite critical point.

The useful object is therefore larger than the displayed formula. It consists
of a finite cover, an affine open inside that cover, and the boundary removed
to obtain the open. Once those pieces are visible, the determinant identity
becomes structural and the surviving plane problem comes into focus.

## Choose a route

<div class="card-grid" markdown>

<div class="story-card" markdown>

### Verify the map

Read the formula, a short structural determinant computation, the explicit
collision, and the exact conclusion.

[Read the counterexample](start/counterexample.md)

</div>

<div class="story-card" markdown>

### See the three pictures

Move from the polynomial formula to the marked-root cover and then to the
finite completion with its deleted boundary.

[Read three views of the example](start/three-views.md)

</div>

<div class="story-card" markdown>

### Understand the construction

Mark one root of a binary cubic and then forget which root was marked. Simple
roots explain local regularity; the three possible markings explain the
global collision.

[See the marked-root construction](background/marked-root-geometry.md)

</div>

<div class="story-card" markdown>

### Follow the plane problem

The two-variable conjecture is still open. See why slicing loses the
required polynomial and Jacobian structure, what a plane counterexample would
have to do at infinity, and where the current degree frontier lies.

[Read about the plane case](background/plane-case.md)

</div>

</div>

## From explanation to research

The [six mathematical ideas](ideas/index.md) develop the concepts that the
example naturally asks for: properness, monodromy, discriminants,
normalization, Puiseux expansions, and dessins. The [four research
fronts](fronts/index.md) are short essays about the questions that connect
those ideas.

The [major-result pages](results/index.md) explain selected theorems and
computations. Their proof locations, source forms, verification scope, and
publication status live separately in the [proof and evidence
ledger](results/evidence-ledger.md), so the mathematical narrative can remain
readable without hiding how each claim is supported.

For a longer reconstruction from geometric first principles, read
[Terence Tao's digestion](start/tao-digestion.md). For books and notes, the
[background reading guide](background/background-reading.md) recommends what
to pick up when a particular idea becomes necessary.
