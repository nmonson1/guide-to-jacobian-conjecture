---
title: "What the Jacobian condition controls—and what it misses"
description: "The guide's central perspective: local invertibility, finite covers, properness, and the boundary through which sheets escape."
---

# What the Jacobian condition controls—and what it misses

The Jacobian determinant is a local measurement. If
\(\det DF(p)\ne0\), then near \(p\) the map \(F\) has a single analytic
inverse branch. If the determinant is nonzero everywhere, the source is
locally divided into smooth sheets over the target.

The condition does not compare distant source points, and it does not control
what happens when a source point runs to infinity. Those are precisely the
two global effects that matter after the counterexample.

![A finite cover retains boundary points that are absent from the affine source.](../assets/images/finite-open-factorization.svg)

## Three increasingly global questions

For a polynomial map

\[
F\colon \mathbf A^n\longrightarrow \mathbf A^n
\]

with nonzero constant Jacobian, it helps to separate three questions.

1. **Local:** Is the derivative invertible at every finite source point?
2. **Cover-theoretic:** How many points lie over a generic target, and how do
   those points move around exceptional values?
3. **Affine-global:** Can any of those sheets disappear through infinity?

The Jacobian condition answers the first question. The conjecture asserted
that, for polynomial self-maps of affine space, the first answer somehow
forced the other two. The counterexample shows that it does not.

## Properness is the missing bridge

A continuous map is proper when inverse images of compact sets are compact.
For a polynomial map of complex affine space, failure of properness means
that there are source points \(x_j\) with \(\lVert x_j\rVert\to\infty\) while
\(F(x_j)\) remains bounded.

A proper local homeomorphism is a covering map. Since \(\mathbf C^n\) is
simply connected, a connected covering of \(\mathbf C^n\) has one sheet. In
algebraic language, a proper Keller map is finite étale of degree one and
therefore a polynomial automorphism.

So every noninvertible Keller map must be nonproper. The global obstruction
is not hidden at an ordinary finite critical point; it lives at infinity.

## Restore the finite cover, then record what was deleted

There is a canonical way to separate the cover from its affine presentation.
The polynomial map induces a finite extension of rational-function fields.
Normalize the target in that extension. Zariski's Main Theorem then factors
the map as

\[
\mathbf A^n\hookrightarrow Z_F\longrightarrow \mathbf A^n,
\]

where the first arrow is an open immersion and the second is finite. The
finite variety \(Z_F\) retains the sheets that the affine source has lost.
The omitted set

\[
D_F=Z_F\setminus \mathbf A^n
\]

is the boundary of the affine opening, and its image in the target is where
properness fails.

This factorization separates two problems that the explicit polynomial
formula mixes together:

- understand the finite cover—degree, monodromy, discriminant, collisions;
- understand the affine opening—which boundary is removed, why the remainder
  is affine space, and how the deletion changes the fibres.

The guide sometimes calls this package a **Keller opening**. The phrase is
convenient, but the ingredients—normalization, a finite map, an open
immersion, and a nonproperness locus—are standard.

## The counterexample makes the picture literal

For the three-dimensional example, the finite cover parametrizes a binary
cubic together with a marked root. A cubic with three simple roots has three
possible markings. Forgetting the mark is therefore generically
three-to-one.

At a repeated root, the finite marked-root cover ramifies. The affine source
is obtained by deleting exactly those repeated marked roots. The affine map
therefore has no finite ramification point: its Jacobian remains nonzero.
Instead, as a target approaches the discriminant, some marked points leave
the affine chart and run to infinity.

That is the basic mechanism:

\[
\boxed{\text{finite collision in the completed cover}
\quad\longleftrightarrow\quad
\text{sheet loss at infinity in the affine map}.}
\]

[See the explicit counterexample](counterexample.md){ .md-button .md-button--primary }
[See the marked-root construction](../background/marked-root-geometry.md){ .md-button }

## Why the plane problem is different

The same language applies in dimension two: a plane counterexample would be
an affine open inside a finite cover of the plane, with all finite
ramification removed and with nontrivial boundary at infinity. But surfaces
and curves at infinity are much more rigid than their three-dimensional
counterparts. Compactifications, valuations, Newton polygons, Puiseux
branches, and dessins constrain how the sheets could disappear.

The counterexample therefore does more than end the all-dimensional
conjecture. It isolates the surviving question:

> Can the required finite cover and affine boundary geometry occur in the
> plane?

## Where to read next

| Goal | Recommendation | Why it helps |
| --- | --- | --- |
| See the construction | [Terence Tao's geometric digestion](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) | Reconstructs the example from multiplication of binary forms and the exceptional affine chart. |
| Learn covering spaces | [Allen Hatcher, *Algebraic Topology*, §1.3](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) | Standard introduction to coverings, lifting, and monodromy. |
| Learn normalization | [The Stacks Project, “Normalization”](https://stacks.math.columbia.edu/tag/035E) | Precise algebraic construction and its functorial properties. |
| Follow the plane problem | [The plane case](../background/plane-case.md) | Connects infinity to the current degree bound and the surviving conjecture. |
