---
title: "Which deformations are genuine?"
description: "How to separate new Keller maps from coordinate motion, degree-cutoff artifacts, and changes introduced by stabilization or normal forms."
---

# Which deformations are genuine?

<p class="dek">Change one coefficient of a Keller map. Have we found a nearby
map, merely rewritten the old one in new coordinates, or produced an
infinitesimal motion that later becomes obstructed?</p>

## A specimen tangent question

Let \(F_t\) be a first-order family

\[
F_t=F+tG+O(t^2)
\]

through a fixed Keller map \(F\). Differentiating the constant-Jacobian
condition gives a linear equation on \(G\). Many solutions arise from
infinitesimal source or target coordinate changes. Those directions move the
presentation without changing the underlying map up to equivalence.

The first deformation problem is therefore a quotient problem:

\[
\frac{\text{infinitesimal Keller deformations}}
     {\text{infinitesimal coordinate motion}}.
\]

The quotient depends on which coordinate changes are allowed and whether a
degree bound has been imposed.

## Why degree bounds distort the picture

An unrestricted formal coordinate change may require terms of increasing
degree at successive orders. Inside the finite-dimensional scheme of maps of
degree at most seven, only part of that coordinate orbit is visible. The
orbit can meet the coefficient scheme nontransversely, creating nilpotent
structure in a chosen slice.

For the fixed degree-seven counterexample, one normalized transverse slice has
a single reduced point and a completed local algebra of length \(584\). Its
ten-dimensional tangent space records many first-order motions. Higher-order
equations obstruct every genuine nearby point in that bounded slice.

The geometry is vivid: the map is isolated after reduction, yet surrounded by
a thick infinitesimal neighborhood.

## Stabilization and normal forms

Other operations change the ambient presentation more radically:

- adjoining identity coordinates;
- polynomial left--right coordinate changes;
- passing through Bass--Connell--Wright or Yagzhev reductions;
- suspending to cubic-homogeneous or Hessian form.

Each operation preserves some invariants and forgets others. Generic degree
survives polynomial equivalence. A boundary modulus in the cubic-frame family
survives arbitrary stabilization. Ordinary degree and sparsity may change
dramatically under normal-form reduction.

The resulting transport problem is to follow an intrinsic feature through
the construction and state exactly which equivalence relation preserves it.

<div class="mental-model" markdown>

**The question behind the calculations.** Which infinitesimal directions move
the underlying cover or boundary, and which merely move the coordinates used
to display them?

</div>

## Two complementary test cases

- [A transverse local algebra of length 584](../results/length-584.md)
- [Stable cubic-frame classification](../results/stable-cubic-frames.md)
- [The cubic-homogeneous normal form](../results/cubic-homogeneous.md)

## The missing comparison theorem

The missing theorem should build an intrinsic deformation object from the
finite cover and its boundary, then compare it with explicit finite-degree
coefficient schemes. Such a theorem should explain:

1. which tangent directions come from coordinate motion;
2. which directions survive after quotienting;
3. where higher-order obstructions appear;
4. how the answer changes under stabilization and normal-form transport.

The length-584 calculation and the stable cubic-frame modulus are complementary
test cases. The first is local and degree-bounded. The second detects a global
boundary invariant after arbitrarily many identity variables are added. A
comparison theorem should explain both phenomena in one language.

