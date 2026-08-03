# Lane 8 exact research source packet

This is the public source packet for **Plane Newton queue and terminal certificates**. It contains the
selected proof notes, exact computation contracts, and checkers used
by the concise lane brief. Read only the files relevant to the route
you pursue. Stored outputs and very large reconstructible matrices are
omitted; the mathematical boundary of each checker remains in its
source text.

Private-source commit: `43fe2294f74c961039a5b522f27a5982d511daa3`.

## Included files

- `lane8-full-root-closure-20260803-v1/FULL_ROOT_CLOSURE_PROOF.md` — `2eeb8b32471a6d0cc46bbdb35adb3e58a9aaa055c44fb3399970f53e9eb1e670`
- `lane8-full-root-closure-20260803-v1/independent_raw_support_replay.py` — `5e84c9b9a3ef77c1de5f28555a28d2f207212b774bc96df3f91b1f37799aab4d`
- `lane8-full-root-closure-20260803-v1/verify_lane8_packet.py` — `35a40633f1e229adadf42150b2f370a75403fc2232bcb8214011bae1a39013a1`
- `lane8-proof-queue-20260802-v1/lane8-proof-queue-repair.md` — `bdbe6c5557e93c3dbafac75ffbf3c833eb22d5988af9e3f7bfcbdd4b040b94f0`
- `lane8-proof-queue-20260802-v1/check_queue.py` — `e1b6556645ff74e18ce04600f1d1e5ff7bcbe30e4dfeaa9ec53cadbe7b32320e`
- `lane8-proof-queue-20260802-v1/full_early_layer_reduction.py` — `ed4a150374eb969e19bf8601f8f4529edae57fb457f9aae9211997fb6f83bd95`
- `lane8-proof-queue-20260802-v1/quintic_face_reconstruction.py` — `e48869fb09d7afcc3c1ae08a604c7656efadf0c3588c0fca82a42817dfaf8c1f`
- `lane8-proof-queue-20260802-v1/truncated_support_certificate.py` — `40daac940f6c82e76a3679495e14cd0fcadfe5a926b3053eeff2cab879401da5`
- `lane8-proof-queue-20260802-v1/queue.seed.json` — `a55e0c1aaf49d834ec0004c14f64e0ba04d8d969d1af9cde5eef01da4ea28743`
- `lane8-proof-queue-20260802-v1/truncated_support_certificate.json` — `f086c7eca67d51f3c48fd6311c55e8fe5012a8b1373ff6eae4746fd4c3fec6ac`
- `planar-descent-no-go-20260802-v1/README.md` — `6e483b4273025c64f004a512b3de80296ff6e7479dfec51e8a484af8c5d06d60`
- `planar-descent-no-go-20260802-v1/three_dimensional_descent_no_go.py` — `e5d51dd28d34f7586539f854a2f40b97591ec0a7d7728bff5acc6ef18ce829a6`
- `planar-descent-no-go-20260802-v1/affine_plane_linear_projection_no_go.py` — `8ea6300b370186911f8109a2aada13679b1612428bae9d045d9c9720aaa1ab02`
- `planar-descent-no-go-20260802-v1/y_graph_descent_no_go.py` — `e157ae481c1e47d234ae5a048e388955d24aebe05b102baf4e7cccb9871be09e`
- `planar-descent-no-go-20260802-v1/linear_target_coordinate_fibres.py` — `3428ddee84b549dcb1f247d41d8abe9dde62c62e7dfae97820ab9d427604de3e`
- `planar-descent-no-go-20260802-v1/hc4_linear_descent_no_go.py` — `8644beef8041ae41578ed84fa58697b6f0aae9726eb37086f4b040c9f2925ce4`
- `planar-descent-no-go-20260802-v1/hc4_square_correction_no_go.py` — `41d933337f35705eb1031e82d54f666853206bda0ec97315e8a4f7aa0ed43b57`
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md` — `63fb30b6de06df86c9c87e968d4d72e58b9218134a9eaa8cbce978b78901eb5e`
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/next_complete_chain_queue.json` — `c161f309194a8f0e86d7b1343d5c7e192e76afb80ab5bb62f02048c28a20c50c`
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi_reduction.md` — `60309805f47062ed2d3a3c8a6a9f0ad04698db44267acfa657377b2cca417ae6`
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/verify_F2_degree125_seed.py` — `6f8ad5aea64d82ef73037260721fc5a5280058ee64cea599442a1bfda2e982a8`
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi.py` — `eab0a34c3f4565999fbcd09389fb059e1f4d5bf63df366cd89541549761b8fc6`
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_face_rigidity.py` — `dcb23b88c89bb3588d48e98826abe3289ce040a469ca610666b17baae8acaa1f`

## `lane8-full-root-closure-20260803-v1/FULL_ROOT_CLOSURE_PROOF.md`

<pre><code class="language-markdown">
# Direct terminal closure for the Lane 8 Newton roots

## 1. Scope and theorem boundary

Work in characteristic zero. The imported Newton reduction leaves two
normalized support polygons after the common degree-`21` lower face has been
selected. Call them the **truncated root** and the **full root**. This note
proves the following relative statement.

### Theorem 1 — Lane 8 closure relative to explicit imports

Assume:

1. the published below-`125` reduction routes every relevant plane Keller pair
   to one of the two displayed normalized `(8,28)` supports;
2. the common face belongs to the exact quintic orbit recorded in the Lane 8
   packet; and
3. the current Program 6 compact toric theorem is valid for its six displayed
   normalized obstruction polynomials.

Then both normalized support loci are empty over an algebraic closure of the
coefficient field. Consequently, using the imported reduction, no
characteristic-zero plane Keller counterexample has maximum coordinate degree
strictly below `125`.

The new work here is the complete raw-support reconstruction through the
necessary layer-eight obstruction, the complement ledger, proof that the
normalization loses no point of that early-layer exact-support locus, and
coefficientwise attachment of the resulting full-root projection to the
six-polynomial toric terminal. The three assumptions above are not reproved.

## 2. Common lower face and coefficient field

Let

\&#91;
K_0=\mathbf Q&#91;u&#93;/(m(u)),\qquad
m(u)=u^5-u^4+3u^3+3u^2+26.
\&#93;

The replay verifies that the reduction of `m` modulo `67` is irreducible by a
Rabin test. Since `m` is monic and primitive, this is an irreducibility witness
over \(\mathbf Q\).

For the valuation

\&#91;
\nu(x^a y^b)=-2a+b,
\&#93;
put \(z=xy^2\). Both support roots have initial forms

\&#91;
P_0=xp(z),\qquad Q_0=x^2yq(z),
\&#93;
with \(\deg p=7\), \(\deg q=10\). Direct differentiation gives

\&#91;
&#91;P_0,Q_0&#93;
=x^2\bigl(pq+2zpq'-3zp'q\bigr).
\&#93;

Hence the normalized bracket condition forces

\&#91;
pq+2zpq'-3zp'q=1. \tag{2.1}
\&#93;

The exact relation fixture reconstructs all coefficients of `p` and `q` in
\(K_0\). The replay checks all eighteen coefficients of (2.1), not merely a
numerical embedding.

## 3. Raw support and triangular layer equation

Set

\&#91;
t=y,\qquad z=xy^2,
\&#93;

and write

\&#91;
P=t^{-2}A(z,t),\qquad Q=t^{-3}B(z,t).
\&#93;

Because \(\det \partial(z,t)/\partial(x,y)=t^2\), the equation
\(&#91;P,Q&#93;=x^2\) becomes

\&#91;
2AB_z-3A_zB+t(A_zB_t-A_tB_z)=z^2. \tag{3.1}
\&#93;

Write

\&#91;
A=\sum_{r\ge0}t^rA_r(z),\qquad
B=\sum_{r\ge0}t^rB_r(z).
\&#93;

The coefficient of \(t^r\) in the left side is

\&#91;
E_r=
\sum_{i+j=r}
\left((2-i)A_iB_j'+(j-3)A_i'B_j\right). \tag{3.2}
\&#93;

The terms involving the new pair \((A_r,B_r)\) form the fixed
\(K_0\)-linear map

\&#91;
\mathscr D_r(A_r,B_r)=
(2-r)A_rB_0'-3A_r'B_0
+2A_0B_r'+(r-3)A_0'B_r. \tag{3.3}
\&#93;

All remaining terms depend only on lower layers. Thus each stage consists of
exact linear algebra over the fixed field \(K_0\), followed by compatibility
polynomials in previously introduced kernel parameters.

For a monomial \(x^a y^b\), its deficiencies are

\&#91;
d_P(a,b)=b-2a+2,\qquad d_Q(a,b)=b-2a+3. \tag{3.4}
\&#93;

The replay generates every lattice point of the two polygons and sorts it by
(3.4). No archived layer matrix is an input.

## 4. Truncated root

The truncated support contains `25` possible `P` monomials and `47` possible
`Q` monomials. Its exact layer data are

| layer | source columns | target rows | rank | kernel dimension | nonzero compatibility equations |
|---:|---:|---:|---:|---:|---:|
| 1 | 19 | 18 | 17 | 2 | 0 |
| 2 | 21 | 19 | 18 | 3 | 0 |
| 3 | 13 | 20 | 12 | 1 | 7 |
| 4 | 0 | 20 | 0 | 0 | 18 |
| 5 | 0 | 21 | 0 | 0 | 0 |

Choose kernel coordinates

\&#91;
X,Y,U,V,W,D
\&#93;

of weights

\&#91;
1,1,2,2,2,3.
\&#93;

The two coordinates `U,D` represent the two split origin vertices. The replay
checks that they do not occur in any compatibility equation. The effective
obstruction variables are therefore

\&#91;
X,Y,V,W
\&#93;

with weights \(1,1,2,2\).

There are fourteen monomials of weighted degree four:

\&#91;
\begin{gathered}
X^4,X^3Y,X^2Y^2,XY^3,Y^4,\\
X^2V,XYV,Y^2V,X^2W,XYW,Y^2W,V^2,VW,W^2.
\end{gathered}
\&#93;

Adjoin to the eighteen layer-four equations the seven layer-three equations
multiplied by `X` and by `Y`. The resulting `32 x 14` Macaulay matrix has rank
`14` over \(K_0\). Its independently reconstructed selected-minor digest is

```text
8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059
```

Thus the obstruction ideal contains every weighted-degree-four monomial. In
particular

\&#91;
X^4,Y^4,V^2,W^2\in I,
\&#93;

so

\&#91;
X,Y,V,W\in\sqrt I. \tag{4.1}
\&#93;

The required top coefficients at `(8,16)` in `P` and `(12,24)` in `Q` are
positive-weight polynomials in these four variables and have no constant
term. Equation (4.1) therefore forces both top coefficients to vanish at
every geometric solution. Exactness of the truncated Newton polygons requires
both coefficients to be nonzero. This contradiction is independent of the
free origin-vertex coordinates `U,D`.

### Conclusion 4.2

The exact truncated-root constructible locus is empty. It is therefore a
terminal-empty queue node, not an open status item.

## 5. Full root through layer four

The full support contains `61` possible `P` monomials and `125` possible `Q`
monomials. The complete layer data are

| layer | source columns | target rows | rank | kernel dimension | nonzero compatibility equations |
|---:|---:|---:|---:|---:|---:|
| 1 | 19 | 18 | 17 | 2 | 0 |
| 2 | 21 | 19 | 18 | 3 | 0 |
| 3 | 21 | 20 | 18 | 3 | 0 |
| 4 | 19 | 20 | 18 | 1 | 2 |
| 5 | 17 | 21 | 17 | 0 | 2 |
| 6 | 15 | 20 | 15 | 0 | 4 |
| 7 | 13 | 19 | 13 | 0 | 5 |
| 8 | 11 | 18 | 11 | 0 | 6 |

Use raw kernel coordinates

\&#91;
(t_{1,0},t_{1,1},U,t_{2,1},t_{2,2},D,t_{3,1},t_{3,2},t_{4,0})
\&#93;

of weights

\&#91;
(1,1,2,2,2,3,3,3,4). \tag{5.1}
\&#93;

Again `U,D` are the split origin-vertex parameters and do not occur in any
compatibility equation.

The two nonzero layer-four compatibility polynomials are scalar multiples of
one polynomial. After unit normalization, that polynomial is

\&#91;
L^2,
\qquad
L=t_{2,2}-\alpha t_{1,1}^2, \tag{5.2}
\&#93;

for an explicitly reconstructed nonzero \(\alpha\in K_0\).

### Scheme versus reduced support

The scheme cut out at layer four contains the double hyperplane

\&#91;
\operatorname{Spec}K_0&#91;\mathbf t&#93;/(L^2).
\&#93;

It is not replaced scheme-theoretically by \((L)\). For the theorem sought
here, however, the target statement is geometric emptiness, and

\&#91;
V(L^2)=V(L)
\&#93;

as sets over an algebraic closure. The queue therefore stores two separate
nodes:

1. the nonreduced square scheme, carrying the multiplicity information; and
2. its reduced support, used only for point-set routing.

No claim about equality of schemes is made.

## 6. Exact-support complements and normalization

On the reduced support \(L=0\), the required top-vertex coefficients become

\&#91;
&#91;P&#93;_{(8,16)}=c_Pt_{1,1}^2,
\qquad
&#91;Q&#93;_{(12,24)}=c_Qt_{1,1}^3, \tag{6.1}
\&#93;

where the replay verifies \(c_P,c_Q\in K_0^\times\).

Therefore the exhaustive split

\&#91;
V(L)=V(L,t_{1,1})\ \cup\ \bigl(V(L)\cap D(t_{1,1})\bigr) \tag{6.2}
\&#93;

has the following dispositions.

- On `t1_1=0`, both coefficients in (6.1) vanish, contradicting exact support.
  This closed child is empty.
- On `t1_1!=0`, normalization is legitimate.

The origin-vertex parameters `U,D` are also required nonzero by exactness of
the declared full support. Their zero loci are not points of the parent exact
root; equivalently, they are saturation factors defining that root. Since
neither variable enters a compatibility equation, no hidden equation branch
is lost by retaining them as free units.

The reconstruction stops at deficiency eight because the fifteen equations
already arise there. It therefore forgets `3` possible `P` coefficients and
`28` possible `Q` coefficients of higher deficiency, including the extra
full-support vertices `(0,8)` and `(0,12)`, of deficiencies `10` and `15`.
None of these coefficients is divided by or set to zero. Every full-support
Keller pair projects to the layer-through-eight necessary-condition locus, so
emptiness of this larger projection excludes every possible choice of the
forgotten coefficients.

Every linear solve before this normalization divides only by a fixed nonzero
element of \(K_0\). Thus no parameter-dependent denominator and no additional
closed child is introduced by Gaussian elimination.

### Weighted cross-section

On `t1_1!=0`, define

\&#91;
\begin{aligned}
U_*&amp;=U/t_{1,1}^2,&amp; D_*&amp;=D/t_{1,1}^3,\\
x&amp;=t_{1,0}/t_{1,1},&amp; a&amp;=t_{2,1}/t_{1,1}^2,\\
b&amp;=t_{3,1}/t_{1,1}^3,&amp; c&amp;=t_{3,2}/t_{1,1}^3,\\
d&amp;=t_{4,0}/t_{1,1}^4.
\end{aligned} \tag{6.3}
\&#93;

The inverse formulas are

\&#91;
\begin{aligned}
U&amp;=t_{1,1}^2U_*,&amp;D&amp;=t_{1,1}^3D_*,\\
t_{1,0}&amp;=t_{1,1}x,&amp;t_{2,1}&amp;=t_{1,1}^2a,\\
t_{2,2}&amp;=\alpha t_{1,1}^2,&amp;t_{3,1}&amp;=t_{1,1}^3b,\\
t_{3,2}&amp;=t_{1,1}^3c,&amp;t_{4,0}&amp;=t_{1,1}^4d.
\end{aligned} \tag{6.4}
\&#93;

The replay verifies that every compatibility polynomial is weighted
homogeneous of its layer number with respect to (5.1). Substitution of (6.4)
therefore factors a nonzero power of `t1_1` from each equation. Consequently,
on the open child, the **layer-through-eight necessary-condition locus** is
isomorphic to

\&#91;
(\mathbf G_m)^3_{U_*,D_*,t_{1,1}}
\times V(F_0,\ldots,F_{14})\subset
(\mathbf G_m)^3\times\mathbf A^5_{x,a,b,c,d}. \tag{6.5}
\&#93;

Every exact full-support solution maps to (6.5); equation (6.5) is not a
parameterization of the forgotten higher-deficiency coefficients. The
weight-one coordinate `t1_1` also makes the corresponding scaling action free;
no finite stabilizer or quotient-descent issue is hidden in the early-layer
cross-section.

## 7. Reconstruction of the fifteen equations

Continuing (3.2) through layer eight, substituting (6.3), and removing only
nonzero scalar duplicates gives

\&#91;
1,3,5,6
\&#93;

distinct equations of weights

\&#91;
5,6,7,8,
\&#93;

respectively. In the replay order these are

\&#91;
F_0,F_1,\ldots,F_{14}\in K_0&#91;x,a,b,c,d&#93;.
\&#93;

Their canonical JSON digest is

```text
d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883
```

which equals the public expected digest. The replay exports a separate digest,
weight, and term count for every `F_i`; these data are pinned in
`stage-manifest.json`.

Equation normalization at this stage divides only by fixed nonzero leading
coefficients in \(K_0\). It creates no geometric complement.

## 8. Direct compact-terminal attachment

Let

\&#91;
I_{15}=(F_0,\ldots,F_{14})
\&#93;

and

\&#91;
J_6=(F_4,F_6,F_8,F_9,F_{10},F_{11}). \tag{8.1}
\&#93;

The current Program 6 residue-provenance proposition identifies exactly these
zero-based indices. The independent replay selects the same six equations
from its reconstructed ordered list and obtains canonical digest

```text
e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a
```

Because the generators of `J6` are literally among the generators of `I15`,

\&#91;
J_6\subset I_{15}
\quad\Longrightarrow\quad
V(I_{15})\subset V(J_6). \tag{8.2}
\&#93;

The imported compact toric terminal theorem states

\&#91;
V(J_6)(\overline{K_0})=\varnothing. \tag{8.3}
\&#93;

Its recorded proof uses the good fiber `(p,u)=(2053,216)`, mixed volume `296`,
`344` proper toric faces (`270` monomial and `74` saturated-unit faces), and
invertibility of multiplication by `F4`, with determinant `682` modulo `2053`.
The five split-embedding determinant residues are

\&#91;
682,116,337,242,740,
\&#93;

with norm product `51` modulo `2053`.

Combining (8.2) and (8.3) gives

\&#91;
V(I_{15})(\overline{K_0})=\varnothing.
\&#93;

Together with (6.5), this proves that the open early-layer `t1_1!=0` child is
empty. The closed child was already empty by (6.1). Every full-support
completion projects to one of these children, so the full root is empty.

This also proves emptiness of the full layer-through-eight obstruction scheme
in which the layer-four equation is retained as `L^2`, rather than only the
corresponding reduced obstruction scheme. If that full finite-type coordinate
algebra over `K0` were nonzero, faithfully flat base change to `overline(K0)`
would remain nonzero, and a nonzero finite-type algebra over an algebraically
closed field has a maximal ideal. That would produce a geometric point on the
reduced full obstruction locus, contrary to the preceding emptiness. Hence
the full obstruction scheme is zero while the square multiplicity has still
been preserved in the manifest. The layer-four hypersurface `L^2=0` alone is
not claimed empty.

### What is and is not replayed here

The coefficientwise identity of the six selected equations is independently
replayed. The large toric matrices and face-saturation archive underlying
(8.3) are not bundled or independently regenerated here; (8.3) is an explicit
imported exact theorem.

## 9. Attempted Lane 9 bridge

The stored adjacent-chart layer-five-through-seven system has an exact
terminal certificate. To use it as a child of the full root, however, one
needs a covering rechart theorem.

For the proposed bare shear

\&#91;
Y'=Y+\lambda X^{-k}
\&#93;

in lower-face coordinates \(t=Y\), \(z=XY^2\), one has \(X=z/t^2\), hence

\&#91;
Y'=t+\lambda(t^2/z)^k=t(1+h),
\qquad
h=\lambda t^{2k-1}z^{-k}, \tag{9.1}
\&#93;

and

\&#91;
z'=X(Y')^2=z(1+h)^2. \tag{9.2}
\&#93;

