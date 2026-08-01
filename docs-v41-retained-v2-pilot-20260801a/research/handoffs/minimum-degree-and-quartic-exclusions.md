---
title: "Model research brief — Minimum Degree and Quartic Exclusions"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 2</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 1 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v14 · site release <code>living-guide-public-v41-retained-v2-pilot</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/programs/minimum-degree-and-quartic-exclusions.md).

!!! tip "Current text proofs — preferred"
    Use the [current TeX source and exact label anchors](../proof-sources/02-low-degree/main.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Program 2: Minimum Degree and Quartic Exclusions

**Research state:** mathematical checkpoint 30 July 2026. Every previously
listed degree-three normal-form calculation now has an exact successful
replay. A fresh paper audit and scoped degree-five/six packet sharpen the
boundaries below. The global case-tree remains open and the quartic synthesis
is still conditional.
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
  component** `G`. For a span-two pair, write
  `H = deg gcd(grad(P) cross grad(Q))`.

The logical order matters. The leading image first determines whether the
top form has target span one, two, or three. Only after the span-two branch
has been reached may one invoke binary-pencil ramification. “Binary” is a
geometric conclusion of the earlier reductions, not a coordinate choice
available at the start. Likewise, a finite symbolic elimination proves only
the chart it actually parametrizes. Every proposed normal form should be
checked against its intended stratum before coefficients are eliminated.

### Coverage rule

Use numbered inputs with their hypotheses; programs prove only their
displayed charts.

### Compact glossary

`rho_4` is target span; `F_4` names one exceptional family.

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
   │  ├─ degree 3 ── all supplied generic/resonant/degenerate charts replay;
   │  │              global placement + independent reproduction open
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
| 2 | The claim graph packages a nondegenerate-conic exclusion using all seven quadratic-factor orbits: four invariant-field orbits and three separate later arguments. The 30 July paper audit found direct support for the four original orbits but not complete proof access for the other three, so retain the full claim package while treating the seven-orbit synthesis as a proof-access gap. | [`JCG-24A6190A`](../../claims/JCG-24A6190A.md), [`JCG-80F5587E`](../../claims/JCG-80F5587E.md), [`JCG-244F8A2E`](../../claims/JCG-244F8A2E.md) · [four-orbit proof and exact terminal calculation](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=10) |
| 3 | Subject to the span-two normal form, the highest Keller equation routes the leading pair into four possibly overlapping loci: a binary quartic pencil; a quadratic-source locus with `(e,d)=(2,2)`; a composition-primitive coprime pencil containing `ell^4`; or a composition-primitive reduced pencil with nonbinary fixed components on special fibers. | [`JCG-93A2594E`](../../claims/JCG-93A2594E.md) · [proof of the four-locus routing](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=10) |
| 4 | Assuming the preceding leading-curve reduction and the rank-one, conic, rational-cubic, balanced-quartic, and tricuspidal-quartic exclusions, every nonautomorphic quartic Keller map has leading target span exactly two. The assumptions are part of the statement. | [`JCG-90614345`](../../claims/JCG-90614345.md), [`JCG-F13D186D`](../../claims/JCG-F13D186D.md) · [proof of both final rational-quartic strata and synthesis](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=16) |
| 5 | In the quadratic-source `(e,d)=(2,2)` branch, the genuinely nonbinary **no-fixed-component** locus is impossible in all nine normalized charts. Fixed-component chart boundaries exit to item 7 or the fixed-component results in items 13–17. | [`JCG-B2D60A95`](../../claims/JCG-B2D60A95.md) · [proof with all nine charts](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=18) |
| 6 | Assume the Program 2 structural reductions and a coprime binary pencil `H_4=(P,Q,0)`. If `Delta=gcd(J(Q,R),J(P,R),J(P,Q))` has degree at most two, then `F` is an automorphism. Regular, simple-root, double-root, and squarefree-double branches are separate mechanisms. | [`JCG-1AE58E51`](../../claims/JCG-1AE58E51.md), [`JCG-176D3DFE`](../../claims/JCG-176D3DFE.md), [`JCG-059D835C`](../../claims/JCG-059D835C.md) · [proof through double ramification](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=18) |
| 7 | In the special chart `H_4=(0,0,x^2y^2)` with cubic pencil `<x^2y,xy^2>`, the Keller equations force the third column of `L` to vanish. This is one rank-one/fixed-component boundary calculation, **not** a target-span-two classification. | [`JCG-34460CE2`](../../claims/JCG-34460CE2.md) · [complete Plücker-chart proof](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=17) |
| 8 | Within the supplied degree-three Hilbert--Burch normal-form system, exact calculations now derive the generic `F_3/F_4` exits and close their nonresonant, `tau=-1`, `tau=0`, `tau^2+1=0`, `c=0`, dependent-syzygy, quadratic-exceptional, and zero-normal charts. This closes the previously listed encoded calculation gates; it does not independently prove that the upstream global quartic case tree reaches and exhausts precisely these charts. | [`JCG-9D9C3DF9`](../../claims/JCG-9D9C3DF9.md) · [paper routing and exceptional queue](../../assets/manuscripts/02-quartic-keller-maps-2026-07-29-v13.pdf#page=20) |
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
| 19 | **Conditional synthesis only:** if the upstream leading-curve, target-span, four-loci, ramification, and fixed-component routing used in items 1–17 is correct and exhaustive, the replayed terminal leaves imply that every quartic Keller map is automorphic and hence `D_min >= 5`. | The v5 terminal-leaf synthesis uses the linked paper inputs and the complete degree-three replay family; no unconditional claim page is asserted. |

Standing hypotheses to keep visible: items 4–17 are conditional on the
manuscript's leading-curve and structural reductions. Item 9 also requires
membership in its reconstructed open chart and every listed nonvanishing
factor. Successful exact replays do not prove the global routing. Item 19
packages that exact conditional boundary and is not an unconditional theorem.
The current unconditional public interval remains `4 <= D_min <= 7`.

**Paper-audit checkpoint.** The rank-one proof and verifier survive, as do
the four conic certificates and the recovered tricuspidal, syzygy, and count
checks. Corollary A.2's exact target-span-two conclusion is not established
by the active paper because three conic orbits and the rational-cubic
exclusion lack complete proof access. B.4 is incomplete; C.2, C.3, and D.2
are not publication-grade. These are audit findings, not withdrawals of
later chart calculations.

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
| 8, degree-three ramification | The controlling exact bundle reconstructs the generic branch elimination and separately closes the nonresonant `F_3/F_4`, `tau=0,-1`, `tau^2+1`, `c=0`, dependent-syzygy, quadratic-exceptional, and zero-normal charts. **Output:** one replayed terminal family for every named degree-three chart. | Five helpers are reconstructed; all programs are one SymPy lineage; global case placement and proof-to-code correspondence remain open. |
| 9, generic `(3,4)` chart | Reconstruct the gradient factorization over `Q(a,b,tau)`, form the six-by-eight next-layer matrix, certify rank six and two kernel vectors, then factor the denominator and rank minor. **Output:** the generic kernel plus the exact exceptional-divisor queue. | Every vanishing factor requires a fresh chart; rational formulas may not be specialized across their poles. |
| 10–12, high ramification and edges | The universal minor syzygy treats `r=5` and dependent `r=4`; the reduced residual quadratic uses a determinant arc plus a complete projective repeated-root audit. Polynomial common generators absorb fourth powers, and Euler/UFD plus a separate determinant arc closes zero minors. | Conditional on entering the primitive coprime binary branch; exact scripts do not certify upstream routing. |
| 13–14, nonbinary fixed components | The signed valuation with its `3s` term eliminates degree-two fibers and reduces degree one to aligned, binary, or residual-pole form. Two normal equations reassemble the residual-pole map and force a zero Jacobian. | Uses the four-loci reduction and a conventional polynomial-centralizer theorem. |
| 15–17, binary fixed factors | Split by factor degree and multiplicity. Generic first-normal determinants expose finite exceptional divisors; exact chart sweeps kill their amplitudes or reduce to plane automorphisms. The quadratic case has four divisors and 38 replay groups. | Programs certify encoded identities and chart ideals, not proof-to-code correspondence or global exhaustiveness. |

## 4. The live frontier

**(F1) Global case-tree and proof-to-code audit.** Evidence checkpoint:
**30 July 2026**. The v5 quartic-binary endgame materially changes the
frontier: every previously listed degree-three calculation gate has an
explicit program and successful exact replay. The bundle reconstructs the
generic branch elimination and separately treats `tau=-1`, `tau=0`,
`tau^2+1=0`, `c=0`, dependent syzygies, the quadratic exceptional case,
and the zero-normal boundary. Every stored deterministic output agrees with
the fresh replay.

What remains is not another missing CAS chart. The chain 1–17 was built
incrementally across several conversations. Write the single case tree from
`rho_4 in {1,2,3}` through the four-loci split to every terminal chart.
For each edge, verify the exact hypotheses in the cited proof; for each
computer-assisted leaf, map every proof chart to a program group and record
any proof-only or code-only chart.

The v5 high-ramification checker is a useful second structural
implementation, but it explicitly imports the complete-specialization claim
[`JCG-5C216C29`](../../claims/JCG-5C216C29.md). Its exact replay checks the
algebra downstream of that claim, not the claim's proof. Likewise, five
degree-three helper modules are explicitly reconstructed and all programs
remain one SymPy lineage.

**(F2) Independent reproduction and proof review.** Reimplement the
degree-three branch discovery and at least one representative from every
exceptional chart without importing the reconstructed helpers. Then compare
the programs line by line with the conventional Hilbert--Burch and
determinant-arc arguments. A clean second lineage would change the status
from “encoded calculation closed” to “independently reproduced”; it still
would not replace the global case-tree audit in F1.

**Working audit lens — companion/Jordan budget (not a promoted theorem).**
For `M(t)=A_0+...+A_s t^s`, `s=D-1`, the supplied companion construction
gives a generically regular nilpotent of length `N=3s` on
`E=direct_sum_{j=0}^{s-1} O(-j)^3`. If `d_i` are its saturated kernel-flag
link-divisor degrees and `kappa_R,kappa_L` the endpoint defects, the proposed
exact moments are

```
sum d_i = 2s-kappa_R-kappa_L,
sum (N-i)d_i = 3s(s-kappa_R),
sum i d_i = 3s(s-kappa_L).
```

In the quartic span-two setup these imply `H >= 4`; the v4 calculations route
or exclude several displayed profiles. This is a presentation-sensitive
consistency check, not an arbitrary-left-right invariant or proof of
`D_min >= 5`.

**Computation checkpoints.** The earlier exploratory packet remains
chart-local and not wholly passing: its `tau=0` expected resultant is off by
`16/(b0^2 c0^2)`, and it asserts 28 nonzero maximal minors where exact counts
are 19 generically and on `tau=0`, and 14 on the minimal-syzygy chart. A
newer structural packet has eight self-contained successful replays. It
routes a primitive coprime quintic line image to binary or aligned
`(L^5,L^4)`, excludes the squarefree binary-cubic conic branch, and leaves an
aligned nonbinary specialization open. Under
`ker Jac(A,B,-)=k[A,B]`, it excludes primitive sextic conic and weighted
`(2,3)` cores. This is not a global degree-five/six exclusion. Separately,
every listed `delta(Q)<=9` certificate passes and gives
`trdeg A_{<=6}<=2`; the residual full-orbit frontier is unramified
`delta(Q)>=10` plus a conceptual filtered-conormal, Wronskian, or conductor
theorem.

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

**P2-T1 — Write the global case tree and audit exhaustiveness.**
Actor: `online_model`. Status: ready.
*Payoff:* removes the standing “conditional on the structural reductions”
qualifier from items 4–19.
*Attack:* start at each `rho_4` value; route span three through every leading
curve type and span two through the four-loci reduction; list every
ramification degree, zero minor, fourth-power member, fixed-factor degree,
multiplicity type, and nonprimitive overlap.
*Done when:* a single document routes every `rho_4` value to a leaf, each
leaf carrying exact hypotheses and a theorem/program locator or open-task
pointer, with every overlap owned.

**P2-T2 — Independently reproduce the v5 degree-three endgame.**
Actor: `online_model` for the derivation plus `independent_cas` for a second
implementation. Status: ready.
*Payoff:* tests the reconstructed helper modules and distinguishes a genuine
classification from a self-consistent program family.
*Attack:* derive the kernel-plane/Veronese branch equations from the
Hilbert--Burch input without reading the helper implementations; cover the
generic, `tau=-1`, `tau=0`, `tau^2+1`, `c=0`, dependent-syzygy,
quadratic-exceptional, and zero-normal charts; then compare outputs and chart
ownership with v5.
*Done when:* a second lineage reproduces every terminal obstruction and
documents every disagreement or imported hypothesis.

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
provides the hash-pinned public computational supplement and focused
Plücker-boundary calculation.

The July 29 evidence adds exact replays for ramification degrees four and
five, fourth-power and zero-minor edges, the corrected fixed-component
valuation, and fixed factors of degrees three, one, and two. All standalone
verifiers and all 38 quadratic replay groups pass from a clean copy. The
quadratic packet's source archive has SHA-256
`9448ae88a3b00f8e6013085ce6fe42ffe84e51c1a6a4fb3fe761f6de2a75090f`;
its internal manifest contains 156 files and verifies without mismatch.
These replays establish the encoded identities and chart calculations, not
the upstream routing or proof arguments outside the encoded algebra.

The controlling v5 supplement supersedes that calculation queue. Its internal
manifest passes, every script succeeds under SymPy 1.14.0, and all seven
stored deterministic outputs match the fresh replay byte-for-byte. It
supplies the missing generic branch-elimination, resonant, `c=0`,
dependent-syzygy, quadratic-exceptional, and zero-normal calculations. Five
helpers are explicit reconstructions, the programs form one symbolic
lineage, and the high-ramification checker imports
[`JCG-5C216C29`](../../claims/JCG-5C216C29.md); retain those qualifications.

The conventional argument/check boundary is deliberate. The scripts verify
displayed identities, finite chart eliminations, matrix ranks, kernels, and
factorizations. They do not independently prove the leading-curve
classification, the conic-pencil valuation lemma, the Hilbert--Burch case
classification, or the claim that the listed charts exhaust the geometric
stratum. Those dependencies belong in the case-tree audit rather than being
hidden behind the successful replay label.

## 8. Do not do

- Do not re-prove items 1–18; use their exact scope and direct locators
  unless the assignment is explicitly independent reproduction.
- Do not treat finite-field samples as characteristic-zero proofs.
- Do not promote the imported degree-five/six charts into classifications or
  use them to bypass the degree-four routing audit.
- Do not describe the conic theorem as a four-orbit result. Four orbits use
  the original invariant-field mechanism; three are closed by separate later
  arguments. Cite all three conic claim tags in item 2.
- Do not cite the generic rank-six certificate as a uniform solution on its
  rank-minor or denominator divisors.
- Do not ask a model to close an individual resonant or `c=0` chart as
  though no implementation exists. The useful work is independent
  reproduction or global case-tree/proof-to-code audit.
- Do not claim `D_min >= 5`: the current unconditional public interval is
  still `4 <= D_min <= 7`.
- Do not promote pre-v4 Jordan-budget prose, infer global exhaustiveness from
  its ten checks, or use it as a left-right orbit invariant.
- Do not trust a normal form by its intended label. Verify directly that its
  leading target span, fixed component, and ramification divisor place it in
  the claimed stratum before running elimination.

[Back to the Program 2 overview](../programs/minimum-degree-and-quartic-exclusions.md)
