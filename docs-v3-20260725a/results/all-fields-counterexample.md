---
title: "A Counterexample Over Every Field"
description: "For every field k, the determinant-one rescaled construction formalized by Dean Cureton gives a polynomial map from k^3 to k^3 that is not injective."
---

# A Counterexample Over Every Field

<p class="dek">For every field k, the determinant-one rescaled construction formalized by Dean Cureton gives a polynomial map from k^3 to k^3 that is not injective.</p>

<span class="status status-kind">Result</span> <span class="status status-draft">Established public record</span>

**Credited to Akhil Mathew (problem suggestion); Levent Alpöge (discovery, construction); Alejandro Radisic (formalization); Dean Cureton (formalization), and 2 others.**

**Source coverage:** Public sources are linked below. No claim is made that one of the six working manuscripts is the source for this page.

## The central idea

The theorem-level package is centered on the following mechanism: For every field k, the determinant-one rescaled construction formalized by Dean Cureton gives a polynomial map from k^3 to k^3 that is not injective.  Its supporting records isolate the ingredients that establish the statement and the qualifications that control its scope.

## For a first reading

Begin with the precise statement, then use the component statements as a map of the argument.  They separate the main assertion from proof ingredients, examples, qualifications, and corrections without requiring the reader to reconstruct the development from a claim ledger.

## Precise statement

For every field k, the determinant-one rescaled construction formalized by Dean Cureton gives a polynomial map from k^3 to k^3 that is not injective.

## Proof idea and technical structure

### A determinant-one counterexample over every field

For every field k, the determinant-one rescaled construction formalized by Dean Cureton gives a polynomial map from k^3 to k^3 that is not injective.

*Defining · Primary Statement · proof offered*

[Open the deeper technical record](../technical/a-determinant-one-counterexample-over-every-field-b7122324.md)

### Constant Jacobian determinant of the Alpöge map

The displayed Alpöge polynomial map has Jacobian determinant equal to the constant -2.

*Shared · Proof Lemma · proof offered*

[Open the deeper technical record](../technical/constant-jacobian-determinant-of-the-alp-ge-map-561802fa.md)

### An explicit triple collision

The three distinct rational points (0,0,-1/4), (1,-3/2,13/2), and (-1,3/2,13/2) have the common image (-1/4,0,0) under the Alpöge map.

*Shared · Proof Lemma · proof offered*

[Open the deeper technical record](../technical/an-explicit-triple-collision-e4fa4cbb.md)

### Failure of the Jacobian conjecture in dimensions at least three

The Jacobian conjecture is false in every dimension n at least 3.

*Shared · Supporting Result · proof offered*

[Open the deeper technical record](../technical/failure-of-the-jacobian-conjecture-in-dimensions-at-least-three-d82b1d43.md)

## Manuscripts and external links

- [jacobian — deancureton](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88)
- [alpoge-lean v0.4.0 documentation — Alejandro Radisic](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/README.md)
- [alpoge-lean v0.4.0 — Alejandro Radisic](https://github.com/alerad/alpoge-lean/releases/tag/v0.4.0)
- [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf)
- [Hello there the Jacobian conjecture is false](https://x.com/__alpoge__/status/2079028340955197566)
- [Pinned source on github.com](https://github.com/alerad/alpoge-lean/tree/b39e3bf3493939db11b0f78c5b369dd028093f0f)
- [feat: add Jacobian disproof — Paul Lezeau](https://github.com/google-deepmind/formal-conjectures/pull/4474)
- [feat(JacobianConjecture): sorry-free refutation at n = 3 over Q — techno-optimist](https://github.com/google-deepmind/formal-conjectures/pull/4486)

## Connects to

- [The Three-Dimensional Counterexample](base-counterexample-and-immediate-consequences.md)
- [Consequences for Neighboring Conjectures](consequences-for-neighboring-conjectures.md)

## Evidence, review, and detailed credit

**Evidence present:** counterexample, exact certificate, formalization, proof.

**Independent review:**

- Machine Check: The source uses one collision when the characteristic is not two and a separate collision in characteristic two.
- Machine Check: Formalization.
- Machine Check: The pinned README identifies the relevant Lean theorems and reports no `sorry` and no axioms beyond Mathlib. No fresh `lake build` was run for this guide.
- Machine Check: Lean formalization.
- Machine Check: Independent lean formalization.

**Detailed credit:**

- Akhil Mathew: problem suggestion; attributed by source — problem suggestion as reported by the source
- Alejandro Radisic: formalization; attributed by source — author and maintainer of the pinned Lean development
- Dean Cureton: formalization; documented authorship — Contribution recorded in Lean counterexamples to the Jacobian conjecture over all fields.
- Levent Alpöge: discovery, construction; attributed by source — formula announced by the named person
- Paul Lezeau: formalization; documented authorship — Contribution recorded in Formal Conjectures PR 4474 — Jacobian disproof.
- techno-optimist: formalization; documented authorship — Contribution recorded in Formal Conjectures PR 4486 — sorry-free refutation over Q.

**AI assistance:**

- Fable: research assistance; work leading to the example as reported by the source
- Responsible human(s): Levent Alpöge

??? info "Registry details"
    Release state: `public`

    Visibility: `catalogued`

    Source form: announcement, repository

    Manuscript coverage: `not_applicable`

    `complete` records have audited exact locators; `manuscript_attached` records are included without requiring page-level locator bookkeeping.

    Grouped members: 4

    Canonical registry: v8

[Back to all results and open problems](../research.md)
