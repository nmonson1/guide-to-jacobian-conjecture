# Lane 4 proof-to-code crosswalk and evidence gaps

## 1. Reading rule

This table covers every computational family referenced by
`lane4-case-tree.csv`.

- **Exact public attachment** means that a source path or command is exposed
  with enough information to bind the calculation to one mathematical chart.
- **Missing public attachment** means that the prose reports a calculation but
  the selected public packet does not expose a complete file/hash/output
  interface.
- A script certifies only the polynomial identities or ideals it actually
  reconstructs. It does not certify the geometric classification that reaches
  its input chart.

The original packet used by this audit is pinned to private-source commit
`ed3137b5ce00f4f206fe1126b4fdc3bc5051b112`. Its selected public files include:

| Artifact | Published SHA-256 |
| --- | --- |
| `PROOF_CODE_CROSSWALK.md` | `529a23a6caf3e34ebaea3de6d1102998b7f5532d3b2f47d89704a781e19c34b7` |
| `case-tree/lane4-global-case-tree.md` | `82393d020cad9346365fe2c388baa7cdd5abb2a2e789eaf3b5e2590998c386d9` |
| `case-tree/lane4-case-tree.csv` | `63962c80bd4a6d61aa3e948109071b9b0393f40c3357bc5c5b0b90aa509ba5c3` |
| `proofs/10-structural-repairs-and-z2.tex` | `03db7a707edf9e4791545e8451fdc2fd7540cd9a026635e0212bd82d53c57a4b` |
| `proofs/20-conic-completion.tex` | `02aee17b2f75ae7deea2961d3dd66bb12290d5873182b70156386f6dcfc38398` |
| `proofs/30-rational-cubic.tex` | `7485acbd0d77bfd9a41763711199c1b1af490b88c9576645e604b84d100d8cec` |
| `proofs/50-high-ramification.tex` | `c30ac4269bfcc45047b6ff4a23b2c9372f09c18cea3ee97c6dbcabac20fb2901` |
| `proofs/60-tau-minus-one.tex` | `a818a9f2559de4f6d8b76d56e017c6d0bcfa75925f81cb7b3832728c83dccc74` |
| `replay_core.py` | `414571f93cb504116146004b02447b03827b64d27262c93985dc266210b264d6` |
| `checks/conic/verify_terminal_identities.py` | `dc1f6915b7256a14b84b3b28c10b12144b4f35f6010fd44807f52743ef186689` |
| `checks/high-ramification/verify_r4_high_ramification.py` | `bf490b014a79dfeba1dd26e0fbb195d0adfe53741ad93d63736ee0a395cc8c6d` |
| `checks/tau-minus-one/verify_tau_minus_one.py` | `3937d64a233eb6200feec829b774ac80c5714da305394242f47ad2c0f46551eb` |

## 2. Conventional structural interfaces added by this contribution

| Interface | Candidate proof | Independent audit check | Remaining boundary |
| --- | --- | --- | --- |
| Leading-image factorization | `structural-repairs.tex`, Proposition `prop:lane4-leading-image-direct` | `verify_structure_repairs.py` enumerates the four degree triples and detects the degree-two relative-closure regression example | specialist review of generic-line rationality, normalization, divisor-coprimality, and integration with the surrounding leading-rank argument |
| Weighted one-variable field | `structural-repairs.tex`, Lemma `lem:lane4-weighted-field` | validator checks the complete finite table `n=e d` for `n<=4` | specialist review of the homogeneous dependence and rational-field argument |
| Four-loci cover | `structural-repairs.tex`, Proposition `prop:lane4-four-loci` | validator checks the parity/fourth-power implication and the impossibility of `4 r=3 mu` for `mu=1,2,3` | specialist review of valuation conventions, overlap ownership, and theorem integration |

These checks test finite consequences of the prose proofs; they do not
mechanically prove the algebraic-geometric inputs.

## 3. Computational crosswalk

