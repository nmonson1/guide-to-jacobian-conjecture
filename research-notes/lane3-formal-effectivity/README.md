# Lane 3 formal effectivity package

This package records a continuation of Lane 3.  It connects the bounded
coefficient germ to the stable quadratic cubic-frame modulus without
identifying those quotient problems.

## Main theorem

For

\[
A_\alpha(c)=c(1+\alpha c),\qquad
B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\]

write \(F_{\alpha,q}=G_{A_\alpha,B_{\alpha,q}}\) and
\(\delta=q'-q\).  A framed root translation of \(c\)-degree at most \(D\)
from \(F_{\alpha,q}\) to \(F_{\alpha,q'}\) exists exactly when

\[
\delta\alpha^{D+2}=0.
\]

For the pointed arc \(\alpha=s\) modulo \(s^M\), the optimal framed degree is
\(M-2\).  The compatible limit is coefficientwise formal but has unbounded
spatial degree.

All Artin truncations of two distinct \(q\)-arcs are ordinarily polynomially
left--right equivalent, compatibly in the truncation order.  The complete
families over \(\mathbf C[[s]]\) are not stably polynomially left--right
equivalent.  For arbitrary unframed equivalences, including arbitrary
stabilization, the package proves

\[
\liminf_{M\to\infty}
\frac{\kappa_M(q,q')}{\log\log M}\ge \frac1{\log4}.
\]

The sharp linear lower bound for arbitrary unframed equivalences remains
open.

## Package map

| File | Role |
| --- | --- |
| `formal_effectivity_theorem.md` | Complete statement, proofs, dependencies, and limitations. |
| `formal_effectivity_insertion.tex` | Manuscript-ready proposed insertion; it is not wired into the pinned manuscript release. |
| `bibliography-additions.bib` | Citation for the parametric effective Nullstellensatz used in the quantitative proof. |
| `lane3-handoff-replacement.md` | Proposed future Lane 3 handoff source; the active immutable v16 release is not modified. |
| `AUDIT.md` | Scope audit, corrected conclusions, and superseded routes. |
| `verify_formal_effectivity.py` | Exact SymPy verification of the root-translation identities, degree staircase, affine-frame equations, and finite Artin samples. |
| `verify_formal_effectivity_independent.py` | Independent sparse-polynomial verification using only the Python standard library. |
| `verify_effective_unframed_bound.py` | Combinatorial verification of coefficient counts, degree bounds, finite inequalities, and asymptotic constants. |
| `manifest.json` / `check_manifest.py` | SHA-256 source inventory and checker. |

The verification programs generate three `*_report.json` files.  They are
not stored in the source package; the dedicated GitHub Actions workflow
uploads them as a run artifact after every successful replay.

## Replay

From the repository root:

```bash
python research-notes/lane3-formal-effectivity/check_manifest.py
python -m pip install "sympy==1.14.0"
python research-notes/lane3-formal-effectivity/verify_formal_effectivity.py
python research-notes/lane3-formal-effectivity/verify_formal_effectivity_independent.py
python research-notes/lane3-formal-effectivity/verify_effective_unframed_bound.py
```

Expected terminal statuses are:

```text
LANE 3 MANIFEST OK: 10 files
ALL FORMAL-EFFECTIVITY CHECKS PASSED
INDEPENDENT EFFECTIVITY STAIRCASE CHECKS PASSED
ALL EFFECTIVE UNFRAMED BOUND CHECKS PASSED
```

The first verifier uses exact SymPy arithmetic.  The independent staircase
checker and the quantitative-bound checker use only the standard library.

## Dependencies and evidence boundary

The unframed nonexistence statements use the Program 4 complete stable
classification of the quadratic family by \(q\).  The effective lower bound
also uses D'Andrea--Krick--Sombra, Theorem 0.5 in *Heights of varieties in
multiprojective spaces and arithmetic Nullstellensätze*.

The programs verify the displayed finite identities and bookkeeping.  They do
not re-prove the stable \(q\)-classification, the generic-combination lemma,
or the external parametric Nullstellensatz.  This package does not prove
characteristic-zero degree-eight orbit saturation and does not identify the
stable modulus with a finite Kuranishi tangent character.

## Provenance

GPT-5.6 Pro performed the source audit, theorem development, proof drafting,
exact implementation, independent finite-support replication, and package
preparation.  Nathaniel Monson remains responsible for accepting, revising,
or rejecting every mathematical assertion.