For `k=4`, the first nonzero normal term has order

\&#91;
2k-1=7. \tag{9.3}
\&#93;

A filtration-preserving conjugacy inducing an invertible associated-graded map
cannot move a nonzero leading symbol from order seven to order four. Thus the
bare `k=4` shear does not identify the one-dimensional layer-four residual
with the stored transformed system.

This is a useful negative Lane 9 lemma, not a covering theorem. The queue
therefore records the adjacent terminal and a noncovering candidate edge, but
no full-root closure path uses that edge.

The weaker theorem sufficient for Lane 8 is instead the direct attachment in
Section 8. It closes the full root without any chart transition.

## 10. Complement and denominator ledger

| Stage | Factor or division | Type | Complement disposition |
|---|---|---|---|
| Face reconstruction | displayed integer relation coefficients and `1+2d` | fixed nonzero scalars | no geometric complement |
| Layer solves `1`--`8` | RREF pivots | fixed nonzero elements of `K0` | no geometric complement |
| Exact support | `U,D` | saturation factors defining the declared origin vertices | zero loci lower the support and are outside the exact-root parent |
| Higher-deficiency coefficients | none | forgotten by the necessary-condition projection | both zero and nonzero values are covered; no localization occurs |
| Layer-four support | `L^2` versus `L` | nilpotent scheme structure | square retained; radical used only for geometric emptiness |
| Normalization | `t1_1` | geometric localization | closed child `t1_1=0` is empty by the two top vertices |
| Equation normalization | one coefficient of each nonzero equation | fixed nonzero element of `K0` | no geometric complement |
| Toric projection | none | generator deletion/relaxation | no complement; inclusion direction is (8.2) |
| Stored adjacent terminal | `D(x)=0` or `D(x)!=0` | internal stored split | both stored children certified, but no covering edge from the full root |
| Bare wall shear | Laurent factor `z^-4` | adjacent Laurent chart | not used in the direct Lane 8 proof |

Thus every parameter-dependent division in the direct full-root path has an
explicit complementary child, and that child is independently eliminated.

## 11. Below-`125` corollary

The literature import recorded in the Lane 8 packet has the following logical
form, after exchanging coordinates when necessary and passing to an algebraic
closure:

1. GGHV Theorem 2.1 leaves the degree pair `(72,108)` below `125`;
2. the `(9,27)` complete-chain case is excluded by the imported Proposition
   4.1/Corollary 5.7 route; and
3. GGHV Proposition 4.3 sends the remaining `(8,28)` case to exactly the
   truncated or full normalized support used above.

Sections 4 and 8 eliminate those two roots. Therefore the imported reduction
has no surviving child.

### Corollary 11.1

Relative to the cited GGHV reduction and the current Program 6 exact terminal
theorem, there is no characteristic-zero plane Keller counterexample with

\&#91;
\max(\deg P,\deg Q)&lt;125.
\&#93;

Polynomial invertibility descends along the faithfully flat extension from a
characteristic-zero base field to its algebraic closure: an isomorphism of the
base-changed affine coordinate algebras, together with its unique inverse, is
fpqc descent data. Thus it is sufficient to exclude the normalized loci over
algebraic closures.

This corollary is a proof assembly with explicit imports. It is not a new
priority claim for the `125` bound, an independent reconstruction of the
literature reduction, or a substitute for specialist review of the imported
toric theorem.
</code></pre>

## `lane8-full-root-closure-20260803-v1/independent_raw_support_replay.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Independently rebuild both Lane 8 roots from raw Newton supports.

The replay uses the published support polygons, the exact degree-21 face
relations, and the coefficient formula for a polynomial Jacobian bracket. It
does not consume archived layer matrices or archived obstruction equations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from lane8_replay.certificates import analyze_full, analyze_truncated, write_json
from lane8_replay.model import FIELD_POLYNOMIAL, FULL, TRUNCATED, build_face, run_layers

