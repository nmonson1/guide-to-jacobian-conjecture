# Lane 8 direct terminal closure for the two normalized `(8,28)` supports

This contribution gives a proof-carrying audit of the two normalized Newton
supports used by Lane 8. It independently reconstructs the degree-21 lower
face and every deficiency layer needed for the truncated and full roots. The
truncated root is replayed and marked closed. The full root is closed by a
direct consequence edge from its fifteen normalized obstruction equations to
the existing compact six-polynomial toric terminal system.

The adjacent-chart layer-five-through-seven terminal system is also audited.
Its stored emptiness theorem is exact, but the proposed bare `k=4` wall shear
starts at normal order seven, not four, so it does not supply the missing
covering edge. That terminal is therefore **not used**. Lane 8 does not need it:
the direct toric route already closes the full root.

The work is AI-assisted, unrefereed, and additive. It does not silently modify
the generated claim graph or theorem spine.

## Main result

Let

\[
K_0=\mathbf Q[u]/(u^5-u^4+3u^3+3u^2+26).
\]

For each of the five conjugate degree-21 lower faces, the following two
necessary-condition systems are empty over an algebraic closure of `K0`:

1. the vertex-saturated truncated `(8,28)` root;
2. the deficiency-through-eight projection of the full `(8,28)` root.

Consequently neither normalized support can occur for a characteristic-zero
plane Keller counterexample. Combining this with the imported reduction of
Guccione--Guccione--Horruitiner--Valqui, specifically Theorem 2.1,
Proposition 4.3, and Corollary 5.7 of arXiv:2204.14178v1, gives the relative
corollary

\[
\max(\deg P,\deg Q)\ge 125
\]

for every characteristic-zero plane Keller counterexample. This last step is
not an independent reproof of the published Newton-polygon reduction.

## Checklist disposition

| # | Checklist item | Disposition |
|---:|---|---|
| 1 | Mark the truncated `(8,28)` root as closed | Complete: `L8-T-ROOT` is terminal empty. |
| 2 | Independently replay the truncated certificate | Complete: rank `14` and the published minor digest are regenerated from the polygon. |
| 3 | Publish the full-support stage manifest | Complete: every stage records its field, ring, variables, equations, bases, matrices, pivots, denominators, saturations, complements, and output. |
| 4 | Reconstruct full layers `(1)`--`(4)` | Complete, including the exact square `unit*(t2_2-alpha*t1_1^2)^2`. |
| 5 | Reconstruct the fifteen equations | Complete: ordered counts `(1,3,5,6)` and the public canonical digest agree. |
| 6 | Preserve denominator-zero complements | Complete for the raw-support pipeline: all linear pivots are fixed field units; `t1_1=0` is an explicit empty child; `U,D` are exact-support factors; higher-deficiency coefficients are included by relaxation rather than divided away. |
| 7 | Separate reduced routing from scheme structure | Complete: the double hyperplane is retained, while its radical is used only for geometric routing. |
| 8 | Attach the compact toric terminal | Complete: the terminal generators are literally equations `4,6,8,9,10,11` of the replayed list. |
| 9 | Attach the stored adjacent terminal | Attempted but not covering: the bare `k=4` shear begins at order `7`; the stored terminal is recorded but unused. |
| 10 | Close every full-root child | Complete for the direct queue: both members of the exhaustive `t1_1` split reach empty terminal nodes without a noncovering edge. |
| 11 | Deduce the below-`125` exclusion | Complete relative to the named GGHV reduction and current compact toric theorem; neither import is independently reproved here. |

## Exact reconstruction

Put `t=Y` and `z=XY^2`. The lower face is represented by

\[
A_0=z p(z),\qquad B_0=z^2 q(z),
\]

where `deg(p)=7`, `deg(q)=10`, and

\[
pq+2zpq'-3zp'q=1.
\]

The replay starts from the two polygon vertex lists, generates every lattice
point, assigns deficiencies

\[
d_P(i,j)=j-2i+2,\qquad d_Q(i,j)=j-2i+3,
\]

and forms every Jacobian coefficient directly from

\[
[X^iY^j,X^kY^\ell]=(i\ell-jk)X^{i+k-1}Y^{j+\ell-1}.
\]

