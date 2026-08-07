---
title: "Keller maps of every generic degree"
description: "How the hidden inverse equation can be tuned so that every number of generic sheets at least three occurs in dimension three."
---

# Keller maps of every generic degree

<p class="byline">Constructions published by Alexis Gallagher and in the
unbylined Ulam technical note on 20 July 2026 · later geometric
generalization by Shuhong Gao</p>

The first counterexample has three generic sheets because its target cubic has
three possible marked roots. Within a day, two constructions showed that the
number of sheets can be prescribed:

\[
d=3,4,5,\ldots
\]

all occur for polynomial self-maps of \(\mathbf A^3\) with constant nonzero
Jacobian.

## Change the hidden inverse equation

A generically finite map can often be inverted by first recovering one hidden
parameter. In the original example, that parameter satisfies a cubic equation.
The later constructions alter this one-variable reconstruction while
preserving the determinant identity.

Gallagher chooses a polynomial \(p(w)\) satisfying endpoint and integral
conditions. These conditions cancel the apparent denominators, while the
inverse problem reduces to

\[
\int_0^w p(s)\,ds=wP-cQ.
\]

When \(p\) has degree \(d-1\), the hidden parameter \(w\) satisfies a
degree-\(d\) equation. A generic target therefore has \(d\) preimages.

The Ulam construction uses a different determinant-preserving modification.
Its hidden-root polynomial \(\Omega_{p,q,r}(s)\) has a degree controlled by an
added polynomial, again producing every \(d\ge3\).

## The theorem

For every integer \(d\ge3\), there is a polynomial map

\[
F_d\colon\mathbf C^3\longrightarrow\mathbf C^3
\]

with constant nonzero Jacobian determinant, generic degree \(d\), and no
polynomial inverse.

Generic degree is invariant under polynomial changes of coordinates. Maps
with different values of \(d\) therefore represent genuinely different
covers.

## Generic degree can be prescribed

The number three is a feature of the first construction. Keller maps admit
every larger generic degree as well. The post-counterexample landscape
contains covers of every integer degree \(d\ge3\), already in the
smallest dimension where a characteristic-zero counterexample is known.

The construction also separates two notions of complexity. Ordinary degree
measures the coordinate formula; generic degree measures the extension

\[
\mathbf C(P,Q,R)\subset\mathbf C(x,y,z).
\]

They can vary independently.

## A geometric reformulation

Shuhong Gao later described this and related constructions as **tangent
sweeps** and generalized the mechanism to direction fields on hypersurfaces.
The geometric viewpoint explains how large generic degree arises from the
number of intersections with a moving line or direction field, while
nonproperness removes exceptional intersections through infinity.

The next classification problem is finer: for a fixed generic degree, which
monodromy groups, boundary types, and affine openings can occur?

[Proof, sources, and chronology](evidence-ledger.md#every-generic-degree){ .evidence-link }
