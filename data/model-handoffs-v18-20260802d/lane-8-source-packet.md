# Lane 8 exact research source packet

This is the public source packet for **Plane Newton queue and terminal certificates**. It contains the
selected proof notes, exact computation contracts, and checkers used
by the concise lane brief. Read only the files relevant to the route
you pursue. Stored outputs and very large reconstructible matrices are
omitted; the mathematical boundary of each checker remains in its
source text.

Private-source commit: `e38fa7bda854c38167b05c7e8b79ca61bbfade04`.

## Included files

- `lane8-proof-queue-20260802-v1/lane8-proof-queue-repair.md` — `bdbe6c5557e93c3dbafac75ffbf3c833eb22d5988af9e3f7bfcbdd4b040b94f0`
- `lane8-proof-queue-20260802-v1/check_queue.py` — `e1b6556645ff74e18ce04600f1d1e5ff7bcbe30e4dfeaa9ec53cadbe7b32320e`
- `lane8-proof-queue-20260802-v1/full_early_layer_reduction.py` — `ed4a150374eb969e19bf8601f8f4529edae57fb457f9aae9211997fb6f83bd95`
- `lane8-proof-queue-20260802-v1/quintic_face_reconstruction.py` — `e48869fb09d7afcc3c1ae08a604c7656efadf0c3588c0fca82a42817dfaf8c1f`
- `lane8-proof-queue-20260802-v1/truncated_support_certificate.py` — `40daac940f6c82e76a3679495e14cd0fcadfe5a926b3053eeff2cab879401da5`
- `lane8-proof-queue-20260802-v1/queue.seed.json` — `a55e0c1aaf49d834ec0004c14f64e0ba04d8d969d1af9cde5eef01da4ea28743`
- `lane8-proof-queue-20260802-v1/truncated_support_certificate.json` — `f086c7eca67d51f3c48fd6311c55e8fe5012a8b1373ff6eae4746fd4c3fec6ac`

## `lane8-proof-queue-20260802-v1/lane8-proof-queue-repair.md`

<pre><code class="language-markdown">
---
title: "Lane 8 proof-queue repair"
description: "A proof-carrying contract for the plane Newton queue, with an audited literature import and exact root-to-face checks."
---

# Lane 8 proof-queue repair

&lt;p class="dek"&gt;This additive repair separates the imported below-125 reduction,
the post-root coefficient queue, and adjacent-chart attachment.  It also closes
the first exact segment of the queue: both normalized `(8,28)` Newton
alternatives force the same degree-21 Belyi face, its five normalized covers
are reconstructed as one explicit quintic Galois orbit, and the entire
truncated root is excluded by a new exact normal-layer certificate.&lt;/p&gt;

!!! warning "Scope"
    This page does not alter the stable claim graph and does not promote the
    public below-125 statement.  It repairs the operational contract for
    &#91;Lane 8&#93;(handoffs/plane-newton-queue-terminal-certificates.md).  The stored
    terminal certificates remain exact for their displayed systems; global
    coverage still requires independently replaying the coefficient-routing
    edges recorded below.

## 1. Repaired theorem architecture

Three logically separate results are required.

### A. Imported root theorem

Let `K` have characteristic zero.  If a noninvertible plane Keller pair over
`K` has maximum coordinate degree below `125`, then, after exchanging the two
coordinates if necessary and applying the reductions in Guccione--Guccione--
Horruitiner--Valqui, it reaches the `(8,28)` family.  Proposition 4.3 of that
paper then produces a Laurent pair

```text
P,Q in K&#91;x,x^(-1),y&#93;,        &#91;P,Q&#93;=x^2,
```

with one of the two Newton-polygon pairs listed in section 2 below.

The primary sources are &#91;the 2022 degree-reduction paper&#93;(https://arxiv.org/abs/2204.14178)
and &#91;the 2017 complete-chain algorithms paper&#93;(https://arxiv.org/abs/1708.07936).
This import is the combination of:

1. Theorem 2.1, which leaves only degree pair `(72,108)` below `125`;
2. Proposition 4.1 and Corollary 5.7, which eliminate the other `(72,108)`
   family `(9,27)`;
3. Proposition 4.3, which gives the two `(8,28)` roots.

The packet independently checks the last monomial-coordinate transformation
and its Jacobian multiplier.  It does not reprove every cited theorem used
inside the literature reduction.

### B. Post-root queue theorem

For each root constructible locus `X_R`, construct a finite directed acyclic
graph with two distinct classes of edges.  A **covering edge** must justify the
backward implication

```text
all covering children empty  =&gt;  parent empty.
```

A **dependency edge** may establish a passport, field model, classification,
or other auxiliary datum, but it cannot propagate emptiness.  Every
nonterminal locus must be covered by its geometric children, and every
terminal locus must carry a replayable exact emptiness certificate.  This is
the mathematical content of Lane 8 after the literature import.

### C. Chart-correspondence theorem

Any edge that changes complete-chain chart must identify the common formal
branch, transport the support and residue conditions, and prove the relevant
overlap statement.  That is principally &#91;Lane 9&#93;(handoffs/plane-chart-correspondence-global-attachment.md).
A stored specialization in an adjacent chart is not a covering edge unless
this correspondence is proved.

The global implication has the form

```text
sub-125 Keller pair
    -- imported theorem --&gt; one of two normalized roots
    -- proof-carrying DAG --&gt; a certified empty terminal system
    -- chart descent when used --&gt; contradiction.
```

## 2. The two exact roots

The two alternatives are named `truncated` and `full` in this repair.
`N(P)` denotes the convex Newton polygon, not the set of coefficients required
to be nonzero.

| root | `N(P)` vertices | `N(Q)` vertices | lattice points `(P,Q)` |
|---|---|---|---:|
| truncated | `(0,0),(1,0),(8,14),(8,16)` | `(0,0),(2,1),(12,21),(12,24)` | `(25,47)` |
| full | `(0,0),(1,0),(8,14),(8,16),(0,8)` | `(0,0),(2,1),(12,21),(12,24),(0,12)` | `(61,125)` |

The lattice-point counts are independently regenerated by
&#91;`root_face_check.py`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/root_face_check.py).
Exact Newton polygon means that each listed vertex coefficient is nonzero and
that no exponent outside the polygon occurs.  Interior and nonvertex boundary
coefficients may vanish.

The final coordinate map in Proposition 4.3 is

```text
phi(x)=x^(-1),       phi(y)=x^4 y.
```

It sends exponent `(a,b)` to `(-a+4b,b)` and has Jacobian determinant `-x^2`.
The packet verifies that it sends the pre-final vertices in the proof to the
two polygon pairs above.  Thus the displayed bracket normalization is also
checked rather than treated as a diagrammatic convention.

### Polygon versus coefficient window

The truncated lattice windows are subsets of the full windows.  Consequently
both roots may be embedded in one full coefficient ambient space by setting
the full-only coefficients to zero on the truncated branch.  This is a sound
**relaxation**, but it does not merge the two exact roots whenever a later step
inverts a full-only coefficient.  Any such localization must retain the
closed complementary branch.

## 3. Exact progress: the common degree-21 face is forced

Give a monomial `x^a y^b` the value

```text
nu(a,b)=-2a+b.
```

For both roots, the minimum values are `-2` on the edge from `(1,0)` to
`(8,14)` in `P`, and `-3` on the edge from `(2,1)` to `(12,21)` in `Q`.
With

```text
z = x y^2,
```

the initial forms therefore have the unique shapes

```text
P_face = x p(z),          deg p = 7,
Q_face = x^2 y q(z),      deg q = 10,
```

where the constant and leading coefficients of `p,q` are nonzero.  Direct
differentiation gives

```text
&#91;P_face,Q_face&#93;
 = x^2 (p q + 2 z p q' - 3 z p' q).
```

Since the full bracket is `x^2`, its least-valuation part forces

```text
p q + 2 z p q' - 3 z p' q = 1.                 (3.1)
```

This closes a previously ambiguous routing step: passage from either
Proposition 4.3 root to the degree-21 face is a forced initial-form edge, not a
chosen specialization.

### The Belyi map

Set

```text
tau(z) = z q(z)^2 / p(z)^3.
```

An exact identity is

```text
tau'(z)
 = q(z)/p(z)^4 * (p q + 2 z p q' - 3 z p' q).
```

Hence (3.1) gives `tau'=q/p^4`.  Equation (3.1) also implies:

- `p(0)q(0)=1`;
- every root of `p` is simple and is not a root of `q`;
- every root of `q` is simple and is not a root of `p`.

It follows that `tau` has degree `21` and passport

```text
(2^10 1),       (3^7),       (17 1^4).
```

The ramification contribution is

```text
10 + 14 + 16 = 40 = 2*21-2,
```

so there is no fourth branch value.  The exact Murnaghan--Nakayama check in
&#91;`hurwitz_degree21.py`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/hurwitz_degree21.py)
returns weighted Hurwitz number `5`.  A disconnected triple would have orbit
sizes `18+3`; on the three-point orbit the required transposition, 3-cycle,
and identity cannot multiply to one.  Thus all triples are transitive.  The
standard primitivity/Jordan argument then gives monodromy `A_21`, hence
trivial deck group, so the weighted count is exactly five isomorphism classes.

### Exact quintic coefficient orbit

The packet now reconstructs the five classes independently of the large
Program 6 archive.  Normalize

```text
p(z)=z^7+z^6+s z^5+...,
q_monic(z)=z^10+(3/2)z^9+... .
```

In reverse coordinates at infinity, the index-17 contact condition is

```text
Q(T)^2-P(T)^3 = O(T^17).
```

Solving its coefficients successively leaves the primitive parameter `s`
with irreducible polynomial

```text
287548593020928 s^5 - 688401965085696 s^4
+ 640652914818432 s^3 - 292066554895024 s^2
+ 65563255857792 s - 5817852446211 = 0.       (3.2)
```

&#91;`quintic_face_reconstruction.py`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/quintic_face_reconstruction.py)
constructs every coefficient of `p` and `q_monic` in `Q(s)`, and
&#91;`quintic_face_coefficients.json`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/quintic_face_coefficients.json)
exports them exactly.  It verifies

```text
deg(z q_monic^2-p^3) &lt;= 4,
p q_monic + 2z p q_monic' - 3z p' q_monic = c != 0.
```

Thus `q=q_monic/c` satisfies equation (3.1) exactly.  The coefficient of
`z^6` in `p` fixes the remaining source scaling: the unique simple point over
one branch value and the unique index-17 point over another already fix `0`
and infinity.  Distinct embeddings of the irreducible quintic therefore give
five distinct normalized covers.  Since the Hurwitz calculation gives only
five classes, these covers exhaust them and form one Galois orbit.

The reconstruction also verifies the exact field isomorphism to the public
Program 6 model

```text
K0 = Q&#91;u&#93;/(u^5-u^4+3u^3+3u^2+26)
```

by the map

```text
s = (20481190 - 2578004u + 1664322u^2
     - 709604u^3 + 221083u^4) / 42799752.       (3.3)
```

This closes the coefficient-field dependency and supplies canonical exact
lower-face input for both normal-layer branches.

## 4. Exact normal-layer equation

Put

```text
t=y,       z=x y^2,
P=t^(-2) A(z,t),       Q=t^(-3) B(z,t).
```

Because `det d(z,t)/d(x,y)=t^2`, the equation `&#91;P,Q&#93;=x^2` is exactly

```text
2 A B_z - 3 A_z B + t(A_z B_t - A_t B_z) = z^2.       (4.1)
```

Write

```text
A=sum_(r&gt;=0) t^r A_r(z),       B=sum_(r&gt;=0) t^r B_r(z).
```

The coefficient of `t^r` in the left side of (4.1) is

```text
E_r = sum_(i+j=r) ((2-i) A_i B_j' + (j-3) A_i' B_j).  (4.2)
```

For `r&gt;0`, the terms containing the new unknowns are

```text
D_r(A_r,B_r)
 = (2-r) A_r B_0' - 3 A_r' B_0
   + 2 A_0 B_r' + (r-3) A_0' B_r,
```

and all other summands are forcing terms from lower layers.  This identifies
the precise triangular operator that a queue implementation must transport.
For a monomial `x^a y^b`, its layer is

```text
d_P(a,b)=b-2a+2,       d_Q(a,b)=b-2a+3.
```

The independently regenerated layer-window sizes are:

```text
truncated P: 8,8,9
truncated Q: 11,11,12,13
full P:      8,8,9,8,7,6,5,4,3,2,1
full Q:      11,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1.
```

These formulas supply a canonical source for every later row and column
label.  A fixed-chart kernel may be quotiented only after its action on these
windows has been proved; a complete-chain operation that changes the window
is a rechart edge instead.


### Exact truncated-support certificate

For the truncated root, the support windows terminate at `A_2` and `B_3`.
Using the exact quintic face as `(A_0,B_0)=(z p,z^2 q)`, the layer maps are

| layer | source dimensions | target dimension | exact rank | free coordinates |
|---:|---:|---:|---:|---|
| `1` | `8+11=19` | `18` | `17` | `X,Y` |
| `2` | `9+12=21` | `19` | `18` | `U,V,W` |
| `3` | `0+13=13` | `19` | `12` | `D` |

The single layer-two compatibility functional vanishes identically.  The
parameters `U` and `D` are the free constant terms that realize the two
origin vertices; they disappear from all later compatibility equations.
The effective parameters are therefore