No archived layer matrix and no archived obstruction equation is used as an
input. All Gaussian pivots are fixed nonzero elements of `K0`; no polynomial
in a deformation parameter is inverted during layer elimination. The replay
records the ordered row/column bases, matrix hashes, pivot columns, and hashes
of the exact pivot units for every layer.

The quintic is certified irreducible by reduction modulo `67` and a Rabin
irreducibility test. The six displayed coefficient relations then reconstruct
`p`; the face equation recursively reconstructs `q`; all eighteen face
coefficients are checked exactly.

## The truncated root

The reconstructed layer data are

| layer | unknowns | target rows | rank | kernel | nonzero compatibility equations |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 19 | 18 | 17 | 2 | 0 |
| 2 | 21 | 19 | 18 | 3 | 0 |
| 3 | 13 | 20 | 12 | 1 | 7 |
| 4 | 0 | 20 | 0 | 0 | 18 |
| 5 | 0 | 21 | 0 | 0 | 0 |

Only four effective variables occur in the obstruction ideal, with weights
`(1,1,2,2)`. The eighteen weight-four equations together with the seven
weight-three equations multiplied by the two weight-one variables span all
fourteen weight-four monomials. The exact selected `14 x 14` minor is nonzero;
its canonical coefficient-vector hash is

```text
8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059
```

Thus the four effective variables lie in the radical. The required top
`P`- and `Q`-vertex coefficients are positive-weight polynomials in those
variables and therefore vanish, contradicting the exact support. The
truncated root is closed.

## The full root through layer four

The layer data through four are

| layer | unknowns | target rows | rank | kernel | nonzero compatibility equations |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 19 | 18 | 17 | 2 | 0 |
| 2 | 21 | 19 | 18 | 3 | 0 |
| 3 | 21 | 20 | 18 | 3 | 0 |
| 4 | 19 | 20 | 18 | 1 | 2 |

After duplicate normalization, the layer-four compatibility ideal contains

\[
\text{unit}\cdot(t_{2,2}-\alpha t_{1,1}^2)^2.
\]

The square is retained in the machine-readable manifest. It is **not**
replaced scheme-theoretically by its linear factor. For geometric routing over
an algebraic closure, however,

\[
V\bigl((t_{2,2}-\alpha t_{1,1}^2)^2\bigr)
 =V(t_{2,2}-\alpha t_{1,1}^2).
\]

On this reduced support the two required upper-right vertex coefficients are

\[
[P]_{(8,16)}=c_Pt_{1,1}^2,
\qquad
[Q]_{(12,24)}=c_Qt_{1,1}^3,
\qquad c_Pc_Q\ne0.
\]

Hence the closed complement `t1_1=0` is empty on the exact-support locus. This
is the only variable denominator introduced by the normalization below.

The origin-vertex parameters

```text
U = [P]_(0,0),    D = [Q]_(0,0)
```

are also nonzero on the exact support, but they never occur in a compatibility
equation. Coefficients of deficiency greater than eight, including the extra
full-support vertices `(0,8)` and `(0,12)`, are not divided by or assigned a
terminal value: the reconstruction simply forgets them. This is a safe
relaxation because every full-support solution projects to the
layer-through-eight system, while emptiness of the projection excludes every
possible higher-deficiency completion.

## Weighted normalization and the fifteen equations

The nine early-layer parameters have weights

```text
1,1,2,2,2,3,3,3,4.
```

On `D(U*D*t1_1)`, the weighted multiplicative action gives the exact
cross-section

\[
t_{1,1}=1,\qquad t_{2,2}=\alpha.
\]

With

\[
x=\frac{t_{1,0}}{t_{1,1}},\quad
 a=\frac{t_{2,1}}{t_{1,1}^2},\quad
 b=\frac{t_{3,1}}{t_{1,1}^3},\quad
 c=\frac{t_{3,2}}{t_{1,1}^3},\quad
 d=\frac{t_{4,0}}{t_{1,1}^4},
\]

the early-layer open locus is

\[
\mathbf G_m^3\times V(F_0,\ldots,F_{14}),
\]

where the three unit coordinates are the normalized `U`, normalized `D`, and
`t1_1`. Continuing the exact recursion gives equation counts

```text
weight 5: 1
weight 6: 3
weight 7: 5
weight 8: 6
```

