# Lane 6 exact research source packet

This is the public source packet for **Homogeneous realization and compression**. It contains the
selected proof notes, exact computation contracts, and checkers used
by the concise lane brief. Read only the files relevant to the route
you pursue. Stored outputs and very large reconstructible matrices are
omitted; the mathematical boundary of each checker remains in its
source text.

Private-source commit: `ed3137b5ce00f4f206fe1126b4fdc3bc5051b112`.

## Included files

- `lane6-transverse-source-obstruction-20260802-v1/stratified-transverse/STRATIFIED_TRANSVERSE_CLASSIFICATION.md` — `46c45f94fafa03340a363771c0726397053379602445b6dfdd5a5d7c0b1c4ffb`
- `lane6-transverse-source-obstruction-20260802-v1/tame-source-coupled/TAME_SOURCE_COUPLED_QUARTIC_OBSTRUCTION.md` — `0050b13a9715a7e7009a2788702813185e521f57b24a8bffa7adaef086b28595`
- `lane6-transverse-source-obstruction-20260802-v1/stratified-transverse/verify_uniform_middle_stratum.py` — `2877ef50243d602d6d885640274b8538289078ae91ea2882f53bbb034b566ec6`
- `lane6-transverse-source-obstruction-20260802-v1/stratified-transverse/verify_deepest_finite_classification.py` — `27a404759dfdc47b2734c2d58aa205044e4853d32c200791ba386971605425f0`
- `lane6-transverse-source-obstruction-20260802-v1/tame-source-coupled/verify_residual_source_target_obstruction.py` — `10986fb1c0cc5e16c192bffb16c1b1aeea12381d232fdc465de4429a272686a4`
- `lane6-transverse-source-obstruction-20260802-v1/tame-source-coupled/verify_tame_quadratic_jet.py` — `71221a9e3f7101b233424f368ddfd38c5189b0058a92043f2d5f57f3db5b3f2d`

## `lane6-transverse-source-obstruction-20260802-v1/stratified-transverse/STRATIFIED_TRANSVERSE_CLASSIFICATION.md`

<pre><code class="language-markdown">
# Stratified transverse classification for the Program 5 rank-six source-field model

## Setting

Work over \(\mathbf Q\) with the hash-pinned eleven-variable tensor whose
source SHA-256 is

```text
a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8
```

Let \(\mathcal E\cong\mathbf A^{115}\) be the space of weight-preserving
quadratic source fields and put

\&#91;
M(P)=C+&#91;Q,P&#93;\in\operatorname{Mat}_{11\times286}.
\&#93;

Split the rows as

\&#91;
Y=(x,y,z,b,c,s),\qquad Z=(a,d,q,h,k).
\&#93;

The rank-six incidence equations are

\&#91;
Z(P)=H\,Y(P),\qquad H\in\operatorname{Mat}_{5\times6}.
\&#93;

Let \(P_0=-d^2e_a\), and let

\&#91;
\mathcal R=P_0+K_{\rm row}
\&#93;

be the exact twenty-dimensional affine row-killing family.  In the retained
basis \(\xi_0,\ldots,\xi_{19}\), write a point of \(\mathcal R\) as
\(P_0+\sum s_i\xi_i\), and set

\&#91;
\alpha=s_5,\qquad \beta=s_1,\qquad
\gamma=3s_0+2s_2-12s_{19}.
\&#93;

## Theorem

### 1. Tangent stratification

The normal tangent dimension of the rank-at-most-six source-field locus along
\(\mathcal R\) is

\&#91;
\dim T_P-20=
\begin{cases}
0,&amp;(s_3,s_4)\ne(0,0),\\
1,&amp;s_3=s_4=0,\ (\alpha,\beta,\gamma)\ne(0,0,0),\\
2,&amp;s_3=s_4=\alpha=\beta=\gamma=0.
\end{cases}
\&#93;

On the middle stratum the normal tangent is represented by \(E_{q,y}\).  On
the deepest stratum the normal plane is
\(\langle E_{q,y},E_{k,y}\rangle\).

### 2. Middle-stratum transverse rigidity

At every point of the tangent-excess-one stratum, every formal incidence arc
whose first derivative has nonzero normal component is obstructed by parameter
order at most four.

The proof is uniform in all row-family parameters.  It uses the sparse
functionals

\&#91;
\lambda=&#91;q:ady&#93;,\qquad
\mu=&#91;q:adq&#93;,\qquad
\omega=&#91;q:adq&#93;-&#91;q:d^2y&#93;
\&#93;

and the five-coordinate dual functional

\&#91;
\ell=-&#91;d:axy&#93;+\frac12&#91;d:d^3&#93;-\frac12&#91;q:d^2q&#93;
     +\frac12&#91;h:ax^2&#93;-\frac12&#91;h:d^2h&#93;.
\&#93;

Lower compatibility forces the distinguished first-order row coefficient
\(a_4=1\).  The exact recurrence then gives

\&#91;
\rho(P_2)=\frac12,\qquad b(P_2)=0,\qquad
x(P_3)=\frac12,
\&#93;

