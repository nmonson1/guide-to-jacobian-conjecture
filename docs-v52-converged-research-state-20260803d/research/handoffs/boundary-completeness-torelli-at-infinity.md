---
title: "Model research brief — Torelli data on the projective resultant boundary"
description: "A self-contained mathematical handoff for a research model."
---

# Torelli data on the projective resultant boundary

<p class="claim-tag">Lane 2 · Updated 3 August 2026</p>

Lane 2 · 2026-08-03

## Scope

Complete the projective-infinity part of the polynomial-remainder-sequence
(PRS) boundary. The finite ordered and unordered quintic charts, including
finite $T=0$ coordinates, are already known; the frontier is normalization
and gluing on the outer $T=0$ charts.

## Setup and definitions

For binary forms $f,g$, the PRS graph records successive remainders together
with all-rank principal subresultant coefficients. Hankel and Schur coordinates
are alternative determinantal presentations of the same finite flag. The
projective parameter $T$ homogenizes the outer scaling; $T=0$ is the
infinity boundary, not the finite zero-resultant divisor.

The ordered outer resolution remembers the ordered roots; the unordered
normalization quotients the symmetric action. A Torelli statement here means
that the normalized boundary data recover the intended marked polynomial
pair, with conductor and overlap maps included.

## Results to use

- The all-rank PSC/Hankel/Schur identities and conventions are exact.
- The finite five-by-five PRS flag, ordered outer resolution, unordered
  normalization, and finite $T=0$ coordinate theorem are exact on their
  declared charts.
- A fresh fail-closed audit replays that finite $T=0$ theorem and confirms
  that the multihomogeneous coordinates, saturated equations, and overlap
  maps for both projective-infinity charts are not present in the current
  packet. Clearing affine denominators would not define their graph closures.
- No current theorem normalizes both projective-infinity $T=0$ charts or
  proves their separated gluing to the finite atlas.

## Example: a finite T=0 point

Keeping the normalized leading remainder while setting the homogenizing
coordinate to zero produces a legitimate finite chart coordinate. It is an
example of the known theorem, not a proxy for the outer projective chart where
additional scale directions survive.

## Live problem

Construct the two outer $T=0$ normalization charts, their conductor ideals,
and their overlap with the finite ordered/unordered PRS atlas. The result
should decide exactly which boundary data retain Torelli recovery.

## Tasks

### L2-T1 — Normalize and glue the outer infinity charts

Inputs: the [all-rank PRS packet](lane-2-source-packet.md),
the [finite ordered-chart packet](lane-2-source-packet.md),
the [finite T=0 theorem](lane-2-source-packet.md),
and [stable-moduli TeX](../proof-sources/04-stable-moduli/main.md).
The [projective-infinity input audit](lane-2-source-packet.md)
gives the exact missing-input contract.

Deliverable: equations for both outer normalizations, normality proofs,
conductor ideals, explicit transition maps on every overlap, and a separated
gluing proof or the exact first failed separation equation.

Dependencies: the fixed PSC sign/order conventions and the symmetric quotient
used by the finite atlas.

Limits: a finite $T=0$ calculation does not cover projective infinity;
normality on each chart alone does not prove separated global gluing.

Alternative connections: a chart-groupoid formulation linked to Lane 9 is
welcome if its arrows include inverse and cocycle formulas.

## Limits

The known boundary theorems are finite-chart theorems. No global Torelli or
properness claim follows until the two infinity complements are routed.

## Direct sources

- [Retained all-rank theorem RMU-4D2E0010](../working-mathematics/units/RMU-4D2E0010.md)
- [Retained projective PRS construction RMU-4D2E0002](../working-mathematics/units/RMU-4D2E0002.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-2-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
