# The projective kernel carrier for five-dimensional collisions

Lane 7 · 2026-08-03

## Scope

Determine the geometry of the regular five-dimensional collision carrier from
its exact $10\times5$ projective-kernel presentation. The algebraic splitting
and chart generators are known; dimensions, purity, components, and the first
normal obstruction are not.

## Setup and definitions

Let $a=(a_0,\ldots,a_6)$, let $d(a)$ be the irreducible determinant defining
the regular open $D(d)$, and let

\[
M(a)\in\operatorname{Mat}_{10\times5}\mathbf Q[a]
\]

be the stored residual matrix. The projective kernel incidence is

\[
\mathcal I=\{(a,[u]) : M(a)u=0,\ d(a)\ne0\}.
\]

Its five standard affine charts $u_i=1$ have ten kernel equations plus the
localizer $zd-1$. The genuine two-marking locus also requires at least one
Plücker coordinate of the reconstructed pair to be nonzero.

## Results to use

- A polynomial left inverse splits the complete fifteen-equation marking
  incidence globally; on $D(d)$, it is scheme-theoretically equivalent to
  $M(a)u=0$, with exact reconstruction of the second marking.
- The stored matrices form an exact factorization with
  $\det S=-256d^2/243$ and $\det T=-243d^8/256$.
- The determinantal carrier is $V(I_5(M))\cap D(d)$. At one
  $\mathbf F_{11}$ point it is smooth of dimension one, which supplies a
  characteristic-zero component through the lifted germ.
- The five chart generators and Plücker transport checks are exact inputs.
  The five chart-dimension runs are still running, and no exact result
  artifacts are present in this worktree. Therefore no global dimension,
  grade, purity, corank, or component conclusion is available from them.

## Example: the smooth mod-11 germ

At $a=(8,7,1,7,2,9,0)$ modulo $11$, $d=1$,
$\operatorname{rank}M=4$, and the determinantal normal map has rank six. This
is an example proving one smooth curve germ, not purity of the entire carrier.

## Live problem

Prove the grade-six/purity statement on $D(d)$ while retaining the Plücker
open, and then determine whether the corank-two locus
$V(I_4(M))\cap D(d)$ is empty.

## Tasks

### L7-T1 — Prove grade six from the exact split architecture

Inputs: the [split-incidence theorem](lane-7-source-packet.md),
the [stored matrix](lane-7-source-packet.md),
and the exact factorization files in the same packet.

Deliverable: a characteristic-zero proof that $I_5(M)$ has grade six after
localizing at $d$, or an explicit lower-grade associated prime; include the
Eagon--Northcott consequence and the Plücker-open disposition component by
component.

Dependencies: only the pinned matrix identities and localization at $d$.

Limits: expected codimension and one smooth point do not prove purity.

### L7-T2 — Interpret preserved chart results when they arrive

Inputs: the [five-chart generators](lane-7-source-packet.md)
and future exact CAS logs preserving commands, versions, characteristics, and
outputs.

Deliverable: a characteristic-zero corank/purity theorem with modular lifting
justified, or a precisely located exceptional component.

Dependencies: preserved exact result artifacts; none are currently present.

Limits: generated ideals are inputs, not dimension results. A failed or
unpreserved workflow supplies no mathematical conclusion.

Alternative connections: a quartic determinantal comparison with Lane 4 is
welcome if the marked-chart opens and Plücker open remain visible.

## Limits

The exact theorem gives architecture and one smooth component germ. It does
not prove $I_4(M):d^\infty=(1)$, global grade six, absolute component
decomposition, or nowhere-solvability of the first-normal equation.

## Direct sources

- [Exact theorem checker](lane-7-source-packet.md)
- [Projective chart generator](lane-7-source-packet.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-7-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
