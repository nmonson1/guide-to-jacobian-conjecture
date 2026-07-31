---
title: "Model research brief — Minimum Degree and Quartic Exclusions"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 2</p>
# Program 2: Minimum Degree and Quartic Exclusions

**Research state:** mathematical checkpoint 29 July 2026, including the
successful generic-triple calculation and the conditional July 29 closures
of high ramification and fixed components. Exact scope, dependencies, and
direct proof-body links are stated per input below.
**Actor guidance:** conceptual classification -> online model; exact
elimination -> local symbolic; nothing here needs a large CAS.

This page is the complete model handoff. A model can work from this URL
alone; the linked [working paper](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf),
[stable claim pages](../../results/all-claims.md), and
[public technical-material index](../../evidence/materials.md) provide deeper
verification when needed. Private conversations and internal replay paths are
deliberately not part of the public handoff.

## 1. Setup and notation

Everything is over an algebraically closed field of characteristic zero.

- The **ordinary degree** of `F = (F_1,F_2,F_3)` is `max_i deg F_i`. This
  is not the generic (fiber) degree. `D_min` denotes the least ordinary
  degree of a three-dimensional Keller counterexample.
- Known interval: `4 <= D_min <= 7` (degree <= 3 is automorphic by
  Vistoli; the base counterexample has coordinate degrees `(7,6,4)`).
- A degree-4 map is written affine-normalized as `F = LX + H_2 + H_3 + H_4`
  with `L in GL_3` and `H_i` homogeneous of degree `i`.
- The **leading target span** is
  `rho_4(F) = dim span{(H_4)_1, (H_4)_2, (H_4)_3}` inside `Sym^4`. The
  projectivized leading map `phi_4: P^2 --> P^2` has image closure
  `C_4(F)`; the Keller condition forces `dim C_4(F) <= 1`, and
  `rho_4 = 1, 2, 3` corresponds (modulo base-locus degeneracies) to point,
  line, and nondegenerate rational-curve image.
- The organizing identity: with `K_eps(X) = eps^4 F(X/eps)`,
  `det JK_eps = eps^9 det JF`. A quartic Keller map is a maximally
  volume-preserving deformation of its singular leading map at infinity;
  every coefficient of the determinant arc below order nine vanishes.
  All exclusion arguments are extractions from these coefficients.
- For binary forms (polynomials in two linear forms `x,y`), `J(f,g)`
  denotes the planar Jacobian. For a leading pair `H_4 = (P,Q,0)` with
  third cubic component `R`, the **common ramification divisor** of the
  pencil is `gcd(J(Q,R), J(P,R), J(P,Q))`; its degree stratifies the
  binary-pencil locus. `P = GA, Q = GB` with `gcd(A,B)=1` names a **fixed
  component** `G`.

The logical order matters. The leading image first determines whether the
top form has target span one, two, or three. Only after the span-two branch
has been reached may one invoke binary-pencil ramification. “Binary” is a
geometric conclusion of the earlier reductions, not a coordinate choice
available at the start. Likewise, a finite symbolic elimination proves only
the chart it actually parametrizes. Every proposed normal form should be
checked against its intended stratum before coefficients are eliminated.

### Coverage rule

This handoff is optimized for research use per token, not
proof-self-contained. Each numbered input gives the reusable statement with
its hypotheses, its dependency exits, and a direct page-level proof link.
The claim link preserves stable identity. The technical archive dated 27
July predates the balanced and tricuspidal exclusions and does **not**
describe the current frontier by itself.

### Compact glossary

- **Target span `rho_4`:** dimension of the coordinate span of the top
  homogeneous layer; it is not the degree of the image curve.
- **Binary pencil:** a two-dimensional linear system in two source linear
  forms, reached only after the leading-image reductions.
- **Ramification divisor:** gcd of the three planar Jacobians of the leading
  pencil and the next component; its degree defines separate strata.
- **Hilbert--Burch type `(e,d)`:** degrees of the two syzygy columns defining
  a codimension-two leading image.
