---
title: "Cubic Homogeneous Descendant Construction"
description: "The explicit constructions give the upper bound N_min <= 19 for cubic-homogeneous counterexamples; the conversation uses the elementary no-collinear-collision argument for the lower bound N_min >= 5."
---

# Cubic Homogeneous Descendant Construction

<p class="dek">The explicit constructions give the upper bound N_min <= 19 for cubic-homogeneous counterexamples; the conversation uses the elementary no-collinear-collision argument for the lower bound N_min >= 5.</p>

<span class="status status-kind">Result</span> <span class="status status-draft">Working draft</span>

**Credited to Nathaniel Monson (research direction and mathematical responsibility); Spacerat (computation); William Thompson (computation).**

**Source coverage:** Public sources are linked below. The linked working manuscript contains this research line. Exact private LaTeX locators are intentionally not part of the public presentation.

## The central idea

The theorem-level package is centered on the following mechanism: The cited explicit map has the form G(U)=U+H(U) over Q^24, with every nonzero component of H homogeneous cubic, determinant 1, 54 nonzero cubic monomials, and a displayed collision of two distinct rational points.  Its supporting records isolate the ingredients that establish the statement and the qualifications that control its scope.

## For a first reading

Begin with the precise statement, then use the component statements as a map of the argument.  They separate the main assertion from proof ingredients, examples, qualifications, and corrections without requiring the reader to reconstruct the development from a claim ledger.

## Precise statement

The explicit constructions give the upper bound N_min <= 19 for cubic-homogeneous counterexamples; the conversation uses the elementary no-collinear-collision argument for the lower bound N_min >= 5.

## Proof idea and technical structure

### An explicit cubic-homogeneous counterexample in 24 variables

The cited explicit map has the form G(U)=U+H(U) over Q^24, with every nonzero component of H homogeneous cubic, determinant 1, 54 nonzero cubic monomials, and a displayed collision of two distinct rational points.

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/an-explicit-cubic-homogeneous-counterexample-in-24-variables-4bb50bb3.md)

### Explicit Counterexample: Starting from the public 11D counterexample, rank-sensitive cubic suspension yields an explic…

Starting from the public 11D counterexample, rank-sensitive cubic suspension yields an explicit 19D cubic-homogeneous Keller counterexample with collision.

*Defining · Supporting Result · recorded*

[Open the deeper technical record](../technical/explicit-counterexample-starting-from-the-public-11d-counterexample-rank-sensitive-cubic-suspension-38caab66.md)

### Superseded Construction: The earlier 26D cubic-homogeneous and 158D Druzkowski constructions remain valid explicit exa…

The earlier 26D cubic-homogeneous and 158D Druzkowski constructions remain valid explicit examples but are superseded as upper bounds by the later 19D and 135D examples.

*Defining · Superseded Construction · recorded*

[Open the deeper technical record](../technical/superseded-construction-the-earlier-26d-cubic-homogeneous-and-158d-druzkowski-constructions-remain-48d22f23.md)

### General Reduction Lemma: For an n-dimensional degree-at-most-three map whose quadratic span has rank r, a block-determ…

For an n-dimensional degree-at-most-three map whose quadratic span has rank r, a block-determinant suspension produces a cubic-homogeneous map in dimension n+r+1.

*Defining · Proof Lemma · proof offered*

[Open the deeper technical record](../technical/general-reduction-lemma-for-an-n-dimensional-degree-at-most-three-map-27af15aa.md)

### Jordan Structure: For the 19D example, the generic Jacobian perturbation JH has Jordan type (18,1); nonzero sca…

For the 19D example, the generic Jacobian perturbation JH has Jordan type (18,1); nonzero scalar fibers are conjugate and the zero fiber is an automorphism degeneration.

*Defining · Supporting Result · recorded*

[Open the deeper technical record](../technical/jordan-structure-for-the-19d-example-the-generic-jacobian-perturbation-jh-has-7affff85.md)

### Dimension Bound: The explicit constructions give the upper bound N_min <= 19 for cubic-homogeneous counterexam…

The explicit constructions give the upper bound N_min <= 19 for cubic-homogeneous counterexamples; the conversation uses the elementary no-collinear-collision argument for the lower bound N_min >= 5.

*Defining · Primary Statement · proof offered*

[Open the deeper technical record](../technical/dimension-bound-the-explicit-constructions-give-the-upper-bound-n-min-19-0edd5ae2.md)

### A straightforward explicit reduction produced a cubic-homogeneous map in \(79\) variables and…

A straightforward explicit reduction produced a cubic-homogeneous map in \(79\) variables and a Drużkowski cubic-linear map in \(426\) variables.

*Defining · Supporting Result · recorded*

[Open the deeper technical record](../technical/a-straightforward-explicit-reduction-produced-a-cubic-homogeneous-map-in-79-variables-b7744f4c.md)

### Rees Suspension Equivalence: The rank-sensitive cubic suspension is triangularly left-right equivalent to (X,v,t) mapped b…

