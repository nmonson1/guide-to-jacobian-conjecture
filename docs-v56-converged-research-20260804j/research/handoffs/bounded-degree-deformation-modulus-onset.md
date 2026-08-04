---
title: "Model research brief — Formal effectivity and finite Kuranishi complexity"
description: "A self-contained mathematical handoff for a research model."
---

# Formal effectivity and finite Kuranishi complexity

<p class="claim-tag">Lane 3 · Updated 4 August 2026</p>

## Why this lane matters

Finite-order deformation calculations can make two maps look equivalent even
when no polynomial equivalence exists over the complete base. This lane asks
which intrinsic datum detects that failure, and how the required complexity
grows with the Artin order.

## Setup and notation

This lane contains two related threads and one ready task in each: Thread A
asks for the exact coverage contract needed before the remaining rational
Betti calculation, while Thread B asks for a non-tautological finite-level
effectivity invariant. No theorem currently identifies the two deformation
complexes.

Their common theme is the gap between finite-order and genuine equivalence.
They are otherwise parallel research packets. Thread A studies bounded-degree
deformations of the normalized degree-seven counterexample, transverse to its
normalized affine source orbit. Thread B studies a separate one-parameter
cubic-frame family. No comparison map between them is assumed.

### Thread A — finite Kuranishi reconstruction

Work over a characteristic-zero field. Let \(G:\mathbf A^3\to\mathbf A^3\)
be the normalized degree-seven counterexample, and let \(K_{3,7}\) be the
coefficient scheme of degree-at-most-seven Keller maps \(H\) satisfying
\(H(0)=0\), \(JH(0)=I\), and \(\det JH=1\). The fixed affine slice through
\(G\) is transverse to the normalized affine source action on \(K_{3,7}\).
Its completed local ring is the Kuranishi quotient below; it measures the
scheme-theoretic transverse thickening of the orbit inside the bounded-degree
Keller scheme, not unrestricted formal deformations of \(G\).

The slice has ten tangent parameters \(u_1,\ldots,u_{10}\), maximal ideal

\[
\mathfrak m=(u_1,\ldots,u_{10}),
\]

and a filtered transverse Kuranishi ideal
\(I=I_\kappa\subset k[[u_1,\ldots,u_{10}]]\). The subscript is retained in
the exact border-basis packet and refers to this same completed Kuranishi
ideal, not a second deformation problem. The torus weights of the tangent
variables in the displayed order are

\[
(-1,2,-3,-2,-1,0,1,1,2,3).
\]

A new minimal generator of initial
degree \(r\) is a nonzero degree-\(r\) initial class in \(I/\mathfrak m I\).
This is the convention used by the order-five and order-six certificates.

### Thread B — formal effectivity of the cubic frame

For a commutative \(\mathbf Q\)-algebra \(R\), put

\[
c=2x-3x^2y-x^3z,\qquad t=y+\frac1x,\qquad r=\frac2x.
\]

