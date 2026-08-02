---
title: "Model research brief — Homogeneous realization and compression"
description: "A self-contained mathematical handoff for a research model."
---

# Lane 6: Homogeneous realization and compression

<p class="claim-tag">Lane 6 · Updated 2 August 2026</p>

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

### Compiler-owned retained result

!!! info "First-class retained mathematics"
    This result, its exact argument, and its evidence boundary are
    rendered from one retained-math v2 selection. The
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

#### Exact argument

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

#### Evidence and exact source links

##### Exact cubic ranks at all three exceptional finite slopes

Exact specialization over Q and Q(sqrt(-3)) of the complete cubic tangent system at every root of the generic pairing generator.

**Establishes:** At r=4 the effect and augmented ranks are (5,6); at each conjugate ratio they are (5,5), giving a 17-dimensional affine cubic-lift fibre.

**Locator:** [Pinned source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0/research-tools/filtered_operation_complex/adapters/program5_rank_six_exceptional_finite_lines.py)

**Does not establish**

- That either conjugate cubic-lift fibre contains an order-four lift.
- Any classification beyond the selected finite plane.

##### Generic finite-slope cubic left-kernel calculation

Exact construction of the cubic effect matrix over Q(r), its primitive polynomial left kernel, and the ideal of pairings with the cubic residual.

**Establishes:** Outside the roots of (r-4)(r^2-8r+64), every finite direction in the selected plane is cubically obstructed.

**Locator:** [Pinned source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0/research-tools/filtered_operation_complex/adapters/program5_rank_six_generic_line_obstruction.py)

**Does not establish**

- Obstruction at one of the three roots of the pairing generator.
- Anything about the point at infinity or directions outside the selected plane.

##### Order-four coefficient-span separator over Q(sqrt(-3))

The complete 17-parameter cubic-lift fibre is propagated to order four; a K-linear functional annihilates every variable coefficient and pairs -1152 with the constant term.

**Establishes:** No point of either conjugate 17-dimensional cubic-lift fibre extends through order four.

**Locator:** [Pinned source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0/research-tools/filtered_operation_complex/adapters/program5_rank_six_algebraic_fourth_order_kuranishi.py)

**Does not establish**

- An obstruction for an untested tangent plane or the full finite row-base fibre.
- A global or convergent deformation theorem.


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

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
