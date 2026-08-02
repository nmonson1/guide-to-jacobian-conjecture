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

<!-- retained-math-v2-selection:ARG-RMU5D8E0003-FINITE-PLANE -->

The automorphism and obstruction formulas are in the Program 5 proof sources.
The public record does not isolate all fourteen finite automorphisms in one
input table. Thus the selected-plane calculation is ready to be reformulated
intrinsically, while full finite transport is blocked.

## Exact live problem

For the **selected finite two-plane** in the compiler-owned result above, let
`A=C[r]`, let `E:U tensor A -> W tensor A` be the supplied cubic
tangent-effect matrix, let `b in W tensor A` be the supplied residual, and
let `beta=[b] in C=coker(E)`. The cubic obstruction vanishes at a slope
exactly when the fibre of `beta` vanishes. This is not the support of `C`,
which can have positive generic rank.

Determine the generic rank `s` of `E`. On the constant-rank open set,
identify the zero scheme of `beta` with the rank-equality locus

```text
rank [E | b] = rank E = s,
```

cut out by the `(s+1)`-minors of the augmented matrix. Treat rank-jump slopes
separately, specifying any saturation needed. Prove that the left-kernel
pairing gives `(r-4)(r^2-8r+64)` as a coordinate of this obstruction section,
not as the Fitting support of `coker(E)`. Then formulate the quartic
coefficient-span separator as a section of the residual obstruction quotient
at the two conjugate roots and recover the value `-1152`.

## Tasks and deliverables

### P5-L6A0 — Selected-plane obstruction-section package

Status: ready.

Inputs: the compiler-owned finite-plane statement, argument, and its three
exact source links above. They supply the cubic effect matrices, residuals,
exceptional slopes, and quartic coefficient-span certificate.

Deliverable: the coherent cokernel and its distinguished section, the
augmented determinantal ideal on the constant-rank locus, a separate analysis
of every rank-jump slope, and the intrinsic quartic residual section whose
recorded evaluation is `-1152`. Explain which construction descends under
basis change and can extend from a line to the full finite row-base fibre.

### P5-L6A — Full operation-invariant obstruction

Status: blocked until the full operation matrices and finite-action table are
publicly isolated.

Inputs: the future public matrices for row-killing, source, target, and
stable-coordinate operations, plus the fourteen finite automorphisms.

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
