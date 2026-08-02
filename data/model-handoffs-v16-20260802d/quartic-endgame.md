# Lane 4: The quartic endgame

## Research objective

Finish the ordinary-degree-four case in three variables by proving that one
global case tree reaches only established theorem leaves and exact terminal
certificates.  If it does not, isolate the uncovered normal form.

The unconditional public conclusion remains

```text
4 <= D_min <= 7.
```

Do not state `D_min>=5` before the routing theorem is complete.

## Reusable mathematics

The current manuscript and register contain exact leaves for:

- leading target span and leading-image reductions;
- nondegenerate conics, rational cubics, and the surviving rational-quartic
  frontier under their recorded hypotheses;
- binary-pencil ramification degrees `0` through `5`, including zero-minor
  boundaries;
- fourth-power, quadratic-source, fixed-line, fixed-conic, fixed-cubic, and
  `R=0` branches;
- high-ramification and dependent-syzygy charts; and
- the encoded exceptional `F_3/F_4` terminal queue.

Representative retained units include [`RMU-B7B975F2`](../working-mathematics/units/RMU-B7B975F2.md), [`RMU-C41D9892`](../working-mathematics/units/RMU-C41D9892.md),
[`RMU-99553B20`](../working-mathematics/units/RMU-99553B20.md), [`RMU-CC15C520`](../working-mathematics/units/RMU-CC15C520.md), [`RMU-D6A4C9D6`](../working-mathematics/units/RMU-D6A4C9D6.md), [`RMU-0616D9BC`](../working-mathematics/units/RMU-0616D9BC.md), and
[`RMU-2920F7C8`](../working-mathematics/units/RMU-2920F7C8.md).  The exact checkers replay their displayed finite systems;
the Program 2 audit notes record the hypotheses and proof-code boundaries.

The high-ramification archive has ten standalone checkers and 38 manifest
groups with successful fresh replays.  The degree-five/six fixed-factor
theorem requires the actual hypothesis

```text
V_P2(G,A,B)=empty.
```

The invariant-degree lemma has weaker hypotheses; the basepoint boundary is
open.

The July 30 quartic terminal packet closes its encoded local charts, including
the corrected exceptional and dependent-syzygy systems.  Several helper
scripts were reconstructed rather than recovered from an original archive;
their exact output is useful but their provenance must remain visible.

## What is not known

No current artifact is a single proof that every quartic Keller map reaches
one of these leaves.  The complete-specialization input, some proof-code
mapping, and a few later curve-orbit reductions still require explicit audit.
Terminal exactness does not imply branch exhaustiveness.

New conversation calculations toward degree five and six are not evidence for
the quartic theorem.  Sandbox-only `F_3/F_4`, binary-cubic quintic, or sextic
resonance calculations are research leads until their exact artifacts and
hypotheses are recovered.

## Exact live problem

Construct one theorem-level case-tree table.  Each edge must record:

1. its exact hypotheses;
2. every saturation, normalization, and specialization;
3. the statement that justifies the edge;
4. the proof body or checker closing the leaf; and
5. the boundary that remains if the edge is conditional.


## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks

### P2-L4A — Global leaf accounting

Actor: `online_model`. Status: ready.

Write the complete case tree without filling a gap by analogy.

### P2-L4B — Proof-code crosswalk

Actor: `local_symbolic`. Status: blocked on P2-L4A.

Map every terminal leaf to exact inputs, commands, outputs, and a short
independent identity or certificate sample.

### P2-L4C — Uncovered branch resolution

Actor: `online_model`. Status: blocked on P2-L4A.

If the tree exposes a leaf, state its normal form and attack that branch.  If
no leaf remains, write the conventional global proof with the computation
interface separated.

## Do not do

- Do not infer `D_min>=5` from a collection of terminal charts.
- Do not specialize a generic rational formula through a vanishing
  denominator instead of opening a new chart.
- Do not use the degree-five/six theorem without basepoint freeness.
- Do not treat a second wrapper around the same formulas as an independent
  derivation.

The retained-unit and proof-source pages linked above are the public mathematical record for this lane.