and canonical digest

```text
d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883
```

## Direct attachment of the compact toric terminal

The compact terminal equations are not an analogous or separately normalized
system. By exact coefficient provenance, they are literally the ordered
subfamily

\[
F_4,F_6,F_8,F_9,F_{10},F_{11}
\]

of the reconstructed fifteen. Therefore

\[
V(F_0,\ldots,F_{14})
 \subseteq
V(F_4,F_6,F_8,F_9,F_{10},F_{11}).
\]

The existing compact toric theorem proves that the six-polynomial locus is
empty over `overline(K0)`. This is the required consequence/relaxation edge,
so the normalized fifteen-equation locus is empty. Together with the closed
`t1_1=0` complement, every child of the reduced full-root node terminates in
an empty node.

Finally, the full layer-through-eight obstruction scheme retaining the square
equation is empty, not merely its reduction. Indeed, a nonzero finite-type
`K0`-algebra remains nonzero after faithfully flat base change to
`overline(K0)` and then has a maximal ideal. Since the geometric support of
the full obstruction scheme after that base change has no point, its
coordinate algebra must already be zero. The layer-four square hypersurface
by itself is, of course, not claimed empty.

## Adjacent-chart attempt

For the bare wall shear

\[
Y'=Y+\lambda X^{-k}
\]

one has, in `(t,z)` coordinates,

\[
t'=t(1+h),\qquad z'=z(1+h)^2,
\qquad h=\lambda t^{2k-1}z^{-k}.
\]

Thus `k=4` starts at normal order `7`. A filtration-preserving conjugacy with
invertible associated graded cannot change the first nonzero order, so this
shear cannot identify the recorded layer-four residual. The stored adjacent
layer-five-through-seven terminal remains exact but unattached. It is included
as a noncovering diagnostic edge only and is absent from both closure paths.

This negative lemma is the weakest Lane 9 result needed here: once the direct
toric projection is established, no adjacent-chart covering theorem is
required to close Lane 8.

## Files

- `lane8-full-root-proof.md` — conventional mathematical proof of the replay,
  complement split, toric consequence edge, scheme boundary, Lane 9 negative
  lemma, and relative below-`125` corollary.
- `stage-manifest.json` — machine-readable index for the fields, rings,
  variables, ideals, layer matrices, pivots, denominators, saturations,
  complements, queue nodes, covering edges, terminal certificates, and the
  below-`125` import boundary stored under `manifest/`.
- `independent_raw_support_replay.py` — standalone exact replay entrypoint.
- `lane8_replay/` — dependency-free exact field, polynomial, support, layer,
  and certificate implementation.
- `fixtures/belyi_exact_field_relations.json` — exact projection of the public
  face packet to the minimal polynomial and six algebraic relations; the
  numerical embedding locator is deliberately omitted.
- `fixtures/quintic_field_fast.py` — exact arithmetic in `K0`.
- `verify_lane8_submission.py` — fail-closed source-pin, replay, manifest, and
  proof-queue validator.
- `VALIDATION.md` — pinned commands, output, and explicit omissions.

## Review boundary

The raw-support reconstruction and the attachment of the six equations are
replayed here. The compact toric emptiness theorem and the external
below-`125` Newton reduction are imported exact results, pinned to their
source labels. Specialist review should check those theorem interfaces before
promoting the relative corollary into a canonical theorem-bearing source.

## Validation

From the repository root, run

```bash
python contributions/JCG-C-0015/verify_lane8_submission.py
```

The command reruns both support reconstructions, verifies every stage hash and
queue reference, checks the exhaustive open/closed split, and rejects any
closure path using the unattached adjacent terminal.

## Evidence and provenance boundary

The raw-support reconstruction and the coefficientwise attachment of the six
terminal equations are independently replayed here. The 88.5 MB compact toric
archive is not independently regenerated; its exact emptiness theorem is an
explicit imported theorem. A direct generic Gröbner-basis attempt on the good
fiber exceeded a five-minute audit cap and is not used as evidence.

AI-assisted and unrefereed. GPT-5.6 Pro assisted with source auditing, exact
symbolic reconstruction, proof development, drafting, and validation. The
repository owner remains responsible for accepting, revising, or rejecting
every assertion.
