---
title: "Why the Double-Root Slice Is Affine Three-Space"
description: "In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space."
---

# Why the Double-Root Slice Is Affine Three-Space

<p class="dek">In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space.</p>

<span class="status status-kind">Result</span> <span class="status status-draft">Established public record</span>

**Credited to Andy Jiang (problem suggestion); Levent Alpöge (construction); Daniel Litt (proof); David Speyer (proof), and 6 others.**

**Source coverage:** Public sources are linked below. No claim is made that one of the six working manuscripts is the source for this page.

## The central idea

The theorem-level package is centered on the following mechanism: In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space.  Its supporting records isolate the ingredients that establish the statement and the qualifications that control its scope.

## For a first reading

Begin with the precise statement, then use the component statements as a map of the argument.  They separate the main assertion from proof ingredients, examples, qualifications, and corrections without requiring the reader to reconstruct the development from a claim ledger.

## Precise statement

In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space.

## Proof idea and technical structure

### The double-root resultant slice is affine three-space

In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space.

*Defining · Primary Statement · proof offered*

[Open the deeper technical record](../technical/the-double-root-resultant-slice-is-affine-three-space-c5d74708.md)

### Three symmetry orbits of dual binary-cubic hyperplanes

Under the projective linear action, dual binary-cubic hyperplanes have three orbits, indexed by the root partitions (3), (2,1), and (1,1,1).

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/three-symmetry-orbits-of-dual-binary-cubic-hyperplanes-037f2bd5.md)

### Comparison with Vitushkin's 1999 rational example

Vitushkin's 1999 rational example has an analogous multiplication-map presentation and is generically two-to-one, but its source is a punctured plane, so the resulting map has a pole.

*Shared · Supporting Result · proof offered*

[Open the deeper technical record](../technical/comparison-with-vitushkin-s-1999-rational-example-aa2df6f0.md)

## Manuscripts and external links

- [alpoge-lean v0.4.0 documentation — Alejandro Radisic](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/README.md)
- [Slice.lean (Lean source) — Alejandro Radisic](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/Alpoge/Slice.lean)
- [Will Sawin's comment — Will Sawin](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27948)
- [David Speyer's comment — David Speyer](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27951)
- [Will Sawin's comment — Will Sawin](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27953)
- [Ravi Vakil's comment — Ravi Vakil](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27958)
- [Lillian Ryan Uhl's comment — Lillian Ryan Uhl](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693549)
- [Will Sawin's comment — Will Sawin](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693551)
- [Felipe's comment — Felipe](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693557)
- [A digestion of the Jacobian conjecture counterexample — Terence Tao](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [Terence Tao's comment — Terence Tao](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693529)
- [Anonymous's comment — Anonymous](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693534)
- [Terence Tao's comment — Terence Tao](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693536)

## Connects to

- [Uniqueness in the Multiplication-Incidence Construction](multiplication-incidence-uniqueness.md)
- [Comparison with Vitushkin's 1999 Rational Example](vitushkin-rational-comparison.md)

## Evidence, review, and detailed credit

**Evidence present:** exact certificate, formalization, literature result, proof.

**Independent review:**

- Machine Check: The pinned Lean module formalizes the coordinate content of the Tao–Sawin affine-slice proof; it does not claim a scheme-level isomorphism or formalize the cohomological torsor argument.

**Detailed credit:**

- Alejandro Radisic: formalization; attributed by source — Lean formalization
- Andy Jiang: problem suggestion; attributed by source — prompted the ChatGPT run that Sawin credits for the geometric construction; prompted the ChatGPT construction according to Sawin's earlier comment
- Anonymous commenter 693534: research assistance; attributed by source — pointed to Vitushkin's 1999 example
- Daniel Litt: proof; attributed by source — independent affine-line-bundle argument, as reported by Ravi Vakil
- David Speyer: proof; attributed by source — general iterated affine-line-bundle lemma and proof guidance
- Levent Alpöge: construction; attributed by source — underlying counterexample map
- Lillian Ryan Uhl: verification; attributed by source — identified and supplied the corrected substitution
- Ravi Vakil: exposition; attributed by source — public report of Litt's independent argument
- Terence Tao: derivation, exposition, proof; attributed by source — public orbit formulation and calculation; expository proof and explicit coordinate digestion; explicit polynomial chart formalized by the module
- Will Sawin: proof; attributed by source — reported the geometric construction and affine-chart calculation publicly; stated the reduction and affine-line fiber proof; public iterated affine-line-bundle argument; coordinate reduction credited in the pinned repository

**AI assistance:**

- ChatGPT: research assistance; AI system credited by Sawin for the geometric construction and initial chart calculation; credited by Sawin in the linked earlier discussion for the initial calculation
- Responsible human(s): Alejandro Radisic, Andy Jiang, Daniel Litt, David Speyer, Levent Alpöge, Lillian Ryan Uhl, Ravi Vakil, Terence Tao, Will Sawin

??? info "Registry details"
    Release state: `public`

    Visibility: `catalogued`

    Source form: announcement, repository

    Manuscript coverage: `not_applicable`

    Complete coverage requires an audited LaTeX locator for every defining claim.

    Grouped members: 3

    Canonical registry: v7

[Back to all results and open problems](../research.md)
