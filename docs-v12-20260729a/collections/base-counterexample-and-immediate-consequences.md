---
title: "The Three-Dimensional Counterexample"
description: "The Jacobian conjecture is false in every dimension n at least 3."
---

# The Three-Dimensional Counterexample

<p class="dek">The Jacobian conjecture is false in every dimension n at least 3.</p>

<span class="status status-kind">Result</span> <span class="status status-draft">Public</span> <span class="status coverage-not_applicable">No program manuscript claimed</span>

## Precise statement

The Jacobian conjecture is false in every dimension n at least 3.

## Claims in this result package

### [JCG-561802FA · Constant Jacobian determinant of the Alpöge map](../claims/JCG-561802FA.md)

The displayed Alpöge polynomial map has Jacobian determinant equal to the constant -2.

*Defining · Proof Lemma · Proof offered — review pending*

### [JCG-E4FA4CBB · An explicit triple collision](../claims/JCG-E4FA4CBB.md)

The three distinct rational points (0,0,-1/4), (1,-3/2,13/2), and (-1,3/2,13/2) have the common image (-1/4,0,0) under the Alpöge map.

*Defining · Proof Lemma · Proof offered — review pending*

### [JCG-D82B1D43 · Failure of the Jacobian conjecture in dimensions at least three](../claims/JCG-D82B1D43.md)

The Jacobian conjecture is false in every dimension n at least 3.

*Defining · Primary Statement · Proof offered — review pending*

### [JCG-015F97FF · Technical claim](../claims/JCG-015F97FF.md)

The determinant \(-2\) has a conceptual rational-factorization explanation.

*Defining · Supporting Result · Recorded*

### [JCG-C4DFAF31 · Technical claim](../claims/JCG-C4DFAF31.md)

The real restriction is already a strong counterexample.

*Defining · Supporting Result · Recorded*

### [JCG-B7122324 · A determinant-one counterexample over every field](../claims/JCG-B7122324.md)

For every field k, the determinant-one rescaled construction formalized by Dean Cureton gives a polynomial map from k^3 to k^3 that is not injective.

*Shared · Strengthening · Proof offered — review pending*

### [JCG-610C33B2 · Technical claim](../claims/JCG-610C33B2.md)

The announced rational collision belongs to a one-parameter orbit of three-point fibers.

*Shared · Supporting Result · Recorded*

## Evidence and manuscript boundary

Public sources are linked below. No claim is made that one of the six working manuscripts is the source for this page.

Complete coverage requires an exact LaTeX location for every program-relevant defining claim. A locator records where the current statement and evidence boundary appear; it is not a proof-review status.

### Public sources

- [alpoge-lean v0.4.0 documentation — Alejandro Radisic](https://github.com/alerad/alpoge-lean/blob/95897469d48ba97f1a80a2db6553fd2f0f43834b/README.md)
- [alpoge-lean v0.4.0 — Alejandro Radisic](https://github.com/alerad/alpoge-lean/releases/tag/v0.4.0)
- [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf)
- [Hello there the Jacobian conjecture is false](https://x.com/__alpoge__/status/2079028340955197566)
- [jacobian — deancureton](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88)
- [https://github.com/alerad/alpoge-lean/tree/b39e3bf3493939db11b0f78c5b369dd028093f0f](https://github.com/alerad/alpoge-lean/tree/b39e3bf3493939db11b0f78c5b369dd028093f0f)
- [feat: add Jacobian disproof — Paul Lezeau](https://github.com/google-deepmind/formal-conjectures/pull/4474)
- [feat(JacobianConjecture): sorry-free refutation at n = 3 over Q — techno-optimist](https://github.com/google-deepmind/formal-conjectures/pull/4486)

### Independent review

- Machine Check: Formalization.
- Machine Check: The pinned README identifies the relevant Lean theorems and reports no `sorry` and no axioms beyond Mathlib. No fresh `lake build` was run for this guide.
- Machine Check: Lean formalization.
- Machine Check: Independent lean formalization.
- Machine Check: The source uses one collision when the characteristic is not two and a separate collision in characteristic two.

## Credit

- Akhil Mathew: problem suggestion; attributed by source — problem suggestion as reported by the source
- Alejandro Radisic: formalization; attributed by source — author and maintainer of the pinned Lean development
- Dean Cureton: formalization; documented authorship — Contribution recorded in Lean counterexamples to the Jacobian conjecture over all fields.
- Levent Alpöge: discovery, construction; attributed by source — formula announced by the named person
- Paul Lezeau: formalization; documented authorship — Contribution recorded in Formal Conjectures PR 4474 — Jacobian disproof.
- techno-optimist: formalization; documented authorship — Contribution recorded in Formal Conjectures PR 4486 — sorry-free refutation over Q.

## Connections

- [A Counterexample Over Every Field](../collections/all-fields-counterexample.md)
- [Base Map Fibers Image And Nonproperness](../collections/base-map-fibers-image-and-nonproperness.md)
- [Consequences for Neighboring Conjectures](../collections/consequences-for-neighboring-conjectures.md)

[Back to Results](../results/index.md)
