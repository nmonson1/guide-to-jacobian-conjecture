# Presentation-stable obstructions to homogeneous compression

Lane 6 · 2026-08-03

## Scope

The fixed nineteen-variable suspension and several restricted obstruction
calculations are exact. A global compression theorem is not yet a defined
finite calculation because the repository has no exhaustive groupoid of
allowed presentation changes. The ready problem is therefore a precise
chain-level theorem that says when a supplied obstruction survives a declared
presentation groupoid and stabilization.

## Setup and definitions

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

## Restricted geometric evidence — not inputs to L6-T1

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

Prove the following groupoid criterion and express it in a finite form that
can be applied when the homogeneous-compression presentation maps become
available:

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

## Tasks

### L6-T1 — Prove and package the presentation-groupoid criterion — ready

Inputs: the definitions on this page, the transition formalism in the
[filtered-operation tool](lane-6-source-packet.md#source-6b8deae43ed5055d),
and the exact fixed-model notation in the
[tangent bridge](lane-6-source-packet.md#source-657b0874e22b951a).

Deliverable: a self-contained theorem and proof establishing functorial
transport of $H^1$, invariance of the forcing class, and invariance under
adding $[W\xrightarrow{\mathrm{id}}W]$. Give a finite generator-and-relations
certificate schema whose successful checks imply the theorem for a declared
finite presentation groupoid.

Dependencies: only finite-dimensional cochain complexes, explicit chain
maps, explicit inverse and relation homotopies, and explicit forcing
coboundaries as defined above.

Limits: the abstract theorem does not show that the geometric
presentation changes have been exhaustively listed or that its obstruction
classes satisfy the criterion.

### L6-T2 — Apply the criterion to all nineteen-to-eighteen presentations — not ready

Inputs: L6-T1, the [nineteen-variable suspension](../proof-sources/05-homogeneous-descendants/main.md),
the [selected-plane theorem](lane-6-source-packet.md#source-657b0874e22b951a),
and the [fixed-lower-target source obstruction](lane-6-source-packet.md#source-d56a78386f6d1442).

Deliverable: either an explicit eighteen-variable homogeneous realization
with its Jacobian and collision checked, or a nonzero obstruction class
transported across every object of an exhaustive presentation groupoid.

Dependencies: a public exhaustive list of allowed presentation operations,
stabilization maps, their linearized source and equation maps, and the
comparison of moving-target gauges. Those data are not currently available.

Limits: the selected plane, the residual fixed-lower-target theorem, and the
ten-direction moving-target pilot are different restricted models and may not
be combined without explicit comparison maps.

Alternative connections: an escaping-complexity invariant from Lane 3 is
relevant only after a chain map proves compatibility with homogeneous
stabilization.

## Limits

No present result proves that nineteen variables are minimal. The ready
output is a reusable mathematical criterion; the concrete global application
remains non-ready until the presentation groupoid and its operation matrices
are supplied.

## Direct sources

- [Rank-sensitive suspension and restricted compression results](../proof-sources/05-homogeneous-descendants/main.md)
- [Filtered operation complex and transition contract](lane-6-source-packet.md#source-6b8deae43ed5055d)
- [Tame source-coupled residual-branch theorem](lane-6-source-packet.md#source-d56a78386f6d1442)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-6-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
