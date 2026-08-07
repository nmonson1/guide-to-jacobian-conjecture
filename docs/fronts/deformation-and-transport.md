---
title: "What survives a change of presentation?"
description: "The deformation-and-transport front: bounded slices, stabilization, normal forms, and intrinsic versus presentation-dependent obstructions."
---

# What survives a change of presentation?

<p class="dek">The same cover can be written by many polynomial maps. Degree
cutoffs, coordinate changes, stabilization, and classical normal-form
reductions preserve different amounts of information.</p>

!!! info "Entry route"
    The pages below state their degree bounds, slices, and equivalence
    relations precisely. Those qualifications are part of the mathematics.

## The running example

The fixed counterexample has ordinary degree seven. One can study nearby
maps in a bounded coefficient space, add unused variables, or convert the map
into cubic-homogeneous and Hessian forms. Each operation answers a different
question.

- A bounded coefficient slice asks about nearby formulas of controlled
  degree.
- Stable left--right equivalence asks what survives polynomial coordinate
  changes after adding identity variables.
- A classical suspension asks whether the failure persists in a restrictive
  normal form.

Confusing these equivalence relations can turn a correct local calculation
into a false global statement.

## Established landmarks

### The bounded degree-seven slice is isolated but nonreduced

After fixing a normalized affine quotient and a transverse degree-at-most-seven
slice, the counterexample is the only reduced point nearby. The local ring
nevertheless has length 584, recording infinitesimal directions that survive
for several orders before becoming obstructed.

[Read the bounded-slice result](../results/length-584.md)

### Some boundary parameters survive arbitrary stabilization

A parameter in a concrete cubic-frame family can be read from normalized
boundary geometry. Because the invariant persists after multiplying by
arbitrary affine-space factors, it distinguishes stable polynomial
left--right equivalence classes.

[Read the stable classification](../results/stable-cubic-frames.md)

### The counterexample reaches classical normal forms

The new failure can be transported to a strict cubic-homogeneous map
\(U+H(U)\) with \(H\) homogeneous cubic. This connects the explicit example
to the Bass--Connell--Wright and Yagzhev reduction framework.

[Read the cubic-homogeneous counterexample](../results/cubic-homogeneous.md)

## Open questions

1. **Intrinsic versus bounded deformation theory.** Which canonical
   deformation object controls the finite Kuranishi slice, and how does the
   degree cutoff select a finite part of it?
2. **Effectivity.** When formal equivalences exist to every finite order, is
   there one polynomial equivalence of uniformly bounded complexity?
3. **Transport of obstructions.** Which classes survive every allowed change
   of presentation, and what hypotheses are needed to compare the relevant
   complexes?
4. **Compression.** How small can a cubic-homogeneous or other normal-form
   realization be without losing the collision?

## Common logical traps

- Isolation in a bounded slice is not isolation among all polynomial maps.
- Formal equivalence to every order need not give a single polynomial
  equivalence.
- A computation in one chart does not automatically survive another chart.
- Stabilization can preserve some invariants while destroying degree-based
  ones.

## A useful target

The immediate goal is a comparison theorem between an intrinsic deformation
object and a finite coefficient scheme, with the equivalence relation, degree
bound, and filtration stated as part of the theorem.

**State reviewed through:** 7 August 2026.
