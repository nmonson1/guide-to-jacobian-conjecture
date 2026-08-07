---
title: "What does the finite cover remember?"
description: "The cover-and-collision front: normalization, monodromy, collision spaces, and affine-opening recognition."
---

# What does the finite cover remember?

<p class="dek">The displayed counterexample is a polynomial map, but its
mechanism is a finite three-sheeted cover with part of its ramification
boundary removed. This front asks which parts of that picture are intrinsic.</p>

!!! info "Entry route"
    Start with [covers and monodromy](../ideas/monodromy.md),
    [normalization](../ideas/normalization.md), and the
    [marked-root construction](../background/marked-root-geometry.md).

## The running example

The target parametrizes a family of binary cubics. The finite cover remembers
a cubic together with one marked root. Over a generic cubic there are three
points, and continuation permutes them with monodromy \(S_3\). The affine
source is the open set where the marked root is simple.

This gives two related but different objects:

\[
\text{finite marked-root cover}
\qquad\text{and}\qquad
\text{affine simple-root opening}.
\]

The first contains the ramification points; the second deletes them and is
étale. Any intrinsic theory must retain both the finite cover and the chosen
open subset.

## Established landmarks

### The finite/open factorization is canonical

For any dominant generically finite polynomial map, normalization of the
target in the source function field gives a canonical finite map, and the
source embeds as an open set. This makes generic degree, trace, discriminant,
and monodromy available independently of the original formula.

[Read the organizing perspective](../start/what-the-jacobian-condition-misses.md)

### Collisions live in fibre products

The fibre product

\[
U\times_Y U
\]

parametrizes ordered pairs with the same image. Its diagonal is the trivial
collision \((x,x)\); the off-diagonal part records genuine global
noninjectivity. For the fixed three-sheeted example, the diagonal and
collision pieces can be separated algebraically, and the local ordered-root
model near a triple root gives a small explicit collision complex.

### Generic degree is flexible

The first example has three sheets, but this is not a universal feature.
There are three-dimensional Keller maps of every generic degree at least
three. The cover, not merely the affine formula, therefore varies across a
large post-counterexample landscape.

[Read Keller maps of every generic degree](../results/every-generic-degree.md)

### The affine-space chart is exceptional

Inside the two-block multiplication construction, the linear-times-quadratic
marked-root chart is the unique tangent, nonosculating case that becomes
affine space, even after stabilization. This is evidence that recognizing an
affine opening is a separate and restrictive problem.

[Read the stable-uniqueness result](../results/two-block-uniqueness.md)

## Open questions

1. **Affine-opening recognition.** Which intrinsic data on a finite cover and
   its boundary are necessary and sufficient for the complement to be
   affine space?
2. **Flatness and normalization defects.** Which defects available to an
   abstract finite cover are forbidden by the existence of a polynomial
   étale opening?
3. **Factorization recognition.** An imprimitive monodromy group supplies an
   intermediate finite cover. When does that cover carry an affine-space open
   giving an actual polynomial factorization?
4. **Collision complexes.** Can the local collision model of the cubic case be
   promoted to a functorial construction for higher generic degree?

## Common logical traps

- A finite cover is not yet a polynomial self-map of affine space.
- An intermediate field is not yet an intermediate Keller map.
- Monodromy can obstruct factorization, but it does not reconstruct the
  deleted boundary.
- A local collision algebra does not by itself prove that a global affine
  opening exists.

## A useful target

A convincing recognition theorem would begin with intrinsic finite-cover and
boundary data, recover the affine opening without privileged binary-cubic
coordinates, and work on at least one family beyond the original example.

**State reviewed through:** 7 August 2026.
