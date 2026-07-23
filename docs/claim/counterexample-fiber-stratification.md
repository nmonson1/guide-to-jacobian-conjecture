---
title: "Generic degree and fiber stratification of the counterexample"
description: "The Alpöge map has generic degree 3, with affine fiber cardinality 3 off the cubic discriminant, 1 on the discriminant away from the triple-root curve, and 0 on the triple-root curve."
---

# Generic degree and fiber stratification of the counterexample

The Alpöge map has generic degree 3, with affine fiber cardinality 3 off the cubic discriminant, 1 on the discriminant away from the triple-root curve, and 0 on the triple-root curve.

**Status:** Proof offered — review pending<br>
**Primary source:** [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf)<br>
**Reviewed:** 2026-07-22

## Credit

Levent Alpöge, Will Sawin, Terence Tao; AI assistance: ChatGPT; +2 more

<details>
<summary>Full credit and attribution basis</summary>

- **Alejandro Radisic** — formalization; credited by the source. author and maintainer of the pinned Lean development
- **Andy Jiang** — problem suggestion; credited by the source. prompted the ChatGPT run that Sawin credits for the geometric construction
- **ChatGPT** (AI system) — research assistance; credited by the source. AI system credited by Sawin for the geometric construction and initial chart calculation
- **Levent Alpöge** — construction; credited by the source. underlying counterexample map
- **Terence Tao** — proof, exposition; credited by the source. expository proof and explicit coordinate digestion
- **Will Sawin** — construction; credited by the source. reported the geometric construction and affine-chart calculation publicly

</details>

## Evidence

### Proof

**Full proof offered.** Proof and explicit inverse formulas.

- [Proof and explicit inverse formulas](https://www.ulam.ai/research/jacobian.pdf)

### Lean formalization

**Full proof offered.** The pinned README identifies the relevant Lean theorems and reports no `sorry` and no axioms beyond Mathlib. No fresh `lake build` was run for this guide.

What this evidence does not settle:

- The same README expressly excludes S3 monodromy/irreducibility, the properness identification, scheme-level factorization, the cohomological torsor proof, and analytic derivative identification.

### Proof

**Partial support.** Tao's post proves the fiber analysis, while the linked public discussion develops the affine-three-space step.

What this evidence does not settle:

- The labor split before Sawin's public report cannot be reconstructed beyond Sawin's own attribution. This record does not convert an AI-system credit into human authorship or priority.

## Review record

This guide has not yet recorded an independent expert or machine check covering the whole claim.

## Limitations

- A classification of all three-sheeted Keller maps.

## Sources

- [alpoge-lean v0.4.0 documentation](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/README.md)
- [alpoge-lean v0.4.0](https://github.com/alerad/alpoge-lean/releases/tag/v0.4.0)
- [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) — primary
- [Hello there the Jacobian conjecture is false](https://x.com/__alpoge__/status/2079028340955197566)
- [Will Sawin's comment](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27948)
- [A digestion of the Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)

[Back to the claim inventory](../claims.md)
