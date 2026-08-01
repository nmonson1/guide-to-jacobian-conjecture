---
title: "Model research brief — Homogeneous Descendants"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 5</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 1 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v12h · site release <code>living-guide-public-v36-retained-mathematics</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/programs/homogeneous-descendants.md).

# Program 5: Homogeneous Descendants
**Research state:** mathematical checkpoint 30 July 2026, including the two
zero-result large-CAS attempts, the exact six-dimensional compression
transversal, and the boundary-normal/source-coupling packet described below.
Exact scope, dependencies, and direct proof-body links are stated per input.

**Actor guidance:** structural tensor and coupling arguments -> online model;
small exact certificates -> local symbolic; saturated collision geometry ->
staged specialist CAS.

This is the complete public handoff. The linked
[working paper](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf),
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
20. The original six-dimensional transversal integrates to exact rank-six
cubic jets and has quartic obstruction `-1`. The newer packet eliminates all
109 source row-killing directions from a boundary-normal obstruction, but
complete moving target gauge can cancel every fixed quartic functional. The
useful frontier is therefore the secondary degree-five class after quartic
target cancellation.

The conceptual link across the descendant ladder is that the 3D, 19D, 38D,
and paired maps present the same underlying three-sheeted function-field
cover. Presentation complexity changes while the finite cover does not.

### Coverage rule

This page is complete for reusing the fixed descendant constructions and for
assigning the two open geometry problems. Each numbered input states its
exact, often tensor-relative scope; the proof-signature table records
dependencies and exits; the final column links to the proof body. Finite-field
samples and zero-result large-CAS runs remain explicitly non-theorems.

### Compact glossary

- **Cubic coordinate-span rank `r`:** dimension of the span of the cubic
  coordinate functions; it controls the displayed suspension size.
- **Presentation-relative:** a property of this tensor or reduction, not of
  every map presenting the same function-field cover.
- **Vector-Waring length:** least number of cubes of linear forms needed for
  the vector-valued cubic tensor.
- **Full-kernel pencil:** a two-parameter nilpotent Jacobian pencil whose
  kernel has the required global dimension; regularity means one Jordan
  block of size five along the collision line.
- **First-normal obstruction:** the next equation transverse to a
  collision-line solution; it is not implied by regularity on the line.

### Case and dependency map

```text
credited 11D degree-three input
└─ rank-sensitive suspension ── 19D cubic homogeneous tensor H
   ├─ nilpotent-chain analysis ── Jordan type (18,1)
   ├─ cotangent/symmetric double ── 38D Hessian quartic
   ├─ vector-Waring / GZ factorization ── 52 <= N_pair <= 110
   └─ compression toward 18D
      ├─ source coupling to all 109 directions ── exact quartic obstruction
      ├─ moving target gauge ── fixed quartic functionals disappear
      └─ secondary degree-five class under arbitrary cancellation ── open

dimension-five full-kernel collision chart
├─ regular locus a_7 != 0 ── exact
├─ characteristic-zero components ── saturation open
└─ first-normal obstruction on each component ── blocked on saturation
```

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

## 3. Reusable inputs, exact scope, and proof access

