---
title: "Characteristic Three Degeneration"
description: "Over an algebraically closed field of characteristic 3, the map is surjective while remaining étale and noninjective."
---

# Characteristic Three Degeneration

<p class="dek">Over an algebraically closed field of characteristic 3, the map is surjective while remaining étale and noninjective.</p>

<span class="status status-kind">Result</span> <span class="status status-draft">Established public record</span>

**Credited to Alejandro Radisic (derivation, proof, formalization).**

**Source coverage:** Public sources are linked below. No claim is made that one of the six working manuscripts is the source for this page.

## The central idea

The theorem-level package is centered on the following mechanism: In characteristic 3, the translation T=b+S puts the fiber cubic into the form cS^3+S^2+W; the missed curve is empty and the triple-root stratum disappears.  Its supporting records isolate the ingredients that establish the statement and the qualifications that control its scope.

## For a first reading

Begin with the precise statement, then use the component statements as a map of the argument.  They separate the main assertion from proof ingredients, examples, qualifications, and corrections without requiring the reader to reconstruct the development from a claim ledger.

## Precise statement

Over an algebraically closed field of characteristic 3, the map is surjective while remaining étale and noninjective.

## Proof idea and technical structure

### Characteristic-three degeneration

In characteristic 3, the translation T=b+S puts the fiber cubic into the form cS^3+S^2+W; the missed curve is empty and the triple-root stratum disappears.

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/characteristic-three-degeneration-cc864a73.md)

### Surjectivity in algebraically closed characteristic three

Over an algebraically closed field of characteristic 3, the map is surjective while remaining étale and noninjective.

*Defining · Primary Statement · proof offered*

[Open the deeper technical record](../technical/surjectivity-in-algebraically-closed-characteristic-three-eb33dc0c.md)

## Manuscripts and external links

- [CharThree.lean (Lean source) — Alejandro Radisic](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/Alpoge/CharThree.lean)
- [Alejandro Radisic's comment — Alejandro Radisic](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559)
- [alpoge-lean v0.4.0 documentation — Alejandro Radisic](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/README.md)

## Connects to

- [A Counterexample Over Every Field](all-fields-counterexample.md)
- [The Three-Dimensional Counterexample](base-counterexample-and-immediate-consequences.md)
- [Base Map Fibers Image And Nonproperness](base-map-fibers-image-and-nonproperness.md)

## Evidence, review, and detailed credit

**Evidence present:** formalization, proof.

**Independent review:**

- Machine Check: The counterexample and its fiber cubic over fields of characteristic 3.

**Detailed credit:**

- Alejandro Radisic: derivation, proof, formalization; attributed by source — stated the consequence and disclosed its formalization boundary; stated and formalized the characteristic-three degeneration

??? info "Registry details"
    Release state: `public`

    Visibility: `catalogued`

    Source form: announcement, repository

    Manuscript coverage: `not_applicable`

    Complete coverage requires an audited LaTeX locator for every defining claim.

    Grouped members: 2

    Canonical registry: v7

[Back to all results and open problems](../research.md)
