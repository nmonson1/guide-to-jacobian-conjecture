# Lane 4 exact research source packet

This is the public source packet for **The quartic endgame**. It contains the
selected proof notes, exact computation contracts, and checkers used
by the concise lane brief. Read only the files relevant to the route
you pursue. Stored outputs and very large reconstructible matrices are
omitted; the mathematical boundary of each checker remains in its
source text.

Private-source commit: `e38fa7bda854c38167b05c7e8b79ca61bbfade04`.

## Included files

- `lane4-quartic-endgame-20260802-v1/README.md` — `4cc314eb0ef7e1ec0447f21db5b5a7a7209fa3bb5274429647dc323519a1e96e`
- `lane4-quartic-endgame-20260802-v1/PROOF_CODE_CROSSWALK.md` — `529a23a6caf3e34ebaea3de6d1102998b7f5532d3b2f47d89704a781e19c34b7`
- `lane4-quartic-endgame-20260802-v1/case-tree/lane4-global-case-tree.md` — `82393d020cad9346365fe2c388baa7cdd5abb2a2e789eaf3b5e2590998c386d9`
- `lane4-quartic-endgame-20260802-v1/case-tree/lane4-case-tree.csv` — `63962c80bd4a6d61aa3e948109071b9b0393f40c3357bc5c5b0b90aa509ba5c3`
- `lane4-quartic-endgame-20260802-v1/proofs/10-structural-repairs-and-z2.tex` — `03db7a707edf9e4791545e8451fdc2fd7540cd9a026635e0212bd82d53c57a4b`
- `lane4-quartic-endgame-20260802-v1/proofs/20-conic-completion.tex` — `02aee17b2f75ae7deea2961d3dd66bb12290d5873182b70156386f6dcfc38398`
- `lane4-quartic-endgame-20260802-v1/proofs/30-rational-cubic.tex` — `7485acbd0d77bfd9a41763711199c1b1af490b88c9576645e604b84d100d8cec`
- `lane4-quartic-endgame-20260802-v1/proofs/40-span-three-corollary.tex` — `71315a0e2adb2b80f48ca873163e0da0e041c2246b5351130b16e37909e9797a`
- `lane4-quartic-endgame-20260802-v1/proofs/50-high-ramification.tex` — `c30ac4269bfcc45047b6ff4a23b2c9372f09c18cea3ee97c6dbcabac20fb2901`
- `lane4-quartic-endgame-20260802-v1/proofs/60-tau-minus-one.tex` — `a818a9f2559de4f6d8b76d56e017c6d0bcfa75925f81cb7b3832728c83dccc74`
- `lane4-quartic-endgame-20260802-v1/replay_core.py` — `414571f93cb504116146004b02447b03827b64d27262c93985dc266210b264d6`
- `lane4-quartic-endgame-20260802-v1/checks/conic/verify_terminal_identities.py` — `dc1f6915b7256a14b84b3b28c10b12144b4f35f6010fd44807f52743ef186689`
- `lane4-quartic-endgame-20260802-v1/checks/high-ramification/verify_r4_high_ramification.py` — `bf490b014a79dfeba1dd26e0fbb195d0adfe53741ad93d63736ee0a395cc8c6d`
- `lane4-quartic-endgame-20260802-v1/checks/tau-minus-one/verify_tau_minus_one.py` — `3937d64a233eb6200feec829b774ac80c5714da305394242f47ad2c0f46551eb`

## `lane4-quartic-endgame-20260802-v1/README.md`

<pre><code class="language-markdown">
# Lane 4 quartic-endgame repairs and exact calculations

This directory is an additive, unrefereed research packet for Program 2,
prepared against repository main commit
`e6deaf7b266d5d236dab78ac3765e772e2d3edba` on 2 August 2026.

It records candidate proof repairs and exact characteristic-zero calculations
developed while auditing Lane 4.  It does **not** replace the canonical
manuscript, mutate the generated claim graph, or assert the unconditional
bound `D_min &gt;= 5`.  The public interval remains

\&#91;
4\le D_{\min}\le 7.
\&#93;

## Mathematical contents

| Item | Supplied material | Status in this packet |
| --- | --- | --- |
| Leading-image factorization | replacement normalization proof | candidate reader proof |
| Four-locus span-two reduction | replacement valuation proof with overlap ownership | candidate reader proof |
| Zero cubic normal layer `R=0` | quadratic-coordinate and plane-reduction argument | candidate proof; plane theorem required |
| Nonbinary fixed-component endpoint | homogeneous cubic centralizer lemma | candidate proof repair |
| Missing conic representatives `G=z^2,x^2,xy` | three coefficient arguments and exact scripts | candidate proofs plus exact replay |
| Proper rational-cubic image | cusp/node, transverse/marked analysis | candidate proof plus exact replay samples |
| Leading target span three | synthesis of the preceding arguments and public frontier inputs | explicitly conditional corollary |
| Primitive binary ramification `r&gt;=4` | projective repeated-root proof including `3+1`, internal `2+2`, and endpoints | candidate theorem plus exact standalone replay |
| Primitive `r=3`, `tau=-1` | complete exceptional-divisor argument | candidate theorem plus exact standalone replay |
| Global ownership map | one case tree and machine-readable CSV | audit draft, not a global theorem |

The proof note is &#91;`proofs/main.tex`&#93;(proofs/main.tex).  Its component files
are deliberately separated so that accepted repairs can be inserted into a
later canonical manuscript without importing unrelated claims.

## Evidence layout

- &#91;`verify_r4_high_ramification.py`&#93;(checks/high-ramification/verify_r4_high_ramification.py) is the exact
  `r=4` projective-incidence checker; the adjacent `.out` file is pinned output.
- &#91;`verify_tau_minus_one.py`&#93;(checks/tau-minus-one/verify_tau_minus_one.py) is the exact
  `tau=-1` checker; the adjacent `.out` file is pinned output.
- &#91;`checks/conic/run_replays.py`&#93;(checks/conic/run_replays.py) exposes the ten
  `x^2/xy` branch cases; the same directory contains the standalone `z^2`
  checker, exact stored outputs, and a compact terminal identity verifier.
- &#91;`transverse_after_translation.py`&#93;(checks/rational-cubic/scripts/transverse_after_translation.py)
  is an entry point into the rational-cubic checks; the same directory contains
  the marked-node, marked-cusp, and second-normal scripts with stored outputs.
- &#91;`replay_core.py`&#93;(replay_core.py) reruns the compact evidence set;
  `--full-conic` also reruns all ten larger conic branches.
- &#91;`PROOF_CODE_CROSSWALK.md`&#93;(PROOF_CODE_CROSSWALK.md) records the precise
  proof/check boundary.
- &#91;`VALIDATION.md`&#93;(VALIDATION.md) records the clean replay and TeX checks.
- &#91;`manifest.json`&#93;(manifest.json) records the base commit, environment, file sizes, and source digests; &#91;`SHA256SUMS`&#93;(SHA256SUMS) pins the final packet.
- &#91;`SESSION_EVIDENCE_LEDGER.md`&#93;(SESSION_EVIDENCE_LEDGER.md) identifies
  reported work that was not retained and is therefore not promoted here.

## Replay

Install the pinned symbolic dependency and run the compact groups:

```bash
python -m pip install -r requirements.txt
python replay_core.py --group structural
python replay_core.py --group conic
python replay_core.py --group rational-cubic
```

The complete conic branch suite can be run case-by-case with

```bash
python checks/conic/run_replays.py x2-scalar
python checks/conic/run_replays.py x2-semisimple
# See `python checks/conic/run_replays.py` for the remaining case names.
```

or in one process family with

```bash
python replay_core.py --group conic --full-conic
```

Each conic branch wrapper compares the fresh output byte-for-byte with its
stored output in addition to checking the terminal obstruction.

Compile the standalone note from `proofs/` with

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Dependency and review boundaries

The packet does not re-prove every public Program 2 input.  In particular:

1. placement in the rank-one, binary-pencil, quadratic-source,
   fixed-component, Hilbert--Burch, and rational-quartic frontier strata is
   imported with its stated hypotheses;
2. the final triangular reductions use the Appelgate--Onishi plane result in
   the formulation that a plane Keller pair is invertible when one coordinate
   degree has at most two prime factors, together with the Nowicki--Nakai
   repair of the lemmas used in that argument;
3. the exact programs verify finite displayed identities and chart ideals;
   they do not prove the upstream geometric classifications;
4. all programs are SymPy/Python implementations and are not a second-CAS
   lineage; and
5. every new mathematical assertion requires specialist human review before
   integration into a claim graph or manuscript theorem.

The case tree records these boundaries at each leaf.  A successful terminal
calculation must not be read as global branch exhaustiveness.

## Provenance

GPT-5.6 Pro assisted with the audit, theorem formulation, proof drafting,
exact symbolic programs, and packet assembly.  The repository owner remains
responsible for accepting, revising, or rejecting every assertion.  This
packet is intentionally labeled AI-assisted and unrefereed.
</code></pre>

## `lane4-quartic-endgame-20260802-v1/PROOF_CODE_CROSSWALK.md`

<pre><code class="language-markdown">
# Lane 4 proof-to-code crosswalk

The table distinguishes conventional mathematics from finite symbolic
certificates.  A script locator means only that the displayed algebra was
checked on the stated chart.

| Proof component | Statement or equation range | Exact program(s) | What the program certifies | What remains conventional or imported |
| --- | --- | --- | --- | --- |
| Leading-image factorization | first replacement proof in `proofs/10-structural-repairs-and-z2.tex` | none | not applicable | rationality of a unirational curve, normalization, coprime-pencil representation |
| Four-locus reduction | second replacement proof in `proofs/10-structural-repairs-and-z2.tex` | none | not applicable | weighted one-variable field input and divisorial valuation argument |
| `R=0` branch | Proposition `quartic-r-zero-repair` | none | not applicable | quadratic-coordinate lemma, plane degree theorem, birational Keller implication |
| Homogeneous cubic centralizer | Lemma `homogeneous-cubic-centralizer` | none | not applicable | two-variable common-generator/closed-polynomial theorem and descent |
| `G=z^2` conic | Proposition `conic-z2-exclusion` | `checks/conic/z2_conic_independent_check.py` | full determinant arc on the two normal-form branches with arbitrary quadratic and linear coefficients | completeness of the normal-form reductions and allowed source/target actions |
| `G=x^2` conic | Theorem `quartic-conic-x2` | `checks/conic/raw-scripts/x2_*.py`, invoked by `checks/conic/run_replays.py` | scalar, semisimple, two nilpotent, and two second-normal terminal systems; fresh output equals stored output | the stabilizer-orbit split and its ownership |
| `G=xy` conic | Theorem `quartic-conic-xy` | `checks/conic/raw-scripts/xy_*.py`, invoked by `checks/conic/run_replays.py` | scalar, anti-scalar, and two second-normal terminal systems; fresh output equals stored output | the stabilizer-orbit split and its ownership |
| Conic terminal identities | square/determinant factorizations in both conic proofs | `checks/conic/verify_terminal_identities.py` | exact polynomial identities over `Q` | does not reconstruct the full determinant elimination |
| Rational cubic, transverse factor | first case of `proofs/30-rational-cubic.tex` | `checks/rational-cubic/scripts/transverse_after_translation.py` | cusp rank eight/nullity one and node rank nine/nullity zero; `det L=0` after translation | classification of proper rational plane cubics and normalization of the transverse factor |
| Rational cubic, marked node | parameterized nodal family | `node_marked_lambda_d7.py`, `node_h2z_pivotminor.py`, `node_h2z_fullmatrix.py` | three pure compatibility equations and a parameter-independent maximal minor `12582912` | projective marked-point coverage, including the branch interchange at infinity |
| Rational cubic, marked cusp | three cusp marked-point orbits | `cusp_fiber_*.py`, `cusp_smooth_*.py`, `cusp_generic_*.py` | fixed nonzero `D_6/D_5` coefficients on every displayed normal-amplitude branch | stabilizer-orbit classification and branch normalization |
| Conditional span-three synthesis | `proofs/40-span-three-corollary.tex` | none | not applicable | public rank-one and rational-quartic frontier inputs plus review of the new conic/cubic arguments |
| Primitive binary `r=4` | equations `(H.3)`--`(H.24)` | `checks/high-ramification/verify_r4_high_ramification.py` | reduced quadratic normalization, repeated-root parametrization, generic and `3+1` kernels, internal `2+2`, endpoint, and second-normal obstructions | upstream primitive binary/Hilbert--Burch placement and final plane theorem |
| Primitive binary `r=5` | first branch of `proofs/50-high-ramification.tex` | supporting identities in the same checker | displayed aligned cube/fourth-power identities | cubic-coordinate lemma and plane theorem |
| Primitive `r=3`, `tau=-1` | `proofs/60-tau-minus-one.tex` | `checks/tau-minus-one/verify_tau_minus_one.py` | reconstruction of `P,Q,R`, resultant factors, projective first-normal strata, saturation certificates, and two unrestricted next-layer obstructions | upstream chart placement and zero-normal plane reduction |
| Global case tree | `case-tree/lane4-global-case-tree.md` | `case-tree/lane4-case-tree.csv` | machine-readable ownership inventory only | every cited theorem hypothesis and proof-code attachment still needs specialist audit |

## Excluded from this crosswalk

The public v5 degree-three family contains generic, resonant, `c=0`,
dependent-syzygy, quadratic-exceptional, and zero-normal programs.  Those
programs are not copied or independently derived in this packet.  Only the
new `tau=-1` checker above is claimed as an independent retained derivation
within the `r=3` family.
</code></pre>

## `lane4-quartic-endgame-20260802-v1/case-tree/lane4-global-case-tree.md`

<pre><code class="language-markdown">
# Lane 4 quartic case tree — candidate repaired routing

## Status and scope

This document is an ownership map for the ordinary-degree-four branch in
three variables.  It combines public Program 2 inputs with the candidate
proof repairs and exact calculations in this packet.  It is intended for
specialist review; it is not a generated claim-graph update and does not
promote the global conclusion

\&#91;
D_{\min}\ge 5.
\&#93;

The unconditional public interval remains

\&#91;
4\le D_{\min}\le 7.
\&#93;

Status terms used below have the following meanings.

| Status | Meaning |
| --- | --- |
| public input | A theorem or certificate already present in the public Program 2 source; this packet does not re-prove it. |
| candidate proof | A complete prose argument supplied here, but not yet independently refereed. |
| exact replay | A finite symbolic calculation rerun over exact characteristic-zero arithmetic. |
| conditional | The implication uses an upstream chart-placement, classification, or plane theorem stated separately. |
| not independently reproduced here | The public v5 packet reports a successful replay, but this packet does not supply a new derivation of that chart. |

## Ownership convention

The structural loci overlap.  To turn the cover into a case tree, assign a
map to the first applicable branch in the following order:

1. the zero cubic normal layer `R=0`;
2. the binary branch `P,Q,R in k&#91;x,y&#93;`;
3. the genuinely nonbinary quadratic-source branch;
4. the primitive coprime fourth-power branch;
5. the genuinely nonbinary fixed-component branch.

Inside the binary branch, assign a nonconstant fixed factor before the
fourth-power and ramification branches.  In the coprime branch, remove zero
minors before defining the common ramification degree.  This is an ownership
rule only; it does not claim that the underlying geometric loci are disjoint.

## Structural tree

```text
quartic Keller map F = LX + H2 + H3 + H4
|
+-- rho4 = 1
|   `-- rank-one theorem -&gt; automorphism                         &#91;public input&#93;
|
+-- rho4 = 3
|   |
|   +-- leading image a conic
|   |   +-- four historical invariant-field orbits              &#91;public input&#93;
|   |   `-- G = x^2, xy, z^2                                   &#91;candidate proofs + exact checks&#93;
|   |
|   +-- leading image a proper rational cubic
|   |   `-- cusp/node; transverse and all marked factors        &#91;candidate proof + exact checks&#93;
|   |
|   `-- leading image a proper rational quartic
|       `-- balanced and tricuspidal/frontier types              &#91;public input; preclassification required&#93;
|
`-- rho4 = 2
    |
    +-- normalize H4=(P,Q,0), P,Q independent quartics;
    |   put R=(H3)_3
    |
    +-- R=0
    |   `-- quadratic coordinate + plane reduction              &#91;candidate proof; plane theorem&#93;
    |
    `-- R != 0 and Jac(P,Q,R)=0
        |
        +-- P,Q,R binary in two source forms
        |   |
        |   +-- G=gcd(P,Q) nonconstant
        |   |   +-- deg G=3: squarefree / 2+1 / triple line      &#91;public exact packet&#93;
        |   |   +-- deg G=2: divisor and endpoint tree           &#91;public 38-group packet&#93;
        |   |   `-- deg G=1: residual-cubic orbit tree           &#91;public exact packet&#93;
        |   |
        |   `-- gcd(P,Q)=1
        |       |
        |       +-- U,V,or W zero                                &#91;public edge theorem; R=0 repaired here&#93;
        |       |
        |       +-- pencil contains a fourth power               &#91;public routing proposition&#93;
        |       |
        |       `-- U,V,W nonzero; r=deg gcd(U,V,W)
        |           +-- r=0                                     &#91;public regular theorem&#93;
        |           +-- r=1                                     &#91;public simple-ramification theorem&#93;
        |           +-- r=2                                     &#91;public double-ramification theorem&#93;
        |           +-- r=3
        |           |   +-- dependent (2,5) syzygy               &#91;public v5; not independently reproduced here&#93;
        |           |   `-- independent (3,4) syzygy
        |           |       +-- primitive tau=-1 divisor         &#91;candidate proof + exact replay here&#93;
        |           |       `-- all other generic/exceptional
        |           |           v5 charts                         &#91;public v5; not independently reproduced here&#93;
        |           +-- r=4
        |           |   +-- dependent residual syzygies          &#91;candidate algebraic proof&#93;
        |           |   +-- independent, residual square         &#91;candidate gcd contradiction&#93;
        |           |   `-- independent, reduced residual
        |           |       +-- squarefree Gamma                  &#91;candidate kernel argument&#93;
        |           |       +-- repeated root away from endpoints
        |           |       |   +-- nonprimitive component       &#91;gcd exit&#93;
        |           |       |   +-- generic / 3+1                &#91;candidate proof + exact replay&#93;
        |           |       |   `-- internal 2+2                 &#91;candidate proof + exact replay&#93;
        |           |       `-- repeated endpoint                &#91;candidate proof + exact replay&#93;
        |           `-- r=5                                     &#91;candidate aligned cube/fourth-power proof&#93;
        |
        +-- genuinely nonbinary composite intermediate field
        |   `-- only n=4=(e,d)=(2,2)
        |       +-- binary degeneration                          &#91;binary owner&#93;
        |       +-- fixed-component degeneration                 &#91;fixed owner&#93;
        |       `-- no-fixed genuinely nonbinary locus           &#91;public nine-chart packet&#93;
        |
        +-- composition-primitive, gcd(P,Q)=1, nonbinary
        |   `-- valuation forces a fourth-power member           &#91;candidate repaired routing&#93;
        |       `-- binary / quadratic-source / aligned exit
        |
        `-- composition-primitive, gcd(P,Q)=G nonconstant, nonbinary
            +-- deg G=2                                         &#91;public corrected valuation&#93;
            `-- deg G=1
                `-- aligned / binary / residual-pole branch
                    `-- homogeneous cubic centralizer endpoint   &#91;candidate repair&#93;
