---
title: "Two constructions (20 July 2026): Keller maps of every generic degree"
description: "Two contemporaneous constructions of three-dimensional counterexamples with every possible generic degree at least three."
---

# Two constructions (20 July 2026): Keller maps of every generic degree

<p class="byline">Constructions in Alexis Gallagher's article and in the
unbylined Ulam technical note · later geometric generalization by Shuhong
Gao</p>

!!! info "Reading level"
    The first section needs only the idea of counting generic preimages. The
    precise mechanisms use one-variable elimination; for the geometric
    language behind “sheets,” see [covers and monodromy](../ideas/monodromy.md).

## What is true and why

The original counterexample is generically three-to-one, but the number
three is not rigid. Two sources published on 20 July give different ways to
alter the hidden one-variable inverse equation without losing the
constant-Jacobian identity. Its degree becomes the number of generic sheets.
Together they show that every integer at least three occurs already for a
Keller map of three-dimensional affine space.

## Precise result

For every integer \(d\ge3\), there is a polynomial map

\[
F_d\colon\mathbf C^3\longrightarrow\mathbf C^3
\]

with constant nonzero Jacobian determinant, generic degree \(d\), and no
polynomial inverse. Generic degree is invariant under polynomial changes of
coordinates, so maps with different \(d\) are inequivalent.

Gallagher chooses a polynomial \(p(w)\) satisfying endpoint and integral
conditions. Those conditions cancel apparent denominators, while inversion
reduces to

\[
\int_0^w p(s)\,ds=wP-cQ.
\]

Choosing \(p\) of degree \(d-1\) gives a degree-\(d\) equation for the hidden
parameter \(w\).

The Ulam technical note uses a separate family \(F_\eta\). It adds terms
that preserve both the determinant calculation and the original
three-point collision. Theorem 5.2 derives a hidden-root equation
\(\Omega_{p,q,r}(s)=0\) whose degree is prescribed by the added polynomial;
Corollary 5.3 obtains every \(d\ge3\).

## Discussion

These constructions show that the post-counterexample landscape contains
genuinely different covers, not merely stabilizations or iterates of the
first three-sheeted map. They also make the escape mechanism visible: when
the reconstruction denominator vanishes, roots of the inverse equation leave
the affine chart.

Shuhong Gao subsequently recast this and related examples as **tangent
sweeps** and generalized the mechanism to direction fields on
hypersurfaces. Gao obtains arbitrarily large generic degree in every
dimension greater than two, including five new explicit maps.

The public timestamps are close: Gallagher's article records 09:37 UTC on
20 July, while the Ulam PDF's embedded creation time is 09:54 UTC. Those
metadata do not by themselves establish when either construction was found
or first circulated, so this guide records both rather than inferring a
priority narrative. The statement is an existence theorem; it does not
classify all Keller maps of a given generic degree.

## Sources

- [Alexis Gallagher, explanatory article](https://alexisgallagher.com/posts/2026/jacobianfun/)
- [Gallagher's pinned construction and exact code](https://github.com/algal/jacobianfun/tree/0a73d4c75bed60660c6e91a56f1595be756cbd59)
- [Unbylined Ulam technical note, Theorem 5.2 and Corollary 5.3](https://www.ulam.ai/research/jacobian.pdf)
- [Shuhong Gao, arXiv:2608.00222](https://arxiv.org/abs/2608.00222)