while the order-four \(&#91;q:ady&#93;\) equation requires \(x(P_3)=0\).

The same \(E_{q,y}\) argument remains valid at the deepest specialization.

### 3. Deepest-stratum finite normal directions

Normalize a finite normal direction as

\&#91;
H_1=rE_{q,y}+E_{k,y}.
\&#93;

Second-order compatibility forces

\&#91;
a_3=0,\quad a_4=r,\quad a_5=0,
\&#93;

\&#91;
3a_0+2a_2-12a_{19}=4s_2r-18s_2+12,
\qquad
a_1=-24-\frac{s_2(r+30)}3,
\&#93;

and leaves a fifteen-dimensional row fibre.

For \(r\ne0\), a polynomial cubic left-null witness has pairing

\&#91;
\frac{r(r^2+24s_2+48)}2.
\&#93;

Thus the cubic equation fails unless

\&#91;
r^2+24s_2+48=0.
\&#93;

On this exceptional hypersurface the sparse recurrence gives

\&#91;
x(P_3)=\frac{r^3}{2},
\&#93;

and the order-four \(&#91;q:ady&#93;\) equation becomes

\&#91;
0=-r x(P_3)=-\frac{r^4}{2},
\&#93;

which is impossible for \(r\ne0\).

For \(r=0\), the specialized cubic pairing is

\&#91;
12(s_2+2).
\&#93;

Hence the only remaining base locus is \(s_2=-2\).  On that locus the exact
quartic scalar is

\&#91;
96-12a_2.
\&#93;

Consequently all remaining first jets are obstructed at order four unless
\(a_2=8\).

### 4. Exact integration of the residual locus

Define the fourteen-dimensional row subspace

\&#91;
W=\left\langle
\xi_6,\ldots,\xi_{18},\ 4\xi_0+\xi_{19}
\right\rangle.
\&#93;

It satisfies

\&#91;
Z(W)=0,\qquad E_{k,y}Y(W)=0.
\&#93;

Put

\&#91;
P_\dagger=P_0+\frac43\xi_0-2\xi_2.
\&#93;

There are explicit quadratic fields \(P_1,A,B\) such that, for every
\(R_0\in W\) and every \(W\)-valued rational function \(R(t)\) regular at
\(t=0\) with \(R(0)=0\),

\&#91;
P(t)=P_\dagger+R_0+R(t)
+tP_1+\frac{t^2}{1-t}A+\frac{t^2}{1-4t}B
\&#93;

satisfies the exact rational identity

\&#91;
\boxed{
Z(P(t))=\frac{t}{1-t}E_{k,y}Y(P(t)).
}
\&#93;

Therefore

\&#91;
\operatorname{rank}M(P(t))\le6
\&#93;

identically over \(\mathbf Q(t)\).  The tangent has nonzero
\(E_{k,y}\)-normal component, so the curve is genuinely transverse to
\(\mathcal R\).

At the specialization \(R_0=R(t)=0\), the fixed active minor equals

\&#91;
\frac{
6(12t^2-5t+2)
(40448t^5+18784t^4-15984t^3+2896t^2-721t+45)
}{(t-1)(4t-1)^2},
\&#93;

whose value at \(t=0\) is \(-540\).  Hence the rank is generically exactly
six.

This integrates the complete residual first-jet locus: the condition
\(a_2=8\) fixes the non-\(W\) row coordinate, while the other fourteen row
coordinates are precisely the freely superposable \(W\)-directions.

## Explicit fields

With \(e_x,\ldots,e_k\) denoting the output coordinate vectors,

\&#91;
P_\dagger=
-d^2e_a+hk\,e_b
+\frac23(ac+2az+ds-4y^2)e_c
-2xz\,e_q.
\&#93;

The transverse first coefficient is

\&#91;
\begin{aligned}
P_1={}&amp;-2hk\,e_x
+4(-bc-2bz-dq+3xz)e_y\\
&amp;+2(-2ac-4az-2ds+dz+11y^2)e_z
-4d^2e_a\\
&amp;+2(-bd+6dx-2hk)e_b
-\frac43(-4ac-8az-4ds+3dz+7y^2)e_c\\
&amp;-4xy\,e_d
+2(bc+4bz+6cx+4xz)e_q
-4x^2e_h\\
&amp;+\frac13(3bc+4bz-6cx+3dq)e_k.
\end{aligned}
\&#93;

The two tail coefficients are

\&#91;
\begin{aligned}
A={}&amp;6hk\,e_x
+12(bc+2bz+dq-3xz)e_y\\
&amp;+12(ac+2az+ds-4y^2)e_z+12d^2e_a\\
&amp;+12(-2ac-4az-2ds+5y^2)e_c+12xy\,e_d\\
&amp;-12(bz+3cx)e_q+12x^2e_h\\
&amp;+\frac13(-bc-8bz+18cx+3dq)e_k,
\end{aligned}
\&#93;

\&#91;
B=12(-cd-2dz+4y^2)e_z
-12b(a-3d)e_b
-12b(c+s+2z)e_q
+\frac43b(4c+11z)e_k.
\&#93;

## Proof of the rational identity

The coefficient sequences reconstructed from exact lifting satisfy

\&#91;
H_n=E_{k,y}\quad(n\ge1),
\&#93;

and

\&#91;
P_n=A+4^{n-2}B\quad(n\ge2).
\&#93;

Summing gives

\&#91;
H(t)=\frac{t}{1-t}E_{k,y},
\qquad
\Delta P(t)=tP_1+\frac{t^2}{1-t}A+\frac{t^2}{1-4t}B.
\&#93;

Direct exact multiplication verifies

\&#91;
Z(\Delta P(t))-H(t)(Y_0+Y(\Delta P(t)))=0.
\&#93;

The verifier multiplies by \((1-t)^2(1-4t)\) and checks every one of the
\(5\cdot286\) coefficients over \(\mathbf Q&#91;t&#93;\).  The identities
\(Z(W)=0\) and \(E_{k,y}Y(W)=0\) prove the stated superposition property.

## Consequence for Lane 6

The source-field rank-six locus is not transversely rigid along the entire
row-killing family.  Rigidity holds on the middle stratum and on all deepest
normal directions except the explicitly described residual locus, but that
locus contains a large exact rational family.

For the canonical subfamily with \(R(t)=0\), uniformly over every base \(R_0\in W\), the stored quartic compression functional does **not** vanish:

\&#91;
\boxed{\Lambda_4\equiv1.}
\&#93;

Thus the curve is a genuine rank-six construction but not, by itself, a
compression solution.

## Boundary

The theorem is exact only in the pinned 115-dimensional quadratic
source-field incidence model.  It does not prove that the source fields
integrate to polynomial automorphisms, does not impose the full moving-target
or stable-presentation quotient, does not solve the separate compression
functional, and does not establish a global \(19\to18\) realization.
</code></pre>

## `lane6-transverse-source-obstruction-20260802-v1/tame-source-coupled/TAME_SOURCE_COUPLED_QUARTIC_OBSTRUCTION.md`

<pre><code class="language-markdown">
# A tame, full-quadratic source-coupled quartic obstruction on the residual rank-six branch

## Setting

Work over \(\mathbf Q\) with the pinned eleven-variable Keller map

\&#91;
F=X+Q+C
\&#93;

whose public source has SHA-256

```text
a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8
```

and with the complete space

\&#91;
\mathcal E_2=V\otimes\operatorname{Sym}^2(V^*)
\&#93;

of homogeneous quadratic source fields.  Thus \(\dim\mathcal E_2=11\binom{12}{2}=726\).
For \(P\in\mathcal E_2\), the cubic change in the conjugacy normal form is

\&#91;
C_P=C+&#91;Q,P&#93;,
\qquad
&#91;Q,P&#93;=JQ\,P-JP\,Q.
\&#93;

Split the cubic-coordinate matrix into the six active rows

\&#91;
Y=(x,y,z,b,c,s)
\&#93;

and the five normal rows

\&#91;
Z=(a,d,q,h,k).
\&#93;

The preceding transverse-classification theorem produced an exact rational
rank-six branch satisfying

\&#91;
Z(P(t))=\frac{t}{1-t}E_{k,y}Y(P(t)).
\&#93;

The present theorem addresses two defects left open there:

1. whether this branch is compatible with actual polynomial source
   automorphisms at quadratic order; and
2. whether its quartic obstruction survives source coupling beyond the
   115-dimensional weight-zero slice and survives an arbitrary quartic target
   correction after the lower target jets have been fixed.

## Divergence-free representative

Let \(P_\dagger,P_1,A,B\) be the exact fields in the rational-curve
certificate.  In the retained row basis \(\xi_0,\ldots,\xi_{19}\), set

\&#91;
\begin{aligned}
P^{\mathrm{sp}}(t)={}&amp;P_\dagger-\frac23\xi_{12}
+t\left(P_1+\frac83\xi_{12}\right)
+\frac{t^2}{1-t}A\\
&amp;+\frac{t^2}{1-4t}
  \left(B+12\xi_{12}-12\xi_{14}\right).
\end{aligned}
\&#93;

The difference from the original branch is an invisible row-killing motion:

\&#91;
Z(\Delta P)=0,
\qquad
E_{k,y}Y(\Delta P)=0.
\&#93;

Hence the exact rank-six incidence identity is unchanged.  Direct
calculation gives

\&#91;
\operatorname{div}P^{\mathrm{sp}}(t)=0.
\&#93;

## Lemma: every divergence-free quadratic jet is tame

Let \(P\) be a homogeneous quadratic vector field on \(\mathbf A^n\) with
\(\operatorname{div}P=0\).  Then

\&#91;
P=\sum_j c_jv_j\ell_j^2,
\qquad
\ell_j(v_j)=0.
\&#93;

Each summand is the quadratic jet of the elementary shear

\&#91;
x\longmapsto x+c_jv_j\ell_j(x)^2,
\&#93;

whose inverse is obtained by replacing \(c_j\) by \(-c_j\).  Therefore \(P\)
is the quadratic jet of a finite product of tame determinant-one polynomial
automorphisms.

### Proof

For \(i\ne j\), pair every term \(b_{ij}x_ix_je_i\) with the companion forced
by divergence-freeness.  The elementary identity

\&#91;
\begin{aligned}
x_ix_je_i-\frac12x_j^2e_j
={}&amp;-\frac14(e_i+e_j)(x_i-x_j)^2\\
&amp;+\frac14(e_i-e_j)(x_i+x_j)^2
 +\frac12e_jx_i^2
\end{aligned}
\&#93;

expresses that pair as three required shears.  After all such terms are
removed, the \(i\)-th component is independent of \(x_i\).  Every remaining
mixed monomial is polarized by

\&#91;
x_jx_k=\frac14\big((x_j+x_k)^2-(x_j-x_k)^2\big),
\&#93;

and every square already has the required form.  The verifier implements this
construction and reconstructs \(P^{\mathrm{sp}}(t)\) from 71 exact shear
terms.

## The full special invisible source space

Define

\&#91;
\mathcal W_{\mathrm{sp}}
=
\left\{
W\in\mathcal E_2:
Z(W)=0,
\ E_{k,y}Y(W)=0,
\ \operatorname{div}W=0
\right\}.
\&#93;

The first two equations ensure that adding \(W\) preserves the exact incidence
identity; the third is the first-jet condition for a special polynomial
automorphism.  Exact weight-block row reduction gives

\&#91;
\boxed{\dim\mathcal W_{\mathrm{sp}}=60.}
\&#93;

Its dimensions by operation weight are

\&#91;
\begin{array}{c|rrrrrrrrrrrrr}
w&amp;-6&amp;-5&amp;-4&amp;-3&amp;-2&amp;-1&amp;0&amp;1&amp;2&amp;3&amp;4&amp;5&amp;6\\
\hline
\dim(\mathcal W_{\mathrm{sp}})_w
&amp;0&amp;0&amp;0&amp;0&amp;3&amp;6&amp;12&amp;11&amp;12&amp;8&amp;5&amp;2&amp;1.
\end{array}
\&#93;

By the lemma, every point of

\&#91;
P^{\mathrm{sp}}(t)+\mathcal W_{\mathrm{sp}}
\&#93;

is an admissible quadratic jet of a tame special polynomial source
automorphism.

## The divergence obstruction quotient

For a quadratic source field \(P\), let \(\mathcal O_4(P)\) be the exact
quartic conjugacy forcing

\&#91;
\begin{aligned}
\mathcal O_4(P)={}&amp;JC\,P-JP\,C
+\frac12D^2Q(P,P)\\
&amp;-JP\big(JQ\,P-JP\,Q\big)
-\frac12D^2P(Q,Q).
\end{aligned}
\&#93;

An arbitrary cubic source correction \(U_3\) changes the quartic term by
\(&#91;Q,U_3&#93;\).  Since \(\operatorname{div}Q=0\),

\&#91;
\operatorname{div}&#91;Q,U_3&#93;
=-Q\cdot\nabla(\operatorname{div}U_3).
\&#93;

An additional target automorphism whose first nonlinear term is a homogeneous
quartic field \(T_4\) satisfies

\&#91;
\operatorname{div}T_4=0.
\&#93;

Consequently divergence maps the source/target quartic quotient to

\&#91;
\mathcal H_Q
=
\frac{\operatorname{Sym}^3(V^*)}
     {(Q\cdot\nabla)\operatorname{Sym}^2(V^*)}.
\&#93;

The transport map

\&#91;
(Q\cdot\nabla):\operatorname{Sym}^2(V^*)
\longrightarrow\operatorname{Sym}^3(V^*)
\&#93;

has exact rank \(65\), one-dimensional kernel \(\langle b^2\rangle\), and
cokernel dimension \(221\).

Define two dual classes on cubic polynomials by

\&#91;
\chi_1=&#91;bsx&#93;,
\qquad
\chi_0=&#91;dqx&#93;-2&#91;hky&#93;.
\&#93;

Both annihilate \((Q\cdot\nabla)\operatorname{Sym}^2(V^*)\).  The second
identity has a particularly sparse audit: the only quadratic monomial whose
transport has a nonzero \(dqx\) or \(hky\) coefficient is \(xy\), and

\&#91;
&#91;dqx&#93;(Q\cdot\nabla(xy))=-1,
\qquad
&#91;hky&#93;(Q\cdot\nabla(xy))=-\frac12.
\&#93;

For a quartic vector field \(R\), use the corresponding divergence
functionals

\&#91;
\widehat\chi_1(R)=&#91;bsx&#93;\operatorname{div}R,
\qquad
\widehat\chi_0(R)=(&#91;dqx&#93;-2&#91;hky&#93;)\operatorname{div}R.
\&#93;

They annihilate every cubic source correction and every divergence-free
quartic target correction.

## Exact values on the branch

For \(P^{\mathrm{sp}}(t)\),

\&#91;
\boxed{
\widehat\chi_1(\mathcal O_4)
=\frac{12t^2}{4t-1},
}
\&#93;

and

\&#91;
\boxed{
\widehat\chi_0(\mathcal O_4)
=-\frac{336t^3-392t^2+71t-12}
        {(t-1)(4t-1)}.
}
\&#93;

The denominator-cleared values generate the unit ideal.  Explicitly,

\&#91;
\begin{aligned}
&amp;(23856t^2-23800t+337)
 (4t-1)\widehat\chi_1(\mathcal O_4)\\
&amp;\quad +(852t+144)(t-1)(4t-1)
 \widehat\chi_0(\mathcal O_4)
=1728.
\end{aligned}
\&#93;

Thus the two obstruction classes never vanish simultaneously anywhere the
rational branch is defined.

## Uniformity under all 60 source directions

The functionals have weight zero, while \(\mathcal O_4\) is linear plus
quadratic in its source field.  Hence only the following polarizations can
contribute:

\&#91;
P^{\mathrm{sp}}\times(\mathcal W_{\mathrm{sp}})_0,
\quad
\operatorname{Sym}^2(\mathcal W_{\mathrm{sp}})_0,
\quad
(\mathcal W_{\mathrm{sp}})_{-1}\times
(\mathcal W_{\mathrm{sp}})_1,
\quad
(\mathcal W_{\mathrm{sp}})_{-2}\times
(\mathcal W_{\mathrm{sp}})_2.
\&#93;

The exact verifier checks respectively

\&#91;
12,\ 78,\ 66,\ 36
\&#93;

polarizations.  Every value is zero.  All remaining weight combinations
vanish formally by grading.  Therefore

\&#91;
\widehat\chi_i\big(\mathcal O_4(P^{\mathrm{sp}}(t)+W)\big)
=
\widehat\chi_i\big(\mathcal O_4(P^{\mathrm{sp}}(t))\big)
\&#93;

for \(i=0,1\) and every \(W\in\mathcal W_{\mathrm{sp}}\), including
parameter-dependent \(W\).

## Theorem

Let \(t\ne1,\frac14\), and let
\(W(t)\in\mathcal W_{\mathrm{sp}}\otimes\mathbf Q(t)\).  Then:

1. \(P^{\mathrm{sp}}(t)+W(t)\) preserves the exact rational rank-six
   incidence identity;
2. it is the quadratic jet of a tame special polynomial source automorphism;
3. for every cubic source correction \(U_3\) and every divergence-free
   quartic target jet \(T_4\),

   \&#91;
   \mathcal O_4(P^{\mathrm{sp}}(t)+W(t))+&#91;Q,U_3&#93;+T_4\ne0.
   \&#93;

Equivalently, the residual branch is uniformly obstructed at quartic order in
the quotient by the complete 60-dimensional special quadratic source
coupling, arbitrary cubic source corrections, and arbitrary additional
quartic target automorphisms in the fixed lower-target gauge.

## Boundary

This theorem is exact but not stable or global.

- Moving quadratic or cubic target jets can change the lower normal form and
  are not included.
- Adding stable variables can absorb divergence in new coordinates, so the
  two classes are not stable invariants.
- The result concerns the pinned eleven-variable conjugacy/incidence model; it
  does not prove a global \(19\to18\) noncompression theorem.

The theorem nevertheless closes the principal admissibility gap on the exact
residual branch and enlarges the source coupling from the 115-dimensional
weight-zero model to all 726 quadratic fields, with a complete exact
60-dimensional special invisible coupling space.
</code></pre>

## `lane6-transverse-source-obstruction-20260802-v1/stratified-transverse/verify_uniform_middle_stratum.py`

<pre><code class="language-python">
#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import core_model as m


def normal(e: sp.Expr) -&gt; sp.Expr:
    return sp.factor(sp.cancel(e))


def sparse_support(vec: sp.Matrix) -&gt; list&#91;tuple&#91;int, str&#93;&#93;:
    return &#91;(i, str(normal(e))) for i, e in enumerate(vec) if normal(e) != 0&#93;


def block_solve_components(A: sp.Matrix, b: sp.Matrix) -&gt; sp.Matrix:
    unseen = set(range(A.rows))
    x = sp.zeros(A.cols, b.cols)
    while unseen:
        rows = {unseen.pop()}
        cols: set&#91;int&#93; = set()
        changed = True
        while changed:
            changed = False
            new_cols = {j for i in rows for j in range(A.cols) if A&#91;i, j&#93; != 0}
            if not new_cols &lt;= cols:
                cols |= new_cols
                changed = True
            new_rows = {i for j in cols for i in range(A.rows) if A&#91;i, j&#93; != 0}
            if not new_rows &lt;= rows:
                rows |= new_rows
                unseen -= new_rows
                changed = True
        rr, cc = sorted(rows), sorted(cols)
        Ab = A&#91;rr, cc&#93;
        bb = b&#91;rr, :&#93;
        if all(e == 0 for e in bb):
            continue
        assert Ab.rows == Ab.cols
        sol = Ab.inv() * bb
        for ii, j in enumerate(cc):
            for k in range(b.cols):
                x&#91;j, k&#93; = normal(sol&#91;ii, k&#93;)
    return x


def coordinate(row_name: str, monomial: sp.Expr) -&gt; int:
    rr = m.V.index(sp.Symbol(row_name))
    lr = m.selected_rows.index(rr)
    return lr * len(m.cubics) + m.mon_index(monomial)


def raw_functional(entries: list&#91;tuple&#91;str, sp.Expr, sp.Rational&#93;&#93;) -&gt; sp.Matrix:
    out = sp.zeros(1, 5 * len(m.cubics))
    for row_name, monomial, coeff in entries:
        out&#91;0, coordinate(row_name, monomial)&#93; = coeff
    return out


def bilinear_matrix(functional: sp.Matrix) -&gt; sp.Matrix:
    B = sp.zeros(30, 115)
    for hi in range(30):
        zr, ar = divmod(hi, 6)
        for pj, M in enumerate(m.variation_matrices):
            value = 0
            offset = zr * len(m.cubics)
            for c in range(len(m.cubics)):
                fc = functional&#91;0, offset + c&#93;
                if fc and M&#91;m.base_rows&#91;ar&#93;, c&#93;:
                    value += fc * M&#91;m.base_rows&#91;ar&#93;, c&#93;
            B&#91;hi, pj&#93; = normal(value)
    return B


def functional_on_HY0(functional: sp.Matrix, Y0: sp.Matrix) -&gt; sp.Matrix:
    out = sp.zeros(1, 30)
    for hi in range(30):
        zr, ar = divmod(hi, 6)
        value = 0
        offset = zr * len(m.cubics)
        for c in range(len(m.cubics)):
            if functional&#91;0, offset + c&#93;:
                value += functional&#91;0, offset + c&#93; * Y0&#91;ar, c&#93;
        out&#91;0, hi&#93; = normal(value)
    return out


def main() -&gt; int:
    s = sp.symbols("s0:20")
    alpha = s&#91;5&#93;
    beta = s&#91;1&#93;
    gamma = 3 * s&#91;0&#93; + 2 * s&#91;2&#93; - 12 * s&#91;19&#93;

    S = sp.zeros(115, 1)
    for i in range(20):
        if i not in (3, 4):
            S += s&#91;i&#93; * m.row&#91;i&#93;
    Y0 = (m.M0 + m.variation(S))&#91;m.base_rows, :&#93;

    h1 = sp.zeros(30, 1)
    h1&#91;13&#93; = 1
    N = m.solveZ(m.Rvec(h1, Y0))

    key_ops = {
        "e_y*a*y": 10,
        "e_d*a*d": 68,
        "e_q*a*y": 77,
        "e_q*d*y": 78,
        "e_q*a*q": 80,
        "e_q*a*k": 81,
        "e_z*q*y": 20,
        "e_c*q*y": 51,
        "e_d*b*y": 65,
    }
    assert all(m.labels&#91;i&#93; == name for name, i in key_ops.items())
    assert all(normal(N&#91;i&#93;) == 0 for i in (10, 68, 77, 78, 80))
    assert normal(N&#91;81&#93; + alpha) == 0
    assert normal(N&#91;20&#93;) == 0
    assert normal(N&#91;51&#93; - sp.Rational(1, 3)) == 0
    assert normal(N&#91;65&#93;) == 0

    # Four sparse raw functionals.
    lam = raw_functional(&#91;("q", m.a * m.d * m.y, sp.Rational(1))&#93;)
    mu = raw_functional(&#91;("q", m.a * m.d * m.q, sp.Rational(1))&#93;)
    omega = raw_functional(&#91;
        ("q", m.a * m.d * m.q, sp.Rational(1)),
        ("q", m.d**2 * m.y, sp.Rational(-1)),
    &#93;)
    adk = raw_functional(&#91;("q", m.a * m.d * m.k, sp.Rational(1))&#93;)
    bqy = raw_functional(&#91;("k", m.b * m.q * m.y, sp.Rational(1))&#93;)

    # Exact dual functional ell with ell Z = rho.
    ell = raw_functional(&#91;
        ("d", m.a * m.x * m.y, sp.Rational(-1)),
        ("d", m.d**3, sp.Rational(1, 2)),
        ("q", m.d**2 * m.q, sp.Rational(-1, 2)),
        ("h", m.a * m.x**2, sp.Rational(1, 2)),
        ("h", m.d**2 * m.h, sp.Rational(-1, 2)),
    &#93;)
    rho = sp.zeros(1, 115)
    rho&#91;0, 10&#93; = 1
    for i in (68, 78, 80):
        rho&#91;0, i&#93; = -sp.Rational(1, 2)
    assert (ell * m.Z - rho) == sp.zeros(1, 115)

    # Support identities.
    assert lam * m.Z == sp.zeros(1, 115)
    assert omega * m.Z == sp.zeros(1, 115)
    assert adk * m.Z == sp.zeros(1, 115)
    assert bqy * m.Z == sp.zeros(1, 115)
    assert mu * m.Z == sp.eye(1, 115)&#91;:, :&#93; * 0 + sp.Matrix(&#91;&#91;1 if j == 77 else 0 for j in range(115)&#93;&#93;)

    B_lam = bilinear_matrix(lam)
    B_mu = bilinear_matrix(mu)
    B_omega = bilinear_matrix(omega)
    B_adk = bilinear_matrix(adk)
    B_bqy = bilinear_matrix(bqy)
    B_ell = bilinear_matrix(ell)

    expected_lam = sp.zeros(30, 115); expected_lam&#91;13, 77&#93; = -1
    expected_mu = sp.zeros(30, 115)
    expected_mu&#91;13, 10&#93; = 1; expected_mu&#91;13, 68&#93; = -1; expected_mu&#91;13, 80&#93; = -1
    expected_omega = sp.zeros(30, 115)
    expected_omega&#91;13, 68&#93; = -1; expected_omega&#91;13, 78&#93; = 1; expected_omega&#91;13, 80&#93; = -1
    expected_adk = sp.zeros(30, 115); expected_adk&#91;13, 81&#93; = -1
    expected_bqy = sp.zeros(30, 115)
    expected_bqy&#91;25, 20&#93; = -2; expected_bqy&#91;25, 51&#93; = -1; expected_bqy&#91;25, 65&#93; = -1
    assert B_lam == expected_lam
    assert B_mu == expected_mu
    assert B_omega == expected_omega
    assert B_adk == expected_adk
    assert B_bqy == expected_bqy

    # Functional values on the moving row-family base.
    assert functional_on_HY0(lam, Y0) == sp.zeros(1, 30)
    assert functional_on_HY0(adk, Y0) == sp.zeros(1, 30)
    assert functional_on_HY0(ell, Y0) == sp.zeros(1, 30)
    omega_Y0 = functional_on_HY0(omega, Y0)
    mu_Y0 = functional_on_HY0(mu, Y0)
    bqy_Y0 = functional_on_HY0(bqy, Y0)
    assert normal(omega_Y0&#91;0, 13&#93;) == 0  # s3 was set to zero in S.
    assert normal(mu_Y0&#91;0, 13&#93;) == 0
    assert normal(bqy_Y0&#91;0, 25&#93;) == 0  # s4 was set to zero in S.
    assert all(omega_Y0&#91;0, j&#93; == 0 for j in range(30))
    assert all(mu_Y0&#91;0, j&#93; == 0 for j in range(30))
    assert all(bqy_Y0&#91;0, j&#93; == 0 for j in range(30))

    # Values of the sparse operation covectors on N and the row basis.
    xcov = sp.zeros(1, 115); xcov&#91;0, 77&#93; = 1
    dcov = sp.zeros(1, 115); dcov&#91;0, 10&#93; = 1; dcov&#91;0, 68&#93; = -1; dcov&#91;0, 80&#93; = -1
    bcov = sp.zeros(1, 115); bcov&#91;0, 68&#93; = -1; bcov&#91;0, 78&#93; = 1; bcov&#91;0, 80&#93; = -1
    assert normal((xcov * N)&#91;0&#93;) == 0
    assert normal((dcov * N)&#91;0&#93;) == 0
    assert normal((bcov * N)&#91;0&#93;) == 0
    assert &#91;(j, normal((dcov * r)&#91;0&#93;)) for j, r in enumerate(m.row) if normal((dcov * r)&#91;0&#93;) != 0&#93; == &#91;(3, 1)&#93;
    assert &#91;(j, normal((bcov * r)&#91;0&#93;)) for j, r in enumerate(m.row) if normal((bcov * r)&#91;0&#93;) != 0&#93; == &#91;(3, 2)&#93;
    assert all(normal((xcov * r)&#91;0&#93;) == 0 for r in m.row)

    ell_N = normal((ell * m.Rvec(h1, m.Yof(N)))&#91;0&#93;)
    ell_rows = &#91;normal((ell * m.Rvec(h1, m.Yof(r)))&#91;0&#93;) for r in m.row&#93;
    assert ell_N == 0
    assert &#91;(j, v) for j, v in enumerate(ell_rows) if v != 0&#93; == &#91;(4, sp.Rational(1, 2))&#93;

    # The order-two normal incidence equations after eliminating the 28 fixed
    # pivot H-coordinates. This calculation keeps all eighteen middle-stratum
    # row-base parameters symbolic.
    Kfull = sp.Matrix.hstack(*&#91;m.projZ(m.Rvec(sp.eye(30)&#91;:, j&#93;, Y0)) for j in range(30)&#93;)
    active = sorted({i for j in range(30) for i, e in enumerate(Kfull&#91;:, j&#93;) if e != 0})
    K = Kfull&#91;active, :&#93;
    K0 = K.subs({x: 0 for x in s})
    cp = list(DomainMatrix.from_Matrix(K0, fmt="sparse").rref()&#91;1&#93;)
    rp = list(DomainMatrix.from_Matrix(K0.T, fmt="sparse").rref()&#91;1&#93;)
    nc = &#91;j for j in range(30) if j not in cp&#93;
    nr = &#91;i for i in range(K.rows) if i not in rp&#93;
    assert nc == &#91;13, 25&#93;
    A = K&#91;rp, cp&#93;
    B = K&#91;rp, nc&#93;
    C = K&#91;nr, cp&#93;
    D = K&#91;nr, nc&#93;
    X = block_solve_components(A, B)
    Mred = (D - C * X).applyfunc(normal)

    def reduce_forcing(qfull: sp.Matrix) -&gt; sp.Matrix:
        q = qfull&#91;active, :&#93;
        xp = block_solve_components(A, q&#91;rp, :&#93;)
        return (q&#91;nr, :&#93; - C * xp).applyfunc(normal)

    qN = reduce_forcing(-m.projZ(m.Rvec(h1, m.Yof(N))))
    q3 = reduce_forcing(-m.projZ(m.Rvec(h1, m.Yof(m.row&#91;3&#93;))))
    q4 = reduce_forcing(-m.projZ(m.Rvec(h1, m.Yof(m.row&#91;4&#93;))))
    a3, a4 = sp.symbols("a3 a4")
    qord2 = (qN + a3 * q3 + a4 * q4).applyfunc(normal)

    # Locate the two reduced normal equations by expression, not by a fragile
    # row number.  The independent a3 equation is the raw omega functional
    # below rather than a row of this secondary Schur reduction.
    eq_first = &#91;&#93;
    eq_second = &#91;&#93;
    for i in range(Mred.rows):
        m13, m25 = normal(Mred&#91;i, 0&#93;), normal(Mred&#91;i, 1&#93;)
        rhs = normal(qord2&#91;i, 0&#93;)
        if m13 == 0 and normal(m25 - (beta + 2 * gamma) / 2) == 0 and normal(rhs - (1 + 9 * a3 - a4) / 6) == 0:
            eq_first.append(i)
        if m13 == 0 and normal(m25 - (3 * beta + 4 * gamma) / 6) == 0 and normal(rhs - (1 + 9 * a3 - a4) / 6) == 0:
            eq_second.append(i)
    assert len(eq_first) == len(eq_second) == 1

    # The raw omega equation at order two is exactly 2*a3=0.
    p1_symbolic = N + a3 * m.row&#91;3&#93; + a4 * m.row&#91;4&#93;
    omega_order_two = normal((omega * m.Rvec(h1, m.Yof(p1_symbolic)))&#91;0&#93;)
    assert normal(omega_order_two - 2 * a3) == 0

    # q:adk at order two is the pure equation alpha=0.
    assert normal((adk * m.Rvec(h1, m.Yof(N)))&#91;0&#93; - alpha) == 0
    assert all(normal((adk * m.Rvec(h1, m.Yof(r)))&#91;0&#93;) == 0 for r in m.row)

    # On gamma=0, the remaining cubic raw equation is the exact square.
    # From the reduced order-two equations, t=(1-a4)/(3 beta).
    t = sp.symbols("t")
    p1_key = N + a4 * m.row&#91;4&#93;
    combo = normal(-2 * p1_key&#91;20&#93; - p1_key&#91;51&#93; - p1_key&#91;65&#93;)
    combo_gamma0 = normal(combo.subs({alpha: 0, gamma: 0}))
    assert normal(combo_gamma0 - (a4 - 1) / 3) == 0
    cubic_square = normal(((1 - a4) / (3 * beta)) * combo_gamma0)
    assert normal(cubic_square + (a4 - 1) ** 2 / (9 * beta)) == 0

    # Formal recurrence certificate. Once lower compatibility forces a3=0 and
    # a4=1, the identities imply x(P3)=1/2 while q:ady at order four requires
    # x(P3)=0.
    recurrence = {
        "order2": {
            "q_adk": "alpha = 0",
            "omega": "a3 = 0",
            "normal_equations": &#91;
                "3*(beta+2*gamma)*t = 1-a4",
                "(3*beta+4*gamma)*t = 1-a4",
            &#93;,
        },
        "gamma_nonzero": "a4 = 1 at order two",
        "gamma_zero_beta_nonzero": "k:b*q*y = -(a4-1)^2/(9*beta), hence a4=1 at order three",
        "deepest_qy_specialization": "at alpha=beta=gamma=0 the two reduced order-two equations directly give a4=1",
        "quartic_chain": &#91;
            "rho(P2)=a4/2",
            "b(P2)=0",
            "d(P2)=rho(P2)+b(P2)/2=a4/2",
            "x(P3)=d(P2)=a4/2",
            "q:a*d*y at order four gives 0=-x(P3)=-1/2",
        &#93;,
    }

    result = {
        "schema_version": 1,
        "name": "Uniform no-transverse-arc theorem on the tangent-excess-one row stratum",
        "source_sha256": "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        "middle_stratum": "s3=s4=0 and (alpha,beta,gamma)!=(0,0,0)",
        "coordinates": {
            "alpha": "s5",
            "beta": "s1",
            "gamma": "3*s0+2*s2-12*s19",
            "normal_H1": "E_(q,y)",
        },
        "exact_dual_functional_ell": {
            "support": &#91;
                &#91;"d:a*x*y", "-1"&#93;,
                &#91;"d:d^3", "1/2"&#93;,
                &#91;"q:d^2*q", "-1/2"&#93;,
                &#91;"h:a*x^2", "1/2"&#93;,
                &#91;"h:d^2*h", "-1/2"&#93;,
            &#93;,
            "operation_covector": "e_y*a*y - (e_d*a*d + e_q*d*y + e_q*a*q)/2",
        },
        "order_two_reduced_rows": {
            "a3_equation": "raw omega functional gives 2*a3=0",
            "beta_plus_2gamma_row_index": eq_first&#91;0&#93;,
            "3beta_plus_4gamma_row_index": eq_second&#91;0&#93;,
        },
        "recurrence": recurrence,
        "conclusion": (
            "For every row-family base in the tangent-excess-one stratum, "
            "every first-order transverse formal incidence arc is obstructed "
            "by parameter order at most four. The same q-normal proof extends "
            "to the deepest specialization alpha=beta=gamma=0. If alpha is nonzero it fails at "
            "order two; otherwise lower compatibility forces a4=1, while the "
            "sparse q:a*d*y recurrence gives the contradiction 0=-1/2 at "
            "order four."
        ),
        "boundary": (
            "This is exact in the pinned 115-dimensional source-field "
            "rank-six incidence model. It does not include moving target or "
            "stable-presentation operations, the separate compression "
            "functional, convergence, or the non-q-normal directions in the tangent-excess-two stratum."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result&#91;"certificate_sha256"&#93; = hashlib.sha256(payload).hexdigest()
    out = HERE / "uniform_middle_stratum_certificate.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `lane6-transverse-source-obstruction-20260802-v1/stratified-transverse/verify_deepest_finite_classification.py`

<pre><code class="language-python">
#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,sys
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import core_model as m
from verify_uniform_middle_stratum import normal,block_solve_components,raw_functional,bilinear_matrix,functional_on_HY0
# General deepest-row base.
r,s2=sp.symbols('r s2')
base_extra=sp.symbols('s6:20')
base={2:s2}
for z,i in zip(base_extra,range(6,20)):base&#91;i&#93;=z
base&#91;0&#93;=(12*base&#91;19&#93;-2*s2)/3
S=sum((co*m.row&#91;i&#93; for i,co in base.items()),sp.zeros(115,1))
Y0=(m.M0+m.variation(S))&#91;m.base_rows,:&#93;
h1=sp.zeros(30,1);h1&#91;13&#93;=r;h1&#91;25&#93;=1
N=m.solveZ(m.Rvec(h1,Y0))
# General order-two-compatible first derivative.  The free coordinates span W.
a2=sp.symbols('a2');aextra=sp.symbols('a6:20')
a={2:a2}
for z,i in zip(aextra,range(6,20)):a&#91;i&#93;=z
g=4*s2*r-18*s2+12
a&#91;0&#93;=(g-2*a2+12*a&#91;19&#93;)/3
a&#91;1&#93;=-24-s2*(r+30)/3
a&#91;3&#93;=0;a&#91;4&#93;=r;a&#91;5&#93;=0
P1=N+sum((co*m.row&#91;i&#93; for i,co in a.items()),sp.zeros(115,1))
# Incidence map K and exact order-two solve.
K=sp.Matrix.hstack(*&#91;m.projZ(m.Rvec(sp.eye(30)&#91;:,j&#93;,Y0)) for j in range(30)&#93;)
zero_sub={s2:0,**{z:0 for z in base_extra}}
K0=K.subs(zero_sub)
cp=list(DomainMatrix.from_Matrix(K0,fmt='sparse').rref()&#91;1&#93;);rp=list(DomainMatrix.from_Matrix(K0.T,fmt='sparse').rref()&#91;1&#93;);nc=&#91;j for j in range(30) if j not in cp&#93;;A=K&#91;rp,cp&#93;
assert nc==&#91;13,25&#93;
def solveK(rhs):
 co=block_solve_components(A,rhs&#91;rp,:&#93;);h=sp.zeros(30,rhs.cols)
 for ii,j in enumerate(cp):
  for c in range(rhs.cols):h&#91;j,c&#93;=normal(co&#91;ii,c&#93;)
 assert (K*h-rhs).applyfunc(normal)==sp.zeros(K.rows,rhs.cols);return h
def projK(v):
 co=block_solve_components(A,v&#91;rp,:&#93;);return (v-K&#91;:,cp&#93;*co).applyfunc(normal)
q2=-m.projZ(m.Rvec(h1,m.Yof(P1)));h2=solveK(q2);p2=m.solveZ(m.Rvec(h2,Y0)+m.Rvec(h1,m.Yof(P1)))
# Complete homogeneous order-two freedom and cubic system.
corr=&#91;&#93;
for j in nc:
 dh=sp.eye(30)&#91;:,j&#93;;dp=m.solveZ(m.Rvec(dh,Y0));corr.append((f'h{j}',dh,dp))
for j,rj in enumerate(m.row):corr.append((f'row{j}',sp.zeros(30,1),rj))
base3=projK(m.projZ(m.Rvec(h2,m.Yof(P1))+m.Rvec(h1,m.Yof(p2))))
cols=&#91;projK(m.projZ(m.Rvec(dh,m.Yof(P1))+m.Rvec(h1,m.Yof(dp)))) for _,dh,dp in corr&#93;
active=sorted({i for i,e in enumerate(base3) if e}|{i for c in cols for i,e in enumerate(c) if e})
E=sp.Matrix(&#91;&#91;c&#91;i&#93; for c in cols&#93; for i in active&#93;);rhs=sp.Matrix(&#91;-base3&#91;i&#93; for i in active&#93;)
# Polynomial generic witness: (3/2)&#91;q:adq&#93; + r&#91;k:bds&#93;.
wpoly=sp.Matrix(&#91;&#91;sp.Rational(3,2) if gi==760 else (r if gi==1361 else 0) for gi in active&#93;&#93;)
assert (wpoly*E).applyfunc(normal)==sp.zeros(1,E.cols)
pairpoly=normal((wpoly*rhs)&#91;0&#93;);assert normal(pairpoly-r*(r**2+24*s2+48)/2)==0
# Specialized r=0 witness: (3/2)&#91;k:adq&#93;+&#91;k:bds&#93;.
E0=E.subs(r,0);rhs0=rhs.subs(r,0)
w0=sp.Matrix(&#91;&#91;sp.Rational(3,2) if gi==1332 else (1 if gi==1361 else 0) for gi in active&#93;&#93;)
assert (w0*E0).applyfunc(normal)==sp.zeros(1,E.cols)
pair0=normal((w0*rhs0)&#91;0&#93;);assert normal(pair0-12*(s2+2))==0
# Sparse q-row recurrence for every r != 0.
lam=raw_functional(&#91;('q',m.a*m.d*m.y,1)&#93;)
mu=raw_functional(&#91;('q',m.a*m.d*m.q,1)&#93;)
omega=raw_functional(&#91;('q',m.a*m.d*m.q,1),('q',m.d**2*m.y,-1)&#93;)
ell=raw_functional(&#91;('d',m.a*m.x*m.y,-1),('d',m.d**3,sp.Rational(1,2)),('q',m.d**2*m.q,sp.Rational(-1,2)),('h',m.a*m.x**2,sp.Rational(1,2)),('h',m.d**2*m.h,sp.Rational(-1,2))&#93;)
for f in (lam,mu,omega,ell):assert functional_on_HY0(f,Y0)==sp.zeros(1,30)
Bl,Bm,Bo,Be=map(bilinear_matrix,(lam,mu,omega,ell))
xc=sp.zeros(1,115);xc&#91;0,77&#93;=1
dc=sp.zeros(1,115);dc&#91;0,10&#93;=1;dc&#91;0,68&#93;=-1;dc&#91;0,80&#93;=-1
bc=sp.zeros(1,115);bc&#91;0,68&#93;=-1;bc&#91;0,78&#93;=1;bc&#91;0,80&#93;=-1
tau=Be&#91;13,:&#93;
assert Bl&#91;13,:&#93;==-xc and all(Bl&#91;i,j&#93;==0 for i in range(30) for j in range(115) if i!=13)
assert Bm&#91;13,:&#93;==dc and all(Bm&#91;i,j&#93;==0 for i in range(30) for j in range(115) if i!=13)
assert Bo&#91;13,:&#93;==bc and all(Bo&#91;i,j&#93;==0 for i in range(30) for j in range(115) if i!=13)
assert all(Be&#91;i,j&#93;==0 for i in range(30) for j in range(115) if i!=13)
assert normal((xc*P1)&#91;0&#93;)==0 and normal((dc*P1)&#91;0&#93;)==0 and normal((bc*P1)&#91;0&#93;)==0
assert normal((tau*P1)&#91;0&#93;-r/2)==0
res={
 'schema_version':1,
 'name':'Deepest-stratum finite-normal cubic/quartic classification',
 'base':'s1=s3=s4=s5=0, gamma=3*s0+2*s2-12*s19=0; all remaining base parameters arbitrary',
 'finite_normal':'H1=r E_(q,y)+E_(k,y)',
 'order_two_first_derivative':{
  'a3':'0','a4':'r','a5':'0','3*a0+2*a2-12*a19':'4*s2*r-18*s2+12','a1':'-24-s2*(r+30)/3','free_subspace':'a2 and a6,...,a19 (dimension 15)'},
 'cubic':{
  'active_rows':active,'generic_polynomial_pairing':'r*(r^2+24*s2+48)/2','for_r_nonzero_obstruction_factor':'(r^2+24*s2+48)/2','r_zero_pairing':'12*(s2+2)'},
 'r_nonzero_quartic_recurrence':&#91;
  'lower lambda/mu/omega equations give x(P1)=d(P1)=b(P1)=x(P2)=b(P2)=0',
  'ell at order two gives rho(P2)=r*tau(P1)=r^2/2',
  'hence d(P2)=r^2/2 and mu at order three gives x(P3)=r^3/2',
  'lambda at order four gives 0=-r*x(P3)=-r^4/2'&#93;,
 'only_unresolved_by_these_obstructions':'r=0, s2=-2; its quartic scalar is treated by the residual-curve certificate',
 'boundary':'Pinned 115-dimensional source-field rank-six incidence model only.'}
payload=json.dumps(res,sort_keys=True,separators=(',',':')).encode();res&#91;'certificate_sha256'&#93;=hashlib.sha256(payload).hexdigest();(HERE/'deepest_finite_classification.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps(res,indent=2,sort_keys=True))
</code></pre>

## `lane6-transverse-source-obstruction-20260802-v1/tame-source-coupled/verify_residual_source_target_obstruction.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify the residual rank-six branch modulo full quadratic special-source coupling.

The calculation is exact over Q.  It works with all 726 homogeneous quadratic
source fields in eleven variables, not merely the 115-dimensional weight-zero
slice.  Along the exact residual rational branch it constructs the full space

    W_sp = {w : Z(w)=0, E_(k,y)Y(w)=0, div(w)=0},

proves dim W_sp=60, and verifies that two divergence-cokernel functionals are
unchanged by arbitrary W_sp-valued motion.  The same functionals annihilate
all cubic source homological corrections &#91;Q,U_3&#93; and every divergence-free
quartic target jet.

The target conclusion is in a fixed lower-target gauge: any additional target
automorphism is assumed to have no nonlinear terms below degree four.  Moving
quadratic/cubic target jets and stable variables are not included.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import core_model as m  # noqa: E402


def normal(value: sp.Expr) -&gt; sp.Expr:
    return sp.factor(sp.cancel(value))


def load_core_vector(payload: dict&#91;str, Any&#93;, key: str) -&gt; sp.Matrix:
    vector = sp.zeros(115, 1)
    for item in payload&#91;key&#93;:
        vector&#91;item&#91;"index"&#93;, 0&#93; = sp.Rational(item&#91;"coefficient"&#93;)
    return vector


# Full 726-dimensional homogeneous quadratic operation basis.
QUADRATICS = &#91;
    sp.prod(m.V&#91;index&#93; for index in indices)
    for indices in itertools.combinations_with_replacement(range(11), 2)
&#93;
FULL_OPERATIONS = &#91;(row, monomial) for row in range(11) for monomial in QUADRATICS&#93;
FULL_OPERATION_WEIGHTS = &#91;
    m.wt(monomial) - m.weights&#91;m.V&#91;row&#93;&#93;
    for row, monomial in FULL_OPERATIONS
&#93;
FULL_INDEX = {
    (row, sp.Poly(monomial, *m.V).monoms()&#91;0&#93;): index
    for index, (row, monomial) in enumerate(FULL_OPERATIONS)
}
CUBIC_EXPONENT_INDEX = {
    sp.Poly(monomial, *m.V).monoms()&#91;0&#93;: index
    for index, monomial in enumerate(m.cubics)
}


def full_from_core(vector: sp.Matrix) -&gt; sp.Matrix:
    result = sp.zeros(726, 1)
    for coefficient, (row, monomial) in zip(vector, m.operation_basis):
        if coefficient:
            exponent = sp.Poly(monomial, *m.V).monoms()&#91;0&#93;
            result&#91;FULL_INDEX&#91;(row, exponent)&#93;, 0&#93; = coefficient
    return result


def full_vector_field(vector: sp.Matrix) -&gt; sp.Matrix:
    field = sp.zeros(11, 1)
    for coefficient, (row, monomial) in zip(vector, FULL_OPERATIONS):
        if coefficient:
            field&#91;row, 0&#93; += coefficient * monomial
    return field


def core_vector_field(vector: sp.Matrix) -&gt; sp.Matrix:
    field = sp.zeros(11, 1)
    for coefficient, (row, monomial) in zip(vector, m.operation_basis):
        if coefficient:
            field&#91;row, 0&#93; += coefficient * monomial
    return field


def quartic_forcing(field: sp.Matrix) -&gt; sp.Matrix:
    JQ = m.Q.jacobian(m.V)
    JP = field.jacobian(m.V)
    d2_q_pp = sp.Matrix(
        &#91;(field.T * sp.hessian(m.Q&#91;i&#93;, m.V) * field)&#91;0&#93; for i in range(11)&#93;
    )
    d2_p_qq = sp.Matrix(
        &#91;(m.Q.T * sp.hessian(field&#91;i&#93;, m.V) * m.Q)&#91;0&#93; for i in range(11)&#93;
    )
    return (
        m.C.jacobian(m.V) * field
        - JP * m.C
        + sp.Rational(1, 2) * d2_q_pp
        - JP * (JQ * field - JP * m.Q)
        - sp.Rational(1, 2) * d2_p_qq
    )


ZERO = {variable: 0 for variable in m.V}


def divergence_squarefree_coefficient(
    field: sp.Matrix,
    variables: tuple&#91;sp.Symbol, sp.Symbol, sp.Symbol&#93;,
) -&gt; sp.Expr:
    return normal(
        sum(
            sp.diff(field&#91;i&#93;, m.V&#91;i&#93;, *variables).subs(ZERO)
            for i in range(11)
        )
    )


def chi_values_from_field(field: sp.Matrix) -&gt; sp.Matrix:
    chi_1 = divergence_squarefree_coefficient(field, (m.b, m.s, m.x))
    chi_0 = (
        divergence_squarefree_coefficient(field, (m.d, m.q, m.x))
        - 2 * divergence_squarefree_coefficient(field, (m.h, m.k, m.y))
    )
    return sp.Matrix(&#91;normal(chi_1), normal(chi_0)&#93;)


def chi_values(vector: sp.Matrix) -&gt; sp.Matrix:
    return chi_values_from_field(quartic_forcing(full_vector_field(vector)))


def sparse_vector(vector: sp.Matrix) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        {"index": index, "coefficient": str(normal(value))}
        for index, value in enumerate(vector)
        if normal(value) != 0
    &#93;


def build_full_special_invisible_weight_spaces() -&gt; dict&#91;int, list&#91;sp.Matrix&#93;&#93;:
    """Exact weight-block RREF for Z=0, E_(k,y)Y=0, and div=0."""
    selected_rows = &#91;3, 6, 7, 9, 10&#93;
    weights = sorted(set(FULL_OPERATION_WEIGHTS))
    columns: dict&#91;int, list&#91;dict&#91;tuple&#91;Any, ...&#93;, sp.Expr&#93;&#93;&#93; = {
        weight: &#91;&#93; for weight in weights
    }
    global_indices: dict&#91;int, list&#91;int&#93;&#93; = {weight: &#91;&#93; for weight in weights}

    for operation_index, (operation_row, monomial) in enumerate(FULL_OPERATIONS):
        weight = FULL_OPERATION_WEIGHTS&#91;operation_index&#93;
        transport = sp.expand(
            sum(sp.diff(monomial, m.V&#91;j&#93;) * m.Q&#91;j&#93; for j in range(11))
        )

        def bracket_row(output_row: int) -&gt; sp.Expr:
            value = sp.expand(
                sp.diff(m.Q&#91;output_row&#93;, m.V&#91;operation_row&#93;) * monomial
            )
            if output_row == operation_row:
                value = sp.expand(value - transport)
            return value

        column: dict&#91;tuple&#91;Any, ...&#93;, sp.Expr&#93; = {}
        for local_row, output_row in enumerate(selected_rows):
            polynomial = sp.Poly(bracket_row(output_row), *m.V, domain=sp.QQ)
            for exponent, coefficient in polynomial.terms():
                if coefficient and sum(exponent) == 3:
                    column&#91;("Z", local_row, CUBIC_EXPONENT_INDEX&#91;exponent&#93;)&#93; = coefficient

        # E_(k,y)Y(w)=0 is exactly the vanishing of the active y row.
        polynomial = sp.Poly(bracket_row(1), *m.V, domain=sp.QQ)
        for exponent, coefficient in polynomial.terms():
            if coefficient and sum(exponent) == 3:
                column&#91;("Y_y", CUBIC_EXPONENT_INDEX&#91;exponent&#93;)&#93; = coefficient

        divergence = sp.diff(monomial, m.V&#91;operation_row&#93;)
        if divergence:
            polynomial = sp.Poly(divergence, *m.V, domain=sp.QQ)
            for exponent, coefficient in polynomial.terms():
                if coefficient and sum(exponent) == 1:
                    column&#91;("div", exponent.index(1))&#93; = coefficient

        columns&#91;weight&#93;.append(column)
        global_indices&#91;weight&#93;.append(operation_index)

    spaces: dict&#91;int, list&#91;sp.Matrix&#93;&#93; = {}
    certificate_weights: dict&#91;str, Any&#93; = {}
    for weight in weights:
        row_keys = sorted(
            set().union(*(column.keys() for column in columns&#91;weight&#93;)), key=str
        )
        row_index = {key: index for index, key in enumerate(row_keys)}
        entries: dict&#91;tuple&#91;int, int&#93;, sp.Expr&#93; = {}
        for local_column, column in enumerate(columns&#91;weight&#93;):
            for key, coefficient in column.items():
                entries&#91;(row_index&#91;key&#93;, local_column)&#93; = coefficient
        matrix = sp.SparseMatrix(
            len(row_keys), len(global_indices&#91;weight&#93;), entries
        )
        reduced, pivots = matrix.rref(simplify=False)
        free_columns = &#91;
            column for column in range(matrix.cols) if column not in pivots
        &#93;
        basis: list&#91;sp.Matrix&#93; = &#91;&#93;
        for free_column in free_columns:
            local_vector = sp.zeros(matrix.cols, 1)
            local_vector&#91;free_column, 0&#93; = 1
            for pivot_row, pivot_column in enumerate(pivots):
                local_vector&#91;pivot_column, 0&#93; = -reduced&#91;pivot_row, free_column&#93;
            vector = sp.zeros(726, 1)
            for local_column, operation_index in enumerate(global_indices&#91;weight&#93;):
                vector&#91;operation_index, 0&#93; = sp.factor(local_vector&#91;local_column, 0&#93;)
            basis.append(vector)
        spaces&#91;weight&#93; = basis
        certificate_weights&#91;str(weight)&#93; = {
            "columns": matrix.cols,
            "rows": matrix.rows,
            "rank": len(pivots),
            "nullity": len(basis),
            "basis": &#91;sparse_vector(vector) for vector in basis&#93;,
        }

    expected_nullities = {
        -6: 0,
        -5: 0,
        -4: 0,
        -3: 0,
        -2: 3,
        -1: 6,
        0: 12,
        1: 11,
        2: 12,
        3: 8,
        4: 5,
        5: 2,
        6: 1,
    }
    observed = {weight: len(basis) for weight, basis in spaces.items()}
    if observed != expected_nullities:
        raise AssertionError(f"full special invisible weight profile changed: {observed}")
    if sum(observed.values()) != 60:
        raise AssertionError("full special invisible space lost dimension 60")

    weight_certificate = {
        "schema_version": 1,
        "name": "Full 726-dimensional special invisible source space by weight",
        "constraints": &#91;
            "Z(w)=0",
            "E_(k,y)Y(w)=0, equivalently the active y row vanishes",
            "div(w)=0",
        &#93;,
        "operation_dimension": 726,
        "dimension": 60,
        "weights": certificate_weights,
    }
    canonical = json.dumps(
        weight_certificate, sort_keys=True, separators=(",", ":")
    ).encode()
    weight_certificate&#91;"certificate_sha256"&#93; = hashlib.sha256(canonical).hexdigest()
    (HERE / "full726_special_invisible_weight_space.json").write_text(
        json.dumps(weight_certificate, indent=2, sort_keys=True) + "\n"
    )
    return spaces


def build_divergence_transport_certificate() -&gt; dict&#91;str, Any&#93;:
    """Compute phi -&gt; Q.grad(phi) on Sym^2 and its two sparse dual classes."""
    cubic_monomials = &#91;
        sp.prod(m.V&#91;index&#93; for index in indices)
        for indices in itertools.combinations_with_replacement(range(11), 3)
    &#93;
    transport = sp.zeros(len(cubic_monomials), len(QUADRATICS))
    for column, phi in enumerate(QUADRATICS):
        expression = sp.expand(
            sum(m.Q&#91;i&#93; * sp.diff(phi, m.V&#91;i&#93;) for i in range(11))
        )
        polynomial = sp.Poly(expression, *m.V, domain=sp.QQ)
        for row, monomial in enumerate(cubic_monomials):
            coefficient = polynomial.coeff_monomial(monomial)
            if coefficient:
                transport&#91;row, column&#93; = coefficient
    rank = transport.rank()
    if rank != 65 or len(transport.nullspace()) != 1:
        raise AssertionError("the divergence transport map changed")
    kernel_generator = sp.factor(
        sum(
            transport.nullspace()&#91;0&#93;&#91;index&#93; * QUADRATICS&#91;index&#93;
            for index in range(len(QUADRATICS))
        )
    )
    if kernel_generator != m.b**2:
        raise AssertionError("the unique quadratic first integral changed")

    index = {monomial: position for position, monomial in enumerate(cubic_monomials)}
    chi_1 = sp.zeros(1, len(cubic_monomials))
    chi_1&#91;0, index&#91;m.b * m.s * m.x&#93;&#93; = 1
    chi_0 = sp.zeros(1, len(cubic_monomials))
    chi_0&#91;0, index&#91;m.d * m.q * m.x&#93;&#93; = 1
    chi_0&#91;0, index&#91;m.h * m.k * m.y&#93;&#93; = -2
    if chi_1 * transport != sp.zeros(1, len(QUADRATICS)):
        raise AssertionError("chi_1 left the transport cokernel")
    if chi_0 * transport != sp.zeros(1, len(QUADRATICS)):
        raise AssertionError("chi_0 left the transport cokernel")
    if sp.Matrix.vstack(chi_1, chi_0).rank() != 2:
        raise AssertionError("the two divergence classes became dependent")

    only_raw_support = &#91;&#93;
    for phi in QUADRATICS:
        expression = sp.expand(
            sum(m.Q&#91;i&#93; * sp.diff(phi, m.V&#91;i&#93;) for i in range(11))
        )
        polynomial = sp.Poly(expression, *m.V, domain=sp.QQ)
        dqx = polynomial.coeff_monomial(m.d * m.q * m.x)
        hky = polynomial.coeff_monomial(m.h * m.k * m.y)
        if dqx or hky:
            only_raw_support.append(
                {
                    "phi": str(phi),
                    "dqx": str(dqx),
                    "hky": str(hky),
                    "dqx_minus_2_hky": str(dqx - 2 * hky),
                }
            )
    expected = &#91;
        {
            "phi": "x*y",
            "dqx": "-1",
            "hky": "-1/2",
            "dqx_minus_2_hky": "0",
        }
    &#93;
    if only_raw_support != expected:
        raise AssertionError("the sparse transport support changed")

    return {
        "domain_dimension": 66,
        "rank": rank,
        "kernel_dimension": 1,
        "kernel_generator": str(kernel_generator),
        "cokernel_dimension": 286 - rank,
        "chi_1": "&#91;b*s*x&#93;",
        "chi_0": "&#91;d*q*x&#93;-2&#91;h*k*y&#93;",
        "two_classes_independent": True,
        "only_nonzero_raw_support_for_chi_0": only_raw_support,
    }


def main() -&gt; int:
    curve = json.loads((HERE / "exact_transverse_rational_curve.json").read_text())
    P1, A, B = (load_core_vector(curve, key) for key in ("P1", "A", "B"))
    t = sp.symbols("t")

    P_dagger = m.p0 + sp.Rational(4, 3) * m.row&#91;0&#93; - 2 * m.row&#91;2&#93;
    xi_12 = m.row&#91;12&#93;
    xi_14 = m.row&#91;14&#93;
    core_branch = (
        P_dagger
        - sp.Rational(2, 3) * xi_12
        + t * (P1 + sp.Rational(8, 3) * xi_12)
        + t**2 / (1 - t) * A
        + t**2 / (1 - 4 * t) * (B + 12 * xi_12 - 12 * xi_14)
    ).applyfunc(normal)
    # The divergence correction lies in the exact invisible W-space and
    # therefore preserves the rational E_(k,y) incidence identity.
    original_core_branch = (
        P_dagger
        + t * P1
        + t**2 / (1 - t) * A
        + t**2 / (1 - 4 * t) * B
    ).applyfunc(normal)
    divergence_correction = (core_branch - original_core_branch).applyfunc(normal)
    e_ky = sp.zeros(30, 1)
    e_ky&#91;25, 0&#93; = 1
    if m.Z * divergence_correction != sp.zeros(m.Z.rows, 1):
        raise AssertionError("the divergence correction left the row-killing kernel")
    if m.Rvec(e_ky, m.Yof(divergence_correction)) != sp.zeros(m.Z.rows, 1):
        raise AssertionError("the divergence correction changed E_(k,y)Y")

    branch_field = core_vector_field(core_branch)
    branch_divergence = normal(
        sum(sp.diff(branch_field&#91;i&#93;, m.V&#91;i&#93;) for i in range(11))
    )
    if branch_divergence != 0:
        raise AssertionError("the adjusted residual branch is not divergence-free")

    branch = full_from_core(core_branch)
    branch_values = chi_values(branch)
    chi_1 = normal(branch_values&#91;0&#93;)
    chi_0 = normal(branch_values&#91;1&#93;)
    expected_1 = 12 * t**2 / (4 * t - 1)
    expected_0 = -(
        336 * t**3 - 392 * t**2 + 71 * t - 12
    ) / ((t - 1) * (4 * t - 1))
    if normal(chi_1 - expected_1) or normal(chi_0 - expected_0):
        raise AssertionError("the residual branch divergence obstruction changed")

    # A polynomial Bezout certificate for the unit ideal generated by the
    # denominator-cleared obstruction values.
    cleared_1 = normal((4 * t - 1) * chi_1)
    cleared_0 = normal((t - 1) * (4 * t - 1) * chi_0)
    bezout_1 = 23856 * t**2 - 23800 * t + 337
    bezout_0 = 852 * t + 144
    bezout_value = sp.expand(bezout_1 * cleared_1 + bezout_0 * cleared_0)
    if bezout_value != 1728:
        raise AssertionError("the obstruction unit certificate changed")

    divergence_Q = normal(sum(sp.diff(m.Q&#91;i&#93;, m.V&#91;i&#93;) for i in range(11)))
    if divergence_Q != 0:
        raise AssertionError("Q is no longer divergence-free")
    print("&#91;stage&#93; divergence transport", flush=True)
    transport_certificate = build_divergence_transport_certificate()
    print("&#91;stage&#93; full exact weight spaces", flush=True)
    spaces = build_full_special_invisible_weight_spaces()
    print("&#91;stage&#93; obstruction polarizations", flush=True)

    # Grading reduces all possible weight-zero quadratic contributions to:
    # branch x W_0, Sym^2(W_0), W_-1 x W_1, and W_-2 x W_2.
    # A homogeneous source vector of nonzero weight has O4-weights w and 2w,
    # so a weight-zero coefficient functional vanishes on it automatically.
    # Only W_0 needs direct pure evaluation.
    pure_values: dict&#91;int, list&#91;sp.Matrix&#93;&#93; = {
        weight: &#91;sp.zeros(2, 1) for _ in basis&#93;
        for weight, basis in spaces.items()
    }
    pure_values&#91;0&#93; = &#91;chi_values(vector) for vector in spaces&#91;0&#93;&#93;
    if any(any(value != 0 for value in values) for values in pure_values&#91;0&#93;):
        raise AssertionError("a weight-zero pure source value survived")

    checks = {"branch_W0": 0, "W0_W0": 0, "Wm1_Wp1": 0, "Wm2_Wp2": 0}
    for index, vector in enumerate(spaces&#91;0&#93;):
        cross = (
            chi_values(branch + vector)
            - branch_values
            - pure_values&#91;0&#93;&#91;index&#93;
        ).applyfunc(normal)
        if cross != sp.zeros(2, 1):
            raise AssertionError(f"branch-W0 polarization survived at index {index}")
        checks&#91;"branch_W0"&#93; += 1

    for left, right in itertools.combinations_with_replacement(
        range(len(spaces&#91;0&#93;)), 2
    ):
        cross = (
            chi_values(spaces&#91;0&#93;&#91;left&#93; + spaces&#91;0&#93;&#91;right&#93;)
            - pure_values&#91;0&#93;&#91;left&#93;
            - pure_values&#91;0&#93;&#91;right&#93;
        ).applyfunc(normal)
        if cross != sp.zeros(2, 1):
            raise AssertionError(f"W0-W0 polarization survived at {left},{right}")
        checks&#91;"W0_W0"&#93; += 1

    for negative, positive, key in &#91;
        (-1, 1, "Wm1_Wp1"),
        (-2, 2, "Wm2_Wp2"),
    &#93;:
        for left, left_vector in enumerate(spaces&#91;negative&#93;):
            for right, right_vector in enumerate(spaces&#91;positive&#93;):
                cross = (
                    chi_values(left_vector + right_vector)
                    - pure_values&#91;negative&#93;&#91;left&#93;
                    - pure_values&#91;positive&#93;&#91;right&#93;
                ).applyfunc(normal)
                if cross != sp.zeros(2, 1):
                    raise AssertionError(
                        f"opposite-weight polarization survived at {negative}:{left}, {positive}:{right}"
                    )
                checks&#91;key&#93; += 1

    if checks != {
        "branch_W0": 12,
        "W0_W0": 78,
        "Wm1_Wp1": 66,
        "Wm2_Wp2": 36,
    }:
        raise AssertionError(f"unexpected polarization ledger: {checks}")

    result = {
        "schema_version": 1,
        "name": "Residual rank-six branch: full quadratic special-source and quartic target obstruction",
        "source_sha256": "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        "branch_parameter": "t",
        "branch_poles": &#91;"t=1", "t=1/4"&#93;,
        "divergence_free_adjustment": {
            "base": "P_dagger-(2/3)xi_12",
            "linear": "P1+(8/3)xi_12",
            "A": "A",
            "B": "B+12xi_12-12xi_14",
            "divergence": "0",
        },
        "obstruction_quotient": {
            "description": "Sym^3(V*)/(Q.grad)Sym^2(V*) after quotienting cubic source corrections and divergence-free quartic target jets by divergence",
            **transport_certificate,
        },
        "functionals_on_quartic_vector_fields": {
            "chi_1": "&#91;b*s*x&#93; div(R)",
            "chi_0": "(&#91;d*q*x&#93;-2&#91;h*k*y&#93;) div(R)",
        },
        "branch_values": {
            "chi_1": str(chi_1),
            "chi_0": str(chi_0),
            "cleared_chi_1": str(cleared_1),
            "cleared_chi_0": str(cleared_0),
            "bezout_identity": (
                "(23856*t^2-23800*t+337)*cleared_chi_1 + "
                "(852*t+144)*cleared_chi_0 = 1728"
            ),
            "unit_value": str(bezout_value),
            "common_zero_away_from_poles": False,
        },
        "full_quadratic_special_source_coupling": {
            "ambient_dimension": 726,
            "constraints": &#91;
                "Z(w)=0",
                "E_(k,y)Y(w)=0",
                "div(w)=0",
            &#93;,
            "dimension": 60,
            "weight_dimensions": {
                str(weight): len(basis) for weight, basis in spaces.items()
            },
            "polarization_checks": checks,
            "obstruction_values_invariant": True,
        },
        "cubic_source_corrections": {
            "identity": "div(JQ*U3-JU3*Q)=-Q.grad(div(U3)) because div(Q)=0",
            "annihilated_by_chi_0_and_chi_1": True,
        },
        "quartic_target_corrections": {
            "gauge_hypothesis": "additional target automorphism has no nonlinear terms below degree four",
            "constraint": "its quartic jet T4 has div(T4)=0",
            "annihilated_by_chi_0_and_chi_1": True,
        },
        "theorem": (
            "For every t away from 1 and 1/4, and after arbitrary motion in the full "
            "60-dimensional special quadratic source space preserving the exact E_(k,y) "
            "incidence relation, the quartic obstruction survives every cubic source "
            "correction and every additional divergence-free quartic target jet."
        ),
        "boundary": (
            "Moving quadratic or cubic target jets can alter the lower normal form and are "
            "not included. Stabilization can absorb divergence in new coordinates, so this "
            "certificate is not a stable obstruction."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result&#91;"certificate_sha256"&#93; = hashlib.sha256(canonical).hexdigest()
    (HERE / "residual_full_source_target_obstruction.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(
        json.dumps(
            {
                "chi_1": str(chi_1),
                "chi_0": str(chi_0),
                "unit_value": str(bezout_value),
                "full_source_dimension": 60,
                "polarization_checks": checks,
                "certificate_sha256": result&#91;"certificate_sha256"&#93;,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `lane6-transverse-source-obstruction-20260802-v1/tame-source-coupled/verify_tame_quadratic_jet.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Construct an elementary-shear decomposition of the residual branch jet.

The mathematical lemma implemented here is:

Every divergence-free homogeneous quadratic vector field P on A^n is a sum
of fields c*v*ell^2 with ell(v)=0.  Each map x -&gt; x+c*v*ell(x)^2 is an
elementary determinant-one polynomial automorphism, with inverse obtained by
changing c to -c.  Hence P is the quadratic jet of a finite product of tame
special polynomial automorphisms.

The verifier applies the constructive proof to the exact divergence-free
residual branch representative over Q(t).
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import core_model as m  # noqa: E402


def normal(value: sp.Expr) -&gt; sp.Expr:
    return sp.factor(sp.cancel(value))


def load_vector(payload: dict&#91;str, Any&#93;, key: str) -&gt; sp.Matrix:
    vector = sp.zeros(115, 1)
    for item in payload&#91;key&#93;:
        vector&#91;item&#91;"index"&#93;, 0&#93; = sp.Rational(item&#91;"coefficient"&#93;)
    return vector


def vector_field(vector: sp.Matrix) -&gt; sp.Matrix:
    result = sp.zeros(11, 1)
    for coefficient, (row, monomial) in zip(vector, m.operation_basis):
        if coefficient:
            result&#91;row, 0&#93; += coefficient * monomial
    return result.applyfunc(normal)


def sparse_coordinate_vector(vector: sp.Matrix) -&gt; dict&#91;str, str&#93;:
    return {
        str(m.V&#91;index&#93;): str(normal(value))
        for index, value in enumerate(vector)
        if normal(value) != 0
    }


def main() -&gt; int:
    curve = json.loads((HERE / "exact_transverse_rational_curve.json").read_text())
    P1, A, B = (load_vector(curve, key) for key in ("P1", "A", "B"))
    t = sp.symbols("t")
    P_dagger = m.p0 + sp.Rational(4, 3) * m.row&#91;0&#93; - 2 * m.row&#91;2&#93;

    coefficients = (
        P_dagger
        - sp.Rational(2, 3) * m.row&#91;12&#93;
        + t * (P1 + sp.Rational(8, 3) * m.row&#91;12&#93;)
        + t**2 / (1 - t) * A
        + t**2 / (1 - 4 * t) * (B + 12 * m.row&#91;12&#93; - 12 * m.row&#91;14&#93;)
    ).applyfunc(normal)
    field = vector_field(coefficients)
    divergence = normal(sum(sp.diff(field&#91;i&#93;, m.V&#91;i&#93;) for i in range(11)))
    if divergence != 0:
        raise AssertionError(f"the adjusted branch is not divergence-free: {divergence}")

    records: list&#91;tuple&#91;sp.Expr, sp.Matrix, sp.Matrix, str&#93;&#93; = &#91;&#93;
    remainder = field.copy()

    def add_shear(
        scalar: sp.Expr,
        direction: sp.Matrix,
        linear_form: sp.Matrix,
        label: str,
    ) -&gt; None:
        scalar = normal(scalar)
        if scalar == 0:
            return
        if normal((linear_form.T * direction)&#91;0&#93;) != 0:
            raise AssertionError(f"non-elementary shear in {label}")
        records.append((scalar, direction, linear_form, label))

    # Remove every term x_i*x_j e_i together with its divergence-canceling
    # companion.  The key identity is
    #
    # x_i*x_j e_i - 1/2*x_j^2 e_j
    # = -1/4(e_i+e_j)(x_i-x_j)^2
    #   +1/4(e_i-e_j)(x_i+x_j)^2 +1/2 e_j*x_i^2.
    for i, xi in enumerate(m.V):
        polynomial = sp.Poly(remainder&#91;i&#93;, *m.V)
        for j, xj in enumerate(m.V):
            if i == j:
                continue
            coefficient = normal(polynomial.coeff_monomial(xi * xj))
            if coefficient == 0:
                continue
            ei = sp.eye(11)&#91;:, i&#93;
            ej = sp.eye(11)&#91;:, j&#93;
            ell_minus = sp.zeros(11, 1)
            ell_minus&#91;i&#93;, ell_minus&#91;j&#93; = 1, -1
            ell_plus = sp.zeros(11, 1)
            ell_plus&#91;i&#93;, ell_plus&#91;j&#93; = 1, 1
            ell_i = sp.zeros(11, 1)
            ell_i&#91;i&#93; = 1
            add_shear(-coefficient / 4, ei + ej, ell_minus, f"pair({i},{j})-")
            add_shear(coefficient / 4, ei - ej, ell_plus, f"pair({i},{j})+")
            add_shear(coefficient / 2, ej, ell_i, f"pair({i},{j})0")
            remainder&#91;i&#93; -= coefficient * xi * xj
            remainder&#91;j&#93; += coefficient * sp.Rational(1, 2) * xj**2
            remainder = remainder.applyfunc(normal)

    # Divergence-freeness implies that the remaining i-th component is
    # independent of x_i.  Polarize each remaining mixed monomial.
    for i, xi in enumerate(m.V):
        if sp.Poly(remainder&#91;i&#93;, *m.V).degree(xi) &gt; 0:
            raise AssertionError(f"remainder component {i} still depends on its coordinate")

    for i, expression in enumerate(remainder):
        ei = sp.eye(11)&#91;:, i&#93;
        for exponents, coefficient in sp.Poly(expression, *m.V).terms():
            if coefficient == 0:
                continue
            indices: list&#91;int&#93; = &#91;&#93;
            for j, exponent in enumerate(exponents):
                indices.extend(&#91;j&#93; * exponent)
            if len(indices) != 2 or i in indices:
                raise AssertionError("unexpected residual quadratic monomial")
            j, k = indices
            if j == k:
                ell = sp.zeros(11, 1)
                ell&#91;j&#93; = 1
                add_shear(coefficient, ei, ell, f"monomial({i};{j}^2)")
            else:
                ell_plus = sp.zeros(11, 1)
                ell_plus&#91;j&#93;, ell_plus&#91;k&#93; = 1, 1
                ell_minus = sp.zeros(11, 1)
                ell_minus&#91;j&#93;, ell_minus&#91;k&#93; = 1, -1
                add_shear(coefficient / 4, ei, ell_plus, f"monomial({i};{j}{k})+")
                add_shear(-coefficient / 4, ei, ell_minus, f"monomial({i};{j}{k})-")

    reconstruction = sp.zeros(11, 1)
    for scalar, direction, linear_form, _ in records:
        ell = (linear_form.T * sp.Matrix(m.V))&#91;0&#93;
        reconstruction += scalar * direction * ell**2
    if (reconstruction - field).applyfunc(normal) != sp.zeros(11, 1):
        raise AssertionError("the shear decomposition does not reconstruct the branch field")

    record_json = &#91;
        {
            "scalar": str(normal(scalar)),
            "direction": sparse_coordinate_vector(direction),
            "linear_form": sparse_coordinate_vector(linear_form),
            "orthogonality": "ell(v)=0",
            "label": label,
        }
        for scalar, direction, linear_form, label in records
    &#93;
    result = {
        "schema_version": 1,
        "name": "Tame special admissibility of the divergence-free residual branch jet",
        "source_sha256": "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        "branch_poles": &#91;"t=1", "t=1/4"&#93;,
        "divergence_free_adjustment": {
            "base": "P_dagger-(2/3)xi_12",
            "linear": "P1+(8/3)xi_12",
            "A": "A",
            "B": "B+12xi_12-12xi_14",
            "verified_divergence": "0",
        },
        "general_lemma": (
            "Every divergence-free homogeneous quadratic vector field is a sum "
            "of c*v*ell^2 with ell(v)=0 and is therefore the quadratic jet of a "
            "finite product of elementary determinant-one polynomial shears."
        ),
        "branch_decomposition": {
            "shear_count": len(records),
            "records": record_json,
            "exact_reconstruction": True,
        },
        "consequence": (
            "For every specialization away from t=1 and t=1/4, and after adding "
            "any divergence-free homogeneous quadratic source field, the resulting "
            "quadratic jet is realizable by a tame special polynomial automorphism."
        ),
        "boundary": (
            "This proves admissibility of the quadratic jet. The higher jets of the "
            "chosen shear product are not asserted to preserve the rank-six incidence "
            "identity without the separate Kuranishi analysis."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result&#91;"certificate_sha256"&#93; = hashlib.sha256(canonical).hexdigest()
    (HERE / "tame_residual_quadratic_jet.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(
        json.dumps(
            {
                "divergence": "0",
                "shear_count": len(records),
                "certificate_sha256": result&#91;"certificate_sha256"&#93;,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

[Back to Lane 6](homogeneous-realization-compression.md)
