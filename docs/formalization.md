---
title: Formal verification
description: What has been checked in Lean and where substantial formal developments should live.
---

# Formal verification

The decisive counterexample is unusually friendly to formal verification. It
requires a polynomial determinant identity and an explicit collision, rather
than a long chain of analytic estimates or abstract existence theorems.

## Current artifacts

| Project | What it contributes | Role |
| --- | --- | --- |
| [Formal Conjectures PR #4474](https://github.com/google-deepmind/formal-conjectures/pull/4474) | Updates the canonical Lean statement and records the disproof. | Shared statement/review layer; open at the status date. |
| [deancureton/jacobian](https://github.com/deancureton/jacobian) | A compact Lean 4 proof over fields, including determinant and noninjectivity. | Standalone complete certificate. |
| [alerad/alpoge-lean](https://github.com/alerad/alpoge-lean) | An independent Lean development with a broader fiber description. | Standalone formal development. |
| [jacobian-anatomy](https://github.com/DrAlexHarrison/jacobian-anatomy) | An independent Lean certificate alongside exact computational geometry and audits. | Cross-check and anatomy. |

## What Lean certifies

Once the relevant statement has been expressed correctly, the Lean kernel
checks that the proof term has that type. For the core counterexample, this can
certify:

1. the displayed coordinate functions are polynomials;
2. their Jacobian determinant is the required constant;
3. the witness points are distinct;
4. their images agree;
5. the formal conjecture therefore fails in dimension three.

It does not automatically certify historical attribution, literature priority,
or that an informal explanation faithfully matches the chosen formal statement.

## Where formal pull requests belong

[Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) is
the natural place for canonical **statements**, corrections, metadata, and short
proofs. Its contribution policy asks longer proofs—roughly more than 25–50
lines—to live in their own repository and be linked with a `formal_proof`
attribute.

This guide fills a different role: English exposition, an evidence ledger,
source comparison, open questions, and links to exact or formal artifacts.
Substantial Lean work should remain in a dedicated Lean repository and be
linked from both places.

## A useful next formalization

The highest explanatory value would come from formalizing the binary-cubic
incidence description on the [geometry page](geometry.md). It would connect the
short refutation to the reason the example works, while building reusable
infrastructure for finite covers, projective roots, discriminants, and fiber
strata.

