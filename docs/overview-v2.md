---
title: Guide to the Jacobian Conjecture
description: The conjecture, the three-dimensional counterexample, and a source-linked claim record.
---

# Guide to the Jacobian Conjecture

The classical Jacobian conjecture asked whether a polynomial self-map of complex affine space with nonzero constant Jacobian determinant must have a polynomial inverse. A three-dimensional counterexample announced by Levent Alpöge in July 2026 shows that the answer is no in every dimension at least three. The plane case remains open.

## Status by dimension

- **Dimension 1:** true. A one-variable polynomial with nonzero constant derivative is linear.
- **Dimension 2:** [open](claim-v3/plane-jacobian-conjecture-open.md).
- **Dimensions 3 and above:** [false](claim-v3/jacobian-conjecture-false-dimension-at-least-three.md).

## The counterexample in one screen

Put \(A=1+xy\) and define \(F=(P,Q,R)\) by
\[
P=A^3z+y^2A(4+3xy),\qquad
Q=y+3xA^2z+3xy^2(4+3xy),\qquad
R=2x-3x^2y-x^3z.
\]
This is the map referred to below.

Two exact facts do the work: [the Jacobian determinant is the constant −2](claim-v3/alpoge-map-constant-jacobian.md), and [three distinct rational points have one common image](claim-v3/alpoge-map-triple-collision.md). The second fact prevents injectivity; the first satisfies the Keller hypothesis. Adding identity coordinates gives counterexamples in every higher dimension.

[Read the exact certificate](certificate.md){ .md-button .md-button--primary }
[Browse the claim inventory](claims-v3.md){ .md-button }

## What this site records

The guide separates mathematical claims from the sources that state or support them, the people credited for specific roles, and any independent review or machine check. **Proof offered** means that a linked source supplies an argument. It does not mean this project has independently verified the whole statement.

The [chronology](chronology-v2.md) links dated events, contribution records, and claims in both directions. Longer methodology and mathematical storylines are intentionally deferred until the underlying record has settled.
