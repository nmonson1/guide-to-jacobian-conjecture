# Validation

## 1. Original audit checker

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

## 2. Structural-repair and `F4` contract checker

Command:

```bash
python contributions/JCG-C-0014/verify_structure_repairs.py
```

Pinned output:

```text
lane4 structural repair validation: PASS
leading_image_degree_leaves=(2,1,2);(2,2,0);(3,1,1);(4,1,0)
relative_closure_regression=degree-2 map detected
four_loci_composite_rows=4
coprime_valuation_fourth_power=PASS
fixed_component_nonconstant_ratio=excluded for multiplicities 1,2,3
f4_schema_required_blocks=11
f4_contract_status=awaiting complete exact input instance
```

The second checker verifies finite arithmetic used by the candidate
leading-image/four-loci proofs, confirms that the relative-algebraic-closure
shortcut admits a degree-two regression example, and checks that the `F4`
schema rejects incomplete input instances. It is not a proof of the geometric
lemmas and does not solve `Q4-F4`.

## 3. Python syntax

Command:

```bash
python -m py_compile \
  contributions/JCG-C-0014/verify_lane4_audit.py \
  contributions/JCG-C-0014/verify_structure_repairs.py
```

Result: `PASS`.

## 4. TeX syntax

`proof-repairs.tex` and `structural-repairs.tex` were each included in minimal
`article` wrappers with the required AMS packages; the structural wrapper also
loaded `cleveref`. Both were compiled using

```bash
pdflatex -interaction=nonstopmode -halt-on-error <wrapper>.tex
```

Result: `PASS`.

## 5. JSON syntax and contract boundary

Commands:

```bash
python -m json.tool \
  contributions/JCG-C-0014/f4-contract.schema.json >/dev/null
python contributions/JCG-C-0014/verify_structure_repairs.py
```

Result: `PASS`.

No `Q4-F4` contract instance is included. This is deliberate: the public
source does not expose the complete `q4`, normalized leading forms, lower-layer
coefficient list, gauge ledger, and localization product needed to construct
one without guessing.

## 6. Deliberate omissions

The complete repository generator, strict MkDocs build, and Program 2 packet
replays were not run in the connector-only environment used to publish these
changes. The selected public handoff does not contain the omitted raw
calculation archives.

No success is claimed for:

- the full repository build;
- absent Program 2 replays;
- specialist verification of the new conventional proofs;
- a complete `Q4-F4` `D6`/`D5` elimination.
