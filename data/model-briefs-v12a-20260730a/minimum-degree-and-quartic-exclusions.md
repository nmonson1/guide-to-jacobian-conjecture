# Program 2: Minimum Degree and Quartic Exclusions

**Actor guidance:** conceptual classification -> online model; exact
elimination -> local symbolic; nothing here needs a large CAS.

**Public one-link handoff:** [Program 2 — exact inputs, dependencies, and
proof links](../../research/handoffs/minimum-degree-and-quartic-exclusions/).

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
  component** `G`. For a span-two leading pair, write
  `H = deg gcd(grad(P) cross grad(Q))`.

The logical order matters. The leading image first determines whether the
top form has target span one, two, or three. Only after the span-two branch
has been reached may one invoke binary-pencil ramification. “Binary” is a
geometric conclusion of the earlier reductions, not a coordinate choice
available at the start. Likewise, a finite symbolic elimination proves only
the chart it actually parametrizes. Every proposed normal form should be
checked against its intended stratum before coefficients are eliminated.

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

The hypotheses in the middle column are part of each statement. The final
column opens the public proof body directly; use the local source or exact
program named there when doing a replay.

| # | Exact statement and boundary exit | Mechanism / reusable output | Proof |
| --- | --- | --- | --- |
| 1 | If `rho_4=1`, the map is an automorphism with arbitrary mixed lower terms and no homogeneity or nilpotency assumption. This is not a general submersion-to-coordinate lemma. | Weighted Lüroth plus valuation reduction; two binary determinant syzygies produce a triangular plane extension. | [paper p. 5](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=5) |
| 2 | The v13 paper and recovered audit packet directly support four nondegenerate conic factor orbits. The project has later arguments claiming the other three, but they are not proved in that PDF and require their own locators and audit before the seven-orbit synthesis is used. | Four certificate-backed orbit exclusions plus a three-orbit proof-access gap. | [paper p. 10](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=10); recovered audit verifiers |
| 3 | Subject to the span-two normal form, the highest Keller equation routes the leading pair into four possibly overlapping loci: binary pencil; quadratic-source `(2,2)`; composition-primitive coprime pencil containing `ell^4`; or composition-primitive reduced pencil with nonbinary fixed components. | `n=ed`, the composite-degree table, the corrected identity `4 nu_Gamma(R)=3s+c_xi m`, and `sum c_xi=3` give the routing. | [paper p. 10](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=10) |
| 4 | Assuming the named leading-curve factorization and rank-one, conic, rational-cubic, balanced-quartic, and tricuspidal-quartic exclusions, every nonautomorphic quartic Keller map has leading target span exactly two. | Tangent syzygies and Hilbert--Burch normal forms close the last two proper rational-quartic strata. | [paper p. 16](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=16) |
| 5 | The genuinely nonbinary **no-fixed-component** quadratic-source `(2,2)` locus is impossible in all nine normalized charts. Fixed-component boundaries exit to items 13–17. | In each chart the determinant arc forces the relevant Hilbert--Burch columns to become proportional. | [paper p. 18](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=18); local bundle 003 |
| 6 | Subject to the structural reductions, every coprime binary pencil with common ramification degree at most two is automorphic. This item alone makes no conclusion for degree at least three. | Separate regular, simple-root, and double-root Hilbert--Burch mechanisms; the last chart ends at coefficient `-1/3`. | [paper p. 18](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=18); local bundle 005 |
| 7 | For `H_4=(0,0,x^2y^2)` and cubic pencil `<x^2y,xy^2>`, the Keller equations force the third column of `L` to vanish. This is one rank-one/fixed-component chart only. | Plücker relations collapse the chart to rank one. | [paper p. 17](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=17); local bundle 002 |
| 8 | Within the supplied degree-three Hilbert--Burch normal-form system, exact calculations now derive the generic `F_3/F_4` exits and close their nonresonant, `tau=-1`, `tau=0`, `tau^2+1=0`, `c=0`, dependent-syzygy, quadratic-exceptional, and zero-normal charts. This closes the previously listed encoded degree-three calculation gates; it does not independently prove that the upstream global quartic case tree reaches and exhausts precisely these charts. | Kernel-plane/Veronese elimination plus exact full-determinant identities in every named divisor chart. | [paper p. 20](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=20); local v5 quartic-binary endgame |
| 9 | On the reconstructed generic `(3,4)` open chart, after every displayed denominator, rank-drop, resonance, and weighted-inflection factor is inverted, the `6 x 8` matrix has rank six and its two-dimensional kernel plane misses the quadratic Veronese away from the origin. | Exact reconstruction over `Q(a,b,tau)` outputs the kernel basis and exceptional-divisor queue. Nothing specializes across an inverted factor. | [paper p. 20](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=20); local July 28 verifier |
| 10 | Subject to items 3–6 and membership in the primitive coprime binary-pencil locus, common ramification degree `r=4` or `r=5` forces an automorphism. The `r=4` proof includes dependent residuals, reduced residual quadratics, the repeated-root incidence, the omitted projective point, and the complete `2+2` kernel. | Universal minor syzygy plus exact determinant-arc and projective-coverage certificates. | [paper p. 21](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=21); local `code/program-2-2026-07-29-v2/high-ramification/` |
| 11 | Subject to the primitive span-two reduction, a fourth-power pencil member adds no leaf: its highest nonzero normal layer routes to an aligned, binary, or quadratic-source branch. | Polynomial common generator plus exact degree audit. | [paper p. 22](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=22); local `quartic_high_ramification_v3.md` and coverage verifier |
| 12 | In the binary branch, if one of `U=J(Q,R)`, `V=J(P,R)`, `W=J(P,Q)` vanishes—including the separate `R=0` case—the map is automorphic. The ordinary `r` filtration is applied only after removing these boundaries. | Euler/UFD argument and exact `R=0` determinant arc. | [paper p. 22](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=22); local `verify_quartic_binary_edges.py` |
| 13 | In the primitive fixed-component branch `P=GA,Q=GB`, if `Gamma` has multiplicity `s` in `G` and `m` in the reduced fiber over `xi`, then `4 nu_Gamma(R)=3s+c_xi m` and `sum c_xi=3`, with the adjusted infinity convention. The `c_xi` can be negative. | Corrected divisor valuation; supersedes the earlier formula without `3s` and every proof assuming all `c_xi>=0`. | [paper p. 23](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=23); local valuation note and verifier |
| 14 | Subject to the four-loci reduction and the standard polynomial-centralizer theorem, every genuinely nonbinary primitive fixed-component branch is closed. | Valuation congruences reduce to the residual-pole normal form; two determinant layers reassemble it and force a zero Jacobian. | [paper p. 23](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=23); local valuation note and verifier |
| 15 | Subject to the binary fixed-component reduction, every cubic fixed factor is automorphic or undergoes a triangular degree drop; squarefree, double-plus-simple, and triple-line multiplicities are all covered. | Exact incidence and normal-layer sweep by multiplicity type. | [paper p. 24](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=24); local cubic note and four verifiers |
| 16 | Subject to the binary fixed-component reduction, every linear fixed factor is automorphic. After `H_4=(x^4,xB,0)`, the two residual-cubic orbits and every exceptional divisor are covered. | Exact `8 x 8` determinant, projective endpoints, and resonant-vertex reassembly. | [paper p. 24](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=24); local linear note and verifier |
| 17 | Subject to the binary fixed-component reduction, every quadratic fixed factor with coprime residual quadrics is automorphic. Normalize `P=x^2G,Q=y^2G`; the four determinant divisors `disc(G)=0`, two axis-tangencies, and `Res(G,R)=0`, including every intersection and endpoint, are covered. | Exact determinant factorization and 38-group replay over rational-function or explicit algebraic-number fields. | [paper pp. 24–25](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=24); local quadratic note and manifest-pinned archive |
| 18 | In dimension three and every degree `d`, no Keller map has a **period-primitive** leading line. “Period-primitive” is distinct from composition-primitive and coprime. | The normal-resonance threshold is `3(d-1)`. | [register p. 9](../../assets/manuscripts/{{MANUSCRIPT_07}}#page=9) |
| 19 | **Conditional synthesis only:** if the upstream leading-curve, target-span, four-loci, ramification, and fixed-component routing used in items 1–17 is correct and exhaustive, the replayed terminal leaves imply that every quartic Keller map is automorphic and hence `D_min >= 5`. | One terminal-leaf table assembled from the July 29 proof packets and the v5 degree-three bundle. | local `code/program-2-2026-07-30-v5/quartic_binary_endgame/quartic_binary_endgame.md` |

Standing hypotheses to keep visible: items 4–17 depend on the named
leading-curve and structural reductions; item 9 also depends on membership
in its explicitly reconstructed open chart. The successful programs do not
prove those upstream reductions or global case-tree exhaustiveness. Item 19
packages that exact conditional boundary and is not an unconditional theorem.
The current unconditional public interval remains `4 <= D_min <= 7`.

**Paper-audit checkpoint, 30 July 2026.** The rank-one theorem and its exact
verifier survive. The four conic certificates and additional tricuspidal,
syzygy, and count checks replay. Corollary A.2's exact target-span-two
conclusion is not supported by the v13 PDF: the paper does not prove the
remaining three conic orbits or the rational-cubic exclusion. B.4 is
incomplete, and C.2, C.3, and D.2 are not yet publication-grade. This audit
strengthens the demand for P2-T1; it does not erase later local calculations.

## 4. The live frontier

**(F1) Global case-tree and proof-to-code audit.** Evidence checkpoint:
**2026-07-30**. The v5 quartic-binary endgame materially changes the frontier:
the previously listed degree-three calculation gates all have explicit
programs and successful exact replays; every stored deterministic output
agrees with the fresh replay.

What remains is not another missing CAS chart. The chain 1–17 was built
incrementally across several conversations. Write the single case tree from
`rho_4 in {1,2,3}` through the four-loci split to every terminal chart.
For each edge, verify the exact hypotheses in the cited proof; for each
computer-assisted leaf, map every proof chart to a program group and record
any proof-only or code-only chart. This is not permission to assume the new
fixed-component and high-ramification results are wrong; it is the work
needed to remove their standing upstream-routing qualifier.

The v5 high-ramification checker is a useful second structural
implementation, but it explicitly imports the complete-specialization claim
`JCG-5C216C29`. Its exact replay therefore checks the algebra downstream of
that claim, not the claim's proof. Likewise, five degree-three helper modules
are explicitly reconstructed and all programs remain one SymPy lineage.

**(F2) Independent reproduction and proof review.** Reimplement the
degree-three branch discovery and at least one representative from every
exceptional chart without importing the reconstructed helpers. Then compare
the programs line by line with the conventional Hilbert--Burch and
determinant-arc arguments. A clean second lineage would change the status
from “encoded calculation closed” to “independently reproduced”; it still
would not replace the global case-tree audit in F1.

**Earlier computation checkpoint.** Nine exact calculations independently
replay on the displayed generic, `c=0`, `tau=0`, `tau=-1`, and zero-normal
charts, without proving global placement. A separate exploratory Lane 4
packet is not all-passed: its `tau=0` expected resultant is off by
`16/(b0^2 c0^2)`, and it asserts 28 nonzero maximal minors where the exact
counts are 19 generically and on `tau=0`, and 14 on the minimal-syzygy
chart. Keep that packet chart-local.

**Degree-five/six checkpoint.** A separate exact packet proves substantially
more than the earlier exploratory Lane 4 material, but only under its stated
leading-pair hypotheses. A primitive coprime quintic line image routes to
binary or aligned `(L^5,L^4)`; the squarefree binary-cubic conic branch is
excluded, while an aligned nonbinary specialization survives the next Keller
layer. Under the closed-pair hypothesis
`ker Jac(A,B,-)=k[A,B]`, the primitive sextic conic and weighted `(2,3)` core
are excluded. All eight self-contained scripts replay. This is neither a
global degree-five/six classification nor evidence that degree four can be
skipped.

Lane 5 has a different, more mature result. After regenerating four omitted
filtered-basis files, every exact certificate for the listed source
filtrations with `delta(Q) <= 9` replays and gives
`trdeg A_{<=6} <= 2`. The remaining frontier is the unramified
`delta(Q) >= 10` case and a conceptual filtered-conormal,
Wronskian, or conductor theorem. This does not prove left-right minimality
or change the unconditional `D_min` interval.

**Working audit lens — companion/Jordan budget (not a promoted theorem).**
For the determinant arc
`M(t)=A_0+A_1 t+...+A_s t^s`, with `s=D-1`, the supplied companion
construction puts multiplication by `t` on
`E=direct_sum_{j=0}^{s-1} O(-j)^3` as a generically regular nilpotent
`T:E -> E(1)` of length `N=3s`. If `d_i` are the effective link-divisor
degrees in its saturated rank-one kernel flag and `kappa_R,kappa_L` are the
two endpoint defects, the proposed exact budgets are

```
sum d_i       = 2s - kappa_R - kappa_L,
sum (N-i)d_i  = 3s(s-kappa_R),
sum i d_i     = 3s(s-kappa_L),
```

together with a second-Chern-character identity for the point defects.
For a quartic span-two leading pair this forces `H >= 4` and leaves a finite
list of equality profiles. The controlling v4 calculations then route the
`H=5,6` linear-kernel leaves into already known structural loci and exclude
the displayed minimal fourth-power, simple fixed-line, and smooth-conic
`H=4` charts, conditional on their normal forms and case placement.

Use this as an alternative derivation and consistency check in P2-T1/T3.
It does not replace the already stronger July 29 closures of ramification
four/five, fourth-power pencils, or fixed factors; it is not invariant under
arbitrary polynomial left-right equivalence. In particular, it does not solve
Lane 5's intrinsic orbit-degree problem or prove `D_min >= 5`. The finite
programs check the algebraic identities, profiles, ranks, and named charts,
not the sheaf-theoretic kernel-flag and endpoint argument by an independent
proof.

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
- **The Jordan budget is not an orbit-degree invariant.** Its companion
  presentation is tied to the displayed degree and determinant arc. An
  arbitrary polynomial left-right change need not preserve that presentation
  or its numerical profile. It is a sharp Program 2 audit tool, not the
  intrinsic Lane 5 monotone.

## 6. Tasks

**P2-T1 — Write the global case tree and audit exhaustiveness.**
Actor: `online_model`. Status: ready.
*Payoff:* removes the standing "conditional on the earlier reductions"
qualifier from items 4–19; referee-facing artifact.
*Attack:* begin at `rho_4 in {1,2,3}`; expand every leading-curve,
composition, four-loci, ramification, and fixed-component split; verify
membership before using a normal form; preserve overlaps explicitly; map
each terminal leaf to a theorem or explicit open edge.
*Done when:* a single document routes every `rho_4` value to a leaf, each
leaf carries exact hypotheses and a theorem/program locator or open-task pointer,
and every overlap has an explicit ownership rule.

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

**P2-T3 — Audit the July 29 proof packets and program correspondence.**
Actor: `online_model` for proof review plus `local_symbolic` for independent
reproduction. Status: ready.
*Payoff:* tests the strongest new inputs before they are used in a
degree-four theorem.
*Attack:* check the `r=4` repeated-root coverage, the signed
fixed-component valuation and residual-pole argument, then the cubic,
linear, and quadratic fixed-factor chart trees. For each proof chart, name
the exact verifier group; independently reproduce the generic determinants
and a representative from every exceptional family.
*Done when:* every proof chart is marked proof-only, code-backed, or
independently reproduced; every unmatched code group is explained; all
dependencies and any counterexamples are recorded.

**Escalation rule.** If T1, T2, or T3 exposes a positive-dimensional stratum that
continues to satisfy all tested Keller layers, stop treating it as merely a
failed exclusion. Record its standing hypotheses and promote it to a
candidate-construction task. A second counterexample with a mechanism
independent of the degree-seven marked-root example would be at least as
valuable as the bound `D_min >= 5`.

## 7. Evidence and replay index

Bundles under `evidence/` (each with `SHA256SUMS`; replay commands in
`COMPUTATION.md`):
`001` rational-quartic frontier exclusion (plus independent pure-Python
implementation) · `002` Plücker fixed-component elimination (see graveyard
for scope) · `003` target-span-two progress: nine quadratic-source charts ·
`004` weighted-inflection reduction (first obstruction only) ·
`005` binary ramification degree <= 2.

The July 28 replay is separate from those recovered dialogue bundles:
`replay/manuscripts/02-low-degree/code/program-2-2026-07-28-v2/` contains the
runner and exact verifier. The successful immutable execution is
`program2-generic-triple-ramification-q-v2-20260728a`. Its JSON records the
coefficient domain, matrix shape, kernel basis, denominator, rank minor,
resultant gcd, and interpretation; its stdout reports `verified: true` and
generic rank six.

The July 29 sources are pinned in
`replay/manuscripts/02-low-degree/code/program-2-2026-07-29-v2/` after handoff
generation. The standalone high-ramification and fixed-component verifiers
all passed. The quadratic archive has SHA-256
`9448ae88a3b00f8e6013085ce6fe42ffe84e51c1a6a4fb3fe761f6de2a75090f`;
its internal manifest passed and all 38 exact replay groups passed from a
fresh temporary copy. The earlier provisional fixed-component files that
omitted `3s` from the valuation or assumed all `c_xi` nonnegative are
superseded and are not evidence for items 13–17.

The candidate `F4` source note, byte-identical source verifier, minimally
replay-fixed verifier, and exact scope record are under
`replay/manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/`.
The repaired verifier passes all seven encoded checks; the source verifier's
single expression-form assertion fails as documented. Four advertised source
artifacts, including an independent verifier, were unavailable and remain
explicitly unresolved rather than reconstructed.

The controlling v5 supplement
`code/program-2-2026-07-30-v5/quartic_binary_endgame/` supersedes that open
calculation queue. Its internal manifest passes, every script in
`run_all.sh` succeeds under SymPy 1.14.0, and all seven stored deterministic
outputs match the fresh replay byte-for-byte. The bundle supplies the missing
generic branch-elimination, resonant, `c=0`, dependent-syzygy,
quadratic-exceptional, and zero-normal calculations. Five helper modules are
explicit reconstructions, the programs form one symbolic lineage, and the
high-ramification checker imports `JCG-5C216C29`; retain those qualifications.

The July 30 companion/Jordan-budget intake contributes two controlling
bundles to the replay packet. The v3 bundle embeds the v2 foundation and
records the fixed-component correction; the v4 bundle controls all earlier
chart prose. The v2, v3, and v4 manifests pass, and local replay passed all
four v2 programs, the v3 correction verifier, and all five v4 verifiers.
The older v2 assertion that an entire ramification-degree-four normal form
was empty is withdrawn. The corrected fixed-component Wronskian contains the
doubled base divisor `2B_0`. Treat the successful ten-program replay as one
SymPy lineage; the conventional companion-module, saturation, endpoint, and
Chern-character proof still needs specialist verification.

The conventional argument/check boundary is deliberate. The scripts verify
displayed identities, finite chart eliminations, matrix ranks, kernels, and
factorizations. They do not independently prove the leading-curve
classification, the conic-pencil valuation lemma, the Hilbert--Burch case
classification, or the claim that the listed charts exhaust the geometric
stratum. Those dependencies belong in the case-tree audit rather than being
hidden behind the successful replay label.

## 8. Do not do

- Treat items 1–18 as qualified project inputs unless the assigned task is
  to audit one of them.  Preserve every stated hypothesis and evidence
  limitation, and report any contradiction rather than silently repairing
  it.
- Do not treat finite-field samples as characteristic-zero proofs.
- Do not promote the imported degree-five/six chart calculations into global
  classifications or use them to bypass the degree-four routing audit.
- Do not relax the conic-orbit hypotheses: the untreated orbits
  `G = xy, z^2, x^2` are excluded from the method for a stated reason
  (odd-degree or degree-six invariants survive), not by oversight.
- Do not cite the generic rank-six certificate as a uniform solution on its
  rank-minor or denominator divisors.
- Do not claim `D_min >= 5`: the current unconditional public interval is
  still `4 <= D_min <= 7`.
- Do not send a model to rederive an individual missing resonant or `c=0`
  chart as though no implementation exists. The useful work is independent
  reproduction or global case-tree/proof-to-code audit.
- Do not promote an older v2/v3 Jordan-budget sentence over the v4 erratum,
  infer global chart exhaustiveness from the ten passing programs, or use the
  presentation-sensitive budget as a left-right orbit invariant.
- Do not cite the Lane 4 kernel--Veronese script as wholly passing until its
  `tau=0` expected-resultant formula is corrected and replayed.
- Do not trust a normal form by its intended label. Verify directly that its
  leading target span, fixed component, and ramification divisor place it in
  the claimed stratum before running elimination.
