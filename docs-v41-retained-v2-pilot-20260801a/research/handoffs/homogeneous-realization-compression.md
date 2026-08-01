---
title: "Model research brief — Homogeneous realization and compression"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 6</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 1 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v14 · site release <code>living-guide-public-v41-retained-v2-pilot</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current text proofs — preferred"
    Use the [current TeX source and exact label anchors](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 6: Homogeneous realization and compression

## Research objective

Determine the true homogeneous realization complexity of the fixed
three-sheeted cover and decide whether its 19-variable cubic-homogeneous
presentation compresses to 18 variables.  Separate invariants of the cover
from obstructions attached only to one tensor or operation slice.

The primary reference is [Program 5](homogeneous-descendants.md), with local
deformation input from [Program 3](local-rigidity-and-deformation-algebra.md).
The newest retained units are the
[five-dimensional polynomial-gauge core](../working-mathematics/units/RMU-5D8E0001.md),
its [three residual surfaces](../working-mathematics/units/RMU-5D8E0002.md),
and the [selected-plane cubic/quartic classification](../working-mathematics/units/RMU-5D8E0003.md).

## Reusable mathematics

The rank-sensitive suspension of the fixed degree-at-most-three map gives a
19-variable cubic-homogeneous counterexample.  Its symmetric cotangent double
has 38 variables.  A Druzkowski pairing is known with length at most 110 and
at least 52 for this fixed tensor.  These are realization bounds, not global
minimum dimensions among all maps with the same cover.

In the weight-zero row-killing calculation, the relevant fibre has dimension
20.  Thirteen reconstructed triangular directions and the elementary shear
`b^2 e_h` integrate to polynomial automorphisms.  Their quotient is six
dimensional; imposing the normal cubic Casimir relation leaves the exact core

```text
A=k_14, B=k_19, C=k_23, D=k_67, E=k_85.
```

Eleven rational degree-one dual sections exclude every core point outside
three two-dimensional surfaces:

```text
Z0: A=B=D=0;
Z1: D=0, A=-3B, C^2+36C+50B-104BC=0;
Z2: A=3D, B=-D, C^2+36C+104CD-50D-84D^2=0;
```

In each surface `E` is free.  The result detects the secondary obstruction by
degree-one dual sections.  It does not say the obstruction vanishes on those
surfaces.  A finite higher-order conjugation theorem from the full weight-zero
fibre to the displayed core is also still missing.

### Compiler-owned retained result

!!! info "Generated from first-class mathematics"
    This result, its complete argument, its evidence boundary, and its
    next task are rendered from one retained-math v2 selection. The
    [machine-readable selection](retained-math-v2-pilot.json) is pinned
    by the handoff release metadata.

#### Cubic and quartic obstructions on the selected finite rank-six plane

`RMU-5D8E0003` · `computational_result` · statement version `1`

For the selected finite two-dimensional rank-six plane in the pinned Program 5 operation model, generic finite slope ratios admit no cubic lift. The exceptional rational ratio r=4 has effect rank 5 and augmented rank 6 and is intrinsically obstructed at cubic order. The two conjugate ratios r=4+4 sqrt(-3) and r=4-4 sqrt(-3) have effect and augmented rank 5, hence 17-dimensional affine fibres of cubic lifts, but the full algebraic order-four Kuranishi map has a nonzero intrinsic obstruction on each; at the first conjugate an exact coefficient-span certificate pairs to -1152, and field conjugation gives the second.

**Hypotheses**

- The tensors, Schur chart, tangent splitting, selected finite plane, and slope parameter are exactly those at GitHub PR 1 head fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0.
- The order-three and order-four systems retain the complete tangent-kernel freedom implemented at that head.
- All calculations use exact arithmetic over Q or Q(sqrt(-3)) under SymPy 1.14.0.

**Applies to**

- Cubic and quartic formal compatibility of the selected finite rank-six plane, including all three exceptional finite slopes.

**Limitations**

- The result does not classify the full 15-dimensional finite row-base fibre or the infinity fibre.
- It does not impose the separate compression functional or quotient by every source, target, and stable operation.
- It does not prove convergence, algebraization, or a global 19-to-18 noncompression theorem.

#### Complete argument

**Finite-slope cubic classification followed by the intrinsic quartic separator** · `ARG-RMU5D8E0003-FINITE-PLANE` · `computational_argument`

The generic left-kernel pairing reduces the finite projective line to three exact slopes; direct rank tests exclude the rational slope cubically, and a constant-term separator excludes the two conjugate slopes at order four.

Write the finite projective direction in the selected second-order-compatible plane as $\theta(r)=\theta_v+r\theta_u$. The exact quadratic Kuranishi residual is identically zero. Over $\mathbf Q(r)$, let $E(r)$ be the cubic tangent-effect matrix and $b(r)$ the deterministic cubic residual. A polynomial basis of the left kernel of $E(r)$ has pairings with $b(r)$ whose ideal is generated by

$$g(r)=(r-4)(r^2-8r+64).$$

Consequently, if $g(r)\ne0$, some left-null functional pairs nontrivially with $b(r)$, so $E(r)x=-b(r)$ has no solution and there is no cubic lift. It remains to specialize at the three roots. At $r=4$, the effect matrix has rank $5$ while the augmented matrix has rank $6$, so this slope is also cubically obstructed. At $r=4\pm4\sqrt{-3}$ both ranks are $5$. Since the rank-six tangent space has dimension $22$, each conjugate slope therefore has a $17$-dimensional affine fibre of cubic lifts.

Work at $r_+=4+4\sqrt{-3}$ over $K=\mathbf Q(\sqrt{-3})$. Choose one affine quadratic correction $P_2^0$ and a basis $v_1,\ldots,v_{17}$ of the homogeneous cubic-lift fibre. For $P_2(x)=P_2^0+\sum x_i v_i$, solve the cubic image equation linearly for the corresponding $P_3(x)$. Substitution into the order-four residual gives a $K$-valued polynomial map $Q_4(x)$ of degree at most two. Collect its constant coefficient $q_0$ and all linear and quadratic coefficient vectors. The variable-coefficient span has rank $1$, whereas adjoining $q_0$ raises the rank to $2$. Equivalently, the recorded left-null functional $\lambda$ annihilates every nonconstant coefficient and satisfies $\lambda(q_0)=-1152\ne0$. Hence $Q_4(x)$ cannot vanish for any point of the complete $17$-dimensional cubic-lift fibre. All model tensors are rational, so Galois conjugation gives the same obstruction at $r_-=4-4\sqrt{-3}$. Together with the generic and rational-slope cubic exclusions, this proves the stated finite-plane classification.

**This argument does not establish**

- A classification of the full 15-dimensional finite row-base fibre or the point at infinity of this selected plane.
- Compatibility with the separate compression functional or a quotient by every source, target, and stable operation.
- Convergence, algebraization, or a global 19-to-18 noncompression theorem.

#### Evidence and exact replay boundary

##### Exact cubic ranks at all three exceptional finite slopes

`EVD-RMU5D8E0003-EXCEPTIONAL-CUBIC` · `program`

Exact specialization over Q and Q(sqrt(-3)) of the complete cubic tangent system at every root of the generic pairing generator.

**Establishes:** At r=4 the effect and augmented ranks are (5,6); at each conjugate ratio they are (5,5), giving a 17-dimensional affine cubic-lift fibre.

**Locator:** [Pinned source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0/research-tools/filtered_operation_complex/adapters/program5_rank_six_exceptional_finite_lines.py)

**Replay**

- `python research-tools/filtered_operation_complex/symbolic_tests/test_program5_exceptional_finite_lines.py`

Environment:

- Run from the repository root at exact Git commit fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0.
- Python 3.12 and SymPy 1.14.0.

Expected:

- r=4 has rank 5 and augmented rank 6.
- Both conjugate ratios have rank 5 and augmented rank 5.

**Does not establish**

- That either conjugate cubic-lift fibre contains an order-four lift.
- Any classification beyond the selected finite plane.

##### Generic finite-slope cubic left-kernel calculation

`EVD-RMU5D8E0003-GENERIC-CUBIC` · `program`

Exact construction of the cubic effect matrix over Q(r), its primitive polynomial left kernel, and the ideal of pairings with the cubic residual.

**Establishes:** Outside the roots of (r-4)(r^2-8r+64), every finite direction in the selected plane is cubically obstructed.

**Locator:** [Pinned source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0/research-tools/filtered_operation_complex/adapters/program5_rank_six_generic_line_obstruction.py)

**Replay**

- `cd research-tools && python -m filtered_operation_complex.adapters.program5_rank_six_generic_line_obstruction`

Environment:

- Start from a checkout at exact Git commit fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0.
- Python 3.12 and SymPy 1.14.0.

Expected:

- The pairing-ideal generator factors as (r - 4)(r^2 - 8*r + 64).
- The interpretation boundary is the selected finite tangent plane.

**Does not establish**

- Obstruction at one of the three roots of the pairing generator.
- Anything about the point at infinity or directions outside the selected plane.

##### Order-four coefficient-span separator over Q(sqrt(-3))

`EVD-RMU5D8E0003-QUARTIC-SEPARATOR` · `certificate`

The complete 17-parameter cubic-lift fibre is propagated to order four; a K-linear functional annihilates every variable coefficient and pairs -1152 with the constant term.

**Establishes:** No point of either conjugate 17-dimensional cubic-lift fibre extends through order four.

**Locator:** [Pinned source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0/research-tools/filtered_operation_complex/adapters/program5_rank_six_algebraic_fourth_order_kuranishi.py)

**Replay**

- `python research-tools/filtered_operation_complex/symbolic_tests/test_program5_algebraic_fourth_order_kuranishi.py`

Environment:

- Run from the repository root at exact Git commit fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0.
- Python 3.12 and SymPy 1.14.0.

Expected:

- The cubic-lift affine dimension is 17.
- The variable-coefficient rank is 1 and the constant augmented rank is 2.
- The certificate pairing with the constant term is -1152.

**Does not establish**

- An obstruction for an untested tangent plane or the full finite row-base fibre.
- A global or convergent deformation theorem.

### Current boundary and next task

#### Extend the selected-plane obstruction to the full finite row-base fibre

`OBL-P5-FULL-FINITE-ROW-BASE`

Determine the formal lifting locus on the full 15-dimensional finite row-base fibre, or prove a coordinate-free obstruction that reduces it to already excluded strata, while retaining the separate compression functional and all relevant source, target, and stable-operation quotients.

The selected-plane calculation is decisive on its two-dimensional slice but does not supply the finite-fibre classification needed for a global 19-to-18 noncompression theorem.

**Done when**

- The full finite row-base parameter space and every quotient or functional imposed are stated exactly.
- Every surviving stratum is either excluded by a proof/certificate or retained with an exact defining ideal and lifting order.
- The result explicitly states what remains at the infinity fibre and at the convergence/algebraization boundary.

#### Find the next invariant obstruction beyond the selected plane

`TSK-P5-FULL-FINITE-ROW-BASE`

**Goal:** Use the exact selected-plane argument as a base case to obtain a rigorous reduction, obstruction, or counterexample on the full finite rank-six row-base fibre.

**Payoff:** A successful reduction would replace an isolated slice calculation by the finite-fibre input required for the Program 5 noncompression strategy.

**Inputs**

- [`RMU-5D8E0001`](../working-mathematics/units/RMU-5D8E0001.md) (unit)
- [`RMU-5D8E0002`](../working-mathematics/units/RMU-5D8E0002.md) (unit)
- [`RMU-5D8E0003`](../working-mathematics/units/RMU-5D8E0003.md) (unit)
- `ARG-RMU5D8E0003-FINITE-PLANE` (argument)
- `EVD-RMU5D8E0003-GENERIC-CUBIC` (evidence)
- `EVD-RMU5D8E0003-EXCEPTIONAL-CUBIC` (evidence)
- `EVD-RMU5D8E0003-QUARTIC-SEPARATOR` (evidence)

**Suggested approaches**

- Identify a coordinate-free version of the cubic left-kernel pairing or quartic constant-term separator and study its degeneracy ideal on the full finite fibre.
- Stratify by exact ranks of the cubic effect and augmented matrices, then compute higher Kuranishi maps only on the rank-equality strata.
- Exploit the weight-zero quotient and the three residual surfaces from RMU-5D8E0002 before expanding the full 15-variable system.

**Done when**

- A theorem, exact computational result, or counterexample resolves a nontrivial full-fibre stratum not already covered by the selected plane.
- All equations, fields, quotient operations, and replay inputs are explicit.
- The conclusion distinguishes formal finite-order obstruction from convergence and from the global compression claim.

**Research freedom**

- Pursue a stronger invariant theorem, a different slice with a conceptual bridge, or a counterexample if it has greater leverage than the suggested approaches.
- Introduce a better coordinate system or connect this problem to deformation, representation, or singularity theory, provided the map back to the retained tensors is explicit.

**Scope fences**

- Do not infer a full-fibre result merely from generic samples or finite-field ranks.
- Do not treat the selected-plane theorem as imposing the separate compression functional.
- Do not call a finite-order formal obstruction a convergence or algebraization theorem.

## High-priority next work

1. Prove finite triangular-gauge compatibility, transporting every higher
   normal term and the moving cokernel section to the five-dimensional core.
2. Construct degree-two dual sections on `Z0`, `Z1`, and `Z2`; prove their
   evaluation ideals are units or isolate a smaller residual locus.
3. Impose the separate compression functional and the full moving target and
   stable gauges.
4. Seek a conceptual lower bound from collision monoliths or the `sl/sp`
   dichotomy that depends on the cover rather than one presentation.

Moving target gauge can kill fixed quartic functionals, so a single scalar
quartic witness is not a global compression invariant.  Use the cokernel sheaf
and the order/Fitting ideal of the moving obstruction section.  Do not infer
finite nonlinear gauge equivalence from a tangent-space direct sum.

## Useful deliverable

The most direct next theorem is unit detection on all three residual surfaces,
conditional only on a separately stated finite-gauge lemma.  A construction
on a persistent surface is equally important.  Broader structural approaches
are encouraged if they account for all moving gauge directions and say exactly
which realization complexity they bound.

[Back to the portfolio hub](state-of-the-program.md)