```text
X,Y,V,W,        weights 1,1,2,2.
```

Layer three gives seven weighted-degree-three equations.  Layer four gives
the eighteen coefficients of

```text
A_1 B_3' - A_2' B_2 = 0,
```

in degrees `z^2,...,z^19`; layer five vanishes identically because the two
coefficients in (4.2) are zero for `(i,j)=(2,3)`.

There are exactly fourteen monomials of weighted degree four:

```text
X^4,X^3Y,X^2Y^2,XY^3,Y^4,
X^2V,XYV,Y^2V,X^2W,XYW,Y^2W,
V^2,VW,W^2.
```

Multiply each layer-three equation by `X` and by `Y`, and adjoin the eighteen
layer-four equations.  The resulting `32 x 14` coefficient matrix has rank
`14` over the quintic field.  The verifier exhibits a selected `14 x 14`
minor with determinant

```text
894 mod 2053
```

at the unramified reduction `u=216`, corresponding to `s=1831`.  Because the
matrix was constructed exactly over the number field and every denominator
is a unit at this prime, the nonzero reduction proves that the same minor is
nonzero in characteristic zero.

Consequently the compatibility ideal contains every weighted-degree-four
monomial, so its radical contains `(X,Y,V,W)`.  The required top vertex
coefficients

```text
coefficient of A_2 z^8   &lt;-&gt;   P exponent (8,16),
coefficient of B_3 z^12  &lt;-&gt;   Q exponent (12,24)
```

have no constant term in these four variables and therefore vanish at every
geometric solution.  Exactness of the truncated Newton polygons requires
both to be nonzero.  This is a contradiction; the origin-vertex parameters
`U,D` remain unrestricted, so no complementary saturation branch has been
discarded.

&#91;`truncated_support_certificate.py`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/truncated_support_certificate.py)
reconstructs the whole calculation, and
&#91;`truncated_support_certificate.json`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/truncated_support_certificate.json)
records the ranks, free columns, selected minor, and vertex conclusion.

## 5. Constructible-locus and edge contract

Represent a node by

```text
X(I;S) = V(I) intersect intersection_(s in S) D(s),
```

where `I` is an ideal over a declared coefficient field and `S` is the list of
all inverted elements.  Required nonzero vertex coefficients belong in `S`,
not in prose.

A branch on a polynomial `h` must record the exhaustive identity

```text
X(I;S)
 = X(I+(h);S) union X(I;S union {h}).
```

On the open branch,

```text
V(I) intersect D(h) = V(I:h^infinity) intersect D(h),
```

but the closed branch `h=0` remains a child until it is independently
eliminated.

Every edge must declare whether it is a covering edge or a dependency
edge.  The main semantics are:

| edge type | role | required implication or data |
|---|---|---|
| `exhaustive_split` | covering | every parent point belongs to a listed child; all children must be empty to exclude the parent |
| `equivalence` | covering | inverse maps on the stated constructible loci |
| `rechart` | covering | same formal branch, transformed support/residue data, overlap theorem |
| `relaxation` | covering | parent maps into a larger child locus; child emptiness excludes parent |
| `localization` / `saturation` | covering | open branch plus an explicit complementary closed branch |
| `normalization` / `finite_cover` | covering | every relevant parent point lifts, or omitted image is separately routed |
| `quotient` | covering | lifting/descent and stabilizers are stated |
| `forced_specialization` | covering | equations or symmetry prove that every parent point reaches the fiber |
| `noncovering_specialization` | neither | useful test case only; cannot propagate terminal emptiness to the parent |
| `elimination` | covering | projection and extension/contraction statement, including all denominators |
| `terminal_certificate` | covering | exact identity, unit ideal, or proper compactification argument proving emptiness |
| `discard` | covering | an exact proof that the discarded constructible locus is empty |
| `forced_consequence` | dependency | derives an auxiliary invariant from an established locus |
| `classification` | dependency | classifies auxiliary objects but does not itself exclude the parent locus |
| `coefficient_reconstruction` | dependency | constructs the exact coefficient field/orbit used by later geometric edges |

The schema uses one geometric `from` node and a separate `requires` list.
This prevents an auxiliary fact such as the quintic reconstruction from being
mistaken for a second parent locus whose emptiness could be inferred from a
terminal certificate.

The machine-readable version is
&#91;`queue.schema.json`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/queue.schema.json),
and the current seed graph is
&#91;`queue.seed.json`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/queue.seed.json).

## 6. Current certified and uncertified edges

| stage | present conclusion | repair status |
|---|---|---|
| sub-125 candidate to degree `(72,108)` | Theorem 2.1 | external theorem statement audited |
| removal of `(9,27)` | Proposition 4.1 plus Corollary 5.7 | external theorem statement audited |
| `(8,28)` family to the two roots | Proposition 4.3 | external theorem statement audited; final monomial transform independently checked |
| either root to equation (3.1) | common lower face | independently proved and checked in this packet |
| equation (3.1) to degree-21 passport | derivative and ramification calculation | independently proved and checked in this packet |
| passport to five dessin classes | Hurwitz count, transitivity, trivial deck group | independently checked, with the group-theoretic argument stated above |
| five classes to one explicit quintic orbit | coefficient reconstruction and field identification | independently reconstructed; exact formulas and an isomorphism to the public `K0` model are exported in this packet |
| truncated root to its vertex-saturated empty system | exact layers `1`--`4`, fourteen-monomial span, and top-vertex contradiction | independently reconstructed and certified in this packet; the queue now propagates emptiness back to the truncated root |
| full root to fifteen normalized equations | layer recursion, square branch, normalization, elimination | stated exact in the Program 6 source; stage-by-stage replay and branch ledger still needed |
| six selected full-support equations to empty locus | compact toric certificate | exact for the displayed polynomials; independent large replay not performed here |
| stored `k=4` adjacent-chart system to empty locus | layer-five-through-seven certificate | exact for the stored system |
| full root to the stored `k=4` system | global coverage | not established; a specialization is not an exhaustive rechart |

Running

```text
python check_queue.py
```

validates the graph, confirms that the literature-root chain and common-face
chain are complete at their declared evidence levels, and deliberately reports
the global root-to-terminal coverage as incomplete.  The checker exits with a
failure under `--require-global`, so a release cannot silently convert the
open queue into a theorem.

## 7. Immediate theorem-facing work

The smallest useful next repairs are now sharply defined.

1. **Publish a stage manifest for the Program 6 archive.**  Every generated
   ideal, saturation element, normalization, branch condition, field model,
   and terminal input needs a node identifier and semantic digest.
2. **Close the full elimination edge.**  Starting with all `61+125`
   coefficient variables and the exact `Q(s)` face coefficients, reproduce
   every elimination and localization that leads to the fifteen equations.
   A denominator introduced during solving creates an explicit closed child;
   it is not silently discarded.
3. **Separate the two terminal architectures.**  The compact six-polynomial
   toric certificate and the later two-branch Nullstellensatz certificates are
   independent terminal proofs.  Each needs its own upstream provenance path.
4. **Use the `k=4` result only after a covering theorem.**  Either prove that
   the relevant branch necessarily crosses to that adjacent chart, or retain
   it as a noncovering stored specialization and continue the full branch by
   another route.

A discovered missing branch is a successful audit result: it becomes a new
queue node rather than being removed by a broader saturation.

## 8. Exact conclusion after this repair

The following statement is now independently checked from the two imported
root polygons:

&gt; Every normalized `(8,28)` root in Proposition 4.3 has the same forced
&gt; degree-21 face equation (3.1), and hence the same Belyi passport
&gt; `(2^10 1),(3^7),(17 1^4)`.  Its five classes are exactly the five
&gt; embeddings of the irreducible quintic (3.2), with the exact field
&gt; identification (3.3) to the Program 6 coefficient model.  Moreover, the
&gt; complete vertex-saturated truncated root is empty in characteristic zero.

The global statement remains:

&gt; The truncated root is now excluded independently.  The standalone
&gt; below-125 theorem is reduced to the full root: its layer elimination,
&gt; localization ledger, and attachment to one of the exact full-support
&gt; terminal certificates still require a covering proof.

The executable packet, captured outputs, and checksum manifest are under
&#91;`lane8-proof-queue-v1`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/README.md).
</code></pre>

## `lane8-proof-queue-20260802-v1/check_queue.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Validate the Lane 8 proof queue and its emptiness-propagation contract."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

PROOF_STATUSES = {
    "verified_in_packet",
    "audited_external_theorem",
    "verified_in_public_source",
    "source_replay_needed",
    "open",
}
EDGE_TYPES = {
    "external_import",
    "exhaustive_split",
    "forced_initial_form",
    "forced_consequence",
    "classification",
    "coefficient_reconstruction",
    "equivalence",
    "rechart",
    "relaxation",
    "localization",
    "saturation",
    "normalization",
    "finite_cover",
    "quotient",
    "forced_specialization",
    "noncovering_specialization",
    "elimination",
    "terminal_certificate",
    "discard",
}