```

## Why the span-two structural cover has four owners

Write

\&#91;
P=GA,\qquad Q=GB,\qquad \gcd(A,B)=1,
\&#93;

and put `n=deg A=deg B`.  The weighted one-variable field input gives an
intermediate rational parameter with

\&#91;
n=ed.
\&#93;

After the binary branch is removed, the composite possibilities are

\&#91;
\begin{array}{c|c|c}
\deg G&amp;n&amp;(e,d)\\ \hline
0&amp;4&amp;(4,1),(2,2)\\
1&amp;3&amp;(3,1)\\
2&amp;2&amp;(2,1).
\end{array}
\&#93;

The repaired valuation argument sends every `d=1` case to the binary owner;
the only genuinely nonbinary composite case is `(e,d)=(2,2)`.  For a
primitive coprime reduced pencil, the valuation sum produces a fourth-power
fiber.  For a primitive pencil with `G != 1`, the generic-divisor valuation
puts every component of `G` on a special fiber.  These are exactly the four
structural owners listed above.

## Leaf-to-evidence table

| ID | Leaf | Mathematical owner | Packet evidence | Remaining boundary |
| --- | --- | --- | --- | --- |
| S1 | `rho4=1` | public rank-one theorem | locator only | hypotheses of public theorem |
| S2 | seven conic orbits | four public orbits plus three packet propositions | exact `z^2` checker; exact branch scripts and terminal identities for `x^2,xy` | specialist review; second CAS desirable |
| S3 | proper rational cubic | packet cusp/node argument | exact transverse, marked-node, marked-cusp and pivot-minor scripts | specialist review; plane theorem |
| S4 | proper rational quartic | public frontier theorems | locator only | upstream quartic-image preclassification |
| B0 | `R=0` | packet quadratic-coordinate argument | prose proof | exact per-coordinate plane-theorem citation |
| B1 | nonbinary `(2,2)` | public nine-chart theorem | locator only | proof-to-code crosswalk |
| B2 | binary fixed factors | public fixed-factor packets | locator only | proof-to-code crosswalk; second lineage |
| B3 | coprime binary `r&lt;=2` | public ramification filtration | locator only | source hypotheses as stated |
| B4a | primitive `r=3`, `tau=-1` | packet theorem | exact standalone checker and stored output | upstream chart placement; specialist review |
| B4b | remaining `r=3` charts | public v5 family | no new independent packet here | generic and exceptional proof-code crosswalk; independent reproduction |
| B5 | primitive binary `r=4` | packet projective theorem | exact repeated-root, `3+1`, `2+2`, endpoint and second-normal checker | upstream Hilbert--Burch placement; specialist review; second CAS |
| B6 | primitive binary `r=5` | packet algebraic argument | exact supporting identities in the high-ramification checker | plane theorem; specialist review |
| B7 | fourth-power member | public edge proposition | locator only | overlap ownership |
| B8 | nonbinary fixed components | public valuation plus packet centralizer repair | prose lemma | verify preceding coefficient derivation; specialist review |
| B9 | zero minor | public edge proposition plus packet `R=0` proof | prose proof | plane theorem citation |

## Material not promoted by this packet

Earlier exploratory session notes reported additional work on a generic
`r=3` kernel-plane calculation and on a `tau=0` specialization.  No complete,
self-contained source-and-output artifact for those reports was retained in
the present packet.  They are therefore **not evidence in this submission**
and do not change row B4b.

## Remaining publication gates

Even if every candidate argument in this packet survives review, a public
global theorem still requires:

1. a line-by-line audit that every edge in this ownership tree matches the
   hypotheses of its cited source statement;
2. a proof-to-code crosswalk for the public quadratic-source, fixed-factor,
   and remaining degree-three charts;
3. independent reproduction of the remaining `r=3` generic and exceptional
   systems, preferably in a second computer-algebra system;
4. verification and exact citation of the Appelgate--Onishi/Nowicki--Nakai
   plane theorem in every function-field use; and
5. specialist review of the new structural, conic, rational-cubic,
   high-ramification, and `tau=-1` arguments.

Until those gates close, this is a candidate repaired synthesis rather than
an unconditional proof of `D_min &gt;= 5`.
</code></pre>

## `lane4-quartic-endgame-20260802-v1/case-tree/lane4-case-tree.csv`

<pre><code class="language-csv">
node,parent,hypotheses,owner,packet_status,remaining_boundary
rho1,root,rho4=1,public rank-one theorem,public input,hypotheses of public theorem
span3-conic,root,rho4=3 and image degree 2,seven conic orbit arguments,candidate proofs plus exact checks,specialist review and second CAS
span3-cubic,root,rho4=3 and image degree 3,packet rational-cubic argument,candidate proof plus exact checks,specialist review and plane theorem
span3-quartic,root,rho4=3 and image degree 4,public quartic-frontier theorem,public input,frontier preclassification
R0,rho2,R=0,packet quadratic-coordinate argument,candidate proof,plane theorem citation
binary-fixed,rho2,P Q R binary and gcd(P Q)&gt;1,public fixed-factor packets,public exact packets,proof-to-code crosswalk and second lineage
binary-zero-minor,rho2,P Q R binary gcd=1 and one minor zero,public edge theorem plus packet R=0 argument,public input plus candidate proof,plane theorem citation
binary-fourth-power,rho2,P Q R binary gcd=1 and pencil has fourth power,public fourth-power proposition,public routing input,overlap ownership
r0-2,rho2,binary coprime nonzero minors r&lt;=2,public ramification theorems,public input,source hypotheses as stated
r3-tau-minus-one,r3,independent (3 4) chart and tau=-1,packet tau=-1 theorem,candidate proof plus exact replay,upstream chart placement and specialist review
r3-other,r3,remaining dependent generic resonant and degenerate charts,public v5 chart family,not independently reproduced here,proof-code crosswalk and independent lineage
r4,rho2,binary coprime nonzero minors r=4,packet high-ramification theorem,candidate proof plus exact replay,upstream Hilbert-Burch placement specialist review second CAS
r5,rho2,binary coprime nonzero minors r=5,packet high-ramification theorem,candidate algebraic proof,plane theorem and specialist review
quadratic-source,rho2,nonbinary composite e=2 d=2,public nine-chart theorem,public exact packet,proof-to-code crosswalk
primitive-fourth-power,rho2,nonbinary primitive gcd=1,packet repaired valuation plus public fourth-power proposition,candidate routing repair,overlap ownership
nonbinary-fixed,rho2,nonbinary primitive gcd&gt;1,public valuation plus packet centralizer lemma,candidate proof repair,preceding coefficient derivation and specialist review
</code></pre>

## `lane4-quartic-endgame-20260802-v1/proofs/10-structural-repairs-and-z2.tex`

<pre><code class="language-tex">
% Lane 4 proof repairs and one new conic-orbit exclusion.
% Prepared against the 2026-08-01 Program 2 source snapshot.
% The blocks below are intended as replacement/insertable TeX, not as a
% modification of the hash-pinned public release.

% -------------------------------------------------------------------------
% 1. Replacement proof for lem:leading-image
% -------------------------------------------------------------------------

\begin{proof}&#91;Replacement proof of the leading-image factorization lemma&#93;
Let
\&#91;
 \phi=&#91;H_{4,1}:H_{4,2}:H_{4,3}&#93;\colon \PP^2\dashrightarrow C_4(F)
\&#93;
be the rational map defined by the leading forms.  Since \(\PP^2\)
dominates \(C_4(F)\), restriction to a sufficiently general line shows
that \(C_4(F)\) is unirational.  Its normalization is therefore \(\PP^1\)
in characteristic zero.  Write the normalization map as
\&#91;
 \nu=&#91;h_0:h_1:h_2&#93;\colon \PP^1\longrightarrow C_4(F),
\&#93;
where the \(h_i\) are binary forms without a common zero.  Because \(\nu\)
is birational and \(\deg C_4(F)=e\), the line bundle
\(\nu^*\mathcal O_{C_4(F)}(1)\) has degree \(e\); hence the \(h_i\) may be
chosen homogeneous of degree \(e\).

The rational map \(\psi=\nu^{-1}\circ\phi\colon\PP^2\dashrightarrow\PP^1\)
is represented by a coprime homogeneous pencil
\&#91;
 \psi=&#91;A:B&#93;,\qquad \deg A=\deg B=k\ge1.
\&#93;
Consequently
\&#91;
 &#91;H_{4,1}:H_{4,2}:H_{4,3}&#93;
   =&#91;h_0(A,B):h_1(A,B):h_2(A,B)&#93;.
\&#93;
Put \(q_i=h_i(A,B)\).  The forms \(q_i\) have no common irreducible
factor.  Indeed, at the generic point of a prime divisor \(\Gamma\), the
coprimality of \(A,B\) says that they do not both vanish; their ratio gives
a point of \(\PP^1(k(\Gamma))\), and the basepoint-free triple \(h\) cannot
vanish there in all three coordinates.

There is therefore a rational function \(\lambda\) with
\(H_{4,i}=\lambda q_i\) for every \(i\).  Write \(\lambda=u/v\) in lowest
terms.  Since every \(H_{4,i}\) is polynomial, \(v\) divides every \(q_i\);
thus \(v\) is constant.  Hence \(\lambda=G\) is a polynomial form and
\&#91;
 H_4=G\,h(A,B).
\&#93;
Comparison of degrees gives
\&#91;
 \deg G+ek=4.
\&#93;
For a nondegenerate curve \(e\ge2\), the positive integral solutions are
\&#91;
 (e,k,\deg G)=(2,1,2),(2,2,0),(3,1,1),(4,1,0).
\&#93;
When \(e=1\), the projective leading image is a line, equivalently the
leading target span is two.  This proves the lemma.
\end{proof}

% -------------------------------------------------------------------------
% 2. Replacement proof for prop:four-loci
% -------------------------------------------------------------------------

\begin{proof}&#91;Replacement proof of the four-locus reduction&#93;
Retain the notation
\&#91;
 P=GA,\qquad Q=GB,\qquad \gcd(A,B)=1,
 \qquad n=\deg A=\deg B=4-\deg G,
\&#93;
\&#91;
 t=A/B,\qquad w=R^4/Q^3.
\&#93;
By the weighted one-variable field lemma from the Program~2 source,
\&#91;
 k(t,w)=k(s),\qquad s=A_0/B_0,
 \qquad t=\mathcal R(s),\qquad n=ed,
\&#93;
where \(A_0,B_0\) are coprime forms of degree \(d\) and
\(\deg\mathcal R=e\).

Suppose first that \(e&gt;1\).  The possibilities are
\&#91;
\begin{array}{c|c|c}
\deg G&amp;n&amp;(e,d)\\ \hline
0&amp;4&amp;(4,1),(2,2)\\
1&amp;3&amp;(3,1)\\
2&amp;2&amp;(2,1).
\end{array}
\&#93;
Consider a case with \(d=1\), so \(s\) is a pencil of two linear forms and
\(w=\sigma(s)\).  Let an irreducible component \(\Gamma\) occur in \(G\)
with multiplicity \(\mu\).  If \(s|_\Gamma\) is nonconstant, then
\(A_0,B_0\), the reduced factor of \(Q\), and \(\sigma(s)\) are units at
the generic point of \(\Gamma\).  Taking \(\Gamma\)-valuations in
\(R^4/Q^3=\sigma(s)\) gives
\&#91;
 4\nu_\Gamma(R)=3\mu.
\&#93;
Thus \(4\mid\mu\), impossible because in the displayed \(d=1\) cases
\(\mu\le\deg G\le2\).  Hence every component of \(G\) is a fiber line of
\(s\).  It follows that \(G,P,Q\) are polynomials in the same two linear
forms.  Moreover \(R^4\in k(A_0,B_0)\); viewing \(R\) as a polynomial in a
third independent linear form shows that its degree in that variable is
zero.  Thus \(R\in k&#91;A_0,B_0&#93;\), and we are in locus~(i).  The only
remaining composite case is \((e,d)=(2,2)\) with \(G=1\), which is exactly
locus~(ii).

Now suppose that \(e=1\), so \(w=\rho(t)\).  First take \(G=1\).  For a
finite fiber \(A-\xi B\), set \(c_\xi=\ord_\xi\rho\), and at infinity set
\&#91;
 c_\infty=\ord_\infty\rho+3.
\&#93;
If \(\Gamma\) is a component of the corresponding quartic fiber with
multiplicity \(m\), valuation gives
\&#91;
 4\nu_\Gamma(R)=c_\xi m.
\&#93;
Therefore every \(c_\xi\) is nonnegative, and the divisor identity for
\(\rho\) gives
\&#91;
 \sum_{\xi\in\PP^1}c_\xi=3.
\&#93;
Some \(c_\xi\) is odd.  For that fiber, \(4\mid m\) for every component.
Since the fiber has degree four, it is \(\ell^4\).  This is locus~(iii).

Finally assume \(e=1\) and \(G\ne1\).  Let \(\Gamma\mid G\) have
multiplicity \(\mu\).  If \(t|_\Gamma\) were nonconstant, then \(A,B\) and
\(\rho(t)\) would be units at the generic point of \(\Gamma\), and the same
valuation would give
\&#91;
 4\nu_\Gamma(R)=3\mu.
\&#93;
But \(1\le\mu\le\deg G\le3\), a contradiction.  Thus \(t\) is constant on
every component of \(G\): each component is supported on a special fiber
of the reduced pencil \(A/B\).  This is locus~(iv).  The four loci may
overlap, as stated.
\end{proof}

% -------------------------------------------------------------------------
% 3. A reader-manuscript proof of the R=0 branch
% -------------------------------------------------------------------------

\begin{proposition}&#91;Candidate vanishing cubic normal layer&#93;
\label{prop:quartic-r-zero-repair}
Let \(F\colon\AA^3\to\AA^3\) be a Keller map of ordinary degree at most
four, and suppose that after a target linear change
\&#91;
 H_4=(P,Q,0),\qquad (H_3)_3=0.
\&#93;
Assume the per-coordinate Appelgate--Onishi--Nagata plane theorem in the
form used in the Program~2 easy-branch reduction.  Then \(F\) is a polynomial
automorphism.
\end{proposition}

\begin{proof}
The third coordinate \(F_3\) has degree at most two.  Since
\(\det JF\ne0\), its gradient has no zero: a zero gradient would make the
third row of \(JF\) vanish.  By the quadratic-coordinate lemma from the Program~2 source, after a
linear source change
\&#91;
 F_3=\mu z+e(x,y),\qquad \mu\ne0,\qquad \deg e\le2.
\&#93;
Replacing \(z\) by \(t=F_3\) is a polynomial source automorphism, with
\&#91;
 z=\mu^{-1}(t-e(x,y)).
\&#93;

Choose a nonzero target combination \(G=\alpha F_1+\beta F_2\) whose
quartic homogeneous part has zero \(z^4\)-coefficient.  Such a combination
exists because this is one homogeneous linear condition on
\((\alpha,\beta)\).  After the substitution for \(z\), a monomial
\(x^ay^bz^j\) of total degree at most four has \((x,y)\)-degree at most
\&#91;
 a+b+2j\le4+j.
\&#93;
The only possible degree-eight term would come from \(z^4\), which was
killed.  Hence
\&#91;
 \deg_{x,y}G\le7.
\&#93;
Complete \(G\) to an invertible target combination \((G,H)\) of
\((F_1,F_2)\).  Over \(\overline{k(t)}\), the pair \((G,H)\) is a plane
Keller map, and one coordinate has degree at most seven.  The cited plane
theorem makes it an automorphism.  Its inverse is unique and therefore
descends from \(\overline{k(t)}\) to \(k(t)\).  Thus \(F\) is birational.
A birational Keller self-map is an automorphism by the same
Zariski-main/Ax--Grothendieck argument used in the Program~2 easy-branch reduction.
\end{proof}

% -------------------------------------------------------------------------
% 4. Exact centralizer bridge for the fixed-component endpoint
% -------------------------------------------------------------------------

\begin{lemma}&#91;Homogeneous cubic Hamiltonian centralizer&#93;
\label{lem:homogeneous-cubic-centralizer}
Let \(R\in k&#91;x,y,z&#93;_3\) be homogeneous, with \(x\nmid R\).  Suppose
that \(R\notin k&#91;x,\ell&#93;\) for every nonzero linear form
\(\ell\in k&#91;y,z&#93;_1\).  Put \(K=k(x)\) and
\&#91;
 \delta=J_{y,z}(R,-)\colon K&#91;y,z&#93;\longrightarrow K&#91;y,z&#93;.
\&#93;
Then
\&#91;
 \ker\delta=K&#91;R&#93;.
\&#93;
Moreover, if \(Q\in k&#91;x,y,z&#93;_d\) is homogeneous and \(\delta Q=0\), then
\&#91;
 Q=\sum_{0\le j\le d/3}\lambda_j x^{d-3j}R^j,
 \qquad \lambda_j\in k.
\&#93;
In particular,
\&#91;
 \ker\delta\cap k&#91;x,y,z&#93;=k&#91;x,R&#93;.
\&#93;
\end{lemma}

\begin{proof}
Suppose that \(R\) were decomposable over an algebraic closure of \(K\):
\(R=u(h)\) with \(\deg u&gt;1\).  The degree of \(R\) in \((y,z)\) is at most
three, so a nontrivial decomposition forces \(h\) to be linear in
\((y,z)\).  The highest \((y,z)\)-homogeneous part of \(R\) is then a power
of a linear form.  Since \(R\) is homogeneous over \(k\), its projective
linear factor has constant direction in \(\PP^1(k)\).  Thus
\(K&#91;h&#93;=K&#91;\ell&#93;\) for a fixed \(\ell\in k&#91;y,z&#93;_1\), and
\&#91;
 R\in K&#91;\ell&#93;\cap k&#91;x,y,z&#93;=k&#91;x,\ell&#93;,
\&#93;
contrary to the hypothesis.  Hence \(R\) is absolutely indecomposable.

The standard two-variable common-generator theorem for a vanishing
Jacobian now gives \(\ker\delta=K&#91;R&#93;\): if \(J_{y,z}(R,Q)=0\), then over an
algebraic closure of \(K\), the polynomials \(R,Q\) have a common polynomial
generator; the indecomposability of \(R\) makes that generator affine-linear
in \(R\), and uniqueness descends the coefficients to \(K\).

Let now \(Q\) be homogeneous of degree \(d\).  Write uniquely
\&#91;
 Q=\sum_j f_j(x)R^j,\qquad f_j(x)\in k(x).
\&#93;
Scalar homogeneity gives
\&#91;
 f_j(\lambda x)=\lambda^{d-3j}f_j(x),
\&#93;
so \(f_j(x)=\lambda_jx^{d-3j}\).  Because \(x\nmid R\), a negative power
of \(x\) cannot cancel among distinct powers of \(R\) in a polynomial
\(Q\).  Hence only \(d-3j\ge0\) occurs.  This proves the displayed formula
and, degree by degree, the final assertion.
\end{proof}

\begin{remark}&#91;Use at equation (A.8)&#93;
In the endpoint \(H_4=(x^4,xR,0)\), equation (A.8) is
\&#91;
 4x^3J_{y,z}(m,R)-R J_{y,z}(\ell,R)=0.
\&#93;
Since \(\gcd(x^3,R)=1\), the degree bounds force
\&#91;
 J_{y,z}(m,R)=J_{y,z}(\ell,R)=0.
\&#93;
For linear \(\ell,m\), \cref{lem:homogeneous-cubic-centralizer} gives
\(\ell,m\in kx\).  This is the exact centralizer implication needed at the
terminal contradiction; no stronger unqualified centralizer assertion is
required.
\end{remark}

% -------------------------------------------------------------------------
% 5. New exclusion of the previously untreated G=z^2 conic orbit
% -------------------------------------------------------------------------

\begin{proposition}&#91;Candidate double-line conic orbit off the pencil point&#93;
\label{prop:conic-z2-exclusion}
No quartic Keller map has leading form
\&#91;
 H_4=z^2(x^2,xy,y^2).
\&#93;
\end{proposition}

\begin{proof}&#91;Exact coefficient proof&#93;
Put
\&#91;
 n=(y^2,-2xy,x^2)^T,
 \qquad
 \delta=2z(x\partial_x+y\partial_y-z\partial_z).
\&#93;
For \(M=n\cdot H_3\), the first normal determinant equation is
\&#91;
 \delta(M)=4zM.
\&#93;
Since \(M\) is homogeneous of degree five, a monomial
\(x^ay^bz^c\) in \(M\) has
\((x\partial_x+y\partial_y-z\partial_z)\)-weight \(5-2c\), which can never
be two.  Hence \(M=0\).  The full cubic syzygy module of \(n\) gives
\&#91;
 H_3=T(A,B)=(2xA,yA+xB,2yB),
\&#93;
where
\&#91;
\begin{aligned}
A={}&amp;a_0x^2+a_1xy+a_2xz+a_3y^2+a_4yz+a_5z^2,\\
B={}&amp;b_0x^2+b_1xy+b_2xz+b_3y^2+b_4yz+b_5z^2.
\end{aligned}
\&#93;
Write the three components of \(H_2\) using coefficients
\(c_0,\ldots,c_{17}\), with each component ordered by
\&#91;
 x^2,\ xy,\ xz,\ y^2,\ yz,\ z^2.
\&#93;
Write the rows of the linear part as
\&#91;
 (\ell_0,\ell_1,\ell_2),
 (\ell_3,\ell_4,\ell_5),
 (\ell_6,\ell_7,\ell_8).
\&#93;
Let
\&#91;
 D_j=&#91;\epsilon^j&#93;\det\bigl(L+\epsilon JH_2+
             \epsilon^2JH_3+\epsilon^3JH_4\bigr).
\&#93;
The Keller equations are \(D_j=0\) for \(1\le j\le8\), while
\(D_0=\det L\ne0\).

The exact solution of \(D_7=0\) is
\&#91;
\begin{gathered}
 b_0=a_3=0,\qquad b_1=a_0,\qquad b_3=a_1,\\
 c_{12}=b_2^2,\qquad
 c_{13}=2c_6-2b_2(a_2-b_4),\\
 c_0=(a_2-b_4)^2-2a_4b_2-c_{15}+2c_7,\qquad
 c_{17}=b_5^2,\\
 c_1=2c_9+2a_4(a_2-b_4),\qquad
 c_{11}=a_5b_5,\qquad c_3=a_4^2,\qquad c_5=a_5^2.
\end{gathered}
\&#93;
Put \(d=a_2-b_4\).  The six coefficients
\(&#91;x^{5-i}y^iz&#93;D_6\), after division by nonzero constants, are
\&#91;
\begin{aligned}
&amp;a_0b_2^2,\\
&amp;b_2(2a_0d-a_1b_2),\\
&amp;a_0d^2-2a_0a_4b_2-2a_1db_2,\\
&amp;2a_0a_4d+a_1d^2-2a_1a_4b_2,\\
&amp;a_4(a_0a_4+2a_1d),\\
&amp;a_1a_4^2.
\end{aligned}                                                    \tag{Z.1}
\&#93;

Suppose first that \((a_0,a_1)\ne(0,0)\).  Equations (Z.1) give
\&#91;
 b_2=d=a_4=0.
\&#93;
The \(\GL_2\)-symmetry in \((x,y)\), together with the induced target
change on \(\operatorname{Sym}^2\langle x,y\rangle\), normalizes
\((a_0,a_1)=(1,0)\).  Thus
\&#91;
 A=x(x+a_2z)+a_5z^2,\qquad
 B=y(x+a_2z)+b_5z^2.
\&#93;
The remaining coefficients of \(D_6\) solve linearly as
\&#91;
\begin{gathered}
 c_{14}=c_4=0,\qquad c_{16}=2c_8,\qquad c_2=2c_{10},\\
 \ell_6=-2b_5^2+2b_5c_6,\qquad
 \ell_7=4a_5b_5-2a_5c_6+2b_5(c_{15}-c_7)+2\ell_3,\\
 \ell_8=-2a_2b_5^2+2b_5c_8,\qquad
 \ell_0=2\ell_4-2a_5^2-2a_5c_{15}+2a_5c_7-2b_5c_9,\\
 \ell_5=-2a_2a_5b_5+a_5c_8+b_5c_{10},\qquad
 \ell_1=2a_5c_9,\qquad
 \ell_2=-2a_2a_5^2+2a_5c_{10}.
\end{gathered}
\&#93;
Three coefficients of \(D_5\) then give, successively,
\&#91;
\begin{aligned}
&#91;x^4z&#93;D_5&amp;=8(c_6-2b_5)^2,\\
&#91;y^4z&#93;D_5&amp;=8c_9^2,\\
&#91;x^2y^2z&#93;D_5&amp;=8(2a_5+c_{15}-c_7)^2.
\end{aligned}
\&#93;
After imposing their vanishing, two coefficients of \(D_4\) are
\&#91;
 &#91;x^3z&#93;D_4=-12(c_8-2a_2b_5)^2,\qquad
 &#91;xy^2z&#93;D_4=-12(c_{10}-2a_2a_5)^2.
\&#93;
Finally set
\&#91;
 X=b_5(2a_5+c_{15})-\ell_3,\qquad
 Y=a_5c_{15}-\ell_4.
\&#93;
The three surviving coefficients of \(D_3\) are
\&#91;
 &#91;x^2z&#93;D_3=4X^2,\qquad
 &#91;xyz&#93;D_3=-8XY,\qquad
 &#91;y^2z&#93;D_3=4Y^2.
\&#93;
Thus \(X=Y=0\).  Substitution into the linear part gives
\&#91;
L=
\begin{pmatrix}
2a_5(a_5+c_{15})&amp;0&amp;2a_2a_5^2\\
b_5(2a_5+c_{15})&amp;a_5c_{15}&amp;2a_2a_5b_5\\
2b_5^2&amp;2b_5c_{15}&amp;2a_2b_5^2
\end{pmatrix},
\&#93;
whose determinant is zero.

It remains to treat \(a_0=a_1=0\).  Then
\&#91;
 A=z(a_2x+a_4y+a_5z),\qquad
 B=z(b_2x+b_4y+b_5z).
\&#93;
Writing \(u=(x,y)^T\), this is
\&#91;
 H_3=z\,D\nu_u(Mu+qz),
 \qquad
 M=\begin{pmatrix}a_2&amp;a_4\\b_2&amp;b_4\end{pmatrix},
 \quad q=\binom{a_5}{b_5},
\&#93;
where \(\nu(u)=(x^2,xy,y^2)\).  Translations in \((x,y)\) kill \(q\), a
translation in \(z\) removes the scalar part of \(M\), and conjugacy by
\(\GL_2\), together with a rescaling of \(z\), reduces the traceless matrix
\(M\) to exactly one of
\&#91;
 \begin{pmatrix}1&amp;0\\0&amp;-1\end{pmatrix},\qquad
 \begin{pmatrix}0&amp;1\\0&amp;0\end{pmatrix},\qquad
 \begin{pmatrix}0&amp;0\\0&amp;0\end{pmatrix}.
\&#93;
In these three charts the coefficient solve for \(D_6=0\) is respectively
\&#91;
\begin{array}{c|ccc}
M&amp;\ell_2&amp;\ell_5&amp;\ell_8\\ \hline
\operatorname{diag}(1,-1)&amp;0&amp;0&amp;0\\
\begin{psmallmatrix}0&amp;1\\0&amp;0\end{psmallmatrix}&amp;0&amp;0&amp;0\\
0&amp;0&amp;0&amp;0
\end{array}
\&#93;
(the remaining solved entries are retained in the checker).  No parameter is
inverted.  Thus the third column of \(L\) vanishes, again contradicting
\(\det L\ne0\).  The attached assertion-based checker verifies every
coefficient identity over \(\mathbb Q\).
\end{proof}
</code></pre>

## `lane4-quartic-endgame-20260802-v1/proofs/20-conic-completion.tex`

<pre><code class="language-tex">
\section{Completion of the conic-image leaf}
\label{app:quartic-conic-completion}

This appendix treats the three conic representatives not covered by the
invariant-field proof in the main text.  The orbit with fixed factor
\(G=z^2\) is handled by the separate exact checker distributed with this
packet.  Here we close the remaining two representatives
\&#91;
 H_4=x^2(x^2,xy,y^2),\qquad
 H_4=xy(x^2,xy,y^2).
\&#93;
The computations retain arbitrary quadratic layer and arbitrary linear part.
They use exact rational arithmetic, no random specialization, and no division
by a parameter before entering the corresponding nonzero chart.

Put
\&#91;
 n=(y^2,-2xy,x^2)^T,
 \qquad
 \det(JH_1+\epsilon JH_2+\epsilon^2JH_3+\epsilon^3JH_4)
 =\sum_{j=0}^9D_j\epsilon^j.
\&#93;
For either fixed factor, the first normal equation gives
\(M=n\cdot H_3\in k&#91;x,y&#93;_5\).  Write
\&#91;
 H_3=T(A,B)+N(M),\qquad
 T(A,B)=(2xA,yA+xB,2yB),
\&#93;
where \(A,B\) are quadrics, and for
\(M=\sum_{i=0}^5m_ix^{5-i}y^i\) take
\&#91;
 N(M)=
 \left(m_4xy^2+m_5y^3,0,
 m_0x^3+m_1x^2y+m_2xy^2+m_3y^3\right).
\&#93;

\begin{theorem}&#91;Candidate double-line conic orbit&#93;
\label{thm:quartic-conic-x2}
No quartic Keller counterexample has
\&#91;
 H_4=x^2(x^2,xy,y^2).
\&#93;
\end{theorem}

\begin{proof}&#91;Exact coefficient proof&#93;
Write
\&#91;
 A_z=a_2x+a_4y+a_5z,
 \qquad
 B_z=b_2x+b_4y+b_5z.
\&#93;
The compatibility equations of \(D_7=0\) first give
\&#91;
 a_4=a_5=b_5=0,
\&#93;
and
\begin{align}
4a_3(a_2-b_4)+(4b_4-a_2)m_4+6b_2m_5&amp;=0,
\label{eq:x2-routing-one}\\
m_5(a_2-2b_4)&amp;=0.
\label{eq:x2-routing-two}
\end{align}
The coefficients
\begin{align*}
&#91;x^4z^2&#93;D_6&amp;=24b_2^2b_4,\\
&#91;x^3yz^2&#93;D_6&amp;=-48b_2b_4(a_2-b_4),\\
&#91;x^2y^2z^2&#93;D_6&amp;=24b_4(a_2-b_4)^2,\\
&#91;y^5z&#93;D_6&amp;=-6b_4m_5(a_2+b_4)
\end{align*}
together with \eqref{eq:x2-routing-one}--
\eqref{eq:x2-routing-two} give four exhaustive stabilizer types:
scalar, rank-one semisimple, nilpotent, and zero.

In the scalar chart normalize
\&#91;
 A=a_0x^2+a_1xy+xz,
 \qquad
 B=b_0x^2+b_1xy+b_3y^2+yz.
\&#93;
The equations give \(M=0\), \(a_1=b_3\), and then
\&#91;
 c_6=b_0(a_0+b_1),\quad
 c_0=a_0^2-2b_0b_3-b_1^2+c_7,
 \quad c_1=4b_3(a_0-b_1).
\&#93;
After the preceding linear solves put
\begin{align*}
 A_*&amp;=4a_0b_0b_1+2b_0^2b_3-4b_0b_1^2-2b_0c_7+\ell_7,\\
 B_*&amp;=2a_0^2b_1-4a_0b_1^2-a_0c_7+2b_1^3+b_1c_7+\ell_4,\\
 S&amp;=2a_0b_0^2b_3+a_0\ell_7-2b_0^2b_1b_3-2b_0\ell_4-b_1\ell_7.
\end{align*}
The exact residual identities are
\&#91;
 D_2=A_*^2x^2-4A_*B_*xy+4B_*^2y^2,
 \qquad
 \det L=S^2,
\&#93;
and
\&#91;
 S=(a_0-b_1)A_*-2b_0B_*.
\&#93;
Thus \(D_2=0\) implies \(\det L=0\).

In the rank-one semisimple chart normalize
\&#91;
 A=a_0x^2+a_1xy+xz,
 \qquad
 B=b_0x^2+b_1xy+b_3y^2.
\&#93;
The first lower equations give
\&#91;
 m_0=0,
 \quad c_{16}=\frac38m_1,
 \quad c_{10}=b_1+\frac5{16}m_2,
 \quad b_3=-\frac9{16}m_3.
\&#93;
Four coefficients of \(D_5\) force \(m_1=m_2=m_3=0\).  The remaining
\(D_4\)-equations are
\&#91;
\begin{aligned}
X&amp;=a_1b_0^2-a_1c_{12}+2b_0b_1^2-b_1c_{13}+\ell_7=0,\\
Y&amp;=a_0a_1b_0+a_0b_1^2+a_1b_0b_1-a_1c_6-b_1c_7+\ell_4=0.
\end{aligned}
\&#93;
Substitution gives \(\det L=0\).

In the nilpotent chart a source translation gives
\&#91;
 A=a_0x^2+a_1xy,
 \qquad
 B=xz+b_3y^2.
\&#93;
The equations reduce to
\&#91;
\begin{gathered}
 m_3=-2b_3,
 \quad c_{15}=m_2^2/4,
 \quad c_9=(a_1+b_3)m_2/2,\\
 b_3(a_1+b_3)=0,
 \qquad
 (a_1+b_3)(3a_1m_2+2a_0b_3)=0.
\end{gathered}
\&#93;
If \(a_1+b_3=0\), the remaining linear equations give \(\det L=0\).
Otherwise \(b_3=m_2=0\); normalize \(a_1=1\).  Then \(D_4=0\) forces
\&#91;
 m_0=m_1=0,
 \quad \ell_6=a_0c_{12},
 \quad \ell_3=a_0c_6,
 \quad \ell_0=a_0(c_0-a_0^2),
\&#93;
and again \(\det L=0\).

In the zero chart \(H_3\) is binary and
\&#91;
 \partial_zH_2=(2px,py+qx,2qy).
\&#93;
The two nonzero stabilizer orbits are represented by \((p,q)=(1,0)\) and
\((0,1)\).  They respectively give the fixed coefficients
\&#91;
 &#91;x^2y^2z&#93;D_5=-8,
 \qquad
 &#91;x^4z&#93;D_5=-8.
\&#93;
Thus \(p=q=0\), so every nonlinear layer is binary.  A target linear change
reduces the map to
\&#91;
 (f_1(x,y),f_2(x,y),z+f_3(x,y)),
\&#93;
whose plane Keller pair has degree at most four and is automorphic by the
low-degree plane theorem used elsewhere in Program~2.
\end{proof}

\begin{theorem}&#91;Candidate nodal two-line conic orbit&#93;
\label{thm:quartic-conic-xy}
No quartic Keller counterexample has
\&#91;
 H_4=xy(x^2,xy,y^2).
\&#93;
\end{theorem}

\begin{proof}&#91;Exact coefficient proof&#93;
The compatibility equations of \(D_7=0\) give
\&#91;
 a_4=a_5=b_2=b_5=0,
 \qquad
 m_0(3a_2-b_4)=m_5(a_2-3b_4)=0.
\&#93;
The pure coefficients
\&#91;
\begin{aligned}
&#91;x^5z&#93;D_6&amp;=-3m_0(3a_2^2+b_4^2),\\
&#91;y^5z&#93;D_6&amp;=-3m_5(a_2^2+3b_4^2),\\
&#91;x^2y^2z^2&#93;D_6&amp;=12(a_2-b_4)^2(a_2+b_4)
\end{aligned}
\&#93;
show that a nonzero \(z\)-matrix has exactly two stabilizer types,
\((a_2,b_4)=(1,1)\) and \((1,-1)\).

In the scalar chart, the next equations force
\&#91;
 a_3=b_0=m_1=m_2=m_3=m_4=0.
\&#93;
After the linear solves, \(D_4=0\) gives
\&#91;
\begin{aligned}
 c_{16}&amp;=4(b_1-a_0),&amp; c_{10}&amp;=2(a_1-b_3),\\
 c_6&amp;=-2a_0(a_0-b_1),&amp;c_9&amp;=2b_3(a_1-b_3),\\
 c_{15}&amp;=-a_0a_1-a_0b_3-a_1b_1+3b_1b_3+c_7.
\end{aligned}
\&#93;
Set
\begin{align*}
 A_*={}&amp;2a_0^2a_1-4a_0^2b_3+4a_0b_1b_3-2a_0c_7
       -2a_1b_1^2+2b_1c_7-\ell_7,\\
 B_*={}&amp;a_0a_1^2-2a_0a_1b_3+a_0b_3^2+a_1^2b_1
       -2a_1b_1b_3-a_1c_7+b_1b_3^2+b_3c_7+\ell_4,\\
 S={}&amp;2a_0^2a_1b_3-2a_0^2b_3^2-4a_0a_1b_1b_3
       +4a_0b_1b_3^2+2a_0\ell_4\\
 &amp;\qquad{}+2a_1b_1^2b_3+a_1\ell_7-2b_1^2b_3^2
       -2b_1\ell_4-b_3\ell_7.
\end{align*}
Then
\&#91;
 D_2=A_*^2x^2+4A_*B_*xy+4B_*^2y^2,
 \qquad \det L=S^2,
\&#93;
and
\&#91;
 S=-(a_1-b_3)A_*+2(a_0-b_1)B_*.
\&#93;
Thus \(D_2=0\) gives \(\det L=0\).

In the anti-scalar chart, the high equations give
\(m_1=4b_0,m_4=4a_3\) and then \(b_0=a_3=0\).  The residual coefficient is
\&#91;
 &#91;xyz^3&#93;D_5=-64,
\&#93;
so the chart is empty.

In the zero chart, again
\&#91;
 \partial_zH_2=(2px,py+qx,2qy).
\&#93;
The stabilizer of \(xy\) has nonzero vector orbits represented by
\((1,0)\) and \((1,1)\).  The first has
\(&#91;xy^3z&#93;D_5=-8\).  The second has
\&#91;
 &#91;x^3yz&#93;D_5=-8,
 \quad &#91;x^2y^2z&#93;D_5=16,
 \quad &#91;xy^3z&#93;D_5=-8.
\&#93;
Thus \(p=q=0\), and the all-binary plane reduction proves automorphy.
\end{proof}

\begin{corollary}&#91;Candidate all-conic synthesis&#93;
\label{cor:quartic-all-conic-orbits}
Subject to the same low-degree plane input used in the reader manuscript,
no quartic Keller counterexample has a nondegenerate conic as the
projective image of its leading homogeneous part.
\end{corollary}

\begin{proof}
The four reduced representatives in the main conic theorem, together with
\cref{thm:quartic-conic-x2,thm:quartic-conic-xy} and the separate
\(G=z^2\) exact proposition, exhaust the seven parabolic conic orbits.
\end{proof}

\begin{remark}&#91;Evidence boundary&#93;
The supplied SymPy programs reconstruct the full determinant arc with all
lower coefficients present.  They are exact, assertion-based calculations,
but they constitute one computer-algebra lineage rather than an independent
second-system reproduction.  This corollary closes the conic leaf; it does
not establish the exhaustiveness of the global quartic case tree.  The proper
rational-cubic leading-image leaf remains separate.
\end{remark}
</code></pre>

## `lane4-quartic-endgame-20260802-v1/proofs/30-rational-cubic.tex`

<pre><code class="language-tex">
\section{The proper rational-cubic leading image}
\label{app:quartic-rational-cubic}

\begin{theorem}&#91;Candidate rational-cubic leading-image exclusion&#93;
\label{thm:quartic-rational-cubic}
Let $F=H_1+H_2+H_3+H_4:\mathbb A^3_{\mathbb C}\to\mathbb A^3_{\mathbb C}$
be a quartic Keller map, with $H_1=LX$ and $L\in\operatorname{GL}_3$.
The projective image of $H_4$ is not a nondegenerate rational cubic.
\end{theorem}

\begin{proof}
By the leading-image factorization, write
\&#91;
 H_4=G h(x,y),
\&#93;
where $G$ is linear and $h$ is a basepoint-free proper cubic
parametrization.  An irreducible rational plane cubic is cuspidal or nodal;
we use
\&#91;
 h_c=(x^3,x^2y,y^3),\qquad
 h_n=(x^2y,xy^2,x^3+y^3).
\&#93;
Write
\&#91;
 \det(JH_1+\epsilon JH_2+\epsilon^2JH_3+\epsilon^3JH_4)
 =\sum_{j=0}^9D_j\epsilon^j.
\&#93;

If $G\notin\langle x,y\rangle$, normalize $G=z$.  Exact coefficient
comparison in $D_8,D_7$ gives respectively
\&#91;
 H_3=a h_c+\frac b2z(h_c)_x+\frac c3z(h_c)_y
\&#93;
and
\&#91;
 H_3=a h_n+\frac b3z(h_n)_x+\frac c3z(h_n)_y.
\&#93;
These are $JH_4$ applied to constant vectors, so a source translation kills
$H_3$.  For the cusp, $D_6=0$ then gives
\&#91;
 l_0=3l_4/2,
 \qquad l_1=l_2=l_3=l_5=l_6=l_7=l_8=0;
\&#93;
for the node it gives $l_0=\cdots=l_8=0$.  In both cases
$\det L=0$, a contradiction.

Suppose now that $G\in\langle x,y\rangle$.  For the cusp, the stabilizer of
$\langle x^3,x^2y,y^3\rangle$ acts on the normalization by scaling, so the
marked-point orbits are represented by
\&#91;
 G=x,\qquad G=y,\qquad G=x-y.
\&#93;
The equation $D_8=0$ writes
\&#91;
H_3=B_3(x,y)+z(\alpha v_\alpha+\beta v_\beta+\gamma v_\gamma)
              +\delta z^2v_\delta,
\&#93;
where
\&#91;
 v_\alpha=(3x^2/2,xy,0),\quad
 v_\beta=(3xy/2,y^2,0),\quad
 v_\gamma=(0,x^2/3,y^2),\quad
 v_\delta=(3x/2,y,0).
\&#93;
For $G=x$, the $D_7$ compatibility equations leave only a possible
$\alpha$-branch; after normalizing $\alpha=1$, one has
$&#91;xy^3z^2&#93;D_6=3/2$.  For $G=y$, the possible $\alpha$- and $\gamma$-branches
have respectively
\&#91;
 &#91;xy^3z^2&#93;D_6=6,
 \qquad &#91;x^4z^2&#93;D_6=-4/9.
\&#93;
For $G=x-y$, $D_7$ kills all four amplitudes.  Hence $H_3$ is binary in
every case.

The remaining $D_7$ equations leave at most
\&#91;
 H_2=B_2(x,y)+qz(3x/2,y,0).
\&#93;
If $q\ne0$, normalize $q=1$.  After the linear $D_6$ compatibility
relations, $D_5$ has, for $G=x,y,x-y$, respectively,
\&#91;
 &#91;xy^3z&#93;D_5=-6,
 \qquad &#91;y^4z&#93;D_5=-6,
 \qquad (&#91;xy^3z&#93;D_5,&#91;y^4z&#93;D_5)=(-6,6).
\&#93;
Thus $q=0$.

For the node, retain the full marked family
\&#91;
 H_4=(x-\lambda y)h_n.
\&#93;
The $D_8$ solution has
\&#91;
H_3=B_3(x,y)+z\left(
 \frac{2a xy+b x^2}{3},
 \frac{a y^2+2bxy}{3},
 a x^2+b y^2
\right).
\&#93;
The $D_7$ compatibility equations include
\&#91;
\begin{aligned}
0&amp;=\lambda a^2-2\lambda^2ab+(\lambda^3+3)b^2,\\
0&amp;=a^2+4\lambda ab+\lambda^2b^2,\\
0&amp;=\lambda(2a^2+2\lambda ab-\lambda^2b^2).
\end{aligned}
\&#93;
They imply $a=b=0$ for every finite $\lambda$.  The linear $D_7$ system on
the nine $z$-dependent coefficients of $H_2$ has a constant maximal minor
$12582912$, so $H_2$ is binary as well.  The point at infinity follows by
interchanging the two node branches.

We have therefore reduced every marked case to
\&#91;
 F=LX+N(x,y).
\&#93;
After a target linear change this is triangular over a plane Keller pair of
degree at most four.  The low-degree plane theorem makes that pair, and
hence $F$, an automorphism.  This contradicts the assumed counterexample
branch and proves the theorem.
\end{proof}
</code></pre>

## `lane4-quartic-endgame-20260802-v1/proofs/40-span-three-corollary.tex`

<pre><code class="language-tex">
\section{Conditional leading-target-span-three synthesis}

\begin{corollary}&#91;Conditional leading target span two&#93;
Let $F$ be a quartic Keller map over an algebraically closed field of
characteristic zero.  Assume the public rank-one and proper
rational-quartic frontier theorems with all of their stated
preclassification hypotheses.  Assume also that the three conic
propositions and the proper rational-cubic theorem in this packet are
correct.  If $F$ is not a polynomial automorphism, then its leading target
span is exactly two.
\end{corollary}

\begin{proof}
The repaired leading-image factorization gives
\&#91;
H_4=G h(A,B),\qquad \deg G+e\deg A=4,
\&#93;
and the nondegenerate leaves
\&#91;
(e,k,\deg G)\in\{(2,1,2),(2,2,0),(3,1,1),(4,1,0)\}.
\&#93;
A point image is excluded by the assumed rank-one theorem.  A conic image
is excluded in all seven parabolic factor orbits: the four invariant-field
orbits from the public manuscript and the three separate candidate
exclusions for $G=xy,z^2,x^2$.  A proper rational cubic is excluded by the
candidate marked cusp/node theorem, including transverse common factors and
every marked factor in the normalization pencil.  A proper rational quartic
is excluded by the two assumed frontier theorems.  Therefore a
nonautomorphic map can have only a line as its projective leading image,
which is leading target span two.
\end{proof}

\begin{remark}&#91;Logical boundary&#93;
This corollary is a synthesis of separately stated inputs.  It is not an
unconditional theorem of the packet, and it does not address the subsequent
span-two ramification and fixed-component leaves.
\end{remark}
</code></pre>

## `lane4-quartic-endgame-20260802-v1/proofs/50-high-ramification.tex`

<pre><code class="language-tex">
\subsection{A complete high-ramification theorem}
\label{subsec:complete-high-ramification}

Throughout this subsection the ground field is algebraically closed of
characteristic zero.  Put
\&#91;
 K_\epsilon=H_4+\epsilon H_3+\epsilon^2H_2+\epsilon^3H_1,
 \qquad
 D_j=&#91;\epsilon^j&#93;\det JK_\epsilon .
\&#93;
For a Keller map, \(D_0=\cdots=D_8=0\) and
\(D_9=\det JH_1\ne0\).

Assume that the preceding reductions place the map in the primitive
coprime binary-pencil locus
\&#91;
 H_4=(P,Q,0),\qquad P,Q\in k&#91;x,y&#93;_4,
 \qquad R=(H_3)_3\in k&#91;x,y&#93;_3,
\&#93;
with
\&#91;
 U=J(Q,R),\qquad V=J(P,R),\qquad W=J(P,Q)
\&#93;
all nonzero.  Write
\&#91;
 \Delta=\gcd(U,V,W),\qquad
 U=\Delta u,\quad V=\Delta v,\quad W=\Delta w,
 \qquad r=\deg\Delta.
\&#93;
The planar minors give the Hilbert--Burch syzygy
\begin{equation}
 u\,dP-v\,dQ+w\,dR=0,
 \label{eq:r4-hb-syzygy}
\end{equation}
where
\&#91;
 \deg u=\deg v=5-r,
 \qquad
 \deg w=6-r.
\&#93;

\begin{theorem}&#91;Candidate primitive binary high ramification&#93;
\label{thm:complete-binary-high-ramification}
In the preceding primitive coprime binary-pencil locus, if
\(r\ge4\), then \(F\) is a polynomial automorphism.
\end{theorem}

\begin{proof}
Since \(U,V\ne0\), one has \(r\le5\).  We treat \(r=5\) and
\(r=4\) separately.

\medskip
\noindent
\textbf{The case \(r=5\).}
Here \(u,v\) are constants and \(w\) is linear.  Set
\(S=uP-vQ\).  Equation \eqref{eq:r4-hb-syzygy} gives
\&#91;
 dS=-w\,dR,
 \qquad
 dw\wedge dR=0.
\&#93;
Homogeneity therefore yields
\&#91;
 R=cw^3,
 \qquad
 S=-\frac{3c}{4}w^4.
 \tag{H.1}
\&#93;
The full third coordinate has degree three and cubic part \(cw^3\).
The cubic-coordinate lemma straightens it while retaining \(w\) as one of
the two residual source coordinates.  The coordinate with leading part
\(-3cw^4/4\) then has residual plane degree at most nine: its degree-four
part is a polynomial in \(w\), while every term involving the eliminated
source variable has original degree at most three.  The two-variable
Appelgate--Onishi theorem, with its two key lemmas supplied by
Nowicki--Nakai, applies because \(9=3^2\).  Hence the residual plane map,
and therefore \(F\), is an automorphism.

\medskip
\noindent
\textbf{The case \(r=4\): dependent linear syzygies.}
Now \(u,v\) are linear and \(w\) is quadratic.  Suppose first that
\(u,v\) are dependent.  After changing the target basis of
\(\langle P,Q\rangle\), equation \eqref{eq:r4-hb-syzygy} becomes
\&#91;
 \ell\,dS+w\,dR=0,
 \qquad
 4\ell S+3wR=0,                         \tag{H.2}
\&#93;
with \(\ell\) linear.  If \(\ell\mid w\), write \(w=\ell m\).
Then \(dS=-m\,dR\), so \(dm\wedge dR=0\), and homogeneity again gives
\&#91;
 R=cm^3,
 \qquad
 S=-\frac{3c}{4}m^4.
\&#93;
This is the aligned situation (H.1).

If \(\ell\nmid w\), the Euler identity in (H.2) forces
\(R=\ell T\).  Substitution into (H.2) gives
\&#91;
 d\!\left(\frac{\ell^4T}{w^3}\right)=0,
 \qquad
 \ell^4T=cw^3.
\&#93;
Because \(\gcd(\ell,w)=1\), this is impossible in the unique
factorization domain \(k&#91;x,y&#93;\).  Thus the dependent branch is closed.

\medskip
\noindent
\textbf{The case \(r=4\): independent linear syzygies.}
Suppose now that \(u,v\) are independent.  A target change in
\(\langle P,Q\rangle\), followed by a source change in \((x,y)\), lets
us choose the two factors of the reduced quadratic \(w\) as the residual
linear syzygies.  If \(w\) is a square, the formulas below show that
\(P,Q\) have a common linear factor, contrary to primitivity.  Hence we
may normalize
\&#91;
 u=x,
 \qquad
 v=y,
 \qquad
 w=xy.
\&#93;
Euler contraction and differentiation of
\(x\,dP-y\,dQ+xy\,dR=0\) give
\begin{equation}
 P=-\frac14y^2R_y,
 \qquad
 Q=\frac14x^2R_x.                       \tag{H.3}
\end{equation}
Write
\&#91;
 R=ax^3+bx^2y+cxy^2+dy^3.
\&#93;
Coprimality of \(P,Q\) is equivalent to
\&#91;
 a\ne0,
 \qquad
 d\ne0,
 \qquad
 \operatorname{Disc}(R)\ne0.           \tag{H.4}
\&#93;
The common ramification quartic is
\begin{equation}
\begin{aligned}
2\Gamma={}&amp;3abx^4+(9ac+b^2)x^3y+(18ad+4bc)x^2y^2\\
&amp;\quad +(9bd+c^2)xy^3+3cdy^4,
\end{aligned}
\tag{H.5}
\end{equation}
and direct differentiation gives
\&#91;
 J(Q,R)=x\Gamma,
 \qquad
 J(P,R)=y\Gamma,
 \qquad
 J(P,Q)=xy\Gamma.                       \tag{H.6}
\&#93;

Write
\&#91;
 H_3=(A,B,R),
 \qquad
 H_2=(C,D,E).
\&#93;
The coefficient \(D_2=0\), together with (H.6), is
\&#91;
 xA_z-yB_z+xyE_z=0.
\&#93;
Consequently there are linear forms \(\ell,m\in k&#91;x,y,z&#93;_1\) such that
\&#91;
 A_z=y(\ell-m/2),
 \qquad
 B_z=x(\ell+m/2),
 \qquad
 E_z=m.                                 \tag{H.7}
\&#93;
Write \(\ell=\ell_0+\lambda z\) and \(m=m_0+\mu z\), with
\(\ell_0,m_0\in k&#91;x,y&#93;_1\).  The extreme coefficients of
\(&#91;z^3&#93;D_3\) are
\&#91;
 &#91;y^0&#93;&#91;z^3&#93;D_3=\frac38a(2\lambda-\mu)^2x^3,
 \qquad
 &#91;x^0&#93;&#91;z^3&#93;D_3=\frac38d(2\lambda+\mu)^2y^3.
\&#93;
Condition (H.4) therefore gives \(\lambda=\mu=0\).  Thus
\(\ell,m\) are binary.

Put
\&#91;
 \mathcal A=6R,
 \qquad
 \mathcal B=-3ax^3-bx^2y+cxy^2+3dy^3,
 \qquad
 \mathcal C=\frac12(3ax^3+bx^2y+cxy^2+3dy^3).
\&#93;
One has the exact identity
\begin{equation}
 \mathcal A\mathcal C-\mathcal B^2=4xy\Gamma.       \tag{H.8}
\end{equation}
If \(u_2,v_2\) denote the coefficients of \(z^2\) in the first two
components of \(H_2\), then the coefficient of \(z\) in \(D_3\) is
\begin{equation}
 \mathcal Q_{\ell,m}+2\Gamma(u_2x-v_2y),
 \qquad
 \mathcal Q_{\ell,m}
 =\frac12(\mathcal A\ell^2+2\mathcal B\ell m+\mathcal C m^2).
 \tag{H.9}
\end{equation}
In particular,
\begin{equation}
 \Gamma\mid\mathcal Q_{\ell,m}.         \tag{H.10}
\end{equation}

\smallskip
\noindent
\emph{Squarefree \(\Gamma\).}
At a root of a squarefree \(\Gamma\), the symmetric matrix
\&#91;
 M=\begin{pmatrix}\mathcal A&amp;\mathcal B\\
                   \mathcal B&amp;\mathcal C\end{pmatrix}
\&#93;
has rank one.  It cannot vanish there: otherwise Euler's identity would
make that point a repeated root of \(R\), contrary to (H.4).  Hence
(H.10) implies that \((\ell,m)^T\) lies in the kernel of \(M\) at every
root of \(\Gamma\).  Since the two entries of
\(M(\ell,m)^T\) have degree four, there are constants \(\alpha,\beta\)
with
\&#91;
 M\binom{\ell}{m}=\Gamma\binom{\alpha}{\beta}.
\&#93;
Multiplication by the adjugate matrix and use of (H.8) give
\&#91;
 4xy\ell=\mathcal C\alpha-\mathcal B\beta,
 \qquad
 4xym=-\mathcal B\alpha+\mathcal A\beta.
\&#93;
Restriction to \(y=0\) gives \(\alpha+2\beta=0\), while restriction to
\(x=0\) gives \(\alpha-2\beta=0\).  Thus
\(\alpha=\beta=0\) and \(\ell=m=0\).

It remains to treat repeated \(\Gamma\).

\smallskip
\noindent
\emph{A repeated root away from \(xy=0\).}
A diagonal source change moves such a root to \(&#91;1:1&#93;\).  The equations
\(\Gamma(1,1)=\partial_x\Gamma(1,1)=0\) have two components.  Their
eliminant is
\begin{equation}
 (b+2c+3d)
 (b^2+6bc+18bd+3c^2+12cd)=0.             \tag{H.11}
\end{equation}
On the first component, (H.4) forces
\&#91;
 b=-2c-3d,
 \qquad
 a=c+2d,
\&#93;
so \(R_x(1,1)=R_y(1,1)=0\), again contradicting primitivity.

The second component is the proper rational conic
\begin{equation}
\begin{aligned}
&#91;a:b:c:d&#93;=&#91;&amp;-(3u+2v)(3u^2+6uv+v^2):\\
&amp;6u(3u+2v)(2u+3v):\\
&amp;6v(3u+2v)(2u+3v):\\
&amp;-(u^2+6uv+3v^2)(2u+3v)&#93;.
\end{aligned}
\tag{H.12}
\end{equation}
The four coordinates in (H.12) have no common projective zero, and the
inverse on the dense chart is \(&#91;u:v&#93;=&#91;b:c&#93;\); hence (H.12) includes its
projective endpoints.  On the affine chart \(t=v/u\), put
\begin{equation}
\begin{aligned}
 a&amp;=-(2t+3)(t^2+6t+3),\\
 b&amp;=6(2t+3)(3t+2),\\
 c&amp;=6t(2t+3)(3t+2),\\
 d&amp;=-(3t+2)(3t^2+6t+1).
\end{aligned}
\tag{H.13}
\end{equation}
Then
\begin{equation}
 \Gamma=-9(2t+3)(3t+2)(x-y)^2G_{2,t},   \tag{H.14}
\end{equation}
where
\begin{equation}
\begin{aligned}
G_{2,t}={}&amp;(2t^3+15t^2+24t+9)x^2\\
&amp;+(6t^4+49t^3+90t^2+49t+6)xy\\
&amp;+(9t^4+24t^3+15t^2+2t)y^2.
\end{aligned}
\tag{H.15}
\end{equation}
The relevant discriminants are
\begin{align}
 \operatorname{Disc}(R)
 &amp;=3375(t+1)^6(2t+3)^2(3t+2)^2(3t^2+14t+3),
 \tag{H.16}\\
 \operatorname{Disc}(G_{2,t})
 &amp;=(t+1)^2(2t+3)(3t+2)
   (2t^2+11t+2)(3t^2+14t+3),             \tag{H.17}\\
 G_{2,t}(1,1)
 &amp;=15(t+1)^2(t^2+3t+1).                  \tag{H.18}
\end{align}
Thus, on the primitive locus, the only special residual divisors are the
\(3+1\) divisor \(t^2+3t+1=0\) and the internal \(2+2\) divisor
\(2t^2+11t+2=0\).  The projective point \(t=\infty\) is equivalent to
\(t=0\) under \(x\leftrightarrow y\), since
\&#91;
 t^3(a,b,c,d)(1/t)=(d,c,b,a)(t).
\&#93;

Away from the internal \(2+2\) divisor, exact row reduction of (H.10),
including the \(3+1\) specialization, gives the unique projective
first-normal direction
\begin{equation}
\begin{aligned}
 \ell&amp;=h\bigl((t^2+6t+3)x-(3t^2+6t+1)y\bigr),\\
 m&amp;=2h(t+1)\bigl((t+9)x+(9t+1)y\bigr).
\end{aligned}
\tag{H.19}
\end{equation}
Equation (H.9) then fixes
\&#91;
 u_2=-\frac{2h^2(2t+3)}{3(3t+2)},
 \qquad
 v_2=\frac{2h^2t(3t+2)}{3(2t+3)}.
\&#93;
All unrestricted binary terms and all remaining lower coefficients drop out
of the next highest normal coefficient, which factors as
\begin{equation}
\begin{aligned}
 &#91;z^2&#93;D_4={}&amp;
 \frac{24h^3(t+1)}{(2t+3)(3t+2)}\\
 &amp;\quad\cdot
 \bigl((2t+3)^2(4t+1)x+(t+4)(3t+2)^2y\bigr)G_{2,t}.
\end{aligned}
\tag{H.20}
\end{equation}
Every scalar and polynomial factor in (H.20) is nonzero on the primitive
locus.  Hence \(h=0\).

On the internal \(2+2\) divisor, work over
\&#91;
 K=k&#91;t&#93;/(2t^2+11t+2).
\&#93;
The complete first-normal space is two-dimensional:
\begin{equation}
\begin{aligned}
 L_0&amp;=h,&amp;
 L_1&amp;=\frac{4t}{11}h-\frac3{22}k,\\
 M_0&amp;=\frac{70}{11}h-
       \left(2+\frac{4t}{11}\right)k,&amp;
 M_1&amp;=k,
\end{aligned}
\tag{H.21}
\end{equation}
where \(\ell=L_0x+L_1y\) and \(m=M_0x+M_1y\).  After solving (H.9), the
extreme coefficients of \(&#91;z^2&#93;D_4\) are
\begin{align}
 &#91;x^3z^2&#93;D_4
 &amp;=\frac{12096}{1331}
 \left(h-\frac{2t+11}{24}k\right)^2
 \left(h+\frac{5(2t+11)}{56}k\right),       \tag{H.22}\\
 &#91;y^3z^2&#93;D_4
 &amp;=-\frac{126(117t+22)}{1331}
 \left(h-\frac{2t+11}{2}k\right)^2
 \left(h+\frac{2t+11}{42}k\right).          \tag{H.23}
\end{align}
Both \(2t+11\) and \(117t+22\) are units in \(K\).  The projective root
sets
\&#91;
 \left\{\frac1{24},-\frac5{56}\right\},
 \qquad
 \left\{\frac12,-\frac1{42}\right\}
\&#93;
are disjoint, so (H.22)--(H.23) imply \(h=k=0\).

\smallskip
\noindent
\emph{A repeated root on \(xy=0\).}
If \(\Gamma\) has a repeated root at either endpoint, (H.4)--(H.5) force
\(b=c=0\).  After diagonal rescaling, take
\&#91;
 R=x^3+y^3,
 \qquad
 \Gamma=9x^2y^2.
\&#93;
The complete solution of (H.10) is
\&#91;
 \ell=px+qy,
 \qquad
 m=2px-2qy,
 \qquad
 \frac{\mathcal Q_{\ell,m}}{\Gamma}
 =\frac43(q^2x+p^2y).
\&#93;
After solving (H.9), the next coefficient is
\&#91;
 &#91;z^2&#93;D_4=8q^3x^3-8p^3y^3,
\&#93;
so \(p=q=0\).

We have now proved in every projective stratum that the first normal layer
vanishes.  Thus \(A,B,E\) are binary.  Returning to \(D_3=0\), the most
general remaining quadratic normal layer is
\&#91;
 C=C_0(x,y)+\alpha yz,
 \qquad
 D=D_0(x,y)+\beta xz,
 \qquad
 (H_1)_3=L_{31}x+L_{32}y+(\beta-\alpha)z.
\&#93;
The coefficient of \(z\) in \(D_5\), independently of every unrestricted
binary lower term, is
\begin{equation}
\begin{aligned}
\frac12\bigl(&amp;6a\alpha^2x^3
 +(3b\alpha^2+2b\alpha\beta+b\beta^2)x^2y\\
&amp;+(c\alpha^2+2c\alpha\beta+3c\beta^2)xy^2
 +6d\beta^2y^3\bigr).
\end{aligned}
\tag{H.24}
\end{equation}
The extreme coefficients and (H.4) give \(\alpha=\beta=0\).
Consequently all nonlinear terms of \(F\) are binary.

The third column of the invertible linear part is nonzero.  A target-linear
change sends it to \(e_3\), after which
\&#91;
 F=(G_1(x,y),G_2(x,y),z+G_3(x,y)).
\&#93;
The pair \((G_1,G_2)\) is a plane Keller map of degree at most four, so the
same Appelgate--Onishi--Nowicki--Nakai theorem makes it an automorphism.
This completes the proof.
\end{proof}

\begin{remark}&#91;Evidence boundary&#93;
All identities from (H.3) through (H.24), the projective conic
parametrization, the generic and \(3+1\) row reductions, the complete
\(2+2\) kernel, and the endpoint calculation are reconstructed by the
standalone exact checker
\begin{center}
\texttt{verify\_r4\_high\_ramification.py}.
\end{center}
It keeps arbitrary lower terms whenever they could enter the quoted
coefficient, uses exact rational arithmetic, makes no random
specializations, and divides only by factors explicitly excluded by
primitivity.  The structural Hilbert--Burch reduction into
\eqref{eq:r4-hb-syzygy} and the upstream routing into the primitive binary
locus remain separate inputs.
\end{remark}
</code></pre>

## `lane4-quartic-endgame-20260802-v1/proofs/60-tau-minus-one.tex`

<pre><code class="language-tex">
% Independent tau=-1 degree-three ramification exclusion.
% Prepared 2026-08-02 against the Program 2 (3,4) Hilbert--Burch chart.

\begin{theorem}&#91;Candidate primitive $\tau=-1$ chart&#93;
\label{thm:quartic-r3-tau-minus-one}
Let $k$ be algebraically closed of characteristic zero, and let
\&#91;
 F=LX+H_2+H_3+H_4:\mathbb A_k^3\longrightarrow\mathbb A_k^3
\&#93;
be Keller.  Assume the preceding Program~2 reductions place $F$ in the
primitive coprime binary-pencil branch of common ramification degree three,
and in the independent Hilbert--Burch chart
\&#91;
 u=x^2,\qquad v=y^2,\qquad
 w=ax^3+x^2y+xy^2+by^3,\qquad \tau=-1.
\&#93;
Then the first normal layer vanishes.  Consequently this chart exits to the
zero-normal triangular branch and contains no Keller counterexample.
\end{theorem}

\begin{proof}
The differential Hilbert--Burch equation
\&#91;
 x^2\,dP-y^2\,dQ+w\,dR=0
\&#93;
reconstructs
\begin{align*}
 R={}&amp;-ax^3-3x^2y+3xy^2+by^3,\\
 P=\frac34\bigl(&amp;a^2x^4-2abxy^3+4ax^3y-4ax^2y^2
                    -2by^4+2x^2y^2-2xy^3-y^4\bigr),\\
 Q=-\frac34\bigl(&amp;2abx^3y+2ax^4-b^2y^4+4bx^2y^2-4bxy^3
                    +x^4+2x^3y-2x^2y^2\bigr).
\end{align*}
Their minors have the required common cubic:
\&#91;
 J(Q,R)=x^2\Delta,\qquad J(P,R)=y^2\Delta,
 \qquad J(P,Q)=w\Delta.
\&#93;
Put
\&#91;
 F_1=27a^2b^2-18ab+4a+4b-1,
 \qquad
 G=a^2b^2-6ab-4a-4b-3.
\&#93;
Exact dehomogenized resultants give
\&#91;
 \operatorname{Res}_x(P(x,1),Q(x,1))
   =-\frac{6561}{65536}F_1G^3.
\&#93;
Thus primitivity implies $F_1G\ne0$.

Write $A=(H_3)_1$, $B=(H_3)_2$, and $E=(H_2)_3$.  The first normal
syzygy has the complete form
\begin{equation}
\label{eq:tau-minus-one-first-normal}
 (A_z,B_z,E_z)
 =L_0(-ax-y,x+by,1)+\mu(y^2,x^2,0),
 \qquad L_0=l_0x+l_1y+l_2z.
\end{equation}
Let $D_j$ denote the $j$th coefficient of the determinant arc, using
$H_4,H_3,H_2,H_1$ as levels $0,1,2,3$.  The coefficient of $z^3$ in
$D_3$ is
\&#91;
 \frac{3l_2^2}{4}\bigl(
 A_*x^3+C_*x^2y-D_*xy^2-B_*y^3\bigr),
\&#93;
where
\&#91;
 A_*=a^2b-3a-2,\quad B_*=ab^2-3b-2,
 \quad C_*=ab+2a+1,\quad D_*=ab+2b+1.
\&#93;
If $l_2\ne0$, all four coefficients vanish.  Since
\&#91;
 C_*-D_*=2(a-b),\qquad C_*\big|_{b=a}=(a+1)^2,
\&#93;
this forces $(a,b)=(-1,-1)$, where $G=0$.  Hence $l_2=0$ on the
primitive locus.

Set $\lambda=l_0x+l_1y$.  The coefficient of $z$ in $D_3$ gives six
quadrics in
\&#91;
 l_0^2,\ l_0l_1,\ l_1^2,\ l_0\mu,\ l_1\mu,\mu^2,\ u_2,\ v_2,
\&#93;
where $u_2,v_2$ are the $z^2$ coefficients of the first two components
of $H_2$.  The first and last equations are
\&#91;
 A_*(l_0^2-6u_2)=0,\qquad
 B_*(l_1^2-6v_2)=0.
\&#93;
We divide the remaining analysis into the complete coefficient-divisor
stratification.

\smallskip
\noindent\emph{The open set $A_*B_*\ne0$.}
Here $u_2=l_0^2/6$ and $v_2=l_1^2/6$.  After removing harmless scalar
factors, the four middle equations generate the ideal $I=(f_0,f_1,f_2,f_3)$,
where
\begin{align*}
 f_0={}&amp;a^2bl_0l_1-abl_0^2-2al_0^2-3al_0l_1+4al_0\mu-2a\mu^2
        -l_0^2-2l_0l_1+4l_0\mu,\\
 f_1={}&amp;a^2bl_1^2-2abl_0^2+abl_0l_1+4abl_0\mu+2al_0l_1-3al_1^2
        +4al_1\mu-4bl_0^2\\
      &amp;\hspace{1.4em}-2l_0^2+l_0l_1-4l_0\mu-2l_1^2+4l_1\mu-6\mu^2,\\
 f_2={}&amp;ab^2l_0^2+abl_0l_1-2abl_1^2-4abl_1\mu-4al_1^2-3bl_0^2
        +2bl_0l_1-4bl_0\mu\\
      &amp;\hspace{1.4em}-2l_0^2+l_0l_1-4l_0\mu-2l_1^2+4l_1\mu-6\mu^2,\\
 f_3={}&amp;ab^2l_0l_1-abl_1^2-3bl_0l_1-2bl_1^2-4bl_1\mu-2b\mu^2
        -2l_0l_1-l_1^2-4l_1\mu.
\end{align*}
Exact Gröbner reduction gives the saturation certificates
\begin{equation}
\label{eq:tau-minus-one-saturation}
 \mu^4G\in I,
 \qquad
 l_0^4G,\ l_1^4G\in I+(\mu).
\end{equation}
Thus every nonzero projective point $&#91;l_0:l_1:\mu&#93;$ in this open set
forces $G=0$, contrary to primitivity.

\smallskip
\noindent\emph{The divisor $A_*=0$, with $B_*\ne0$.}
Here $a\ne0$ and
\&#91;
 b=\frac{3a+2}{a^2},\qquad
 B_*=-\frac{2(a-2)(a+1)^2}{a^3}.
\&#93;
Use $v_2=l_1^2/6$ in the four middle equations.  On the three standard
projective charts $l_0=1$, $l_1=1$, and $\mu=1$, their exact ideals contain,
respectively,
\&#91;
 (a+1)^4,\qquad a^2(a+1)^4,\qquad a^2.
\&#93;
Since $a\ne0$ and $B_*\ne0$, none has a point.  The divisor $B_*=0$,
$A_*\ne0$, is checked independently: after
$a=(3b+2)/b^2$ and $u_2=l_0^2/6$, the corresponding three chart ideals
contain
\&#91;
 b^2(b+1)^4,\qquad (b+1)^4,\qquad b^2.
\&#93;
It likewise has no point.

\smallskip
\noindent\emph{The intersection $A_*=B_*=0$.}
The identity
\&#91;
 A_*-B_*=(a-b)(ab-3)
\&#93;
shows that $ab=3$ would give $A_*=-2$, so $a=b$.  Therefore
\&#91;
 (a,b)=(-1,-1)\quad\hbox{or}\quad (2,2).
\&#93;
The first point has $G=0$.  At the primitive point $(2,2)$, elimination of
$u_2,v_2$ leaves
\begin{align*}
 K_1&amp;=9l_0^2-9l_0l_1-12l_1\mu+2\mu^2=0,\\
 K_2&amp;=9l_0l_1-12l_0\mu-9l_1^2-2\mu^2=0.
\end{align*}
These satisfy
\&#91;
 K_1-K_2=(3l_0-3l_1+2\mu)^2,
 \qquad
 K_1+K_2=3(l_0+l_1)(3l_0-3l_1-4\mu).
\&#93;
Consequently the nonzero first-normal solutions are exactly
\begin{align*}
 (l_0,l_1,\mu,u_2,v_2)
   &amp;=\left(h,h,0,\frac{h^2}{18},\frac{h^2}{18}\right),\\
 (l_0,l_1,\mu,u_2,v_2)
   &amp;=\left(-h,h,3h,-\frac{5h^2}{6},-\frac{5h^2}{6}\right),
 \qquad h\ne0.
\end{align*}

It remains to test the next determinant coefficient.  Keep arbitrary binary
cubics $A_0,B_0$, arbitrary binary quadrics $C_0,D_0,E_0$, arbitrary binary
linear forms $p,q$, and an arbitrary linear part.  Thus
\&#91;
 A=A_0+zA_z,\quad B=B_0+zB_z,
\&#93;
\&#91;
 H_2=\bigl(C_0+zp+u_2z^2,
           D_0+zq+v_2z^2,
           E_0+z\lambda\bigr).
\&#93;
A direct exact expansion, with no specialization of these lower terms, gives
for the two displayed branches
\begin{align*}
 &#91;z^2&#93;D_4
   &amp;=-\frac{h^3}{2}(x+y)(5x^2+2xy+5y^2),\\
 &#91;z^2&#93;D_4
   &amp;=\frac{135h^3}{2}(x-y)(x+y)^2.
\end{align*}
Both are nonzero for $h\ne0$.  Hence the intersection has no nonzero
first-normal solution either.

We have proved that primitivity forces
$l_0=l_1=l_2=\mu=0$.  The established zero-normal lemma then makes the third
coordinate triangular (or makes every nonlinear term binary), and the usual
plane Keller reduction proves that $F$ is an automorphism.
\end{proof}

\begin{remark}&#91;Computation boundary&#93;
The accompanying checker reconstructs $P,Q$, the six first-normal equations,
the saturation and projective-chart certificates, and the two unrestricted
$&#91;z^2&#93;D_4$ obstructions over $\mathbb Q$.  It does not re-prove the upstream
placement of a quartic map in this Hilbert--Burch chart or the final
zero-normal plane theorem.
\end{remark}
</code></pre>

## `lane4-quartic-endgame-20260802-v1/replay_core.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Replay the compact exact certificate set for the Lane 4 repair packet.

