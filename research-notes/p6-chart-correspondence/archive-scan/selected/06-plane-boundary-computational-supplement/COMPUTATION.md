# Computation index

The supplement distinguishes exact theorems about displayed finite systems
from the upstream claim that those systems exhaust every candidate below the
degree bound.

| Mathematical role | Directory | Main checks |
| --- | --- | --- |
| Exact normal linearization | `code/verify_exact_normal_form.py` | logarithmic wedge coefficient, determinant-one jet block, \((8,28)\) boundary-volume identity, and full-support window dimensions |
| Terminal boundary program | `computational-supplement/terminal-boundary/` | layer operator, final-face rigidity, dessin counts, and explicit terminal examples |
| Degree-\(21\) quotient faces | `computational-supplement/degree-twenty-one/` | character count, five dessins, exact Belyi reconstruction, passports, and lower-face substitutions |
| Terminal unit ideals | `computational-supplement/terminal-unit-ideal/` | exact GMP and Python replay programs for the two stored exceptional branch ideals; the large archive supplies the matrices and cofactors |
| Residue provenance of the fifteen equations | `computational-supplement/degree-296-compact/scripts/export_residue_audit.py` | reconstructs every layer matrix through order \(8\), verifies every filtered adjoint, recovers every compatibility pairing as a residue, and matches all fifteen normalized equations |
| Compact \(296\)-point obstruction | `computational-supplement/degree-296-compact/` | mixed volume, all \(344\) toric faces, reduced \(296\)-point modular algebra, invertibility of the sixth obstruction, and characteristic-zero lifting |

The large-data archive adds the selected Macaulay matrices, exact
Nullstellensatz cofactors, complete residue tables, and other generated
inputs. The two strongest finite statements are unconditional for the
systems as displayed:

- each stored terminal ideal contains \(1\);
- every one of the fifteen stored terminal equations has the asserted exact
  filtered-residue provenance; and
- the six-polynomial toric system has no characteristic-zero solution.

The exact normal-linearization theorem and terminal-layer injectivity theorem
have conventional proofs in the manuscript. The compact SymPy program is a
regression check for their algebraic identities and window arithmetic; it is
not the logical source of the degree argument.

Their global below-\(125\) interpretation depends on the prior
Newton-polygon reduction. One upstream utility,
`lower_face_layers.py`, was not recovered, so the present archive does not
claim a clean regeneration of that whole reduction from raw supports.

The legacy `verify_quintic_field.py` utility now takes its input directory
explicitly, but the thirteen intermediate `F*_r4.txt` files it expects were
not present in the recovered attachments. It is retained for provenance and
is not part of the proof path above; the exact Belyi reconstruction and
terminal certificates use the self-contained files listed in the table.

Minimal replay commands are documented in
`computational-supplement/terminal-unit-ideal/EXACT_CERTIFICATE_REPORT.md`
and `computational-supplement/degree-296-compact/README.md`.
