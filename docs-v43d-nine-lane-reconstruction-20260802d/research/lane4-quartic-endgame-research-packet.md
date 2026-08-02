---
title: "Lane 4 quartic endgame repair and reproduction packet"
description: "Unrefereed proof repairs, candidate quartic exclusions, a global case-tree audit, and exact symbolic replays."
---

# Lane 4 quartic endgame repair and reproduction packet

<p class="claim-tag">Unrefereed research packet · Program 2 · 2 August 2026</p>

This additive packet records proof repairs and exact symbolic reproductions
produced during an audit of Lane 4. It does not modify the generated claim
graph or promote a new unconditional theorem.

!!! warning "Current theorem boundary"
    The unconditional public interval remains
    \[
    4\le D_{\min}\le 7.
    \]
    This packet does **not** assert \(D_{\min}\ge5\). The new arguments are
    candidate proofs requiring specialist review, and the remaining
    degree-three proof-to-code attachment has not been completed.

## Downloads

- [Packet README and archive instructions](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/README.md)
- [Standalone compilable TeX manuscript](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/lane4-quartic-endgame-repairs.tex)
- [Global case-tree audit](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/case-tree/global-case-tree-draft.md)
- [Machine-readable case-tree table](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/case-tree/global-case-tree.csv)
- [Compact exact replay driver](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/replay_packet.py)
- [Captured compact replay](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/replay-compact.out)
- [Captured forty-check replay](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/replay-full.out)
- [Packet manifest](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/MANIFEST.json)
- [SHA-256 checksums](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/SHA256SUMS)
- [Archive assembly script](../assets/audit-repairs/lane4-quartic-endgame-repairs-2026-08-02-v1/assemble_archive.py)

## Candidate mathematical advances

### Structural repairs

The leading-image factorization is reproved using the normalization of the
actual projective image curve rather than the invalid implication from
relative algebraic closedness to birationality. The repaired argument gives

\[
H_4=G\,h(A,B),\qquad \deg G+e\deg A=4,
\]

with the same four nondegenerate numerical leaves

\[
(e,\deg A,\deg G)=(2,1,2),(2,2,0),(3,1,1),(4,1,0).
\]

The span-two four-locus routing is also rewritten as an explicit
composite/primitive valuation argument. It distinguishes the binary,
quadratic-source, fourth-power, and nonbinary fixed-component loci and states
an ownership convention for their overlaps.

The packet additionally supplies:

- a reader-level route for the vanishing cubic normal layer \(R=0\), subject
  to the same low-degree plane theorem used elsewhere in Program 2; and
- a homogeneous cubic Hamiltonian-centralizer lemma that gives the exact
  hypothesis needed in the nonbinary fixed-component endpoint.

### Completion of the conic and rational-cubic span-three leaves

Three conic representatives not covered by the original four-orbit
invariant-field proof are treated separately:

\[
G=z^2,\qquad G=x^2,\qquad G=xy.
\]

The `z^2` checker retains every quadratic coefficient and the entire linear
part. The `x^2` and `xy` calculations split the stabilizer action into scalar,
semisimple, nilpotent, anti-scalar, and zero-normal charts; every exact branch
forces \(\det L=0\) or contains a fixed nonzero determinant coefficient.

A separate candidate theorem excludes a proper rational-cubic leading image.
It treats cuspidal and nodal cubics, transverse and marked common factors, the
full one-parameter marked nodal family, and the projective endpoint. One exact
nodal quadratic-layer maximal minor is the constant

\[
12582912=2^{22}\cdot 3.
\]

Together with the existing rank-one and rational-quartic leaves, these
arguments yield a candidate leading-target-span-two corollary.

### High ramification and one exceptional degree-three divisor

For a primitive coprime binary quartic pencil, put

\[
U=J(Q,R),\qquad V=J(P,R),\qquad W=J(P,Q),\qquad
r=\deg\gcd(U,V,W).
\]

The packet gives a candidate conventional proof that \(r=4\) or \(5\)
forces an automorphism. Its \(r=4\) argument includes the complete projective
repeated-root incidence, the internal \(2+2\) divisor, and the endpoint
strata; it therefore does not import the earlier complete-specialization
assertion as a black box.

It also independently reconstructs and excludes the primitive
\(r=3\), \(\tau=-1\) Hilbert--Burch divisor. The terminal primitive
intersection has two possible first-normal rays, and the next determinant
coefficient is respectively

\[
-\frac{h^3}{2}(x+y)(5x^2+2xy+5y^2)
\]

and

\[
\frac{135h^3}{2}(x-y)(x+y)^2,
\]

so both amplitudes vanish.

## Exact reproduction

The recorded environment is Python 3.13.5 with SymPy 1.14.0. The compact
replay runs six independent program entry points covering the `z^2` conic,
quoted conic terminal identities, the complete \(r=4,5\) checker, the
\(\tau=-1\) checker, one transverse rational-cubic calculation, and the
constant nodal maximal minor.

The complete archive is stored as four adjacent `.zip.partNN` files. After
checking out the pull-request branch, reconstruct and replay it with:

```bash
cd docs-v43d-nine-lane-reconstruction-20260802d/assets/audit-repairs/\
lane4-quartic-endgame-repairs-2026-08-02-v1
python assemble_archive.py
unzip lane4-quartic-endgame-repairs-2026-08-02-v1.zip
cd lane4-quartic-endgame-repairs-2026-08-02-v1
python -m pip install -r requirements.txt
python replay_packet.py
```

The archive additionally contains the full ten-branch `x^2`/`xy` conic
replay, the wider rational-cubic script family, raw outputs, the exact
high-ramification and \(\tau=-1\) checkers, and a checksum manifest.

## Evidence and scope boundaries

The exact scripts verify displayed determinant identities, finite chart
eliminations, projective incidence equations, ranks, kernels, saturation
certificates, and terminal factors. They do not independently prove every
upstream geometric classification or Hilbert--Burch placement statement.
All programs remain one SymPy lineage.

Earlier exploratory conversation notes described additional independent work
on a generic `F_4` family and the `tau=0` divisor. Their complete source files
were unavailable during packet assembly. They are deliberately omitted from
the source-backed claims here; the public v5 supplement remains the evidence
for those charts.

Before any unconditional quartic theorem is asserted, the following gates
remain:

1. attach every remaining \(r=3\) exceptional divisor to an exact theorem and
   program group, and independently reconstruct or audit `tau^2+1=0`, `c=0`,
   dependent-syzygy, and quadratic-exceptional charts;
2. complete the proof-to-code crosswalk for quadratic-source and fixed-factor
   leaves;
3. verify the precise low-degree plane theorem formulation used by the
   triangular exits; and
4. obtain specialist review of the new conventional proofs and a genuinely
   independent computational reproduction.

## Provenance

GPT-5.6 Pro assisted with the mathematical audit, proof exploration and
drafting, exact-program construction, replay, and packet assembly. The
repository owner remains responsible for accepting, revising, or rejecting
every statement before it enters the authoritative mathematical record.
