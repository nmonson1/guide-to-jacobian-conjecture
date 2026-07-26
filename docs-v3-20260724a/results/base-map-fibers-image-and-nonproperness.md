---
title: "Base Map Fibers Image And Nonproperness"
description: "The nonproperness hypersurface is the cubic discriminant, its singular/omitted locus is a cusp-type curve C1, and the fibers have the described 3/1/0 pattern."
---

# Base Map Fibers Image And Nonproperness

<p class="dek">The nonproperness hypersurface is the cubic discriminant, its singular/omitted locus is a cusp-type curve C1, and the fibers have the described 3/1/0 pattern.</p>

<span class="status status-kind">Result</span> <span class="status status-draft">Established public record</span>

**Credited to Andy Jiang (problem suggestion); Levent Alpöge (construction); Will Sawin (construction); Terence Tao (proof, exposition), and 1 others.**

**Source coverage:** Public sources are linked below. No claim is made that one of the six working manuscripts is the source for this page.

## The central idea

The theorem-level package is centered on the following mechanism: The Alpöge map has generic degree 3, with affine fiber cardinality 3 off the cubic discriminant, 1 on the discriminant away from the triple-root curve, and 0 on the triple-root curve.  Its supporting records isolate the ingredients that establish the statement and the qualifications that control its scope.

## For a first reading

Begin with the precise statement, then use the component statements as a map of the argument.  They separate the main assertion from proof ingredients, examples, qualifications, and corrections without requiring the reader to reconstruct the development from a claim ledger.

## Precise statement

The nonproperness hypersurface is the cubic discriminant, its singular/omitted locus is a cusp-type curve C1, and the fibers have the described 3/1/0 pattern.

## Proof idea and technical structure

### Generic degree and fiber stratification of the counterexample

The Alpöge map has generic degree 3, with affine fiber cardinality 3 off the cubic discriminant, 1 on the discriminant away from the triple-root curve, and 0 on the triple-root curve.

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/generic-degree-and-fiber-stratification-of-the-counterexample-55104ef2.md)

### Image and nonproperness set of the counterexample

The image of the Alpöge map is complex affine 3-space minus the triple-root curve Gamma, while its nonproperness set is the discriminant hypersurface V(Delta).

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/image-and-nonproperness-set-of-the-counterexample-173427e9.md)

### Fiber And Nonproperness Classification: The nonproperness hypersurface is the cubic discriminant, its singular/omitted locus is a cus…

The nonproperness hypersurface is the cubic discriminant, its singular/omitted locus is a cusp-type curve C1, and the fibers have the described 3/1/0 pattern.

*Defining · Primary Statement · proof offered*

[Open the deeper technical record](../technical/fiber-and-nonproperness-classification-the-nonproperness-hypersurface-is-the-cubic-discriminant-its-a10c42ef.md)

### Technical claim

The announced rational collision belongs to a one-parameter orbit of three-point fibers.

*Defining · Supporting Result · recorded*

[Open the deeper technical record](../technical/technical-claim-610c33b2.md)

### Invertibility and properness for complex Keller maps

For a Keller map over the complex numbers, polynomial invertibility, properness, emptiness of the nonproperness set, and codimension at least 2 of that set are equivalent, with the empty set assigned infinite codimension.

*Shared · Supporting Result · proof offered*

[Open the deeper technical record](../technical/invertibility-and-properness-for-complex-keller-maps-ed2c6665.md)

### Technical claim

The off-diagonal collision space is a smooth factorial affine threefold with trivial Picard group and unit group modulo constants \(\mathbb Z\).

*Shared · Supporting Result · certificate offered*

[Open the deeper technical record](../technical/technical-claim-e1f739d1.md)

### Technical claim

Escape rates are \(\varepsilon^{-1/2}\) near a smooth discriminant point and \(\varepsilon^{-2/3}\) near the cusp, with more degenerate arcs allowing larger half-integral exponents.

*Shared · Supporting Result · recorded*

[Open the deeper technical record](../technical/technical-claim-914949bf.md)

## Manuscripts and external links

- [alpoge-lean v0.4.0 documentation — Alejandro Radisic](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/README.md)
- [alpoge-lean v0.4.0 — Alejandro Radisic](https://github.com/alerad/alpoge-lean/releases/tag/v0.4.0)
- [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf)
- [Hello there the Jacobian conjecture is false](https://x.com/__alpoge__/status/2079028340955197566)
- [Will Sawin's comment — Will Sawin](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/#comment-27948)
- [A digestion of the Jacobian conjecture counterexample — Terence Tao](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)

## Connects to

- [The Three-Dimensional Counterexample](base-counterexample-and-immediate-consequences.md)
- [Why the Double-Root Slice Is Affine Three-Space](double-root-affine-source.md)
- [Escape Rates Near the Discriminant](escape-rates-near-the-discriminant.md)
- [Invertibility and Properness for Complex Keller Maps](keller-invertibility-and-properness.md)
- [Lost Sheet Local Models](lost-sheet-local-models.md)
- [Uniqueness in the Multiplication-Incidence Construction](multiplication-incidence-uniqueness.md)
- [The Off-Diagonal Collision Space](off-diagonal-collision-space.md)

## Evidence, review, and detailed credit

**Evidence present:** computation, formalization, literature result, proof.

**Independent review:**

- Machine Check: The pinned README identifies the relevant Lean theorems and reports no `sorry` and no axioms beyond Mathlib. No fresh `lake build` was run for this guide.

**Detailed credit:**

- Alejandro Radisic: formalization; attributed by source — author and maintainer of the pinned Lean development
- Andy Jiang: problem suggestion; attributed by source — prompted the ChatGPT run that Sawin credits for the geometric construction
- Levent Alpöge: construction; attributed by source — underlying counterexample map
- Terence Tao: proof, exposition; attributed by source — expository proof and explicit coordinate digestion
- Will Sawin: construction; attributed by source — reported the geometric construction and affine-chart calculation publicly

**AI assistance:**

- ChatGPT: research assistance; AI system credited by Sawin for the geometric construction and initial chart calculation
- Responsible human(s): Alejandro Radisic, Andy Jiang, Levent Alpöge, Terence Tao, Will Sawin

??? info "Registry details"
    Release state: `public`

    Visibility: `catalogued`

    Source form: announcement, repository

    Manuscript coverage: `not_applicable`

    `complete` records have audited exact locators; `manuscript_attached` records are included without requiring page-level locator bookkeeping.

    Grouped members: 7

    Canonical registry: v8

[Back to all results and open problems](../research.md)
