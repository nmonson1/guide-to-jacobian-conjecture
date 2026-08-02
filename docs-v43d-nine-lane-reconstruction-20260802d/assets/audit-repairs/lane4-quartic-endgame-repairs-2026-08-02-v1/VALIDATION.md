# Validation record

## Environment

- Date: 2 August 2026
- Python: 3.13.5
- SymPy: 1.14.0
- TeX engine: pdfTeX 1.40.26

## Source checks

- Every Python source in the packet compiled with `python -m py_compile`.
- The case-tree CSV parsed successfully and contains 15 owned leaves.
- Text sources were scanned for private filesystem paths, sandbox links,
  private conversation URLs, and internal locator strings; no matches were
  found.

## Exact replay

The compact driver completed six checks:

```text
PASS: 6 exact Lane 4 checks completed in 31.16s
```

The broad driver completed forty checks:

```text
PASS: 40 exact Lane 4 checks completed in 234.82s
elapsed=3:55.37 maxrss=228896KB
```

The broad run includes every named `x^2` and `xy` conic branch, the exact
`z^2` checker, the high-ramification and `tau=-1` checkers, all listed
cuspidal and nodal rational-cubic systems, and the constant nodal maximal
minor. The approximately two-minute nodal full-matrix program is stored with
its captured output but is not duplicated in the automatic broad run; the
constant-minor program checks the same rank conclusion.

## TeX validation

`lane4-quartic-endgame-repairs.tex` compiled twice with `pdflatex
-interaction=nonstopmode -halt-on-error` to a 19-page PDF. The second pass had
no undefined references, overfull boxes, or TeX errors. A rendered contact
sheet of all nineteen pages was visually inspected; no clipping or malformed
page was observed. The generated PDF and auxiliary files are not included in
the source packet.

## Interpretation

A passing replay verifies the encoded identities and finite charts only. It
does not change the unrefereed status of the proof drafts, prove every
upstream chart-placement statement, provide a second-CAS lineage, or justify
an unconditional claim that `D_min >= 5`.
