# Lane 4 quartic endgame repair and reproduction packet

**Version:** 2026-08-02-v1  
**Status:** unrefereed research packet; exact calculations use one SymPy lineage  
**Scope:** ordinary-degree-four Keller maps in three variables over an algebraically closed characteristic-zero field

This packet consolidates the proof repairs, candidate theorem statements,
case-tree audit, exact symbolic programs, and fresh replay outputs developed
in the Lane 4 audit.  It is additive: it does not replace the generated claim
graph or silently revise the public working manuscripts.

The unconditional public conclusion remains

```text
4 <= D_min <= 7.
```

Nothing in this packet should be cited as an unconditional proof of
`D_min >= 5` before the remaining proof-to-code attachment and specialist
review gates are closed.

## Contents and mathematical status

| Item | Deliverable | Status in this packet |
| --- | --- | --- |
| Leading-image factorization | replacement proof using the normalization of the actual image curve | candidate reader-level repair |
| Four-locus reduction | exhaustive composite/primitive valuation proof with explicit overlap convention | candidate reader-level repair |
| `R=0` branch | quadratic-coordinate and plane-reduction argument | candidate reader-level repair; retains the Program 2 plane-theorem dependency |
| Nonbinary fixed components | homogeneous cubic Hamiltonian-centralizer lemma | candidate reader-level repair |
| Conic orbit `G=z^2` | exact coefficient proof and standalone checker | freshly replayed |
| Conic orbits `G=x^2,xy` | complete stabilizer-chart proofs and exact branch programs | freshly replayed |
| Proper rational cubic | cuspidal/nodal, transverse/marked, and full nodal marked-family proof | exact supporting programs freshly replayed |
| Span-three synthesis | candidate corollary routing every nonautomorphic quartic map to leading target span two | depends on the stated curve exclusions and their upstream classification |
| Primitive binary ramification `r=4,5` | projective repeated-root proof replacing the imported specialization step | exact supporting checker freshly replayed |
| Primitive `r=3`, `tau=-1` | independent exceptional-divisor exclusion | exact supporting checker freshly replayed |
| Global quartic tree | ownership-based case tree and machine-readable CSV | structural audit draft; terminal proof-code attachment remains incomplete |

The words **candidate**, **draft**, and **unrefereed** are substantive.  The
new proofs have not received independent specialist review, and the programs
are not a second-computer-algebra-system reproduction.

## Important provenance boundary

Earlier exploratory conversation notes also described independent work on a
generic `F_4` family and the `tau=0` divisor.  Their complete source programs
were not available when this packet was assembled, so those calculations are
**not** promoted or represented here as archived source-backed results.  The
public v5 package remains the evidence for those named charts.

## Principal files

- `lane4-quartic-endgame-repairs.tex` — standalone compilable manuscript that
  inputs all six proof fragments.
- `proofs/` — insertion-ready TeX fragments.
- `case-tree/global-case-tree-draft.md` — global routing and status audit.
- `case-tree/global-case-tree.csv` — machine-readable leaf table.
- `checks/` — exact scripts, raw branch calculations, and stored outputs.
- `outputs/` — fresh outputs captured during assembly.
- `replay_packet.py` — scoped replay driver.
- `MANIFEST.json` and `SHA256SUMS` — environment, scope, and file hashes.

## Reproduction

The recorded environment was Python 3.13.5 with SymPy 1.14.0.

```bash
python -m pip install -r requirements.txt
python replay_packet.py
```

The default replay runs the compact structural checkers and representative
rational-cubic calculations.  The broader branch suite is available as

```bash
python replay_packet.py --full
```

The full mode replays every named `x^2` and `xy` conic branch and the broader
rational-cubic suite.  The expensive nodal full-matrix computation is omitted
from the automatic full mode because the constant-minor checker proves the
same rank statement much more quickly; its script and captured output remain
included.

To verify the packet hashes after extraction:

```bash
sha256sum -c SHA256SUMS
```

## Exact boundaries

The symbolic scripts verify displayed determinant identities, finite
projective charts, rank statements, saturation certificates, and terminal
coefficients.  They do not independently prove:

1. the complete leading-curve classification used before the span-three
   leaves;
2. every upstream Hilbert--Burch chart-placement assertion in the public v5
   degree-three family;
3. the proof-to-code correspondence for every quadratic-source and
   fixed-factor leaf;
4. the exact cited formulation of the low-degree plane automorphism theorem;
5. independent reproduction in another CAS; or
6. specialist review of the new conventional arguments.

See `case-tree/global-case-tree-draft.md` for the current ownership tree and
remaining gates.

## AI assistance and responsibility

GPT-5.6 Pro assisted with the audit, mathematical exploration, proof drafting,
exact-program construction, replay, and packet assembly.  Every mathematical
claim requires review by the repository owner and appropriate specialists
before promotion into the authoritative claim graph or a refereed manuscript.
