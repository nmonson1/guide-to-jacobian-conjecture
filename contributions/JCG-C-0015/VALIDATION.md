# Validation record for JCG-C-0015

## Required commands

Run from the repository root:

```bash
python -m py_compile \
  contributions/JCG-C-0015/independent_raw_support_replay.py \
  contributions/JCG-C-0015/verify_lane8_submission.py \
  contributions/JCG-C-0015/lane8_replay/*.py \
  contributions/JCG-C-0015/fixtures/quintic_field_fast.py

python contributions/JCG-C-0015/verify_lane8_submission.py
```

To retain the compact replay output rather than using a temporary directory:

```bash
python contributions/JCG-C-0015/verify_lane8_submission.py \
  --replay-output build/JCG-C-0015-replay
```

The output directory must not already exist. The verifier performs the complete
exact reconstruction but asks the replay to write only `summary.json`; this
avoids materializing roughly 25 MB of expanded equation JSON during routine
CI.

## Expected verifier output

```text
lane8 submission validation: PASS
nodes=9
edges=7 covering=6 noncovering=1
truncated_rank=14
truncated_minor_sha256=8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059
full_equations=15
full_equation_sha256=d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883
terminal_projection_sha256=e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a
full_closure_paths=2
adjacent_terminal=empty_but_unattached
below_125=relative_to_imported_GGHV_and_toric_theorems
```

A fresh local replay on Python 3.13 used approximately 21 seconds of wall time
and 176 MB maximum resident memory. The algorithm is exact and deterministic;
the timing is not a validation criterion.

## What the verifier checks

The checker fails unless all of the following hold:

1. the active Lane 8 reconstruction packet and source packet match their
   pinned SHA-256 values;
2. the Program 6 theorem source matches its pinned Git blob and contains all
   four imported labels;
3. the local face fixture is exactly the `minimal_polynomial` and `relations`
   projection of the public reconstruction JSON;
4. the quintic passes the recorded mod-67 Rabin irreducibility witness;
5. both support polygons and every layer are rebuilt without archived matrices
   or archived equations;
6. every basis, matrix, pivot column, and pivot-unit digest matches the indexed
   stage manifest and its committed fragments;
7. no layer inversion contains a deformation-parameter polynomial;
8. the truncated rank, minor digest, layer-four square, endpoint powers,
   fifteen equation hashes, and six-equation projection agree with the
   manifest and public expected digests;
9. the queue has unique identifiers, is acyclic, and every recorded closure
   path uses only covering edges;
10. the `t1_1=0` and `t1_1!=0` children form the displayed exhaustive split;
11. the adjacent-chart edge remains noncovering and is absent from both full
   closure paths;
12. the below-125 conclusion remains explicitly relative to imported theorems.

The existing technical-materials manifest pins the Program 6 computational
supplement at SHA-256

```text
4238149caa6e8a73723368e997b8c714a99258600268f14a008c5e514ecea585
```

This contribution does not download or expand that archive during its own
validator; the compact toric theorem remains an explicit imported interface.

## Full-output replay

For a coefficient-level review, omit `--summary-only` and run the entrypoint
directly:

```bash
python contributions/JCG-C-0015/independent_raw_support_replay.py \
  --output build/JCG-C-0015-full-replay
```

This writes:

- `summary.json`;
- `full_equations.json`;
- `full_exact_fivevar_w8.json` in the legacy archive-compatible format;
- `full_terminal_projection.json` for indices `4,6,8,9,10,11`.

The large JSON files are intentionally generated rather than committed.

## Explicit omissions and theorem interfaces

- The contribution reconstructs and attaches the six selected equations, but
  it imports the existing compact toric emptiness theorem rather than
  independently rebuilding its 296-point toric special fibre from first
  principles.
- It imports Theorem 2.1, Proposition 4.3, and Corollary 5.7 of
  Guccione--Guccione--Horruitiner--Valqui rather than reproving the complete
  below-125 Newton-polygon reduction.
- It does not attach the stored adjacent-chart terminal. The exact order-seven
  calculation disproves the proposed bare-`k=4` layer-four bridge.
- It does not reconstruct coefficients of deficiency greater than eight. They
  are never divided by; every full-support solution merely projects to the
  empty layer-through-eight necessary-condition scheme.
- It retains the layer-four square as a nonreduced scheme equation. The linear
  factor is used only for reduced geometric routing.
- It does not update generated theorem or claim metadata automatically.
