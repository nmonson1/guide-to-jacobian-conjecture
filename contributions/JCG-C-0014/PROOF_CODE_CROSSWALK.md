# Lane 4 proof-to-code crosswalk and evidence gaps

## 1. Reading rule

This table covers every computational family referenced by
`lane4-case-tree.csv`.  “Exact public attachment” means that the public Lane 4
source packet identifies enough information to bind a mathematical leaf to a
specific file or command.  “Missing public attachment” is a negative audit
result: the mathematical prose may report a successful private or archival
replay, but this contribution does not invent filenames, hashes, or output
from that report.

The source packet is pinned to private-source commit
`ed3137b5ce00f4f206fe1126b4fdc3bc5051b112`.  The selected public Lane 4 files
have these published SHA-256 digests:

| Artifact | SHA-256 |
| --- | --- |
| `README.md` | `4cc314eb0ef7e1ec0447f21db5b5a7a7209fa3bb5274429647dc323519a1e96e` |
| `PROOF_CODE_CROSSWALK.md` | `529a23a6caf3e34ebaea3de6d1102998b7f5532d3b2f47d89704a781e19c34b7` |
| `case-tree/lane4-global-case-tree.md` | `82393d020cad9346365fe2c388baa7cdd5abb2a2e789eaf3b5e2590998c386d9` |
| `case-tree/lane4-case-tree.csv` | `63962c80bd4a6d61aa3e948109071b9b0393f40c3357bc5c5b0b90aa509ba5c3` |
| `proofs/10-structural-repairs-and-z2.tex` | `03db7a707edf9e4791545e8451fdc2fd7540cd9a026635e0212bd82d53c57a4b` |
| `proofs/20-conic-completion.tex` | `02aee17b2f75ae7deea2961d3dd66bb12290d5873182b70156386f6dcfc38398` |
| `proofs/30-rational-cubic.tex` | `7485acbd0d77bfd9a41763711199c1b1af490b88c9576645e604b84d100d8cec` |
| `proofs/40-span-three-corollary.tex` | `71315a0e2adb2b80f48ca873163e0da0e041c2246b5351130b16e37909e9797a` |
| `proofs/50-high-ramification.tex` | `c30ac4269bfcc45047b6ff4a23b2c9372f09c18cea3ee97c6dbcabac20fb2901` |
| `proofs/60-tau-minus-one.tex` | `a818a9f2559de4f6d8b76d56e017c6d0bcfa75925f81cb7b3832728c83dccc74` |
| `replay_core.py` | `414571f93cb504116146004b02447b03827b64d27262c93985dc266210b264d6` |
| `checks/conic/verify_terminal_identities.py` | `dc1f6915b7256a14b84b3b28c10b12144b4f35f6010fd44807f52743ef186689` |
| `checks/high-ramification/verify_r4_high_ramification.py` | `bf490b014a79dfeba1dd26e0fbb195d0adfe53741ad93d63736ee0a395cc8c6d` |
| `checks/tau-minus-one/verify_tau_minus_one.py` | `3937d64a233eb6200feec829b774ac80c5714da305394242f47ad2c0f46551eb` |

## 2. Crosswalk

