---
title: "Normalization: separating branches without changing the generic object"
description: "Why normalization is the natural finite model behind an affine Keller opening."
---

# Normalization: separating branches without changing the generic object

A singular algebraic variety can identify branches that are distinct away
from the singular point. **Normalization** replaces it by the closest normal
variety with the same rational functions. For a curve, one can picture the
operation as pulling apart branches of a node or parametrizing a cusp.

The cusp \(y^2=x^3\) is the standard toy example. Its coordinate ring is
\(\mathbf C[t^2,t^3]\), while its normalization is \(\mathbf C[t]\), with

\[
t\longmapsto (t^2,t^3).
\]

The parameter \(t\) gives a smooth line with the same rational functions as
the cusp and remembers how to approach its singular point.

## The finite object behind the affine map

A generically finite polynomial map gives an extension of rational-function
fields. Normalize the target in that extension. The result is a canonical
finite map

\[
Z\longrightarrow \mathbf A^n.
\]

The original affine source is generally only an open subset of \(Z\). The
points in \(Z\) that were omitted form a boundary. For the marked-cubic
counterexample, \(Z\) remembers all marked roots, including the repeated
ones; the source \(\mathbf A^3\) is the simple-root open.

This **finite/open factorization** separates two questions that the affine
formula mixes together:

1. What finite cover of the target is determined by the function field?
2. Which boundary was removed so that the remaining open became affine
   space and the map became étale?

## Why it is useful

Normalization makes trace, discriminant, conductor, and monodromy available
as intrinsic invariants. But it does not solve the recognition problem by
itself: one must still understand the deleted boundary and prove that the
remaining open is affine space.

That is a recurring lesson of the new landscape. Abstract cover data and
polynomial presentation data are related, but neither determines the other
for free.

## Sources

- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
- [David Speyer, Secret Blogging Seminar discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)

[Next: Newton--Puiseux expansions read branches at infinity](newton-puiseux.md){ .md-button }