- **`F_4` family:** the exceptional weighted-inflection normal form left by
  the degree-three ramification classification; it is not “all quartics.”

### Case and dependency map

```text
quartic Keller map
├─ rho_4 = 1 ── automorphic
├─ rho_4 = 3
│  ├─ conic image ── excluded (all seven quadratic-factor orbits)
│  └─ proper rational cubic/quartic image ── excluded
└─ rho_4 = 2 ── four-locus reduction
   ├─ genuinely quadratic-source (2,2) ── excluded in 9 charts
   ├─ coprime binary pencil
   │  ├─ ramification degree 0,1,2 ── excluded
   │  ├─ degree 3 ── branch exits + generic (3,4) / exceptional F_4
   │  └─ degree 4 or 5 ── automorphic
   ├─ pencil containing a fourth power ── absorbed into recorded branches
   └─ fixed component ── all factor degrees conditionally closed
```

## 2. Goal and payoff

Decide ordinary degree four: either prove no degree-4 counterexample
exists, or exhibit one.

- Exclusion gives `D_min >= 5` — the first unconditional degree bound
  beyond the classical `<= 3` theorem, and a clean externally citable
  result.
- **This search is two-sided.** A stratum that resists exclusion is a
  candidate construction for a second, mechanism-independent
  counterexample. If a family keeps failing to die, escalate it as a
  construction lead; do not grind.

## 3. Reusable inputs, exact scope, and proof access

