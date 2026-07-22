---
title: Claims
description: The normalized claim inventory as of 22 July 2026.
---

# Claim inventory

These are normalized statements, not a narrative guide. `Evidence present`
means the linked artifact contains a proof, calculation, formalization, or
argument. It does not mean this project has independently assessed it. Every
project assessment field remains empty.

## Foundation and historical attribution

| ID | Normalized statement | Posture | Evidence state |
| --- | --- | --- | --- |
| `JCG-CLAIM-0001` | Every polynomial Keller map over (mathbb C) is a polynomial automorphism. | Conjecture; refuted for (nge3), open for (n=2) | Classical source |
| `JCG-CLAIM-0010` | Kraus's 1884 paper states the modern plane conjecture as its main result. | Historical-attribution claim | Refereed historical study |
| `JCG-CLAIM-0011` | Kraus's final step fails at infinity and does not prove the plane case. | Historical proof-audit claim | Refereed line-by-line analysis |

## Core counterexample and its geometry

| ID | Normalized statement | Posture | Evidence state |
| --- | --- | --- | --- |
| `JCG-CLAIM-0002` | The displayed three-variable map has Jacobian determinant (-2). | Unconditional theorem claim | Proof and formalizations |
| `JCG-CLAIM-0003` | Three displayed rational source points have one common image. | Unconditional theorem claim | Exact certificate and formalizations |
| `JCG-CLAIM-0004` | The Jacobian conjecture is false in every dimension (nge3). | Refutation | Dimension-three example and stabilization |
| `JCG-CLAIM-0005` | The plane Jacobian conjecture remains open. | Open question | Public-source status |
| `JCG-CLAIM-0006` | The displayed map has generic degree three and corrected fiber cardinalities 3, 1, or 0. | Unconditional theorem claim | Proof and exact formulas |
| `JCG-CLAIM-0007` | Its image is (mathbb C^3\setminusGamma), while its nonproperness set is (V(\Delta)). | Unconditional theorem claim | Proof and exact formulas |
| `JCG-CLAIM-0008` | Nonproper Keller maps in dimension three exist for every generic degree at least three. | Unconditional theorem claim | Two public constructions and exact atlas |
| `JCG-CLAIM-0009` | For complex Keller maps, invertibility, properness, empty nonproperness set, and codimension at least two are equivalent. | Unconditional theorem claim | Public proof and classical dependency |

## Formal and structural extensions

| ID | Normalized statement | Posture | Evidence state |
| --- | --- | --- | --- |
| `JCG-CLAIM-0012` | A related determinant-one map is formally noninjective over every field. | Unconditional theorem claim | Pinned Lean development |
| `JCG-CLAIM-0013` | The induced degree-three function-field extension has (S_3) Galois closure. | Working analysis | Closed, unanswered MathOverflow post |
| `JCG-CLAIM-0014` | The displayed map has trivial rational deck group over its target. | Working analysis | Closed, unanswered MathOverflow post |
| `JCG-CLAIM-0015` | An explicit 11-variable map has total degree three, 52 terms, determinant (-2), and a rational three-point collision. | Unconditional theorem claim | Exact executable certificate |
| `JCG-CLAIM-0021` | An explicit (U+H) map over (mathbb Q^{24}) is cubic homogeneous, has determinant 1, 54 cubic monomials, and a rational collision. | Unconditional theorem claim | Derivation and two verifier implementations |

## Downstream consequences

| ID | Normalized statement | Posture | Evidence state |
| --- | --- | --- | --- |
| `JCG-CLAIM-0016` | The Mathieu conjecture for (SU(3)) is false. | Claimed consequence | Public note; primary implication not project-audited |
| `JCG-CLAIM-0017` | Zhao's Vanishing Conjecture is false in some finite dimension. | Claimed consequence | Public note; primary equivalence not project-audited |
| `JCG-CLAIM-0018` | The Image Conjecture is false in some finite dimension. | Claimed consequence | Public note; primary implication not project-audited |
| `JCG-CLAIM-0019` | The Dixmier conjecture fails for (A_n(mathbb C)) for every (nge3). | Unconditional theorem claim | Public proof and exact audit package |
| `JCG-CLAIM-0020` | The Gaussian Moments Conjecture is false for every (nge3), with explicit small witnesses. | Unconditional theorem claim | arXiv proof with explicit formulas |

The structured files state dependencies, boundaries, exact source versions,
AI disclosures where available, and the empty assessment fields:
[browse `claims/`](https://github.com/nmonson1/guide-to-jacobian-conjecture/tree/main/claims).
