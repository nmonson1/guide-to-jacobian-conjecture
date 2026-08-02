# Validation

## Audit checker

Command:

```bash
python contributions/JCG-C-0014/verify_lane4_audit.py
```

Pinned output:

```text
lane4 audit validation: PASS
rows=34
named_open_interfaces_or_candidates=7
crosswalk_ids_used=15
plane_degree_set=1,2,3,4,5,6,7,9
surviving_quartic_candidate=Q4-F4
degree_five_boundary=D56-BASEPOINT (not a quartic child)
```

## Python syntax

Command:

```bash
python -m py_compile contributions/JCG-C-0014/verify_lane4_audit.py
```

Result: `PASS`.

## TeX syntax

`proof-repairs.tex` was included in a minimal `article` wrapper with
`amsmath,amsthm` and compiled using

```bash
pdflatex -interaction=nonstopmode -halt-on-error lane4-proof-wrapper.tex
```

Result: `PASS`.

## Deliberate omissions

The complete repository generator, strict MkDocs build, and Program 2 packet
replays were not run in this environment because the work was performed
through the GitHub connector rather than a full repository checkout.  The
selected public handoff does not contain the omitted raw calculation archives.
No success is claimed for those unavailable checks.
