# A startable edge of the quartic case tree

Lane 4 · 2026-08-03

## Scope

The global degree-four reduction is not yet a closed proof. This page isolates
one concrete parent-to-child edge that can be settled from the supplied
mathematics: the branch on which the cubic normal layer vanishes. A separate
historical coefficient reconstruction is recorded at the end as non-ready
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

## Tasks

### L4-T1 — Settle the zero cubic normal edge — ready

Inputs: the exact statement and proposed proof in
[§3 of the structural-repair packet](lane-4-source-packet.md#source-4da06de9a68fd581),
the [quadratic-coordinate lemma and easy-branch argument](../proof-sources/02-low-degree/main.md),
the [proof-to-code crosswalk](lane-4-source-packet.md#source-d366da3c3ac74538),
and the [case-tree entry](lane-4-source-packet.md#source-c42d7cab59ee8cfa).

Deliverable: a self-contained proof of the displayed theorem, or an explicit
counterexample to one of its steps. In particular, justify the coordinate
change $t=F_3$, the choice killing the $z^4$ term, the bound
$\deg_{x,y}G\le7$, applicability of the per-coordinate plane theorem over
$\overline{k(t)}$, descent of the inverse, and the final birational-Keller
implication.

Dependencies: the quadratic-coordinate lemma and the cited plane theorem in
its per-coordinate form.

Limits: this closes only the `B0` edge. It does not establish that the whole
quartic case tree is exhaustive or settle another terminal branch.

## Separate non-ready historical reconstruction

The regular marked $(3,4)$ Hilbert--Burch chart in the primitive binary
triple-ramification branch has a weighted-inflection subchart called $F_4$.
Its exact local highest-$z$ obstruction is useful, but the historical
$Q_4$--$F_4$ packet is a different coefficient presentation and no
equivalence between them is assumed.

### L4-T2 — Reconstruct the full $Q_4$–$F_4$ system — not ready

Inputs: the [fail-closed contract](lane-4-source-packet.md#source-b20b8a2a6775ef79),
the [recovered partial chart](lane-4-source-packet.md#source-65df544f4fa7c99b),
its [machine-readable instance](lane-4-source-packet.md#source-5c0a6360445bfa69),
and the [marked-chart theorem](lane-4-source-packet.md#source-a97c6985d00b30b6).

Deliverable: once the missing data exist, a complete instance with forward
and inverse chart maps, unrestricted lower forms and cancellation variables,
the total open factor, a route for every complement, both $104/3$ anchors,
and an exact characteristic-zero saturation certificate.

Dependencies: the currently unavailable historical gauge table, unrestricted
$H_3,H_2,L$ formulas, complete open product, and complement routes.

Limits: the partial JSON instance deliberately fails the complete contract;
it cannot be filled by guessing omitted formulas from its four resultants.

Alternative connections: a determinantal-carrier comparison with Lane 7 is
welcome if it retains the exact chart opens and does not assume global
case-tree coverage.

## Limits

The zero cubic normal theorem is a determinate proof problem with all stated
inputs available. The full $Q_4$–$F_4$ reconstruction and the global quartic
case-tree closure are not presently executable from the repository.

## Direct sources

- [Quartic case tree](lane-4-source-packet.md#source-c42d7cab59ee8cfa)
- [Structural repair containing the zero-normal proposition](lane-4-source-packet.md#source-4da06de9a68fd581)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-4-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
