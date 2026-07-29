---
title: "Model research brief — Minimum Degree and Quartic Exclusions"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 2</p>
# Program 2: Minimum Degree and Quartic Exclusions

**Research state:** content checkpoint 29 July 2026, including the successful
July 28 generic-triple calculation. Verification and review status is stated
per input below.
**Actor guidance:** conceptual classification -> online model; exact
elimination -> local symbolic; nothing here needs a large CAS.

This page is the complete model handoff. A model can work from this URL
alone; the linked [working paper](../../assets/manuscripts/02-quartic-keller-maps-2026-07-22-v11.pdf),
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

This handoff is complete enough to assign a quartic leaf without a private
bundle. “Accepted as project input” means reuse the cited result at its exact
scope; it is not a claim of external review. None of the Program 2 inputs
below has independent review recorded. The technical archive dated 27 July
is a historical computation package: it predates the later balanced and
tricuspidal exclusions and therefore does **not** describe the current
mathematical frontier by itself.

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
   │  └─ degree 4 or 5 ── open
   ├─ pencil containing a fourth power ── routed into the same branch audit
   └─ fixed component / nonprimitive overlap ── partly closed, partly open
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

## 3. What is proved and accepted as project input

All rows are project inputs at their stated scope. The four-locus and
Plücker records are `recorded`; the later conic subcase certificate is
`certificate offered`; the other exclusions are `proof offered`. None has
independent review recorded.

| # | Statement | Where |
| --- | --- | --- |
| 1 | `rho_4 = 1` implies automorphism (arbitrary mixed lower terms; no homogeneity or nilpotency hypothesis) | [`JCG-99911351`](../../claims/JCG-99911351.md); paper Thm `thm:rank-one`, §5 |
| 2 | No quartic Keller map in three variables has a nondegenerate conic as projective leading image. The proof package separates four historical quadratic-factor orbits from three later orbit-specific arguments; it is not only the older four-orbit theorem. | [`JCG-24A6190A`](../../claims/JCG-24A6190A.md), [`JCG-80F5587E`](../../claims/JCG-80F5587E.md), [`JCG-244F8A2E`](../../claims/JCG-244F8A2E.md); paper §6 plus supplemental conic records |
| 3 | Span-two structural reduction to four loci: binary quartic pencil / quadratic-source `(e,d)=(2,2)` / pencil containing `ell^4` / fixed components on special fibers | [`JCG-93A2594E`](../../claims/JCG-93A2594E.md); paper Prop `prop:four-loci`, §5 |
| 4 | Proper rational-quartic leading images (tricuspidal and balanced) excluded; hence any quartic counterexample has leading target span exactly two | [`JCG-90614345`](../../claims/JCG-90614345.md), [`JCG-F13D186D`](../../claims/JCG-F13D186D.md); continuation appendix, Cor `cor:quartic-target-span-two` |
| 5 | Genuinely nonbinary quadratic-source locus excluded (nine charts) | [`JCG-B2D60A95`](../../claims/JCG-B2D60A95.md); continuation appendix |
| 6 | Coprime binary pencils with common ramification divisor of degree <= 2 are automorphic | [`JCG-1AE58E51`](../../claims/JCG-1AE58E51.md), [`JCG-176D3DFE`](../../claims/JCG-176D3DFE.md), [`JCG-059D835C`](../../claims/JCG-059D835C.md); Thm `thm:target-span-two-ramification-two` |
| 7 | Fixed-component Plücker chart closed — **as a rank-one special case only** (see graveyard) | [`JCG-34460CE2`](../../claims/JCG-34460CE2.md); continuation appendix |
| 8 | Triple ramification (degree exactly 3) reduces, via the Hilbert–Burch branches of types `(2,5)` and generic `(3,4)`, to an explicit `F_4` weighted-inflection family | [`JCG-9D9C3DF9`](../../claims/JCG-9D9C3DF9.md); continuation appendix; **conditional on the leading-curve reductions above** |
| 9 | On the generic `(3,4)` branch, away from the displayed denominator, rank-drop, resonance, and weighted-inflection divisors, the six next Keller equations have rank six and exactly two quadratic kernel directions; their span meets the quadratic Veronese only at the origin | [`JCG-9D9C3DF9`](../../claims/JCG-9D9C3DF9.md); continuation appendix, `subsec:degree-three-ramification-frontier` |

Standing hypotheses to keep visible: items 4–8 are conditional on the
manuscript's leading-curve reductions (items 1–3); the case tree is audited
in task T3 below.

### Proof-signature index

