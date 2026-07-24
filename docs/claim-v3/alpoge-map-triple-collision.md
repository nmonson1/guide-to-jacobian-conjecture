---
title: "An explicit triple collision"
description: "The three distinct rational points (0,0,-1/4), (1,-3/2,13/2), and (-1,3/2,13/2) have the common image (-1/4,0,0) under the Alpöge map."
---

# An explicit triple collision

The three distinct rational points (0,0,-1/4), (1,-3/2,13/2), and (-1,3/2,13/2) have the common image (-1/4,0,0) under the Alpöge map.

**Status:** Proof offered — review pending<br>
**Primary source:** [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf)<br>
**Record assessed on:** 2026-07-22

## Definition and context

Put \(A=1+xy\) and define \(F=(P,Q,R)\) by
\[
P=A^3z+y^2A(4+3xy),\qquad
Q=y+3xA^2z+3xy^2(4+3xy),\qquad
R=2x-3x^2y-x^3z.
\]
The collision is an exact rational certificate for this map.

## Scope

The displayed rational points and the displayed map over the rational numbers, and hence over every field into which those rational data embed.

## Claim relations

Claims that use this claim:

- [Failure of the Jacobian conjecture in dimensions at least three](jacobian-conjecture-false-dimension-at-least-three.md)

## In the chronological record

- Event: [Alpöge posts the explicit three-variable counterexample](../chronology-v2.md#event-jcg-e-0007)
- Event: [A technical note gives exact checks and the binary-cubic model](../chronology-v2.md#event-jcg-e-0008)
- Contribution: [A Counterexample to the Jacobian Conjecture](../chronology-v2.md#contribution-jcg-c-0002)

## Credit

Levent Alpöge, Akhil Mathew, Alejandro Radisic; AI assistance: Fable; +1 more

<details>
<summary>Full credit and attribution basis</summary>

- **Akhil Mathew** — problem suggestion; credited by the source. problem suggestion as reported by the source
- **Alejandro Radisic** — formalization; credited by the source. author and maintainer of the pinned Lean development
- **deancureton** — formalization; documented authorship. Contribution recorded in Lean counterexamples to the Jacobian conjecture over all fields.
- **Fable** (AI system) — research assistance; credited by the source. work leading to the example as reported by the source
- **Levent Alpöge** — discovery, construction; credited by the source. formula announced by the named person

</details>

## Evidence

### Exact certificate

**Full proof offered.** Exact certificate.

- [Exact certificate](https://www.ulam.ai/research/jacobian.pdf)

### Lean formalization

**Full proof offered.** Formalization.

- [Formalization](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88)

### Lean formalization

**Full proof offered.** The pinned README identifies the relevant Lean theorems and reports no `sorry` and no axioms beyond Mathlib. No fresh `lake build` was run for this guide.

What this evidence does not settle:

- The same README expressly excludes S3 monodromy/irreducibility, the properness identification, scheme-level factorization, the cohomological torsor proof, and analytic derivative identification.

## Review record

This guide has not yet recorded an independent expert or machine check covering the whole claim.

## Limitations

- The constant-Jacobian property without a separate determinant calculation.

## Sources

- [alpoge-lean v0.4.0 documentation](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/README.md)
- [alpoge-lean v0.4.0](https://github.com/alerad/alpoge-lean/releases/tag/v0.4.0)
- [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) — primary
- [Hello there the Jacobian conjecture is false](https://x.com/__alpoge__/status/2079028340955197566)
- [jacobian](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88)

[Back to the claim inventory](../claims-v3.md)
