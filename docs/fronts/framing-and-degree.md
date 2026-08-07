---
title: "How small can a counterexample be?"
description: "The framing-and-degree front: ordinary degree, generic degree, dimension, sparsity, and the logic of low-complexity exclusions."
---

# How small can a counterexample be?

<p class="dek">Once counterexamples exist, “the smallest one” is not a
single question. Different complexity measures see different parts of the
geometry.</p>

!!! info "Keep the measures separate"
    Generic degree, ordinary coordinate degree, ambient dimension, number of
    monomials, and boundary complexity are not interchangeable.

## The running example

The first map is three-dimensional, has ordinary component degrees
\((7,6,4)\), and has generic degree three. Those numbers describe different
features:

- ordinary degree measures one chosen polynomial presentation;
- generic degree counts sheets of the finite cover;
- dimension measures the ambient affine space;
- sparsity measures how much of the formula is actually used.

Adding identity variables preserves the counterexample but changes the
ambient dimension. Polynomial coordinate changes can alter ordinary degree
without changing generic degree. Normal-form reductions can lower degree only
by introducing many variables.

## Established landmarks

### Every generic degree occurs

The first example has three sheets, but three is not minimal in the sense of
being rigid or unique. Three-dimensional Keller maps exist with every generic
degree \(d\ge3\).

[Read every generic degree](../results/every-generic-degree.md)

### Cubic-homogeneous form is possible in 24 variables

A strict map \(U+H(U)\), with \(H\) homogeneous cubic, gives an explicit
counterexample in dimension 24. The result is structurally important because
it reaches the classical reduction normal form; 24 is an upper bound, not a
minimality theorem.

[Read the 24-variable construction](../results/cubic-homogeneous.md)

### The plane has a much larger announced degree bound

An announced computer-assisted theorem says that a characteristic-zero plane
counterexample must have maximum coordinate degree at least 125. The bound is
about ordinary degree in two variables and does not constrain the displayed
three-dimensional map.

[Read the announced bound](../results/below-125.md)

### The marked-root affine chart is exceptional in its construction class

Within the tangent, nonosculating two-block multiplication construction, the
linear-times-quadratic chart is the only case that becomes affine space, even
after stabilization. This is a structural notion of smallness rather than a
numerical degree bound.

[Read the exceptional-chart theorem](../results/two-block-uniqueness.md)

## Open questions

1. What is the minimum ordinary degree of a counterexample in three
   variables?
2. What is the minimum dimension of a strict cubic-homogeneous
   counterexample?
3. Can sparsity or symmetry force stronger lower bounds than ordinary degree
   alone?
4. Is there any characteristic-zero plane counterexample—and, if so, how far
   above 125 must its degree lie?
5. Which complexity measures can be recovered from the intrinsic finite
   cover, and which depend irreducibly on a frame?

## Common logical traps

- A lower bound in one dimension does not automatically stabilize to another.
- Generic degree is not ordinary polynomial degree.
- A terminal calculation is not a global exclusion without an exhaustive
  reduction.
- A normal-form dimension is an upper bound unless minimality is separately
  proved.

## A useful target

A satisfactory low-complexity theorem has two parts: an exclusion of a
precisely stated class and a reduction proving that every candidate under
discussion belongs to that class.

**State reviewed through:** 7 August 2026.
