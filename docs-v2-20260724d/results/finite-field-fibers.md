---
title: "Finite Field Fibers"
description: "Over every finite field F_q of odd order, every rational fiber has size 0, 1, or 3; writing N_j for the number of targets with j rational preimages, N_1+3N_3=q^3 and N_0=2N_3, with 6N_3=(q-1)(q^2+2) outside characteristic 3 and 6N_3=q^2(q-1) in characteristic 3."
---

# Finite Field Fibers

<p class="dek">Over every finite field F_q of odd order, every rational fiber has size 0, 1, or 3; writing N_j for the number of targets with j rational preimages, N_1+3N_3=q^3 and N_0=2N_3, with 6N_3=(q-1)(q^2+2) outside characteristic 3 and 6N_3=q^2(q-1) in characteristic 3.</p>

<span class="status status-kind">Result</span> <span class="status status-draft">Established public record</span>

**Credited to Alejandro Radisic (derivation, formalization, proof).**

## The central idea

The theorem-level package is centered on the following mechanism: Over every finite field F_q of odd order, every rational fiber has size 0, 1, or 3; writing N_j for the number of targets with j rational preimages, N_1+3N_3=q^3 and N_0=2N_3, with 6N_3=(q-1)(q^2+2) outside characteristic 3 and 6N_3=q^2(q-1) in characteristic 3.  Its supporting records isolate the ingredients that establish the statement and the qualifications that control its scope.

## For a first reading

Begin with the precise statement, then use the component statements as a map of the argument.  They separate the main assertion from proof ingredients, examples, qualifications, and corrections without requiring the reader to reconstruct the development from a claim ledger.

## Precise statement

Over every finite field F_q of odd order, every rational fiber has size 0, 1, or 3; writing N_j for the number of targets with j rational preimages, N_1+3N_3=q^3 and N_0=2N_3, with 6N_3=(q-1)(q^2+2) outside characteristic 3 and 6N_3=q^2(q-1) in characteristic 3.

## Proof idea and technical structure

### Exact finite-field fiber counts

Over every finite field F_q of odd order, every rational fiber has size 0, 1, or 3; writing N_j for the number of targets with j rational preimages, N_1+3N_3=q^3 and N_0=2N_3, with 6N_3=(q-1)(q^2+2) outside characteristic 3 and 6N_3=q^2(q-1) in characteristic 3.

*Defining · Primary Statement · proof offered*

[Open the deeper technical record](../technical/exact-finite-field-fiber-counts-859b7e20.md)

### Asymptotic S3 fiber distribution

The normalized finite-field fiber-count distribution (N_0,N_1,N_3)/q^3 tends to (1/3,1/2,1/6), matching the proportions of elements of S3 with 0, 1, and 3 fixed points.

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/asymptotic-s3-fiber-distribution-689c15c4.md)

## Manuscripts and external links

- [Counting.lean (Lean source) — Alejandro Radisic](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/Alpoge/Counting.lean)
- [Alejandro Radisic's comment — Alejandro Radisic](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559)

## Connects to

- [A Counterexample Over Every Field](all-fields-counterexample.md)
- [The Three-Dimensional Counterexample](base-counterexample-and-immediate-consequences.md)
- [Base Map Fibers Image And Nonproperness](base-map-fibers-image-and-nonproperness.md)

## Evidence, review, and detailed credit

**Evidence present:** formalization.

**Independent review:**

- Machine Check: The determinant-one rescaling of the counterexample over finite fields of odd cardinality.
- Machine Check: The asymptotic consequence of the exact finite-field formulas as q grows through odd prime powers.

**Detailed credit:**

- Alejandro Radisic: derivation, formalization, proof; attributed by source — finite-field count and S3 fixed-point interpretation; stated and formalized the exact finite-field counts

??? info "Registry details"
    Release state: `public`

    Visibility: `catalogued`

    Source form: announcement, repository

    Grouped members: 2

    Canonical registry: v7

[Back to all results and open problems](../research.md)
