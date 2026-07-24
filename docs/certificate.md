---
title: Exact counterexample certificate
description: The displayed map, determinant identity, collision, and dimensional consequence.
---

# Exact counterexample certificate

This page isolates the finite algebraic data needed to refute the classical conjecture in dimension three. It is a reading certificate, not a new independent verification.

## The map

Put \(A=1+xy\) and define \(F=(P,Q,R)\) by
\[
P=A^3z+y^2A(4+3xy),\qquad
Q=y+3xA^2z+3xy^2(4+3xy),\qquad
R=2x-3x^2y-x^3z.
\]
This is the map referred to below.

## The two exact checks

1. **Constant Jacobian.** The displayed Alpöge polynomial map has Jacobian determinant equal to the constant -2. [Constant Jacobian determinant of the Alpöge map](claim-v3/alpoge-map-constant-jacobian.md)
2. **Failure of injectivity.** The three distinct rational points (0,0,-1/4), (1,-3/2,13/2), and (-1,3/2,13/2) have the common image (-1/4,0,0) under the Alpöge map. [An explicit triple collision](claim-v3/alpoge-map-triple-collision.md)

| Input | Common output |
|---|---|
| \((0,0,-1/4)\) | \((-1/4,0,0)\) |
| \((1,-3/2,13/2)\) | \((-1/4,0,0)\) |
| \((-1,3/2,13/2)\) | \((-1/4,0,0)\) |

Because the determinant is nonzero and constant, the map satisfies the hypothesis. Because the three inputs are distinct, the map is not injective and therefore cannot be a polynomial automorphism.

## Higher dimensions

For every \(n>3\), take \(F\times\operatorname{id}_{\mathbb A^{n-3}}\). Its Jacobian determinant is still \(-2\), and the displayed collision remains after appending the same extra coordinates. Thus the conjecture is false in every dimension at least three.

See the normalized dimensional claim: [Failure of the Jacobian conjecture in dimensions at least three](claim-v3/jacobian-conjecture-false-dimension-at-least-three.md).

## Boundary of the certificate

- It says nothing against the two-dimensional conjecture, which [remains open](claim-v3/plane-jacobian-conjecture-open.md).
- It does not establish every geometric, arithmetic, or downstream claim associated with the counterexample.
- Source proofs, executable checks, and Lean formalizations are listed on the individual claim pages. Their presence is distinct from an independent full-scope project verification.

[Back to the overview](overview-v2.md)