Here **admissible** means
\(A(0)=0\), \(A'(0)=1\), \(B(0)=-2\), and
\(B'(0)=-2A''(0)\). For an admissible pair \(A,B\in R[c]\), the cubic-frame map
\(G_{A,B}=(a,b,c)\) is defined by

\[
b=r-3A(c)t^2-2B(c)t,\qquad
2a=A(c)t^3+B(c)t^2+tb.
\]

The admissibility conditions make these expressions polynomial. Define

\[
A_\alpha(c)=c(1+\alpha c),\qquad
B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\]

and let \(F_{\alpha,q}=G_{A_\alpha,B_{\alpha,q}}\) be the associated
cubic-frame Keller map. For \(\phi(c)\in cR[c]\), the source root translation

\[
\Theta_\phi(x,y,z)=
\left(x,\,y+\phi(c),\,z-3\frac{\phi(c)}x\right)
\]

is polynomial because \(c/x=2-3xy-x^2z\). The explicit triangular target
map \(\Xi_\phi\) in the linked theorem satisfies

\[
G_{A,B+3A\phi}=\Xi_\phi\circ G_{A,B}\circ\Theta_\phi.
\]

A **framed degree-\(D\) equivalence** here means one of these \(c\)-fixed
root translations with \(\deg_c\phi\le D\), together with its displayed
target correction. This is narrower than arbitrary stable polynomial
left-right equivalence.

For \(q\ne q'\) and \(R_M=\mathbf C[s]/(s^M)\), let
\(\kappa_M(q,q')\) be the minimum, over all ordinary or stabilized polynomial
left-right equivalences between \(F_{s,q}\) and \(F_{s,q'}\) over \(R_M\), of

\[
\max\{m,\deg\Phi,\deg\Phi^{-1},\deg\Psi,\deg\Psi^{-1}\},
\]

where \(m\) is the number of stabilization variables.

For \(\alpha=s\), the normalized conductor chart has an escaping divisor
\(c=-1/s\). Its boundary value
\(B_{s,q}(-1/s)=q+2\) is the **escaping conductor decoration** that the
stable classification recovers on the generic fibre.

## Reusable mathematics

### Thread B: exact framed law

Put \(\delta=q'-q\). A framed translation of \(c\)-degree at most \(D\)
exists exactly when \(\delta\alpha^{D+2}=0\). It is unique, with residual
\((-1)^D\delta\alpha^{D+2}c^{D+2}\). Thus for
\(\alpha=s\bmod s^M\) its exact degree is \(M-2\).

### Thread B: formal non-effectivity

The maps \(F_{s,q}\) and \(F_{s,q'}\) are compatibly polynomially
left-right equivalent over every \(R_M\), but are not stably polynomially
left-right equivalent over \(\mathbf C[[s]]\). The nonexistence uses the
proved stable \(q\)-classification after passage to the generic fibre.

### Thread B: unrestricted lower bound

The exact theorem proves

\[
\liminf_{M\to\infty}
\frac{\kappa_M(q,q')}{\log\log M}\ge \frac1{\log4}.
\]

It does not prove a linear unrestricted degree law.

### Thread A: finite reconstruction

The exact direct-coordinate replay gives

| degree | initial rank | Hilbert value | new minimal generators |
| ---: | ---: | ---: | ---: |
| 2 | 11 | 44 | 11 |
| 3 | 112 | 108 | 13 |
| 4 | 558 | 157 | 11 |
| 5 | 1857 | 145 | 0 |

At degree five, \(\operatorname{rank}(\mathfrak m I)=2503\) and
\(\operatorname{rank}(I)=2538\). This is an exact replay of recovered
equations, not an independent derivation from the canonical degree-seven
base map in the linked source packet.

### Thread A: the primitive sextic

The order-six computation gives one new weight-three class, represented by

\[
642816u_1u_6u_7^4-60u_4u_7u_8^4+5u_4u_8^5
-75u_5u_6u_8^4.
\]

Here \(\operatorname{rank}(\mathfrak m I)=542\),
\(\operatorname{rank}(I)=545\), and the corresponding pure-sextic initial
ranks are \(341\) and \(342\). This is a finite weighted calculation, not an
orbit classification.

### Thread A: exact rational second Betti number

For Thread A, let
\(S=\mathbf Q[[u_1,\ldots,u_{10}]]\) and
\(R=S/I_\kappa\) be the length-584 completed transverse local algebra of
the fixed Kuranishi problem. Its exact border basis and ten rational
multiplication matrices define the Koszul complex. The 49 exact rational
blocks contributing to \(\operatorname{Tor}^S_2(R,\mathbf Q)\) give

\[
\beta_2=354\qquad\text{over }\mathbf Q.
\]

The audit receipt pins the queue, every stored exact rank, the multiplier and
rank executable, and the replayed aggregate. The endpoint values
\(\beta_0=1\), \(\beta_1=36\), and \(\beta_{10}=60\) are also exact over
\(\mathbf Q\). Thus only \(\beta_3,\ldots,\beta_9\) remain to be certified
over \(\mathbf Q\); the
three good-prime tables are cross-checks rather than replacements for those
rational calculations.

## Live problem

Find a non-tautological finite-level invariant of the unframed stable
left-right groupoid that recovers the escaping conductor decoration in the
family \(F_{s,q}\). Merely naming the stable-equivalence class does not count:
the invariant must be explicit at each Artin level and come with a proved
transport inequality under complexity-\(D\) equivalences. Use it to improve
the double-logarithmic lower bound, or explain sharply why this finite-level
information cannot do so.

The rational-Betti calculation has a separate first step.  Build a
hash-pinned task manifest for every nonzero weight block of the adjacent
Koszul differentials needed for \(\beta_3,\ldots,\beta_9\), and prove from the
exact graded basis that the manifest is complete and that its aggregation
formulas compute precisely those homology dimensions.  The multiplier and
rank engine are supplied, but the rank campaign is not ready until that
coverage contract exists; good-prime records may guide resource estimates but
may not define the characteristic-zero queue.

The direct/marked-root chain comparison remains blocked: the marked-root
contracting homotopy and compatible basis beyond order four are not in the
packet, and the known ranks and sextic are not a substitute for that map.

## Current tasks

<!-- RETAINED_TASKS_START -->
### Build the exact Betti queue and prove its coverage contract — Ready now

`TSK-L3-RATIONAL-BETTI-COVERAGE-V1` · computation, proof · bounded

**Goal.** Enumerate every nonzero torus-weight block of the adjacent Koszul differentials needed for beta_3 through beta_9, fix one deterministic task manifest, and prove from the exact graded basis that the manifest is complete and that its aggregation formulas compute precisely those seven homology dimensions.

**Why it matters.** This makes the later rank campaign finite, schedulable, and fail-closed instead of assuming that a set of generated jobs covers the Koszul complex.

**Public inputs.**

- [Exact rational second Betti number](../working-mathematics/units/RMU-3B2E0001.md) (retained unit `RMU-3B2E0001`).
- [Rational Betti certification](../working-mathematics/units/RMU-C76886E8.md) (retained unit `RMU-C76886E8`).
- [Exact 584-dimensional multiplier and graded basis in the documented KMRAT001 format.](../inputs/lane3-exact-multiplier.bin).
- [Exact complex, binary, queue, rank, and write-once output conventions.](lane-3-source-packet.md#source-9bf807df6c4005d1).
- [Existing deterministic queue builder to generalize from the beta-two campaign.](lane-3-source-packet.md#source-6fd3e76417213008).

**Complete when.**

- A hash-pinned manifest lists every required differential block with dimensions and aggregation role, and an independent checker proves no admissible weight block is omitted or duplicated.

**Possible starts.**

- Derive block source and target dimensions directly from the exterior basis and multiplier weight metadata rather than treating good-prime output files as the definition of coverage.
- Emit both a task table and an independently recomputed coverage summary by homological degree and weight.

**Freedom.**

- A homology-basis queue may replace adjacent-rank queues if its coverage proof is equally explicit.

**Mathematical limits.**

- Good-prime rank records may estimate resources but cannot define the characteristic-zero coverage set.
- This task constructs and proves the queue; it does not claim any remaining rational rank.

### Certify beta three through beta nine over Q — Blocked

`TSK-L3-RATIONAL-BETTI-3-9-V3` · computation · sustained

**Goal.** Run exact rational rank or homology calculations for every task in the certified coverage manifest and aggregate beta_3 through beta_9.

**Why it matters.** This replaces the remaining good-prime evidence by characteristic-zero certificates with a proved completeness boundary.

**Public inputs.**

- [Exact rational second Betti number](../working-mathematics/units/RMU-3B2E0001.md) (retained unit `RMU-3B2E0001`).
- [Rational Betti certification](../working-mathematics/units/RMU-C76886E8.md) (retained unit `RMU-C76886E8`).
- [Exact GMP rational block-rank engine.](lane-3-source-packet.md#source-ee80ccde287b2cc7).
- [Hash-checking single-block runner.](lane-3-source-packet.md#source-464b94476ce549e0).
- [Bounded CPU-only Slurm array wrapper.](lane-3-source-packet.md#source-204b8229e0ddf8af).

**Task dependencies.**

- `TSK-L3-RATIONAL-BETTI-COVERAGE-V1`

**Blocked on.**

- The complete hash-pinned block queue and independent coverage proof for the seven homological degrees have not yet been constructed.

**Complete when.**

- Every manifest block has an exact rational certificate and the seven Betti numbers are replayably aggregated from the complete queue.

**Possible starts.**

- Schedule independent certified blocks and aggregate only after the manifest checker accounts for every expected output.

**Freedom.**

- Exact homology bases or deterministic nonzero minors may replace full row-echelon outputs.

**Mathematical limits.**

- Do not infer rational ranks from finitely many primes, and do not rerun beta_2 except as a regression test.

### Compare the direct and marked-root deformation complexes — Blocked

`TSK-L3-DIRECT-MARKED-CHAIN-COMPARISON` · proof, computation · sustained

**Goal.** Construct a chain map and homotopy comparison through order six that identifies the direct and marked-root generators in fixed bases.

**Why it matters.** This would connect the exact direct-coordinate ranks and primitive sextic to the root-native deformation complex.

**Public inputs.**

- [Exact fifth-order calculation](../working-mathematics/units/RMU-40375935.md) (retained unit `RMU-40375935`).
- [Known direct-coordinate ranks, recovered scope, and missing comparison data.](lane-3-source-packet.md#source-2210ec80b02f0f23).

**Blocked on.**

- The marked-root contracting homotopy and a basis compatible with the direct complex beyond order four are not publicly available.

**Complete when.**

- Explicit chain maps, inverse up to homotopy, basis correspondence, and order-six generator transport are checked.

**Possible starts.**

- Recover or independently derive a compatible marked-root contraction and basis first.

**Freedom.**

- An intrinsic quasi-isomorphism may replace coordinate matrices if it still identifies the finite certificates.

**Mathematical limits.**

- Known rank agreement and the primitive sextic are not themselves a chain comparison.

### Construct a non-tautological finite-level effectivity invariant — Ready now

`TSK-L3-INTRINSIC-EFFECTIVITY` · proof, exploration · open ended

**Goal.** Define explicit finite-level data recovering the escaping conductor decoration and prove a transport inequality under complexity-bounded unframed stable equivalences.

**Why it matters.** This can sharpen the proved double-logarithmic divergence into a meaningful intrinsic effectivity theorem.

**Public inputs.**

- [Quadratic-frame effectivity staircase and stable non-effectivity](../working-mathematics/units/RMU-3FEF0011.md) (retained unit `RMU-3FEF0011`).
- [Exact framed staircase, stable non-effectivity, and unrestricted lower bound.](lane-3-source-packet.md#source-c413ecb87f258d26).

**Complete when.**

- The invariant is explicit at finite order, is not the equivalence class itself, and comes with a proved transport inequality and quantitative consequence.

**Possible starts.**

- Seek finite-level divisorial, valuation, or orbit data that are Lipschitz under elementary stable operations.
- Compare effective invariant theory with the explicit Artin staircase.

**Freedom.**

- A proof that no invariant of a precisely stated finite-level class can improve the bound is also useful.

**Mathematical limits.**

- Do not promote the framed M-2 law to an unframed result without a new argument.
<!-- RETAINED_TASKS_END -->

## Exact sources

- [Order-five replay and scope](lane-3-source-packet.md#source-cd92beb1f9f8cbbe)
- [Order-five verifier](lane-3-source-packet.md#source-68c9400aba7a75f5)
- [Order-six reconstruction statement and primitive sextic](../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md)
- [Exact rational \(\beta_2\) audit packet](lane-3-source-packet.md#source-8a20e73c5c1d9046)
- [Betti appendix](../proof-sources/03-local-rigidity/appendices/border-basis-and-betti.md)
- [Formal family and theorem](lane-3-source-packet.md#source-c413ecb87f258d26)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Optional runnable source ZIP](../inputs/lane-3-source-files.zip) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
