---
title: "Asymptotic S3 fiber distribution"
description: "The normalized finite-field fiber-count distribution (N_0,N_1,N_3)/q^3 tends to (1/3,1/2,1/6), matching the proportions of elements of S3 with 0, 1, and 3 fixed points."
---

# Asymptotic S3 fiber distribution

The normalized finite-field fiber-count distribution (N_0,N_1,N_3)/q^3 tends to (1/3,1/2,1/6), matching the proportions of elements of S3 with 0, 1, and 3 fixed points.

**Status:** Proof offered — review pending<br>
**Primary source:** [Alejandro Radisic's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559)<br>
**Reviewed:** 2026-07-22

## Scope

The asymptotic consequence of the exact finite-field formulas as q grows through odd prime powers.

## Credit

Alejandro Radisic

<details>
<summary>Full credit and attribution basis</summary>

- **Alejandro Radisic** — derivation, formalization; credited by the source. finite-field count and S3 fixed-point interpretation

</details>

## Evidence

### Lean formalization

**Full proof offered.** The exact formalized counts imply the limit; the S3 fixed-point match is an arithmetic interpretation.

What this evidence does not settle:

- The limit agrees with an S3/Chebotarev heuristic, but the pinned repository explicitly does not formalize irreducibility or S3 monodromy.

## Review record

This guide has not yet recorded an independent expert or machine check covering the whole claim.

## Limitations

- The pinned repository does not formalize irreducibility or S3 monodromy.

## Sources

- [Counting.lean (Lean source)](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/Alpoge/Counting.lean)
- [Alejandro Radisic's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559) — primary

[Back to the claim inventory](../claims.md)
