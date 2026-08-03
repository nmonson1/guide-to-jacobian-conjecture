# Lane 6: Homogeneous realization and compression

## Problem and scope

Let `F_0` be the fixed **eleven-variable** degree-at-most-three Keller
counterexample used in
[`manuscripts/05-homogeneous-descendants/main.tex`](../proof-sources/05-homogeneous-descendants/main.md). Its rank-sensitive
suspension gives a 19-variable cubic-homogeneous map with the same
three-sheeted cover. Lane 6 asks whether that cover has an 18-variable
cubic-homogeneous realization.

Here *Keller* means constant nonzero Jacobian determinant, and
*counterexample* means noninvertible. The linked source states the fixed
eleven-variable map and the rank-sensitive suspension theorem.

The problem permits source, target, and stable-coordinate operations. An
obstruction on one suspension, tensor presentation, or transverse slice is
not automatically an invariant of the cover.

## Setup and notation

Write a candidate cubic-homogeneous map as `X-H(X)`, with `H` cubic and
nilpotent Jacobian. `P_*` is the rank-six point fixed in the Program 5
deformation coordinates. `P_3` denotes its cubic term, `Q` an infinitesimal
operation, and `O_4(P)` the quartic lifting obstruction. The scalar functional

```text
Gamma_4(E)=[h^4](E_z)
```

annihilates commutator corrections `[Q,P_3]` in the displayed slice.

The *row-killing directions* are infinitesimal changes annihilating the
chosen redundant row. Fourteen relevant weight-zero directions are known
polynomial automorphisms: thirteen triangular directions and `b^2 e_h`.
After quotienting them and imposing the Casimir relation, the remaining core
has coordinates `(A,B,C,D,E)`.

## Reusable mathematics

The fixed map has a 19-variable cubic-homogeneous suspension, a 38-variable
symmetric double, and a square-zero pairing of length 110.

At `P_*`, the complete six-dimensional transverse rank-six cone is

```text
V(u_0*u_5,u_2*u_3,u_3*u_5)
 = V(u_3,u_5) union V(u_0,u_3) union V(u_2,u_5).
```

Every point integrates to an exact cubic jet, but `Gamma_4=-1` on the family,
so none lifts through quartic order. Unit: [`RMU-25A1F543`](../working-mathematics/units/RMU-25A1F543.md).

The five-dimensional core contains the only loci not excluded by eleven
degree-one dual sections:

```text
Z0: A=B=D=0;
Z1: D=0, A=-3B, C^2+36C+50B-104BC=0;
Z2: A=3D, B=-D, C^2+36C+104CD-50D-84D^2=0,
```

with `E` free. These evaluations do not prove that the obstruction vanishes
on the surfaces. Units: [`RMU-5D8E0001`](../working-mathematics/units/RMU-5D8E0001.md), [`RMU-5D8E0002`](../working-mathematics/units/RMU-5D8E0002.md).

The fixed-model calculation has now been enlarged. The exact transverse
equations are classified by middle and deepest strata and include an explicit
residual rational curve. The compression functional is constant and nonzero
on that curve. After adjoining all 60 encoded tame source directions,
transporting divergence, and evaluating the full weight spaces and
polarizations, the pinned quartic obstruction is still the nonzero scalar
`1728`. Unit: [`RMU-5C6E0010`](../working-mathematics/units/RMU-5C6E0010.md); theorem notes, certificates and fresh exact
replays: [`research-notes/lane6-transverse-source-obstruction-20260802-v1/`](lane-6-source-packet.md).

<!-- retained-math-v2-selection:ARG-RMU5D8E0003-FINITE-PLANE -->

This strengthens the selected-plane result, but it retains a fixed
lower-target normalization and an encoded tame source space. It is not an
invariant of every source, target and stable presentation of the cover.

## Exact live problem

Starting from the exact 60-direction source-coupled complex in
[`RMU-5C6E0010`](../working-mathematics/units/RMU-5C6E0010.md), enlarge the moving effect map to include the missing lower-
target, finite target and stable-presentation directions. Determine whether
the quartic functional descends to the resulting cokernel. A successful
obstruction must be unchanged under presentation moves; a failure is also
useful if it gives an explicit new direction that cancels the value `1728`.

## Tasks and deliverables

### P5-L6A0 — Upgrade the 60-direction obstruction

Status: ready.

Inputs: [`RMU-5C6E0010`](../working-mathematics/units/RMU-5C6E0010.md), both theorem notes and all matrices and certificates
in [`research-notes/lane6-transverse-source-obstruction-20260802-v1/`](lane-6-source-packet.md). These
give the complete encoded transverse strata, residual curve, 60 source
directions, divergence transport and obstruction polarizations.

Deliverable: the coherent cokernel over the full encoded transverse carrier,
its distinguished quartic section, and the additional target/stabilization
blocks required for presentation invariance. Either prove the section
survives those blocks or supply an exact cancelling direction and the next
corrected quotient problem.

### P5-L6A — Full operation-invariant obstruction

Status: blocked only on the operation blocks not present in the new packet.

Inputs: P5-L6A0 plus future matrices for the missing target and stable-
coordinate operations and any finite actions not generated by the encoded
tame source directions.

Deliverable after recovery: define the moving cokernel over the full
operation quotient and produce an invariant section or Fitting ideal that
restricts to every slice witness.

### P5-L6B — Finite triangular transport

Status: blocked until the fourteen finite automorphisms are exposed as one
public input table.

Inputs: that table and P5-L6A.

Deliverable: transport all higher normal terms to the five-dimensional core
without replacing a finite action by its tangent space.

### P5-L6C — Residual surfaces

Status: blocked on P5-L6A and P5-L6B.

Inputs: the invariant obstruction and finite transport produced by those tasks.

Deliverable: evaluate the invariant obstruction on `Z0,Z1,Z2`, or construct
an explicit persistent family on one surface.

## Scope cautions

- Tangent direct sums do not imply finite gauge equivalence.
- Eleven vanishing evaluations do not make the whole obstruction vanish.
- Selected planes do not classify the global compression locus.
- The eleven-variable `F_0` here is not Lane 3's three-variable `F_0`.