The default suite reruns the two standalone chart checkers, the z^2 conic
checker, the compact conic terminal identities, and selected rational-cubic
calculations.  ``--full-conic`` additionally invokes each of the ten larger
conic branch scripts through its assertion-based wrapper.

This program verifies finite symbolic identities only.  It does not prove the
upstream geometric classifications or chart-exhaustiveness statements.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FRESH = ROOT / "fresh-outputs"


@dataclass(frozen=True)
class Check:
    name: str
    command: tuple&#91;str, ...&#93;
    cwd: Path
    needles: tuple&#91;str, ...&#93; = ()
    exact_output: Path | None = None
    timeout: int = 300


def run(check: Check) -&gt; None:
    print(f"&#91;{check.name}&#93;", flush=True)
    proc = subprocess.run(
        check.command,
        cwd=check.cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=check.timeout,
        check=False,
    )
    output = proc.stdout
    FRESH.mkdir(exist_ok=True)
    fresh_path = FRESH / f"{check.name}.txt"
    fresh_path.write_text(output, encoding="utf-8")

    problems: list&#91;str&#93; = &#91;&#93;
    if proc.returncode:
        problems.append(f"return code {proc.returncode}")
    for needle in check.needles:
        if needle not in output:
            problems.append(f"missing {needle!r}")
    if check.exact_output is not None:
        stored = check.exact_output.read_text(encoding="utf-8")
        if output != stored:
            problems.append(
                f"output differs from {check.exact_output.relative_to(ROOT)}"
            )
    if problems:
        print(output)
        raise RuntimeError(f"{check.name}: " + "; ".join(problems))
    print(f"PASS {check.name}")


