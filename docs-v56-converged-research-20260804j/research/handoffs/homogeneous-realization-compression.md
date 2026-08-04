---
title: "Model research brief — Presentation-stable obstructions to homogeneous compression"
description: "A self-contained mathematical handoff for a research model."
---

# Presentation-stable obstructions to homogeneous compression

<p class="claim-tag">Lane 6 · Updated 4 August 2026</p>

## Scope

The fixed nineteen-variable suspension and several restricted obstruction
calculations are exact. A global compression theorem is not yet a defined
finite calculation because the repository has no exhaustive groupoid of
allowed presentation changes. The ready problem is therefore a precise
chain-level theorem that says when a supplied obstruction survives a declared
presentation groupoid and stabilization.

## Setup and definitions

The starting map is the [public Atkins--Turkish eleven-variable
source](https://gist.github.com/Spacerat/08b4a43f6b6ca57178efabc220170ce8), a
degree-at-most-three descendant of the Alpöge--Fable three-dimensional
counterexample. It already carries three explicit colliding source points.
The number eleven belongs to that supplied descendant; the passage from
eleven to nineteen is the general rank-sensitive suspension below, not an
additional dimension-reduction claim.

The fixed construction begins with an eleven-variable Keller map
$K=X+Q+C$, where $Q$ and $C$ are homogeneous of degrees two and three and
the coordinate span of $C$ has dimension seven. Writing $C=Bq$ and adjoining
$w\in\mathbb A^7$ and a homogenizing coordinate $t$ gives

\[
G(X,w,t)=\bigl(X+tQ(X)+t^2Bw,\ w-q(X),\ t\bigr),
\]

a nineteen-variable Keller map of the form \(I+H\), where its nonlinear part
\(H=(tQ+t^2Bw,-q,0)\) is homogeneous of degree three, carrying the known
collision. Here the entries of \(q\) are cubic forms: they form a basis of the
coordinate span of \(C\).

For the abstract comparison, let $\mathcal P$ be a groupoid of declared
presentations. Each object $p$ has a two-term cochain complex

\[
K_p=[V_p\xrightarrow{d_p}E_p]
\]

in degrees $0$ and $1$. Here $V_p$ is the direct sum of the source, target,
and presentation directions allowed at $p$, $E_p$ is the equation space, and

\[
H^1(K_p)=\operatorname{coker}(d_p)
\]

is the obstruction space. A forcing vector $o_p\in E_p$ defines the class
$[o_p]\in H^1(K_p)$.

A morphism $g:p\to q$ consists of linear maps

\[
A_g:V_p\to V_q,\qquad B_g:E_p\to E_q
\]

satisfying $B_gd_p=d_qA_g$, together with a chain-homotopy inverse. It
transports the forcing when

\[
B_g(o_p)-o_q\in\operatorname{im}(d_q).
\]

Concretely, if $\bar g:q\to p$ is the chosen inverse, the degree-$-1$
homotopies are maps $h_p:E_p\to V_p$ and $h_q:E_q\to V_q$ satisfying

\[
A_{\bar g}A_g-I_{V_p}=h_pd_p,\qquad
B_{\bar g}B_g-I_{E_p}=d_ph_p,
\]

and the analogous two identities on $q$. These equations fix the cochain
degree and sign convention used by the requested certificate.

A **stabilization** replaces $K_p$ by
$K_p\oplus[W\xrightarrow{\mathrm{id}}W]$ and $o_p$ by $(o_p,0)$.
Thus a presentation-stable obstruction is a nonzero class preserved by the
induced $H^1$ isomorphisms for all declared morphisms and by these
contractible stabilizations.

## Results to use

- The filtered-operation tool checks finite transition identities, operation
  image transport, rechart transport, dual obstruction pullback, forcing
  transport, and induced quotient maps. It does not discover the true
  presentation groupoid.

For the separate row-base calculation, let \(\mathcal E\cong\mathbf A^{115}\)
be the space of weight-preserving quadratic source vector fields
\(e_{v_i}m\), where \(m\) is a quadratic monomial of the same torus weight as
\(v_i\). For the fixed eleven-variable tensor put
\(M(P)=C+[Q,P]\in\operatorname{Mat}_{11\times286}\). Splitting its rows as
\(Y=(x,y,z,b,c,s)\) and \(Z=(a,d,q,h,k)\), the rank-six incidence is
\(Z(P)=H\,Y(P)\) with \(H\in\operatorname{Mat}_{5\times6}\).

The exact row-killing family is the affine twenty-plane
\(\mathcal R=P_0+K_{\rm row}\) with retained basis
\(\xi_0,\ldots,\xi_{19}\). A finite projective normal slope
\(r=u/v\) has a fifteen-dimensional compatible row fibre with basis

\[
\xi_2-\tfrac23\xi_0,\quad \xi_{19}+4\xi_0,\quad
\xi_6,\ldots,\xi_{18},
\]

while the infinity slope \(v=0,u=1\) has the eighteen-dimensional basis
\(\{\xi_i:i\ne3,4\}\). The linked adapters reconstruct these vectors and
allow the full 22-dimensional higher-correction freedom. A “full row-base
locus” means all points of both affine fibres, not the finite coordinate
samples already tested.

## Restricted geometric evidence — not assumptions of the interface theorem

- On one selected projective rank-six plane in a pinned 115-dimensional
  source-operation model, every nonzero projective direction is obstructed
  at cubic or quartic order. This is a theorem about that plane only.
- A separate residual rational rank-six branch has a divergence-free tame
  quadratic-jet representative and two exact obstruction functionals in a
  fixed lower-target gauge. Moving lower target jets and stabilization are
  outside that theorem.
- A ten-direction moving-target pilot is a third restricted model. It is not
  a calculation on the residual rational branch.

These computations motivate the interface theorem; no comparison map among
the three restricted models has been supplied.

## Example: a contractible stabilization

If $K=[V\xrightarrow dE]$ has a nonzero obstruction class $[o]$, then

\[
K' = K\oplus[W\xrightarrow{\mathrm{id}}W]
\]

has $H^1(K')\cong H^1(K)$ and $(o,0)$ represents the same nonzero class.
This is a genuine stability statement for an explicitly contractible added
block; it does not assert that every geometric stable-variable operation has
already been identified with such a block.

## Live problem

Prove the following obstruction-groupoid criterion, shared with Lane 9, and
express it in a finite form that applies both to homogeneous presentations
and to boundary-chart attachment:

The cohomological invariance in the criterion is standard. The research
deliverable is infrastructure: an exact schema, checker, and mutation tests
that prevent a program-specific geometric groupoid from being silently
replaced by an incomplete list of moves.

> Chain-homotopy equivalences $(A_g,B_g)$ induce a functor
> $p\mapsto H^1(K_p)$ on $\mathcal P$. If the forcing vectors satisfy
> $B_g(o_p)-o_q\in\operatorname{im}(d_q)$ on a generating set of morphisms,
> compatibly with the groupoid relations, then nonvanishing of one class
> $[o_p]$ is equivalent to nonvanishing at every object in its connected
> component and is unchanged by contractible stabilization.

The finite success criterion must state exactly which matrices, inverse
homotopies, relation homotopies, and forcing coboundaries have to be checked.

For a finite presentation \(\langle G\mid\mathcal R\rangle\) of the declared
groupoid, the intended certificate lists the complex at each object; a chain
map, chosen inverse, and inverse homotopies for every generator; a forcing
coboundary for every generator; and, for every relation word in
\(\mathcal R\), a displayed chain homotopy from the composite chain map to
the identity at its base object. Checking the two boundary identities for
each such homotopy is the relation-coherence condition needed here; no
unstated geometric presentation moves may be inferred from the certificate.

This abstract theorem, fail-closed schema, checker, and negative test suite
form the ready task.  Encoding the supplied characteristic-zero ambient
\(E_0,E_1,E_{-1}\) wall atlas is a separate application blocked on that
interface.  It is a useful cross-lane benchmark after the checker exists, but
it neither belongs to the theorem's hypotheses nor supplies the missing
nineteen-to-eighteen presentation groupoid.

## Current tasks

<!-- RETAINED_TASKS_START -->
### Resolve the full finite and infinity row-base obstruction locus — Ready now

`TSK-L6-FULL-ROW-BASE-V3` · proof, computation, exploration · sustained

**Goal.** Classify every point of the 15-dimensional finite-slope and 18-dimensional infinity row-base fibres by finite-order obstruction, formal lift, or an exact reduction to certified strata.

**Why it matters.** This supplies the full-fibre source-field input needed by the homogeneous noncompression strategy, rather than another finite sample.

**Public inputs.**

- [Complete cubic-quartic obstruction on the selected projective rank-six plane](../working-mathematics/units/RMU-5D8E0004.md) (retained unit `RMU-5D8E0004`).
- [Exact 38-direction benchmark in the Program 5 row-base fibres](../working-mathematics/units/RMU-5D8E0005.md) (retained unit `RMU-5D8E0005`).
- [Exact finite-slope and infinity fibre bases, sample convention, and cubic-lift adapter.](lane-6-source-packet.md#source-52fbb794f2109238).
- [Order-four infinity-fibre lifting convention and precise sampling boundary.](lane-6-source-packet.md#source-35353179167a0fb2).
- [Exact 115-dimensional operation model, row-killing family, finite-direction theorem, and residual strata.](lane-6-source-packet.md#source-439f409d568135ac).
- [Canonical eleven-variable tensor and extension verifier imported by the adapters.](lane-6-source-packet.md#source-2ef74db0cfea125b).

**Complete when.**

- Every point of both row-base fibres lies in a proved obstruction stratum, an explicitly integrated stratum, or a finite certified reduction whose cases are all resolved.

**Possible starts.**

- Use the displayed affine fibre bases to stratify exact cubic effect and augmented ranks before lifting each remaining stratum.
- Seek a coordinate-free left-kernel pairing or quartic separator uniform on both projective slope charts.

**Freedom.**

- A stronger invariant theorem or a genuine lifting family is welcome.

**Mathematical limits.**

- Coordinate samples and the selected plane do not classify either fibre.
- This pinned source-field model does not include all target, stabilization, or presentation moves.

### Prove and implement the fail-closed obstruction-groupoid interface — Ready now

`TSK-L6-L9-OBSTRUCTION-GROUPOID-SCHEMA-V3` · proof, reusable interface theorem, computation · bounded

**Goal.** State and prove the finite generator-and-relations transport and contractible-stabilization theorem, define a certificate schema containing every required complex, map, homotopy, forcing coboundary, quotient, and dual field, and implement a checker that rejects any omitted or inconsistent field.

**Why it matters.** This supplies one reusable theorem and machine-checkable interface for both homogeneous-presentation transport and plane-chart attachment.

**Public inputs.**

- [Parameter-complete obstruction criterion for an F2 attachment block](../working-mathematics/units/RMU-6C9E0011.md) (retained unit `RMU-6C9E0011`).
- [Existing finite transition, quotient, dual, forcing, relation, and stabilization contract.](lane-6-source-packet.md#source-6b8deae43ed5055d).
- [Current exact checker schema to extend fail-closed.](lane-6-source-packet.md#source-32f266f643e1100f).

**Complete when.**

- The theorem is proved, every proof hypothesis is a required certificate field, valid examples replay, and mutation tests show that omission or corruption of each field fails.

**Possible starts.**

- Prove functoriality on generators and relation words, then encode exactly the identities used by the proof as mandatory schema fields and negative tests.

**Freedom.**

- An equivalent derived formulation is allowed if it exports the same finite certificate and verdict.

**Mathematical limits.**

- The interface does not discover or prove exhaustive any program-specific geometric operation groupoid.
- Passing the schema does not identify ambient wall charts with actual adjacent F2 charts.

### Certify the characteristic-zero ambient three-wall atlas — Blocked

`TSK-L6-L9-AMBIENT-WALL-CERTIFICATE-V1` · computation, proof · bounded

**Goal.** Encode the supplied characteristic-zero E_0,E_1,E_{-1} wall atlas in the certified schema and prove by one hash-pinned replay that its transitions, relations, forcing transport, quotients, duals, and triple overlaps pass.

**Why it matters.** This gives the shared interface one concrete cross-lane benchmark without confusing the ambient atlas with either program's missing geometric groupoid.

**Public inputs.**

- [Exact k=4 wall transport, grading correction and finite overlap groupoid](../working-mathematics/units/RMU-6C9E0010.md) (retained unit `RMU-6C9E0010`).
- [Exact ambient wall maps and finite-order overlap identities.](lane-6-source-packet.md#source-d6c38a4c865ab7c9).
- [Dual transport and triple-overlap theorem for the ambient atlas.](lane-6-source-packet.md#source-bcb444020cf39f50).

**Task dependencies.**

- `TSK-L6-L9-OBSTRUCTION-GROUPOID-SCHEMA-V3`

**Blocked on.**

- The fail-closed shared certificate schema and checker have not yet been completed.

**Complete when.**

- The complete ambient certificate and source hashes pass the shared checker and independently reproduce all 73 declared identities.

**Possible starts.**

- Use the nilpotent quadratic wall transport to certify that parameters 0, 1, and -1 generate the stated finite-order ambient saturation in characteristic zero.

**Freedom.**

- An equivalent three-parameter certificate is allowed if its equivalence to the supplied atlas is proved.

**Mathematical limits.**

- The certificate does not prove either geometric operation list exhaustive.
- The ambient wall charts are not the absent actual adjacent F2 charts.

### Apply the interface to every nineteen-to-eighteen presentation — Blocked

`TSK-L6-EXHAUSTIVE-19-18-V3` · proof, computation · open ended

**Goal.** Transport a nonzero obstruction across every allowed nineteen-to-eighteen presentation or construct an explicit eighteen-variable realization.

**Why it matters.** This is the actual global compression question beyond restricted planes, branches, and pilots.

**Public inputs.**

- [Complete cubic-quartic obstruction on the selected projective rank-six plane](../working-mathematics/units/RMU-5D8E0004.md) (retained unit `RMU-5D8E0004`).
- [Exact 38-direction benchmark in the Program 5 row-base fibres](../working-mathematics/units/RMU-5D8E0005.md) (retained unit `RMU-5D8E0005`).

**Task dependencies.**

- `TSK-L6-L9-OBSTRUCTION-GROUPOID-SCHEMA-V3`

**Blocked on.**

- The exhaustive presentation-operation list is absent.
- Its source, equation, gauge, stabilization, and comparison maps are absent.

**Complete when.**

- Every allowed presentation is covered and yields either a transported nonzero class or a verified realization.

**Possible starts.**

- First enumerate the actual presentation moves and encode their maps in the shared certificate schema.

**Freedom.**

- A coordinate-free obstruction reducing the full groupoid to finitely many strata is welcome.

**Mathematical limits.**

- Do not combine the selected plane, residual fixed-gauge branch, and moving-target pilot without comparison maps.
<!-- RETAINED_TASKS_END -->

## Limits

No present result proves that nineteen variables are minimal. The ready
output is a reusable mathematical criterion; the concrete global application
remains non-ready until the presentation groupoid and its operation matrices
are supplied.

## Direct sources

- [Rank-sensitive suspension and restricted compression results](../proof-sources/05-homogeneous-descendants/main.md)
- [Filtered operation complex and transition contract](lane-6-source-packet.md#source-6b8deae43ed5055d)
- [Tame source-coupled residual-branch theorem](lane-6-source-packet.md#source-d56a78386f6d1442)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Optional runnable source ZIP](../inputs/lane-6-source-files.zip) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
