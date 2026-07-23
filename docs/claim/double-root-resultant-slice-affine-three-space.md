---
title: "The double-root resultant slice is affine three-space"
description: "In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space."
---

# The double-root resultant slice is affine three-space

In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space.

**Status:** Proof offered — review pending<br>
**Primary source:** [A digestion of the Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)<br>
**Reviewed:** 2026-07-22

## Scope

The double-root hyperplane slice in the binary-linear-times-binary-quadratic multiplication model.

## Credit

Levent Alpöge, Terence Tao, Andy Jiang; AI assistance: ChatGPT; +6 more

<details>
<summary>Full credit and attribution basis</summary>

- **Alejandro Radisic** — formalization; credited by the source. Lean formalization
- **Andy Jiang** — problem suggestion; credited by the source. prompted the ChatGPT run that Sawin credits for the geometric construction; prompted the ChatGPT construction according to Sawin's earlier comment
- **ChatGPT** (AI system) — research assistance; credited by the source. AI system credited by Sawin for the geometric construction and initial chart calculation; credited by Sawin in the linked earlier discussion for the initial calculation
- **Daniel Litt** — proof; credited by the source. independent affine-line-bundle argument, as reported by Ravi Vakil
- **David Speyer** — proof; credited by the source. general iterated affine-line-bundle lemma and proof guidance
- **Levent Alpöge** — construction; credited by the source. underlying counterexample map
- **Lillian Ryan Uhl** — verification; credited by the source. identified and supplied the corrected substitution
- **Ravi Vakil** — exposition; credited by the source. public report of Litt's independent argument
- **Terence Tao** — proof, exposition; credited by the source. expository proof and explicit coordinate digestion; explicit polynomial chart formalized by the module
- **Will Sawin** — proof; credited by the source. reported the geometric construction and affine-chart calculation publicly; stated the reduction and affine-line fiber proof; public iterated affine-line-bundle argument; coordinate reduction credited in the pinned repository

</details>

## Evidence

### Lean formalization

**Partial support.** The pinned Lean module formalizes the coordinate content of the Tao–Sawin affine-slice proof; it does not claim a scheme-level isomorphism or formalize the cohomological torsor argument.

What this evidence does not settle:

- This is K-point equivalence over fields with 2 invertible, not the full scheme/cohomological statement.

### Exact certificate

**Partial support.** Lillian Ryan Uhl identified the needed root-translating substitution; Tao's public post now uses the corrected translation.

What this evidence does not settle:

- The WordPress API leaves the author-name field blank; the comment is signed 'Lillian Ryan Uhl', which is the basis for credit.

### Proof

**Full proof offered.** Tao gives explicit coordinates; the linked public discussion gives coordinate and affine-bundle proofs.

What this evidence does not settle:

- The labor split before Sawin's public report cannot be reconstructed beyond Sawin's own attribution. This record does not convert an AI-system credit into human authorship or priority.

### Proof

**Full proof offered.** A concise proof of the affine-three-space chart, stated by Will Sawin in the Tao thread and consistent with the earlier linked construction.

What this evidence does not settle:

- The exact Tao-thread argument is Sawin's signed comment. The AI/Andy Jiang note records Sawin's own provenance statement and should not be sharpened further without a released transcript.

### Proof

**Full proof offered.** Publicly argued in the linked Secret Blogging Seminar thread. David Speyer supplied the general iterated-affine-line-bundle lemma; Will Sawin developed the bundle structure; Ravi Vakil records an independent argument by Daniel Litt.

What this evidence does not settle:

- Litt's credit is second-hand in this archived source; the linked X post is the direct source if a more exact priority record is later needed.

## Review record

This guide has not yet recorded an independent expert or machine check covering the whole claim.

## Limitations

- The pinned Lean development proves a field-valued polynomial bijection, not the full scheme-level or cohomological statement.

## Notes

- Felipe raised a coefficient-normalization question about the factorial convention for a differential operator. It does not challenge the explicit final map; the convention should be checked against the full coordinate equations before changing the exposition. [Source](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693557)

## Sources

- [alpoge-lean v0.4.0 documentation](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/README.md)
- [Slice.lean (Lean source)](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/Alpoge/Slice.lean)
- [Will Sawin's comment](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27948)
- [David Speyer's comment](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27951)
- [Will Sawin's comment](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27953)
- [Ravi Vakil's comment](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27958)
- [Lillian Ryan Uhl's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693549)
- [Will Sawin's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693551)
- [Felipe's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693557)
- [A digestion of the Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) — primary

[Back to the claim inventory](../claims.md)
