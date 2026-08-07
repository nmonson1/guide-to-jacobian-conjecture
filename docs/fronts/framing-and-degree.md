---
title: "How small can a counterexample be?"
description: "The competing notions of size for Keller maps and the different arguments needed to minimize each one."
---

# How small can a counterexample be?

<p class="dek">Once counterexamples exist, “smallest” separates into several
mathematical problems. A map can be small as a cover, large as a formula, and
smaller again after a change of normal form.</p>

## Six notions of size

For a polynomial map \(F\colon\mathbf A^n\to\mathbf A^n\), one may try to
minimize:

| Measure | What it sees | Typical behavior |
| --- | --- | --- |
| Ambient dimension \(n\) | Number of variables | Increases under stabilization and degree reduction |
| Ordinary degree | Largest degree of a coordinate | Changes under coordinate transformations and suspensions |
| Generic degree | Number of points in a typical fiber | Intrinsic to the function-field extension |
| Sparsity | Number of monomial terms | Highly presentation-dependent |
| Normal-form dimension | Cost of reaching cubic-homogeneous or cubic-linear form | Depends on the chosen reduction |
| Boundary complexity | Components, singularities, and intersection data at infinity | Often survives equivalence more robustly |

A theorem about one row rarely settles another. This is why low-degree
classification, minimal dimension, and intrinsic cover complexity have
developed into distinct fronts.

## What the first examples already show

The original map has ordinary degree seven, ambient dimension three, and
generic degree three. Subsequent constructions realize every generic degree
\(d\ge3\) already in dimension three. Generic degree is therefore a property
of the cover, largely independent of how closely the coordinates resemble
the first formula.

William Thompson's 24-variable map reaches the strict cubic-homogeneous form
\(U+H(U)\), with \(H\) homogeneous cubic. It supplies a concrete upper bound
on the dimension required by that construction. Finding the smallest
cubic-homogeneous dimension is a separate optimization problem.

Within a broad two-block multiplication construction, the \((1,2)\) cubic
chart is uniquely capable of becoming affine space after stabilization. Here
simplicity is measured geometrically: can the incidence open become affine
space after unused variables are added?

## Low-degree exclusion in the plane

A plane counterexample would have highly constrained behavior at infinity.
Degree bounds convert that geometry into a finite list of Newton polygons,
valuations, and support systems. The current announced result places the
maximum coordinate degree at least \(125\).

A complete low-degree exclusion has two essential parts. A global reduction
must send every map in the stated degree range to one of the terminal
systems, and exact calculation must then eliminate each system.

## Questions with distinct answers

- What is the smallest dimension of a cubic-homogeneous counterexample?
- Which ordinary degrees occur in dimension three?
- Can one lower the number of monomials without increasing dimension?
- Which boundary complexities occur for a given generic degree?
- Is there any characteristic-zero plane counterexample?
- Which measures survive stable polynomial equivalence?

Each question requires its own notion of equivalence, and that equivalence
belongs in the theorem statement.

## Problems to compare

- [Every generic degree](../results/every-generic-degree.md)
- [The 24-variable cubic-homogeneous map](../results/cubic-homogeneous.md)
- [The announced plane degree bound 125](../results/below-125.md)
- [Two-block stable uniqueness](../results/two-block-uniqueness.md)

## Toward a complexity theory

A useful complexity theory would attach several measurements to each
counterexample and track how they change under coordinate transformation,
stabilization, and normal-form reduction. Even a partial theorem relating
ordinary degree to intrinsic boundary data would connect two currently
different kinds of search. Any claim about the smallest counterexample must
therefore begin by naming the quantity being minimized and the transformations
allowed.