def unique_ids(items: list&#91;dict&#91;str, Any&#93;&#93;, key: str, failures: list&#91;str&#93;) -&gt; set&#91;str&#93;:
    values = &#91;str(item.get(key, "")) for item in items&#93;
    missing = &#91;i for i, value in enumerate(values) if not value&#93;
    if missing:
        failures.append(f"{key}: missing at indices {missing}")
    duplicates = sorted({value for value in values if values.count(value) &gt; 1})
    if duplicates:
        failures.append(f"{key}: duplicate values {duplicates}")
    return set(values)


def topological_check(nodes: set&#91;str&#93;, edges: list&#91;dict&#91;str, Any&#93;&#93;, failures: list&#91;str&#93;) -&gt; None:
    adjacency: dict&#91;str, set&#91;str&#93;&#93; = defaultdict(set)
    indegree = {node: 0 for node in nodes}
    for edge in edges:
        parent = edge&#91;"from"&#93;
        for child in edge&#91;"to"&#93;:
            if child not in adjacency&#91;parent&#93;:
                adjacency&#91;parent&#93;.add(child)
                indegree&#91;child&#93; += 1
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for child in sorted(adjacency&#91;node&#93;):
            indegree&#91;child&#93; -= 1
            if indegree&#91;child&#93; == 0:
                queue.append(child)
    if visited != len(nodes):
        failures.append("routing graph contains a directed cycle")


def established_nodes(
    starts: set&#91;str&#93;, edges: list&#91;dict&#91;str, Any&#93;&#93;, accepted: set&#91;str&#93;
) -&gt; set&#91;str&#93;:
    established = set(starts)
    changed = True
    while changed:
        changed = False
        for edge in edges:
            if edge&#91;"proof_status"&#93; not in accepted:
                continue
            if edge&#91;"coverage"&#93; == "noncovering" or edge&#91;"edge_type"&#93; == "noncovering_specialization":
                continue
            if edge&#91;"from"&#93; not in established:
                continue
            if not set(edge.get("requires", &#91;&#93;)) &lt;= established:
                continue
            before = len(established)
            established.update(edge&#91;"to"&#93;)
            changed |= len(established) != before
    return established


def empty_nodes(
    assumptions: set&#91;str&#93;,
    node_map: dict&#91;str, dict&#91;str, Any&#93;&#93;,
    edges: list&#91;dict&#91;str, Any&#93;&#93;,
    accepted: set&#91;str&#93;,
) -&gt; tuple&#91;set&#91;str&#93;, set&#91;str&#93;, list&#91;str&#93;&#93;:
    """Return established nodes, proved-empty nodes, and an explanation trace."""
    established = established_nodes(assumptions, edges, accepted)
    empty = {
        node_id
        for node_id, node in node_map.items()
        if node.get("terminal")
        and node.get("proof_status") in accepted
        and node.get("certificate_refs")
    }
    trace = &#91;f"terminal certificate: {node_id}" for node_id in sorted(empty)&#93;

    changed = True
    while changed:
        changed = False
        for edge in edges:
            if edge&#91;"proof_status"&#93; not in accepted or not edge.get("propagates_emptiness"):
                continue
            if edge&#91;"coverage"&#93; in {"noncovering", "dependency"}:
                continue
            if edge&#91;"from"&#93; not in established:
                continue
            if not set(edge.get("requires", &#91;&#93;)) &lt;= established:
                continue
            # An exhaustive split excludes its parent only after every child
            # is empty. The same all-children rule is harmless for one-child
            # covers, relaxations, eliminations, and terminal certificates.
            if not set(edge&#91;"to"&#93;) &lt;= empty:
                continue
            parent = edge&#91;"from"&#93;
            if parent not in empty:
                empty.add(parent)
                trace.append(f"{edge&#91;'edge_id'&#93;}: all children empty =&gt; {parent} empty")
                changed = True
    return established, empty, trace


def target_result(
    target: dict&#91;str, Any&#93;, node_map: dict&#91;str, dict&#91;str, Any&#93;&#93;, edges: list&#91;dict&#91;str, Any&#93;&#93;
) -&gt; tuple&#91;bool, list&#91;str&#93;&#93;:
    accepted = set(target&#91;"accepted_proof_statuses"&#93;)
    details: list&#91;str&#93; = &#91;&#93;
    if target&#91;"kind"&#93; == "routing":
        passed = True
        for requirement in target&#91;"requirements"&#93;:
            start = requirement&#91;"from_node"&#93;
            reached = established_nodes({start}, edges, accepted)
            if "all_of" in requirement:
                missing = sorted(set(requirement&#91;"all_of"&#93;) - reached)
                ok = not missing
                details.append(f"from {start}: all_of missing={missing}")
            else:
                found = sorted(set(requirement&#91;"any_of"&#93;) &amp; reached)
                ok = bool(found)
                details.append(f"from {start}: any_of reached={found}")
            passed &amp;= ok
        return passed, details

    established, empty, trace = empty_nodes(
        set(target&#91;"assumption_nodes"&#93;), node_map, edges, accepted
    )
    missing = sorted(set(target&#91;"prove_empty"&#93;) - empty)
    details.append(f"established nodes: {len(established)}")
    details.append(f"proved-empty nodes: {sorted(empty)}")
    details.append(f"missing emptiness proofs: {missing}")
    details.extend(trace)
    return not missing, details


def validate(data: dict&#91;str, Any&#93;, require_global: bool) -&gt; int:
    failures: list&#91;str&#93; = &#91;&#93;
    if data.get("schema_version") != 1:
        failures.append("schema_version must be 1")

    node_ids = unique_ids(data.get("nodes", &#91;&#93;), "node_id", failures)
    edge_ids = unique_ids(data.get("edges", &#91;&#93;), "edge_id", failures)
    source_ids = unique_ids(data.get("sources", &#91;&#93;), "source_id", failures)
    obligation_ids = unique_ids(data.get("obligations", &#91;&#93;), "obligation_id", failures)
    target_ids = unique_ids(data.get("coverage_targets", &#91;&#93;), "target_id", failures)
    del source_ids, obligation_ids, target_ids

    node_pattern = re.compile(r"^L8-&#91;A-Z0-9-&#93;+$")
    edge_pattern = re.compile(r"^L8-E-&#91;A-Z0-9-&#93;+$")
    for node_id in node_ids:
        if not node_pattern.fullmatch(node_id):
            failures.append(f"invalid node id: {node_id}")
    for edge_id in edge_ids:
        if not edge_pattern.fullmatch(edge_id):
            failures.append(f"invalid edge id: {edge_id}")

    node_map = {node&#91;"node_id"&#93;: node for node in data.get("nodes", &#91;&#93;) if node.get("node_id")}
    edge_map = {edge&#91;"edge_id"&#93;: edge for edge in data.get("edges", &#91;&#93;) if edge.get("edge_id")}

    for node_id, node in node_map.items():
        if node.get("proof_status") not in PROOF_STATUSES:
            failures.append(f"{node_id}: invalid proof status")
        if node.get("terminal") and not node.get("certificate_refs"):
            failures.append(f"{node_id}: terminal node lacks certificate_refs")
        if not isinstance(node.get("constructible_data", {}).get("inverted_elements"), list):
            failures.append(f"{node_id}: inverted_elements must be an explicit list")

    for edge_id, edge in edge_map.items():
        if edge.get("from") not in node_ids:
            failures.append(f"{edge_id}: unknown parent {edge.get('from')}")
        for key in ("to", "requires"):
            for node_id in edge.get(key, &#91;&#93;):
                if node_id not in node_ids:
                    failures.append(f"{edge_id}: unknown {key} node {node_id}")
        if edge.get("edge_type") not in EDGE_TYPES:
            failures.append(f"{edge_id}: invalid edge type {edge.get('edge_type')}")
        if edge.get("proof_status") not in PROOF_STATUSES:
            failures.append(f"{edge_id}: invalid proof status")
        if edge.get("edge_type") == "noncovering_specialization":
            if edge.get("coverage") != "noncovering" or edge.get("propagates_emptiness"):
                failures.append(f"{edge_id}: noncovering specialization has unsafe semantics")
        if edge.get("coverage") == "dependency" and edge.get("propagates_emptiness"):
            failures.append(f"{edge_id}: dependency edge cannot propagate emptiness")
        if edge.get("edge_type") == "terminal_certificate":
            if edge.get("coverage") != "terminal" or not edge.get("propagates_emptiness"):
                failures.append(f"{edge_id}: terminal certificate semantics are malformed")
            for child in edge.get("to", &#91;&#93;):
                if child in node_map and not node_map&#91;child&#93;.get("terminal"):
                    failures.append(f"{edge_id}: terminal certificate points to nonterminal {child}")
        if edge.get("edge_type") in {"localization", "saturation"}:
            complements = edge.get("complement_edges", &#91;&#93;)
            if not complements:
                failures.append(f"{edge_id}: localization/saturation lacks complementary branch")
            for complement in complements:
                if complement not in edge_ids:
                    failures.append(f"{edge_id}: unknown complement edge {complement}")
                elif edge_map&#91;complement&#93;.get("from") != edge.get("from"):
                    failures.append(f"{edge_id}: complement {complement} has a different parent")

    for obligation in data.get("obligations", &#91;&#93;):
        for edge_id in obligation.get("blocks", &#91;&#93;):
            if edge_id not in edge_ids:
                failures.append(f"{obligation&#91;'obligation_id'&#93;}: blocks unknown edge {edge_id}")

    for target in data.get("coverage_targets", &#91;&#93;):
        for status in target.get("accepted_proof_statuses", &#91;&#93;):
            if status not in PROOF_STATUSES:
                failures.append(f"{target&#91;'target_id'&#93;}: invalid accepted proof status {status}")
        references: set&#91;str&#93; = set()
        if target.get("kind") == "routing":
            for req in target.get("requirements", &#91;&#93;):
                references.add(req.get("from_node", ""))
                references.update(req.get("all_of", &#91;&#93;))
                references.update(req.get("any_of", &#91;&#93;))
        elif target.get("kind") == "exclusion":
            references.update(target.get("assumption_nodes", &#91;&#93;))
            references.update(target.get("prove_empty", &#91;&#93;))
        else:
            failures.append(f"{target&#91;'target_id'&#93;}: invalid target kind")
        for node_id in references:
            if node_id not in node_ids:
                failures.append(f"{target&#91;'target_id'&#93;}: unknown node {node_id}")

    topological_check(node_ids, data.get("edges", &#91;&#93;), failures)

    if failures:
        print("STRUCTURAL FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 2

    print(
        f"STRUCTURAL PASS: {len(node_ids)} nodes, {len(edge_ids)} edges, "
        f"{len(data.get('obligations', &#91;&#93;))} obligations"
    )

    expectation_failures: list&#91;str&#93; = &#91;&#93;
    global_incomplete = False
    for target in data&#91;"coverage_targets"&#93;:
        actual, details = target_result(target, node_map, data&#91;"edges"&#93;)
        actual_label = "complete" if actual else "incomplete"
        expected = target&#91;"expected"&#93;
        print(f"{target&#91;'target_id'&#93;}: {actual_label} (expected {expected})")
        for detail in details:
            print(f"  {detail}")
        if actual_label != expected:
            expectation_failures.append(
                f"{target&#91;'target_id'&#93;}: expected {expected}, got {actual_label}"
            )
        if target&#91;"target_id"&#93; == "L8-COVERAGE-SUB125-EXCLUSION" and not actual:
            global_incomplete = True

    if expectation_failures:
        print("EXPECTATION FAIL")
        for failure in expectation_failures:
            print(f"- {failure}")
        return 3
    if require_global and global_incomplete:
        print("GLOBAL FAIL: the standalone below-125 exclusion is not certified")
        return 1

    print("PASS: declared complete targets are complete and declared gaps remain visible")
    return 0


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("queue", nargs="?", default="queue.seed.json")
    parser.add_argument(
        "--require-global",
        action="store_true",
        help="fail unless the standalone below-125 exclusion target is complete",
    )
    args = parser.parse_args()
    path = Path(args.queue)
    data = json.loads(path.read_text(encoding="utf-8"))
    return validate(data, require_global=args.require_global)


if __name__ == "__main__":
    sys.exit(main())
</code></pre>

## `lane8-proof-queue-20260802-v1/full_early_layer_reduction.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact early-layer reduction for the full (8,28) Newton root.

The calculation reconstructs layers 1 through 4 over the quintic field.  The
first three compatibility functionals vanish identically.  The sole layer-4
condition is an exact square a*(W-kappa*Y^2)^2.  Thus the reduced geometric
branch is forced to W=kappa*Y^2, while the scheme-level double structure must
be retained in any elimination proof.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import quintic_face_reconstruction as face
import truncated_support_certificate as exact

# Nine early free coordinates:
# layer 1: X,Y; layer 2: U,V,W; layer 3: R,S,T; layer 4: H.
exact.N = 9


def reconstruct_base():
    K, ONE, ZERO = exact.K, exact.ONE, exact.ZERO
    a = {i: K.from_expr(v) for i, v in face.A_RAW.items()}
    reverse_p = &#91;ONE&#93; + &#91;a&#91;i&#93; for i in range(1, 8)&#93;
    cube = &#91;&#93;
    for total in range(21):
        value = ZERO
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if i + j + k == total:
                        value = value + reverse_p&#91;i&#93; * reverse_p&#91;j&#93; * reverse_p&#91;k&#93;
        cube.append(value)
    reverse_q = &#91;ONE&#93;
    for total in range(1, 11):
        known = ZERO
        for i in range(1, total):
            known = known + reverse_q&#91;i&#93; * reverse_q&#91;total - i&#93;
        reverse_q.append((cube&#91;total&#93; - known) / K(2))
    inverse_constant = (a&#91;7&#93; * reverse_q&#91;10&#93;).inv()
    p = {7: ONE}
    p.update({7 - i: a&#91;i&#93; for i in range(1, 8)})
    q = {10: inverse_constant}
    q.update({10 - i: reverse_q&#91;i&#93; * inverse_constant for i in range(1, 11)})
    return (
        exact.z_from_field({degree + 1: value for degree, value in p.items()}),
        exact.z_from_field({degree + 2: value for degree, value in q.items()}),
    )


def a_exponents(layer):
    if layer == 1:
        return list(range(1, 9))
    if layer == 2:
        return list(range(0, 9))
    if 3 &lt;= layer &lt;= 10:
        return list(range(0, 11 - layer))
    return &#91;&#93;


def b_exponents(layer):
    if layer == 1:
        return list(range(2, 13))
    if layer == 2:
        return list(range(1, 13))
    if layer == 3:
        return list(range(0, 13))
    if 4 &lt;= layer &lt;= 15:
        return list(range(0, 16 - layer))
    return &#91;&#93;


def forcing(layer, A, B):
    pieces = &#91;&#93;
    for i in range(1, layer):
        j = layer - i
        if i &gt;= len(A) or j &gt;= len(B) or not A&#91;i&#93; or not B&#91;j&#93;:
            continue
        pieces.append(
            exact.zscale(exact.zmul(A&#91;i&#93;, exact.zder(B&#91;j&#93;)), 2 - i)
        )
        pieces.append(
            exact.zscale(exact.zmul(exact.zder(A&#91;i&#93;), B&#91;j&#93;), j - 3)
        )
    return exact.zadd(*pieces)


def build_reduction():
    A0, B0 = reconstruct_base()
    X, Y, U, V, W, R, S, T, H = &#91;exact.pp_var(i) for i in range(9)&#93;
    A = &#91;A0&#93;
    B = &#91;B0&#93;
    compatibilities = {}

    free_parameters = {
        1: &#91;X, Y&#93;,
        2: &#91;U, V, W&#93;,
        3: &#91;R, S, T&#93;,
        4: &#91;H&#93;,
    }
    expected = {
        1: (17, &#91;17, 18&#93;),
        2: (18, &#91;0, 19, 20&#93;),
        3: (18, &#91;8, 18, 19&#93;),
        4: (18, &#91;17&#93;),
    }

    for layer in range(1, 5):
        data = exact.linear_data(
            layer, a_exponents(layer), b_exponents(layer), A0, B0
        )
        assert (len(data&#91;4&#93;), data&#91;5&#93;) == expected&#91;layer&#93;
        rhs = {} if layer == 1 else exact.zscale(forcing(layer, A, B), -1)
        solution, compatibility = exact.solve(
            data, rhs, free_parameters&#91;layer&#93;
        )
        Ar, Br = exact.vecpair(
            solution, a_exponents(layer), b_exponents(layer)
        )
        A.append(Ar)
        B.append(Br)
        compatibilities&#91;layer&#93; = compatibility

    assert all(not equation for layer in (1, 2, 3)
               for equation in compatibilities&#91;layer&#93;)
    assert len(compatibilities&#91;4&#93;) == 1
    equation = compatibilities&#91;4&#93;&#91;0&#93;
    expected_support = {
        (0, 0, 0, 0, 2, 0, 0, 0, 0),  # W^2
        (0, 2, 0, 0, 1, 0, 0, 0, 0),  # Y^2 W
        (0, 4, 0, 0, 0, 0, 0, 0, 0),  # Y^4
    }
    assert set(equation) == expected_support
    a = equation&#91;(0, 0, 0, 0, 2, 0, 0, 0, 0)&#93;
    b = equation&#91;(0, 2, 0, 0, 1, 0, 0, 0, 0)&#93;
    c = equation&#91;(0, 4, 0, 0, 0, 0, 0, 0, 0)&#93;
    assert not (b * b - exact.K(4) * a * c)
    kappa = -b / (exact.K(2) * a)
    assert not (c - a * kappa * kappa)

    return {
        "schema_version": 1,
        "field_polynomial": str(face.M_EXPR),
        "early_free_parameters": {
            "layer_1": &#91;"X", "Y"&#93;,
            "layer_2": &#91;"U", "V", "W"&#93;,
            "layer_3": &#91;"R", "S", "T"&#93;,
            "layer_4": &#91;"H"&#93;,
        },
        "ranks": {
            "D1": 17,
            "D2": 18,
            "D3": 18,
            "D4": 18,
        },
        "compatibility": {
            "layers_1_to_3_identically_zero": True,
            "layer_4_support": &#91;"W^2", "Y^2*W", "Y^4"&#93;,
            "leading_coefficient": str(a.expr()),
            "kappa": str(kappa.expr()),
            "exact_factorization": "a*(W-kappa*Y^2)^2",
        },
        "conclusion": {
            "reduced_geometric_branch": "W=kappa*Y^2",
            "scheme_structure": "double square; do not replace by the reduced branch in scheme-level arguments",
            "all_later_free_parameters": "none after layer 4; see full_layer_rank_profile.json",
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_reduction()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("exact early ranks: D1=17, D2=18, D3=18, D4=18")
    print("compatibility at layers 1,2,3: identically zero")
    print("layer-4 compatibility: a*(W-kappa*Y^2)^2")
    print("reduced geometric branch: W=kappa*Y^2")
    if args.output:
        print(f"reduction export: {args.output.name}")
    print("PASS: the full-support square branch is independently reconstructed")


if __name__ == "__main__":
    main()
</code></pre>

## `lane8-proof-queue-20260802-v1/quintic_face_reconstruction.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact reconstruction of the five normalized degree-21 face covers.

This script is independent of the large Program 6 certificate archive.  It
works in the explicitly reconstructed quintic field Q(s), builds normalized
polynomials p and q, checks the order-17 Belyi contact, normalizes the face
Jacobian equation to 1, and verifies an exact isomorphism with the quintic
field model used by the public Program 6 source.

The normalization is

    p(z) = z^7 + z^6 + s z^5 + ...,
    q_monic(z) = z^10 + (3/2) z^9 + ... .

The unique simple point over 0 and the unique index-17 point over the third
branch value fix 0 and infinity on the source.  The remaining source scaling
is killed by the coefficient of z^6 in p being 1.  Thus the five embeddings
of the irreducible quintic give five distinct normalized covers.  Combined
with the independent Hurwitz count of five, they exhaust the dessin classes
and form one Galois orbit.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import sympy as sp

s, z, u = sp.symbols("s z u")

# Positive-leading defining polynomial of the reconstructed coefficient field.
M_EXPR = (
    287548593020928 * s**5
    - 688401965085696 * s**4
    + 640652914818432 * s**3
    - 292066554895024 * s**2
    + 65563255857792 * s
    - 5817852446211
)
M = sp.Poly(M_EXPR, s, domain=sp.QQ)

# Public Program 6 field model.
K0_EXPR = u**5 - u**4 + 3 * u**3 + 3 * u**2 + 26
K0 = sp.Poly(K0_EXPR, u, domain=sp.QQ)

# Exact embedding of the reconstructed primitive element into K0.
S_IN_K0 = (
    20481190
    - 2578004 * u
    + 1664322 * u**2
    - 709604 * u**3
    + 221083 * u**4
) / sp.Integer(42799752)

# Coefficients a_i of p(z)=z^7+a_1 z^6+...+a_7.
A_RAW: dict&#91;int, sp.Expr&#93; = {
    1: sp.Integer(1),
    2: s,
    3: (
        3771978574908902400 * s**4
        - 7556165936778735360 * s**3
        + 5450946367591254384 * s**2
        - 1699030592727011128 * s
        + 194711288931974931
    )
    / sp.Integer(2789916527204736),
    4: 7
    * (
        1472867824488238080 * s**4
        - 2950502889599315712 * s**3
        + 2129064709044490224 * s**2
        - 664388468462807608 * s
        + 76242600010205835
    )
    / sp.Integer(11159666108818944),
    5: 7
    * (
        1898608366334131200 * s**4
        - 3803361970401319680 * s**3
        + 2745126606514279984 * s**2
        - 857130636468363480 * s
        + 98443252126745919
    )
    / sp.Integer(66957996652913664),
    6: (
        5513086784810050560 * s**4
        - 11023906566235965696 * s**3
        + 7949047218967327952 * s**2
        - 2481117197487437928 * s
        + 284986511308009521
    )
    / sp.Integer(401747979917481984),
    7: (
        2473699609838592 * s**4
        - 4880250718447104 * s**3
        + 3484831588909616 * s**2
        - 1079655594514872 * s
        + 123291106405875
    )
    / sp.Integer(15858472891479552),
}


def reduce_field(expr: sp.Expr) -&gt; sp.Expr:
    """Reduce a rational function in s to the degree-&lt;5 basis of Q(s)."""
    expr = sp.cancel(expr)
    numerator, denominator = sp.fraction(expr)
    denominator_poly = sp.Poly(denominator, s, domain=sp.QQ)
    try:
        inverse = sp.invert(denominator_poly, M).as_expr()
    except sp.polys.polyerrors.NotInvertible as exc:
        raise ValueError(f"denominator is zero in Q(s): {denominator}") from exc
    reduced = sp.rem(
        sp.Poly(sp.expand(numerator * inverse), s, domain=sp.QQ), M
    ).as_expr()
    return sp.cancel(reduced)


def reduce_z_coefficients(expr: sp.Expr) -&gt; sp.Poly:
    """Reduce every z coefficient of expr in the field Q(s)."""
    polynomial = sp.Poly(sp.expand(expr), z)
    result = sp.Integer(0)
    for (power,), coefficient in polynomial.terms():
        result += reduce_field(coefficient) * z**power
    return sp.Poly(sp.expand(result), z)


def coefficient_list_descending(poly: sp.Poly, degree: int) -&gt; list&#91;sp.Expr&#93;:
    return &#91;reduce_field(poly.coeff_monomial(z**power)) for power in range(degree, -1, -1)&#93;


def expression_strings(values: Iterable&#91;sp.Expr&#93;) -&gt; list&#91;str&#93;:
    return &#91;sp.sstr(sp.factor(value)) for value in values&#93;


def reconstruct() -&gt; dict&#91;str, object&#93;:
    assert M.degree() == 5 and M.is_irreducible
    assert K0.degree() == 5 and K0.is_irreducible

    a = {index: reduce_field(value) for index, value in A_RAW.items()}
    p = sp.Poly(z**7 + sum(a&#91;i&#93; * z ** (7 - i) for i in range(1, 8)), z)

    # Reverse-polynomial contact condition.  If
    # P(T)=1+a_1 T+...+a_7 T^7 and Q(T)=1+b_1 T+...+b_10 T^10,
    # solve Q(T)^2=P(T)^3 successively through degree 10.
    p_reverse = &#91;sp.Integer(1)&#93; + &#91;a&#91;i&#93; for i in range(1, 8)&#93;
    p_cube: list&#91;sp.Expr&#93; = &#91;&#93;
    for total in range(21):
        coefficient = sum(
            p_reverse&#91;i&#93; * p_reverse&#91;j&#93; * p_reverse&#91;k&#93;
            for i in range(8)
            for j in range(8)
            for k in range(8)
            if i + j + k == total
        )
        p_cube.append(reduce_field(coefficient))

    q_reverse = &#91;sp.Integer(1)&#93;
    for total in range(1, 11):
        known = sum(q_reverse&#91;i&#93; * q_reverse&#91;total - i&#93; for i in range(1, total))
        q_reverse.append(reduce_field((p_cube&#91;total&#93; - known) / 2))

    # The remaining contact equations, degrees 11 through 16, produce M(s).
    contact_residuals: dict&#91;int, sp.Expr&#93; = {}
    for total in range(11, 17):
        q_square = sum(
            q_reverse&#91;i&#93; * q_reverse&#91;total - i&#93;
            for i in range(max(0, total - 10), min(10, total) + 1)
        )
        contact_residuals&#91;total&#93; = reduce_field(q_square - p_cube&#91;total&#93;)
    assert all(value == 0 for value in contact_residuals.values())

    q_monic = sp.Poly(
        z**10 + sum(q_reverse&#91;i&#93; * z ** (10 - i) for i in range(1, 11)), z
    )

    # In z coordinates, order-17 contact at infinity means z*q^2-p^3 has
    # degree at most 4.
    belyi_residual = reduce_z_coefficients(z * q_monic.as_expr() ** 2 - p.as_expr() ** 3)
    nonzero_residual_degrees = sorted(
        power&#91;0&#93;
        for power, coefficient in belyi_residual.terms()
        if reduce_field(coefficient) != 0
    )
    assert nonzero_residual_degrees == &#91;0, 1, 2, 3, 4&#93;

    face_expression = reduce_z_coefficients(
        p.as_expr() * q_monic.as_expr()
        + 2 * z * p.as_expr() * sp.diff(q_monic.as_expr(), z)
        - 3 * z * sp.diff(p.as_expr(), z) * q_monic.as_expr()
    )
    nonzero_face_terms = &#91;
        (power&#91;0&#93;, reduce_field(coefficient))
        for power, coefficient in face_expression.terms()
        if reduce_field(coefficient) != 0
    &#93;
    assert len(nonzero_face_terms) == 1 and nonzero_face_terms&#91;0&#93;&#91;0&#93; == 0
    face_constant = nonzero_face_terms&#91;0&#93;&#91;1&#93;
    assert face_constant != 0
    assert reduce_field(p.nth(0) * q_monic.nth(0) - face_constant) == 0

    # Normalize q so the Jacobian face equation has right side 1.
    q_face_expr = sp.expand(q_monic.as_expr() / face_constant)
    normalized_face = reduce_z_coefficients(
        p.as_expr() * q_face_expr
        + 2 * z * p.as_expr() * sp.diff(q_face_expr, z)
        - 3 * z * sp.diff(p.as_expr(), z) * q_face_expr
    )
    assert normalized_face.as_expr() == 1
    assert reduce_field(p.nth(0) * q_monic.nth(0) / face_constant) == 1

    # Verify exact compatibility with the public K0 field model.
    map_numerator, _ = sp.fraction(sp.cancel(M_EXPR.subs(s, S_IN_K0)))
    map_remainder = sp.rem(sp.Poly(map_numerator, u, domain=sp.QQ), K0).as_expr()
    assert map_remainder == 0
    # Since both defining polynomials are irreducible of degree five and the
    # image is visibly nonconstant, this homomorphism is an isomorphism.
    assert sp.Poly(sp.together(S_IN_K0).as_numer_denom()&#91;0&#93;, u).degree() &gt; 0

    p_coefficients = coefficient_list_descending(p, 7)
    q_coefficients = coefficient_list_descending(q_monic, 10)

    return {
        "schema_version": 1,
        "normalization": {
            "p": "monic degree 7 with coefficient of z^6 equal to 1",
            "q_monic": "monic degree 10",
            "q_face": "q_monic / face_constant, so pq+2zpq'-3zp'q=1",
            "source_scaling": "fixed by the coefficient of z^6 in p",
        },
        "reconstructed_field": {
            "generator": "s",
            "defining_polynomial": sp.sstr(M_EXPR),
            "degree": 5,
            "irreducible_over_Q": True,
        },
        "public_program6_field": {
            "generator": "u",
            "defining_polynomial": sp.sstr(K0_EXPR),
            "degree": 5,
            "irreducible_over_Q": True,
            "field_isomorphism_s_in_terms_of_u": sp.sstr(S_IN_K0),
        },
        "p_coefficients_descending": expression_strings(p_coefficients),
        "q_monic_coefficients_descending": expression_strings(q_coefficients),
        "face_constant": sp.sstr(sp.factor(face_constant)),
        "q_face_relation": "q_face = q_monic / face_constant",
        "checks": {
            "reverse_contact_zero_degrees": sorted(contact_residuals),
            "z_q_squared_minus_p_cubed_nonzero_degrees": nonzero_residual_degrees,
            "face_equation_after_scaling": "1",
            "p0_times_q_face0": "1",
            "five_distinct_normalized_embeddings": True,
            "one_galois_orbit": True,
        },
    }


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        help="write the exact reconstructed coefficients and field map as JSON",
    )
    args = parser.parse_args()

    result = reconstruct()
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

    print("reconstructed field degree: 5")
    print("reconstructed field irreducible over Q: yes")
    print("order-17 contact equations: exact")
    print("z*q_monic^2-p^3 nonzero degrees: 0,1,2,3,4")
    print("normalized face equation: p*q+2z*p*q'-3z*p'*q = 1")
    print("exact field isomorphism to Program 6 K0: verified")
    print("five embeddings: five distinct normalized covers in one Galois orbit")
    if args.output is not None:
        print(f"coefficient export: {args.output.name}")
    print("PASS: exact quintic degree-21 face reconstruction succeeded")


if __name__ == "__main__":
    main()
</code></pre>

## `lane8-proof-queue-20260802-v1/truncated_support_certificate.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact independent certificate for the truncated (8,28) Newton root.

The script reconstructs the quintic degree-21 face, solves the complete
truncated normal-layer system over the exact number field, and proves that
the required top P and Q vertex coefficients vanish on every solution.

No Program 6 terminal archive is read.
"""
from __future__ import annotations
from fractions import Fraction
import argparse
import json
from pathlib import Path
import sympy as sp
import quintic_face_reconstruction as qr

class K:
    __slots__=('c',)
    def __init__(self,c=(0,0,0,0,0)):
        if isinstance(c,K): self.c=c.c
        elif isinstance(c,(int,Fraction)): self.c=(Fraction(c),Fraction(0),Fraction(0),Fraction(0),Fraction(0))
        else:
            cc=tuple(Fraction(x) for x in c); self.c=cc+(Fraction(0),)*(5-len(cc))
    @staticmethod
    def from_expr(e):
        e=qr.reduce_field(e); p=sp.Poly(e,qr.s,domain=sp.QQ)
        return K(tuple(Fraction(int(p.nth(i).p),int(p.nth(i).q)) for i in range(5)))
    def expr(self): return sum(sp.Rational(x.numerator,x.denominator)*qr.s**i for i,x in enumerate(self.c))
    def __add__(self,o):
        o=K(o); return K(tuple(a+b for a,b in zip(self.c,o.c)))
    __radd__=__add__
    def __neg__(self):return K(tuple(-a for a in self.c))
    def __sub__(self,o):return self+(-K(o))
    def __rsub__(self,o):return K(o)-self
    def __mul__(self,o):
        o=K(o); conv=&#91;Fraction(0)&#93;*9
        for i,a in enumerate(self.c):
            for j,b in enumerate(o.c):conv&#91;i+j&#93;+=a*b
        # relation L s5 = 688...s4 -640...s3 +292...s2 -655...s +5817...
        L=287548593020928
        rel=&#91;Fraction(5817852446211,L),Fraction(-65563255857792,L),Fraction(292066554895024,L),Fraction(-640652914818432,L),Fraction(688401965085696,L)&#93;
        for d in range(8,4,-1):
            x=conv&#91;d&#93;
            if x:
                conv&#91;d&#93;=0
                for i,r in enumerate(rel):conv&#91;d-5+i&#93;+=x*r
        return K(tuple(conv&#91;:5&#93;))
    __rmul__=__mul__
    def inv(self):
        if not self:raise ZeroDivisionError
        e=sp.invert(sp.Poly(self.expr(),qr.s,domain=sp.QQ),qr.M).as_expr()
        return K.from_expr(e)
    def __truediv__(self,o):return self*K(o).inv()
    def __bool__(self):return any(self.c)
    def __eq__(self,o):return self.c==K(o).c
    def mod(self,p,s0):
        ans=0
        for i,x in enumerate(self.c):ans=(ans+(x.numerator%p)*pow(x.denominator%p,-1,p)*pow(s0,i,p))%p
        return ans
    def __repr__(self):return str(self.expr())
ZERO=K();ONE=K(1)

# parameter polynomial six vars exponents tuple
N=6
def pp_const(c):
 c=K(c);return {} if not c else {(0,)*N:c}
def pp_var(i):
 e=&#91;0&#93;*N;e&#91;i&#93;=1;return {tuple(e):ONE}
def pp_add(*aa):
 out={}
 for a in aa:
  for m,c in a.items():
   v=out.get(m,ZERO)+c
   if v:out&#91;m&#93;=v
   elif m in out:del out&#91;m&#93;
 return out
def pp_neg(a):return {m:-c for m,c in a.items()}
def pp_sub(a,b):return pp_add(a,pp_neg(b))
def pp_scale(a,c):
 c=K(c);return {m:c*v for m,v in a.items() if c*v}
def pp_mul(a,b):
 out={}
 for m,c in a.items():
  for n,d in b.items():
   k=tuple(x+y for x,y in zip(m,n));v=out.get(k,ZERO)+c*d
   if v:out&#91;k&#93;=v
   elif k in out:del out&#91;k&#93;
 return out

def zadd(*aa):
 out={}
 for a in aa:
  for k,v in a.items():
   w=pp_add(out.get(k,{}),v)
   if w:out&#91;k&#93;=w
   elif k in out:del out&#91;k&#93;
 return out
def zscale(a,c):return {k:pp_scale(v,c) for k,v in a.items() if pp_scale(v,c)}
def zder(a):return {k-1:pp_scale(v,k) for k,v in a.items() if k and pp_scale(v,k)}
def zmul(a,b):
 out={}
 for i,x in a.items():
  for j,y in b.items():
   out&#91;i+j&#93;=pp_add(out.get(i+j,{}),pp_mul(x,y))
 return {k:v for k,v in out.items() if v}

def z_from_field(d):return {k:pp_const(v) for k,v in d.items() if v}

def rref_transform(mat):
 m=len(mat);n=len(mat&#91;0&#93;);R=&#91;&#91;K(x) for x in row&#93; for row in mat&#93;;T=&#91;&#91;ONE if i==j else ZERO for j in range(m)&#93; for i in range(m)&#93;
 piv=&#91;&#93;;row=0
 for col in range(n):
  pr=next((r for r in range(row,m) if R&#91;r&#93;&#91;col&#93;),None)
  if pr is None:continue
  R&#91;row&#93;,R&#91;pr&#93;=R&#91;pr&#93;,R&#91;row&#93;;T&#91;row&#93;,T&#91;pr&#93;=T&#91;pr&#93;,T&#91;row&#93;
  inv=R&#91;row&#93;&#91;col&#93;.inv();R&#91;row&#93;=&#91;x*inv for x in R&#91;row&#93;&#93;;T&#91;row&#93;=&#91;x*inv for x in T&#91;row&#93;&#93;
  for r in range(m):
   if r!=row and R&#91;r&#93;&#91;col&#93;:
    c=R&#91;r&#93;&#91;col&#93;;R&#91;r&#93;=&#91;R&#91;r&#93;&#91;j&#93;-c*R&#91;row&#93;&#91;j&#93; for j in range(n)&#93;;T&#91;r&#93;=&#91;T&#91;r&#93;&#91;j&#93;-c*T&#91;row&#93;&#91;j&#93; for j in range(m)&#93;
  piv.append(col);row+=1
  if row==m:break
 return R,T,piv

def Dmap(r,A,B,A0,B0):
 return zadd(zscale(zmul(A,zder(B0)),2-r),zscale(zmul(zder(A),B0),-3),zscale(zmul(A0,zder(B)),2),zscale(zmul(zder(A0),B),r-3))
def linear_data(r,ae,be,A0,B0):
 cols=&#91;&#93;
 for e in ae:cols.append(Dmap(r,{e:pp_const(1)},{},A0,B0))
 for e in be:cols.append(Dmap(r,{}, {e:pp_const(1)},A0,B0))
 ds=sorted(set().union(*(x.keys() for x in cols)));degrees=list(range(min(ds),max(ds)+1))
 M=&#91;&#93;
 for d in degrees:
  row=&#91;&#93;
  for col in cols:
   pp=col.get(d,{})
   row.append(pp.get((0,)*N,ZERO))
  M.append(row)
 R,T,piv=rref_transform(M);free=&#91;j for j in range(len(M&#91;0&#93;)) if j not in piv&#93;
 ns=&#91;&#93;
 for f in free:
  v=&#91;ZERO&#93;*len(M&#91;0&#93;);v&#91;f&#93;=ONE
  for i,pc in enumerate(piv):v&#91;pc&#93;=-R&#91;i&#93;&#91;f&#93;
  ns.append(v)
 return degrees,M,R,T,piv,free,ns

def solve(data,rhs,freepps):
 degrees,M,R,T,piv,free,ns=data
 rv=&#91;rhs.get(d,{}) for d in degrees&#93;
 tr=&#91;&#93;
 for i in range(len(degrees)):
  tr.append(pp_add(*(pp_scale(rv&#91;j&#93;,T&#91;i&#93;&#91;j&#93;) for j in range(len(degrees)))))
 compat=tr&#91;len(piv):&#93;
 sol=&#91;{} for _ in range(len(M&#91;0&#93;))&#93;
 for i,pc in enumerate(piv):sol&#91;pc&#93;=tr&#91;i&#93;
 for par,v in zip(freepps,ns):
  for j,c in enumerate(v):
   if c:sol&#91;j&#93;=pp_add(sol&#91;j&#93;,pp_scale(par,c))
 return sol,compat

def vecpair(vec,ae,be):
 return ({e:vec&#91;i&#93; for i,e in enumerate(ae) if vec&#91;i&#93;},{e:vec&#91;len(ae)+j&#93; for j,e in enumerate(be) if vec&#91;len(ae)+j&#93;})


def rank_mod(rows, prime):
 if not rows:return 0
 a=&#91;&#91;x%prime for x in row&#93; for row in rows&#93;;m=len(a);n=len(a&#91;0&#93;);rank=0
 for col in range(n):
  pivot=next((r for r in range(rank,m) if a&#91;r&#93;&#91;col&#93;),None)
  if pivot is None:continue
  a&#91;rank&#93;,a&#91;pivot&#93;=a&#91;pivot&#93;,a&#91;rank&#93;
  inv=pow(a&#91;rank&#93;&#91;col&#93;,-1,prime)
  a&#91;rank&#93;=&#91;(x*inv)%prime for x in a&#91;rank&#93;&#93;
  for r in range(m):
   if r!=rank and a&#91;r&#93;&#91;col&#93;:
    c=a&#91;r&#93;&#91;col&#93;
    a&#91;r&#93;=&#91;(a&#91;r&#93;&#91;j&#93;-c*a&#91;rank&#93;&#91;j&#93;)%prime for j in range(n)&#93;
  rank+=1
  if rank==m:break
 return rank

def determinant_mod(matrix, prime):
 a=&#91;&#91;x%prime for x in row&#93; for row in matrix&#93;;n=len(a);det=1
 assert all(len(row)==n for row in a)
 for col in range(n):
  pivot=next((r for r in range(col,n) if a&#91;r&#93;&#91;col&#93;),None)
  if pivot is None:return 0
  if pivot!=col:
   a&#91;col&#93;,a&#91;pivot&#93;=a&#91;pivot&#93;,a&#91;col&#93;;det=-det
  pv=a&#91;col&#93;&#91;col&#93;%prime;det=det*pv%prime;inv=pow(pv,-1,prime)
  for r in range(col+1,n):
   c=a&#91;r&#93;&#91;col&#93;*inv%prime
   a&#91;r&#93;=&#91;(a&#91;r&#93;&#91;j&#93;-c*a&#91;col&#93;&#91;j&#93;)%prime for j in range(n)&#93;
 return det%prime

def build_certificate():
 # Exact lower face in Q(s).
 a={i:K.from_expr(v) for i,v in qr.A_RAW.items()}
 reverse_p=&#91;ONE&#93;+&#91;a&#91;i&#93; for i in range(1,8)&#93;
 cube=&#91;&#93;
 for total in range(21):
  c=ZERO
  for i in range(8):
   for j in range(8):
    for k in range(8):
     if i+j+k==total:c=c+reverse_p&#91;i&#93;*reverse_p&#91;j&#93;*reverse_p&#91;k&#93;
  cube.append(c)
 reverse_q=&#91;ONE&#93;
 for total in range(1,11):
  known=ZERO
  for i in range(1,total):known=known+reverse_q&#91;i&#93;*reverse_q&#91;total-i&#93;
  reverse_q.append((cube&#91;total&#93;-known)/K(2))
 face_constant=a&#91;7&#93;*reverse_q&#91;10&#93;;inverse_constant=face_constant.inv()
 pcoef={7:ONE};pcoef.update({7-i:a&#91;i&#93; for i in range(1,8)})
 qcoef={10:inverse_constant};qcoef.update({10-i:reverse_q&#91;i&#93;*inverse_constant for i in range(1,11)})
 A0=z_from_field({k+1:v for k,v in pcoef.items()})
 B0=z_from_field({k+2:v for k,v in qcoef.items()})

 X,Y,U,V,W,D=&#91;pp_var(i) for i in range(6)&#93;
 data1=linear_data(1,list(range(1,9)),list(range(2,13)),A0,B0)
 assert len(data1&#91;4&#93;)==17 and data1&#91;5&#93;==&#91;17,18&#93;
 sol1,compat1=solve(data1,{},&#91;X,Y&#93;);assert all(not equation for equation in compat1)
 A1,B1=vecpair(sol1,list(range(1,9)),list(range(2,13)))

 forcing2=zadd(zmul(A1,zder(B1)),zscale(zmul(zder(A1),B1),-2))
 data2=linear_data(2,list(range(0,9)),list(range(1,13)),A0,B0)
 assert len(data2&#91;4&#93;)==18 and data2&#91;5&#93;==&#91;0,19,20&#93;
 sol2,compat2=solve(data2,zscale(forcing2,-1),&#91;U,V,W&#93;)
 assert all(not equation for equation in compat2)
 A2,B2=vecpair(sol2,list(range(0,9)),list(range(1,13)))

 forcing3=zadd(zmul(A1,zder(B2)),zscale(zmul(zder(A1),B2),-1),zscale(zmul(zder(A2),B1),-2))
 data3=linear_data(3,&#91;&#93;,list(range(0,13)),A0,B0)
 assert len(data3&#91;4&#93;)==12 and data3&#91;5&#93;==&#91;0&#93;
 sol3,compat3=solve(data3,zscale(forcing3,-1),&#91;D&#93;)
 _,B3=vecpair(sol3,&#91;&#93;,list(range(0,13)))
 assert len(compat3)==7

 E4=zadd(zmul(A1,zder(B3)),zscale(zmul(zder(A2),B2),-1))
 assert sorted(E4)==list(range(2,20)) and len(E4)==18

 # U,D are free origin-vertex coefficients. Compatibility uses only X,Y,V,W.
 for equation in compat3+list(E4.values()):
  assert all(m&#91;2&#93;==0 and m&#91;5&#93;==0 for m in equation)
  weights={sum((m&#91;0&#93;,m&#91;1&#93;,m&#91;3&#93;*2,m&#91;4&#93;*2)) for m in equation}
  assert len(weights)==1 and next(iter(weights)) in (3,4)

 m4=&#91;
  (4,0,0,0,0,0),(3,1,0,0,0,0),(2,2,0,0,0,0),(1,3,0,0,0,0),(0,4,0,0,0,0),
  (2,0,0,1,0,0),(1,1,0,1,0,0),(0,2,0,1,0,0),
  (2,0,0,0,1,0),(1,1,0,0,1,0),(0,2,0,0,1,0),
  (0,0,0,2,0,0),(0,0,0,1,1,0),(0,0,0,0,2,0),
 &#93;
 equations=&#91;&#93;;labels=&#91;&#93;
 for i,equation in enumerate(compat3):
  equations.extend(&#91;pp_mul(X,equation),pp_mul(Y,equation)&#93;)
  labels.extend(&#91;f'X*layer3&#91;{i}&#93;',f'Y*layer3&#91;{i}&#93;'&#93;)
 for degree in sorted(E4):
  equations.append(E4&#91;degree&#93;);labels.append(f'layer4&#91;z^{degree}&#93;')
 kmatrix=&#91;&#91;equation.get(m,ZERO) for m in m4&#93; for equation in equations&#93;

 prime=2053;u_value=216
 num,den=sp.fraction(sp.cancel(qr.S_IN_K0.subs(qr.u,u_value)))
 s_value=int(num)%prime*pow(int(den)%prime,-1,prime)%prime
 assert int(qr.K0_EXPR.subs(qr.u,u_value))%prime==0
 assert int(sp.diff(qr.K0_EXPR,qr.u).subs(qr.u,u_value))%prime!=0
 assert int(qr.M_EXPR.subs(qr.s,s_value))%prime==0
 matrix=&#91;&#91;coefficient.mod(prime,s_value) for coefficient in row&#93; for row in kmatrix&#93;
 selected=&#91;&#93;
 for i,row in enumerate(matrix):
  if rank_mod(&#91;matrix&#91;j&#93; for j in selected&#93;+&#91;row&#93;,prime)&gt;len(selected):selected.append(i)
  if len(selected)==14:break
 assert len(selected)==14
 determinant=determinant_mod(&#91;matrix&#91;i&#93; for i in selected&#93;,prime)
 assert determinant

 # Exact top vertices are in the radical (X,Y,V,W).
 for top in (A2&#91;8&#93;,B3&#91;12&#93;):
  assert top and (0,0,0,0,0,0) not in top
  assert all(m&#91;2&#93;==0 and m&#91;5&#93;==0 for m in top)

 return {
  'schema_version':1,
  'field':{
   'reconstructed':sp.sstr(qr.M_EXPR),
   'public_model':sp.sstr(qr.K0_EXPR),
  },
  'linear_layers':{
   'D1':{'shape':&#91;18,19&#93;,'rank':17,'free_columns':&#91;17,18&#93;},
   'D2':{'shape':&#91;19,21&#93;,'rank':18,'free_columns':&#91;0,19,20&#93;,'compatibility_zero':True},
   'D3':{'shape':&#91;19,13&#93;,'rank':12,'free_columns':&#91;0&#93;,'compatibility_count':7},
   'layer4_equation_count':18,
  },
  'effective_parameters':{'names':&#91;'X','Y','V','W'&#93;,'weights':&#91;1,1,2,2&#93;,
                          'free_origin_vertices':&#91;'U','D'&#93;},
  'degree_four_span':{
   'basis_dimension':14,'equation_rows':32,'rank':14,
   'good_reduction':{'prime':prime,'u':u_value,'s':s_value,
                     'selected_row_indices':selected,
                     'selected_row_labels':&#91;labels&#91;i&#93; for i in selected&#93;,
                     'minor_determinant':determinant},
  },
  'conclusion':{
   'P_top_vertex':'A2 coefficient of z^8, exponent (8,16)',
   'Q_top_vertex':'B3 coefficient of z^12, exponent (12,24)',
   'both_vanish_on_geometric_zero_set':True,
   'vertex_saturated_truncated_locus_empty':True,
  },
 }

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--output',type=Path)
 args=parser.parse_args()
 result=build_certificate()
 if args.output:
  args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
 witness=result&#91;'degree_four_span'&#93;&#91;'good_reduction'&#93;
 print('exact layer ranks: D1=17, D2=18, D3=12')
 print('compatibility equations: 7 at weight 3 and 18 at weight 4')
 print('effective parameter weights: X,Y,V,W = 1,1,2,2')
 print(f"weighted-degree-four span: rank 14/14; determinant {witness&#91;'minor_determinant'&#93;} mod 2053")
 print('required top P and Q vertex coefficients vanish on every solution')
 if args.output:print(f'certificate export: {args.output.name}')
 print('PASS: the vertex-saturated truncated Newton root is empty')

if __name__=='__main__':main()
</code></pre>

## `lane8-proof-queue-20260802-v1/queue.seed.json`

<pre><code class="language-json">
{
  "schema_version": 1,
  "queue_id": "lane8-proof-queue-v1",
  "scope": {
    "base_characteristic": 0,
    "geometric_semantics": "Terminal emptiness means no points over an algebraic closure of the declared coefficient field.",
    "claim_boundary": "This audit graph validates evidence and routing semantics. It does not promote the public degree-below-125 claim until the root-to-terminal coverage target becomes complete."
  },
  "sources": &#91;
    {
      "source_id": "GGHV-2022",
      "kind": "literature",
      "title": "Increasing the degree of a possible counterexample to the Jacobian Conjecture from 100 to 108",
      "locator": "arXiv:2204.14178; Theorem 2.1, Proposition 4.1, Proposition 4.3, Corollary 5.7"
    },
    {
      "source_id": "GGHV-2017",
      "kind": "literature",
      "title": "Some algorithms related to the Jacobian Conjecture",
      "locator": "arXiv:1708.07936; Theorem 2.20, Definition 2.25, Algorithm 8"
    },
    {
      "source_id": "PROGRAM6-SOURCE",
      "kind": "public_proof_source",
      "title": "Program 6 current text proof source",
      "locator": "research/proof-sources/06-plane-boundary/main/ and appendix degree-twenty-one-certificates"
    },
    {
      "source_id": "PROGRAM6-ARCHIVE",
      "kind": "technical_archive",
      "title": "Program 6 complete computational supplement",
      "locator": "assets/technical-materials/06-plane-boundary-computational-supplement.zip",
      "sha256": "4238149caa6e8a73723368e997b8c714a99258600268f14a008c5e514ecea585"
    },
    {
      "source_id": "L8-REPAIR-PACKET",
      "kind": "repair_packet",
      "title": "Lane 8 root-to-face and proof-queue checks",
      "locator": "assets/audit-repairs/lane8-proof-queue-v1/"
    }
  &#93;,
  "nodes": &#91;
    {
      "node_id": "L8-CANDIDATE-SUB125",
      "kind": "candidate_class",
      "statement": "Noninvertible plane Keller pairs in characteristic zero with maximum coordinate degree below 125, modulo exchange of coordinates.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "after extension to an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "&#91;P,Q&#93; is a nonzero constant"
        &#93;,
        "inverted_elements": &#91;
          "Jacobian constant"
        &#93;,
        "variables": &#91;
          "coefficients of P",
          "coefficients of Q"
        &#93;
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;&#93;,
      "notes": "The imported literature theorem concerns hypothetical counterexamples; noninvertibility is not encoded by one finite coefficient ideal here."
    },
    {
      "node_id": "L8-DEGREE-72-108",
      "kind": "degree_family",
      "statement": "The surviving below-125 degree pair is (72,108), up to exchange.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "after extension to an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;&#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;
        "GGHV-2022:Theorem-2.1"
      &#93;
    },
    {
      "node_id": "L8-FAMILY-828",
      "kind": "degree_family",
      "statement": "The surviving (72,108) case is the complete-chain family denoted (8,28); the (9,27) family is excluded.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "after extension to an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;&#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;
        "GGHV-2022:Proposition-4.1",
        "GGHV-2022:Corollary-5.7"
      &#93;
    },
    {
      "node_id": "L8-ROOT-828-TRUNCATED",
      "kind": "newton_root",
      "statement": "A Laurent Keller pair with bracket x^2 and the truncated Proposition 4.3 Newton polygons.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "&#91;P,Q&#93;=x^2"
        &#93;,
        "inverted_elements": &#91;
          "product of P vertex coefficients",
          "product of Q vertex coefficients"
        &#93;,
        "required_zero": &#91;
          "all coefficients outside the two declared polygons"
        &#93;,
        "variables": &#91;
          "25 allowed P coefficients",
          "47 allowed Q coefficients"
        &#93;
      },
      "support": {
        "P": {
          "vertices": &#91;
            &#91;
              0,
              0
            &#93;,
            &#91;
              1,
              0
            &#93;,
            &#91;
              8,
              14
            &#93;,
            &#91;
              8,
              16
            &#93;
          &#93;,
          "lattice_count": 25,
          "deficiency": "b-2a+2",
          "layer_counts": &#91;
            8,
            8,
            9
          &#93;
        },
        "Q": {
          "vertices": &#91;
            &#91;
              0,
              0
            &#93;,
            &#91;
              2,
              1
            &#93;,
            &#91;
              12,
              21
            &#93;,
            &#91;
              12,
              24
            &#93;
          &#93;,
          "lattice_count": 47,
          "deficiency": "b-2a+3",
          "layer_counts": &#91;
            11,
            11,
            12,
            13
          &#93;
        }
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;
        "GGHV-2022:Proposition-4.3-case-2"
      &#93;
    },
    {
      "node_id": "L8-ROOT-828-FULL",
      "kind": "newton_root",
      "statement": "A Laurent Keller pair with bracket x^2 and the full Proposition 4.3 Newton polygons.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "&#91;P,Q&#93;=x^2"
        &#93;,
        "inverted_elements": &#91;
          "product of P vertex coefficients",
          "product of Q vertex coefficients"
        &#93;,
        "required_zero": &#91;
          "all coefficients outside the two declared polygons"
        &#93;,
        "variables": &#91;
          "61 allowed P coefficients",
          "125 allowed Q coefficients"
        &#93;
      },
      "support": {
        "P": {
          "vertices": &#91;
            &#91;
              0,
              0
            &#93;,
            &#91;
              1,
              0
            &#93;,
            &#91;
              8,
              14
            &#93;,
            &#91;
              8,
              16
            &#93;,
            &#91;
              0,
              8
            &#93;
          &#93;,
          "lattice_count": 61,
          "deficiency": "b-2a+2",
          "layer_counts": &#91;
            8,
            8,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1
          &#93;
        },
        "Q": {
          "vertices": &#91;
            &#91;
              0,
              0
            &#93;,
            &#91;
              2,
              1
            &#93;,
            &#91;
              12,
              21
            &#93;,
            &#91;
              12,
              24
            &#93;,
            &#91;
              0,
              12
            &#93;
          &#93;,
          "lattice_count": 125,
          "deficiency": "b-2a+3",
          "layer_counts": &#91;
            11,
            11,
            12,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1
          &#93;
        }
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;
        "GGHV-2022:Proposition-4.3-case-1"
      &#93;
    },
    {
      "node_id": "L8-FACE-DEG21",
      "kind": "face_locus",
      "statement": "Polynomials p,q of degrees 7 and 10 with nonzero endpoint coefficients satisfying p*q+2*z*p*q'-3*z*p'*q=1.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "p*q+2*z*p*q'-3*z*p'*q=1"
        &#93;,
        "inverted_elements": &#91;
          "p(0)",
          "q(0)",
          "lc(p)",
          "lc(q)"
        &#93;,
        "variables": &#91;
          "coefficients of p of degree at most 7",
          "coefficients of q of degree at most 10"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:root_face_check.py"
      &#93;
    },
    {
      "node_id": "L8-PASSPORT-DEG21",
      "kind": "passport_locus",
      "statement": "The rational map tau=z*q^2/p^3 has degree 21 and passport (2^10 1),(3^7),(17 1^4).",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "tau=z*q^2/p^3",
          "tau'=q/p^4"
        &#93;,
        "inverted_elements": &#91;
          "resultant(p,q)",
          "p(0)",
          "q(0)",
          "lc(p)",
          "lc(q)"
        &#93;,
        "variables": &#91;
          "z"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:root_face_check.py"
      &#93;
    },
    {
      "node_id": "L8-DESSIN-COUNT-5",
      "kind": "dessin_classification",
      "statement": "The degree-21 passport has five connected isomorphism classes, each with trivial deck group.",
      "field": {
        "base": "characteristic zero",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "sigma_0*sigma_1*sigma_infinity=1"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "permutation triples with the declared cycle types"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:hurwitz_degree21.py"
      &#93;
    },
    {
      "node_id": "L8-QUINTIC-ORBIT",
      "kind": "coefficient_field_orbit",
      "statement": "The five normalized degree-21 faces form one Galois orbit over K0=Q&#91;u&#93;/(u^5-u^4+3u^3+3u^2+26); exact coefficient formulas are reconstructed in the repair packet.",
      "field": {
        "base": "K0",
        "geometric_points": "all five embeddings into an algebraic closure",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "exact p,q coefficient formulas in quintic_face_coefficients.json",
          "p*q+2*z*p*q'-3*z*p'*q=1",
          "z*q_monic^2-p^3 has degree at most 4"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "u"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:quintic_face_reconstruction.py",
        "L8-REPAIR-PACKET:quintic_face_coefficients.json",
        "L8-REPAIR-PACKET:quintic_face_reconstruction.out"
      &#93;,
      "notes": "The packet reconstructs an irreducible quintic in the normalized coefficient s, verifies all face and order-17 contact identities, and gives an exact field isomorphism s=(20481190-2578004u+1664322u^2-709604u^3+221083u^4)/42799752 to the public Program 6 K0 model."
    },
    {
      "node_id": "L8-TRUNCATED-LAYER-SYSTEM",
      "kind": "finite_system",
      "statement": "The complete truncated-support compatibility system reconstructed exactly from the quintic face and all 25+47 coefficient windows.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "7 exact weight-three compatibility polynomials",
          "18 exact weight-four compatibility polynomials",
          "the 14-dimensional weighted-degree-four monomial span"
        &#93;,
        "inverted_elements": &#91;
          "P coefficient at exponent (8,16)",
          "Q coefficient at exponent (12,24)",
          "the already nonzero lower-face vertex coefficients"
        &#93;,
        "variables": &#91;
          "four effective positive-weight parameters"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json",
        "L8-REPAIR-PACKET:truncated_support_certificate.out"
      &#93;
    },
    {
      "node_id": "L8-TRUNCATED-EMPTY",
      "kind": "terminal_empty",
      "statement": "The exact vertex-saturated truncated Proposition 4.3 root is empty in characteristic zero for the complete quintic orbit.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "1=0 after radical/vertex contradiction"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": true,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json"
      &#93;
    },
    {
      "node_id": "L8-FULL-EARLY-LAYERS",
      "kind": "finite_system",
      "statement": "The exact full-support layers 1 through 4 over the quintic face, including the forced square relation a*(W-kappa*Y^2)^2.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "layer-1, layer-2, and layer-3 compatibility functionals vanish identically",
          "layer-4 compatibility is a*(W-kappa*Y^2)^2"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "X,Y at layer 1",
          "U,V,W at layer 2",
          "R,S,T at layer 3",
          "H at layer 4"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:full_early_layer_reduction.py",
        "L8-REPAIR-PACKET:full_early_layer_reduction.json",
        "L8-REPAIR-PACKET:full_layer_rank_profile.py",
        "L8-REPAIR-PACKET:full_layer_rank_profile.json"
      &#93;,
      "notes": "The reduced geometric locus satisfies W=kappa*Y^2, but the exact scheme-level equation is a square and its double structure is retained. All full-support layer maps from layer 5 onward are injective."
    },
    {
      "node_id": "L8-FULL-15-EQUATIONS",
      "kind": "finite_system",
      "statement": "The fifteen normalized compatibility equations in five variables obtained from the full support through layers five to eight.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "15 normalized equations with layer counts 1,3,5,6"
        &#93;,
        "inverted_elements": &#91;
          "the recorded normalization factor t_(1,1)"
        &#93;,
        "variables": &#91;
          "five normalized terminal variables"
        &#93;
      },
      "proof_status": "source_replay_needed",
      "terminal": false,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:terminal-residue-provenance"
      &#93;
    },
    {
      "node_id": "L8-FULL-SIX-POLYNOMIALS",
      "kind": "finite_system",
      "statement": "The six selected obstruction polynomials rho,g1,...,g5 used in the compact toric certificate.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "rho",
          "g1",
          "g2",
          "g3",
          "g4",
          "g5"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "five normalized terminal variables"
        &#93;
      },
      "proof_status": "verified_in_public_source",
      "terminal": false,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:compact-toric-terminal-certificate"
      &#93;
    },
    {
      "node_id": "L8-FULL-TORIC-EMPTY",
      "kind": "terminal_empty",
      "statement": "The six displayed full-support obstruction polynomials have no common geometric zero over K0.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "1=0 on the six-polynomial zero locus"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "verified_in_public_source",
      "terminal": true,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:compact-toric-terminal-certificate",
        "PROGRAM6-ARCHIVE"
      &#93;
    },
    {
      "node_id": "L8-K4-STORED-SYSTEM",
      "kind": "finite_system",
      "statement": "The stored degree-21 specialization after the canonical k=4 adjacent-chart transition and forced common approximate root.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "complete layer-five-through-seven support and chart-matching equations"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "stored adjacent-chart coefficients"
        &#93;
      },
      "proof_status": "verified_in_public_source",
      "terminal": false,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:k4-chart-transition"
      &#93;
    },
    {
      "node_id": "L8-K4-LAYER7-EMPTY",
      "kind": "terminal_empty",
      "statement": "The stored adjacent-chart layer-five-through-seven system has no common geometric zero over K0.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "1=0 after the two recorded affine/weighted branches"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "verified_in_public_source",
      "terminal": true,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:stored-terminal-layer-seven",
        "PROGRAM6-ARCHIVE"
      &#93;
    }
  &#93;,
  "edges": &#91;
    {
      "edge_id": "L8-E-SUB125-DEGREE",
      "from": "L8-CANDIDATE-SUB125",
      "to": &#91;
        "L8-DEGREE-72-108"
      &#93;,
      "edge_type": "external_import",
      "coverage": "cover",
      "proof_status": "audited_external_theorem",
      "statement": "Theorem 2.1 leaves only degree pair (72,108), up to exchange, below 125.",
      "hypotheses": &#91;
        "characteristic zero",
        "hypothetical noninvertible Keller pair",
        "maximum coordinate degree below 125"
      &#93;,
      "source_refs": &#91;
        "GGHV-2022:Theorem-2.1"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-DEGREE-FAMILY",
      "from": "L8-DEGREE-72-108",
      "to": &#91;
        "L8-FAMILY-828"
      &#93;,
      "edge_type": "external_import",
      "coverage": "cover",
      "proof_status": "audited_external_theorem",
      "statement": "The (9,27) family is reduced by Proposition 4.1 to the system excluded by Corollary 5.7, leaving (8,28).",
      "hypotheses": &#91;
        "the complete-chain family list used in GGHV-2022"
      &#93;,
      "source_refs": &#91;
        "GGHV-2022:Proposition-4.1",
        "GGHV-2022:Corollary-5.7"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FAMILY-ROOT-SPLIT",
      "from": "L8-FAMILY-828",
      "to": &#91;
        "L8-ROOT-828-TRUNCATED",
        "L8-ROOT-828-FULL"
      &#93;,
      "edge_type": "exhaustive_split",
      "coverage": "cover",
      "proof_status": "audited_external_theorem",
      "statement": "Proposition 4.3 gives exactly the two normalized Newton-polygon alternatives.",
      "hypotheses": &#91;
        "the (8,28) family",
        "the Laurent transformations in Proposition 4.3"
      &#93;,
      "source_refs": &#91;
        "GGHV-2022:Proposition-4.3"
      &#93;,
      "verifier": "root_face_check.py verifies the final exponent transform and bracket multiplier",
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-TRUNCATED-FACE",
      "from": "L8-ROOT-828-TRUNCATED",
      "to": &#91;
        "L8-FACE-DEG21"
      &#93;,
      "edge_type": "forced_initial_form",
      "coverage": "cover",
      "proof_status": "verified_in_packet",
      "statement": "The minimum (-2,1)-valuation faces are x*p(x*y^2) and x^2*y*q(x*y^2), and their bracket forces the degree-21 face equation.",
      "hypotheses": &#91;
        "exact truncated Newton polygons",
        "&#91;P,Q&#93;=x^2"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET"
      &#93;,
      "verifier": "root_face_check.py",
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FULL-FACE",
      "from": "L8-ROOT-828-FULL",
      "to": &#91;
        "L8-FACE-DEG21"
      &#93;,
      "edge_type": "forced_initial_form",
      "coverage": "cover",
      "proof_status": "verified_in_packet",
      "statement": "The full polygons have the same minimum (-2,1)-valuation faces, hence force the identical degree-21 face equation.",
      "hypotheses": &#91;
        "exact full Newton polygons",
        "&#91;P,Q&#93;=x^2"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET"
      &#93;,
      "verifier": "root_face_check.py",
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FACE-PASSPORT",
      "from": "L8-FACE-DEG21",
      "to": &#91;
        "L8-PASSPORT-DEG21"
      &#93;,
      "edge_type": "forced_consequence",
      "coverage": "dependency",
      "proof_status": "verified_in_packet",
      "statement": "For tau=z*q^2/p^3, the face equation gives tau'=q/p^4 and the complete degree-21 passport.",
      "hypotheses": &#91;
        "degree p=7",
        "degree q=10",
        "nonzero endpoint coefficients"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET"
      &#93;,
      "verifier": "root_face_check.py",
      "requires": &#91;&#93;,
      "propagates_emptiness": false
    },
    {
      "edge_id": "L8-E-PASSPORT-DESSINS",
      "from": "L8-PASSPORT-DEG21",
      "to": &#91;
        "L8-DESSIN-COUNT-5"
      &#93;,
      "edge_type": "classification",
      "coverage": "dependency",
      "proof_status": "verified_in_packet",
      "statement": "The exact Frobenius/Murnaghan--Nakayama count is five; transitivity and trivial deck group turn the weighted count into five connected isomorphism classes.",
      "hypotheses": &#91;
        "cycle types (2^10 1),(3^7),(17 1^4)"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET"
      &#93;,
      "verifier": "hurwitz_degree21.py",
      "requires": &#91;&#93;,
      "propagates_emptiness": false
    },
    {
      "edge_id": "L8-E-DESSINS-QUINTIC",
      "from": "L8-DESSIN-COUNT-5",
      "to": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "edge_type": "coefficient_reconstruction",
      "coverage": "dependency",
      "proof_status": "verified_in_packet",
      "statement": "Under the monic normalization p=z^7+z^6+s z^5+... and q_monic monic of degree 10, exact order-17 contact determines p,q over an irreducible quintic. Its five embeddings give five distinct normalized covers and an exact isomorphism to the public Program 6 field K0.",
      "hypotheses": &#91;
        "a fixed normalization of p,q and z",
        "the five connected dessin classes"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET:quintic_face_reconstruction.py",
        "L8-REPAIR-PACKET:quintic_face_coefficients.json",
        "PROGRAM6-SOURCE:degree-21-Belyi-reconstruction"
      &#93;,
      "notes": "Because the passport has exactly five connected classes, the five distinct embeddings of the irreducible quintic exhaust the classes and form one Galois orbit.",
      "requires": &#91;&#93;,
      "propagates_emptiness": false,
      "verifier": "quintic_face_reconstruction.py"
    },
    {
      "edge_id": "L8-E-TRUNCATED-LAYERS",
      "from": "L8-ROOT-828-TRUNCATED",
      "to": &#91;
        "L8-TRUNCATED-LAYER-SYSTEM"
      &#93;,
      "edge_type": "elimination",
      "coverage": "cover",
      "proof_status": "verified_in_packet",
      "statement": "The exact layer recursion has ranks 17,18,12 at layers 1,2,3; it produces seven weight-three and eighteen weight-four equations in effective parameters X,Y,V,W of weights 1,1,2,2.",
      "hypotheses": &#91;
        "one of the five normalized face embeddings",
        "truncated coefficient windows"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json"
      &#93;,
      "notes": "The origin-vertex parameters U,D remain free. The required top vertices are explicit polynomials in X,Y,V,W.",
      "requires": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "propagates_emptiness": true,
      "verifier": "truncated_support_certificate.py"
    },
    {
      "edge_id": "L8-E-TRUNCATED-CERTIFICATE",
      "from": "L8-TRUNCATED-LAYER-SYSTEM",
      "to": &#91;
        "L8-TRUNCATED-EMPTY"
      &#93;,
      "edge_type": "terminal_certificate",
      "coverage": "terminal",
      "proof_status": "verified_in_packet",
      "statement": "Products of the seven weight-three equations with X,Y together with the eighteen weight-four equations span all fourteen weighted-degree-four monomials. A selected 14x14 minor has determinant 894 modulo (2053,u-216), so X,Y,V,W lie in the radical; the required top P and Q vertices therefore vanish.",
      "hypotheses": &#91;
        "the exact regenerated truncated system",
        "the declared vertex saturation"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true,
      "verifier": "truncated_support_certificate.py"
    },
    {
      "edge_id": "L8-E-FULL-EARLY",
      "from": "L8-ROOT-828-FULL",
      "to": &#91;
        "L8-FULL-EARLY-LAYERS"
      &#93;,
      "edge_type": "elimination",
      "coverage": "cover",
      "proof_status": "verified_in_packet",
      "statement": "Reconstruct the complete full-support layers 1 through 4 exactly. The only nonzero early compatibility condition is the square a*(W-kappa*Y^2)^2; the exact layer-rank profile is recorded through layer 15.",
      "hypotheses": &#91;
        "one of the five normalized quintic face embeddings",
        "the full Proposition 4.3 coefficient windows"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET:full_early_layer_reduction.py",
        "L8-REPAIR-PACKET:full_layer_rank_profile.py"
      &#93;,
      "verifier": "full_early_layer_reduction.py; full_layer_rank_profile.py",
      "requires": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FULL-LAYERS",
      "from": "L8-FULL-EARLY-LAYERS",
      "to": &#91;
        "L8-FULL-15-EQUATIONS"
      &#93;,
      "edge_type": "elimination",
      "coverage": "cover",
      "proof_status": "source_replay_needed",
      "statement": "Starting from the exact square branch and the injective layer maps from layer 5 onward, reproduce the obstruction equations through layer 8, every normalization/localization, and the reduction to the fifteen equations in five variables.",
      "hypotheses": &#91;
        "the exact full early-layer system",
        "the scheme-level square relation is retained until a radical argument is declared",
        "the full coefficient windows"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:terminal-residue-provenance",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "requires": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "propagates_emptiness": true,
      "notes": "The early layers and all linear ranks are now independently closed. The remaining gap begins with nonlinear forcing at layer 5 and the provenance of the five-variable normalization."
    },
    {
      "edge_id": "L8-E-FULL-PROJECTION",
      "from": "L8-FULL-15-EQUATIONS",
      "to": &#91;
        "L8-FULL-SIX-POLYNOMIALS"
      &#93;,
      "edge_type": "relaxation",
      "coverage": "superset",
      "proof_status": "source_replay_needed",
      "statement": "Forget nine equations and retain the six indexed equations used in the compact toric certificate; emptiness of the larger six-equation zero locus excludes the fifteen-equation locus.",
      "hypotheses": &#91;
        "coefficientwise identification of the fifteen regenerated equations with the stored normalized system"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:terminal-residue-provenance",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "notes": "This direction is a relaxation: V(15 equations) is contained in V(the selected 6).",
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FULL-TORIC-CERTIFICATE",
      "from": "L8-FULL-SIX-POLYNOMIALS",
      "to": &#91;
        "L8-FULL-TORIC-EMPTY"
      &#93;,
      "edge_type": "terminal_certificate",
      "coverage": "terminal",
      "proof_status": "verified_in_public_source",
      "statement": "The compact toric argument proves that the six displayed polynomials have no common geometric zero over K0.",
      "hypotheses": &#91;
        "the exact six displayed polynomials",
        "the recorded good-prime and toric data"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:compact-toric-terminal-certificate",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FULL-K4-STORED",
      "from": "L8-ROOT-828-FULL",
      "to": &#91;
        "L8-K4-STORED-SYSTEM"
      &#93;,
      "edge_type": "noncovering_specialization",
      "coverage": "noncovering",
      "proof_status": "verified_in_public_source",
      "statement": "The stored specialization admits the canonical k=4 adjacent-chart calculation, but no theorem presently says every full-root point reaches this stored system.",
      "hypotheses": &#91;
        "the additional stored specialization conditions"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:k4-chart-transition"
      &#93;,
      "notes": "This edge is deliberately excluded from global coverage propagation.",
      "requires": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "propagates_emptiness": false
    },
    {
      "edge_id": "L8-E-K4-CERTIFICATE",
      "from": "L8-K4-STORED-SYSTEM",
      "to": &#91;
        "L8-K4-LAYER7-EMPTY"
      &#93;,
      "edge_type": "terminal_certificate",
      "coverage": "terminal",
      "proof_status": "verified_in_public_source",
      "statement": "The complete stored layer-five-through-seven equations are empty after the two recorded branches are certified.",
      "hypotheses": &#91;
        "the exact stored adjacent-chart system"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:stored-terminal-layer-seven",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    }
  &#93;,
  "obligations": &#91;
    {
      "obligation_id": "L8-O-LITERATURE-IMPORT",
      "statement": "State the exact external theorem chain from a sub-125 candidate to the two Proposition 4.3 roots and independently check the final monomial transformation.",
      "status": "closed",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "GGHV-2022",
        "L8-REPAIR-PACKET:root_face_check.py"
      &#93;,
      "next_action": "A full rederivation of the imported literature proofs is optional specialist verification, not an unrecorded queue edge."
    },
    {
      "obligation_id": "L8-O-COMMON-FACE",
      "statement": "Prove that both roots force the same degree-21 face and normal-layer operator.",
      "status": "closed",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "L8-REPAIR-PACKET:root_face_check.py"
      &#93;,
      "next_action": "Use the canonical layer labels in every downstream manifest."
    },
    {
      "obligation_id": "L8-O-QUINTIC-RECONSTRUCTION",
      "statement": "Independently regenerate normalized p,q for all five dessins and prove the displayed quintic field realizes one complete Galois orbit.",
      "status": "closed",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "L8-REPAIR-PACKET:quintic_face_reconstruction.py",
        "L8-REPAIR-PACKET:quintic_face_coefficients.json",
        "L8-REPAIR-PACKET:quintic_face_reconstruction.out"
      &#93;,
      "next_action": "Use the exported exact coefficients as the canonical lower-face input for the truncated and full normal-layer replays."
    },
    {
      "obligation_id": "L8-O-ARCHIVE-STAGE-MANIFEST",
      "statement": "Expose every root-to-terminal generation stage with node identifiers, branch conditions, code/input/output hashes, and semantic digests.",
      "status": "open",
      "blocks": &#91;
        "L8-E-TRUNCATED-LAYERS",
        "L8-E-FULL-LAYERS",
        "L8-E-FULL-PROJECTION"
      &#93;,
      "evidence": &#91;
        "PROGRAM6-ARCHIVE"
      &#93;,
      "next_action": "Materialize the archive and generate a deterministic stage manifest rather than relying on filenames and narrative provenance."
    },
    {
      "obligation_id": "L8-O-TRUNCATED-REPLAY",
      "statement": "Rebuild the 7+18 compatibility equations, the fourteen-monomial span, and the exact vertex saturation from the raw truncated windows.",
      "status": "closed",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json",
        "L8-REPAIR-PACKET:truncated_support_certificate.out"
      &#93;,
      "next_action": "Use the closed truncated branch as an independently certified child while auditing the full branch."
    },
    {
      "obligation_id": "L8-O-FULL-ELIMINATION-REPLAY",
      "statement": "Continue the independently reconstructed full branch from layer 5 through the fifteen normalized equations, preserving every denominator-zero branch and the nonreduced square structure.",
      "status": "open",
      "blocks": &#91;
        "L8-E-FULL-LAYERS",
        "L8-E-FULL-PROJECTION"
      &#93;,
      "evidence": &#91;
        "L8-REPAIR-PACKET:full_early_layer_reduction.py",
        "L8-REPAIR-PACKET:full_layer_rank_profile.py",
        "PROGRAM6-SOURCE:terminal-residue-provenance",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "next_action": "Derive the layer-5 obstruction from the exact square branch, then emit a row/column and extension/contraction ledger through layer 8. Use W=kappa*Y^2 only when explicitly passing to geometric radicals."
    },
    {
      "obligation_id": "L8-O-K4-COVERAGE",
      "statement": "Determine whether the k=4 adjacent-chart system covers a full-root branch or is only a stored specialization.",
      "status": "blocked",
      "blocks": &#91;
        "L8-E-FULL-K4-STORED"
      &#93;,
      "evidence": &#91;
        "PROGRAM6-SOURCE:k4-chart-transition"
      &#93;,
      "next_action": "Prove a Lane 9 chart-correspondence theorem or keep the edge noncovering."
    },
    {
      "obligation_id": "L8-O-INDEPENDENT-TERMINAL-REPLAY",
      "statement": "Independently replay at least one large terminal certificate from its exact generators and archived data.",
      "status": "open",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "PROGRAM6-SOURCE",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "next_action": "Prefer the compact six-polynomial toric certificate because its mathematical lifting argument is already isolated."
    }
  &#93;,
  "coverage_targets": &#91;
    {
      "target_id": "L8-COVERAGE-LITERATURE-ROOTS",
      "kind": "routing",
      "expected": "complete",
      "accepted_proof_statuses": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source"
      &#93;,
      "requirements": &#91;
        {
          "from_node": "L8-CANDIDATE-SUB125",
          "all_of": &#91;
            "L8-ROOT-828-TRUNCATED",
            "L8-ROOT-828-FULL"
          &#93;
        }
      &#93;,
      "notes": "Statement-level audit of the imported theorem chain, not a new proof of every cited literature lemma."
    },
    {
      "target_id": "L8-COVERAGE-ROOTS-TO-FACE",
      "kind": "routing",
      "expected": "complete",
      "accepted_proof_statuses": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source"
      &#93;,
      "requirements": &#91;
        {
          "from_node": "L8-ROOT-828-TRUNCATED",
          "all_of": &#91;
            "L8-FACE-DEG21",
            "L8-PASSPORT-DEG21",
            "L8-DESSIN-COUNT-5"
          &#93;
        },
        {
          "from_node": "L8-ROOT-828-FULL",
          "all_of": &#91;
            "L8-FACE-DEG21",
            "L8-PASSPORT-DEG21",
            "L8-DESSIN-COUNT-5"
          &#93;
        }
      &#93;,
      "notes": "The common face, passport, and count are independently checked in this packet."
    },
    {
      "target_id": "L8-COVERAGE-ROOTS-TO-TERMINALS",
      "kind": "exclusion",
      "expected": "incomplete",
      "accepted_proof_statuses": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source"
      &#93;,
      "assumption_nodes": &#91;
        "L8-ROOT-828-TRUNCATED",
        "L8-ROOT-828-FULL"
      &#93;,
      "prove_empty": &#91;
        "L8-ROOT-828-TRUNCATED",
        "L8-ROOT-828-FULL"
      &#93;,
      "notes": "The missing independently replayed edges are the quintic reconstruction and the raw-support-to-terminal elimination ledgers."
    },
    {
      "target_id": "L8-COVERAGE-SUB125-EXCLUSION",
      "kind": "exclusion",
      "expected": "incomplete",
      "accepted_proof_statuses": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source"
      &#93;,
      "assumption_nodes": &#91;
        "L8-CANDIDATE-SUB125"
      &#93;,
      "prove_empty": &#91;
        "L8-CANDIDATE-SUB125"
      &#93;,
      "notes": "This is the standalone below-125 conclusion. It can become complete only after both imported roots are excluded through covering edges."
    }
  &#93;
}
</code></pre>

## `lane8-proof-queue-20260802-v1/truncated_support_certificate.json`

<pre><code class="language-json">
{
  "conclusion": {
    "P_top_vertex": "A2 coefficient of z^8, exponent (8,16)",
    "Q_top_vertex": "B3 coefficient of z^12, exponent (12,24)",
    "both_vanish_on_geometric_zero_set": true,
    "vertex_saturated_truncated_locus_empty": true
  },
  "degree_four_span": {
    "basis_dimension": 14,
    "equation_rows": 32,
    "good_reduction": {
      "minor_determinant": 894,
      "prime": 2053,
      "s": 1831,
      "selected_row_indices": &#91;
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        14,
        15,
        16
      &#93;,
      "selected_row_labels": &#91;
        "X*layer3&#91;0&#93;",
        "Y*layer3&#91;0&#93;",
        "X*layer3&#91;1&#93;",
        "Y*layer3&#91;1&#93;",
        "X*layer3&#91;2&#93;",
        "Y*layer3&#91;2&#93;",
        "X*layer3&#91;3&#93;",
        "Y*layer3&#91;3&#93;",
        "X*layer3&#91;4&#93;",
        "Y*layer3&#91;4&#93;",
        "X*layer3&#91;5&#93;",
        "layer4&#91;z^2&#93;",
        "layer4&#91;z^3&#93;",
        "layer4&#91;z^4&#93;"
      &#93;,
      "u": 216
    },
    "rank": 14
  },
  "effective_parameters": {
    "free_origin_vertices": &#91;
      "U",
      "D"
    &#93;,
    "names": &#91;
      "X",
      "Y",
      "V",
      "W"
    &#93;,
    "weights": &#91;
      1,
      1,
      2,
      2
    &#93;
  },
  "field": {
    "public_model": "u**5 - u**4 + 3*u**3 + 3*u**2 + 26",
    "reconstructed": "287548593020928*s**5 - 688401965085696*s**4 + 640652914818432*s**3 - 292066554895024*s**2 + 65563255857792*s - 5817852446211"
  },
  "linear_layers": {
    "D1": {
      "free_columns": &#91;
        17,
        18
      &#93;,
      "rank": 17,
      "shape": &#91;
        18,
        19
      &#93;
    },
    "D2": {
      "compatibility_zero": true,
      "free_columns": &#91;
        0,
        19,
        20
      &#93;,
      "rank": 18,
      "shape": &#91;
        19,
        21
      &#93;
    },
    "D3": {
      "compatibility_count": 7,
      "free_columns": &#91;
        0
      &#93;,
      "rank": 12,
      "shape": &#91;
        19,
        13
      &#93;
    },
    "layer4_equation_count": 18
  },
  "schema_version": 1
}
</code></pre>

[Back to Lane 8](plane-newton-queue-terminal-certificates.md)