| # | Exact input and hypotheses | Claim · direct proof body |
| --- | --- | --- |
| 1 | The credited public eleven-variable map is a degree-three Keller counterexample with 52 nonlinear monomial terms, determinant `-2`, and the displayed collision. It is an external starting input, not derived by the suspension theorem. | [`JCG-A39E3CCD`](../../claims/JCG-A39E3CCD.md) · [statement and formulas used here](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=1) |
| 2 | If `K=X+Q+C` and the cubic coordinate span has dimension `r`, the rank-sensitive construction gives a cubic-homogeneous counterexample in dimension `n+r+1` and lifts a collision. For the eleven-variable input, `r=7`, hence dimension 19. | [`JCG-38CAAB66`](../../claims/JCG-38CAAB66.md) · [proof](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=2) |
| 3 | For the fixed nineteen-variable tensor only, its generic nonlinear Jacobian has Jordan type `(18,1)`. | [`JCG-7AFFFF85`](../../claims/JCG-7AFFFF85.md) · [proof](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=5) |
| 4 | The displayed 38-variable cotangent/symmetric double is polynomially stably right-equivalent to the nineteen-variable map times an identity factor and induces the same generic function-field cover. | [`JCG-301AAE68`](../../claims/JCG-301AAE68.md) · [proof](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=12) |
| 5 | For that fixed double, the generic Hessian Jordan type is `(35,2,1)`. Its explicit inverse-ray formula makes every stated Laplacian term nonzero at every order. This is not a general Hessian-nilpotent nonvanishing theorem. | [`JCG-57051B08`](../../claims/JCG-57051B08.md), [`JCG-D55D3D6A`](../../claims/JCG-D55D3D6A.md) · [Hessian proof](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=7) · [all-order Laplacian proof](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=14) |
| 6 | For the fixed nineteen-variable tensor and the stated full-rank square-zero pairing model, `52 <= N_pair <= 110`; the explicit 110-variable map is a stable presentation of the nineteen-variable map. No global minimum is asserted. | [`JCG-263402AA`](../../claims/JCG-263402AA.md), [`JCG-99288D5E`](../../claims/JCG-99288D5E.md) · [lower and upper proofs](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=9) |
| 7 | On the specified full-kernel pencil chart with `det T != 0`, regularity is equivalent to `a_7 != 0`; after the displayed linear change, the parameter space is `C lambda ⊕ Sym^6(C^2)` with the stated determinant invariant. | [`JCG-2EC7F92F`](../../claims/JCG-2EC7F92F.md) · [proof](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=17) |
| 8 | Exactly thirty enumerated full-kernel samples over `F_7`, `F_11`, and `F_13` are first-normally obstructed. This finite sample is evidence only; it does not imply characteristic-zero nowhere-vanishing. | [`JCG-86F5C9FA`](../../claims/JCG-86F5C9FA.md) · [finite sample calculation](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=18) |
| 9 | At the fixed nineteen-to-eighteen compression point, the affine row-killing family has dimension 109, including a proved 75-dimensional triangular-automorphism subspace; the residual tangent quotient has dimension 20. Other row-killers are not automatically automorphisms. | [`JCG-F245F636`](../../claims/JCG-F245F636.md) · [proof](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=18) |
| 10 | On the complete displayed six-dimensional transversal, the rank-at-most-six cone is the reduced union `V(u_3,u_5) ∪ V(u_0,u_3) ∪ V(u_2,u_5)`, and the quartic obstruction is identically `-1`; no point of this transversal lifts through quartic order. This paper statement alone did not control the 109 directions; item 12 records the later source-coupling result. | [`JCG-24F172FB`](../../claims/JCG-24F172FB.md) · [proof](../../assets/manuscripts/05-homogeneous-descendants-2026-07-29-v13.pdf#page=19) |
| 11 | For the fixed nineteen-variable presentation, the codimension-one collision core has Lie algebra `sl_18`; the symplectic alternative is excluded by the exact full-rank alternating-form system. This is presentation-relative. | [`JCG-5CA10BFA`](../../claims/JCG-5CA10BFA.md) · [full archival proof](../../assets/proof-archives/05-homogeneous-descendants-2026-07-22-v8.pdf#page=23) |
| 12 | In the recovered v2 boundary-normal model, the quartic class is homological through `I^2` but nonzero in `I^2/I^3`; three K-basic obstruction functions eliminate every point of the exact rank-six cone after all 109 source row-killing directions are included. A coupled one-parameter source path remains nonhomological for every complex parameter. | Fresh exact replay of the seven v2 verifiers on 30 July 2026. |
| 13 | Static admitted target gauge of degree at most three does not kill the quartic class; degree-four target gauge can. After cancellation, a degree-five remainder survives the complete stored 17-dimensional quartic-null triangular family. The v3 packet further reports component-wise nonlinear secondary unit ideals after one chosen cancellation. | Exact v2 rank replay; v3 source/results inspection only. |

Each statement has the scope shown on its claim page. In particular, the
pairing bound belongs to one fixed tensor; the six-dimensional transversal
does not control arbitrary nonlinear coupling; and the finite-field samples
do not settle characteristic zero.

**Paper-audit checkpoint, 30 July 2026.** The central construction spine is
coherent, but the vector-Waring lower bound needs its equality-case lemma
written out. The fixed 19D and 38D constructions are strong. The 110-variable
and Appendix E certificates were not independently regenerated in the audit,
and none of the new six-dimensional or 109-direction calculations supplies a
global minimum-dimension theorem.

### Proof-signature index

| Inputs | Proof signature / reusable output | Boundary exits |
| --- | --- | --- |
| 1–2 | Factor the cubic layer as `C=Bq` using a basis of its coordinate span; stabilize by triangular maps, adjoin a homogenizing coordinate, and take the Schur complement `det(I+tJQ+t^2BJq)=det JK(tX)=1`. Lift the explicit collision by `(p,q(p),1)`. **Output:** the general `n+r+1` suspension and the fixed 19D tensor. | Optimal only inside the factorized suspension model; other stable presentations may be smaller. |
| 3 | Exhibit two generic kernel vectors, certify rank 17 at one specialization, and compute `A^17 e_t` as a nonzero multiple of one kernel vector. Nilpotence plus two blocks forces `(18,1)`. **Output:** a long-chain certificate and kernel basis. | Generic Jordan type; special fibers can degenerate. |
| 4–5 | Cotangent-double the map, then apply a complex linear twist so the nonlinear part is a gradient. Similarity identifies the Hessian with a block matrix built from `A` and `A^T`; kernel identities, a rank-35 specialization, and a nonzero `N^34` entry give `(35,2,1)`. An explicit inverse ray plus Zhao's inversion formula yields nonzero Laplacian values at every relevant order. **Output:** Hessian type and all-order scalar certificate. | Applies to the fixed 38D potential; it is not a general vanishing theorem. |
| 6 | Lower bound: derivatives span a 39-space with a 12-dimensional common zero block; equality would force coordinate-projector invariance, but the computed stabilizer commutant contains a nonzero square-zero matrix. Upper bound: explicit full-rank `B,D` satisfy `BD=0` and `H=B(Dz)^3`; Sylvester transfers the Keller determinant and an explicit correction transfers a collision. **Output:** `52 <= N_pair <= 110`. | Fixed tensor and full-rank square-zero pairing model only. |
| 7–8 | Factor the fourth power of the full-kernel pencil as `6 a_7 k ell T^{-1}K`; it is regular exactly when `a_7!=0`. A linear change identifies parameters with `C lambda ⊕ Sym^6(C^2)` and gives the determinant invariant. Exhaustive samples over `F_7,F_11,F_13` then test the first-normal covariant. **Output:** invariant chart plus a finite-field audit set. | Sample nonvanishing is not a characteristic-zero component theorem. |
| 9–10 | Compute the affine row-killing family and its quotient by proved triangular automorphisms. At a rank-six point, take a six-coordinate transversal; its determinantal cone is the reduced union of three coordinate planes. The functional `Gamma_4`, extracting the `h^4` coefficient of `E_z`, kills every quartic homological image but equals `-1` on the full explicit family. **Output:** an integrated transverse cone with a constant obstruction. | Nonlinear coupling to all 109 directions, target changes, and stable changes remains. |
| 11 | Minimality makes the collision algebra monolithic; nonzero second prolongation and the classification of irreducible prolongations leave `sl` or `sp`. For the fixed tensor, partial multiplications generate `End(U)` and a full-rank alternating-form system excludes `sp`, leaving `sl_18`. **Output:** special-linear core and an extension-theorem template. | Presentation-relative; it does not prove dimension minimality. |

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

**(F3) Nonlinear coupling in 19-to-18 compression.** Source coupling is no
longer the main missing step: the v2 K-basic duals eliminate all 109
row-killing directions on the exact rank-six cone, and the coupled-path
certificate is uniform over its exceptional cubic field. Target gauge is the
real boundary. Complete moving target gauge destroys every fixed quartic
functional; admitted degree-four shears can cancel the primary representative.
The exact v2 cascade leaves a degree-five class after the stored
17-dimensional quartic-null family. The v3 notes report stronger
component-wise nonlinear secondary unit ideals after one chosen `h^4 e_z`
cancellation, but several referenced pickles/modules are absent from the
recovered packet. Prove the secondary class survives arbitrary moving target
and stable cancellation, or return the cancellation locus as a compression
lead.

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
- **The six-dimensional transversal is the full coupled germ.** The newer
  source-coupling calculation controls all 109 row-killers only in its stated
  boundary-normal model. It does not control arbitrary moving target or
  stable changes.
- **The 52-cube bound is universal.** Its equality-case argument uses the
  stabilizer/commutant of the fixed 19-variable tensor.
- **Delete an invariant slice from the 38D double.** The graph records that
  no proper nondegenerate invariant linear slice surjects to the original
  variables. A smaller construction must change the realization mechanism
  ([`JCG-FE704029`](../../claims/JCG-FE704029.md)).
- **A row-killing formal direction is a polynomial automorphism.** Only the
  stated 75-dimensional subfamily has that proof.

## 6. Tasks

Each item is a task capsule. T1 must return staged characteristic-zero
geometry, not process telemetry. Checkpoint every saturation and open factor;
if an obstruction vanishes generically on a component, stop the exclusion
workflow and return that component as a reconstruction-ready construction
lead.

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

**P5-T2 — Control the secondary class under arbitrary moving target gauge.**

Actor: `online_model`. Status: ready.

*Inputs:* the working paper, the v2 K-basic source-coupling certificate, the
moving-target rank calculation, the quartic-null 17-family, and the
fragmentary v3 component-wise secondary calculations.

*Payoff:* turns the fully replayed source obstruction into a restricted
19-to-18 noncompression theorem, or exposes a genuine compression locus.

*Attack:* formulate the moving source/target quotient intrinsically; classify
all quartic cancellations; transport the first nonzero secondary class
through that family; reconstruct missing v3 inputs independently rather than
treating its saved fragments as a complete replay packet.

*Done when:* every admitted quartic cancellation has a degree-five-or-higher
obstruction with a proof or independently replayed certificate, or an
explicit cancellation locus is reconstructed as a candidate 18D model.

**P5-T3 — Decide the obstruction on each saturated component.**

Actor: `large_cas` plus conceptual analysis. Status: blocked on T1.

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

All seven self-contained v2 boundary-frame verifiers replay in the
repository's pinned environment, including the heavier Smith-form
coupled-path calculation. The v3 results are not assigned the same replay
status: its recovered directory contains useful scripts, logs, and small
pickles but omits several companion inputs those scripts reference.

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
component ledger.

## 8. Do not do

- Do not rerun the unchanged large-CAS job.
- Do not turn finite-field nonvanishing into a characteristic-zero theorem.
- Do not call the collision-line chart a five-dimensional counterexample.
- Do not retreat to the claim that all 109 source directions are untreated;
  the v2 K-basic certificate handles them in its stated model.
- Do not extend that source result through arbitrary moving target or stable
  gauge without a secondary-class argument.
- Do not claim the 52 lower bound beyond the fixed 19-variable tensor.
- Do not count every row-killing direction as an automorphism.
- Do not report a failed process as mathematical evidence.
- Do not interpret a component where the obstruction vanishes merely as a
  failed exclusion; promote it to a candidate-construction route.

[Back to the Program 5 overview](../../research/programs/homogeneous-descendants.md)

[Back to the Program 5 overview](../programs/homogeneous-descendants.md)
