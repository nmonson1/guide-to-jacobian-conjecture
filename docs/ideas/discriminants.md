---
title: "Discriminants: where roots collide"
description: "How one equation locates repeated roots and connects ramification in the finite cover with lost sheets in the affine chart."
---

# Discriminants: where roots collide

For a one-variable polynomial, the discriminant is a polynomial in the
coefficients that vanishes exactly when the polynomial has a repeated root.
It turns a statement about roots into an equation on parameter space.

For example,

\[
t^2+bt+c
\]

has discriminant \(b^2-4c\). Off the parabola \(b^2=4c\), the two roots are
distinct. On it, they coincide at \(-b/2\).

## The root cover over coefficient space

Consider all pairs

\[
(\text{polynomial},\text{chosen root}).
\]

Over a polynomial with distinct roots, this is a finite cover of the
coefficient space. As the coefficients approach the discriminant, two chosen
roots may coalesce. The finite cover records the collision as ramification.

The marked-cubic construction begins with exactly this picture. Its affine
source retains the simple marked roots and omits the repeated ones. Hence the
same limiting event has two descriptions:

| Viewpoint | What happens at the discriminant |
| --- | --- |
| Finite marked-root cover | Two roots meet at a ramification point |
| Affine Keller map | A sheet leaves the affine chart and approaches the boundary |

The Jacobian determinant of the affine map remains nonzero because the
ramification point is absent from its source.

## One event in three languages

The discriminant synchronizes three kinds of information:

- **algebra:** a resultant vanishes;
- **geometry:** roots collide in a finite cover;
- **affine behavior:** a preimage escapes through the deleted boundary.

Together, these translations let a calculation in coefficients speak about
the global geometry of the map.

<div class="mental-model" markdown>

**How to think about it.** The discriminant is the shadow, in the target, of
where the completed cover ramifies. Deleting those ramification points from
the source turns the same shadow into evidence of nonproperness.

</div>

## Singular points of the discriminant

A smooth point of the discriminant usually represents one simple collision,
such as a double root. Singular points record more complicated behavior: a
triple root, simultaneous collisions, or several local branches of the
discriminant meeting.

To separate those branches and study them intrinsically, one passes to the
normalization of the discriminant—or, more globally, the normalization of the
target in the function field of the source.

[Next: normalization and the finite completion](normalization.md){ .md-button .md-button--primary }

## Sources

- [Terence Tao, geometric digestion](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