| Input | Proof signature / reusable output | Boundary exits |
| --- | --- | --- |
| 1, rank one | A weighted Lüroth argument puts the coordinate field in one variable; degree factorization and valuations reduce the top layer to cube/binary cases; two determinant syzygies force a triangular plane Keller map. **Output:** a weighted one-variable field and two binary determinant identities. | Uses `rho_4=1`; it is not a coordinate lemma for arbitrary submersions. |
| 2, conic | For four historical factor orbits, the characteristic derivation has invariant field `C(x/y,Gy^2)`; invariant-degree gaps kill the first normal defects and five exact terminal charts force `det L=0`. The remaining three orbits use separate later certificate/automorphism arguments. **Output:** complete seven-orbit conic exclusion. | Do not extend the four-orbit invariant-field proof to the other three; cite the full three-claim package. |
| 3, four loci | Factor the rational map degrees as `n=ed`, enumerate the composite-degree table, and apply the primitive valuation identity `4 nu(R)=c_xi m` with `sum c_xi=3`. **Output:** an exhaustive structural routing into four span-two loci. | Exhaustiveness still depends on recording every overlap and special fiber in T3. |
| 4, rational curves | Use tangent syzygies and Hilbert--Burch classification, then projective duality. Explicit tricuspidal and balanced normal forms make the first terminal coefficients force binary normal layers and finally `L_z=0`; the target-span synthesis also invokes the rational-cubic exclusion. **Output:** span-three proper rational images are closed. | Only after the leading-curve classification; it does not close span-two ramification. |
| 5, quadratic source | On the no-fixed-component `(2,2)` locus, normalize source and target data in nine charts; in each, the determinant arc makes the Hilbert--Burch columns proportional. **Output:** a chart-complete exclusion of the genuinely nonbinary quadratic-source leaf. | Fixed components and chart-boundary overlaps leave through their own branches. |
| 6, ramification at most two | Regular branch: Hilbert--Burch degrees kill every `z` term. Simple branch: a weighted inflection plus anchor coefficients closes the chart. Double branch: the two Hilbert--Burch types reduce to a terminal coefficient `-1/3`. **Output:** three separately proved low-ramification exclusions. | No statement for ramification degree at least three. |
| 7, Plücker special case | The Plücker relations force the third column of the relevant linear matrix `L` to vanish, collapsing the intended chart to rank one. **Output:** a fixed-component/rank-one boundary certificate. | This is not the full target-span-two locus. |
| 8, triple ramification | Hilbert--Burch classification splits into cube, fourth-power, fixed-component, and source-shear exits; the remaining generic `(3,4)` branch enters the explicit `F_4` weighted-inflection family. **Output:** a finite branch list and normal forms. | Exceptional divisors and `F_4` compatibility remain; “triple ramification closed” would be false. |
| 9, generic `(3,4)` chart | Reconstruct the gradient factorization over `Q(a,b,tau)`, form the six-by-eight next-layer matrix, certify rank six and two kernel vectors, then factor the denominator and rank minor. **Output:** the generic kernel plus the exact exceptional-divisor queue. | Every vanishing factor requires a fresh chart; rational formulas may not be specialized across their poles. |

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
are required. The endgame data are not present in the reviewed mathematical
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

**(F2) Common ramification divisor of degree >= 4.** No reduction is
recorded. The expected route is the same valuation table as
`prop:four-loci` plus the Hilbert–Burch analysis that handled degree 3;
the ramification degree is at most 5, so this is finitely many strata.

**(F3) Fixed-component boundaries,** including nonprimitive overlaps with
the binary locus. Partially covered by items 3 and 7; no complete
classification.

**(F4) Exhaustiveness audit.** The chain 1–8 was built incrementally across
several conversations; nobody has written the single case tree from
`rho_4 in {1,2,3}` to the leaves and checked that the union of closed
strata plus F1–F3 is everything.

The dependencies are therefore: a case-tree audit certifies that the
span-two reduction reaches the stated pencil/fixed-component leaves; the
Hilbert--Burch classification routes the degree-three ramification leaf to
generic and exceptional `(3,4)` charts; the generic verifier removes the
open complement of its displayed divisors; and the `F_4` compatibility plus
higher-ramification/fixed-component work must close the remaining divisors.
Do not describe “triple ramification” as closed until that entire chain is
present. Conversely, do not send a model back into the generic rank-six
calculation: that exact finite problem is complete.

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

**P2-T2 — Classify ramification >= 4 and fixed-component boundaries.**
Actor: `online_model`. Status: ready.
*Payoff:* the last open strata; with T1, `D_min >= 5`.
*Attack:* extend the degree-3 Hilbert–Burch analysis; the valuation table
of `prop:four-loci`; Wall's classification of binary quartic pencils for
the stratum bookkeeping. Remember two-sidedness (Section 2).
*Done when:* every stratum is a theorem, a reduction to an exact
calculation with a spec, or an explicitly isolated open case.

**P2-T3 — Write the case tree and audit exhaustiveness.**
Actor: `online_model`. Status: ready.
*Payoff:* removes the standing "conditional on the earlier reductions"
qualifier from items 4–8; referee-facing artifact.
*Done when:* a single document routes every `rho_4` value to a leaf, each
leaf carrying a theorem locator or an open-task pointer, with no gaps.

**Escalation rule.** If T1 or T2 exposes a positive-dimensional stratum that
continues to satisfy all tested Keller layers, stop treating it as merely a
failed exclusion. Record its standing hypotheses and promote it to a
candidate-construction task. A second counterexample with a mechanism
independent of the degree-seven marked-root example would be at least as
valuable as the bound `D_min >= 5`.

## 7. Evidence and replay index

The [Program 2 working paper](../../assets/manuscripts/02-quartic-keller-maps-2026-07-22-v11.pdf)
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

- Do not re-prove items 1–8; cite them.
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
