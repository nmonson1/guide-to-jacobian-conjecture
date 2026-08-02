# Lane 4 global audit and surviving quartic candidate

This contribution is an additive, unrefereed audit of the Lane 4 quartic
endgame.  It was prepared against repository `main` commit
`7c51062f0879fbd12cbb1e2bb03b25918e4e8c07` on 2 August 2026.

It does **not** prove that every quartic Keller map is invertible, does not
change the public bound

\[
4\le D_{\min}\le 7,
\]

and does not promote any candidate proof or exact replay into the generated
claim graph.  Its purpose is narrower: make the global ownership problem
explicit enough that a reader can see which parts are theorem imports, which
parts are finite calculations, which complements are routed, and which
interfaces are still missing.

## Deliverables

| Obligation | Disposition in this contribution |
| --- | --- |
| Rooted case tree | `lane4-global-case-tree.md` and `lane4-case-tree.csv` begin with an arbitrary normalized quartic Keller map. |
| Vanishing complements | Every row that uses a normalization or localization names the zero/complementary child.  A validator rejects an unnamed complement. |
| Imported theorem hypotheses | The theorem-interface ledger records the exact field, degree, curve, orbit, basepoint, and chart hypotheses used by each imported result. |
| Proof/code crosswalk | `PROOF_CODE_CROSSWALK.md` gives a row for every computational family used by the tree.  Missing public file hashes or commands are recorded as blockers rather than reconstructed from prose. |
| Appelgate--Onishi / Nowicki--Nakai | `proof-repairs.tex` gives journal locators, the characteristic-zero transfer, and the descent from `\overline{k(t)}` to `k(t)`. |
| Fixed-factor basepoints | The degree-five/six boundary is separated from the quartic tree.  The surviving quintic `(g,e)=(1,2)` locus is reduced to a pointed normal form; it is not falsely declared impossible. |
| Cubic centralizer exposition | `proof-repairs.tex` expands the common-generator, homogeneity, Gauss-intersection, and descent steps. |
| Final quartic conclusion | No quartic theorem follows.  Conditional on all upstream routing imports, the surviving terminal candidate is the exceptional triple-ramification `Q4-F4` compatibility system. |

## Principal conclusion

There are two logically different kinds of unresolved object.

1. **Routing/evidence gaps.**  The public sources do not yet provide a
   line-by-line proof that every normalized quartic reaches the imported
   leading-curve, four-loci, quadratic-source, fixed-factor, and orbit charts.
   These are labeled `AUDIT-*` in the tree.  They are obligations, not asserted
   families of Keller maps.
2. **A terminal algebraic survivor.**  After accepting all recorded routing
   inputs, the primitive coprime binary-pencil branch with ramification
   `r=3`, Hilbert--Burch type `(3,4)`, and the exceptional weighted-inflection
   family `F_4` still requires the unrestricted degree-five compatibility
   calculation.  This is labeled `Q4-F4`.

Thus the contribution satisfies the requested final alternative by exhibiting
an exact surviving *candidate system*, not an explicit noninvertible quartic
map.  A solution of the system would still have to be checked against every
upstream hypothesis before it could yield a map.

## Files

- `lane4-global-case-tree.md` — mathematical tree, theorem interfaces, and
  ownership discussion.
- `lane4-case-tree.csv` — machine-readable edge ledger.
- `PROOF_CODE_CROSSWALK.md` — exact public evidence map and missing-artifact
  report.
- `proof-repairs.tex` — Appelgate--Onishi transfer, cubic-centralizer descent,
  and fixed-factor basepoint normal form.
- `verify_lane4_audit.py` — structural validation of the CSV, crosswalk IDs,
  degree criterion, and normal-form sample identities.
- `VALIDATION.md` — validation command and pinned output.

## Validation

From the repository root, run

```bash
python contributions/JCG-C-0014/verify_lane4_audit.py
```

The checker is deliberately modest.  It validates the audit artifact; it does
not replay the omitted Program 2 calculation archives and does not certify a
Keller-map nonexistence theorem.

## Provenance and review boundary

GPT-5.6 Thinking assisted with source comparison, mathematical auditing,
proof drafting, and the validator.  The repository owner remains responsible
for accepting, revising, or rejecting every assertion.  Specialist review is
required before any part is incorporated into a theorem-bearing manuscript or
claim graph.
