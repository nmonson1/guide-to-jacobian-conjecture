---
title: "How the counterexample works: mark a root, then forget it"
description: "The incidence construction behind the three-sheeted counterexample, explained without hiding the exceptional affine chart."
---

# How the counterexample works: mark a root, then forget it

A **binary cubic** is a homogeneous degree-three polynomial in two
variables. Its roots are directions \([S:T]\) on the projective line
\(\mathbf P^1\): ordinary values \(S/T\), together with the direction at
infinity when \(T=0\).

Consider a binary cubic

\[
f(S,T)=cT^3-2ST^2+bS^2T-2aS^3.
\]

The coefficients \((a,b,c)\) form an affine three-dimensional parameter
space. Now enlarge the data by choosing a root \([S:T]\in\mathbf P^1\) of
the cubic. The resulting incidence space consists of pairs

\[
(\text{cubic},\text{marked root}).
\]

For a cubic with three distinct roots there are three possible markings.
Forgetting the mark is therefore generically three-to-one.

## A one-variable toy model

Take

\[
g(t)=(t-1)(t-2)(t-3).
\]

The three pairs \((g,1)\), \((g,2)\), and \((g,3)\) are different pieces of
marked data, but forgetting the second entry sends all three to the same
polynomial \(g\). Each mark moves smoothly when the coefficients change,
because \(g'(1)\), \(g'(2)\), and \(g'(3)\) are nonzero. By contrast, for
\((t-1)^2(t-3)\), the mark at \(1\) is repeated and the derivative vanishes.

The counterexample turns this elementary three-choice picture into a
polynomial map between affine three-spaces. Its special work is arranging
that all repeated marked roots lie outside the chosen affine source.

## Why the derivative stays invertible

Delete the locus where the marked root is repeated. On the remaining open
set, the root moves smoothly when the coefficients move: the ordinary
implicit-function theorem applies because the derivative of the cubic at
the marked root is nonzero. Consequently, forgetting the mark is étale—its
derivative is invertible everywhere on this open set.

This is the key separation:

- **local behavior:** a simple marked root gives no ramification;
- **global behavior:** three different choices of mark can describe the same
  unmarked cubic.

An invertible derivative detects the first fact but not the second.

## Why affine three-space appears

The full marked-root incidence space is not automatically affine
three-space. The construction uses the special tangent hyperplane whose
coefficient of \(ST^2\) is fixed at \(-2\), and removes the repeated-root
divisor. In this particular chart, the resulting marked-root open is
isomorphic to \(\mathbf A^3\). Writing down that isomorphism gives the
coordinates \((x,y,z)\) and the explicit map in the counterexample page.

This step is the genuinely special part. “Mark a root and forget it” produces
many finite covers; very few of their simple-root opens are affine space.

## The boundary is where the missing sheets go

At an ordinary target, all three roots are simple and all three source points
are present. Along the discriminant, roots collide. But the repeated marked
root was deleted from the source chart, so some points of a limiting fiber
run out through the boundary. The map can lose sheets without developing a
finite critical point.

That boundary behavior is why [local and global invertibility](../ideas/local-and-global.md),
[discriminants](../ideas/discriminants.md), and [normalization](../ideas/normalization.md)
are central to the post-counterexample story.

## Sources

- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
- [Terence Tao, original geometric digestion](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [David Speyer, Secret Blogging Seminar discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
