---
title: "Discriminants: where roots collide"
description: "A worked introduction to repeated roots, ramification, and the conversion of a finite collision into affine sheet loss."
---

# Discriminants: where roots collide

A discriminant is an equation in parameter space for the place where a
polynomial acquires a repeated root. It translates a geometric event—two
sheets meeting—into an algebraic equation in the coefficients.

## Worked example: deriving the quadratic discriminant

Let

\[
q(t)=t^2+bt+c.
\]

A number \(r\) is a repeated root exactly when

\[
q(r)=0,
\qquad
q'(r)=2r+b=0.
\]

The second equation gives \(r=-b/2\). Substituting into the first gives

\[
\frac{b^2}{4}-\frac{b^2}{2}+c=0,
\]

or

\[
\boxed{b^2-4c=0.}
\]

Thus the discriminant

\[
\Delta=b^2-4c
\]

vanishes precisely when the two roots coincide.

The formula can also be read from the roots. If
\(q(t)=(t-r_1)(t-r_2)\), then

\[
\Delta=(r_1-r_2)^2.
\]

The square makes the expression symmetric, so it can be written in the
coefficients even though the individual roots cannot be globally labeled.

## The local model of a collision

The simplest two-sheeted branched cover is

\[
s\longmapsto t=s^2.
\]

For \(t\ne0\), the fibre consists of \(\pm\sqrt t\). At \(t=0\), the two
points meet at \(s=0\), where the derivative vanishes. This is ordinary
ramification.

Now delete the ramification point from the source:

\[
\mathbf C^\times\longrightarrow\mathbf C,
\qquad s\longmapsto s^2.
\]

The derivative is nonzero everywhere on the remaining source. Generic fibres
still have two points, but the fibre over \(0\) is empty. The finite cover has
a collision; the affine open has lost two sheets through its deleted
boundary.

This toy map is not a polynomial self-map of affine space, but it isolates
the exact distinction used by the counterexample.

## Cubics and singular discriminants

For a family of cubics, the discriminant is a hypersurface in the
three-dimensional coefficient space. A smooth point of that hypersurface
usually represents one double root and one simple root. A singular point can
represent a more degenerate event, such as a triple root.

The marked-root construction has two related spaces:

- the finite space of cubics with a chosen root;
- the affine source obtained by deleting points where the chosen root is
  repeated.

The finite cover ramifies over the discriminant. The affine Keller map has
deleted the ramified points, so its Jacobian stays nonzero and the same target
locus becomes a nonproperness boundary.

![Deleting the ramification point converts a finite collision into missing affine sheets.](../assets/images/finite-open-factorization.svg)

## Algebra, geometry, and affine behavior

The discriminant links three descriptions of one event:

- **algebra:** a resultant or determinant vanishes;
- **finite geometry:** roots collide and the cover ramifies;
- **affine geometry:** deleted ramification points appear as sheets escaping
  through infinity.

Its normalization can then separate the branches of the discriminant itself,
and its conductor measures where the singular discriminant differs from that
normalization.

## What a discriminant does not tell you

The discriminant identifies exceptional target values. By itself it does not
specify:

- which points have been removed from the source;
- whether the remaining source is affine space;
- whether a local model globalizes to a polynomial map;
- whether two coordinate descriptions encode the same intrinsic boundary.

## Where to read next

| Level | Recommendation | Use it for |
| --- | --- | --- |
| Computational introduction | Cox, Little, and O'Shea, *Ideals, Varieties, and Algorithms*, sections on resultants | Eliminating a variable and detecting common roots. |
| Structural reference | Gelfand, Kapranov, and Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants* | The general geometry of discriminants and resultants. |
| This example | [Terence Tao's geometric digestion](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) | How the resultant and repeated-root locus enter the construction. |

[Next: normalization restores the finite object](normalization.md){ .md-button }