The rank-sensitive cubic suspension is triangularly left-right equivalent to (X,v,t) mapped by (t^{-1}K(tX),v,t); it preserves generic degree and the geometric Galois closure after adjoining transcendental variables.

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/rees-suspension-equivalence-the-rank-sensitive-cubic-suspension-is-triangularly-left-right-d1eb696a.md)

### Minimal Output Mode Suspension: The n+r+1 cubic suspension is coordinate-free on V plus the dual of the output-mode span plus…

The n+r+1 cubic suspension is coordinate-free on V plus the dual of the output-mode span plus one scalar, and r=rank(C^flat) is the minimum possible auxiliary dimension for any factorization of the cubic tensor through an intermediate vector space.

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/minimal-output-mode-suspension-the-n-r-1-cubic-suspension-is-coordinate-f701e994.md)

### An explicit degree-three counterexample in 11 variables

The cited map from complex affine 11-space to itself has total degree 3, 52 nonzero monomial terms, constant Jacobian determinant -2, and three displayed distinct rational inputs with one common image.

*Shared · Supporting Result · proof offered*

[Open the deeper technical record](../technical/an-explicit-degree-three-counterexample-in-11-variables-a39e3ccd.md)

### Open Question: What is the true smallest dimension of a cubic-homogeneous counterexample?

What is the true smallest dimension of a cubic-homogeneous counterexample?

*Shared · Open Question · open*

[Open the deeper technical record](../technical/open-question-what-is-the-true-smallest-dimension-of-a-cubic-homogeneous-ddaf375f.md)

### Explicit Common S3 Cover: The original three-variable map has the displayed invariant quotient cubic theta^3-2theta^2+B…

The original three-variable map has the displayed invariant quotient cubic theta^3-2theta^2+Btheta-2A, whose irreducibility and nonsquare discriminant give generic Galois group S3; the descendant ladder presents this same three-sheeted cover.

*Shared · Supporting Result · recorded*

[Open the deeper technical record](../technical/explicit-common-s3-cover-the-original-three-variable-map-has-the-displayed-8aa6a8c5.md)

## Manuscripts and external links

- [Normal-Form Complexity of a Three-Sheeted Keller Map](../assets/manuscripts/05-homogeneous-descendants-2026-07-22-v3.pdf) — Nathaniel Monson, 2026-07-22; working manuscript; contains this result or its supporting argument; SHA-256 `2e6d293f0f2a6bdf53b2d763ba23cb845b233d49c93d6b13576cdf287748415f`
- [explicit-cubic-homogeneous-jacobian-counterexample — William Thompson](https://github.com/wtho704/explicit-cubic-homogeneous-jacobian-counterexample/tree/45a7616fdf5a20c065564f2676190093722696b9)
- [Zenodo record 21466221 — William Thompson](https://zenodo.org/records/21466221)
- [11 variable cubic jacobian conjecture counterexample — Spacerat](https://gist.github.com/Spacerat/08b4a43f6b6ca57178efabc220170ce8/2224dace71e8763a8621a7f557bbc545a53aa820)

## Connects to

- [Base Cover Monodromy And Deck Group](base-cover-monodromy-and-deck-group.md)
- [The Common Cover of the Descendant Ladder](common-cover-of-the-descendant-ladder.md)
- [Drużkowski Pairing](druzkowski-pairing.md)
- [The Explicit Eleven-Dimensional Cubic Counterexample](eleven-dimensional-cubic-counterexample.md)
- [A 38-Dimensional Hessian Quartic from Five Reduction Strategies](hessian-quartic-five-attacks.md)
- [Mathieu Correction And Valid Consequence](mathieu-correction-and-valid-consequence.md)
- [The Minimum Dimension for a Cubic-Homogeneous Counterexample](minimum-cubic-homogeneous-dimension.md)
- [Bounds and Obstructions for Symmetric Dilations](symmetric-dilation-bounds.md)

## Evidence, review, and detailed credit

**Evidence present:** computation, exact certificate, proof.

**Independent review:**

- None Recorded: No independent review is represented in this public record.

**Detailed credit:**

- Nathaniel Monson: research direction and mathematical responsibility; attributed by source
- Spacerat: computation; documented authorship — Contribution recorded in An explicit degree-three Jacobian counterexample in 11 variables.
- William Thompson: computation; documented authorship — Contribution recorded in An explicit 24-variable cubic-homogeneous Jacobian counterexample.

**AI assistance:**

- ChatGPT: derivation and drafting; research assistance
- ChatGPT: research assistance; explicit construction, simplification, and verification code
- Responsible human(s): Nathaniel Monson, Spacerat

??? info "Registry details"
    Release state: `draft_public`

    Visibility: `catalogued`

    Source form: repository, working manuscript

    Manuscript coverage: `manuscript_attached`

    `complete` records have audited exact locators; `manuscript_attached` records are included without requiring page-level locator bookkeeping.

    Grouped members: 12

    Canonical registry: v8

[Back to all results and open problems](../research.md)