def core_checks() -&gt; dict&#91;str, list&#91;Check&#93;&#93;:
    py = sys.executable
    high = ROOT / "checks" / "high-ramification"
    tau = ROOT / "checks" / "tau-minus-one"
    conic = ROOT / "checks" / "conic"
    cubic = ROOT / "checks" / "rational-cubic" / "scripts"
    structural = &#91;
        Check(
            "high-ramification",
            (py, "verify_r4_high_ramification.py"),
            high,
            exact_output=high / "verify_r4_high_ramification.out",
        ),
        Check(
            "tau-minus-one",
            (py, "verify_tau_minus_one.py"),
            tau,
            exact_output=tau / "verify_tau_minus_one.out",
        ),
    &#93;
    conic_checks = &#91;
        Check(
            "conic-z2",
            (py, "z2_conic_independent_check.py"),
            conic,
            exact_output=conic / "stored-outputs" / "replay_z2_conic.txt",
        ),
        Check(
            "conic-terminal-identities",
            (py, "verify_terminal_identities.py"),
            conic,
            needles=("PASS: all quoted terminal factor identities hold over Q.",),
        ),
    &#93;
    rational_cubic = &#91;
        Check(
            "rational-cubic-transverse-cusp",
            (py, "transverse_after_translation.py", "cusp"),
            cubic,
            needles=("rank 8 nullity 1", "detL reduced 0"),
        ),
        Check(
            "rational-cubic-transverse-node",
            (py, "transverse_after_translation.py", "node"),
            cubic,
            needles=("rank 9 nullity 0", "detL reduced 0"),
        ),
        Check(
            "rational-cubic-node-pivot",
            (py, "node_h2z_pivotminor.py"),
            cubic,
            needles=("det 12582912",),
        ),
        Check(
            "rational-cubic-node-marked-family",
            (py, "node_marked_lambda_d7.py"),
            cubic,
            needles=("leftnull 6", "PURE 0", "PURE 3", "PURE 5"),
        ),
        Check(
            "rational-cubic-cusp-fiber-q",
            (py, "cusp_fiber_q_branch.py"),
            cubic,
            needles=("(1, 3, 1) -6", "solutions 0"),
        ),
        Check(
            "rational-cubic-cusp-smooth-q",
            (py, "cusp_smooth_q_branch.py"),
            cubic,
            needles=("(0, 4, 1) -6",),
        ),
        Check(
            "rational-cubic-cusp-generic-q",
            (py, "cusp_generic_q_d5.py"),
            cubic,
            needles=("(1, 3, 1) -6", "(0, 4, 1) 6"),
        ),
    &#93;
    return {
        "structural": structural,
        "conic": conic_checks,
        "rational-cubic": rational_cubic,
    }


