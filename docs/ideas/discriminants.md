---
title: "Discriminants: where roots collide"
description: "How a discriminant locates repeated roots, branch behavior, and the boundary of the marked-root counterexample."
---

# Discriminants: where roots collide

For a one-variable polynomial, the discriminant is a polynomial in the
coefficients that vanishes exactly when the polynomial has a repeated root.
For a family of cubics, its zero set is a hypersurface in coefficient space.

For example, the quadratic \(t^2+bt+c\) has discriminant
\(b^2-4c\). When this number is nonzero, the two roots are distinct. When it
vanishes, both roots equal \(-b/2\). The discriminant is therefore an
equation in the **parameter space** \((b,c)\) for the place where two sheets
of the root cover meet.

The marked-root construction has two related spaces:

- the finite space of cubics with a chosen root;
- the affine source obtained by deleting points where the chosen root is
  repeated.

Over a cubic with three distinct roots, the finite map has three points.
Over the discriminant, some choices coalesce. The finite cover records that
collision as ramification. The affine counterexample has deleted the
ramified points, so the same target can instead appear to have lost sheets at
infinity.

## Why this distinction matters

The Jacobian determinant of the affine map stays nonzero because the
repeated-root points are absent from its source. The discriminant has not
disappeared; it has become boundary information. Its singularities record
more complicated collisions, such as a triple root.

The discriminant therefore links three descriptions of the same event:

- algebra: a resultant or determinant vanishes;
- geometry: roots collide in the finite cover;
- affine behavior: sheets escape through the deleted boundary.

To use this information intrinsically, one often passes to the
[normalization](normalization.md), which separates the branches of the
discriminant itself.

## Sources

- [Terence Tao, geometric digestion](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)

[Next: normalization separates singular branches](normalization.md){ .md-button }
