# Lane 6: Homogeneous realization and compression

## Research objective

Determine whether the fixed three-sheeted cover has an 18-variable
cubic-homogeneous realization, and separate cover invariants from
obstructions attached to one suspension, tensor, or operation slice.

## Reusable mathematics

The rank-sensitive suspension of the fixed degree-at-most-three map gives a
19-variable cubic-homogeneous Keller counterexample.  Its symmetric double
has 38 variables.  The fixed cubic tensor has a square-zero pairing of length
110 and a proven vector-Waring lower bound 52.  Thus

```text
52 <= N_pair <= 110
```

for this tensor.  These are model-relative realization bounds.

### Complete six-dimensional transverse cone

At the displayed rank-six point `P_*`, the determinantal tangent space has
dimension 115 and the row-killing space dimension 109.  In transverse
coordinates `u_0,...,u_5`, the complete second-order rank-six cone is

```text
V(u_0*u_5,u_2*u_3,u_3*u_5)
 = V(u_3,u_5) union V(u_0,u_3) union V(u_2,u_5).
```

An explicit polynomial family integrates every point to an exact cubic jet of
coordinate-span rank six and has no other rank-six points.  Nevertheless

```text
Gamma_4(E)=[h^4](E_z),
Gamma_4([Q,P_3])=0,
Gamma_4(O_4(P(u)))=-1.
```

No member lifts through quartic order.  Retained unit: [`RMU-25A1F543`](../working-mathematics/units/RMU-25A1F543.md).

### Weight-zero quotient core

The relevant equivariant row-killing fibre is 20-dimensional.  Thirteen
triangular directions and the elementary shear `b^2 e_h` are actual
polynomial automorphisms.  After quotienting them and imposing the normal
Casimir relation, the unresolved core has coordinates

```text
A=k_14, B=k_19, C=k_23, D=k_67, E=k_85.
```

Retained unit: [`RMU-5D8E0001`](../working-mathematics/units/RMU-5D8E0001.md).

Eleven exact degree-one dual sections exclude every core point except

```text
Z0: A=B=D=0;
Z1: D=0, A=-3B, C^2+36C+50B-104BC=0;
Z2: A=3D, B=-D, C^2+36C+104CD-50D-84D^2=0,
```

with `E` free.  They do not prove that the obstruction vanishes on these
surfaces.  Retained unit: [`RMU-5D8E0002`](../working-mathematics/units/RMU-5D8E0002.md).

### Selected-plane classification

For one selected two-plane, all 66 quadratic tangent-kernel freedoms fail the
cubic compatibility test with ranks `15/16` and witness `-256/3`
([`RMU-5A110523`](../working-mathematics/units/RMU-5A110523.md)).

<!-- retained-math-v2-selection:ARG-RMU5D8E0003-FINITE-PLANE -->

## What is not known

None of these slices proves a global 19-to-18 impossibility.  Missing pieces
include:

- finite nonlinear transport from the whole weight-zero fibre to the
  five-dimensional core;
- the obstruction on `Z0,Z1,Z2`;
- nonlinear coupling to all 109 row-killing directions;
- the complete finite row-base and infinity fibres; and
- independent moving target and stable-coordinate changes.

A fixed scalar quartic witness can move under target gauge; the global object
must be the moving cokernel section or its order/Fitting ideal.

## Exact live problem

Prove finite triangular-gauge compatibility for the five-dimensional core.
Then construct degree-two dual sections separately on `Z0`, `Z1`, and `Z2`
and decide whether their evaluation ideals are units.


## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks

### P5-L6A — Finite gauge theorem

Actor: `online_model`. Status: ready.

Transport every higher normal term and moving cokernel section under the 14
actual polynomial automorphism directions.

### P5-L6B — Residual-surface obstruction

Actor: `online_model`. Status: blocked on P5-L6A.

Construct degree-two dual sections or explicit persistent families on each
surface.

### P5-L6C — Full operation quotient

Actor: `online_model`. Status: ready.

Add the remaining row-killing, target, and stable directions and determine
whether any nonlinear coupling reaches the constant `Gamma_4` class.

## Do not do

- Do not infer finite gauge equivalence from a tangent direct sum.
- Do not interpret vanishing of the eleven evaluations as vanishing of the
  obstruction section.
- Do not promote selected-plane or selected-transversal results to the full
  compression locus.
- Do not call `52` a universal dimension lower bound.

The retained-unit and proof-source pages linked above are the public mathematical record for this lane.
