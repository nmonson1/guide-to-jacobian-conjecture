---
title: "Front I: intrinsic cover and collision geometry"
description: "From the affine formula to the finite cover, monodromy, collision algebra, and flatness defects."
---

# Front I: intrinsic cover and collision geometry

!!! info "For researchers"
    Start with [covers and monodromy](../ideas/monodromy.md) and
    [normalization](../ideas/normalization.md) if the terminology is new.

The displayed counterexample is a polynomial map, but its central mechanism
is a finite three-sheeted cover with part of its boundary removed. This front
asks which features of that picture are intrinsic and which depend on the
coordinates used to display it.

## The story so far

The function-field extension determines a finite normalization of the target.
Over a regular value, its points are the sheets of the map; monodromy records
how those sheets permute. Fiber products record collisions: the off-diagonal
part of \(X\times_YX\) parametrizes pairs of distinct source points with the
same image.

For the fixed cubic opening, these objects can be calculated explicitly. The
generic monodromy is \(S_3\), and the diagonal splits from the collision
algebra by a canonical idempotent. Near a triple-root point, the three
boundary functions generate the square of the maximal ideal.

The collision geometry now does more than describe multiple fibers. On the
normalized \(S_3\)-Galois closure, the three conjugate source openings and
their pairwise and triple intersections form a Čech complex. At an omitted
target value, the closed-point saturation failure in that complex is exactly

\[
D_A\operatorname{Ext}^1_A(B,A)\otimes V_{\mathrm{std}}.
\]

Thus the collision nerve detects the finite cubic normalization's punctual
flatness defect, including its multiplicity and natural sheet-permutation
representation.

Composition supplies a second intrinsic structure. A nontrivial polynomial
factorization forces an invariant block system in monodromy. The project uses
this to construct full-\(S_d\), composition-prime counterexamples of every
generic degree \(d\ge3\).

## The main open question

Can one recognize an affine Keller opening from intrinsic finite-cover data?
Knowing the abstract cover is not enough: one must recover which boundary was
deleted and why the remaining open is affine space. A useful answer should
work without choosing the binary-cubic coordinates that made the first
example visible.

The cubic saturation theorem is a prototype, not a general answer. The next
step is to understand when higher collision nerves compute intrinsic
duality, flatness, or factorization defects for broader finite openings.

## Places to enter

- [Covers and monodromy](../ideas/monodromy.md)
- [Normalization](../ideas/normalization.md)
- [The marked-root construction](../background/marked-root-geometry.md)
- [When collisions detect a hidden flatness defect](../results/collision-flatness.md)
- [Every generic degree—and prime examples in every degree](../results/every-generic-degree.md)

The concrete target is an intrinsic recognition theorem: finite-cover and
boundary data that are both necessary and sufficient for an affine Keller
opening, tested on at least one family beyond the original coordinates.
