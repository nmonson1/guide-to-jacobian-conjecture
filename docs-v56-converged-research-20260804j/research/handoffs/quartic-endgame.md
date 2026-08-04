---
title: "Model research brief — A startable edge of the quartic case tree"
description: "A self-contained mathematical handoff for a research model."
---

# A startable edge of the quartic case tree

<p class="claim-tag">Lane 4 · Updated 4 August 2026</p>

## Scope

The global degree-four reduction is not yet a closed proof. This page isolates
one concrete parent-to-child edge that can be settled from the supplied
mathematics: the branch on which the cubic normal layer vanishes. A separate
historical coefficient reconstruction is recorded later as non-ready
work so that it does not obscure the startable theorem.

## Setup and definitions

Let $k$ be an algebraically closed field of characteristic zero and let

\[
F=LX+H_2+H_3+H_4:\mathbb A_k^3\longrightarrow\mathbb A_k^3
\]

be a polynomial map of degree at most four, where $L$ is linear, $H_i$ is
homogeneous of degree $i$, and $\det JF\in k^*$. The
**leading-target-span-two branch** is the case in which the three coordinate
polynomials of $H_4$ span a two-dimensional $k$-space. A target-linear change
then puts

\[
H_4=(P,Q,0),\qquad R=(H_3)_3.
\]

The **zero cubic normal edge** is the locus $R=0$; the supplied case tree
labels this edge `B0`.

## Results to use

### Quadratic coordinate

If a polynomial in three variables has degree at most two and no critical
point, the quadratic-coordinate lemma makes it a polynomial coordinate.

### Plane Keller input

After straightening such a coordinate to a parameter $t$, the other two
coordinates form a plane Keller pair over $\overline{k(t)}$. The
Appelgate--Onishi theorem in
[Nagata, Theorem 7.3](https://repository.kulib.kyoto-u.ac.jp/server/api/core/bitstreams/9ef8e868-5526-4830-b19f-543c0af09e7c/content)
says, in the per-coordinate form used here, that a characteristic-zero plane
Keller pair is invertible when the degree of one coordinate is a product of
at most two primes. Every positive degree at most seven has that form.

### Descent and the last implication

Uniqueness of the inverse descends it from $\overline{k(t)}$ to $k(t)$.
The final step uses the standard fact that a birational Keller self-map of
affine space is a polynomial automorphism.

## Live problem

Prove or disprove the following exact edge theorem.

> Let $F=LX+H_2+H_3+H_4$ be Keller of degree at most four. If a target-linear
> change gives $H_4=(P,Q,0)$ and $(H_3)_3=0$, then $F$ is a polynomial
> automorphism.

The supplied proof strategy straightens $F_3$, chooses a nonzero combination
of $F_1,F_2$ whose $z^4$ coefficient vanishes, obtains plane degree at most
seven after substitution, and invokes the per-coordinate plane theorem.

## Separate non-ready historical reconstruction

The regular marked $(3,4)$ Hilbert--Burch chart in the primitive binary
triple-ramification branch has a weighted-inflection subchart called $F_4$.
Its exact local highest-$z$ obstruction is useful, but the historical
$Q_4$--$F_4$ packet is a different coefficient presentation and no
equivalence between them is assumed.

The [fail-closed contract](lane-4-source-packet.md#source-b20b8a2a6775ef79)
and [recovered partial chart](lane-4-source-packet.md#source-65df544f4fa7c99b)
preserve one exact local calculation. Full \(Q_4\)--\(F_4\) recovery is
blocked on the historical gauge table, unrestricted lower forms and
cancellation variables, complete open factor, and complement routes. The
partial instance deliberately fails the complete contract and must not be
completed by guessing those data.

## Current tasks

<!-- RETAINED_TASKS_START -->
### Recover the complete Q4-F4 terminal system — Blocked

`TSK-L4-Q4-F4-RECOVERY` · computation, proof · sustained

**Goal.** Complete the fail-closed Q4-F4 instance and run an exact characteristic-zero terminal saturation.

**Why it matters.** This would turn the surviving local calculation into a complete historical terminal certificate.

**Public inputs.**

- [Recovered partial Q4-F4 local-chart certificate](../working-mathematics/units/RMU-2D4E0015.md) (retained unit `RMU-2D4E0015`).
- [Fail-closed completeness contract and missing-field inventory.](lane-4-source-packet.md#source-b20b8a2a6775ef79).

**Blocked on.**

- The historical gauge table is absent.
- Unrestricted lower forms and cancellation variables are absent.
- The complete open factor and complement routes are absent.

**Complete when.**

- The complete contract validates and a replayable characteristic-zero saturation covers every declared open and complement.

**Possible starts.**

- Recover the named historical sources before extending the local algebra.

**Freedom.**

- An equivalent coordinate presentation is allowed only with forward and inverse chart maps.

**Mathematical limits.**

- Do not guess missing formulas from the partial resultants.
- Do not call the partial local chart exhaustive.

### Settle the zero cubic normal quartic edge — Ready now

`TSK-L4-ZERO-NORMAL-EDGE-V2` · proof · bounded

**Goal.** Prove or refute the exact B0 theorem for degree-at-most-four Keller maps with leading target span two and zero cubic normal component.

**Why it matters.** This closes one load-bearing edge of the quartic case tree without claiming global exhaustiveness.

**Public inputs.**

- [Exact candidate theorem statement and proposed proof.](lane-4-source-packet.md#source-4da06de9a68fd581).

**Complete when.**

- Every stated step is proved under the exact hypotheses or an explicit counterexample identifies the failed step.

**Possible starts.**

- Check the coordinate straightening, z^4 cancellation, degree-seven plane bound, descent, and birational-Keller implication in sequence.

**Freedom.**

- A shorter replacement proof is welcome.

**Mathematical limits.**

- This task closes only B0 and does not prove the quartic case tree exhaustive.
<!-- RETAINED_TASKS_END -->

## Limits

The zero cubic normal theorem is a determinate proof problem with all stated
inputs available. The full $Q_4$–$F_4$ reconstruction and the global quartic
case-tree closure are not presently executable from the repository.

## Direct sources

- [Quartic case tree](lane-4-source-packet.md#source-c42d7cab59ee8cfa)
- [Structural repair containing the zero-normal proposition](lane-4-source-packet.md#source-4da06de9a68fd581)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Optional runnable source ZIP](../inputs/lane-4-source-files.zip) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
