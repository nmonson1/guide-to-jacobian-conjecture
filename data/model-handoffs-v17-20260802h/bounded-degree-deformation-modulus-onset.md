# Lane 3: Bounded-degree deformation and modulus onset

## Problem and scope

Let `F_0` be the explicit three-dimensional degree-seven Alpöge--Fable
Keller counterexample in the normalization used in
[`manuscripts/03-local-rigidity/main.tex`](../proof-sources/03-local-rigidity/main.md). This lane compares its local
deformation scheme inside maps of degree at most seven with operation
components that appear when degree eight is allowed.

Here *Keller* means `det DF_0=1`, and *counterexample* means that `F_0` is
not a polynomial automorphism. The linked source displays the map and the
proof/citation boundary for that fact.

The degree-seven statement is rigidity after quotienting the normalized
affine source orbit. It is not unrestricted formal rigidity and does not
exclude degree-increasing source or target shears.

## Setup and notation

The *degree-at-most-seven transverse slice* is the 337-dimensional affine
coefficient slice through `F_0` obtained by setting eleven displayed
component--monomial coefficients to zero. The determinant linearization has
rank 327 there, leaving ten tangent coordinates. Its completed transverse
local algebra is the Kuranishi algebra of the Jacobian equations.

The *direct coefficient complex* in parameter order `r` has as cochains the
degree-at-most-seven coefficient perturbations of `F_0` at order `r`; its
differential is the coefficientwise linearization of `det D(F_0+H)=1`. The
*marked-root complex* rewrites the same perturbations in the inverse-cubic
root coordinates and uses the weighted-divergence differential of
[`manuscripts/03-local-rigidity/appendices/root-coordinate-source-flow.tex`](../proof-sources/03-local-rigidity/appendices/root-coordinate-source-flow.md).
A comparison is a chain map
that sends a root-coordinate perturbation to its reconstructed coefficient
perturbation and intertwines these two differentials, modulo the explicitly
listed source and target operation directions.

At degree eight, the selected first-normal calculation has 24 order-five
bending variables. After quotienting their fixed image over `F_1000033`, the
remaining coordinates are

```text
c_14,c_19,c_26,t_8,t_15.
```

The exact modular matrices and their corrected 325-column assembly support
[`RMU-3D8E0002`](../working-mathematics/units/RMU-3D8E0002.md); they are not reproduced here. Characteristic-zero determinant
work is therefore a local CAS task, not the principal online-model task.

## Reusable mathematics

The completed degree-at-most-seven transverse algebra has

```text
length                         584
Hilbert function               (1,10,44,108,157,145,86,30,3)
nilpotence                     m^9=0 != m^8
Cohen--Macaulay type           60
minimal Kuranishi equations    36 = 11+13+11+1 in orders 2,3,4,6.
```

Its reduced germ is a point. Units: [`RMU-C9E196D6`](../working-mathematics/units/RMU-C9E196D6.md), [`RMU-A815C162`](../working-mathematics/units/RMU-A815C162.md),
[`RMU-AF82754A`](../working-mathematics/units/RMU-AF82754A.md), [`RMU-601F2BED`](../working-mathematics/units/RMU-601F2BED.md).

The determinant reconstruction and marked-root source-flow complex agree
through order four. The direct lineage reaches order six, reproduces
`H(5)=145`, finds no new quintic equation, and finds the unique primitive
weight-three sextic. Orders seven and eight lack an independent reconstruction.

Two selected characteristic-zero lower jets are inconsistent through order
six after all 24 bendings are retained ([`RMU-3D8E0001`](../working-mathematics/units/RMU-3D8E0001.md)). The universal
five-variable reduction is exact over `F_1000033`, with kernel/image/cokernel
dimensions `24/5/3` ([`RMU-3D8E0002`](../working-mathematics/units/RMU-3D8E0002.md)). It does not prove constant rank,
characteristic-zero lifting, or complete orbit saturation.

## Exact live problem

Reconstruct the **direct** order-five Kuranishi calculation independently from
the displayed map and slice. The public main source gives every coefficient of
`F_0`, the eleven coefficients removed to define the 337-dimensional slice,
and the determinant equation. Starting from those data, compute the rank-327
linearization over `Q`, choose and record an explicit pivot minor, solve the
327 pivot variables recursively through parameter order five, and form the
Macaulay row space of the resulting equations. The target checks are rank
1857, `H(5)=145`, and no new minimal quintic generator, but they must be
verified after the construction rather than used to select rows.

This task deliberately produces the public matrix/basis package that the
marked-root comparison lacks. The linked source states that a native
contracting homotopy was used through order four, but it does not expose that
homotopy or a root-native order-five matrix. The chain-map comparison is
therefore blocked rather than part of the ready task.

## Tasks and deliverables

### P3-L3A0 — Direct order-five reconstruction

Status: ready.

Inputs: the normalized base map, the 337-dimensional slice, and the determinant
equation in [`manuscripts/03-local-rigidity/main.tex`](../proof-sources/03-local-rigidity/main.md). The recorded target
invariants and evidence boundary are in
[`manuscripts/03-local-rigidity/appendices/source-flow-reconstruction-progress.tex`](../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md)
and [`RMU-C9E196D6`](../working-mathematics/units/RMU-C9E196D6.md).

Deliverable: exact rational pivot and Macaulay matrices with stated monomial
orders, the nonzero pivot-minor certificate, proofs of the fifth-order rank,
Hilbert value, and minimal-generator count, plus a compact public input bundle
with hashes. State computational complexity and every normalization.

### P3-L3A — Marked-root/direct chain comparison

Status: blocked until the native contracting homotopy, root-native bases, and
the P3-L3A0 direct matrix package are public inputs.

Deliverable after recovery: a chain map through order five, a proof that it
intertwines the differentials, and the images of every supplied operation
direction, all independent of the chosen presentations.

### P3-L3A2 — Orders six through eight extension

Status: blocked until P3-L3A, the
order-six coefficient system, and the order-seven and order-eight bases are
packaged as public inputs.

Inputs: P3-L3A and those packaged systems.

Deliverable: chain maps in orders six through eight and a determination of
whether the degree-eight tangent jump has a component not generated by the
known operations.

### P3-L3B — Characteristic-zero rank stratification

Status: local CAS follow-up; blocked until the five-variable matrices are
packaged as public inputs.

Inputs: the corrected matrices underlying [`RMU-3D8E0002`](../working-mathematics/units/RMU-3D8E0002.md).

Deliverable: exact rational determinants, factorization, and rank-drop strata.
Modular ranks alone do not satisfy this task.

### P3-L3C — Residual deformation components

Status: blocked on P3-L3A2 and P3-L3B.

Deliverable: equations for any component not generated by known operations,
or a proof that the reduced degree-eight germ is their union.

## Scope cautions

- The length-584 result concerns the bounded, quotiented degree-seven slice.
- A modular fixed-image calculation is not a characteristic-zero theorem.
- Saturation must retain every known source and target operation component.
