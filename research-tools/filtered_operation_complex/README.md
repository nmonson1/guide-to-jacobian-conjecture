# Filtered operation complex

**Status:** reusable research diagnostic, not an integrated theorem or a
replacement for any program-specific geometric classification.

This package audits finite-dimensional complexes of the form

\[
\mathfrak g_r^{(i)}
 \xrightarrow{\Theta_r^{(i)}}
E_r
 \xrightarrow{D_r}
W_r,
\]

with several named operation spaces, tangent directions to adjacent
presentations, optional chart-transition maps, and optional higher-order
forcing vectors. Its purpose is to prevent three logically different notions
from being merged:

1. a direction that kills the linearized equations;
2. a direction induced by an admissible fixed-presentation operation;
3. a direction induced by changing to an adjacent presentation.

For a layer with declared true gauge space \(B_r\) and rechart space \(R_r\),
the reported quotient is

\[
T_r^{\mathrm{true}}=\ker D_r/(B_r+R_r).
\]

A nonzero quotient is an **unclassified direction**, not automatically an
obstruction. It can signal a missing operation, a missing adjacent chart, or a
genuine deformation.

## What is checked

For each layer the engine computes, exactly:

- `rank(D_r)`, `dim ker(D_r)`, and `dim coker(D_r)`;
- the source dimension, image rank, and source stabilizer dimension of each
  named operation;
- declared image inclusions such as `filtered <= polynomial <= formal`;
- containment of every operation and rechart image in `ker(D_r)`;
- the rank of the union of all declared true gauge spaces;
- the independent contribution of the rechart spaces;
- a basis of the unexplained quotient;
- left-null obstruction functionals and their pairings with an optional
  forcing vector;
- exact solvability of the affine equation
  \[
  D_rx=-\Phi_r,
  \]
  including a deterministic particular solution and verification against the
  complete left nullspace.

An operation may be supplied either by image generators or by its full action
matrix. In the latter form the package records

\[
\dim\mathfrak g_r,\qquad
\dim\ker\Theta_r,\qquad
\operatorname{rank}\Theta_r.
\]

The generator form is treated as a map from a coordinate source space whose
basis vectors are the listed generators, so dependencies among generators are
also reported as a source stabilizer.

## Explicit operation maps

The preferred full action form is:

```json
{
  "name": "filtered",
  "role": "filtered",
  "parent": "polynomial",
  "source_dimension": 3,
  "source_basis": ["u0", "u1", "u2"],
  "action_matrix": [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0]
  ]
}
```

The action matrix has `deformation_dimension` rows and `source_dimension`
columns. Its columns are the images of the named source-operation basis.

The legacy image-only form remains supported:

```json
{
  "name": "filtered",
  "role": "filtered",
  "generators": [
    {"name": "u0", "vector": [0, 1, 0, 0]},
    {"name": "u1", "vector": [0, 1, 0, 0]}
  ]
}
```

In this example the image rank is one and the source stabilizer dimension is
one.

## Chart and presentation transitions