SCRIPT_DIR = Path(__file__).resolve().parent


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--relations",
        type=Path,
        default=(
            SCRIPT_DIR / "fixtures" / "belyi_exact_field_relations.json"
        ),
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="write only summary.json after performing the complete exact reconstruction",
    )
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)

    p, q = build_face(args.relations)
    truncated = run_layers(TRUNCATED, p, q)
    full = run_layers(FULL, p, q)
    truncated_summary = analyze_truncated(truncated)
    full_summary, full_equations, legacy, selected = analyze_full(full)

    args.output.mkdir(parents=True)
    if not args.summary_only:
        write_json(args.output / "full_equations.json", full_equations)
        write_json(args.output / "full_exact_fivevar_w8.json", legacy)
        write_json(args.output / "full_terminal_projection.json", selected)
    summary = {
        "schema": "lane8-independent-raw-support-replay-v1",
        "field": {
            "minimal_polynomial": FIELD_POLYNOMIAL,
            "basis": &#91;"1", "u", "u^2", "u^3", "u^4"&#93;,
            "irreducible_over_Q": True,
            "irreducibility_witness": {"prime": 67, "method": "Rabin test"},
        },
        "inputs": {
            "relations_file_sha256": hashlib.sha256(args.relations.read_bytes()).hexdigest(),
            "archived_layers_used": False,
            "archived_equations_used": False,
        },
        "face": {
            "p_degree": len(p) - 1,
            "q_degree": len(q) - 1,
            "jacobian_coefficients_verified": 18,
            "endpoint_coefficients_nonzero": True,
        },
        "truncated": truncated_summary,
        "full": full_summary,
        "public_expected": {
            "truncated_minor_determinant_sha256": "8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059",
            "full_equation_sha256": "d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883",
        },
    }
    summary&#91;"matches_public_expected"&#93; = {
        "truncated_minor": truncated_summary&#91;"minor_determinant_sha256"&#93;
        == summary&#91;"public_expected"&#93;&#91;"truncated_minor_determinant_sha256"&#93;,
        "full_equations": full_summary&#91;"final_equation_sha256"&#93;
        == summary&#91;"public_expected"&#93;&#91;"full_equation_sha256"&#93;,
    }
    if not all(summary&#91;"matches_public_expected"&#93;.values()):
        raise AssertionError(summary&#91;"matches_public_expected"&#93;)
    write_json(args.output / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `lane8-full-root-closure-20260803-v1/verify_lane8_packet.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Fail-closed validation entrypoint for contribution JCG-C-0015."""
from lane8_validator.main import cli

if __name__ == "__main__":
    cli()
</code></pre>

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

## `planar-descent-no-go-20260802-v1/README.md`

<pre><code class="language-markdown">
# Planar descent from the known higher-dimensional examples

&gt; **Status: incomplete proof strategy — not a proof of the planar Jacobian
&gt; conjecture.**

This packet tests a possible route to the planar Jacobian conjecture: descend
one of the known higher-dimensional noninjective constant-Jacobian or
constant-Hessian examples to dimension two, then remove the ramification
introduced by the descent.  The supplied calculations rule out several
natural versions of the first step.  They do not supply the missing global
descent theorem or a way to remove the branch factor.

## Proposed proof route

For a minimal plane Keller counterexample, run the normalized Newton reduction
to a terminal complete-chain system.  The desired global theorem would say
that every terminal system has one of two outcomes:

1. it cannot have simultaneous finite polynomial support in the two adjacent
   boundary charts; or
2. it comes from an admissible polynomial approximate-root operation that
   strictly lowers the chosen Newton complexity.

Together with an exhaustive starting reduction and termination, this would
exclude a minimal counterexample.  Lane 8 owns the exhaustive Newton queue and
terminal systems; Lane 9 owns the adjacent-chart correspondence and polynomial
descent step.

## Exact evidence supplied

For the displayed three-dimensional Keller map, the scripts check:

- its invariant quotient has Jacobian `-2*C^2`, and in affine-modification
  coordinates the residual Jacobian is `2*c`;
- no affine source plane followed by a rank-two linear target projection gives
  a planar counterexample—the only Keller restriction is triangular;
- no polynomial graph over any coordinate plane followed by a rank-two linear
  target projection is Keller; and
- no nonzero linear target combination is a source coordinate, using the
  recorded generic-fibre calculation.

For the displayed five-variable constant-Hessian example, the scripts check:

- there is no second constant linear Schur direction;
- no affine hyperplane through the recorded collision yields a four-variable
  nonzero constant-Hessian restriction;
- the birational near-descent is a planar fold with Hessian determinant
  `64*s^2`; and
- the displayed six-parameter square correction cannot make that determinant
  a nonzero constant.

These are exact, sharply bounded no-go calculations.  They show that
noninjectivity can survive while a boundary or fold factor remains.  They do
not show that all possible descents fail.

## Missing proof obligations

- Prove—or replace—the imported reduction from a hypothetical planar Keller
  counterexample to the normalized support queue.
- Prove that the queue routes every saturation complement, coefficient branch,
  and rechart and terminates in the stated systems.
- Construct the actual adjacent complete-chain charts and prove simultaneous
  two-sided finite support is impossible, or identify an admissible
  complexity-lowering operation.
- Show that every possible higher-dimensional descent is covered by an
  invariant class broad enough to matter; the affine-plane, polynomial-graph,
  linear-projection, and displayed square-correction families are not
  exhaustive.
- Verify the literature attributions and the source formulas independently
  before treating the no-go statements as publication-ready results.

## Reproducible checks

- `three_dimensional_descent_no_go.py`
- `affine_plane_linear_projection_no_go.py`
- `y_graph_descent_no_go.py`
- `linear_target_coordinate_fibres.py`
- `hc4_linear_descent_no_go.py`
- `hc4_square_correction_no_go.py`

All six scripts use exact SymPy arithmetic.  A successful replay establishes
only the identities and finite coefficient eliminations encoded in that
script; it does not establish the proposed global proof route.
</code></pre>

## `planar-descent-no-go-20260802-v1/three_dimensional_descent_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checks for simple planar descents of the 2026 three-dimensional Keller map.

This script proves/checks three sharply scoped statements.

1. The G_m-invariant quotient is a polynomial map A^2 -&gt; A^2 whose
   Jacobian is -2 times the square of the contracted invariant.
2. After a birational monomial simplification it is the cubic cover
       s^3 - 2 s^2 + P s - 2 Q = 0,
   but its planar Jacobian still has the unavoidable branch factor.
3. For every polynomial graph z=h(x,y), and every rank-two linear target
   projection, the induced map A^2 -&gt; A^2 cannot have nonzero constant
   Jacobian.  The proof is degree-theoretic and valid for arbitrary degree h.

The script uses exact symbolic arithmetic only.
"""
from __future__ import annotations

import sympy as sp

x, y, z = sp.symbols("x y z")
u = 1 + x * y
F1 = sp.expand(u**3 * z + y**2 * u * (4 + 3 * x * y))
F2 = sp.expand(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
F3 = sp.expand(2 * x - 3 * x**2 * y - x**3 * z)

# ---------------------------------------------------------------------------
# 1. Coarse G_m quotient.
# ---------------------------------------------------------------------------
a, b = sp.symbols("a b")
uq = 1 + a
X = sp.expand(uq**3 * b + a**2 * uq * (4 + 3 * a))
C = 2 - 3 * a - b
D = sp.expand(a + 3 * uq**2 * b + 3 * a**2 * (4 + 3 * a))
P = sp.expand(X * C**2)
Q = sp.expand(D * C)
Jquot = sp.factor(sp.det(sp.Matrix(&#91;
    &#91;sp.diff(P, a), sp.diff(P, b)&#93;,
    &#91;sp.diff(Q, a), sp.diff(Q, b)&#93;,
&#93;)))
assert sp.expand(Jquot + 2 * C**2) == 0

# A useful affine-modification coordinate.  Set r=a+1 and p=C*r.
r, c, p = sp.symbols("r c p")
Xrc = sp.expand(-c * r**3 + r**2 + r)
Drc = sp.expand(-3 * c * r**2 + 4 * r + 2)
Ppc = sp.expand((c**2 * Xrc).subs(r, p / c))
Qpc = sp.expand((c * Drc).subs(r, p / c))
assert Ppc == -p**3 + p**2 + c * p
assert Qpc == -3 * p**2 + 4 * p + 2 * c
Jpc = sp.factor(sp.det(sp.Matrix(&#91;
    &#91;sp.diff(Ppc, p), sp.diff(Ppc, c)&#93;,
    &#91;sp.diff(Qpc, p), sp.diff(Qpc, c)&#93;,
&#93;)))
assert Jpc == 2 * c
s = sp.symbols("s")
c_from_Q = sp.expand((Qpc + 3 * p**2 - 4 * p) / 2)
cubic = sp.expand(p**3 - 2 * p**2 + Qpc * p - 2 * Ppc)
assert cubic == 0

# ---------------------------------------------------------------------------
# 2. Polynomial graph z=h(x,y), arbitrary linear target projection.
# ---------------------------------------------------------------------------
H, Hx, Hy = sp.symbols("H Hx Hy")
hfun = sp.Function("h")(x, y)
Fs = &#91;F1, F2, F3&#93;


def graph_jacobian(i: int, j: int) -&gt; sp.Expr:
    fi = Fs&#91;i&#93;.subs(z, hfun)
    fj = Fs&#91;j&#93;.subs(z, hfun)
    jac = sp.det(sp.Matrix(&#91;
        &#91;sp.diff(fi, x), sp.diff(fi, y)&#93;,
        &#91;sp.diff(fj, x), sp.diff(fj, y)&#93;,
    &#93;))
    return sp.expand(jac.subs({
        hfun: H,
        sp.diff(hfun, x): Hx,
        sp.diff(hfun, y): Hy,
    }))


J12 = graph_jacobian(0, 1)
J13 = graph_jacobian(0, 2)
J23 = graph_jacobian(1, 2)

# The unique top-degree quadratic-in-h pieces.  If h_d is the leading
# homogeneous form of a nonconstant h, these become the leading homogeneous
# terms of the restricted Jacobians.
expected_top_12 = -3 * x * (x * y) ** 4 * H * (3 * H + x * Hx)
expected_top_13 = 3 * x**3 * (x * y) ** 2 * H * (3 * H + x * Hx)
expected_top_23 = 6 * x**4 * (x * y) * H * (3 * H + x * Hx)


def quadratic_part(expr: sp.Expr) -&gt; sp.Expr:
    # Degree two when H and either derivative are assigned degree one.
    poly = sp.Poly(expr, H, Hx, Hy)
    out = 0
    for (e_h, e_hx, e_hy), coeff in poly.terms():
        if e_h + e_hx + e_hy == 2:
            out += coeff * H**e_h * Hx**e_hx * Hy**e_hy
    return sp.expand(out)


q12 = quadratic_part(J12)
q13 = quadratic_part(J13)
q23 = quadratic_part(J23)

# Each quadratic part also has lower total (x,y)-degree terms involving Hy;
# extract the highest x,y-degree coefficient to verify the formulas above.
def leading_after_homogeneous_substitution(expr: sp.Expr) -&gt; sp.Expr:
    """Terms of maximal total degree after H-&gt;h_d and dH-&gt;degree d-1."""
    poly = sp.Poly(expr, x, y, H, Hx, Hy)
    score = lambda mon: mon&#91;0&#93; + mon&#91;1&#93; - mon&#91;3&#93; - mon&#91;4&#93;
    max_score = max(score(mon) for mon, _ in poly.terms())
    out = 0
    for mon, coeff in poly.terms():
        ex, ey, e_h, e_hx, e_hy = mon
        if score(mon) == max_score:
            out += coeff * x**ex * y**ey * H**e_h * Hx**e_hx * Hy**e_hy
    return sp.expand(out)


assert sp.expand(leading_after_homogeneous_substitution(q12) - expected_top_12) == 0
assert sp.expand(leading_after_homogeneous_substitution(q13) - expected_top_13) == 0
assert sp.expand(leading_after_homogeneous_substitution(q23) - expected_top_23) == 0

# Explanation encoded as a check: if h_d=sum c_i x^i y^(d-i), the equation
# x*d_x h_d=-3 h_d has no nonzero polynomial solution because every exponent
# i is a nonnegative integer.  We verify this coefficientwise for a symbolic
# generic degree d up to a representative range; the written proof is uniform.
for degree in range(1, 13):
    coeffs = sp.symbols(f"t0:{degree + 1}")
    hd = sum(coeffs&#91;i&#93; * x**i * y**(degree - i) for i in range(degree + 1))
    relation = sp.Poly(sp.expand(x * sp.diff(hd, x) + 3 * hd), x, y)
    for i in range(degree + 1):
        assert relation.coeff_monomial(x**i * y**(degree-i)) == (i+3)*coeffs&#91;i&#93;
    # Solving the diagonal equations gives all zero.
    diagonal = &#91;sp.expand((i + 3) * coeffs&#91;i&#93;) for i in range(degree + 1)&#93;
    assert sp.solve(diagonal, coeffs, dict=True) == &#91;dict(zip(coeffs, &#91;0&#93; * len(coeffs)))&#93;

# Constant h cannot work either.  The coefficients x^3 y^6, x^3 y^4,
# and x^3 y^3 successively kill the three Pluecker coordinates.
h0, lam12, lam13, lam23, kappa = sp.symbols(
    "h0 lam12 lam13 lam23 kappa"
)
const_combination = sp.Poly(
    sp.expand(
        lam12 * J12.subs({H: h0, Hx: 0, Hy: 0})
        + lam13 * J13.subs({H: h0, Hx: 0, Hy: 0})
        + lam23 * J23.subs({H: h0, Hx: 0, Hy: 0})
        - kappa
    ),
    x,
    y,
)
assert const_combination.coeff_monomial(x**3 * y**6) == -54 * lam12
assert sp.expand(
    const_combination.coeff_monomial(x**3 * y**4).subs(lam12, 0)
) == 54 * lam13
assert sp.expand(
    const_combination.coeff_monomial(x**3 * y**3).subs({lam12: 0, lam13: 0})
) == 108 * lam23

print("3D Keller map determinant: -2 (source formula imported from the paper)")
print(f"Coarse quotient Jacobian: {Jquot}")
print(f"Affine-modification quotient Jacobian: {Jpc}")
print("Fiber cubic: p^3 - 2 p^2 + Q p - 2 P = 0")
print("Polynomial z-graph + linear target projection: NO Keller descent")

# ---------------------------------------------------------------------------
# 3. Polynomial graph x=g(y,z), arbitrary linear target projection.
#    The only Keller case is the trivial plane x=0, where the restriction is
#    the triangular automorphism (y,z)-&gt;(z+4y^2,y) up to a linear target map.
# ---------------------------------------------------------------------------
G, Gy, Gz = sp.symbols("G Gy Gz")
gfun = sp.Function("g")(y, z)


def x_graph_jacobian(i: int, j: int) -&gt; sp.Expr:
    fi = Fs&#91;i&#93;.subs(x, gfun)
    fj = Fs&#91;j&#93;.subs(x, gfun)
    jac = sp.det(sp.Matrix(&#91;
        &#91;sp.diff(fi, y), sp.diff(fi, z)&#93;,
        &#91;sp.diff(fj, y), sp.diff(fj, z)&#93;,
    &#93;))
    return sp.expand(jac.subs({
        gfun: G,
        sp.diff(gfun, y): Gy,
        sp.diff(gfun, z): Gz,
    }))


K12 = x_graph_jacobian(0, 1)
K13 = x_graph_jacobian(0, 2)
K23 = x_graph_jacobian(1, 2)
expected_k12 = 3 * G**5 * y**4 * z * (G + 3 * z * Gz)
expected_k13 = -3 * G**5 * y**2 * z * (G + 3 * z * Gz)
expected_k23 = -6 * G**5 * y * z * (G + 3 * z * Gz)


def leading_g_degree(expr: sp.Expr) -&gt; sp.Expr:
    """Highest degree after G-&gt;g_d, dG-&gt;degree d-1, for any d&gt;=1."""
    poly = sp.Poly(expr, y, z, G, Gy, Gz)
    # total after substitution is d*(eG+eGy+eGz)+base-eGy-eGz.
    # Lexicographically maximize slope then intercept, valid uniformly d&gt;=1
    # here because the unique slope-six block also has maximal intercept.
    data = &#91;&#93;
    for mon, coeff in poly.terms():
        ey, ez, eG, eGy, eGz = mon
        slope = eG + eGy + eGz
        intercept = ey + ez - eGy - eGz
        data.append((slope, intercept, mon, coeff))
    max_slope = max(item&#91;0&#93; for item in data)
    max_intercept = max(item&#91;1&#93; for item in data if item&#91;0&#93; == max_slope)
    out = 0
    for slope, intercept, mon, coeff in data:
        if slope == max_slope and intercept == max_intercept:
            ey, ez, eG, eGy, eGz = mon
            out += coeff * y**ey * z**ez * G**eG * Gy**eGy * Gz**eGz
    return sp.expand(out)


assert sp.expand(leading_g_degree(K12) - expected_k12) == 0
assert sp.expand(leading_g_degree(K13) - expected_k13) == 0
assert sp.expand(leading_g_degree(K23) - expected_k23) == 0

# The equation g_d+3 z*d_z g_d=0 has no nonzero homogeneous polynomial
# solution: the coefficient of y^(d-j)z^j is multiplied by 1+3j.
for degree in range(1, 13):
    coeffs = sp.symbols(f"q0:{degree + 1}")
    gd = sum(coeffs&#91;j&#93; * y**(degree-j) * z**j for j in range(degree + 1))
    relation = sp.Poly(sp.expand(gd + 3*z*sp.diff(gd,z)), y, z)
    for j in range(degree+1):
        assert relation.coeff_monomial(y**(degree-j)*z**j) == (1+3*j)*coeffs&#91;j&#93;

# Constants: c!=0 is killed successively by y^4 z, y^2 z, yz; c=0
# leaves K12=-1 and K13=K23=0.
g0 = sp.symbols("g0")
assert sp.Poly(K12.subs({G:g0,Gy:0,Gz:0}),y,z).coeff_monomial(y**4*z) == 3*g0**6
assert sp.Poly(K13.subs({G:g0,Gy:0,Gz:0}),y,z).coeff_monomial(y**2*z) == -3*g0**6
assert sp.Poly(K23.subs({G:g0,Gy:0,Gz:0}),y,z).coeff_monomial(y*z) == -6*g0**6
assert K12.subs({G:0,Gy:0,Gz:0}) == -1
assert K13.subs({G:0,Gy:0,Gz:0}) == 0
assert K23.subs({G:0,Gy:0,Gz:0}) == 0
print("Polynomial x-graph + linear target projection: only x=0, a triangular automorphism")
</code></pre>

## `planar-descent-no-go-20260802-v1/affine_plane_linear_projection_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Classify all affine-plane / linear-projection descents of the 2026 JC_3 map.

Let F:A^3-&gt;A^3 be the explicit Keller counterexample.  Let

    S={m_1 x+m_2 y+m_3 z=d}

be an affine source plane, and let pi:A^3-&gt;A^2 be a rank-two linear map with
kernel direction k.  Up to fixed nonzero choices of volume forms, the Jacobian
of pi o F|_S is

    R_{m,k}=m^T adj(JF) k   modulo (m.X-d).

The exact coefficient calculation below proves:

* R_{m,k} cannot be a nonzero constant unless S={x=0};
* on S={x=0}, nonzero constant Jacobian occurs precisely when the target
  projection is nondegenerate on the first two target coordinates;
* every such restriction is a linear target change of
      (y,z) -&gt; (z+4y^2,y),
  hence a polynomial automorphism.

Therefore this entire descent class contains no planar counterexample.
"""
from __future__ import annotations

import sympy as sp

x, y, z = sp.symbols("x y z")
u = 1 + x*y
F1 = sp.expand(u**3*z + y**2*u*(4+3*x*y))
F2 = sp.expand(y + 3*x*u**2*z + 3*x*y**2*(4+3*x*y))
F3 = sp.expand(2*x - 3*x**2*y - x**3*z)
F = (F1,F2,F3)
JF = sp.Matrix(&#91;&#91;sp.diff(fi,v) for v in (x,y,z)&#93; for fi in F&#93;)
assert sp.factor(JF.det()) == -2
Adj = JF.adjugate()
k1,k2,k3 = sp.symbols("k1 k2 k3")
k = sp.Matrix(&#91;k1,k2,k3&#93;)

# Case I: m3 != 0.  Normalize m=(a,b,1), z=d-a*x-b*y.
a,b,d = sp.symbols("a b d")
m = sp.Matrix(&#91;&#91;a,b,1&#93;&#93;)
R = sp.expand((m*Adj*k)&#91;0&#93;.subs(z,d-a*x-b*y))
P = sp.Poly(R,x,y)
assert P.coeff_monomial(y**3) == -89*k3
assert sp.expand(P.coeff_monomial(x*y**2).subs(k3,0)) == -6*k2
assert sp.expand(P.coeff_monomial(x*y).subs({k3:0,k2:0})) == -42*k1

# Case II: m3=0,m2 != 0. Normalize m=(a,1,0), y=d-a*x.
a,d = sp.symbols("a d")
m = sp.Matrix(&#91;&#91;a,1,0&#93;&#93;)
R = sp.expand((m*Adj*k)&#91;0&#93;.subs(y,d-a*x))
P = sp.Poly(R,x,z)
assert P.coeff_monomial(z) == 3*k3
assert sp.expand(P.coeff_monomial(x**2*z).subs(k3,0)) == 3*k2
assert sp.expand(P.coeff_monomial(x).subs({k3:0,k2:0})) == 6*k1

# Case III: m3=m2=0. Normalize m=(1,0,0), x=d.
d = sp.symbols("d")
m = sp.Matrix(&#91;&#91;1,0,0&#93;&#93;)
R = sp.expand((m*Adj*k)&#91;0&#93;.subs(x,d))
P = sp.Poly(R,y,z)
assert P.coeff_monomial(y**3*z) == 12*d**5*k3
assert sp.expand(P.coeff_monomial(y**3).subs(k3,0)) == 9*d**5*k2
assert sp.expand(P.coeff_monomial(y).subs({k3:0,k2:0})) == -6*d**4*k1
# At d=0 every nonconstant coefficient vanishes, and the constant is -k3.
for mon,coeff in P.terms():
    if mon != (0,0):
        assert sp.expand(coeff.subs(d,0)) == 0
assert sp.expand(P.coeff_monomial(1).subs(d,0)) == -k3

# The exceptional restriction is triangular.
assert sp.expand(F1.subs(x,0) - (z+4*y**2)) == 0
assert F2.subs(x,0) == y
assert F3.subs(x,0) == 0
assert sp.det(sp.Matrix(&#91;
    &#91;sp.diff(F1.subs(x,0),y),sp.diff(F1.subs(x,0),z)&#93;,
    &#91;sp.diff(F2.subs(x,0),y),sp.diff(F2.subs(x,0),z)&#93;,
&#93;)) == -1

print("Case m3!=0: y^3, x*y^2, x*y force k3=k2=k1=0")
print("Case m3=0,m2!=0: z, x^2*z, x force k3=k2=k1=0")
print("Case m=(1,0,0), d!=0: y^3*z, y^3, y force k3=k2=k1=0")
print("Exceptional plane x=0: restriction (z+4*y^2,y,0), triangular automorphism")
</code></pre>

## `planar-descent-no-go-20260802-v1/y_graph_descent_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""No planar Keller descent from a polynomial graph y=h(x,z).

For the 2026 three-dimensional Keller counterexample F=(F1,F2,F3), this
script computes the three restricted 2x2 Jacobians on y=h(x,z).  It verifies
the degree argument proving that no nonzero Pluecker combination can be a
nonzero constant, for any polynomial h and any rank-two linear target
projection.

Together with three_dimensional_descent_no_go.py, this covers polynomial
graphs over each of the three coordinate planes.
"""
from __future__ import annotations

import sympy as sp

x, y, z = sp.symbols("x y z")
u = 1 + x * y
F1 = sp.expand(u**3 * z + y**2 * u * (4 + 3 * x * y))
F2 = sp.expand(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
F3 = sp.expand(2 * x - 3 * x**2 * y - x**3 * z)
Fs = (F1, F2, F3)

G, Gx, Gz = sp.symbols("G Gx Gz")
gfun = sp.Function("g")(x, z)


def restricted_jacobian(i: int, j: int) -&gt; sp.Expr:
    fi = Fs&#91;i&#93;.subs(y, gfun)
    fj = Fs&#91;j&#93;.subs(y, gfun)
    value = sp.det(sp.Matrix(&#91;
        &#91;sp.diff(fi, x), sp.diff(fi, z)&#93;,
        &#91;sp.diff(fj, x), sp.diff(fj, z)&#93;,
    &#93;))
    return sp.expand(value.subs({
        gfun: G,
        sp.diff(gfun, x): Gx,
        sp.diff(gfun, z): Gz,
    }))


J12 = restricted_jacobian(0, 1)
J13 = restricted_jacobian(0, 2)
J23 = restricted_jacobian(1, 2)


def highest_g_slope(expr: sp.Expr) -&gt; sp.Expr:
    """Highest degree in G,Gx,Gz; ties by actual base-degree intercept."""
    poly = sp.Poly(expr, x, z, G, Gx, Gz)
    data = &#91;&#93;
    for mon, coeff in poly.terms():
        ex, ez, e_g, e_gx, e_gz = mon
        slope = e_g + e_gx + e_gz
        intercept = ex + ez - e_gx - e_gz
        data.append((slope, intercept, mon, coeff))
    max_slope = max(item&#91;0&#93; for item in data)
    max_intercept = max(item&#91;1&#93; for item in data if item&#91;0&#93; == max_slope)
    out = 0
    for slope, intercept, mon, coeff in data:
        if slope == max_slope and intercept == max_intercept:
            ex, ez, e_g, e_gx, e_gz = mon
            out += coeff * x**ex * z**ez * G**e_g * Gx**e_gx * Gz**e_gz
    return sp.expand(out)


assert sp.factor(highest_g_slope(J12)) == -54 * G**6 * Gz * x**3
assert sp.factor(highest_g_slope(J13)) == 54 * G**4 * Gz * x**3
assert sp.factor(highest_g_slope(J23)) == 108 * G**3 * Gz * x**3

# Hence the leading homogeneous form h_d must satisfy d_z h_d=0 whenever
# the corresponding Pluecker coefficient is the first nonzero one.  Thus
# h_d=c*x^d.  Direct substitution gives a nonzero next leading term.  The
# d=1,2 cases are exceptional only in which equal-degree terms tie; d&gt;=3 has
# the uniform monomial listed below.
c = sp.symbols("c", nonzero=True)
expected = {
    1: (
        3 * c**5 * x**10 * z,
        -3 * c**3 * x**8 * z,
        -6 * c**2 * x**7 * z,
    ),
    2: (
        6 * c**5 * x**15 * (3 * c * x + z),
        -6 * c**3 * x**11 * (3 * c * x + z),
        -12 * c**2 * x**9 * (3 * c * x + z),
    ),
}
for degree in (1, 2):
    for expr, target in zip((J12, J13, J23), expected&#91;degree&#93;):
        specialized = sp.Poly(
            sp.expand(expr.subs({
                G: c * x**degree,
                Gx: c * degree * x**(degree - 1),
                Gz: 0,
            })),
            x,
            z,
        )
        top_degree = max(sum(mon) for mon, _ in specialized.terms())
        top = sum(
            coeff * x**mon&#91;0&#93; * z**mon&#91;1&#93;
            for mon, coeff in specialized.terms()
            if sum(mon) == top_degree
        )
        assert sp.expand(top - target) == 0

for degree in range(3, 10):
    targets = (
        9 * degree * c**6 * x**(6 * degree + 4),
        -9 * degree * c**4 * x**(4 * degree + 4),
        -18 * degree * c**3 * x**(3 * degree + 4),
    )
    for expr, target in zip((J12, J13, J23), targets):
        specialized = sp.Poly(
            sp.expand(expr.subs({
                G: c * x**degree,
                Gx: c * degree * x**(degree - 1),
                Gz: 0,
            })),
            x,
            z,
        )
        top_degree = max(sum(mon) for mon, _ in specialized.terms())
        top = sum(
            coeff * x**mon&#91;0&#93; * z**mon&#91;1&#93;
            for mon, coeff in specialized.terms()
            if sum(mon) == top_degree
        )
        assert sp.expand(top - target) == 0

# Constant h: coefficients z, x, and x^2*z successively kill the three
# Pluecker coordinates (the target constant is allowed in the (0,0) term).
h0, l12, l13, l23 = sp.symbols("h0 l12 l13 l23")
combination = sp.Poly(sp.expand(
    l12 * J12.subs({G: h0, Gx: 0, Gz: 0})
    + l13 * J13.subs({G: h0, Gx: 0, Gz: 0})
    + l23 * J23.subs({G: h0, Gx: 0, Gz: 0})
), x, z)
assert combination.coeff_monomial(z) == -3 * l12
assert sp.factor(combination.coeff_monomial(x).subs(l12, 0)) == -6 * l23
assert sp.factor(
    combination.coeff_monomial(x**2 * z).subs({l12: 0, l23: 0})
) == 3 * l13

print("y=h(x,z): every nonconstant leading form is excluded by degree")
print("constant h: z, x, x^2*z coefficients force all Pluecker coordinates zero")
print("No polynomial y-graph with a rank-two linear target projection is Keller")
</code></pre>

## `planar-descent-no-go-20260802-v1/linear_target_coordinate_fibres.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Structure of generic fibres of every linear target coordinate.

For H=alpha*F1+beta*F2+gamma*F3 of the 2026 three-dimensional Keller map,
write H=A(x,y)z+B(x,y), and put t=1+xy.  The script verifies

    A = alpha*t^3 + 3*beta*x*t^2 - gamma*x^3,

and, on each hyperbola t=rho*x satisfying

    alpha*rho^3 + 3*beta*rho^2 - gamma = 0,

the restriction

    B = alpha*rho^2 + 4*beta*rho + (alpha*rho+2*beta)/x.

These formulas give a short Euler-characteristic proof that no nonzero
linear combination of F1,F2,F3 is a coordinate polynomial.  The one case
whose generic Euler characteristic is 1 is F1 itself; its generic fibre is
A^2 minus the hyperbola 1+xy=0 and has the nonconstant unit 1+xy.
"""
from __future__ import annotations

import sympy as sp

x, y, z, t, rho = sp.symbols("x y z t rho")
alpha, beta, gamma = sp.symbols("alpha beta gamma")
u = 1 + x * y
F1 = sp.expand(u**3 * z + y**2 * u * (4 + 3 * x * y))
F2 = sp.expand(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
F3 = sp.expand(2 * x - 3 * x**2 * y - x**3 * z)
H = sp.expand(alpha * F1 + beta * F2 + gamma * F3)
A = sp.expand(sp.diff(H, z))
B = sp.expand(H - A * z)

A_t = sp.factor(A.subs(y, (t - 1) / x))
B_t = sp.factor(sp.together(B.subs(y, (t - 1) / x)))
assert A_t == alpha * t**3 + 3 * beta * x * t**2 - gamma * x**3

root_relation = {gamma: alpha * rho**3 + 3 * beta * rho**2}
B_on_component = sp.factor(
    sp.together(B_t.subs(t, rho * x).subs(root_relation))
)
expected = alpha * rho**2 + 4 * beta * rho + (alpha * rho + 2 * beta) / x
assert sp.factor(B_on_component - expected) == 0

# A root component is constant for B exactly when alpha*rho+2*beta=0.
# Such a root is repeated because the derivative of the cubic is
# 3*rho*(alpha*rho+2*beta).
R = alpha * rho**3 + 3 * beta * rho**2 - gamma
assert sp.factor(sp.diff(R, rho)) == 3 * rho * (alpha * rho + 2 * beta)

# Special repeated-root factorizations used in the case split.
b = sp.symbols("b")
assert sp.expand((rho + 2 * b) ** 2 * (rho - b)) == rho**3 + 3 * b * rho**2 - 4 * b**3
assert sp.expand(rho**2 * (rho + 3 * b)) == rho**3 + 3 * b * rho**2

print("A(x,t) = alpha*t^3 + 3*beta*x*t^2 - gamma*x^3")
print("On t=rho*x: B = alpha*rho^2+4*beta*rho+(alpha*rho+2*beta)/x")
print("alpha!=0, not F1: at least one nonconstant G_m component, so chi(generic fibre)&gt;=2")
print("alpha=0,beta!=0: line plus one/two G_m components, so chi(generic fibre)&gt;=2")
print("H=gamma*F3: generic fibre is G_m x A^1")
print("H=alpha*F1: generic fibre has the nonconstant unit 1+x*y")
print("Therefore no nonzero linear target coordinate pulls back to a source coordinate")
</code></pre>

## `planar-descent-no-go-20260802-v1/hc4_linear_descent_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact no-go checks for descending the 5-variable Hessian counterexample to HC_4.

The five-variable potential is the Meng--Yang 2026 counterexample

    Psi = A^2 + 13 A + 2 B.

This script verifies three sharply scoped statements:

1. There is no nonzero constant linear direction c for which the second
   directional derivative c^T Hess(Psi)c is constant.  Hence the published
   one-variable Schur descent cannot simply be repeated after a linear change.
2. No affine linear hyperplane containing the two known collision points
   carries a four-variable restriction with nonzero constant Hessian
   determinant.  The four projective cases are exhausted exactly.
3. A birational partial Schur reduction does produce a polynomial
   four-variable near-example with a two-point gradient collision, but its
   Hessian determinant is 64*s^2.  After a linear change this is just the
   doubled planar fold (s,u)-&gt;((u^2-s^2)/2,4u); the missing constant-Jacobian
   condition is precisely the remaining planar obstruction.

All calculations are exact over Q.  This does not prove HC_4 or JC_2; it rules
out the most direct linear restriction/second-Schur descent of this particular
HC_5 counterexample.
"""
from __future__ import annotations

import itertools
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.rings import ring

# ---------------------------------------------------------------------------
# Source potential and collision.
# ---------------------------------------------------------------------------
x1, x2, y1, y2, y3 = sp.symbols("x1 x2 y1 y2 y3")
u = 1 + x1 * x2
A = y1 * u**3 + 3 * x1 * y2 * u**2 - x1**3 * y3
B = (
    y1 * x2**2 * u * (4 + 3 * x1 * x2)
    + y2 * (x2 + 3 * x1 * x2**2 * (4 + 3 * x1 * x2))
    + y3 * (2 * x1 - 3 * x1**2 * x2)
)
Psi = sp.expand(A**2 + 13 * A + 2 * B)
vars5 = (x1, x2, y1, y2, y3)
P_plus = {x1: 1, x2: -sp.Rational(3, 2), y1: 0, y2: 0, y3: 0}
P_minus = {x1: -1, x2: sp.Rational(3, 2), y1: 0, y2: 0, y3: 0}
grad = &#91;sp.diff(Psi, v) for v in vars5&#93;
assert &#91;g.subs(P_plus) for g in grad&#93; == &#91;g.subs(P_minus) for g in grad&#93;

# ---------------------------------------------------------------------------
# 1. No second constant linear Schur direction.
# ---------------------------------------------------------------------------
H5 = sp.hessian(Psi, vars5)
columns: list&#91;sp.Poly&#93; = &#91;&#93;
for i in range(5):
    for j in range(i, 5):
        entry = H5&#91;i, j&#93; if i == j else 2 * H5&#91;i, j&#93;
        columns.append(sp.Poly(entry, *vars5))
all_monomials = sorted(set().union(*(set(p.monoms()) for p in columns)))
nonconstant_monomials = &#91;m for m in all_monomials if any(m)&#93;
coefficient_matrix = sp.Matrix(&#91;
    &#91;p.coeff_monomial(m) for p in columns&#93;
    for m in nonconstant_monomials
&#93;)
assert coefficient_matrix.shape == (158, 15)
assert coefficient_matrix.rank() == 15

# ---------------------------------------------------------------------------
# Sparse exact determinant helper.
# ---------------------------------------------------------------------------
def permutation_sign(perm: tuple&#91;int, ...&#93;) -&gt; int:
    inversions = sum(
        perm&#91;i&#93; &gt; perm&#91;j&#93;
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def determinant4(R, matrix):
    value = R.zero
    for perm in itertools.permutations(range(4)):
        term = R.one
        for i in range(4):
            term *= matrix&#91;i&#93;&#91;perm&#91;i&#93;&#93;
        value += permutation_sign(perm) * term
    return value

# Every affine hyperplane through P_+ and P_- has equation
#   3*s*x1 + 2*s*x2 + n3*y1+n4*y2+n5*y3=0.
# The four cases below cover projective &#91;s:n3:n4:n5&#93;.

# Case 1: n5 != 0, normalize n5=1.
R1, X1, X2, Y1, Y2, S, aa, bb = ring(
    "x1,x2,y1,y2,s,a,b", QQ
)
Y3 = -(3 * S * X1 + 2 * S * X2 + aa * Y1 + bb * Y2)
U = 1 + X1 * X2
AA = Y1 * U**3 + 3 * X1 * Y2 * U**2 - X1**3 * Y3
BB = (
    Y1 * X2**2 * U * (4 + 3 * X1 * X2)
    + Y2 * (X2 + 3 * X1 * X2**2 * (4 + 3 * X1 * X2))
    + Y3 * (2 * X1 - 3 * X1**2 * X2)
)
PP = AA**2 + 13 * AA + 2 * BB
V = (X1, X2, Y1, Y2)
HH = &#91;&#91;PP.diff(vi).diff(vj) for vj in V&#93; for vi in V&#93;
det1 = determinant4(R1, HH)
assert len(det1.terms()) == 9397
assert det1&#91;(0, 0, 1, 0, 0, 0, 0)&#93; == -36504

# Case 2: n5=0, n4 != 0, normalize n4=1.
R2, X1, X2, Y1, Y3, S, aa = ring("x1,x2,y1,y3,s,a", QQ)
Y2 = -(3 * S * X1 + 2 * S * X2 + aa * Y1)
U = 1 + X1 * X2
AA = Y1 * U**3 + 3 * X1 * Y2 * U**2 - X1**3 * Y3
BB = (
    Y1 * X2**2 * U * (4 + 3 * X1 * X2)
    + Y2 * (X2 + 3 * X1 * X2**2 * (4 + 3 * X1 * X2))
    + Y3 * (2 * X1 - 3 * X1**2 * X2)
)
PP = AA**2 + 13 * AA + 2 * BB
V = (X1, X2, Y1, Y3)
HH = &#91;&#91;PP.diff(vi).diff(vj) for vj in V&#93; for vi in V&#93;
det2 = determinant4(R2, HH)
assert len(det2.terms()) == 3710
assert det2&#91;(0, 0, 1, 0, 0, 0)&#93; == -512

# Case 3: n5=n4=0, n3 != 0, normalize n3=1.
R3, X1, X2, Y2, Y3, S = ring("x1,x2,y2,y3,s", QQ)
Y1 = -(3 * S * X1 + 2 * S * X2)
U = 1 + X1 * X2
AA = Y1 * U**3 + 3 * X1 * Y2 * U**2 - X1**3 * Y3
BB = (
    Y1 * X2**2 * U * (4 + 3 * X1 * X2)
    + Y2 * (X2 + 3 * X1 * X2**2 * (4 + 3 * X1 * X2))
    + Y3 * (2 * X1 - 3 * X1**2 * X2)
)
PP = AA**2 + 13 * AA + 2 * BB
V = (X1, X2, Y2, Y3)
HH = &#91;&#91;PP.diff(vi).diff(vj) for vj in V&#93; for vi in V&#93;
det3 = determinant4(R3, HH)
assert len(det3.terms()) == 950
assert det3&#91;(1, 1, 0, 0, 0)&#93; == 2688

# Case 4: n3=n4=n5=0, hence s != 0; set 3*x1+2*x2=0.
R4, X1, Y1, Y2, Y3 = ring("x1,y1,y2,y3", QQ)
X2 = -QQ(3, 2) * X1
U = 1 + X1 * X2
AA = Y1 * U**3 + 3 * X1 * Y2 * U**2 - X1**3 * Y3
BB = (
    Y1 * X2**2 * U * (4 + 3 * X1 * X2)
    + Y2 * (X2 + 3 * X1 * X2**2 * (4 + 3 * X1 * X2))
    + Y3 * (2 * X1 - 3 * X1**2 * X2)
)
PP = AA**2 + 13 * AA + 2 * BB
V = (X1, Y1, Y2, Y3)
HH = &#91;&#91;PP.diff(vi).diff(vj) for vj in V&#93; for vi in V&#93;
det4 = determinant4(R4, HH)
assert det4 == R4.zero

# ---------------------------------------------------------------------------
# 3. Birational Schur near-descent: a polynomial four-variable fold.
# ---------------------------------------------------------------------------
s, xx, yy, zz = sp.symbols("s x y z")
Phi = sp.expand(
    (
        -16 * s**4 + 48 * s**3 * xx - 36 * s**2 * xx**2
        + 16 * s**2 * yy + 104 * s**2 + 24 * s * xx * yy
        - 156 * s * xx + 48 * s * zz + 8 * xx**2 * yy
        + 32 * xx * zz - 169
    ) / 4
)
vars4 = (s, xx, yy, zz)
assert sp.factor(sp.hessian(Phi, vars4).det()) == 64 * s**2
q_plus = {s: 1, xx: -sp.Rational(3, 2), yy: 0, zz: 0}
q_minus = {s: -1, xx: sp.Rational(3, 2), yy: 0, zz: 0}
grad4 = &#91;sp.diff(Phi, v) for v in vars4&#93;
assert &#91;g.subs(q_plus) for g in grad4&#93; == &#91;g.subs(q_minus) for g in grad4&#93;

# Phi=phi0(s,x)+y*f(s,x)+z*g(s,x).  Its Hessian determinant is the square
# of the planar Jacobian of (f,g).
f = sp.diff(Phi, yy)
g = sp.diff(Phi, zz)
Jfg = sp.factor(sp.det(sp.Matrix(&#91;
    &#91;sp.diff(f, s), sp.diff(f, xx)&#93;,
    &#91;sp.diff(g, s), sp.diff(g, xx)&#93;,
&#93;)))
assert Jfg == -8 * s
assert sp.expand(sp.hessian(Phi, vars4).det() - Jfg**2) == 0
new_u = sp.symbols("u")
assert sp.expand(f.subs(xx, (new_u - 3 * s) / 2) - (new_u**2 - s**2) / 2) == 0
assert sp.expand(g.subs(xx, (new_u - 3 * s) / 2) - 4 * new_u) == 0

print("Directional-second-derivative coefficient matrix: 158 x 15, rank 15")
print("Hyperplane cases: coefficients -36504, -512, 2688; final case determinant 0")
print("No linear hyperplane through the collision yields nonzero constant Hessian")
print("Birational four-variable near-descent: det Hess = 64*s^2")
print("Underlying planar fold: ((u^2-s^2)/2, 4u), Jacobian -8s")
</code></pre>

## `planar-descent-no-go-20260802-v1/hc4_square_correction_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact no-go for the first natural quadratic correction of the HC4 fold.

In coordinates (s,u,y,z), the polynomial four-variable near-descent is

    Phi = -(13*s^2 - 3*s*u - 13)^2/4
          + (u^2-s^2)*y/2 + 4*u*z,

and det Hess(Phi)=16*s^2.  This script proves that adding

    w^2,  w=(a0+a1*s+a2*u)*y + (b0+b1*s+b2*u)*z,

cannot make the Hessian determinant a nonzero constant.  It is enough to
restrict the Hessian determinant to y=z=0; the displayed coefficient
conditions give a contradiction over every characteristic-zero field.
"""
from __future__ import annotations

import sympy as sp

s, u, y, z = sp.symbols("s u y z")
a0, a1, a2, b0, b1, b2 = sp.symbols("a0 a1 a2 b0 b1 b2")
q = 13 * s**2 - 3 * s * u - 13
Phi = -q**2 / 4 + (u**2 - s**2) * y / 2 + 4 * u * z
assert sp.factor(sp.hessian(Phi, (s, u, y, z)).det()) == 16 * s**2

A = a0 + a1 * s + a2 * u
B = b0 + b1 * s + b2 * u
w = A * y + B * z
F = sp.expand(Phi + w**2)

# At y=z=0, the base-base and mixed corrections from w^2 vanish; only the
# rank-one fibre Hessian 2(A,B)^T(A,B) remains.  Computing this specialization
# is much smaller than expanding the full four-variable determinant.
H = sp.hessian(F, (s, u, y, z)).subs({y: 0, z: 0})
D = sp.Poly(sp.expand(H.det()), s, u)

assert sp.factor(D.coeff_monomial(s**6)) == 9 * b1**2
assert sp.factor(D.coeff_monomial(u**6)) == 9 * b2**2
assert sp.factor(D.coeff_monomial(s)) == -104 * a0 * (104 * a1 + 3 * b0)
assert sp.factor(D.coeff_monomial(u)) == -2704 * a0 * (4 * a2 - b0)
assert D.coeff_monomial(1) == -5408 * a0**2

# If D were a nonzero constant, b1=b2=0 and a0!=0.  The coefficients of s
# and u then force b0=-104*a1/3=4*a2.  Under these relations the u^2
# coefficient is 144*a0^2, a contradiction.
u2_reduced = sp.factor(
    D.coeff_monomial(u**2).subs({b1: 0, b2: 0, b0: 4 * a2})
)
assert u2_reduced == 144 * a0**2

print("det Hess(Phi) = 16*s^2")
print("s^6 and u^6 coefficients force b1=b2=0")
print("nonzero constant term forces a0!=0")
print("s,u coefficients force 104*a1+3*b0=0 and 4*a2-b0=0")
print("then the u^2 coefficient is 144*a0^2: contradiction")
</code></pre>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md`

<pre><code class="language-markdown">
# Boundary seed for the first post-125 complete-chain case

## Source data

The first family at maximum degree 125 in the complete-chain table is

\&#91;
F_2:\qquad A_0=(5,20),\quad A_0'=(1,0),\quad A_1=(7/5,2),
\qquad (m,n)=(3,5).
\&#93;

This note extracts the exact terminal-edge information that is available before a full Newton-support normalization.

## 1. Starting direction and fractional coordinate

The edge difference is

\&#91;
A_0-A_0'=(4,20),
\&#93;

so its primitive normal direction is

\&#91;
(\rho,\sigma)=(5,-1).
\&#93;

The standard fractional edge coordinate is therefore

\&#91;
z=x^{-\sigma/\rho}y=x^{1/5}y.
\&#93;

For the \(P\)-coordinate, the edge runs from

\&#91;
mA_0'=(3,0)
\quad\text{to}\quad
mA_0=(15,60),
\&#93;

so

\&#91;
\ell_{5,-1}(P)=x^3p(z),\qquad \deg p=60,\qquad p(0)\ne0.
\&#93;

For \(Q\), the corresponding edge runs from \((5,0)\) to \((25,100)\), hence

\&#91;
\ell_{5,-1}(Q)=x^5q(z),\qquad \deg q=100.
\&#93;

Because the original pair is polynomial in \(x,y\), only powers \(z^{5j}\) occur. Equivalently, with

\&#91;
w=z^5=xy^5,
\&#93;

one may write

\&#91;
\ell_{5,-1}(P)=x^3\widetilde p(w),\quad \deg\widetilde p=12,
\&#93;

\&#91;
\ell_{5,-1}(Q)=x^5\widetilde q(w),\quad \deg\widetilde q=20.
\&#93;

## 2. Common-power and double-root constraint

The standard leading-form theorem for an \((m,n)=(3,5)\) pair gives, up to nonzero scalars,

\&#91;
p(z)=R(z)^3,\qquad q(z)=R(z)^5,
\qquad \deg R=20.
\&#93;

In the integral coordinate \(w=z^5\), this becomes

\&#91;
\widetilde p(w)=S(w)^3,\qquad
\widetilde q(w)=S(w)^5,
\qquad \deg S=4.
\&#93;

The child-corner formula is

\&#91;
A_1=A_0'+\frac{m_\lambda}{m}
\left(-\frac\sigma\rho,1\right).
\&#93;

Substituting the table data gives

\&#91;
(7/5,2)=(1,0)+\frac{m_\lambda}{3}(1/5,1),
\&#93;

and therefore

\&#91;
\boxed{m_\lambda=6.}
\&#93;

Thus the chosen root has multiplicity six in \(p=R^3\), hence multiplicity two in \(R\). Since \(p(0)\ne0\), the root is nonzero. After the fractional shear

\&#91;
y\longmapsto y+\lambda x^{-1/5},
\qquad z\longmapsto z+\lambda,
\&#93;

we have

\&#91;
R(z+\lambda)=z^2T(z),\qquad T(0)\ne0,
\&#93;

and the new leading monomial of \(P\) is

\&#91;
x^3z^6=x^{21/5}y^6.
\&#93;

Dividing its exponent pair by \(m=3\) gives

\&#91;
(7/5,2)=A_1,
\&#93;

which independently verifies the chain transition.

## 3. What this fixes, and what it does not

The complete-chain data already force:

- the fractional scale \(l_1=5\);
- a quartic integral common-root polynomial \(S(w)\);
- a distinguished nonzero double root of \(S\);
- the first approximate-root shear;
- the child corner \((7/5,2)\).

They do **not** yet determine:

- the complete normalized Newton polygons after the shear;
- the monomial bracket exponent \(\kappa\) in the final toric chart;
- the adjacent-component pole scale \(a\);
- the higher normal-neighborhood line-bundle windows (the reduced primary Hurwitz problem is determined in Section 5);
- the secondary contact degree \(e\).

Once \((a,\kappa)\) are obtained, with common powers \((3,5)\), the universal contact formula gives

\&#91;
\boxed{e=8a-\kappa-1.}
\&#93;

If \(e&gt;a^2\), the secondary cover is then forced by the universal transport theorem and has passport

\&#91;
(a^a\,(e-a^2)),\qquad(e),\qquad(a+1\,1^{e-a-1}).
\&#93;

## 4. Remaining support-normalization task

The reduced primary face can be determined without the entire support (Section 5). Full support propagation is still needed for the gluing problem:

1. propagate the fractional shear through the full standard rectangle;
2. use the terminal-corner inequalities and the gap-five congruence to discard forbidden lattice points;
3. choose the adjacent toric ray and return to the quotient coordinate \(u=z^5\);
4. enumerate the finite normal-layer windows;
5. compute \(a\), \(\kappa\), the secondary contact data, and the two-point line-bundle spaces.

This is the first meaningful test of whether the degree-21 gluing mechanism is a terminal-chain mechanism rather than a special feature of the \((8,28)\) support.

## 5. Subsequent terminal-face determination and lattice quotient

The type-I.b final-corner formulas give

\&#91;
A_1=(7/5,2),\quad k=1,\quad(m,n)=(3,5),
\&#93;

\&#91;
(\rho,\sigma)=(25,-17),\qquad z=x^{17/25}y,
\&#93;

\&#91;
P_E=x^{4/5}y\,p(z),\quad\deg p=5,
\qquad
Q_E=x^{1/5}q(z),\quad\deg q=10,
\&#93;

and

\&#91;
5pq-3zpq'+5zp'q=1.
\tag{5.1}
\&#93;

The fractional uniformizing cover has degree 30 and passport

\&#91;
(5^6),(3^{10}),(15,1^{15}).
\&#93;

That ambient passport has eleven connected dessin classes.  However, the complete-chain lattice gap is

\&#91;
g=\operatorname{gap}(25,5)=5.
\&#93;

Polynomial support therefore forces

\&#91;
p(z)=\bar p(z^5),\qquad q(z)=\bar q(z^5).
\&#93;

With \(u=z^5\), equation (5.1) becomes

\&#91;
\bar p\bar q-3u\bar p\bar q'+5u\bar p'\bar q=\frac15,
\&#93;

with

\&#91;
\deg\bar p=1,\qquad\deg\bar q=2.
\&#93;

The lattice-compatible quotient passport is

\&#91;
\boxed{(5,1),(3^2),(3,1^3),}
\&#93;

of degree six.  Its connected Hurwitz count is one, and its deck group is trivial.  A normalized representative is

\&#91;
\bar p=1-u,
\qquad
\bar q=\frac15-\frac35u+\frac9{25}u^2,
\&#93;

so, up to target scaling,

\&#91;
\boxed{
\phi_6(u)=\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
}
\&#93;

The degree-30 ambient face is the cyclic pullback \(\phi_6(z^5)\).  Thus only the unique \(C_5\)-symmetric one among the eleven ambient dessins is compatible with the polynomial lattice.

## 6. Revised next exact computation

The reduced terminal map is now completely fixed.  The next calculation is not an eleven-case degree-30 search.  It is one \(C_5\)-equivariant normal-neighborhood computation around the explicit degree-six map above:

1. propagate the full Newton support through the complete chain into the quotient coordinate \(u=z^5\);
2. determine the allowed two-point line-bundle windows for the normal coefficients;
3. form the intrinsic determinant layer operators and their pole-filtered residue adjoints;
4. compute the boundary Kuranishi section;
5. prove either no gluing or a strict complete-chain descent.

See `terminal_primary_belyi_reduction.md` and `verify_post125_terminal_examples.py`.
</code></pre>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/next_complete_chain_queue.json`

<pre><code class="language-json">
&#91;
  {
    "priority": 1,
    "label": "F2",
    "chain": &#91;
      "(5,20)",
      "(7/5,2)"
    &#93;,
    "starting_lower_endpoint": "(1,0)",
    "m_n": &#91;
      3,
      5
    &#93;,
    "maximum_degree": 125,
    "reason": "first candidate at the post-(8,28) boundary; one-step chain; different degree ratio",
    "terminal_k": 1,
    "terminal_b": 2,
    "terminal_coordinate_exponent": "17/25",
    "terminal_ode": "5*p*q - 3*z*p*q' + 5*z*p'*q = 1",
    "terminal_direction": &#91;
      25,
      -17
    &#93;,
    "lattice_gap": 5,
    "ambient_terminal_degree": 30,
    "ambient_terminal_passport": &#91;
      "(5^6)",
      "(3^10)",
      "(15,1^15)"
    &#93;,
    "lattice_quotient_degree": 6,
    "lattice_quotient_passport": &#91;
      "(5,1)",
      "(3^2)",
      "(3,1^3)"
    &#93;,
    "lattice_quotient_classes": 1,
    "deck_group": "trivial (unique fixed sheet in the first branch partition)",
    "quotient_ode": "1*pbar*qbar - 3*u*pbar*qbar' + 5*u*pbar'*qbar = 1/5",
    "explicit_quotient_map_available": true,
    "ambient_connected_classes": 11,
    "lattice_compatible_ambient_classes": 1,
    "fixed_constant_linearization": {
      "status": "verified surjective",
      "kernel": "source scaling span{(u pbar'(u), u qbar'(u))}",
      "artifact": "terminal_face_rigidity.json"
    }
  },
  {
    "priority": 2,
    "label": "length-1 case",
    "chain": &#91;
      "(7,35)",
      "(19/7,5)"
    &#93;,
    "m_n": &#91;
      2,
      3
    &#93;,
    "maximum_degree": 126,
    "reason": "smallest next one-step chain after F2",
    "terminal_k": 2,
    "terminal_b": 5,
    "terminal_coordinate_exponent": "11/21",
    "terminal_ode": "3*p*q - 2*z*p*q' + 3*z*p'*q = 1",
    "terminal_direction": &#91;
      21,
      -11
    &#93;,
    "lattice_gap": 3,
    "ambient_terminal_degree": 30,
    "ambient_terminal_passport": &#91;
      "(3^10)",
      "(2^15)",
      "(24,1^6)"
    &#93;,
    "lattice_quotient_degree": 10,
    "lattice_quotient_passport": &#91;
      "(3^3,1)",
      "(2^5)",
      "(8,1^2)"
    &#93;,
    "lattice_quotient_classes": 1,
    "deck_group": "trivial (unique fixed sheet in the first branch partition)",
    "quotient_ode": "1*pbar*qbar - 2*u*pbar*qbar' + 3*u*pbar'*qbar = 1/3",
    "explicit_quotient_map_available": true,
    "fixed_constant_linearization": {
      "status": "verified surjective",
      "kernel": "source scaling span{(u pbar'(u), u qbar'(u))}",
      "artifact": "terminal_face_rigidity.json"
    }
  },
  {
    "priority": 3,
    "label": "length-2 case",
    "chain": &#91;
      "(12,30)",
      "(16/3,10)",
      "(11/6,3)"
    &#93;,
    "m_n": &#91;
      3,
      2
    &#93;,
    "maximum_degree": 126,
    "reason": "first same-bound example testing compatibility across more than one corner",
    "terminal_k": 1,
    "terminal_b": 3,
    "terminal_coordinate_exponent": "7/12",
    "terminal_ode": "2*p*q - 3*z*p*q' + 2*z*p'*q = 1",
    "terminal_direction": &#91;
      12,
      -7
    &#93;,
    "lattice_gap": 2,
    "ambient_terminal_degree": 18,
    "ambient_terminal_passport": &#91;
      "(2^9)",
      "(3^6)",
      "(14,1^4)"
    &#93;,
    "lattice_quotient_degree": 9,
    "lattice_quotient_passport": &#91;
      "(2^4,1)",
      "(3^3)",
      "(7,1^2)"
    &#93;,
    "lattice_quotient_classes": 1,
    "deck_group": "trivial (unique fixed sheet in the first branch partition)",
    "quotient_ode": "1*pbar*qbar - 3*u*pbar*qbar' + 2*u*pbar'*qbar = 1/2",
    "explicit_quotient_map_available": true,
    "fixed_constant_linearization": {
      "status": "verified surjective",
      "kernel": "source scaling span{(u pbar'(u), u qbar'(u))}",
      "artifact": "terminal_face_rigidity.json"
    }
  },
  {
    "priority": 4,
    "label": "F24",
    "chain": &#91;
      "(8,24)",
      "(14/4,6)",
      "(19/8,3)"
    &#93;,
    "intermediate_endpoints": &#91;
      "(2,0)",
      "(5/4,0)"
    &#93;,
    "m_n": &#91;
      3,
      4
    &#93;,
    "maximum_degree": 128,
    "reason": "different degree ratio and a two-level complete chain",
    "terminal_k": 1,
    "terminal_b": 3,
    "terminal_coordinate_exponent": "25/32",
    "terminal_ode": "4*p*q - 3*z*p*q' + 4*z*p'*q = 1",
    "terminal_direction": &#91;
      32,
      -25
    &#93;,
    "lattice_gap": 4,
    "ambient_terminal_degree": 36,
    "ambient_terminal_passport": &#91;
      "(4^9)",
      "(3^12)",
      "(20,1^16)"
    &#93;,
    "lattice_quotient_degree": 9,
    "lattice_quotient_passport": &#91;
      "(4^2,1)",
      "(3^3)",
      "(5,1^4)"
    &#93;,
    "lattice_quotient_classes": 2,
    "deck_group": "trivial (unique fixed sheet in the first branch partition)",
    "quotient_ode": "1*pbar*qbar - 3*u*pbar*qbar' + 4*u*pbar'*qbar = 1/4",
    "explicit_quotient_map_available": true,
    "fixed_constant_linearization": {
      "status": "verified surjective",
      "kernel": "source scaling span{(u pbar'(u), u qbar'(u))}",
      "artifact": "terminal_face_rigidity.json"
    }
  },
  {
    "priority": 5,
    "label": "length-1 case",
    "chain": &#91;
      "(11,33)",
      "(19/4,8)"
    &#93;,
    "m_n": &#91;
      2,
      3
    &#93;,
    "maximum_degree": 132,
    "reason": "tests scaling of residue windows at a larger terminal corner",
    "terminal_b": 8,
    "terminal_direction": &#91;
      12,
      -7
    &#93;,
    "lattice_gap": 3,
    "ambient_terminal_degree": 48,
    "ambient_terminal_passport": &#91;
      "(3^16)",
      "(2^24)",
      "(39,1^9)"
    &#93;,
    "lattice_quotient_degree": 16,
    "lattice_quotient_passport": &#91;
      "(3^5,1)",
      "(2^8)",
      "(13,1^3)"
    &#93;,
    "lattice_quotient_classes": 2,
    "deck_group": "trivial (unique fixed sheet in the first branch partition)",
    "terminal_ode": "3*p*q - 2*z*p*q' + 3*z*p'*q = 1",
    "quotient_ode": "1*pbar*qbar - 2*u*pbar*qbar' + 3*u*pbar'*qbar = 1/3",
    "explicit_quotient_map_available": false
  }
&#93;
</code></pre>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi_reduction.md`

<pre><code class="language-markdown">
# Lattice-gap reduction of terminal type-I.b boundary covers

**Working research note — 22 July 2026.** This note records an exact reduction obtained from the final-corner formulas for standard plane Keller pairs after replacing the fractional boundary parameter by the lattice quotient forced by the complete-chain gap. The result is a finite Hurwitz problem of substantially smaller degree than the ambient uniformizing cover. It does not prove that any listed boundary map extends to a Keller pair.

## 1. Final face equation on the fractional uniformizing line

Let a final regular corner of type I.b have

\&#91;
A=\left(\frac a\ell,b\right),\qquad
\operatorname{st}(Q)=\left(\frac k\ell,0\right),\qquad
\operatorname{st}(P)=\left(1-\frac k\ell,1\right),
\&#93;

with a standard coprime degree ratio \((m,n)\), in the orientation of equation (3.17) of Guccione--Guccione--Horruitiner--Valqui. Then

\&#91;
\operatorname{en}(P)=mA,\qquad \operatorname{en}(Q)=nA,
\&#93;

and

\&#91;
\frac{\sigma}{\rho}=\frac{k-na}{n\ell b}.
\&#93;

Put

\&#91;
r=-\frac\sigma\rho=\frac{na-k}{n\ell b},\qquad z=x^r y.
\&#93;

The terminal faces have the forms

\&#91;
P_E=x^{1-k/\ell}y\,p(z),\qquad \deg p=mb-1,
\&#93;

\&#91;
Q_E=x^{k/\ell}q(z),\qquad \deg q=nb.
\&#93;

For

\&#91;
P=x^Ay^Bp(z),\qquad Q=x^Cy^Dq(z),\qquad z=x^ry,
\&#93;

a direct differentiation gives

\&#91;
&#91;P,Q&#93;=x^{A+C-1}y^{B+D-1}
\left((AD-BC)pq+(A-Br)zpq'+(rD-C)zp'q\right).
\&#93;

The final-corner relation

\&#91;
(m+n)bk-n(b\ell-a)=k
\&#93;

reduces the three coefficients to a common scalar multiple of \((n,-m,n)\). After a nonzero target normalization,

\&#91;
\boxed{npq-mzpq'+nzp'q=1.}
\tag{1.1}
\&#93;

Therefore

\&#91;
\tau(z)=z^n\frac{p(z)^n}{q(z)^m},
\qquad
\boxed{\tau'(z)=z^{n-1}\frac{p(z)^{n-1}}{q(z)^{m+1}}.}
\tag{1.2}
\&#93;

If one forgets the lattice of the polynomial pair, this is a degree-\(mnb\) Belyi map with passport

\&#91;
(n^{mb}),\qquad(m^{nb}),\qquad
\bigl((m+n)b-1,1^{mnb-(m+n)b+1}\bigr).
\tag{1.3}
\&#93;

We call (1.3) the **ambient uniformizing passport**.

## 2. The lattice-gap quotient

Let

\&#91;
g=\operatorname{gap}(\rho,\ell)=\frac{\rho}{\gcd(\rho,\ell)}.
\&#93;

The complete-chain lattice theorem forces both face polynomials to use only powers of \(z^g\):

\&#91;
p(z)=\bar p(u),\qquad q(z)=\bar q(u),\qquad u=z^g.
\tag{2.1}
\&#93;

Consequently

\&#91;
g\mid mb-1,\qquad g\mid nb.
\&#93;

Since \(g\mid mb-1\), one has \(\gcd(g,b)=1\); hence \(g\mid n\). Set

\&#91;
N=\frac ng,\qquad
A_0=\frac{mb-1}{g},\qquad
B_0=\frac{nb}{g}.
\&#93;

Substitution into (1.1), followed by division by \(g\), gives the quotient equation

\&#91;
\boxed{
N\bar p\bar q-mu\bar p\bar q'
+nu\bar p'\bar q=\frac1g.
}
\tag{2.2}
\&#93;

Define

\&#91;
\boxed{
\bar\tau(u)=u^N\frac{\bar p(u)^n}{\bar q(u)^m}.
}
\tag{2.3}
\&#93;

Then

\&#91;
\boxed{
\bar\tau'(u)=\frac1g\,
 u^{N-1}\frac{\bar p(u)^{n-1}}{\bar q(u)^{m+1}}.
}
\tag{2.4}
\&#93;

Put

\&#91;
D=\frac{mnb}{g},\qquad
H=\frac{(m+n)b-1}{g}.
\&#93;

The actual lattice-compatible boundary cover has degree \(D\) and passport

\&#91;
\boxed{
(n^{A_0},N),\qquad
(m^{B_0}),\qquad
(H,1^{D-H}).
}
\tag{2.5}
\&#93;

Repeated parts are combined in the usual partition notation. The ambient map factors as

\&#91;
\tau(z)=\bar\tau(z^g).
\&#93;

Thus the degree-\(mnb\) cover is a cyclic \(g\)-pullback; the finite Hurwitz problem relevant to a polynomial complete-chain corner is the smaller degree-\(D\) problem (2.5).

### Connectedness

Every permutation triple with passport (2.5) is transitive. Indeed, an orbit not containing the unique \(H\)-cycle is fixed by the third permutation, so on that orbit the first two permutations are mutual inverses. Their cycle lengths would therefore have to agree. The ordinary cycles have lengths \(n\) and \(m\), which are coprime and greater than one. The only exceptional first-cycle length is \(N\mid n\); equality \(N=m\) would force \(m\mid n\), again impossible. Hence no second orbit exists.

## 3. The first five boundary problems

Exact Murnaghan--Nakayama character calculations give the following connected Hurwitz counts. In each listed quotient passport, the first partition has a unique fixed sheet. A deck transformation centralizing a transitive monodromy group is semiregular on the sheets, so that fixed sheet forces the deck group to be trivial. The weighted count is therefore the ordinary number of dessin classes.

| Case | \((m,n,b;k)\) | \(g\) | Ambient degree | Lattice quotient passport | Quotient degree | Classes |
|---|---:|---:|---:|---|---:|---:|
| \(F_2\), max degree 125 | \((3,5,2;1)\) | 5 | 30 | \((5,1),(3^2),(3,1^3)\) | 6 | 1 |
| one-step max 126 | \((2,3,5;2)\) | 3 | 30 | \((3^3,1),(2^5),(8,1^2)\) | 10 | 1 |
| two-step max 126 | \((3,2,3;1)\) | 2 | 18 | \((2^4,1),(3^3),(7,1^2)\) | 9 | 1 |
| \(F_{24}\), max 128 | \((3,4,3;1)\) | 4 | 36 | \((4^2,1),(3^3),(5,1^4)\) | 9 | 2 |
| one-step max 132 | \((2,3,8;1)\) | 3 | 48 | \((3^5,1),(2^8),(13,1^3)\) | 16 | 2 |

The first four rows have explicit quotient maps below.

## 4. The \(F_2\) correction: one relevant map, not eleven

For

\&#91;
A=(7/5,2),\qquad k=1,\qquad(m,n)=(3,5),
\&#93;

one has

\&#91;
(\rho,\sigma)=(25,-17),\qquad g=5,
\&#93;

and the ambient equation

\&#91;
5pq-3zpq'+5zp'q=1,
\qquad \deg(p,q)=(5,10).
\&#93;

The ambient degree-30 passport

\&#91;
(5^6),(3^{10}),(15,1^{15})
\&#93;

has eleven connected dessin classes: eight asymmetric, two with deck group \(C_3\), and one with deck group \(C_5\). This is an exact count, but it is **not** the polynomial complete-chain count.

The gap condition requires \(p,q\in K&#91;z^5&#93;\), so only the unique \(C_5\)-symmetric class survives. On \(u=z^5\),

\&#91;
\bar p(u)=1-u,
\qquad
\bar q(u)=\frac15-\frac35u+\frac9{25}u^2,
\tag{4.1}
\&#93;

and

\&#91;
\bar p\bar q-3u\bar p\bar q'+5u\bar p'\bar q=\frac15.
\&#93;

The unique quotient Belyi map is, up to target scaling,

\&#91;
\boxed{
\phi_6(u)=
\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
}
\tag{4.2}
\&#93;

The ambient terminal map is \(\phi_6(z^5)\). Therefore the reduced boundary datum for the first degree-125 complete-chain family is unique up to the standard source and target normalizations.

## 5. Explicit maps for the first post-125 rows

### 5.1 One-step maximum degree 126

Here

\&#91;
A=(19/7,5),\quad k=2,\quad(m,n)=(2,3),
\quad(\rho,\sigma)=(21,-11),\quad g=3.
\&#93;

The quotient passport is

\&#91;
(3^3,1),(2^5),(8,1^2),
\&#93;

and it has one class. Put

\&#91;
P=u^3+u^2+\frac5{12}u+\frac1{18},
\&#93;

\&#91;
Q=u^5+\frac32u^4+u^3+\frac13u^2+\frac5{96}u+\frac1{576}.
\&#93;

Then

\&#91;
\boxed{uP^3-Q^2=-\frac{36u^2+28u+9}{2985984}.}
\tag{5.1}
\&#93;

With \(\bar p=18P\) and \(\bar q=192Q\), equation (2.2) is

\&#91;
\bar p\bar q-2u\bar p\bar q'+3u\bar p'\bar q=\frac13.
\&#93;

The ambient face is obtained by \(u=z^3\).

### 5.2 Two-step maximum degree 126

Here

\&#91;
A=(11/6,3),\quad k=1,\quad(m,n)=(3,2),
\quad(\rho,\sigma)=(12,-7),\quad g=2.
\&#93;

The quotient passport

\&#91;
(2^4,1),(3^3),(7,1^2)
\&#93;

has one class. A normalized pair is

\&#91;
\bar p=1+\frac{20}{3}u+24u^2+\frac{288}{7}u^3+\frac{288}{7}u^4,
\&#93;

\&#91;
\bar q=\frac12+5u+12u^2+18u^3,
\&#93;

satisfying

\&#91;
\bar p\bar q-3u\bar p\bar q'+2u\bar p'\bar q=\frac12.
\&#93;

Equivalently, for

\&#91;
P=u^4+u^3+\frac7{12}u^2+\frac{35}{216}u+\frac7{288},
\&#93;

\&#91;
Q=u^3+\frac23u^2+\frac5{18}u+\frac1{36},
\&#93;

one has

\&#91;
\boxed{uP^2-Q^3=-\frac{72u^2+39u+16}{746496}.}
\tag{5.2}
\&#93;

The ambient face is obtained by \(u=z^2\).

### 5.3 Family \(F_{24}\), maximum degree 128

Here

\&#91;
A=(19/8,3),\quad k=1,\quad(m,n)=(3,4),
\quad(\rho,\sigma)=(32,-25),\quad g=4.
\&#93;

The quotient passport

\&#91;
(4^2,1),(3^3),(5,1^4)
\&#93;

has exactly two classes, conjugate over \(\mathbf Q(\sqrt6)\). With \(\varepsilon=\pm1\), set

\&#91;
\bar p_\varepsilon
=1+u+\left(\frac13+\varepsilon\frac{\sqrt6}{18}\right)u^2,
\&#93;

\&#91;
\bar q_\varepsilon
=\frac14+\frac58u
+\left(\frac25+\varepsilon\frac{\sqrt6}{40}\right)u^2
+\left(\frac{17}{160}+\varepsilon\frac{11\sqrt6}{480}\right)u^3.
\&#93;

They satisfy

\&#91;
\bar p\bar q-3u\bar p\bar q'+4u\bar p'\bar q=\frac14.
\&#93;

The ambient faces are obtained by \(u=z^4\).


## 6. Reduced-cover infinitesimal rigidity

Fix the constant terms of a quotient solution and write

\&#91;
\bar p=p_0+\sum_{i=1}^{A}a_i u^i,
\qquad
\bar q=q_0+\sum_{j=1}^{B}b_j u^j.
\&#93;

The differential of

\&#91;
\mathcal F(\bar p,\bar q)
=N\bar p\bar q-mu\bar p\bar q'+nu\bar p'\bar q
\&#93;

at a solution is

\&#91;
\mathscr L(\alpha,\beta)
=N(\alpha\bar q+\bar p\beta)
-mu(\alpha\bar q'+\bar p\beta')
+nu(\alpha'\bar q+\bar p'\beta).
\tag{6.1}
\&#93;

The infinitesimal source rescaling \(u\mapsto(1+\varepsilon)u\) gives

\&#91;
(\alpha,\beta)=(u\bar p',u\bar q')\in\ker\mathscr L.
\tag{6.2}
\&#93;

Exact coefficient matrices give:

| quotient map | \((A,B)\) | domain dimension | target dimension | rank | kernel |
|---|---:|---:|---:|---:|---|
| \(F_2\), max 125 | \((1,2)\) | 3 | 2 | 2 | source scaling |
| one-step max 126 | \((3,5)\) | 8 | 7 | 7 | source scaling |
| two-step max 126 | \((4,3)\) | 7 | 6 | 6 | source scaling |
| \(F_{24}\), minus | \((2,3)\) | 5 | 4 | 4 | source scaling |
| \(F_{24}\), plus | \((2,3)\) | 5 | 4 | 4 | source scaling |

The nonzero maximal minors produced by the verifier are respectively

\&#91;
-\frac{36}{5},\qquad
2090188800,\qquad
\frac{37791360}{7},\qquad
\frac{99}{20}\mp\frac{153\sqrt6}{40}.
\&#93;

Hence, after quotienting by source scaling, each explicit reduced terminal map is a reduced isolated point of its coefficient scheme.  The terminal-primary Hurwitz problem contributes no hidden infinitesimal modulus in these cases.  Any surviving flexibility must occur in the normal-neighborhood coefficients and their global residue gluing, not in a deformation of the reduced Belyi cover itself.

This is a coefficient-level statement.  It does not yet prove that the complete Newton-bounded boundary-gluing functor is an etale product of the reduced-cover point with the normal-jet Kuranishi problem; establishing that functorial splitting remains part of the global program.

## 7. Consequence for the gluing--descent program

The lattice correction changes the next computational problem materially:

- the degree-125 family \(F_2\) no longer requires eleven boundary Kuranishi calculations;
- it requires one calculation around the explicit degree-six quotient map (4.2), with the \(C_5\)-equivariant normal windows inherited from the polynomial lattice;
- the next two degree-126 chains likewise have unique quotient maps of degrees ten and nine;
- the first branching occurs at \(F_{24}\), with only two conjugate degree-nine maps.

The next exact geometric task is therefore finite and sharply specified:

1. propagate the complete-chain Newton polygons into the \(u=z^g\) quotient chart;
2. compute the two-point line-bundle windows for every normal layer;
3. construct the intrinsic operators \(\mathscr D_r\), their pole-filtered adjoints, and the Kuranishi forcing classes;
4. test whether the resulting gluing scheme is empty or whether vanishing high-pole residues produce a strict complete-chain descent.

The reduction in this note does not establish the gluing obstruction for these cases. It removes the unnecessary cyclic pullback and leaves a small, exact list of reduced boundary maps on which the universal residue machinery can be tested.

## Reproducibility

- `terminal_primary_belyi.py` verifies the final-corner equation, primitive direction, gap divisibility, quotient equation, derivative, passports, and the explicit \(F_2\) map.
- `count_F2_terminal_dessins.py` computes the eleven ambient classes and verifies that exactly one is the lattice-compatible \(C_5\) pullback.
- `verify_post125_terminal_examples.py` verifies all five quotient passports and Hurwitz counts, together with the explicit maps in Sections 4 and 5.
- `post125_terminal_passports.json` contains the exact machine-readable output.
- `terminal_face_rigidity.py` verifies the exact tangent ranks, scaling kernels, and nonzero maximal minors in Section 6.
</code></pre>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/verify_F2_degree125_seed.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact arithmetic checks for the F2, maximum-degree-125 complete-chain seed."""
from fractions import Fraction
from math import gcd

A0 = (Fraction(5), Fraction(20))
A0p = (Fraction(1), Fraction(0))
A1 = (Fraction(7, 5), Fraction(2))
m, n = 3, 5

# Primitive normal to the edge A0-A0'.
dx = A0&#91;0&#93; - A0p&#91;0&#93;
dy = A0&#91;1&#93; - A0p&#91;1&#93;
g = gcd(dx.numerator, dy.numerator)
rho = dy / g
sigma = -dx / g
assert (rho, sigma) == (5, -1)

# Degrees in z=x^(1/5)y.
p_degree = m * (A0&#91;1&#93; - A0p&#91;1&#93;)
q_degree = n * (A0&#91;1&#93; - A0p&#91;1&#93;)
assert p_degree == 60 and q_degree == 100
assert p_degree % m == 0 and q_degree % n == 0
R_degree = p_degree / m
assert R_degree == 20
assert R_degree % 5 == 0
S_degree = R_degree / 5
assert S_degree == 4

# Child formula A1=A0' + (m_lambda/m)(-sigma/rho,1).
mult_ratio = A1&#91;1&#93; - A0p&#91;1&#93;
m_lambda = m * mult_ratio
assert m_lambda == 6
computed_A1 = (
    A0p&#91;0&#93; + mult_ratio * Fraction(-sigma, rho),
    A0p&#91;1&#93; + mult_ratio,
)
assert computed_A1 == A1

# After shifting a double root of R to zero, P has x^3 z^6.
new_x_exp = Fraction(3) + Fraction(6, 5)
new_y_exp = Fraction(6)
assert (new_x_exp / m, new_y_exp / m) == A1

print("F2 edge direction:", (rho, sigma))
print("degrees in z:", p_degree, q_degree, "common R degree:", R_degree)
print("integral common-root polynomial S(x y^5) degree:", S_degree)
print("chosen p-root multiplicity:", m_lambda, "=&gt; double root of R/S")
print("child corner verified:", computed_A1)
print("all exact F2 seed checks passed")
</code></pre>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact terminal-primary Belyi formulas for type-I.b complete-chain corners.

There are two distinct covers.

1. On the fractional uniformizing coordinate z=x^{-sigma/rho}y, the final
   face equation is

       n*p*q - m*z*p*q' + n*z*p'*q = 1,

   with deg(p)=m*b-1 and deg(q)=n*b.  It defines an ambient Belyi map

       tau(z)=z**n*p(z)**n/q(z)**m

   of degree m*n*b.

2. Polynomial lattice support forces p(z)=pbar(z**g), q(z)=qbar(z**g), where

       g=gap(rho,ell)=rho/gcd(rho,ell).

   Put N=n/g and u=z**g.  The lattice-compatible quotient satisfies

       N*pbar*qbar - m*u*pbar*qbar' + n*u*pbar'*qbar = 1/g

   and defines

       taubar(u)=u**N*pbar(u)**n/qbar(u)**m

   of degree m*n*b/g.  This quotient, not the ambient cyclic pullback, is the
   finite Hurwitz problem attached to the polynomial complete-chain corner.

The script checks the final-corner arithmetic, divisibility, passports,
Riemann--Hurwitz identities, and the explicit F2 quotient/lift.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from fractions import Fraction
from math import gcd
import json
from pathlib import Path
from typing import Iterable

import sympy as sp

z, u = sp.symbols("z u")


def _partition_text(parts: Iterable&#91;int&#93;) -&gt; str:
    counts: dict&#91;int, int&#93; = {}
    for part in sorted(parts, reverse=True):
        counts&#91;part&#93; = counts.get(part, 0) + 1
    pieces: list&#91;str&#93; = &#91;&#93;
    for part in sorted(counts, reverse=True):
        mult = counts&#91;part&#93;
        pieces.append(str(part) if mult == 1 else f"{part}^{mult}")
    return "(" + ",".join(pieces) + ")"


@dataclass(frozen=True)
class Passport:
    degree: int
    cycle_types: tuple&#91;tuple&#91;int, ...&#93;, tuple&#91;int, ...&#93;, tuple&#91;int, ...&#93;&#93;
    display: tuple&#91;str, str, str&#93;
    ramification_total: int


@dataclass(frozen=True)
class TerminalReduction:
    a: int
    ell: int
    b: int
    k: int
    m: int
    n: int
    rho: int
    sigma: int
    gap: int
    N: int
    deg_p: int
    deg_q: int
    deg_p_bar: int
    deg_q_bar: int
    uniformizing: Passport
    lattice_quotient: Passport
    terminal_coordinate_exponent_r: str
    uniformizing_ode: str
    quotient_ode: str


def _passport(parts0: tuple&#91;int, ...&#93;, parts1: tuple&#91;int, ...&#93;, parts2: tuple&#91;int, ...&#93;) -&gt; Passport:
    degree = sum(parts0)
    assert sum(parts1) == degree and sum(parts2) == degree
    rh = sum(x - 1 for parts in (parts0, parts1, parts2) for x in parts)
    assert rh == 2 * degree - 2
    return Passport(
        degree=degree,
        cycle_types=(parts0, parts1, parts2),
        display=tuple(_partition_text(parts) for parts in (parts0, parts1, parts2)),
        ramification_total=rh,
    )


def terminal_passport(m: int, n: int, b: int) -&gt; Passport:
    """Ambient passport on the fractional uniformizing z-line.

    Kept under the historical function name for compatibility with earlier
    scripts.  For the polynomial/lattice-compatible passport use
    ``terminal_reduction(...).lattice_quotient``.
    """
    if min(m, n, b) &lt;= 0:
        raise ValueError("m,n,b must be positive")
    if gcd(m, n) != 1 or min(m, n) &lt;= 1:
        raise ValueError("standard-pair application assumes coprime m,n&gt;1")
    D = m * n * b
    H = (m + n) * b - 1
    return _passport(
        tuple(&#91;n&#93; * (m * b)),
        tuple(&#91;m&#93; * (n * b)),
        tuple(&#91;H&#93; + &#91;1&#93; * (D - H)),
    )


def primitive_direction(*, a: int, ell: int, b: int, k: int, n: int) -&gt; tuple&#91;int, int&#93;:
    """Primitive (rho,sigma) from sigma/rho=(k-na)/(n ell b)."""
    numerator = k - n * a
    denominator = n * ell * b
    d = gcd(abs(numerator), denominator)
    rho, sigma = denominator // d, numerator // d
    assert rho &gt; 0 and gcd(rho, abs(sigma)) == 1
    return rho, sigma


def terminal_reduction(
    *, a: int, ell: int, b: int, k: int, m: int, n: int
) -&gt; TerminalReduction:
    if min(a, ell, b, k, m, n) &lt;= 0:
        raise ValueError("all corner parameters must be positive")
    if gcd(m, n) != 1 or min(m, n) &lt;= 1:
        raise ValueError("m,n must be coprime and &gt;1")

    # Equation (3.17), in the orientation st(Q)=(k/ell,0).
    assert (m + n) * b * k - n * (b * ell - a) == k

    rho, sigma = primitive_direction(a=a, ell=ell, b=b, k=k, n=n)
    r = Fraction(-sigma, rho)
    assert r == Fraction(n * a - k, n * ell * b)
    gap = rho // gcd(rho, ell)

    A, B = Fraction(ell - k, ell), Fraction(1)
    C, D = Fraction(k, ell), Fraction(0)
    c_pq = A * D - B * C
    c_pqprime = A - B * r
    c_pprimeq = r * D - C
    scale = -Fraction(n * ell, k)
    assert (scale * c_pq, scale * c_pqprime, scale * c_pprimeq) == (n, -m, n)

    deg_p, deg_q = m * b - 1, n * b
    assert A + r * deg_p == Fraction(m * a, ell)
    assert B + deg_p == m * b
    assert C + r * deg_q == Fraction(n * a, ell)
    assert D + deg_q == n * b

    # Lattice support: only powers z^gap occur.  The degree divisibilities
    # are therefore necessary for a genuine complete-chain corner.
    assert deg_p % gap == 0
    assert deg_q % gap == 0
    assert gcd(gap, b) == 1
    assert n % gap == 0

    N = n // gap
    Abar, Bbar = deg_p // gap, deg_q // gap
    Dbar = m * n * b // gap
    Hbar_num = (m + n) * b - 1
    assert Hbar_num % gap == 0
    Hbar = Hbar_num // gap
    quotient = _passport(
        tuple(sorted(&#91;n&#93; * Abar + &#91;N&#93;, reverse=True)),
        tuple(&#91;m&#93; * Bbar),
        tuple(&#91;Hbar&#93; + &#91;1&#93; * (Dbar - Hbar)),
    )

    return TerminalReduction(
        a=a,
        ell=ell,
        b=b,
        k=k,
        m=m,
        n=n,
        rho=rho,
        sigma=sigma,
        gap=gap,
        N=N,
        deg_p=deg_p,
        deg_q=deg_q,
        deg_p_bar=Abar,
        deg_q_bar=Bbar,
        uniformizing=terminal_passport(m, n, b),
        lattice_quotient=quotient,
        terminal_coordinate_exponent_r=str(r),
        uniformizing_ode=f"{n}*p*q - {m}*z*p*q' + {n}*z*p'*q = 1",
        quotient_ode=f"{N}*pbar*qbar - {m}*u*pbar*qbar' + {n}*u*pbar'*qbar = 1/{gap}",
    )


def verify_final_corner_arithmetic(
    *, a: int, ell: int, b: int, k: int, m: int, n: int
) -&gt; dict&#91;str, object&#93;:
    """Backward-compatible JSON-style wrapper around :func:`terminal_reduction`."""
    rec = terminal_reduction(a=a, ell=ell, b=b, k=k, m=m, n=n)
    return {
        "direction": &#91;rec.rho, rec.sigma&#93;,
        "direction_ratio_sigma_over_rho": str(Fraction(rec.sigma, rec.rho)),
        "terminal_coordinate_exponent_r": rec.terminal_coordinate_exponent_r,
        "gap": rec.gap,
        "N": rec.N,
        "deg_p": str(rec.deg_p),
        "deg_q": str(rec.deg_q),
        "deg_p_bar": str(rec.deg_p_bar),
        "deg_q_bar": str(rec.deg_q_bar),
        "normalized_ode": rec.uniformizing_ode,
        "quotient_ode": rec.quotient_ode,
        "uniformizing_passport": rec.uniformizing.display,
        "lattice_quotient_passport": rec.lattice_quotient.display,
        "uniformizing_degree": rec.uniformizing.degree,
        "lattice_quotient_degree": rec.lattice_quotient.degree,
    }


def verify_explicit_f2_solution() -&gt; dict&#91;str, str&#93;:
    """Verify the unique lattice-compatible F2 quotient and its C5 pullback."""
    pbar = 1 - u
    qbar = sp.Rational(1, 5) - sp.Rational(3, 5) * u + sp.Rational(9, 25) * u**2
    qode = sp.expand(
        pbar * qbar
        - 3 * u * pbar * sp.diff(qbar, u)
        + 5 * u * sp.diff(pbar, u) * qbar
    )
    assert qode == sp.Rational(1, 5)
    taubar = sp.cancel(u * pbar**5 / qbar**3)
    assert sp.cancel(sp.diff(taubar, u) - sp.Rational(1, 5) * pbar**4 / qbar**4) == 0

    p = sp.expand(pbar.subs(u, z**5))
    q = sp.expand(qbar.subs(u, z**5))
    ode = sp.expand(5 * p * q - 3 * z * p * sp.diff(q, z) + 5 * z * sp.diff(p, z) * q)
    assert ode == 1
    tau = sp.cancel(z**5 * p**5 / q**3)
    assert sp.cancel(tau - taubar.subs(u, z**5)) == 0
    assert sp.cancel(sp.diff(tau, z) - z**4 * p**4 / q**4) == 0

    return {
        "pbar": str(sp.expand(pbar)),
        "qbar": str(sp.expand(qbar)),
        "taubar": "u*pbar(u)^5/qbar(u)^3",
        "p": str(p),
        "q": str(q),
        "tau": "taubar(z^5)",
    }


def _serialize(obj: object) -&gt; object:
    if isinstance(obj, Passport):
        data = asdict(obj)
        data&#91;"cycle_types"&#93; = &#91;list(x) for x in obj.cycle_types&#93;
        data&#91;"display"&#93; = list(obj.display)
        return data
    if isinstance(obj, TerminalReduction):
        return {
            **{k: v for k, v in asdict(obj).items() if k not in {"uniformizing", "lattice_quotient"}},
            "uniformizing": _serialize(obj.uniformizing),
            "lattice_quotient": _serialize(obj.lattice_quotient),
        }
    return obj


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int, default=7)
    parser.add_argument("--ell", type=int, default=5)
    parser.add_argument("--b", type=int, default=2)
    parser.add_argument("--k", type=int, default=1)
    parser.add_argument("--m", type=int, default=3)
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rec = terminal_reduction(a=args.a, ell=args.ell, b=args.b, k=args.k, m=args.m, n=args.n)
    payload: dict&#91;str, object&#93; = {"terminal_reduction": _serialize(rec)}
    if (args.a, args.ell, args.b, args.k, args.m, args.n) == (7, 5, 2, 1, 3, 5):
        payload&#91;"explicit_F2_solution"&#93; = verify_explicit_f2_solution()
        assert rec.gap == 5
        assert rec.lattice_quotient.degree == 6
        assert rec.lattice_quotient.display == ("(5,1)", "(3^2)", "(3,1^3)")

    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    print("all terminal-face, lattice-gap, quotient, passport, derivative, and RH checks passed")


if __name__ == "__main__":
    main()
</code></pre>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_face_rigidity.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact infinitesimal rigidity of the first lattice-quotient boundary maps.

For the quotient equation

    N p q - m u p q' + n u p' q = 1/g,

the constants p(0),q(0) are fixed and u-scaling remains.  This script forms
the exact linearization on the full coefficient windows, proves surjectivity,
and verifies that its kernel is exactly the scaling vector (u p',u q').
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp

u = sp.symbols("u")


def linearization_record(
    *, label: str, p: sp.Expr, q: sp.Expr, m: int, n: int, g: int, extension: Any = None
) -&gt; dict&#91;str, Any&#93;:
    A, B = int(sp.degree(p, u)), int(sp.degree(q, u))
    N = n // g
    avec = sp.symbols(f"a1:{A+1}")
    bvec = sp.symbols(f"b1:{B+1}")
    alpha = sum(avec&#91;i - 1&#93; * u**i for i in range(1, A + 1))
    beta = sum(bvec&#91;j - 1&#93; * u**j for j in range(1, B + 1))
    Dexpr = sp.expand(
        N * (alpha * q + p * beta)
        - m * u * (alpha * sp.diff(q, u) + p * sp.diff(beta, u))
        + n * u * (sp.diff(alpha, u) * q + sp.diff(p, u) * beta)
    )
    variables = list(avec) + list(bvec)
    rows = A + B - 1
    matrix = sp.Matrix(
        &#91;&#91;sp.expand(Dexpr).coeff(u, degree).coeff(var) for var in variables&#93; for degree in range(1, rows + 1)&#93;
    )
    rank = int(matrix.rank(iszerofunc=lambda x: sp.simplify(x) == 0))
    assert rank == rows
    null = matrix.nullspace(iszerofunc=lambda x: sp.simplify(x) == 0)
    assert len(null) == 1

    scaling_alpha = sp.expand(u * sp.diff(p, u))
    scaling_beta = sp.expand(u * sp.diff(q, u))
    scaling = sp.Matrix(
        &#91;scaling_alpha.coeff(u, i) for i in range(1, A + 1)&#93;
        + &#91;scaling_beta.coeff(u, j) for j in range(1, B + 1)&#93;
    )
    scaling_residual = (matrix * scaling).applyfunc(sp.simplify)
    assert scaling_residual == sp.zeros(rows, 1)
    # Kernel generator and scaling vector must be proportional.
    gen = null&#91;0&#93;
    ratios = &#91;sp.simplify(gen&#91;i&#93; / scaling&#91;i&#93;) for i in range(len(gen)) if scaling&#91;i&#93; != 0&#93;
    assert ratios and all(sp.simplify(r - ratios&#91;0&#93;) == 0 for r in ratios)
    assert all(sp.simplify(gen&#91;i&#93;) == 0 for i in range(len(gen)) if sp.simplify(scaling&#91;i&#93;) == 0)

    _, pivots = matrix.rref(iszerofunc=lambda x: sp.simplify(x) == 0)
    pivot_cols = &#91;int(j) for j in pivots&#91;:rows&#93;&#93;
    minor = sp.simplify(matrix&#91;:, pivot_cols&#93;.det())
    assert minor != 0

    return {
        "label": label,
        "degrees": &#91;A, B&#93;,
        "domain_dimension_fixed_constants": A + B,
        "target_dimension": rows,
        "rank": rank,
        "kernel_dimension": 1,
        "kernel": "span{(u p'(u), u q'(u))}",
        "pivot_columns_zero_based": pivot_cols,
        "nonzero_maximal_minor": str(minor),
    }


def maps() -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    sqrt6 = sp.sqrt(6)
    out: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;

    out.append(
        dict(
            label="F2_max125",
            p=1 - u,
            q=sp.Rational(1, 5) - sp.Rational(3, 5) * u + sp.Rational(9, 25) * u**2,
            m=3,
            n=5,
            g=5,
        )
    )

    P = u**3 + u**2 + sp.Rational(5, 12) * u + sp.Rational(1, 18)
    Q = (
        u**5
        + sp.Rational(3, 2) * u**4
        + u**3
        + sp.Rational(1, 3) * u**2
        + sp.Rational(5, 96) * u
        + sp.Rational(1, 576)
    )
    out.append(dict(label="one_step_max126", p=18 * P, q=192 * Q, m=2, n=3, g=3))

    out.append(
        dict(
            label="two_step_max126",
            p=1
            + sp.Rational(20, 3) * u
            + 24 * u**2
            + sp.Rational(288, 7) * u**3
            + sp.Rational(288, 7) * u**4,
            q=sp.Rational(1, 2) + 5 * u + 12 * u**2 + 18 * u**3,
            m=3,
            n=2,
            g=2,
        )
    )

    for sign in (-1, 1):
        p = 1 + u + (sp.Rational(1, 3) + sign * sqrt6 / 18) * u**2
        q = (
            sp.Rational(1, 4)
            + sp.Rational(5, 8) * u
            + (sp.Rational(2, 5) + sign * sqrt6 / 40) * u**2
            + (sp.Rational(17, 160) + sign * sp.Rational(11, 480) * sqrt6) * u**3
        )
        out.append(
            dict(
                label=f"F24_max128_{'plus' if sign == 1 else 'minus'}",
                p=p,
                q=q,
                m=3,
                n=4,
                g=4,
                extension=sqrt6,
            )
        )
    return out


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    records = &#91;linearization_record(**item) for item in maps()&#93;
    if args.json:
        args.json.write_text(json.dumps(records, indent=2) + "\n")
    print(json.dumps(records, indent=2))
    print("all reduced terminal maps are infinitesimally rigid modulo source scaling")


if __name__ == "__main__":
    main()
</code></pre>

[Back to Lane 8](plane-newton-queue-terminal-certificates.md)
