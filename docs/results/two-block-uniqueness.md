---
title: "The marked-root affine-space construction is exceptional"
description: "Among tangent, nonosculating two-block incidence opens, only the linear-times-quadratic chart becomes affine space, even after stabilization."
---

# The marked-root affine-space construction is exceptional

<p class="dek">The recipe “multiply two binary forms, remove the common-root
locus, and cut by a tangent hyperplane” almost never produces affine space.</p>

!!! info "Technical subtitle"
    Stable uniqueness for nonosculating two-block multiplication charts.

## What is true and why

The marked-cubic example can be described by multiplying a linear binary
form by a quadratic one, then deleting the locus where the factors share a
root and one tangent hyperplane. The same recipe makes a family of spaces
from block sizes \((a,b)\). Class-group and Hodge-theoretic obstructions show
that none of the larger nonosculating cases can become affine space after
multiplying by an affine-space factor.

## Precise result

Let

\[
\mu_{a,b}\colon
\mathbf P(V_a)\times\mathbf P(V_b)
\longrightarrow\mathbf P(V_{a+b}),
\qquad ([L],[Q])\longmapsto[LQ],
\]

where \(V_d\) is the space of binary forms of degree \(d\). Delete the
resultant divisor and the pullback of a hyperplane tangent, but not
osculating, to the rational normal curve. Call the resulting open
\(U_{a,b,H}\).

Then

\[
U_{a,b,H}\times\mathbf A^r\simeq\mathbf A^{a+b+r}
\]

for some \(r\ge0\) if and only if

\[
\{a,b\}=\{1,2\}.
\]

The surviving case is already \(\mathbf A^3\) without stabilization.

## Proof architecture

The divisor classes of the two deleted loci first rule out nonadjacent block
sizes. For larger adjacent sizes, a deficit in the Hodge--Deligne polynomial
survives multiplication by every affine-space factor. The positive
\((1,2)\) case is closed by an explicit coordinate isomorphism that includes
the retained section at infinity.

The argument is scheme-theoretic and does not assume that all roots are
simple.

## Why it matters

The theorem isolates the genuinely exceptional step in the counterexample.
Marking a factor and forgetting it is easy; making the simple-root open into
ordinary affine space is not. The result therefore supports the view that
affine-opening recognition is a central problem rather than a routine
coordinate choice.

## What it does not prove

This is uniqueness inside the tangent-but-nonosculating part of the two-block
multiplication-incidence construction. It says nothing about osculating
hyperplanes and is not a uniqueness theorem for all cubic Keller
presentations or all possible routes to affine space.

## Public proof route

- [Working manuscript source, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/01-cubic-incidence/main.tex) — theorem and proof source.
- [Working manuscript PDF, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/01-cubic-marked-root-covers-2026-07-29-v13.pdf) — reader-facing snapshot dated 29 July 2026.

This is a theorem claimed in the linked project manuscript, authored by
Nathaniel Monson. Its appearance in the guide is not a separate independent
verification of that proof.