For a transition \(C\to C'\), the engine checks

\[
D_{C'}T_E=T_WD_C.
\]

It can additionally check:

- transport of operation image spans;
- transport of rechart spans;
- a source-operation map \(T_{\mathfrak g}\) satisfying
  \[
  T_E\Theta_C=\Theta_{C'}T_{\mathfrak g};
  \]
- transport of source stabilizers;
- transport of the full true explained space \(B_C+R_C\);
- the rank of the induced map
  \[
  T_C^{\mathrm{true}}\longrightarrow T_{C'}^{\mathrm{true}};
  \]
- pullback of dual obstruction functionals;
- transport of forcing vectors;
- preservation of obstruction pairings.

A transition packet with an explicit operation map uses:

```json
{
  "operation_map_pairs": [
    {
      "from": "filtered",
      "to": "filtered",
      "source_map": [[1, 0], [0, 1]],
      "require_isomorphism": true
    }
  ],
  "rechart_span_pairs": [
    {"from": "wall-shear", "to": "inverse-wall-shear"}
  ],
  "true_quotient_map": {"require_isomorphism": true}
}
```

The transition matrices are finite-dimensional stand-ins for coefficient,
equation, operation, and residue/adjoint transport maps derived from the
geometry.

## Coefficient fields

The dependency-free core supports `Q` and a simple algebraic number field in a
power basis. A number field is specified by a low-to-high modulus, for example

```json
{"field": {"kind": "number_field", "modulus": [-2, 0, 1], "symbol": "u"}}
```

for `Q[u]/(u^2-2)`. Number-field elements are coefficient vectors.
Program-specific exporters may use a pinned symbolic dependency to derive the
finite contract; the emitted contract is then replayed by the exact core.

## Minimal layer contract

```json
{
  "id": "chart-C:layer-r",
  "deformation_dimension": 4,
  "equation_dimension": 2,
  "operator": [[1, 0, 0, 0], [0, 0, 0, 0]],
  "actions": [
    {
      "name": "formal",
      "role": "formal",
      "generators": [[0, 1, 0, 0], [0, 0, 1, 0]]
    },
    {
      "name": "filtered",
      "role": "filtered",
      "parent": "formal",
      "source_dimension": 2,
      "source_basis": ["g0", "g1"],
      "action_matrix": [
        [0, 0],
        [1, 1],
        [0, 0],
        [0, 0]
      ]
    }
  ],
  "gauge_actions": ["filtered"],
  "recharts": [
    {"name": "adjacent-wall", "generators": [[0, 0, 1, 0]]}
  ],
  "forcing": [0, 1]
}
```

Several action spaces may be listed in `gauge_actions`; their union is the
fixed-presentation gauge space. Recharts are added separately so their rank
contribution remains visible. See `schema-v1.json` and
`examples/two_chart_rational.json` for the full transition and dual-pairing
contract.

## Commands

```bash
PYTHONPATH=research-tools python -m filtered_operation_complex \
  research-tools/filtered_operation_complex/examples/two_chart_rational.json

python -m unittest discover \
  -s research-tools/filtered_operation_complex/tests \
  -p 'test_*.py' -v
```

## Program 6 adapter

`adapters/program6_legacy.py` consumes the existing
`chart_correspondence.py` JSON format. It treats `gauge_vectors` as the
declared filtered fixed-chart space and `rechart_vectors` as adjacent-chart
tangents. It also reproduces the finite support closure under
`Y=Y'-lambda X^(-k)`.

```bash
PYTHONPATH=research-tools python -m \
  filtered_operation_complex.adapters.program6_legacy \
  research-notes/p6-chart-correspondence/synthetic_k4_contract.json
```

The adapter does not discover the approximate-root subgroup or prove the
chart list exhaustive. For the exact degree-21 lower face, the next useful
export is a generic contract containing the exact `D_r` matrices; formal
Laurent, affine-polynomial, and complete-chain-filtered action maps; the
`k=4` tangent; support transition matrices; and residue-adjoint/forcing data.
The first two action levels are computable; the complete-chain subgroup
remains mathematical input.

## Program 5 exact public instantiation

`adapters/program5_compression_export.py` reconstructs the compression systems
from the hash-pinned public `extensions_verifier.py`. It does **not** import or
claim the later 109-direction/75-automorphism packet stated in the Program 5
handoff; that packet is absent from the public supplement inspected here.

The exact exported contract has an ambient operation space of 115
weight-preserving quadratic source fields and two real layers:

1. the affine row-killing system for the `a,d,q,h,k` rows,
   \[
   \operatorname{rank}A=\operatorname{rank}(A\mid b)=95,
   \qquad \dim\ker A=20;
   \]
2. the tangent system to the rank-at-most-six cubic-coordinate locus at
   \(P_0=-d^2\partial_a\),
   \[
   \operatorname{rank}D_{\mathrm{rank}}=93,
   \qquad \dim\ker D_{\mathrm{rank}}=22.
   \]

The published twelve-parameter family is verified as a subspace of both. The
affine forcing equation is solved by the generic engine, and the public
quartic functional is independently reconstructed as

\[
\Lambda_4=1
\]

on the full 20-dimensional affine row-killing slice.

Run:

```bash
PYTHONPATH=research-tools python -m \
  filtered_operation_complex.adapters.program5_compression_export \
  --contract /tmp/program5-compression-contract.json \
  --report /tmp/program5-compression-report.json \
  --summary /tmp/program5-compression-summary.json
```

Generated exact contracts, reports, and provenance are retained under

```text
research-tools/filtered_operation_complex/intake/program5/
```

## Program 5 tangent bridge

`adapters/program5_tangent_bridge.py` compares the two real tangent spaces. It
verifies

\[
K_{\mathrm{row}}\subset K_{\mathrm{rank}},
\qquad
\dim K_{\mathrm{rank}}/K_{\mathrm{row}}=2,
\]

constructs explicit complement vectors \(\eta_0,\eta_1\), and evaluates the
full quadratic expression \(\Lambda_4(O_4(P))\) on

\[
P=P_0+K_{\mathrm{row}}+\mathbf Q\eta_0+\mathbf Q\eta_1.
\]

The result is the exact identity

\[
\boxed{\Lambda_4(O_4(P))=1}
\]

on the entire 22-dimensional affine tangent plane. There are no linear,
quadratic, or mixed parameter terms. Thus the two first-order rank-six
directions omitted by the row-zero normal form cannot cancel the displayed
quartic functional.

This is stronger than the earlier row-zero calculation but remains
restricted: the affine tangent plane is not proved to lie in the nonlinear
rank-at-most-six locus, and the true source/target/stable operation quotient
has not been supplied. See [`PROGRAM5_TANGENT_BRIDGE.md`](PROGRAM5_TANGENT_BRIDGE.md)
for the exact vectors, proof contract, and conclusion boundary.

```bash
PYTHONPATH=research-tools python -m \
  filtered_operation_complex.adapters.program5_tangent_bridge \
  --output /tmp/program5-tangent-bridge.json
```

## Other uses

The same interface can encode Program 2 determinant kernels versus
integrable source shears, Program 3 formal source-flow versus degree-bounded
operations, Program 4 orbit directions versus infinity-wall degeneration
directions, and Program 1 local gauges versus globally nontrivial overlap
classes.

The explicit operation-map square is the linear precursor of a filtered
groupoid or `L_infinity` comparison. The affine-forcing solver is the first
Kuranishi-facing layer, but nonlinear problems still require recursive forcing,
higher brackets, or Maurer--Cartan data.

## Mathematical boundary

The engine verifies a supplied finite linear-algebra contract. It does not
determine the correct admissible group, discover all adjacent charts, prove
support-window completeness, infer global realization, promote an
unexplained tangent to an obstruction, or prove nonlinear orbit saturation.
Those are the program-specific theorems the report is intended to expose
rather than hide.