| # | Exact input and hypotheses | Claim · direct proof body |
| --- | --- | --- |
| 1 | Let `F=LX+H_2+H_3+H_4: A^3 -> A^3` be Keller over an algebraically closed characteristic-zero field, with arbitrary mixed lower terms. If `rho_4=dim span((H_4)_i)=1`, then `F` is an automorphism. No homogeneity or nilpotency hypothesis is assumed. | [`JCG-99911351`](../../claims/JCG-99911351.md) · [proof, weighted-field reduction through terminal determinant](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=5) |
| 2 | No quartic Keller map in three variables has a nondegenerate conic as its projective leading image. The conclusion uses all seven quadratic-factor orbits: four invariant-field orbits and three separate later orbit arguments; the four-orbit theorem alone is insufficient. | [`JCG-24A6190A`](../../claims/JCG-24A6190A.md), [`JCG-80F5587E`](../../claims/JCG-80F5587E.md), [`JCG-244F8A2E`](../../claims/JCG-244F8A2E.md) · [proof and exact terminal calculation](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=10) |
| 3 | Subject to the span-two normal form, the highest Keller equation routes the leading pair into four possibly overlapping loci: a binary quartic pencil; a quadratic-source locus with `(e,d)=(2,2)`; a composition-primitive coprime pencil containing `ell^4`; or a composition-primitive reduced pencil with nonbinary fixed components on special fibers. | [`JCG-93A2594E`](../../claims/JCG-93A2594E.md) · [proof of the four-locus routing](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=10) |
| 4 | Assuming the preceding leading-curve reduction and the rank-one, conic, rational-cubic, balanced-quartic, and tricuspidal-quartic exclusions, every nonautomorphic quartic Keller map has leading target span exactly two. The assumptions are part of the statement. | [`JCG-90614345`](../../claims/JCG-90614345.md), [`JCG-F13D186D`](../../claims/JCG-F13D186D.md) · [proof of both final rational-quartic strata and synthesis](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=16) |
| 5 | In the quadratic-source `(e,d)=(2,2)` branch, the genuinely nonbinary **no-fixed-component** locus is impossible in all nine normalized charts. Fixed-component chart boundaries exit to item 7 or the fixed-component results in items 13–17. | [`JCG-B2D60A95`](../../claims/JCG-B2D60A95.md) · [proof with all nine charts](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=18) |
| 6 | Assume the Program 2 structural reductions and a coprime binary pencil `H_4=(P,Q,0)`. If `Delta=gcd(J(Q,R),J(P,R),J(P,Q))` has degree at most two, then `F` is an automorphism. Regular, simple-root, double-root, and squarefree-double branches are separate mechanisms. | [`JCG-1AE58E51`](../../claims/JCG-1AE58E51.md), [`JCG-176D3DFE`](../../claims/JCG-176D3DFE.md), [`JCG-059D835C`](../../claims/JCG-059D835C.md) · [proof through double ramification](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=18) |
| 7 | In the special chart `H_4=(0,0,x^2y^2)` with cubic pencil `<x^2y,xy^2>`, the Keller equations force the third column of `L` to vanish. This is one rank-one/fixed-component boundary calculation, **not** a target-span-two classification. | [`JCG-34460CE2`](../../claims/JCG-34460CE2.md) · [complete Plücker-chart proof](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=17) |
| 8 | Subject to items 1–4, the degree-three ramification branch splits by Hilbert–Burch type `(2,5)` or `(3,4)` and exits to automorphic, cube, fourth-power, fixed-component, or source-shear cases, except for the explicit `F_4` weighted-inflection family. This is a routing result, not a triple-ramification exclusion. | [`JCG-9D9C3DF9`](../../claims/JCG-9D9C3DF9.md) · [routing calculation and exact exceptional queue](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=20) |
| 9 | On the reconstructed generic `(3,4)` open chart, after inverting the displayed denominator, rank-minor, resonance, and weighted-inflection factors, the `6 x 8` next-layer matrix has rank six and the two displayed kernel vectors span its kernel; over the algebraic closure their plane meets the quadratic Veronese only at the origin. Nothing is asserted on the inverted divisors. | [`JCG-9D9C3DF9`](../../claims/JCG-9D9C3DF9.md) · [exact generic calculation and nonvanishing factors](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=20) |
| 10 | Subject to items 3–6 and membership in the primitive coprime binary-pencil locus, common ramification degree `r=4` or `r=5` forces an automorphism. The `r=4` proof covers dependent residuals, the square and reduced residual quadratics, the complete repeated-root incidence, the omitted projective point, and the `2+2` kernel. | [`JCG-5C216C29`](../../claims/JCG-5C216C29.md) · [theorem and proof](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=21) |
| 11 | Subject to the primitive span-two reduction, a fourth-power pencil member adds no leaf: its highest nonzero normal layer routes to an aligned, binary, or quadratic-source branch. | [`JCG-5EF7883D`](../../claims/JCG-5EF7883D.md) · [proposition and proof](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=22) |
| 12 | In the binary branch, if one of `U=J(Q,R)`, `V=J(P,R)`, or `W=J(P,Q)` vanishes—including the separate `R=0` case—the map is automorphic. Apply the ordinary ramification-degree filtration only after removing these boundaries. | [`JCG-5E7E9377`](../../claims/JCG-5E7E9377.md) · [proposition and proof](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=22) |
| 13 | In the primitive fixed-component branch `P=GA,Q=GB`, if `Gamma` has multiplicity `s` in `G` and `m` in the reduced fiber over `xi`, then `4 nu_Gamma(R)=3s+c_xi m` and `sum c_xi=3`, with the adjusted infinity convention. The `c_xi` can be negative. This supersedes the formula without `3s` and every proof assuming all `c_xi>=0`. | [`JCG-39A7571B`](../../claims/JCG-39A7571B.md) · [corrected lemma and proof](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=23) |
| 14 | Subject to the four-loci reduction and the standard two-variable polynomial-centralizer theorem, every genuinely nonbinary primitive fixed-component branch is closed. | [`JCG-48D499D2`](../../claims/JCG-48D499D2.md) · [valuation and residual-pole proof](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=23) |
| 15 | Subject to the binary fixed-component reduction, every cubic fixed factor is automorphic or undergoes a triangular degree drop; squarefree, double-plus-simple, and triple-line multiplicities are covered. | [`JCG-DAFBEDD5`](../../claims/JCG-DAFBEDD5.md) · [computer-assisted theorem](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=24) |
| 16 | Subject to the binary fixed-component reduction, every linear fixed factor is automorphic. After `H_4=(x^4,xB,0)`, both residual-cubic orbits and every exceptional divisor are covered. | [`JCG-4077AC78`](../../claims/JCG-4077AC78.md) · [computer-assisted theorem](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=24) |
| 17 | Subject to the binary fixed-component reduction, every quadratic fixed factor with coprime residual quadrics is automorphic. Normalize `P=x^2G,Q=y^2G`; the discriminant, two axis-tangencies, resultant, all intersections, and projective endpoints are covered by 38 exact replay groups. | [`JCG-3C448C71`](../../claims/JCG-3C448C71.md) · [determinant and exceptional sweep](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=24) |
| 18 | In dimension three, for every ordinary degree `d`, a Keller map cannot have a **period-primitive** leading line. “Period-primitive” is distinct from composition-primitive and coprime. | [stable register statement and derivation](../../assets/manuscripts/07-results-and-research-register-2026-07-29-v13.pdf#page=9) |

Standing hypotheses to keep visible: items 4–17 are conditional on the
manuscript's leading-curve and structural reductions. Item 9 also requires
membership in its reconstructed open chart and every listed nonvanishing
factor. Successful exact replays do not prove the global routing. That case
tree is task T2 below.

### Proof-signature index

| Input | Proof signature / reusable output | Boundary exits |
| --- | --- | --- |
| 1, rank one | A weighted Lüroth argument puts the coordinate field in one variable; degree factorization and valuations reduce the top layer to cube/binary cases; two determinant syzygies force a triangular plane Keller map. **Output:** a weighted one-variable field and two binary determinant identities. | Uses `rho_4=1`; it is not a coordinate lemma for arbitrary submersions. |
| 2, conic | For four historical factor orbits, the characteristic derivation has invariant field `C(x/y,Gy^2)`; invariant-degree gaps kill the first normal defects and five exact terminal charts force `det L=0`. The remaining three orbits use separate later certificate/automorphism arguments. **Output:** complete seven-orbit conic exclusion. | Do not extend the four-orbit invariant-field proof to the other three; cite the full three-claim package. |
| 3, four loci | Factor the rational map degrees as `n=ed`, enumerate the composite-degree table, and apply the corrected primitive valuation identity `4 nu_Gamma(R)=3s+c_xi m` with `sum c_xi=3`. **Output:** a structural routing into four span-two loci. | Exhaustiveness still depends on recording every overlap and special fiber in T2. |
| 4, rational curves | Use tangent syzygies and Hilbert--Burch classification, then projective duality. Explicit tricuspidal and balanced normal forms make the first terminal coefficients force binary normal layers and finally `L_z=0`; the target-span synthesis also invokes the rational-cubic exclusion. **Output:** span-three proper rational images are closed. | Only after the leading-curve classification; it does not close span-two ramification. |
| 5, quadratic source | On the no-fixed-component `(2,2)` locus, normalize source and target data in nine charts; in each, the determinant arc makes the Hilbert--Burch columns proportional. **Output:** a chart-complete exclusion of the genuinely nonbinary quadratic-source leaf. | Fixed components and chart-boundary overlaps leave through their own branches. |
| 6, ramification at most two | Regular branch: Hilbert--Burch degrees kill every `z` term. Simple branch: a weighted inflection plus anchor coefficients closes the chart. Double branch: the two Hilbert--Burch types reduce to a terminal coefficient `-1/3`. **Output:** three separately proved low-ramification exclusions. | No statement for ramification degree at least three. |
| 7, Plücker special case | The Plücker relations force the third column of the relevant linear matrix `L` to vanish, collapsing the intended chart to rank one. **Output:** a fixed-component/rank-one boundary certificate. | This is not the full target-span-two locus. |
| 8, triple ramification | Hilbert--Burch classification splits into cube, fourth-power, fixed-component, and source-shear exits; the remaining generic `(3,4)` branch enters the explicit `F_4` weighted-inflection family. **Output:** a finite branch list and normal forms. | Exceptional divisors and `F_4` compatibility remain; “triple ramification closed” would be false. |
| 9, generic `(3,4)` chart | Reconstruct the gradient factorization over `Q(a,b,tau)`, form the six-by-eight next-layer matrix, certify rank six and two kernel vectors, then factor the denominator and rank minor. **Output:** the generic kernel plus the exact exceptional-divisor queue. | Every vanishing factor requires a fresh chart; rational formulas may not be specialized across their poles. |
| 10–12, high ramification and edges | The universal minor syzygy treats `r=5` and dependent `r=4`; the reduced residual quadratic uses a determinant arc plus a complete projective repeated-root audit. Polynomial common generators absorb fourth powers, and Euler/UFD plus a separate determinant arc closes zero minors. | Conditional on entering the primitive coprime binary branch; exact scripts do not certify upstream routing. |
| 13–14, nonbinary fixed components | The signed valuation with its `3s` term eliminates degree-two fibers and reduces degree one to aligned, binary, or residual-pole form. Two normal equations reassemble the residual-pole map and force a zero Jacobian. | Uses the four-loci reduction and a conventional polynomial-centralizer theorem. |
| 15–17, binary fixed factors | Split by factor degree and multiplicity. Generic first-normal determinants expose finite exceptional divisors; exact chart sweeps kill their amplitudes or reduce to plane automorphisms. The quadratic case has four divisors and 38 replay groups. | Programs certify encoded identities and chart ideals, not proof-to-code correspondence or global exhaustiveness. |

## 4. The live frontier

**(F1) The exceptional degree-three `F_4` endgame** *(unblocks item 8 into a
uniform theorem).* The generic calculation is no longer the missing step.
Over `Q(a,b,tau)` it reconstructs the Hilbert--Burch gradient factorization,
checks the quadratic-normal-form and determinantal identities, builds the
six-by-eight next-layer matrix, proves generic rank six, and verifies the two
displayed kernel vectors. The nonzero rank minor exposes all factors that
the generic argument inverted. Those factors are the next case list, not
noise to be discarded.

On the weighted-inflection family, with quartic

```
Q = q0*x^4 + q2*x^2*y^2 + q3*x*y^3 + q4*y^4     (reduced case: q3 = 0)
```

the remaining problem is: solve the `D_6 = 0` system over
`Q(tau)[d]/(q4(d,tau))` and show, uniformly over that extension and every
exceptional parameter, that lower binary terms cannot cancel the pure
`D_5` obstruction.

**The complete formulas for `q4(d,tau)`, the remaining `D_6` compatibility
system, and the pure `D_5` obstruction were never recovered.** The July 28
verifier does not manufacture those missing formulas: it closes the open
generic next-layer chart and identifies the divisors where separate charts
are required. The endgame data are not present in the available mathematical
artifacts. They must be re-derived, not searched for. Recipe: start from the
generic `(3,4)` Hilbert–Burch branch normal form in the continuation appendix;
specialize successively to each denominator/rank-minor/resultant factor
displayed by `generic-triple-ramification.json`; then recompute the
determinant arc rather than specializing a rational formula across a pole.
The obstructions are coefficients at orders six and five under the
weighted-inflection normalization.
Consistency anchors that *are* recorded and must be reproduced:

```
[x*y^4*z] D_6 = [y^5*z] D_6 = 104/3,        [y^3*z^2] D_5 = -1/3 .
```

**(F2) Global routing and exhaustiveness audit.** The chain in items 1–17
was built incrementally. The manuscript now records closures of
ramification degrees four and five, the fourth-power and zero-minor edges,
and every primitive fixed-factor degree. What is still missing is one
referee-facing case tree from `rho_4 in {1,2,3}` to every leaf, with all
overlaps, nonprimitive exits, and conventional dependencies checked.

The dependency picture is therefore short: the case-tree audit must certify
that the span-two reduction really reaches the stated
pencil/fixed-component leaves; all of those leaves are conditionally closed
except the explicit `F_4` weighted-inflection system. Exact programs verify
the identities and chart ideals they encode, but do not themselves prove
proof-to-code correspondence or global exhaustiveness. Do not describe
“triple ramification” as closed until the `F_4` system is solved.
Conversely, do not reopen ramification degrees four and five or any
fixed-factor degree: those calculations are complete within their stated
reductions.

## 5. Graveyard (causes of death — read before proposing routes)

- **Plücker target-span-two calculation (superseded).** The computed chart
  did not parametrize the span-two locus it was believed to cover; on
  inspection its normal form re-imposed rank-one leading structure, so the
  computation survives only as a fixed-component elimination inside the
  rank-one route. *Lesson: before any elimination, verify the normal form
  actually parametrizes the intended stratum — write down the stratum
  membership check first.*
- **Known-false general principles** (corrected in the ledger; they will
  tempt you when reasoning about candidate boundary geometry): the
  nonproperness set need not equal branch support; not every nonproperness
  component carries a transposition; the omitted locus need not be only the
  triple-root curve.
- **Submersion-to-coordinate beyond its hypotheses.** `x + x^2*y` is a
  critical-point-free non-coordinate; the degree-7 counterexample's own
  transverse component `x(2 - 3xy - x^2 z)` is a smooth submersion that is
  not a coordinate. The coordinate lemmas are a low-degree phenomenon
  (degree <= 2, and degree 3 with cube-containing top part); do not attempt
  to extend them.
- **Finite-field searches are exploratory only.** They live in a separate
  subdirectory precisely because they are not characteristic-zero
  nonexistence proofs.
- **Generic rank is not an exceptional-stratum theorem.** The July 28
  certificate proves rank six over a rational function field and exhibits a
  nonzero minor. It intentionally leaves the vanishing factors of that minor
  and the denominator divisors for separate charts. Clearing denominators
  and declaring the same conclusion on those factors would repeat the error
  that this program's chart discipline is designed to prevent.

## 6. Tasks

Each item is a task capsule. Its inputs, stop condition, and done-when clause
are part of the contract. Stop immediately if an exact chart retains a
positive-dimensional Keller locus: return its defining equations and promote
it to the construction branch instead of assuming the exclusion must win.

**P2-T1 — Re-derive and solve the exceptional `F_4` compatibility system.**
Actor: `local_symbolic`. Status: ready. The missing input is explicitly a
re-derivation task, not an absent promised bundle.
*Payoff:* converts item 8 into a theorem; with T2 it closes degree 4.
*Attack:* use the v2 generic certificate to enumerate the denominator,
rank-minor, resonance, and weighted-inflection divisors; recompute the
`(3,4)` branch normal form on each chart; derive `q4, D_6, D_5`; check the
three anchor coefficients; solve in the extension; sweep exceptional
parameters without division by a parameter that may vanish.
*Done when:* one compact exact verifier, or a manifest-linked finite family
of chart verifiers, covers the uniform solve and every exceptional branch in
the style of `verify_conic_certificates.py`, and the manuscript states which
geometric classification lemmas remain conventional dependencies.

**P2-T2 — Write the case tree and audit exhaustiveness.**
Actor: `online_model`. Status: ready.
*Payoff:* determines whether T1 is genuinely the only mathematical leaf and
removes the standing “conditional on the structural reductions” qualifier.
*Attack:* start at each `rho_4` value; route span three through all leading
curve types and span two through the four-loci reduction; list every
ramification degree, zero minor, fourth-power member, fixed-factor degree,
multiplicity type, and nonprimitive overlap. Treat items 1–17 as inputs, not
as results to re-prove.
*Done when:* a single document routes every `rho_4` value to a leaf, each
leaf carrying a theorem locator or an open-task pointer, with no gaps.

**P2-T3 — Audit proof packets against the mathematical statements.**
Actor: `local_audit`. Status: ready.
*Payoff:* distinguishes successful algebra replays from a verified
proof-to-code correspondence.
*Attack:* for each computer-assisted theorem in items 9–17, match every
normalization, localization, ideal generator, exceptional divisor, and
terminal condition in the paper to the exact program; then check the
program's manifest and rerun it from a clean copy.
*Done when:* a matrix names every theorem subcase, source program, input
domain, excluded divisor, replay command, observed result, and any gap.

**Escalation rule.** If T1 or T2 exposes a positive-dimensional stratum that
continues to satisfy all tested Keller layers, stop treating it as merely a
failed exclusion. Record its standing hypotheses and promote it to a
candidate-construction task. A second counterexample with a mechanism
independent of the degree-seven marked-root example would be at least as
valuable as the bound `D_min >= 5`.

## 7. Evidence and replay index

The [Program 2 working paper](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf)
contains the conventional arguments and exact theorem locators. The
[public technical-material index](../../evidence/materials.md#2-minimum-degree-and-quartic-exclusions)
provides the hash-pinned complete computational supplement and focused
Plücker-boundary calculation. The principal calculation groups are:

The complete supplement at that link is versioned historical evidence. Its
old limitation sentence that balanced and tricuspidal cases “remain open”
describes the archive at creation time, not the current handoff; those later
exclusions are in item 4 and the version-pinned working paper.

- rational-quartic frontier exclusion, with a second pure-Python
  implementation;
- fixed-component Plücker elimination, with the restricted scope recorded in
  the graveyard above;
- target-span-two progress, including nine quadratic-source charts;
- weighted-inflection reduction, covering only the first obstruction;
- binary ramification of degrees zero, one, and two; and
- the July 28 generic triple-ramification calculation.

The July 29 evidence adds exact replays for ramification degrees four and
five, fourth-power and zero-minor edges, the corrected fixed-component
valuation, and fixed factors of degrees three, one, and two. All standalone
verifiers and all 38 quadratic replay groups pass from a clean copy. The
quadratic packet's source archive has SHA-256
`9448ae88a3b00f8e6013085ce6fe42ffe84e51c1a6a4fb3fe761f6de2a75090f`;
its internal manifest contains 156 files and verifies without mismatch.
These replays establish the encoded identities and chart calculations, not
the upstream routing or an independent review of the proofs.

The July 28 exact result records coefficient domain `Q(a,b,tau)`, a
six-by-eight equation matrix, generic rank six, two kernel directions, the
denominator and nonzero rank minor, the resultant gcd, and the exceptional
divisors. Its independent execution reports successful verification and
generic rank six. A prior runner failure occurred before the mathematics was
imported and supplies no evidence; it is intentionally omitted from this
public research handoff.

The conventional argument/check boundary is deliberate. The scripts verify
displayed identities, finite chart eliminations, matrix ranks, kernels, and
factorizations. They do not independently prove the leading-curve
classification, the conic-pencil valuation lemma, the Hilbert--Burch case
classification, or the claim that the listed charts exhaust the geometric
stratum. Those dependencies belong in the case-tree audit rather than being
hidden behind the successful replay label.

## 8. Do not do

- Do not re-prove items 1–18; use their exact scope and direct locators.
- Do not treat finite-field samples as characteristic-zero proofs.
- Do not open degrees 5 and 6 until degree 4 is decided (partial degree-5/6
  fixed-factor results exist; they are out of scope here).
- Do not describe the conic theorem as a four-orbit result. Four orbits use
  the original invariant-field mechanism; three are closed by separate later
  arguments. Cite all three conic claim tags in item 2.
- Do not cite the generic rank-six certificate as a uniform solution on its
  rank-minor or denominator divisors.
- Do not claim `D_min >= 5`: the current unconditional public interval is
  still `4 <= D_min <= 7`.
- Do not trust a normal form by its intended label. Verify directly that its
  leading target span, fixed component, and ramification divisor place it in
  the claimed stratum before running elimination.

[Back to the Program 2 overview](../programs/minimum-degree-and-quartic-exclusions.md)