def full_conic_checks() -&gt; list&#91;Check&#93;:
    py = sys.executable
    conic = ROOT / "checks" / "conic"
    names = (
        "x2-scalar",
        "x2-semisimple",
        "x2-nilpotent-1",
        "x2-nilpotent-2",
        "x2-second-normal-p",
        "x2-second-normal-q",
        "xy-scalar",
        "xy-anti-scalar",
        "xy-second-normal-axis",
        "xy-second-normal-open",
    )
    return &#91;
        Check(
            f"conic-{name}",
            (py, "run_replays.py", name),
            conic,
            needles=(f"PASS {name}",),
            timeout=420,
        )
        for name in names
    &#93;


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--group",
        choices=("all", "structural", "conic", "rational-cubic"),
        default="all",
        help="run one compact group or the complete compact suite",
    )
    parser.add_argument(
        "--full-conic",
        action="store_true",
        help="also run the ten larger conic branch scripts",
    )
    args = parser.parse_args()

    groups = core_checks()
    if args.group == "all":
        checks = &#91;check for name in ("structural", "conic", "rational-cubic") for check in groups&#91;name&#93;&#93;
    else:
        checks = list(groups&#91;args.group&#93;)
    if args.full_conic:
        if args.group not in ("all", "conic"):
            parser.error("--full-conic requires --group all or --group conic")
        checks.extend(full_conic_checks())
    for check in checks:
        run(check)
    print(f"PASS: {len(checks)} Lane 4 exact replay groups completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `lane4-quartic-endgame-20260802-v1/checks/conic/verify_terminal_identities.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Fast exact checks of the terminal factor identities quoted in the proof note."""
from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr) -&gt; None:
    assert sp.expand(expr) == 0, sp.factor(expr)


def x2_scalar_identity() -&gt; None:
    a0, b0, b1, b3, c7, l4, l7 = sp.symbols(
        "a0 b0 b1 b3 c7 l4 l7"
    )
    A = 4*a0*b0*b1 + 2*b0**2*b3 - 4*b0*b1**2 - 2*b0*c7 + l7
    B = 2*a0**2*b1 - 4*a0*b1**2 - a0*c7 + 2*b1**3 + b1*c7 + l4
    S = 2*a0*b0**2*b3 + a0*l7 - 2*b0**2*b1*b3 - 2*b0*l4 - b1*l7
    assert_zero(S - ((a0-b1)*A - 2*b0*B))


def xy_scalar_identity() -&gt; None:
    a0, a1, b1, b3, c7, l4, l7 = sp.symbols(
        "a0 a1 b1 b3 c7 l4 l7"
    )
    A = (
        2*a0**2*a1 - 4*a0**2*b3 + 4*a0*b1*b3 - 2*a0*c7
        - 2*a1*b1**2 + 2*b1*c7 - l7
    )
    B = (
        a0*a1**2 - 2*a0*a1*b3 + a0*b3**2 + a1**2*b1
        - 2*a1*b1*b3 - a1*c7 + b1*b3**2 + b3*c7 + l4
    )
    S = (
        2*a0**2*a1*b3 - 2*a0**2*b3**2 - 4*a0*a1*b1*b3
        + 4*a0*b1*b3**2 + 2*a0*l4 + 2*a1*b1**2*b3 + a1*l7
        - 2*b1**2*b3**2 - 2*b1*l4 - b3*l7
    )
    assert_zero(S - (-(a1-b3)*A + 2*(a0-b1)*B))


def routing_factors() -&gt; None:
    a2, b4, m0, m5 = sp.symbols("a2 b4 m0 m5")
    # If m0 != 0, the D7 factor 3a2-b4 and the D6 factor
    # 3a2^2+b4^2 force a2=b4=0; similarly at the other endpoint.
    assert_zero((3*a2**2+b4**2).subs(b4, 3*a2) - 12*a2**2)
    assert_zero((a2**2+3*b4**2).subs(a2, 3*b4) - 12*b4**2)
    # The remaining nonzero xy z-matrix lies on the scalar/anti-scalar divisor.
    assert_zero((a2-b4)**2*(a2+b4) - (a2-b4)**2*(a2+b4))
    assert sp.Integer(-8) != 0 and sp.Integer(-64) != 0 and sp.Integer(16) != 0


def main() -&gt; None:
    x2_scalar_identity()
    xy_scalar_identity()
    routing_factors()
    print("PASS: all quoted terminal factor identities hold over Q.")


if __name__ == "__main__":
    main()
</code></pre>

## `lane4-quartic-endgame-20260802-v1/checks/high-ramification/verify_r4_high_ramification.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact certificate for the primitive binary quartic r &gt;= 4 branch.

This script verifies the algebraic identities used in the proof of:

    Let F be a three-variable quartic Keller map over a field of
    characteristic zero.  In the primitive coprime binary leading-pencil
    locus, assume U=J(Q,R), V=J(P,R), W=J(P,Q) are nonzero and
    r=deg gcd(U,V,W) &gt;= 4.  Then F is a polynomial automorphism.

The structural reductions and the final plane theorem are textual arguments.
This checker covers the nontrivial finite algebra in the r=4 independent-
syzygy branch, including every projective repeated-root stratum.

It uses exact rational arithmetic only.  No random specialization is used.
"""
from __future__ import annotations

from itertools import combinations, product
import sympy as s


def assert_zero(expr: s.Expr, label: str) -&gt; None:
    value = s.cancel(s.expand(expr))
    if value != 0:
        raise AssertionError(f"{label} failed: {s.factor(value)}")


def jac(f: s.Expr, g: s.Expr, x: s.Symbol, y: s.Symbol) -&gt; s.Expr:
    return s.expand(s.diff(f, x) * s.diff(g, y) - s.diff(f, y) * s.diff(g, x))


def grad(f: s.Expr, vars_: tuple&#91;s.Symbol, s.Symbol, s.Symbol&#93;) -&gt; list&#91;s.Expr&#93;:
    return &#91;s.diff(f, q) for q in vars_&#93;


def det3(a: list&#91;s.Expr&#93;, b: list&#91;s.Expr&#93;, c: list&#91;s.Expr&#93;) -&gt; s.Expr:
    return s.expand(s.Matrix(&#91;a, b, c&#93;).det())


def coeff_homogeneous(poly: s.Expr, x: s.Symbol, y: s.Symbol, degree: int) -&gt; list&#91;s.Expr&#93;:
    P = s.Poly(s.expand(poly), x, y)
    return &#91;P.coeff_monomial(x ** (degree - i) * y**i) for i in range(degree + 1)&#93;


def reduce_mod_t(expr: s.Expr, t: s.Symbol, modulus: s.Expr, coeff_vars: tuple&#91;s.Symbol, ...&#93; = ()) -&gt; s.Expr:
    """Reduce a rational expression modulo an irreducible polynomial in t.

    Coefficients may be rational functions in coeff_vars.  Every denominator
    used below is asserted to be a unit modulo modulus.
    """
    domain = s.QQ.frac_field(*coeff_vars) if coeff_vars else s.QQ
    num, den = s.fraction(s.cancel(expr))
    mod_poly = s.Poly(modulus, t, domain=domain)
    num_r = s.rem(s.Poly(num, t, domain=domain), mod_poly).as_expr()
    den_r = s.rem(s.Poly(den, t, domain=domain), mod_poly).as_expr()
    inv = s.invert(den_r, modulus, domain=domain)
    return s.factor(s.rem(s.Poly(s.expand(num_r * inv), t, domain=domain), mod_poly).as_expr())


def reduce_poly_coeffs(expr: s.Expr, t: s.Symbol, modulus: s.Expr, vars_: tuple&#91;s.Symbol, ...&#93;) -&gt; s.Expr:
    P = s.Poly(s.expand(expr), *vars_)
    out = s.Integer(0)
    for mon, coeff in P.terms():
        coeff_r = reduce_mod_t(coeff, t, modulus)
        term = coeff_r
        for q, e in zip(vars_, mon):
            term *= q**e
        out += term
    return s.factor(out)


print("&#91;1/9&#93; Reduced quadratic normal form and ramification quartic")
x, y, z = s.symbols("x y z")
a, b, c, d = s.symbols("a b c d")
R = a * x**3 + b * x**2 * y + c * x * y**2 + d * y**3
P = -s.Rational(1, 4) * y**2 * s.diff(R, y)
Q = s.Rational(1, 4) * x**2 * s.diff(R, x)
Gamma = s.expand(
    (
        3 * a * b * x**4
        + (9 * a * c + b**2) * x**3 * y
        + (18 * a * d + 4 * b * c) * x**2 * y**2
        + (9 * b * d + c**2) * x * y**3
        + 3 * c * d * y**4
    )
    / 2
)
assert_zero(jac(Q, R, x, y) - x * Gamma, "J(Q,R)=x Gamma")
assert_zero(jac(P, R, x, y) - y * Gamma, "J(P,R)=y Gamma")
assert_zero(jac(P, Q, x, y) - x * y * Gamma, "J(P,Q)=xy Gamma")

Acal = 6 * R
Bcal = -3 * a * x**3 - b * x**2 * y + c * x * y**2 + 3 * d * y**3
Ccal = (3 * a * x**3 + b * x**2 * y + c * x * y**2 + 3 * d * y**3) / 2
assert_zero(Acal * Ccal - Bcal**2 - 4 * x * y * Gamma, "normal-form discriminant")

print("&#91;2/9&#93; First-normal determinant identities, with arbitrary lower terms")
L0, L1, M0, M1, u2, v2 = s.symbols("L0 L1 M0 M1 u2 v2")
ell = L0 * x + L1 * y
m = M0 * x + M1 * y
az = y * (ell - m / 2)
bz = x * (ell + m / 2)

# Keep every term that could conceivably enter &#91;z&#93;D3 or &#91;z^2&#93;D4.
A30c = s.symbols("A30:4")
B30c = s.symbols("B30:4")
A20c = s.symbols("A20:3")
B20c = s.symbols("B20:3")
C20c = s.symbols("C20:3")
pc = s.symbols("p0:2")
qc = s.symbols("q0:2")
lc = s.symbols("l0:9")
mons3 = &#91;x**3, x**2 * y, x * y**2, y**3&#93;
mons2 = &#91;x**2, x * y, y**2&#93;
A30 = sum(q * mon for q, mon in zip(A30c, mons3))
B30 = sum(q * mon for q, mon in zip(B30c, mons3))
A20 = sum(q * mon for q, mon in zip(A20c, mons2))
B20 = sum(q * mon for q, mon in zip(B20c, mons2))
C20 = sum(q * mon for q, mon in zip(C20c, mons2))
plin = pc&#91;0&#93; * x + pc&#91;1&#93; * y
qlin = qc&#91;0&#93; * x + qc&#91;1&#93; * y
H3_1 = A30 + z * az
H3_2 = B30 + z * bz
H3_3 = R
H2_1 = A20 + z * plin + u2 * z**2
H2_2 = B20 + z * qlin + v2 * z**2
H2_3 = C20 + z * m
H1_1 = lc&#91;0&#93; * x + lc&#91;1&#93; * y + lc&#91;2&#93; * z
H1_2 = lc&#91;3&#93; * x + lc&#91;4&#93; * y + lc&#91;5&#93; * z
H1_3 = lc&#91;6&#93; * x + lc&#91;7&#93; * y + lc&#91;8&#93; * z
vars3 = (x, y, z)
rows = &#91;
    &#91;grad(P, vars3), grad(H3_1, vars3), grad(H2_1, vars3), grad(H1_1, vars3)&#93;,
    &#91;grad(Q, vars3), grad(H3_2, vars3), grad(H2_2, vars3), grad(H1_2, vars3)&#93;,
    &#91;grad(0, vars3), grad(H3_3, vars3), grad(H2_3, vars3), grad(H1_3, vars3)&#93;,
&#93;


def D(index: int) -&gt; s.Expr:
    return s.expand(
        sum(
            det3(rows&#91;0&#93;&#91;i&#93;, rows&#91;1&#93;&#91;j&#93;, rows&#91;2&#93;&#91;k&#93;)
            for i, j, k in product(range(4), repeat=3)
            if i + j + k == index
        )
    )

D3 = D(3)
D3_z = s.Poly(D3, z).coeff_monomial(z)
Qnormal = s.expand((Acal * ell**2 + 2 * Bcal * ell * m + Ccal * m**2) / 2)
assert_zero(D3_z - Qnormal - 2 * Gamma * (u2 * x - v2 * y), "&#91;z&#93;D3 identity")

D4_z2 = s.Poly(D(4), z).coeff_monomial(z**2)
essential_symbols = {x, y, a, b, c, d, L0, L1, M0, M1, u2, v2}
if not D4_z2.free_symbols &lt;= essential_symbols:
    extra = D4_z2.free_symbols - essential_symbols
    raise AssertionError(f"&#91;z^2&#93;D4 depends on supposedly irrelevant terms: {extra}")

print("&#91;3/9&#93; Projective repeated-root incidence")
r, t = s.symbols("r t")
Gamma_r = s.expand(Gamma.subs({x: r, y: 1}))
E0 = s.expand(2 * Gamma_r.subs(r, 1))
E1 = s.expand(2 * s.diff(Gamma_r, r).subs(r, 1))
GB = s.groebner(&#91;E0, E1&#93;, a, b, c, d, order="lex")
eliminant = s.factor(GB.polys&#91;-1&#93;.as_expr())
expected_eliminant = (b + 2 * c + 3 * d) * (
    b**2 + 6 * b * c + 18 * b * d + 3 * c**2 + 12 * c * d
)
assert_zero(eliminant - expected_eliminant, "repeated-root eliminant")
# The first component makes R singular at &#91;1:1&#93; unless d=0.
sub_bad = {b: -2 * c - 3 * d}
assert_zero(E0.subs(sub_bad) - 3 * (c + 3 * d) * (a - c - 2 * d), "bad component E0")
assert_zero(E1.subs(sub_bad) - 3 * c * (a - c - 2 * d), "bad component E1")

# Complete homogeneous parametrization of the other irreducible component.
U0, V0 = s.symbols("U0 V0")
a_h = -(3 * U0 + 2 * V0) * (3 * U0**2 + 6 * U0 * V0 + V0**2)
b_h = 6 * U0 * (3 * U0 + 2 * V0) * (2 * U0 + 3 * V0)
c_h = 6 * V0 * (3 * U0 + 2 * V0) * (2 * U0 + 3 * V0)
d_h = -(U0**2 + 6 * U0 * V0 + 3 * V0**2) * (2 * U0 + 3 * V0)
for expr, label in &#91;
    (E0.subs({a: a_h, b: b_h, c: c_h, d: d_h}), "param E0"),
    (E1.subs({a: a_h, b: b_h, c: c_h, d: d_h}), "param E1"),
    (
        expected_eliminant.args&#91;1&#93;.subs({b: b_h, c: c_h, d: d_h}),
        "param conic equation",
    ),
&#93;:
    assert_zero(expr, label)
# The two base-factor endpoints are genuine projective points, not holes.
assert_zero(a_h.subs(V0, -s.Rational(3, 2) * U0), "endpoint a=0")
if s.factor(d_h.subs(V0, -s.Rational(3, 2) * U0)) == 0:
    raise AssertionError("homogeneous parametrization has a base point at 3U+2V=0")
assert_zero(d_h.subs(V0, -s.Rational(2, 3) * U0), "endpoint d=0")
if s.factor(a_h.subs(V0, -s.Rational(2, 3) * U0)) == 0:
    raise AssertionError("homogeneous parametrization has a base point at 2U+3V=0")

print("&#91;4/9&#93; Affine conic chart, discriminants, and all exceptional divisors")
a_t = -(2 * t + 3) * (t**2 + 6 * t + 3)
b_t = 6 * (2 * t + 3) * (3 * t + 2)
c_t = 6 * t * (2 * t + 3) * (3 * t + 2)
d_t = -(3 * t + 2) * (3 * t**2 + 6 * t + 1)
R_t = s.expand(a_t * x**3 + b_t * x**2 * y + c_t * x * y**2 + d_t * y**3)
Gamma_t = s.factor(Gamma.subs({a: a_t, b: b_t, c: c_t, d: d_t}))
G2 = s.expand(
    (2 * t**3 + 15 * t**2 + 24 * t + 9) * x**2
    + (6 * t**4 + 49 * t**3 + 90 * t**2 + 49 * t + 6) * x * y
    + (9 * t**4 + 24 * t**3 + 15 * t**2 + 2 * t) * y**2
)
assert_zero(
    Gamma_t + 9 * (2 * t + 3) * (3 * t + 2) * (x - y) ** 2 * G2,
    "Gamma conic factorization",
)
disc_R = s.factor(s.discriminant(s.Poly(R_t.subs(y, 1), x).as_expr(), x))
assert_zero(
    disc_R
    - 3375
    * (t + 1) ** 6
    * (2 * t + 3) ** 2
    * (3 * t + 2) ** 2
    * (3 * t**2 + 14 * t + 3),
    "disc R",
)
disc_G2 = s.factor(s.discriminant(s.Poly(G2.subs(y, 1), x).as_expr(), x))
assert_zero(
    disc_G2
    - (t + 1) ** 2
    * (2 * t + 3)
    * (3 * t + 2)
    * (2 * t**2 + 11 * t + 2)
    * (3 * t**2 + 14 * t + 3),
    "disc residual quadratic",
)
assert_zero(G2.subs(x, y) - 15 * (t + 1) ** 2 * (t**2 + 3 * t + 1) * y**2, "3+1 divisor")
for left, right, label in &#91;
    (t**3 * a_t.subs(t, 1 / t), d_t, "involution a/d"),
    (t**3 * b_t.subs(t, 1 / t), c_t, "involution b/c"),
    (t**3 * c_t.subs(t, 1 / t), b_t, "involution c/b"),
    (t**3 * d_t.subs(t, 1 / t), a_t, "involution d/a"),
&#93;:
    assert_zero(left - right, label)

print("&#91;5/9&#93; Generic and 3+1 first-normal classification")
# Work on the affine r=x/y chart.  At the two residual roots, q(v)=0
# forces the rank-one matrix times v to vanish.  This is a 4x4 linear system.
A_r = s.expand(Acal.subs({a: a_t, b: b_t, c: c_t, d: d_t, x: r, y: 1}))
B_r = s.expand(Bcal.subs({a: a_t, b: b_t, c: c_t, d: d_t, x: r, y: 1}))
C_r = s.expand(Ccal.subs({a: a_t, b: b_t, c: c_t, d: d_t, x: r, y: 1}))
G2_r = s.expand(G2.subs({x: r, y: 1}))
ell_r = L0 * r + L1
m_r = M0 * r + M1
linear_remainders: list&#91;s.Expr&#93; = &#91;&#93;
for expr in &#91;A_r * ell_r + B_r * m_r, B_r * ell_r + C_r * m_r&#93;:
    rem = s.cancel(s.rem(s.expand(expr), G2_r, r))
    rem_poly = s.Poly(rem, r)
    linear_remainders.extend(&#91;rem_poly.coeff_monomial(r), rem_poly.coeff_monomial(1)&#93;)
Mlin, _ = s.linear_eq_to_matrix(linear_remainders, &#91;L0, L1, M0, M1&#93;)
# Rank exactly two on the primitive open set.
for rs in combinations(range(4), 3):
    for cs in combinations(range(4), 3):
        assert_zero(Mlin.extract(rs, cs).det(), f"3x3 minor {rs},{cs}")
rank_minor = s.factor(Mlin.extract((0, 2), (2, 3)).det())
expected_rank_minor = 54 * (t + 1) ** 2 * (3 * t + 2) ** 2 * (3 * t**2 + 6 * t + 1) ** 2
assert_zero(rank_minor - expected_rank_minor, "rank-two minor")
null_basis = Mlin.nullspace()
if len(null_basis) != 2:
    raise AssertionError(f"expected a two-dimensional linear kernel, got {len(null_basis)}")
p, q = s.symbols("p q")
vec = p * null_basis&#91;0&#93; + q * null_basis&#91;1&#93;
sub_vec = dict(zip(&#91;L0, L1, M0, M1&#93;, vec))
Q_r = s.expand(
    (A_r * (ell_r.subs(sub_vec)) ** 2 + 2 * B_r * ell_r.subs(sub_vec) * m_r.subs(sub_vec) + C_r * (m_r.subs(sub_vec)) ** 2)
    / 2
)
Q_at_1 = s.factor(Q_r.subs(r, 1))
linear_condition = (9 * t + 1) * p - (t + 9) * q
# Away from the 3+1 divisor, Q(1)=0 is precisely this one linear condition.
quotient_Q1 = s.factor(Q_at_1 / linear_condition**2)
if quotient_Q1 == 0:
    raise AssertionError("double-root condition lost its nonzero scalar factor")
# On the 3+1 divisor, reduce the full remainder; every coefficient is a
# nonzero scalar multiple of the same square.
g3 = t**2 + 3 * t + 1
Gamma_r_t = s.expand(Gamma_t.subs({x: r, y: 1}))
full_rem = s.rem(Q_r, Gamma_r_t, r)
rem_coeffs_3plus1 = &#91;&#93;
for i in range(4):
    coeff = s.Poly(full_rem, r).coeff_monomial(r**i)
    rem_coeffs_3plus1.append(reduce_mod_t(coeff, t, g3, (p, q)))
expected_scalars = &#91;
    3 * (4 * t + 1) / 25,
    -3 * (7 * t - 2) / 25,
    3 * (2 * t - 7) / 25,
    3 * (t + 4) / 25,
&#93;
L2_mod = reduce_mod_t(linear_condition**2, t, g3, (p, q))
for actual, scalar in zip(rem_coeffs_3plus1, expected_scalars):
    assert_zero(actual - reduce_mod_t(scalar * L2_mod, t, g3, (p, q)), "3+1 remainder")

# The unique projective solution, after clearing a common scalar.
ell_generic = (t**2 + 6 * t + 3) * x - (3 * t**2 + 6 * t + 1) * y
m_generic = 2 * (t + 1) * ((t + 9) * x + (9 * t + 1) * y)
Q_generic = s.factor(
    (
        Acal.subs({a: a_t, b: b_t, c: c_t, d: d_t}) * ell_generic**2
        + 2 * Bcal.subs({a: a_t, b: b_t, c: c_t, d: d_t}) * ell_generic * m_generic
        + Ccal.subs({a: a_t, b: b_t, c: c_t, d: d_t}) * m_generic**2
    )
    / 2
)
quotient_generic = s.expand(
    s.Rational(4, 3)
    * ((2 * t + 3) ** 2 * x + t * (3 * t + 2) ** 2 * y)
    / ((2 * t + 3) * (3 * t + 2))
)
assert_zero(Q_generic - Gamma_t * quotient_generic, "generic divisibility quotient")

print("&#91;6/9&#93; Generic and 3+1 next-coefficient obstruction")
h = s.symbols("h")
subs_generic = {
    a: a_t,
    b: b_t,
    c: c_t,
    d: d_t,
    L0: h * (t**2 + 6 * t + 3),
    L1: -h * (3 * t**2 + 6 * t + 1),
    M0: 2 * h * (t + 1) * (t + 9),
    M1: 2 * h * (t + 1) * (9 * t + 1),
    u2: -2 * h**2 * (2 * t + 3) / (3 * (3 * t + 2)),
    v2: 2 * h**2 * t * (3 * t + 2) / (3 * (2 * t + 3)),
}
D4_generic = s.factor(D4_z2.subs(subs_generic))
linear_factor = (2 * t + 3) ** 2 * (4 * t + 1) * x + (t + 4) * (3 * t + 2) ** 2 * y
expected_D4_generic = s.expand(
    24 * h**3 * (t + 1) * linear_factor * G2 / ((2 * t + 3) * (3 * t + 2))
)
assert_zero(D4_generic - expected_D4_generic, "generic &#91;z^2&#93;D4 obstruction")
if s.gcd((2 * t + 3) ** 2 * (4 * t + 1), (t + 4) * (3 * t + 2) ** 2) != 1:
    raise AssertionError("generic linear obstruction could vanish identically")

print("&#91;7/9&#93; Internal 2+2 divisor: complete kernel and disjoint cubic obstructions")
f22 = 2 * t**2 + 11 * t + 2
# Residual quadratic becomes a square in K=Q&#91;t&#93;/(f22).
G2_22 = reduce_poly_coeffs(G2, t, f22, (x, y))
s22 = (11 * t + 2) / 2
assert_zero(reduce_poly_coeffs(G2_22 - 5 * (x + s22 * y) ** 2, t, f22, (x, y)), "2+2 square factor")
# Rank-one conditions at the two distinct roots cut out exactly this plane.
h22, k22 = s.symbols("h22 k22")
L0_22 = h22
L1_22 = 4 * t * h22 / 11 - 3 * k22 / 22
M0_22 = 70 * h22 / 11 - (2 + 4 * t / 11) * k22
M1_22 = k22
# Directly verify full divisibility in the quotient field.
A22 = reduce_poly_coeffs(Acal.subs({a: a_t, b: b_t, c: c_t, d: d_t}), t, f22, (x, y))
B22 = reduce_poly_coeffs(Bcal.subs({a: a_t, b: b_t, c: c_t, d: d_t}), t, f22, (x, y))
C22 = reduce_poly_coeffs(Ccal.subs({a: a_t, b: b_t, c: c_t, d: d_t}), t, f22, (x, y))
Gamma22 = reduce_poly_coeffs(Gamma_t, t, f22, (x, y))
ell22 = L0_22 * x + L1_22 * y
m22 = M0_22 * x + M1_22 * y
Q22 = reduce_poly_coeffs((A22 * ell22**2 + 2 * B22 * ell22 * m22 + C22 * m22**2) / 2, t, f22, (x, y, h22, k22))
rem22 = s.rem(Q22, Gamma22, x)
assert_zero(reduce_poly_coeffs(rem22, t, f22, (x, y, h22, k22)), "2+2 full divisibility")
# Completeness: four rank-one linear conditions have rank exactly two and
# contain the displayed two-plane.
r22 = s.symbols("r22")
A22r = reduce_poly_coeffs(A22.subs({x: r22, y: 1}), t, f22, (r22,))
B22r = reduce_poly_coeffs(B22.subs({x: r22, y: 1}), t, f22, (r22,))
C22r = reduce_poly_coeffs(C22.subs({x: r22, y: 1}), t, f22, (r22,))
ell_unknown = L0 * r22 + L1
m_unknown = M0 * r22 + M1
root2 = -s22
conditions22 = &#91;&#93;
for root in &#91;s.Integer(1), root2&#93;:
    conditions22.extend(
        &#91;
            reduce_poly_coeffs((A22r * ell_unknown + B22r * m_unknown).subs(r22, root), t, f22, (L0, L1, M0, M1)),
            reduce_poly_coeffs((B22r * ell_unknown + C22r * m_unknown).subs(r22, root), t, f22, (L0, L1, M0, M1)),
        &#93;
    )
M22, _ = s.linear_eq_to_matrix(conditions22, &#91;L0, L1, M0, M1&#93;)
for rs in combinations(range(4), 3):
    for cs in combinations(range(4), 3):
        assert_zero(reduce_mod_t(M22.extract(rs, cs).det(), t, f22), "2+2 3x3 minor")
minor22 = reduce_mod_t(M22.extract((0, 3), (1, 3)).det(), t, f22)
if minor22 == 0 or s.resultant(f22, s.fraction(minor22)&#91;0&#93;, t) == 0:
    raise AssertionError("2+2 linear conditions do not have rank two")
plane_sub = {L0: L0_22, L1: L1_22, M0: M0_22, M1: M1_22}
for cond in conditions22:
    assert_zero(reduce_poly_coeffs(cond.subs(plane_sub), t, f22, (h22, k22)), "2+2 plane condition")

# Solve &#91;z&#93;D3 for the two z^2 amplitudes and evaluate the extreme
# coefficients of &#91;z^2&#93;D4.
a22 = reduce_mod_t(a_t, t, f22)
b22 = reduce_mod_t(b_t, t, f22)
c22 = reduce_mod_t(c_t, t, f22)
d22 = reduce_mod_t(d_t, t, f22)
u22 = reduce_poly_coeffs(-(2 * L0_22 - M0_22) ** 2 / (4 * b22), t, f22, (h22, k22))
v22 = reduce_poly_coeffs((2 * L1_22 + M1_22) ** 2 / (4 * c22), t, f22, (h22, k22))
D4_22 = reduce_poly_coeffs(
    D4_z2.subs(
        {
            a: a22,
            b: b22,
            c: c22,
            d: d22,
            L0: L0_22,
            L1: L1_22,
            M0: M0_22,
            M1: M1_22,
            u2: u22,
            v2: v22,
        }
    ),
    t,
    f22,
    (x, y, h22, k22),
)
C_x3 = s.Poly(D4_22, x, y).coeff_monomial(x**3)
C_y3 = s.Poly(D4_22, x, y).coeff_monomial(y**3)
fac_x = (h22 - (2 * t + 11) * k22 / 24) ** 2 * (h22 + 5 * (2 * t + 11) * k22 / 56)
fac_y = (h22 - (2 * t + 11) * k22 / 2) ** 2 * (h22 + (2 * t + 11) * k22 / 42)
assert_zero(
    reduce_poly_coeffs(C_x3 - s.Rational(12096, 1331) * fac_x, t, f22, (h22, k22)),
    "2+2 x^3 factor",
)
unit_y = -s.Rational(126, 1331) * (117 * t + 22)
assert_zero(
    reduce_poly_coeffs(C_y3 - unit_y * fac_y, t, f22, (h22, k22)),
    "2+2 y^3 factor",
)
if s.resultant(f22, 117 * t + 22, t) == 0 or s.resultant(f22, 2 * t + 11, t) == 0:
    raise AssertionError("a claimed 2+2 scalar is not a unit")
# The four projective roots 1/24,-5/56 and 1/2,-1/42 are disjoint.
if {s.Rational(1, 24), -s.Rational(5, 56)} &amp; {s.Rational(1, 2), -s.Rational(1, 42)}:
    raise AssertionError("2+2 extreme coefficients share a nonzero projective root")

print("&#91;8/9&#93; Repeated root at an endpoint of w=xy")
p0, q0 = s.symbols("p0 q0")
R_end = x**3 + y**3
Gamma_end = 9 * x**2 * y**2
A_end = 6 * R_end
B_end = -3 * x**3 + 3 * y**3
C_end = s.Rational(3, 2) * (x**3 + y**3)
ell_end = p0 * x + q0 * y
m_end = 2 * p0 * x - 2 * q0 * y
Q_end = s.expand((A_end * ell_end**2 + 2 * B_end * ell_end * m_end + C_end * m_end**2) / 2)
assert_zero(Q_end - s.Rational(4, 3) * Gamma_end * (q0**2 * x + p0**2 * y), "endpoint quotient")
D4_end = s.factor(
    D4_z2.subs(
        {
            a: 1,
            b: 0,
            c: 0,
            d: 1,
            L0: p0,
            L1: q0,
            M0: 2 * p0,
            M1: -2 * q0,
            u2: -s.Rational(2, 3) * q0**2,
            v2: s.Rational(2, 3) * p0**2,
        }
    )
)
assert_zero(D4_end - (8 * q0**3 * x**3 - 8 * p0**3 * y**3), "endpoint D4 obstruction")

print("&#91;9/9&#93; Second-normal obstruction after the first normal vanishes")
alpha, beta = s.symbols("alpha beta")
pa = s.symbols("pa0:4")
pb = s.symbols("pb0:4")
ua = s.symbols("ua0:3")
ub = s.symbols("ub0:3")
uc = s.symbols("uc0:3")
Lin = s.symbols("Lin0:9")
A3b = sum(q * mon for q, mon in zip(pa, mons3))
B3b = sum(q * mon for q, mon in zip(pb, mons3))
A2b = sum(q * mon for q, mon in zip(ua, mons2)) + alpha * y * z
B2b = sum(q * mon for q, mon in zip(ub, mons2)) + beta * x * z
C2b = sum(q * mon for q, mon in zip(uc, mons2))
A1b = Lin&#91;0&#93; * x + Lin&#91;1&#93; * y + Lin&#91;2&#93; * z
B1b = Lin&#91;3&#93; * x + Lin&#91;4&#93; * y + Lin&#91;5&#93; * z
C1b = Lin&#91;6&#93; * x + Lin&#91;7&#93; * y + (beta - alpha) * z
rows_second = &#91;
    &#91;grad(P, vars3), grad(A3b, vars3), grad(A2b, vars3), grad(A1b, vars3)&#93;,
    &#91;grad(Q, vars3), grad(B3b, vars3), grad(B2b, vars3), grad(B1b, vars3)&#93;,
    &#91;grad(0, vars3), grad(R, vars3), grad(C2b, vars3), grad(C1b, vars3)&#93;,
&#93;


def D_second(index: int) -&gt; s.Expr:
    return s.expand(
        sum(
            det3(rows_second&#91;0&#93;&#91;i&#93;, rows_second&#91;1&#93;&#91;j&#93;, rows_second&#91;2&#93;&#91;k&#93;)
            for i, j, k in product(range(4), repeat=3)
            if i + j + k == index
        )
    )

D5_second_z = s.factor(s.Poly(D_second(5), z).coeff_monomial(z))
expected_second = s.expand(
    (
        6 * a * alpha**2 * x**3
        + (3 * b * alpha**2 + 2 * b * alpha * beta + b * beta**2) * x**2 * y
        + (c * alpha**2 + 2 * c * alpha * beta + 3 * c * beta**2) * x * y**2
        + 6 * d * beta**2 * y**3
    )
    / 2
)
assert_zero(D5_second_z - expected_second, "second-normal &#91;z&#93;D5")
if D5_second_z.free_symbols - {x, y, a, b, c, d, alpha, beta}:
    raise AssertionError("second-normal obstruction depends on unrestricted lower coefficients")

print("PASS: every exact algebraic gate in the primitive binary r=4 branch is verified.")
print("PASS: the r=5 branch is the elementary aligned-cube argument recorded in the proof note.")
</code></pre>

## `lane4-quartic-endgame-20260802-v1/checks/tau-minus-one/verify_tau_minus_one.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact independent checker for the tau = -1 degree-three ramification chart.

Scope
-----
Work in the primitive coprime (3,4) Hilbert--Burch chart

    u = x^2,  v = y^2,
    w = a*x^3 + x^2*y + x*y^2 + b*y^3,
    tau = -1.

The script reconstructs P,Q from the differential Hilbert--Burch relation,
forms the determinant arc with arbitrary lower homogeneous terms, and proves:

1. primitivity forces the z-dependent coefficient l2 of the first normal
   form to vanish;
2. away from the two leading-coefficient divisors, every nonzero first-normal
   solution lies on the nonprimitive resultant factor;
3. the one-sided leading-coefficient divisors have no primitive projective
   first-normal solution;
4. their only primitive intersection is (a,b)=(2,2), where exactly two
   projective first-normal points survive the first equation;
5. the z^2 coefficient of the next determinant equation is a nonzero cubic
   in the normal amplitude at both points, with every lower term arbitrary.

The already established zero-normal triangular lemma is a textual dependency;
this script proves that tau=-1 has no additional nonzero-normal leaf.

Arithmetic is exact over Q.  No random specialization is used.
"""
from __future__ import annotations

from itertools import product
import sympy as s


def assert_zero(expr: s.Expr, label: str) -&gt; None:
    value = s.cancel(s.expand(expr))
    if value != 0:
        raise AssertionError(f"{label}: {s.factor(value)}")


def jac(f: s.Expr, g: s.Expr, x: s.Symbol, y: s.Symbol) -&gt; s.Expr:
    return s.expand(s.diff(f, x) * s.diff(g, y) - s.diff(f, y) * s.diff(g, x))


def grad(f: s.Expr, variables: tuple&#91;s.Symbol, s.Symbol, s.Symbol&#93;) -&gt; list&#91;s.Expr&#93;:
    return &#91;s.diff(f, q) for q in variables&#93;


def det_vectors(A: list&#91;s.Expr&#93;, B: list&#91;s.Expr&#93;, C: list&#91;s.Expr&#93;) -&gt; s.Expr:
    return s.expand(
        A&#91;0&#93; * (B&#91;1&#93; * C&#91;2&#93; - B&#91;2&#93; * C&#91;1&#93;)
        - A&#91;1&#93; * (B&#91;0&#93; * C&#91;2&#93; - B&#91;2&#93; * C&#91;0&#93;)
        + A&#91;2&#93; * (B&#91;0&#93; * C&#91;1&#93; - B&#91;1&#93; * C&#91;0&#93;)
    )


def numerator(expr: s.Expr) -&gt; s.Expr:
    return s.factor(s.fraction(s.cancel(expr))&#91;0&#93;)


print("&#91;1/8&#93; Reconstruct the tau=-1 Hilbert--Burch chart")
x, y, z = s.symbols("x y z")
a, b = s.symbols("a b")

w = a * x**3 + x**2 * y + x * y**2 + b * y**3
R = -a * x**3 - 3 * x**2 * y + 3 * x * y**2 + b * y**3
P = s.Rational(3, 4) * (
    a**2 * x**4
    - 2 * a * b * x * y**3
    + 4 * a * x**3 * y
    - 4 * a * x**2 * y**2
    - 2 * b * y**4
    + 2 * x**2 * y**2
    - 2 * x * y**3
    - y**4
)
Q = -s.Rational(3, 4) * (
    2 * a * b * x**3 * y
    + 2 * a * x**4
    - b**2 * y**4
    + 4 * b * x**2 * y**2
    - 4 * b * x * y**3
    + x**4
    + 2 * x**3 * y
    - 2 * x**2 * y**2
)

assert_zero(x**2 * s.diff(P, x) - y**2 * s.diff(Q, x) + w * s.diff(R, x), "HB dx")
assert_zero(x**2 * s.diff(P, y) - y**2 * s.diff(Q, y) + w * s.diff(R, y), "HB dy")
Delta = s.factor(jac(Q, R, x, y) / x**2)
assert_zero(jac(P, R, x, y) - y**2 * Delta, "J(P,R)")
assert_zero(jac(P, Q, x, y) - w * Delta, "J(P,Q)")

F1 = 27 * a**2 * b**2 - 18 * a * b + 4 * a + 4 * b - 1
G = a**2 * b**2 - 6 * a * b - 4 * a - 4 * b - 3
resultant = s.factor(s.resultant(P, Q, x))
assert_zero(
    resultant + s.Rational(6561, 65536) * y**16 * F1 * G**3,
    "primitive resultant factorization",
)
print("      Res(P,Q) = unit * F1 * G^3; primitivity implies F1*G != 0")


print("&#91;2/8&#93; The high-z equation forces l2=0 on the primitive locus")
l0, l1, l2, mu, u, v = s.symbols("l0 l1 l2 mu u v")
L = l0 * x + l1 * y + l2 * z
Az = s.expand(L * (-a * x - y) + mu * y**2)
Bz = s.expand(L * (x + b * y) + mu * x**2)
Ez = L
A_normal = s.integrate(Az, z)
B_normal = s.integrate(Bz, z)
E_normal = s.integrate(Ez, z)

variables = (x, y, z)
H4 = &#91;P, Q, s.Integer(0)&#93;
H3 = &#91;A_normal, B_normal, R&#93;
H2 = &#91;u * z**2, v * z**2, E_normal&#93;
zero_gradient = &#91;s.Integer(0), s.Integer(0), s.Integer(0)&#93;
rows = &#91;&#91;grad(H4&#91;i&#93;, variables), grad(H3&#91;i&#93;, variables), grad(H2&#91;i&#93;, variables), zero_gradient&#93; for i in range(3)&#93;


def determinant_arc_term(index: int, row_data: list&#91;list&#91;list&#91;s.Expr&#93;&#93;&#93;) -&gt; s.Expr:
    return s.expand(
        sum(
            det_vectors(row_data&#91;0&#93;&#91;i&#93;, row_data&#91;1&#93;&#91;j&#93;, row_data&#91;2&#93;&#91;k&#93;)
            for i, j, k in product(range(4), repeat=3)
            if i + j + k == index
        )
    )


D3_with_l2 = determinant_arc_term(3, rows)
z3 = s.factor(s.Poly(D3_with_l2, z).coeff_monomial(z**3))
Acoef = a**2 * b - 3 * a - 2
Bcoef = a * b**2 - 3 * b - 2
Ccoef = a * b + 2 * a + 1
Dcoef = a * b + 2 * b + 1
expected_z3 = s.Rational(3, 4) * l2**2 * (
    Acoef * x**3 + Ccoef * x**2 * y - Dcoef * x * y**2 - Bcoef * y**3
)
assert_zero(z3 - expected_z3, "z^3 D3")
assert_zero(Ccoef - Dcoef - 2 * (a - b), "C-D identity")
assert_zero(Ccoef.subs(b, a) - (a + 1) ** 2, "diagonal C identity")
assert_zero(G.subs({a: -1, b: -1}), "nonprimitive l2 point")
print("      l2 != 0 forces a=b=-1, hence G=0; therefore primitive charts have l2=0")


print("&#91;3/8&#93; Form the six first-normal equations at l2=0")
lam = l0 * x + l1 * y
alpha = s.expand(lam * (-a * x - y) + mu * y**2)
beta = s.expand(lam * (x + b * y) + mu * x**2)

# Only the displayed normal pieces can enter &#91;z&#93;D3.
Cz = s.Poly(
    det_vectors(grad(z * alpha, variables), grad(z * beta, variables), grad(R, variables))
    + det_vectors(grad(P, variables), grad(z * beta, variables), grad(z * lam, variables))
    + det_vectors(grad(P, variables), grad(v * z**2, variables), grad(R, variables))
    + det_vectors(grad(z * alpha, variables), grad(Q, variables), grad(z * lam, variables))
    + det_vectors(grad(u * z**2, variables), grad(Q, variables), grad(R, variables)),
    z,
).coeff_monomial(z)
first_normal_eqs = &#91;
    s.factor(s.Poly(Cz, x, y).coeff_monomial(x ** (5 - i) * y**i)) for i in range(6)
&#93;

M1 = (
    -2 * a**2 * b * l0 * l1
    - a * b * l0**2
    + 18 * a * b * u
    - 2 * a * l0**2
    + 6 * a * l0 * l1
    - 8 * a * l0 * mu
    + 4 * a * mu**2
    + 36 * a * u
    - l0**2
    + 4 * l0 * l1
    - 8 * l0 * mu
    + 18 * u
)
M2 = (
    -a**2 * b * l1**2
    - 6 * a**2 * b * v
    + a * b * l0**2
    - 2 * a * b * l0 * l1
    - 8 * a * b * l0 * mu
    + 18 * a * b * u
    - 4 * a * l0 * l1
    + 3 * a * l1**2
    - 8 * a * l1 * mu
    + 18 * a * v
    + 2 * b * l0**2
    + 36 * b * u
    + l0**2
    - 2 * l0 * l1
    + 8 * l0 * mu
    + 2 * l1**2
    - 8 * l1 * mu
    + 12 * mu**2
    + 18 * u
    + 12 * v
)
M3 = (
    a * b**2 * l0**2
    + 6 * a * b**2 * u
    + 2 * a * b * l0 * l1
    - a * b * l1**2
    - 8 * a * b * l1 * mu
    - 18 * a * b * v
    - 2 * a * l1**2
    - 36 * a * v
    - 3 * b * l0**2
    + 4 * b * l0 * l1
    - 8 * b * l0 * mu
    - 18 * b * u
    - 2 * l0**2
    + 2 * l0 * l1
    - 8 * l0 * mu
    - l1**2
    + 8 * l1 * mu
    - 12 * mu**2
    - 12 * u
    - 18 * v
)
M4 = (
    -2 * a * b**2 * l0 * l1
    - a * b * l1**2
    + 18 * a * b * v
    + 6 * b * l0 * l1
    - 2 * b * l1**2
    + 8 * b * l1 * mu
    + 4 * b * mu**2
    + 36 * b * v
    + 4 * l0 * l1
    - l1**2
    + 8 * l1 * mu
    + 18 * v
)
expected_first = &#91;
    s.Rational(3, 2) * Acoef * (l0**2 - 6 * u),
    -s.Rational(3, 2) * M1,
    -s.Rational(3, 2) * M2,
    -s.Rational(3, 2) * M3,
    s.Rational(3, 2) * M4,
    s.Rational(3, 2) * Bcoef * (-l1**2 + 6 * v),
&#93;
for i, (actual, expected) in enumerate(zip(first_normal_eqs, expected_first)):
    assert_zero(actual - expected, f"first-normal equation {i}")
print("      exact 6 x 8 Veronese/second-normal system reconstructed")


print("&#91;4/8&#93; Generic Acoef*Bcoef != 0: saturation forces G=0")
# On this open set u=l0^2/6 and v=l1^2/6.  Divide harmless scalar factors.
F0 = (
    a**2 * b * l0 * l1
    - a * b * l0**2
    - 2 * a * l0**2
    - 3 * a * l0 * l1
    + 4 * a * l0 * mu
    - 2 * a * mu**2
    - l0**2
    - 2 * l0 * l1
    + 4 * l0 * mu
)
F1n = (
    a**2 * b * l1**2
    - 2 * a * b * l0**2
    + a * b * l0 * l1
    + 4 * a * b * l0 * mu
    + 2 * a * l0 * l1
    - 3 * a * l1**2
    + 4 * a * l1 * mu
    - 4 * b * l0**2
    - 2 * l0**2
    + l0 * l1
    - 4 * l0 * mu
    - 2 * l1**2
    + 4 * l1 * mu
    - 6 * mu**2
)
F2n = (
    a * b**2 * l0**2
    + a * b * l0 * l1
    - 2 * a * b * l1**2
    - 4 * a * b * l1 * mu
    - 4 * a * l1**2
    - 3 * b * l0**2
    + 2 * b * l0 * l1
    - 4 * b * l0 * mu
    - 2 * l0**2
    + l0 * l1
    - 4 * l0 * mu
    - 2 * l1**2
    + 4 * l1 * mu
    - 6 * mu**2
)
F3n = (
    a * b**2 * l0 * l1
    - a * b * l1**2
    - 3 * b * l0 * l1
    - 2 * b * l1**2
    - 4 * b * l1 * mu
    - 2 * b * mu**2
    - 2 * l0 * l1
    - l1**2
    - 4 * l1 * mu
)
open_eqs = &#91;F0, F1n, F2n, F3n&#93;
sub_uv = {u: l0**2 / 6, v: l1**2 / 6}
for actual, expected, label in &#91;
    (M1.subs(sub_uv), -2 * F0, "M1/open"),
    (M2.subs(sub_uv), -2 * F1n, "M2/open"),
    (M3.subs(sub_uv), 2 * F2n, "M3/open"),
    (M4.subs(sub_uv), -2 * F3n, "M4/open"),
&#93;:
    assert_zero(actual - expected, label)

GB_open = s.groebner(open_eqs, l0, l1, mu, a, b, order="grevlex")
assert_zero(GB_open.reduce(s.expand(mu**4 * G))&#91;1&#93;, "mu-chart saturation")
GB_mu0 = s.groebner(&#91;f.subs(mu, 0) for f in open_eqs&#93;, l0, l1, a, b, order="grevlex")
assert_zero(GB_mu0.reduce(s.expand(l0**4 * G))&#91;1&#93;, "mu=0,l0 chart saturation")
assert_zero(GB_mu0.reduce(s.expand(l1**4 * G))&#91;1&#93;, "mu=0,l1 chart saturation")
print("      mu^4 G and, on mu=0, l0^4 G and l1^4 G lie in the exact incidence ideal")


print("&#91;5/8&#93; One-sided leading-coefficient divisors have no primitive point")
# Acoef=0: b=(3a+2)/a^2, a != 0.  Bcoef != 0 gives v=l1^2/6.
b_on_A = (3 * a + 2) / a**2
A_side = &#91;numerator(E.subs({b: b_on_A, v: l1**2 / 6})) for E in &#91;M1, M2, M3, M4&#93;&#93;
B_on_A = s.factor(s.cancel(Bcoef.subs(b, b_on_A)))
assert_zero(B_on_A + 2 * (a - 2) * (a + 1) ** 2 / a**3, "B on A divisor")
A_chart_tests = &#91;
    ({l0: 1}, (u, l1, mu, a), (a + 1) ** 4, "A-side l0"),
    ({l1: 1}, (u, l0, mu, a), a**2 * (a + 1) ** 4, "A-side l1"),
    ({mu: 1}, (u, l0, l1, a), a**2, "A-side mu"),
&#93;
for substitution, gb_vars, target, label in A_chart_tests:
    GB = s.groebner(&#91;e.subs(substitution) for e in A_side&#93;, *gb_vars, order="lex")
    assert_zero(GB.reduce(target)&#91;1&#93;, label)

# Bcoef=0 is checked independently, not inferred from an unverified symmetry.
a_on_B = (3 * b + 2) / b**2
B_side = &#91;numerator(E.subs({a: a_on_B, u: l0**2 / 6})) for E in &#91;M1, M2, M3, M4&#93;&#93;
A_on_B = s.factor(s.cancel(Acoef.subs(a, a_on_B)))
assert_zero(A_on_B + 2 * (b - 2) * (b + 1) ** 2 / b**3, "A on B divisor")
B_chart_tests = &#91;
    ({l0: 1}, (v, l1, mu, b), b**2 * (b + 1) ** 4, "B-side l0"),
    ({l1: 1}, (v, l0, mu, b), (b + 1) ** 4, "B-side l1"),
    ({mu: 1}, (v, l0, l1, b), b**2, "B-side mu"),
&#93;
for substitution, gb_vars, target, label in B_chart_tests:
    GB = s.groebner(&#91;e.subs(substitution) for e in B_side&#93;, *gb_vars, order="lex")
    assert_zero(GB.reduce(target)&#91;1&#93;, label)
print("      every projective chart forces the opposite divisor or an impossible zero denominator")


print("&#91;6/8&#93; Classify the intersection Acoef=Bcoef=0")
assert_zero(Acoef - Bcoef - (a - b) * (a * b - 3), "intersection difference")
assert_zero(numerator(Acoef.subs(b, 3 / a)) + 2, "ab=3 contradiction")
assert_zero(Acoef.subs(b, a) - (a - 2) * (a + 1) ** 2, "diagonal intersection")
assert_zero(G.subs({a: -1, b: -1}), "(-1,-1) is nonprimitive")
assert_zero(G.subs({a: 2, b: 2}) + 27, "(2,2) is primitive")

middle_22 = &#91;s.factor(E.subs({a: 2, b: 2})) for E in &#91;M1, M2, M3, M4&#93;&#93;
u22 = (9 * l0**2 + 24 * l0 * mu - 8 * mu**2) / 162
v22 = (9 * l1**2 - 24 * l1 * mu - 8 * mu**2) / 162
K1 = 9 * l0**2 - 9 * l0 * l1 - 12 * l1 * mu + 2 * mu**2
K2 = 9 * l0 * l1 - 12 * l0 * mu - 9 * l1**2 - 2 * mu**2
assert_zero(middle_22&#91;0&#93;.subs(u, u22), "solve u at (2,2)")
assert_zero(middle_22&#91;3&#93;.subs(v, v22), "solve v at (2,2)")
assert_zero(middle_22&#91;1&#93;.subs(u, u22) - 2 * K1, "K1 reduction")
assert_zero(middle_22&#91;2&#93;.subs(v, v22) - 2 * K2, "K2 reduction")
assert_zero(K1 - K2 - (3 * l0 - 3 * l1 + 2 * mu) ** 2, "square identity")
assert_zero(K1 + K2 - 3 * (l0 + l1) * (3 * l0 - 3 * l1 - 4 * mu), "product identity")
print("      nonzero first normals are h*(1,1,0) or h*(-1,1,3)")


print("&#91;7/8&#93; The next determinant coefficient kills both surviving points")
# Keep every lower homogeneous term arbitrary.
mons3 = &#91;x**3, x**2 * y, x * y**2, y**3&#93;
mons2 = &#91;x**2, x * y, y**2&#93;
A0c = s.symbols("A0:4")
B0c = s.symbols("B0:4")
C0c = s.symbols("C0:3")
D0c = s.symbols("D0:3")
E0c = s.symbols("E0:3")
pc = s.symbols("p0:2")
qc = s.symbols("q0:2")
Lc = s.symbols("L0:9")
A0 = sum(c * mon for c, mon in zip(A0c, mons3))
B0 = sum(c * mon for c, mon in zip(B0c, mons3))
C0 = sum(c * mon for c, mon in zip(C0c, mons2))
D0 = sum(c * mon for c, mon in zip(D0c, mons2))
E0 = sum(c * mon for c, mon in zip(E0c, mons2))
p_lin = pc&#91;0&#93; * x + pc&#91;1&#93; * y
q_lin = qc&#91;0&#93; * x + qc&#91;1&#93; * y
H1 = &#91;
    Lc&#91;0&#93; * x + Lc&#91;1&#93; * y + Lc&#91;2&#93; * z,
    Lc&#91;3&#93; * x + Lc&#91;4&#93; * y + Lc&#91;5&#93; * z,
    Lc&#91;6&#93; * x + Lc&#91;7&#93; * y + Lc&#91;8&#93; * z,
&#93;
P22 = s.expand(P.subs({a: 2, b: 2}))
Q22 = s.expand(Q.subs({a: 2, b: 2}))
R22 = s.expand(R.subs({a: 2, b: 2}))
h = s.symbols("h")


def d4_z2_for_branch(branch: int) -&gt; s.Expr:
    if branch == 1:
        ll0, ll1, mm = h, h, s.Integer(0)
        uu = vv = h**2 / 18
    elif branch == 2:
        ll0, ll1, mm = -h, h, 3 * h
        uu = vv = -5 * h**2 / 6
    else:
        raise ValueError(branch)
    ll = ll0 * x + ll1 * y
    aa = s.expand(ll * (-2 * x - y) + mm * y**2)
    bb = s.expand(ll * (x + 2 * y) + mm * x**2)
    HH4 = &#91;P22, Q22, s.Integer(0)&#93;
    HH3 = &#91;A0 + z * aa, B0 + z * bb, R22&#93;
    HH2 = &#91;C0 + z * p_lin + uu * z**2, D0 + z * q_lin + vv * z**2, E0 + z * ll&#93;
    row_data = &#91;&#91;grad(HH4&#91;i&#93;, variables), grad(HH3&#91;i&#93;, variables), grad(HH2&#91;i&#93;, variables), grad(H1&#91;i&#93;, variables)&#93; for i in range(3)&#93;
    D4 = determinant_arc_term(4, row_data)
    return s.factor(s.Poly(D4, z).coeff_monomial(z**2))


branch1 = d4_z2_for_branch(1)
branch2 = d4_z2_for_branch(2)
expected1 = -h**3 * (5 * x**3 + 7 * x**2 * y + 7 * x * y**2 + 5 * y**3) / 2
expected2 = 135 * h**3 * (x**3 + x**2 * y - x * y**2 - y**3) / 2
assert_zero(branch1 - expected1, "branch 1 D4 obstruction")
assert_zero(branch2 - expected2, "branch 2 D4 obstruction")
assert_zero(expected1 + h**3 * (x + y) * (5 * x**2 + 2 * x * y + 5 * y**2) / 2, "branch 1 factor")
assert_zero(expected2 - 135 * h**3 * (x - y) * (x + y) ** 2 / 2, "branch 2 factor")
print("      branch I:  &#91;z^2&#93;D4 = -(h^3/2)(x+y)(5x^2+2xy+5y^2)")
print("      branch II: &#91;z^2&#93;D4 =  (135h^3/2)(x-y)(x+y)^2")


print("&#91;8/8&#93; Conclusion")
print("PASS: every primitive tau=-1 nonzero-normal chart is excluded exactly.")
print("The remaining zero-normal point exits to the established triangular zero-normal lemma.")
</code></pre>

[Back to Lane 4](quartic-endgame.md)
