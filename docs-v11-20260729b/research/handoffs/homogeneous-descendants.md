---
title: "Model research brief — Homogeneous Descendants"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 5</p>
# Program 5: Homogeneous Descendants

**Research state:** 29 July 2026, Pacific time, including the two
zero-result large-CAS attempts and the exact six-dimensional compression
transversal.

**Actor guidance:** structural tensor and coupling arguments -> online model;
small exact certificates -> local symbolic; saturated collision geometry ->
staged specialist CAS.

This is the complete public handoff. The linked
[working paper](../../assets/manuscripts/05-homogeneous-descendants-2026-07-22-v11.pdf),
[stable claims](../../results/all-claims.md), and
[Program 5 technical materials](../../evidence/materials.md#5-homogeneous-descendants)
provide proof and replay access without a private bundle.

## 1. Setup and notation

The program asks how efficiently a nonhomogeneous Keller counterexample can
be converted into a cubic-homogeneous or Drużkowski one while preserving a
collision. Start from a degree-at-most-three map

```
K(X) = X + Q(X) + C(X),
```

where `Q` and `C` are quadratic and cubic. Let

```
r = dim span{C_1,...,C_n}
```

be the cubic coordinate-span rank. A rank-sensitive suspension produces a
cubic-homogeneous counterexample in dimension `n+r+1`, improving the usual
coordinate-count bound when the cubic coordinates are dependent.

For the credited public 11-variable input, `r=7`; the construction gives a
19-variable cubic-homogeneous map `I+H`. Its nonlinear Jacobian has generic
Jordan type `(18,1)`, and the original collision lifts. Two standard
descendant mechanisms are then applied to this fixed tensor:

- a symmetric double gives a 38-variable gradient map `I + grad Q`, with
  Hessian-nilpotent quartic potential and generic Hessian type `(35,2,1)`;
- a Gorni--Zampieri/Drużkowski pairing represents `H(z)` as
  `B(Dz)^{*3}` with `BD=0`, producing a square-zero cubic-linear map.

For this fixed tensor, the known pairing interval is

```
52 <= N_pair <= 110.
```

This is model-relative. It is neither a universal lower bound for all
homogeneous counterexamples nor the exact minimum for the 19-variable
tensor.

The second half of the program explores dimension five and compression from
19 to 18 variables. In dimension five, a full-kernel nilpotent quadratic
pencil has an affine collision chart described by fifteen primitive quintics
in sixteen variables. On the regular open set, its parameters form a scalar
plus the binary-sextic module `C lambda + Sym^6(C^2)`, with an explicit
determinant invariant. A **first-normal obstruction** asks whether a
collision-line solution extends to a globally nilpotent Jacobian off the
line.

For compression, exact ranks produce a 109-dimensional family of quadratic
source directions that kill one cubic row; 75 are proved triangular
automorphisms. Modulo these directions the tangent quotient has dimension
20. A complete displayed six-dimensional transversal integrates to exact
rank-six cubic jets, but its universal quartic obstruction is `-1`.

The conceptual link across the descendant ladder is that the 3D, 19D, 38D,
and paired maps present the same underlying three-sheeted function-field
cover. Presentation complexity changes while the finite cover does not.

## 2. Goal and payoff

The main finite goal is to determine the characteristic-zero geometry of the
regular full-kernel collision chart: saturate by the open-locus factors,
find its components and dimensions, inspect the singular locus, and only
then normalize the relevant components. This is the prerequisite for proving
that the first-normal obstruction is nowhere zero, or for finding a component
on which it vanishes.

The theorem-facing goal is two-sided. If the obstruction is nowhere zero,
the regular Jordan-type-(5) collision-line stratum is excluded. If it
vanishes identically or on a component, that component is a construction
lead toward a five-dimensional homogeneous counterexample. A saturation job
must therefore return geometry, not merely “failed to exclude.”

For 19-to-18 compression, the goal is to control nonlinear coupling between
the six-dimensional obstructed transversal and all 109 row-killing
directions, including the 34 directions not currently realized as
triangular automorphisms. Extending the constant quartic obstruction to that
coupled germ would be a serious restricted lower bound on presentation
dimension.

Longer term, boundary invariants of the common three-sheeted cover may give
lower bounds on realization complexity—ordinary degree, homogeneous
dimension, and pairing rank—without repeating tensor-specific elimination
in every presentation.

## 3. What is proved (statements only; proofs at the locators)

| # | Statement | Where |
| --- | --- | --- |
| 1 | The credited public 11-variable counterexample has degree three, 52 nonzero monomial terms, determinant `-2`, and an explicit collision. | [`JCG-A39E3CCD`](../../claims/JCG-A39E3CCD.md) |
| 2 | Rank-sensitive suspension of that input yields an explicit 19-variable cubic-homogeneous Keller counterexample with collision. | [`JCG-38CAAB66`](../../claims/JCG-38CAAB66.md); paper suspension theorem |
| 3 | The fixed 19-variable nonlinear Jacobian has generic Jordan type `(18,1)`. | [`JCG-7AFFFF85`](../../claims/JCG-7AFFFF85.md) |
| 4 | The 38-variable symmetric double is stably right-equivalent to the 19-variable map times an identity factor and presents the same generic cover. | [`JCG-301AAE68`](../../claims/JCG-301AAE68.md) |
| 5 | The fixed Hessian quartic has generic Hessian type `(35,2,1)` and its Laplacian sequence is nonzero at every order. | [`JCG-57051B08`](../../claims/JCG-57051B08.md), [`JCG-D55D3D6A`](../../claims/JCG-D55D3D6A.md) |
| 6 | For the fixed 19-variable tensor, the explicit pairing and equality-case obstruction give `52 <= N_pair <= 110`; the 110-variable square-zero map is a stable presentation of the 19-variable map. | [`JCG-263402AA`](../../claims/JCG-263402AA.md), [`JCG-99288D5E`](../../claims/JCG-99288D5E.md) |
| 7 | On the regular full-kernel chart, regularity is equivalent to `a_7 != 0`, and the parameter space is `C lambda + Sym^6(C^2)` with the displayed determinant invariant. | [`JCG-2EC7F92F`](../../claims/JCG-2EC7F92F.md) |
| 8 | Thirty finite-field full-kernel samples are first-normally obstructed. This is evidence, not a characteristic-zero nowhere-vanishing theorem. | [`JCG-86F5C9FA`](../../claims/JCG-86F5C9FA.md) |
| 9 | The 19-to-18 compression point has 109 row-killing directions, including 75 triangular automorphisms, and a 20-dimensional residual tangent quotient. | [`JCG-F245F636`](../../claims/JCG-F245F636.md) |
| 10 | On the complete displayed six-dimensional transversal, the rank-six cone is the reduced union of three coordinate planes and the quartic obstruction is identically `-1`; no point lifts through quartic order. | [`JCG-24F172FB`](../../claims/JCG-24F172FB.md) |
| 11 | The fixed 19-variable tensor has an `sl_18` codimension-one core; the symplectic alternative is excluded by an exact certificate. | [`JCG-5CA10BFA`](../../claims/JCG-5CA10BFA.md) |

Each statement has the scope shown on its claim page. In particular, the
pairing bound belongs to one fixed tensor; the six-dimensional transversal
does not control arbitrary nonlinear coupling; and the finite-field samples
do not settle characteristic zero.

## 4. The live frontier

**(F1) Saturated collision geometry in characteristic zero.** The input is
an exact fifteen-equation affine chart plus open-locus factors. The desired
output is the saturation, radical/component decomposition, dimensions and
degrees, and open-chart singular locus. Two pinned Macaulay2 attempts
produced no mathematical result: the first failed after heavy memory use,
and the second reached a four-hour limit without reporting a dimension,
degree, decomposition, or singular locus. The next run must reduce variables,
split stages, checkpoint, or use modular/elimination-first methods.

**(F2) Global first-normal obstruction.** The obstruction covariant is
nonzero at thirty finite-field points, and an explicit residue disk is
excluded. That does not prove nowhere-vanishing on every
characteristic-zero component. Once F1 identifies components, compute the
obstruction in each component's function field or prove a geometric rank-drop
contradiction.

**(F3) Nonlinear coupling in 19-to-18 compression.** The exact transverse
cone and constant `-1` obstruction solve one six-dimensional slice. The full
problem includes 109 row-killing directions and target/stable changes. A
normal-form or equivariant argument must show that coupling cannot cancel the
quartic cokernel class, or isolate a smaller coupled system for exact
elimination.

**(F4) Extension theorem for collision monoliths.** The `sl/sp`
prolongation dichotomy is understood for the fixed tensor, but the proposed
general extension theorem `E(N)` remains open, especially the
codimension-one symplectic branch. This is conceptual work and should not be
folded into the collision saturation task.

Dependencies: F1 supplies the geometric components needed by F2. F3 is an
independent compression program. F4 may eventually explain the fixed-tensor
obstruction representation-theoretically but is not required to run F1.

## 5. Graveyard (causes of death — read before proposing routes)

- **Smooth-component interpretation.** A tangent-dimension or smooth point
  in the collision-line chart does not produce a smooth component of the
  global nilpotent-Jacobian scheme. Normal extension imposes additional
  equations. Keep the conclusion at the tangent/line-chart level.
- **Finite-field obstruction samples prove characteristic zero.** Thirty
  nonzero samples can guide component searches but do not prove a covariant
  is nowhere zero on a characteristic-zero curve.
- **Repeat the four-hour saturation unchanged.** The previous job produced
  no mathematical output. More wall time without variable elimination,
  modular staging, checkpointing, or smaller ideals is not a research plan.
- **The six-dimensional transversal is the full coupled germ.** It is a
  complete transversal only inside the displayed ansatz. The 109
  row-killing directions can couple nonlinearly.
- **The 52-cube bound is universal.** Its equality-case argument uses the
  stabilizer/commutant of the fixed 19-variable tensor.
- **Delete an invariant slice from the 38D double.** The graph records that
  no proper nondegenerate invariant linear slice surjects to the original
  variables. A smaller construction must change the realization mechanism
  ([`JCG-FE704029`](../../claims/JCG-FE704029.md)).
- **A row-killing formal direction is a polynomial automorphism.** Only the
  stated 75-dimensional subfamily has that proof.

## 6. Tasks

**P5-T1 — Compute the saturated collision curve and its components.**

Actor: `large_cas`. Status: ready after restrategy.

*Inputs:* the exact denominator-cleared fifteen-equation chart, open-locus
factors, and source-checked CAS template in the public Program 5 materials.

*Payoff:* supplies the component geometry required to settle the global
first-normal obstruction, with either an exclusion or construction lead.

*Attack:* eliminate linear/solvable variables first; test dimension and
codimension modulo several good primes; split saturation by open factors;
checkpoint intermediate ideals; compute normalization only after component
inspection.

*Done when:* a pinned run reports saturation, radical components, dimensions,
degrees, and singular locus with reproducible intermediate stages. A timeout
or heap failure is not completion.

**P5-T2 — Control nonlinear coupling to all row-killing directions.**

Actor: `online_model`. Status: ready.

*Inputs:* the working paper, 109-direction decomposition, exact
six-dimensional cone, and quartic cokernel functional.

*Payoff:* extends the narrow obstruction toward a restricted 19-to-18
noncompression theorem.

*Attack:* use the torus/representation decomposition of the tangent quotient;
separate genuine automorphisms from formal row-killers; identify which
bilinear couplings can reach the one-dimensional quartic cokernel.

*Done when:* a theorem proves the cokernel class survives the full coupled
germ, or reduces cancellation to a finite exact system with resolved inputs.

**P5-T3 — Decide the obstruction on each saturated component.**

Actor: `large_cas` plus conceptual review. Status: blocked on T1.

*Done when:* on every characteristic-zero component, the obstruction is
proved nonzero in the function field or a generic vanishing component is
exhibited with its reconstruction data.

## 7. Evidence and replay index

The technical release contains the fixed 19D tensor, collision and
nilpotence checks, 38D quartic, 110D pairing matrices, Waring/compression
certificates, monolith/prolongation checks, the fifteen global chart
quintics, and finite-field first-normal rank profiles. Exact rational and
finite-field evidence are labeled separately.

The fixed-tensor identities, ranks, pairings, and displayed compression
calculations replay exactly. The large-CAS source and wrappers are validated,
but the two attempted runs produced no saturation or component theorem.
That absence is part of the evidence boundary, not a reason to infer that the
ideal is difficult in a mathematically meaningful sense.

Use the [full-kernel geometry](../../collections/full-kernel-regular-pencil-geometry.md),
[global obstruction frontier](../../collections/global-first-normal-obstruction-in-dimension-five.md),
and [compression package](../../collections/nineteen-to-eighteen-compression-obstructions.md)
as the main claim-level entry points.

For T1, record the open-locus factors and the order of saturation explicitly.
Different saturation orders can expose embedded components differently, so a
final component list without intermediate ideals is difficult to audit. For
T2, every proposed normal form must distinguish actual polynomial
automorphisms from formal coordinate changes and from tangent row-killers.
If the coupling analysis discovers a locus where the quartic functional can
vanish, retain its equations and generic rank data as a candidate
construction package even if later nilpotence conditions fail.
Report component-wise conclusions: dimension, degree, generic stabilizer,
whether the obstruction vanishes, and whether reconstruction yields a global
nilpotent Jacobian. This prevents a single exceptional or embedded component
from being lost behind a generic calculation.
Preserve every open-factor hypothesis and reconstruction denominator in that
component ledger for later independent review.

## 8. Do not do

- Do not rerun the unchanged large-CAS job.
- Do not turn finite-field nonvanishing into a characteristic-zero theorem.
- Do not call the collision-line chart a five-dimensional counterexample.
- Do not extend the six-dimensional `-1` obstruction to all 109 directions
  without a coupling argument.
- Do not claim the 52 lower bound beyond the fixed 19-variable tensor.
- Do not count every row-killing direction as an automorphism.
- Do not report a failed process as mathematical evidence.
- Do not interpret a component where the obstruction vanishes merely as a
  failed exclusion; promote it to a candidate-construction route.

[Back to the Program 5 overview](../programs/homogeneous-descendants.md)
