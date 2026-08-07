---
title: "Why the cubic two-block chart is exceptional"
description: "Among tangent nonosculating two-block multiplication charts, only the cubic (1,2) case becomes affine space, even after stabilization."
---

# Why the cubic two-block chart is exceptional

<p class="byline">A project theorem of Nathaniel Monson</p>

The marked-cubic example can be built by multiplying a linear binary form by
a quadratic one, then deleting the common-root divisor and the pullback of a
specially chosen tangent hyperplane. The same recipe exists for larger block
sizes \((a,b)\). Global invariants isolate the first cubic chart as the only
stably affine member of this nonosculating family.

## The multiplication construction

Let \(V_d\) be the vector space of binary forms of degree \(d\), and consider

\[
\mu_{a,b}\colon
\mathbf P(V_a)\times\mathbf P(V_b)
\longrightarrow
\mathbf P(V_{a+b}),
\qquad
([L],[Q])\longmapsto[LQ].
\]

Delete two divisors:

1. the resultant divisor, where \(L\) and \(Q\) share a root;
2. the pullback of a hyperplane tangent and nonosculating to the rational
   normal curve.

Write \(U_{a,b,H}\) for the resulting open variety. The case
\(\{a,b\}=\{1,2\}\) is the affine three-space underlying the first
counterexample.

## The stable classification

For some \(r\ge0\), suppose

\[
U_{a,b,H}\times\mathbf A^r
\simeq
\mathbf A^{a+b+r}.
\]

Then

\[
\{a,b\}=\{1,2\}.
\]

Conversely, the \((1,2)\) case is already \(\mathbf A^3\) before any
stabilization.

## Two different obstructions

The proof separates the larger cases in two stages.

First, the divisor classes of the resultant and tangent loci rule out
nonadjacent block sizes. Their complement has the wrong class-group behavior
to become affine space after multiplication by \(\mathbf A^r\).

For the remaining adjacent block sizes, a deficit in the Hodge--Deligne
polynomial survives every affine-space factor. The stable cohomological
signature still disagrees with affine space.

The positive \((1,2)\) case is verified by an explicit coordinate
isomorphism, including the retained section at infinity. The argument is
scheme-theoretic and does not require all roots to be simple.

## Why this is surprising

Multiplication of binary forms gives an abundant family of finite incidence
covers. Tangency removes ramification in a geometrically natural way. One
might expect affine examples to occur sporadically in larger degrees. Instead,
the cubic chart is isolated by two robust global invariants.

The affine-space requirement is therefore much more restrictive than finding
an étale open inside a finite cover. Any broader construction of Keller maps
must solve an affineness problem of comparable strength.

## Where the classification stops

The theorem covers tangent nonosculating hyperplanes in the stated two-block
multiplication construction. Osculating hyperplanes and other incidence
constructions remain outside its scope.

[Proof and status](evidence-ledger.md#the-cubic-two-block-chart){ .evidence-link }
