---
title: "Exact finite-field fiber counts"
description: "Over every finite field F_q of odd order, every rational fiber has size 0, 1, or 3; writing N_j for the number of targets with j rational preimages, N_1+3N_3=q^3 and N_0=2N_3, with 6N_3=(q-1)(q^2+2) outside characteristic 3 and 6N_3=q^2(q-1) in characteristic 3."
---

# Exact finite-field fiber counts

Over every finite field F_q of odd order, every rational fiber has size 0, 1, or 3; writing N_j for the number of targets with j rational preimages, N_1+3N_3=q^3 and N_0=2N_3, with 6N_3=(q-1)(q^2+2) outside characteristic 3 and 6N_3=q^2(q-1) in characteristic 3.

**Status:** Proof offered — review pending<br>
**Primary source:** [Alejandro Radisic's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559)<br>
**Reviewed:** 2026-07-22

## Scope

The determinant-one rescaling of the counterexample over finite fields of odd cardinality.

## Credit

Alejandro Radisic

<details>
<summary>Full credit and attribution basis</summary>

- **Alejandro Radisic** — proof, formalization; credited by the source. stated and formalized the exact finite-field counts

</details>

## Evidence

### Lean formalization

**Full proof offered.** Radisic states the exact formulas and supplies a pinned Lean formalization in Counting.lean.

What this evidence does not settle:

- The repository reports an AI-assisted development. Credit here follows the signed public comment and repository authorship; no more granular human/AI labor split is public.

## Review record

This guide has not yet recorded an independent expert or machine check covering the whole claim.

## Limitations

- The pinned theorem inventory was inspected, but no fresh Lean build was run for this guide.

## Sources

- [Counting.lean (Lean source)](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/Alpoge/Counting.lean)
- [Alejandro Radisic's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559) — primary

[Back to the claim inventory](../claims.md)