| Crosswalk ID | Tree leaves | Exact mathematical input | Public command / attachment | Certified output | Boundary not certified | Audit status |
| --- | --- | --- | --- | --- | --- | --- |
| `CW-CONIC-FAMILY` | `S3-CONIC-FIXED` | proper reduced conic; one of the stated orbit representatives; arbitrary permitted lower coefficients retained | `python replay_core.py --group conic`; full ten branches with `--full-conic`; core hash `414571...`; compact identity hash `dc1f69...` | pinned branch output comparison and displayed square/determinant identities | completeness of source/target orbit split and every invariant-zero sibling | compact attachment exact; raw per-branch hashes omitted |
| `CW-RATIONAL-CUBIC` | `S3-CUBIC` | proper reduced cusp/node; transverse or stated marked-point orbit | `python replay_core.py --group rational-cubic`; core hash `414571...` | transverse ranks/nullities, marked-node minor `12582912`, and displayed cusp coefficients | marked-point coverage, branch interchange at infinity, per-script hashes | group attachment exact; classification remains conventional |
| `CW-RATIONAL-QUARTIC` | `S3-QUARTIC` | proper quartic already reduced to tangent-syzygy type `(3,(1,2))` or `(2,(2,2))` | no selected Lane 4 file/hash interface | source reports exact terminal calculations | entire frontier preclassification and proof/code attachment | missing public attachment; `AUDIT-RQ-FRONTIER` remains |
| `CW-QUAD-SOURCE` | `S3-CONIC-PRIMITIVE`, `S2-QUAD-SOURCE` | one of nine quadratic-source charts, including its chosen nonzero minor | no per-chart filename, command, hash, or output in the selected packet | source reports nine exact chart eliminations | chart exhaustiveness, zero-minor siblings, independent sample identity | missing public attachment; `AUDIT-QUAD-XW` |
| `CW-PLANE-DEGREE` | `S2-R0`, `S2-R5` | straightened coordinate over `K=k(t)`; plane Keller pair over `overline K`; one coordinate degree in `{1,2,3,4,5,6,7,9}` | conventional theorem; dependency and descent proof in `proof-repairs.tex` | Appelgate--Onishi criterion after Nowicki--Nakai repair and Galois descent of the inverse | upstream coordinate lemma and separate birational-Keller implication | conventional import requiring citation/proof review |
| `CW-FOURTH-POWER` | `S2-FOURTH-POWER` | primitive coprime pencil containing a fourth power; aligned and zero-minor children separated | no selected standalone file/hash | source reports exact theorem bundle | normalization and every zero-pivot complement | missing public file-level attachment |
| `CW-CENTRALIZER` | `S2-NONBINARY-FIXED` | endpoint `(x^4,xR,0)`, `x` not dividing `R`, and `R` genuinely nonbinary | conventional proof in `proof-repairs.tex` | homogeneous kernel described by `k[x,R]` | common-generator/closed-polynomial theorem over `k(x)` | candidate conventional repair |
| `CW-BINARY-FIXED` | `S2-BINARY-FIXED-G123` | binary fixed factor of degree `1`, `2`, or `3` in its exact chart | source reports 38 groups and an internal manifest; selected packet omits the per-group map | reported exact divisor/intersection sweeps | theorem-to-group attachment, hashes, outputs, independent lineage | missing public attachment; `AUDIT-BINARY-FIXED-XW` |
| `CW-ZERO-MINOR` | `S2-ZERO-MINOR` | specified vanishing Hilbert--Burch minor with alternate pivots/rank children | no selected standalone command/hash | source reports exact zero-minor bundle | ownership of all pivot-zero intersections | missing public file-level attachment |
| `CW-RLE2` | `S2-RLE2`, `S2-R3-25` | primitive coprime binary pencil; regular/simple/double ramification or the earlier `(2,5)` owner | no selected standalone command/hash | source reports exact continuation bundle | ramification classification and all discriminant complements | missing public file-level attachment |
| `CW-TAU-MINUS-ONE` | `S2-R3-TAUM1` | `r=3`, type `(3,4)`, `tau=-1`, projective first-normal strata and stated unrestricted next layer | `python checks/tau-minus-one/verify_tau_minus_one.py`; SHA-256 `3937d64a...` | reconstruction of `P,Q,R`, resultant factors, saturation certificates, and two next-layer obstructions | upstream chart placement and zero-normal plane reduction | exact public attachment |
| `CW-Q4-F4` | `Q4-F4` | `r=3`, type `(3,4)`, exceptional weighted-inflection family; full unrestricted binary `H3,H2` and permitted `L` | `F4_INPUT_CONTRACT.md` and `f4-contract.schema.json` specify the required input; no complete contract instance or checker is public | only the fail-closed data/certificate protocol and regression checks in `verify_structure_repairs.py` | explicit `q4`, normalized `P,Q,R`, gauges, open product `S`, all `D6/D5` coefficients, and exceptional saturations | genuinely open; public data are insufficient for an honest elimination |
| `CW-R4` | `S2-R4` | primitive coprime binary pencil; `r=4`; generic, `3+1`, internal `2+2`, endpoint, and second-normal charts | `python checks/high-ramification/verify_r4_high_ramification.py`; SHA-256 `bf490b014...` | repeated-root parametrization, kernels, and terminal obstructions | upstream Hilbert--Burch placement and final plane reduction | exact public attachment |
| `CW-R5` | `S2-R5` | primitive `r=5`; aligned cube/fourth-power identities | supporting identities use the same high-ramification checker | exact aligned-power identities | cubic-coordinate lemma and plane theorem | exact shared attachment, not an independent lineage |
| `CW-D56-NORMAL-FORM` | `D56-BASEPOINT` | degree-five `(g,e)=(1,2)` fixed-factor basepoint with regular-sequence and nonconstant-ratio hypotheses | `python contributions/JCG-C-0014/verify_lane4_audit.py` | sample restriction `xy,y^2`, selected point, and lifted normal-form vanishings | Keller determinant equations on this quintic boundary | exact audit sample; boundary remains open |

## 4. Commands exposed by the original Lane 4 packet

```bash
python -m pip install -r requirements.txt
python replay_core.py --group structural
python replay_core.py --group conic
python replay_core.py --group rational-cubic
python replay_core.py --group conic --full-conic
python checks/high-ramification/verify_r4_high_ramification.py
python checks/tau-minus-one/verify_tau_minus_one.py
```

The public handoff embeds selected source text rather than a complete checkout
of all reported archives. This contribution records the published commands
and hashes but does not claim to have rerun absent files.

## 5. Independent checks in this contribution

```bash
python contributions/JCG-C-0014/verify_lane4_audit.py
python contributions/JCG-C-0014/verify_structure_repairs.py
```

Together the scripts check:

1. parentage and complement routing in the machine-readable tree;
2. declaration of every `CW-*` identifier used by that tree;
3. the plane-degree factor-count condition;
4. the cubic-centralizer homogeneity samples and pointed quintic sample;
5. the four solutions of `deg G + e k = 4` with `e>=2`;
6. the degree-two relative-closure counterexample;
7. the complete composite table `n=e d` in degree four;
8. the parity/fourth-power valuation implication;
9. the fixed-factor congruence for multiplicities `1,2,3`;
10. the fail-closed top-level shape of an eventual `Q4-F4` input instance.

These are audit and regression checks, not substitutes for the Program 2
terminal systems or for specialist proof review.