| Crosswalk ID | Tree leaves | Proof locator and exact input hypotheses | Command / public input hash | Certified output or sample identity | Boundary not certified | Audit status |
| --- | --- | --- | --- | --- | --- | --- |
| `CW-CONIC-FAMILY` | `S3-CONIC-FIXED` | `proofs/20-conic-completion.tex`; proper reduced conic; one of the seven stated normal representatives; arbitrary lower coefficients retained as specified | `python replay_core.py --group conic`; core hash `414571...`; terminal identity hash `dc1f69...`; full ten branches: `python replay_core.py --group conic --full-conic` | fresh branch output is compared byte-for-byte with pinned output; compact checker verifies displayed square/determinant factorizations | completeness of source/target orbit split, stabilizer boundaries, and every vanishing chart | exact public attachment for compact dispatcher and terminal identities; raw branch hashes omitted |
| `CW-RATIONAL-CUBIC` | `S3-CUBIC` | `proofs/30-rational-cubic.tex`; proper reduced cusp/node; transverse or stated marked-point orbit | `python replay_core.py --group rational-cubic`; core hash `414571...` | transverse cusp rank 8/nullity 1; node rank 9/nullity 0; marked-node maximal minor `12582912`; fixed nonzero cusp coefficients on displayed branches | proper cubic classification, marked-point coverage at infinity, script-level hashes for each raw program | group command exact; per-script hashes missing from selected public packet |
| `CW-RATIONAL-QUARTIC` | `S3-QUARTIC` | Program 2 frontier theorem; only types `(3,(1,2))` and `(2,(2,2))` after preclassification | no selected Lane 4 command or file hash exposed | source reports exact terminal calculations | entire frontier preclassification and proof/code attachment | missing public attachment; tree remains conditional |
| `CW-QUAD-SOURCE` | `S3-CONIC-PRIMITIVE`, `S2-QUAD-SOURCE` | nine quadratic-source charts with exact selected minors and overlap ownership | no per-chart filename, hash, command, or output in selected Lane 4 packet | source reports nine exact charts | chart exhaustiveness, zero-minor siblings, independent sample identity | missing public attachment; `AUDIT-QUAD-XW` |
| `CW-PLANE-DEGREE` | `S2-R0`, `S2-R5` | straightened coordinate over `K=k(t)`; plane Keller pair over `\overline K`; one coordinate degree in `{1,...,7,9}` | conventional theorem, no program | Appelgate--Onishi degree criterion; field transfer and descent in `proof-repairs.tex` | upstream coordinate lemma and birational Keller implication | conventional import requiring specialist citation review |
| `CW-FOURTH-POWER` | `S2-FOURTH-POWER` | primitive coprime binary pencil containing a fourth power; aligned and nonaligned/zero-minor children separated | selected packet does not expose a standalone file/hash | source reports exact theorem bundle | normalization and all zero-minor complements | missing public file-level attachment |
| `CW-CENTRALIZER` | `S2-NONBINARY-FIXED` | `proofs/10-structural-repairs-and-z2.tex`; endpoint `(x^4,xR,0)`, `x\nmid R`, `R` not binary after a linear form | conventional proof; no program | kernel of `J_{y,z}(R,-)` on homogeneous polynomials is `k[x,R]`; expanded in `proof-repairs.tex` | common-generator theorem over `k(x)` must be accepted | candidate conventional repair |
| `CW-BINARY-FIXED` | `S2-BINARY-FIXED-G123` | binary fixed factors `g=1,2,3`; exact bundle chart hypotheses | source reports 38 groups and an internal manifest, but selected packet has no per-group command/hash list | reported fresh replay of all groups | theorem-to-group attachment, exact outputs, and independent lineage | missing public attachment; `AUDIT-BINARY-FIXED-XW` |
| `CW-ZERO-MINOR` | `S2-ZERO-MINOR` | specified vanishing Hilbert--Burch minor, with alternate pivot/rank children | no selected standalone public command/hash | source reports zero-minor exact bundle | ownership of all pivot-zero intersections | missing public file-level attachment |
| `CW-RLE2` | `S2-RLE2`, `S2-R3-25` | primitive coprime binary pencil; regular/simple/double ramification or earlier `(2,5)` owner | no selected standalone public command/hash | source reports exact continuation bundle | ramification classification and all discriminant complements | missing public file-level attachment |
| `CW-TAU-MINUS-ONE` | `S2-R3-TAUM1` | `proofs/60-tau-minus-one.tex`; `r=3`, type `(3,4)`, `tau=-1`, projective first-normal strata, saturation factors and next-layer amplitudes | `python checks/tau-minus-one/verify_tau_minus_one.py`; SHA-256 `3937d64a233eb6200feec829b774ac80c5714da305394242f47ad2c0f46551eb` | reconstructs `P,Q,R`; resultant factors; projective strata; saturation certificates; two unrestricted next-layer obstructions | upstream chart placement and zero-normal plane reduction | exact public attachment |
| `CW-Q4-F4` | `Q4-F4` | `r=3`, type `(3,4)`, exceptional `F_4`; coefficient field `Q(tau)[d]/(q4)`; unrestricted lower binary `H_3,H_2`; solve `D_6`, then `D_5` | no complete checker attached in public source | only pure/sample obstruction calculations are reported | whether lower binary terms cancel the `D_5` obstruction; exceptional-factor saturations | genuinely open terminal candidate |
| `CW-R4` | `S2-R4` | `proofs/50-high-ramification.tex`, equations `(H.3)`--`(H.24)`; primitive coprime binary pencil; `r=4`; generic, `3+1`, internal `2+2`, endpoint, and second-normal charts | `python checks/high-ramification/verify_r4_high_ramification.py`; SHA-256 `bf490b014a79dfeba1dd26e0fbb195d0adfe53741ad93d63736ee0a395cc8c6d` | reduced quadratic normalization, repeated-root parametrization, kernels and terminal obstructions | upstream Hilbert--Burch placement and plane reduction | exact public attachment |
| `CW-R5` | `S2-R5` | first branch of `proofs/50-high-ramification.tex`; primitive `r=5`; aligned cube/fourth-power identities | supporting identities run through the same high-ramification checker, SHA-256 `bf490b...` | exact aligned-power identities | cubic-coordinate lemma and plane theorem | exact shared attachment, not independent from `CW-R4` |
| `CW-D56-NORMAL-FORM` | `D56-BASEPOINT` | degree five `(g,e)=(1,2)`; `G` linear; `A,B` quadrics regular sequence; common point on `G=0`; ratio nonconstant there | `python contributions/JCG-C-0014/verify_lane4_audit.py` | verifies the restricted binary quadrics `xy,y^2` have one common point, gcd `y`, and nonconstant residual ratio `x/y`; checks `A=xy+z l1`, `B=y^2+z l2` vanish at `[1:0:0]` | Keller determinant equations on this quintic boundary | exact audit sample; mathematical boundary remains open |

## 3. Commands that can be run from the original Lane 4 packet

```bash
python -m pip install -r requirements.txt
python replay_core.py --group structural
python replay_core.py --group conic
python replay_core.py --group rational-cubic
python replay_core.py --group conic --full-conic
python checks/high-ramification/verify_r4_high_ramification.py
python checks/tau-minus-one/verify_tau_minus_one.py
```

The public handoff page embeds selected source text rather than a standalone
checkout of the full packet.  This contribution therefore records those
commands and published hashes but does not claim to have rerun absent files in
its own branch.

## 4. Independent sample identities in this contribution

`verify_lane4_audit.py` supplies checks independent of the omitted archives:

1. the degree set `{1,2,3,4,5,6,7,9}` satisfies the “at most two prime
   factors, counted with multiplicity” condition;
2. every machine-readable normalization/localization row has a named
   complement;
3. every crosswalk ID used by the tree occurs in this document;
4. the pointed degree-five basepoint normal form has the asserted restriction,
   gcd, point, and nonconstant residual ratio;
5. the homogeneous centralizer basis monomials
   `x^(d-3j) R^j` all have degree `d` for the tested range.

These are audit checks, not substitutes for the Program 2 exact systems.
