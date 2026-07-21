---
title: Claims
description: The normalized baseline claim inventory as of 21 July 2026.
---

# Baseline claim inventory

This inventory contains the conjecture, the mathematical claims from the first
public core ledger, and the properness theorem already used by that version of
the site. It freezes the baseline before any explanatory article is added.

`Evidence present` reports linked material. `Assessment` reports what this
project has itself checked. At this stage, every assessment field is empty.

| ID | Normalized statement | Posture | Evidence present | Guide relation |
| --- | --- | --- | --- | --- |
| `JCG-CLAIM-0001` | Every polynomial Keller map over \(\mathbb C\) is a polynomial automorphism. | Conjecture; refuted for \(n\ge3\), open for \(n=2\) | Classical source | Indexed only |
| `JCG-CLAIM-0002` | The displayed three-variable map has Jacobian determinant \(-2\). | Unconditional theorem claim | Proof, exact certificate, formalizations | Indexed only |
| `JCG-CLAIM-0003` | Three displayed rational source points have the same image. | Unconditional theorem claim | Exact certificate, formalizations | Indexed only |
| `JCG-CLAIM-0004` | The Jacobian conjecture is false in every dimension \(n\ge3\). | Refutation | Proof by dimension-three example and stabilization | Indexed only |
| `JCG-CLAIM-0005` | The plane Jacobian conjecture remains open. | Open question | Public-source status | Indexed only |
| `JCG-CLAIM-0006` | The displayed map has generic degree three and fibers of cardinality 3, 1, or 0 as specified by its cubic discriminant. | Unconditional theorem claim | Proof and exact formulas | Indexed only |
| `JCG-CLAIM-0007` | Its image is \(\mathbb C^3\setminus\Gamma\), while its nonproperness set is \(V(\Delta)\). | Unconditional theorem claim | Proof and exact formulas | Indexed only |
| `JCG-CLAIM-0008` | There are three-dimensional nonproper Keller maps of every generic degree at least three. | Unconditional theorem claim | Public construction | Indexed only |
| `JCG-CLAIM-0009` | For a Keller map over \(\mathbb C\), polynomial invertibility, properness, emptiness of the nonproperness set, and codimension at least two of that set are equivalent. | Unconditional theorem claim | Public proof and classical dependency | Indexed only |

The complete structured records include dependencies, boundaries, exact source
versions, and the empty assessment fields:
[browse `claims/`](https://github.com/nmonson1/guide-to-jacobian-conjecture/tree/main/claims).

## Deliberately excluded from the baseline

Repository workflow statements—such as whether a particular pull request is
open—are dated source observations rather than mathematical claims. They will
be recorded as contribution or assessment events, not inserted into the
mathematical claim inventory.
