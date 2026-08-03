# Compression limits for homogeneous realizations

Lane 6 · 2026-08-03

## Scope

Determine whether the nineteen-variable homogeneous suspension can be
compressed to eighteen variables, or prove a presentation-stable obstruction.
The known selected-plane and fixed-target calculations are exact benchmarks,
not a global noncompression theorem.

## Setup and definitions

Program 5 starts from an eleven-variable Keller object and constructs a
nineteen-variable homogeneous realization. A **compression** is an allowed
change of homogeneous presentation followed by realization in fewer ambient
variables. At a fixed realization, the filtered operation complex maps source
presentation directions to target-equation variations; its cokernel records
transverse first-order failures for that fixed target.

For the abstract problem, fix finite complexes $C_{\rm src}$,
$C_{\rm tgt}$, and $C_{\rm pres}$ of source, target, and presentation
directions, with a linearized equation map

\[
d:C_{\rm src}\oplus C_{\rm tgt}\oplus C_{\rm pres}\longrightarrow C_{\rm eq}.
\]

Its mapping cone records deformations and obstructions simultaneously. A
**presentation-stable obstruction** means a cohomology class transported by
the quasi-isomorphisms induced by changes of presentation and stabilization;
it is stronger than a nonzero cokernel functional for one fixed $d$.

## Results to use

- On one selected projective rank-six plane, the cubic--quartic Schur-chart
  calculation is exact: every projective direction in that plane reaches the
  constant contradiction $-1/2=0$. The associated 38-direction calculation
  is a finite benchmark, not a classification of all row bases.
- The fixed-lower-target source theorem computes the complete 60-dimensional
  special invisible tame-source space and obstruction functionals with
  constant value $1728$.
- In the exact ten-dimensional low-output moving-target pilot, the ten
  quadratic target corrections have independent quartic images;
  $D_{4,z}$ and $D_{4,c}$ remain outside their span, while the unique
  $-Y_d^2$ correction cancels $D_{4,a}$ and restores cubic span seven. This
  is not the full moving-target or stable quotient.
- The suspension and filtered-operation tools also expose 15- and
  18-dimensional fibres and third-order compatibility data.
- None of these results handles all presentation operations, a moving target,
  stabilization, or every candidate 18-variable realization.
- The repository does not yet contain a complete list of allowed
  presentation operations and their linearized columns. Consequently the
  abstract invariance theorem below is ready, while its concrete Program 5
  instantiation and finite transport are blocked on that input.

## Example: the selected rank-six plane

The contradiction on the selected plane is an example of a complete local
Schur-chart exclusion. It does not show that every projective rank-six plane,
row-base choice, or stabilized presentation has the same obstruction.

## Live problem

First prove a reusable mapping-cone criterion that turns an obstruction class
into a presentation-stable class under explicit equivariant chain maps. Then,
once the missing operation list is supplied, instantiate the criterion for the
nineteen-variable realization or find an eighteen-variable presentation that
escapes it.

## Tasks

### L6-T1 — Prove the abstract presentation-stability criterion

Inputs: [Program 5 tangent bridge](lane-6-source-packet.md),
the [source-obstruction packet](lane-6-source-packet.md),
the [moving-target pilot receipt](lane-6-source-packet.md),
and [homogeneous-descendants TeX](../proof-sources/05-homogeneous-descendants/main.md).

Deliverable: a theorem giving sufficient and necessary chain-level conditions
under which a class in $H^1(\operatorname{Cone}(d))$ is transported unchanged
by presentation moves and stabilization, including inverse and composition
laws. Explain exactly what additional columns and chain homotopies are needed
to apply it to the known 60-dimensional space and $1728$ functional.

Dependencies: the finite complexes and equivariant chain maps defined above;
the concrete Program 5 operation list is not needed for the abstract theorem.

Limits: an abstract criterion does not prove that Program 5 satisfies its
hypotheses, and the fixed-lower-target cokernel is not stable under adding
target or presentation columns until the concrete comparison maps are given.

### L6-T2 — Instantiate the criterion and decide compression — blocked input

Inputs: L6-T1, the nineteen-variable suspension, and the exact selected-plane
benchmark.

Deliverable: either an explicit eighteen-variable homogeneous realization with
Jacobian verification, or a nonzero invariant obstruction applying to every
eighteen-variable presentation.

Dependencies: L6-T1 and a public, exhaustive list of the allowed presentation
operations, stabilization maps, and their linearized action. That list is not
currently available, so this task cannot yet be executed as a finite Program 5
calculation.

Limits: failure on one plane or one row base does not establish global
noncompression.

Alternative connections: an escaping-complexity invariant from Lane 3 is
welcome if it is proved compatible with homogeneous stabilization.

## Limits

Current exact results concern a selected plane and a fixed lower target. They
do not classify the whole fibre or establish a presentation-invariant lower
bound of nineteen variables.

## Direct sources

- [Retained selected-plane theorem RMU-5D8E0004](../working-mathematics/units/RMU-5D8E0004.md)
- [Filtered operation tools](lane-6-source-packet.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-6-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
