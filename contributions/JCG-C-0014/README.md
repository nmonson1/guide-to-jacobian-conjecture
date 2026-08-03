# Lane 4 global audit, structural repairs, and surviving quartic candidate

This contribution is an additive, unrefereed audit of the Lane 4 quartic
endgame. It was initially prepared against repository `main` commit
`7c51062f0879fbd12cbb1e2bb03b25918e4e8c07` on 2 August 2026 and has since
been extended by comparing the later sanitized Program 2 sources.

It does **not** prove that every quartic Keller map is invertible, does not
change the public bound

\[
4\le D_{\min}\le 7,
\]

and does not promote any candidate proof or exact replay into the generated
claim graph.

## Deliverables

| Obligation | Disposition in this contribution |
| --- | --- |
| Rooted case tree | `lane4-global-case-tree.md` and `lane4-case-tree.csv` begin with an arbitrary normalized quartic Keller map. |
| Vanishing complements | Every recorded normalization or localization names its zero/complementary child; `verify_lane4_audit.py` rejects an unnamed complement. |
| Leading-image factorization | `structural-repairs.tex` replaces the relative-algebraic-closure shortcut by a direct normalization proof and records the line/rank complements. |
| Four-loci routing | `structural-repairs.tex` proves the weighted-field reduction and the binary, quadratic-source, fourth-power, and fixed-component cover, retaining the sign distinction between coprime and fixed-factor valuations. |
| Imported theorem hypotheses | The theorem-interface ledger records the field, degree, curve, orbit, basepoint, and chart hypotheses used by each imported result. |
| Proof/code crosswalk | `PROOF_CODE_CROSSWALK.md` gives a row for every computational family used by the tree and records absent public files as blockers. |
| Plane dependency documentation | `proof-repairs.tex` gives the Appelgate--Onishi and Nowicki--Nakai locators, characteristic-zero transfer, and descent from `\overline{k(t)}` to `k(t)`. |
| Cubic centralizer exposition | `proof-repairs.tex` separates common generation over `k(x)`, homogeneity, Gauss intersection, and polynomial descent. |
| Fixed-factor basepoints | The degree-five/six boundary is separated from the quartic tree; the surviving quintic `(g,e)=(1,2)` locus is normalized but not excluded. |
| `Q4-F4` progress | `F4_INPUT_CONTRACT.md` and `f4-contract.schema.json` specify the exact data and certificate standard required before the open extension-field calculation can be run honestly. |
| Final quartic conclusion | No unconditional quartic theorem follows. The terminal `Q4-F4` system and the remaining orbit/frontier and evidence interfaces still have to be closed. |

## New structural finding

The current manuscript proof of leading-image factorization passes through the
relative algebraic closure of the image field and then treats the resulting
map `P^1 -> C` as birational. Relative algebraic closure alone does not imply
that conclusion: the map

\[
[x:y:z]\longmapsto[x^2:y^2:0]
\]

already gives a degree-two parametrization after adjoining `x/y`. The
replacement proof chooses the normalization of `C` first, composes its
rational inverse with the leading map, and only then selects the coprime
source pencil `[A:B]`. This gives

\[
H_4=G\,h(A,B),\qquad \deg G+\deg(h)\deg(A)=4
\]

without the shortcut.

The four-loci proof is also written out rather than summarized. In the
coprime composition-primitive case it uses nonnegative valuation coefficients
summing to three and obtains a fourth-power fiber. In the fixed-factor case it
does **not** impose nonnegativity: a nonconstant pencil ratio on a component
of multiplicity `mu <= 3` would give `4 nu(R)=3 mu`, which is impossible, so
the component lies on a special fiber.

These are candidate conventional proofs. The audit nodes remain review gates
until the arguments are independently checked and integrated with the exact
hypotheses of the surrounding manuscript.

## The `Q4-F4` boundary

The sanitized sources identify the surviving branch as primitive coprime
binary ramification `r=3`, Hilbert--Burch type `(3,4)`, on an exceptional
weighted-inflection family over

\[
\mathbf Q(\tau)[d]/(q_4(d,\tau)).
\]

They do not expose a complete reconstructible package containing the explicit
`q4`, normalized `P,Q,R`, all unrestricted lower coefficients, all gauge
actions, and the full open-factor product. Therefore this contribution does
not fabricate a symbolic checker from prose.

The contract requires the missing data and prescribes the next calculation:

1. solve the full `D6` system as a module, recording Fitting/rank-drop loci;
2. test the `D5` obstruction in the cokernel of **all** remaining cancellation
   variables;
3. produce an exact saturation or Nullstellensatz certificate over
   characteristic zero;
4. recompute every exceptional factor from its own chart.

A non-unit saturated ideal would instead produce a concrete surviving
candidate component to be tested against the remaining determinant layers.

## Files

- `lane4-global-case-tree.md` — mathematical tree and theorem interfaces.
- `lane4-case-tree.csv` — machine-readable edge ledger.
- `PROOF_CODE_CROSSWALK.md` — public evidence map and missing-artifact report.
- `proof-repairs.tex` — plane transfer, cubic centralizer, and quintic
  basepoint normalization.
- `structural-repairs.tex` — direct leading-image and four-loci candidate
  proofs.
- `F4_INPUT_CONTRACT.md` — closed-world algebraic specification and
  elimination protocol for `Q4-F4`.
- `f4-contract.schema.json` — fail-closed schema for a complete `F4` input
  instance.
- `verify_lane4_audit.py` — validates the case-tree artifact.
- `verify_structure_repairs.py` — checks the finite degree/valuation skeleton,
  the relative-closure regression, and the `F4` contract shape.
- `VALIDATION.md` — commands, outputs, and explicit omissions.

## Validation

From the repository root, run

```bash
python contributions/JCG-C-0014/verify_lane4_audit.py
python contributions/JCG-C-0014/verify_structure_repairs.py
python -m py_compile \
  contributions/JCG-C-0014/verify_lane4_audit.py \
  contributions/JCG-C-0014/verify_structure_repairs.py
```

The checkers validate the audit and finite arithmetic used by the candidate
structural proofs. They do not replay the omitted Program 2 archives, prove
the geometric inputs automatically, or solve `Q4-F4`.

## Provenance and review boundary

GPT-5.6 Pro assisted with source comparison, mathematical auditing, proof
drafting, and validation. The repository owner remains responsible for
accepting, revising, or rejecting every assertion. Specialist review is
required before incorporation into a theorem-bearing manuscript or claim
graph.
