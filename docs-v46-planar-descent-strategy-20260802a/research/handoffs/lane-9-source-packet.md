# Lane 9 exact research source packet

This is the public source packet for **Plane chart correspondence and global attachment**. It contains the
selected proof notes, exact computation contracts, and checkers used
by the concise lane brief. Read only the files relevant to the route
you pursue. Stored outputs and very large reconstructible matrices are
omitted; the mathematical boundary of each checker remains in its
source text.

Private-source commit: `ed3137b5ce00f4f206fe1126b4fdc3bc5051b112`.

## Included files

- `lane9-wall-shear-20260802-v1/LANE9_CONTINUATION_V3_REPORT.md` — `c95708358a4bb8486d3823d15279e4acec3574fd55d2e5ad49234f032e57d510`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_GRADING_AUDIT.md` — `afeec62e2950cc4a120e9b5280dfbf04d1e1c86135a290c2bc3a1f0df84df745`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_OVERLAP_THEOREM.md` — `94d278bd3285f8eadc2d31901a8518b84de8e8f53ec40d0d6cfa86975e412059`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_DUAL_TRIPLE_OVERLAP.md` — `43a45be475ebeadb54f553f88038e446cce9a34d3e7d17e73ae92d48260da3b0`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_REES_FLOW.md` — `9f763c0acd13a068b96cef1f073b46cf1a2afa9d82fa8fa32426c812648662ab`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/F2_CYCLIC_WALL_DESCENT.md` — `2485be2f147247108a3c7dd828187a4985d5086d712ccc8ad14b2dd70696cce5`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/wall_shear_master_covariance.py` — `ae914d451e4ec3ab1b583c5f35c2e35c396c5596b9340dd817672961abc460cd`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_jet_transport_audit.py` — `4d240c1e6dc80412e1aa29fc55e7b6bf44208fb870577ab4f5ed642e7a758954`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_overlap_saturation.py` — `4a3c3d76037ebbae7328fe65a3e35d04ad85c3311fc72566881d5895b0511848`
- `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_triple_overlap.py` — `5639081b7a0c4d72c8e4bf80170c9f43fcb45deb01146f323e1a396d65dd5988`

## `lane9-wall-shear-20260802-v1/LANE9_CONTINUATION_V3_REPORT.md`

<pre><code class="language-markdown">
# Lane 9 continuation v3 report

## Result

The ambient wall atlas now includes exact residue-dual transport, forcing
pairings, triple-overlap constraints, an operation-space commutator, and
cyclic parameter descent.

## 1. Obstruction duals and forcing transport

For primal density transport

\&#91;
T e_{n,j}
 =\sum_q\binom{n-p+2j}{q}\lambda^q
 e_{n+q(2k-1),j-qk},
\&#93;

the exact contragredient is

\&#91;
U\epsilon_{m,l}
 =\sum_q\binom{p-m-2l-1}{q}\lambda^q
 \epsilon_{m-q(2k-1),l+qk}.
\&#93;

It satisfies

\&#91;
U^\mathsf TT=I.
\&#93;

The formula was checked on every basis vector of the 114-dimensional `P`,
180-dimensional `Q`, and 300-dimensional equation-density wall
saturations. Consequently left-null obstruction functionals and their
pairings with forcing vectors transport exactly through the ambient chain
map.

## 2. Triple overlap adds real conditions

Through layer 15,

\&#91;
T_\lambda=I+\lambda N+\lambda^2N^2/2.
\&#93;

The old chart and one nonzero transported chart overlap in 89 deformation
dimensions. The intersection of the charts at parameters `0`, `1`, and `-1`
is only 68-dimensional and equals the subspace stable under every wall
parameter.

For the equation density, the corresponding dimensions are 216 and 206.
Thus a two-chart check leaves

\&#91;
\boxed{21\text{ deformation directions}}
\&#93;

and

\&#91;
\boxed{10\text{ equation directions}}
\&#93;

that fail triple-overlap compatibility.

The first-order coefficient overflow has rank 97, but all-parameter stability
imposes 118 independent source conditions. The quadratic wall term therefore
adds 21 independent constraints, even though it creates only 11 new ambient
coefficient coordinates.

## 3. Transporting the layer-four candidate forces a layer-eleven term

Let the layer-four support-admissible field be

\&#91;
f_4=c_0+c_1z+z^2,
\qquad g_4=2c_0z^{-1}+3c_1+4z,
\&#93;

and let the `k=4` wall field be

\&#91;
f_7=2z^{-3},
\qquad g_7=z^{-4}.
\&#93;

Their bracket is the layer-eleven field

\&#91;
f_{11}=18c_0z^{-4}+30c_1z^{-3}+42z^{-2},
\&#93;

\&#91;
g_{11}=6c_0z^{-5}+5c_1z^{-4}.
\&#93;

Its action on the degree-21 face has unavoidable top terms

\&#91;
336\operatorname{lead}(A_0)z^5,
\qquad
504\operatorname{lead}(B_0)z^9.
\&#93;

The stored layer-eleven windows allow no `P` coefficient and only `Q`
exponents `0,...,4`. Therefore carrying the layer-four direction across the
wall requires a genuine adjacent-chart layer-eleven operation coordinate.
The old fixed-chart operation space cannot be used unchanged.

## 4. The F2 wall parameter is a character line

For a cyclic quotient `u=z^g`, the order-`q` `k`-wall term shifts cyclic
character by `-qk`. Equivariance requires

\&#91;
\lambda\mapsto\zeta^k\lambda.
\&#93;

For `F_2`, `g=5` and `k=4`. The parameter has `C_5` character four, and an
invariant scalar effect first returns at wall order five, unweighted normal
shift 35.

If one simultaneously tries to reconcile the public layer-four label with
the bare layer-seven wall, the unique required normal weight is `-3`. The
necessary parameter bidegree is therefore

\&#91;
\boxed{(-3,4\bmod5)}.
\&#93;

This negative Rees weight is chart-moving data, not an ordinary fixed-chart
deformation coordinate.


## 5. Parameter weight alone fails the layer-four kernel test

Assigning weight `-3` to the `k=4` wall parameter changes the bookkeeping
layer from seven to four, but the bare source pair then has exact defect

\&#91;
-3z^{-2}
\&#93;

in the ordinary \(D_4\) weighted-divergence identity.  The unique correction
with the same horizontal component changes

\&#91;
g:z^{-4}\longmapsto -2z^{-4}.
\&#93;

This produces the candidate associated-graded rechart field

\&#91;
t^4(2z^{-3}\partial_z-2z^{-4}t\partial_t),
\&#93;

whose degree-21 action exits the old layer-four window only through the
principal parts `A={-3,-2,-1}` and `B={-2,-1}`.  The remaining task is to
construct the Rees/Euler action producing this correction and compare it with
the archived residual vector.


## 6. The corrected candidate is a Kummer Hamiltonian flow

Using the original affine-coordinate dictionary

\&#91;
t=x^4y,\qquad z=x^7y^2,
\&#93;

the corrected associated-graded field becomes

\&#91;
\boxed{
V=-6x^{-11}y^{-4}\partial_x
  +22x^{-12}y^{-3}\partial_y.
}
\&#93;

It has ordinary divergence zero and is Hamiltonian for

\&#91;
H=2x^{-11}y^{-3}.
\&#93;

With

\&#91;
M=x^{-12}y^{-4}=t^4z^{-4},
\&#93;

one has

\&#91;
V(H)=0,\qquad V(M)=-16M^2.
\&#93;

The exact formal flow is therefore

\&#91;
R^8=1+16sM,
\&#93;

\&#91;
\boxed{
x_s=xR^{-3},\qquad y_s=yR^{11},\qquad
t_s=tR^{-1},\qquad z_s=zR.
}
\&#93;

The binomial root exists formally in the deformation parameter.  It is not,
however, rational over \(K(x,y,s)\): the radicand has valuation one at the
prime \(x^{12}y^4+16s\), whereas an eighth power has valuation divisible by
eight.  The generic algebraic flow therefore requires a degree-eight Kummer
extension.

There is an exact quotient-coordinate linearization.  Put

\&#91;
H=2x^{-11}y^{-3}=\frac{2}{tz},
\qquad
Q=x^{12}y^4=\left(\frac zt\right)^4=M^{-1}.
\&#93;

Then

\&#91;
V(H)=0,
\qquad
V(Q)=16,
\&#93;

so the flow on the quotient is simply

\&#91;
\boxed{H_s=H,\qquad Q_s=Q+16s.}
\&#93;

The exponent-lattice determinant of \((x,y)\mapsto(H,Q)\) is \(-8\), and

\&#91;
x^8=\frac{16}{H^4Q^3},
\qquad
y^8=\frac{H^{12}Q^{11}}{4096}.
\&#93;

Thus the Kummer extension is exactly the inverse of a degree-eight monomial
quotient.  For the `F_2` `C_5` assignment, both \(Q\) and the parameter have
character four, so \(Q\mapsto Q+16s\) is equivariant; lifting back to
\((x,y)\) still requires the independent eighth root.

In the adjacent blowdown variables used by the stored proposition,

\&#91;
u=(xy)^{-1},\qquad v=y,
\&#93;

these quotient coordinates are

\&#91;
H=2u^{11}v^8,
\qquad
Q=u^{-12}v^{-8}.
\&#93;

Therefore

\&#91;
\boxed{K(H,Q)=K(u,v^8).}
\&#93;

The degree-eight quotient is exactly the \(\mu_8\)-quotient of the adjacent
blowdown chart.  The corrected field descends to this quotient, while the bare
`k=4` operation is the translation \(v\mapsto v+s\), which is not the same
quotient operation.  This isolates a precise missing lift in the public
correspondence claim.


The corrected layer-four candidate is therefore an ordinary translation on a
concrete degree-eight quotient chart, but not an ordinary same-function-field
rational wall operation.  A successful complete-chain interpretation would
have to identify this quotient—or another filtration-changing model—with the
actual adjacent presentation.


Because

\&#91;
Q=\left(\frac zt\right)^4
\&#93;

has normal \(t\)-exponent \(-4\), translation in \(Q\) naturally has the
missing layer-four label.  This gives the strongest current repaired
correspondence candidate:

&gt; match the stored layer-four residual to the pullback of the quotient
&gt; translation \(Q\mapsto Q+16s\), not to the bare layer-seven translation
&gt; \(v\mapsto v+s\).

The scalar `16` is a parameter normalization.  What remains is an exact
coefficientwise comparison with the archived residual representative.

## 7. Current boundary

These results provide an exact finite ambient wall groupoid with:

- coefficient transport;
- nonlinear equation transport;
- inverse and additive cocycles;
- residue-dual and forcing transport;
- pairwise and triple-overlap dimensions;
- a required operation-map commutator term;
- cyclic eigenparameter descent;
- the exact weight-only defect and unique corrected layer-four vertical term.

They still do not provide the actual complete-chain monomial adjacent chart,
its presentation stabilizer, or the real `F_2` order-by-order matrices. Those
are now the remaining external inputs rather than undefined linear-algebra
steps.

## 8. Validation

The combined bundle contains 73 exact regression tests, all passing.
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_GRADING_AUDIT.md`

<pre><code class="language-markdown">
# Wall-shear grading audit for the degree-21 lower face

**Status:** exact coordinate calculation and regression-tested research note.
It identifies a grading/provenance gap in the current public formulation of the
claimed layer-four/`k=4` correspondence. It does not invalidate the separate
adjacent-chart terminal calculation; it shows that the bridge to that
calculation has not been written in a filtration-compatible form.

**Audited repository state:** draft PR 1, head
`fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0`.

## 1. Coordinate dictionary

The degree-21 lower face uses

\&#91;
t=Y,\qquad z=XY^2,
\&#93;

and

\&#91;
P=t^{-\alpha}\sum_{n\ge 0}t^nA_n(z),\qquad
Q=t^{-\beta}\sum_{n\ge 0}t^nB_n(z),
\qquad (\alpha,\beta)=(2,3).
\&#93;

Consider the elementary wall shear

\&#91;
X'=X,\qquad Y'=Y+\lambda X^{-k},\qquad k\ge 1,
\&#93;

with scalar parameter \(\lambda\). Since \(X=z/t^2\), put

\&#91;
h=\lambda t^{2k-1}z^{-k}.
\&#93;

Then the transport in normal coordinates is the exact identity

\&#91;
\boxed{
 t'=t(1+h),\qquad z'=z(1+h)^2.
}
\&#93;

No series expansion is used here.

## 2. The normal order is \(2k-1\)

Differentiating at \(\lambda=0\) gives

\&#91;
\delta t=t^{2k}z^{-k},\qquad
\delta z=2t^{2k-1}z^{1-k}.
\&#93;

In the source-field convention

\&#91;
V_r=t^r\bigl(f(z)\partial_z+g(z)t\partial_t\bigr),
\&#93;

this is

\&#91;
\boxed{
 r=2k-1,\qquad f=2z^{1-k},\qquad g=z^{-k}.
}
\&#93;

For the lower face \(\Psi=z^2\), the weighted-divergence identity is checked
exactly:

\&#91;
(fz^2)' +(r-5)gz^2
=2(3-k)z^{2-k}+2(k-3)z^{2-k}=0.
\&#93;

Thus the shear tangent lies in the unrestricted determinant kernel at normal
order \(2k-1\).

For \(k=4\),

\&#91;
\boxed{
 r=7,\qquad
 V_4=t^7\bigl(2z^{-3}\partial_z+z^{-4}t\partial_t\bigr).
}
\&#93;

Consequently, under the displayed lower-face grading, the bare `k=4` shear is
the identity on the normal jet through layer six. It cannot itself be a
nonzero vector in the layer-four coefficient space.

In the archived affine coordinates

\&#91;
X=x^{-1},\qquad Y=x^4y,
\&#93;

the same operation is simply

\&#91;
y\longmapsto y+\lambda.
\&#93;

This explains why it is a polynomial source operation globally while changing
the center of the completed Newton chart. It does not alter the \(t\)-adic
order computed above.

## 3. Exact transport of every normal monomial

For a normal basis monomial

\&#91;
t^{n-\alpha}z^j,
\&#93;

one has

\&#91;
\boxed{
(t')^{n-\alpha}(z')^j
 =\sum_{q\ge0}
 \binom{n-\alpha+2j}{q}\lambda^q
 t^{n-\alpha+q(2k-1)}z^{j-qk}.
}
\&#93;

The generalized binomial coefficient is interpreted in the usual way for
negative integral upper index. The first-order basis shift is therefore

\&#91;
(n,j)\longmapsto(n+2k-1,j-k)
\&#93;

with coefficient \(n-\alpha+2j\). Define the infinitesimal transport
operator

\&#91;
N_k e_{n,j}=(n-\alpha+2j)e_{n+2k-1,j-k}.
\&#93;

After one application the coefficient drops by one, so

\&#91;
N_k^q e_{n,j}
=(n-\alpha+2j)_{\underline q}
 e_{n+q(2k-1),j-qk}.
\&#93;

Consequently the exact wall transport is

\&#91;
\boxed{F_\lambda^*=\exp(\lambda N_k).}
\&#93;

This supplies the inverse and composition laws formally:

\&#91;
F_{-\lambda}^*=(F_\lambda^*)^{-1},\qquad
F_\lambda^*F_\mu^*=F_{\lambda+\mu}^*.
\&#93;

On a finite normal jet, \(N_k\) is nilpotent after an ambient cutoff is
chosen. This exact sparse operator, rather than support-set closure alone, is
the transition matrix needed in a chart-correspondence packet.

For `k=4`, every first-order coefficient moves up by exactly seven normal
layers and left by four \(z\)-exponents.

## 4. Full stored-window transport profile

Applying \(N_4\) to all 186 monomial basis elements in the archived full
support gives:

| classification | count |
| --- | ---: |
| internal old-window entries | 55 |
| exits through a stored coefficient wall | 97 |
| terms above the stored layer-15 cutoff | 31 |
| zero first-order entries | 3 |

The componentwise counts are:

| component | dimension | internal | window exit | above cutoff | zero |
| --- | ---: | ---: | ---: | ---: | ---: |
| `P` | 61 | 10 | 46 | 3 | 2 |
| `Q` | 125 | 45 | 51 | 28 | 1 |

On the old-window projection, \(N_4^2\) has rank three and
\(N_4^3=0\). Those three second-order entries are the falling-factorial paths

\&#91;
(0,8)\mapsto(14,0):13\cdot12,
\quad
(0,9)\mapsto(14,1):15\cdot14,
\quad
(1,8)\mapsto(15,0):14\cdot13
\&#93;

in the `Q` component.

The important datum is not the small internal rank. More than half of the
first-order basis vectors leave the old coefficient window. Deleting those
97 entries is not a quotient or a chart transition; they must be expressed in
an explicit adjacent-chart basis.

## 5. First exact support exit for the stored degree-21 face

Write

\&#91;
A_0=zp(z),\qquad B_0=z^2q(z).
\&#93;

At the first nonzero normal layer \(r=2k-1\), the tangent action is

\&#91;
a_r=fA_0'-2gA_0=2z^{2-k}p'(z),
\&#93;

\&#91;
b_r=fB_0'-3gB_0
=z^{2-k}q(z)+2z^{3-k}q'(z).
\&#93;

For `k=4`, this becomes

\&#91;
\boxed{
 a_7=2z^{-2}p'(z),\qquad
 b_7=z^{-2}q(z)+2z^{-1}q'(z).
}
\&#93;

The exact degree-21 face has nonzero coefficients through
\(\deg p=7\) and \(\deg q=10\). Hence

\&#91;
\operatorname{supp}(a_7)=\{-2,-1,0,1,2,3,4\},
\&#93;

\&#91;
\operatorname{supp}(b_7)=\{-2,-1,0,1,2,3,4,5,6,7,8\}.
\&#93;

The archived full fixed-chart layer-seven windows are

\&#91;
\operatorname{supp}(A_7)\subseteq\{0,1,2,3\},\qquad
\operatorname{supp}(B_7)\subseteq\{0,1,2,3,4,5,6,7,8\}.
\&#93;

Therefore the exact forbidden exponents are

\&#91;
\boxed{
 A:\{-2,-1,4\},\qquad B:\{-2,-1\}.
}
\&#93;

This is a clean support certificate that the `k=4` tangent leaves the old
fixed-chart window at layer seven. It is consistent with a rechart there; it
is not a fixed-chart gauge vector.

## 6. Consequence for the public layer-four statement

The current public proposition combines:

1. a one-dimensional residual quotient at normal layer four;
2. the elementary operation \(Y\mapsto Y+\lambda X^{-4}\);
3. a subsequent adjacent-chart terminal calculation.

Items 1 and 2 do not match under the public coordinate dictionary:

\&#91;
\text{wall index }k=4
\quad\Longrightarrow\quad
\text{normal order }r=2k-1=7,
\&#93;

not \(r=4\).

A valid repair must provide at least one of the following and verify it
coefficientwise:

- a different pair of coordinates denoted by \((X,Y)\) in the operation;
- a nonzero filtration degree assigned to \(\lambda\);
- an intervening conjugation whose induced graded map sends order seven to
  the stated layer-four quotient;
- a correction of either the layer label or the operation.

A relabeling by `k` alone is insufficient because the manuscript explicitly
uses the normal-layer operator \(D_r\) and calls the residual a normal
layer-four class.

Until this bridge is supplied, the safe public statement is:

&gt; The stored calculation reports a one-dimensional layer-four residual and a
&gt; separate `k=4` adjacent-chart operation. Their claimed identification has an
&gt; unresolved grading map. The adjacent-chart no-gluing certificate should be
&gt; treated as exact for its displayed transformed system, while its provenance
&gt; from the layer-four quotient remains review-pending.

## 7. A separate layer-four integrability result

The maximal linear support-admissible Laurent calculation at normal layer four
has a one-dimensional source basis with

\&#91;
f(z)=c_0+c_1z+z^2.
\&#93;

In the original affine coordinates \(z=x^7y^2\), the corresponding source
field is Hamiltonian:

\&#91;
D_H=H_y\partial_x-H_x\partial_y,
\qquad
H=x^{10}y^3(c_0+c_1z+z^2).
\&#93;

The highest monomial of \(H\) is \(x^{24}y^7\). Its Hamiltonian derivation
acts on a monomial by

\&#91;
D_{\mathrm{top}}(x^py^q)
 =(7p-24q)x^{p+23}y^{q+6}.
\&#93;

Inductively, the leading term of \(D_H^n(x)\) is

\&#91;
\boxed{
\left(\prod_{m=0}^{n-1}(7+17m)\right)
 x^{1+23n}y^{6n}.
}
\&#93;

Every factor is nonzero in characteristic zero, so \(D_H^n(x)\ne0\) for all
\(n\). Hence this support-admissible polynomial derivation is **not locally
nilpotent** and does not generate an algebraic additive one-parameter shear.

This result does not prove the manuscript's full fixed-chart nonintegrability
claim: arbitrary formal flows and non-group polynomial paths are broader than
\(\mathbb G_a\)-actions. It does prove a useful strict separation:

\&#91;
\text{supported polynomial infinitesimal field}
\not\Longrightarrow
\text{integrable additive complete-chain operation}.
\&#93;

The certificate is replayed by
`degree21_r4_hamiltonian_audit.py`.

## 8. Correct chart-correspondence target

For each chart \(C\) and layer \(r\), distinguish

\&#91;
\mathfrak g^{\mathrm{adm}}_{C,r}
 \xrightarrow{\Theta_{C,r}}
E_{C,r}
 \xrightarrow{D_{C,r}}
W_{C,r}.
\&#93;

The tangent and obstruction spaces are

\&#91;
T_{C,r}=\ker D_{C,r}/\operatorname{im}\Theta_{C,r},
\qquad
O_{C,r}=\operatorname{coker}D_{C,r}.
\&#93;

A chart transition \(\tau:C\to C'\) must include exact maps

\&#91;
T_{\tau,E},\quad T_{\tau,W},\quad T_{\tau,\mathfrak g}
\&#93;

satisfying

\&#91;
D_{C'}T_{\tau,E}=T_{\tau,W}D_C,
\qquad
T_{\tau,E}\Theta_C=\Theta_{C'}T_{\tau,\mathfrak g}.
\&#93;

If coefficient transport is affine,

\&#91;
e'=T_{\tau,E}e+\delta_\tau,
\&#93;

then forcing must satisfy

\&#91;
T_{\tau,W}\Phi_C=\Phi_{C'}+D_{C'}\delta_\tau.
\&#93;

Inverse transitions and triple overlaps must satisfy their corresponding
cocycle identities. Only after these checks is it legitimate to identify two
local tangent classes or to quotient by rechart directions.

## 9. Exact nonlinear master-equation covariance

For a coefficient density of pole order \(p\), define

\&#91;
T^{(p)}_{k,\lambda}(t^nz^j)
=
\sum_{q\ge0}
\binom{n-p+2j}{q}\lambda^q
t^{n+q(2k-1)}z^{j-qk}.
\&#93;

Let

\&#91;
\mathcal R_{\alpha,\beta}(A,B)
=
\alpha AB_z-\beta A_zB
+t(A_zB_t-A_tB_z)-z^2.
\&#93;

The residual density has pole order \(\alpha+\beta-1\), and exact two-form
pullback gives

\&#91;
\boxed{
\mathcal R_{\alpha,\beta}
(T^{(\alpha)}A,T^{(\beta)}B)
=
T^{(\alpha+\beta-1)}
\mathcal R_{\alpha,\beta}(A,B).
}
\&#93;

Differentiation gives the full cumulative-jet chain-map square. Thus the wall
transition now has an exact equation-space map, not merely a coefficient
support closure.

## 10. Minimal transported-window overlap

For the archived full degree-21 support through layer 15, the minimal
`k=4` wall-saturated deformation space has dimension 294:

| component | old | saturated | added |
| --- | ---: | ---: | ---: |
| `P` | 61 | 114 | 53 |
| `Q` | 125 | 180 | 55 |
| total | 186 | 294 | 108 |

For every nonzero wall parameter,

\&#91;
\dim(E_0\cap E_\lambda)=89,\qquad
\dim(E_0+E_\lambda)=283.
\&#93;

The transported chart contributes 97 independent directions beyond the old
window, exactly the first-order wall-exit rank. The corresponding nonlinear
equation-density dimensions are

\&#91;
\dim W_0=257,\quad
\dim W^{\mathrm{sat}}=300,\quad
\dim(W_0\cap W_\lambda)=216,\quad
\dim(W_0+W_\lambda)=298.
\&#93;

The base chart and the two opposite charts span the whole minimal saturation:

\&#91;
E^{\mathrm{sat}}=E_0+E_1+E_{-1},\qquad
W^{\mathrm{sat}}=W_0+W_1+W_{-1}.
\&#93;

This is an exact ambient Laurent-jet chart groupoid. It is not yet the
complete-chain monomial atlas.

## 11. Two consequences

First, a filtration-preserving conjugacy cannot turn the `k=4` shift seven
into shift four. If \(C\) has invertible associated graded, then

\&#91;
\sigma_7(CN_4C^{-1})
=
\operatorname{gr}(C)\sigma_7(N_4)\operatorname{gr}(C)^{-1}\ne0.
\&#93;

Any reconciliation of the public layer-four statement must therefore change
the filtration, reweight the wall parameter, or correct a label.

Second, the exact face

\&#91;
A_0=z+\frac32z^2,\qquad B_0=z^2+z^3
\&#93;

has a `k=4` wall arc

\&#91;
A=A_0+3t^7z^{-2}+\frac32t^{14}z^{-6},
\&#93;

\&#91;
B=B_0+t^7(z^{-2}+3z^{-1})+3t^{14}z^{-5}.
\&#93;

At layer 14 the quadratic forcing is

\&#91;
6z^{-5}-27z^{-4},
\&#93;

and the second wall correction has linear image

\&#91;
-6z^{-5}+27z^{-4}.
\&#93;

They cancel exactly. Setting the second correction to zero creates a false
nonzero residual.

## 12. Reproduction

```bash
python research-notes/p6-chart-correspondence/wall_shear_normal_coordinates.py \
  --k 4 \
  --output /tmp/wall-shear-k4.json

python research-notes/p6-chart-correspondence/degree21_k4_support_audit.py \
  research-notes/p6-chart-correspondence/fixtures/exact_belyi_data.json \
  research-notes/p6-chart-correspondence/lower_face_supports.json \
  --k 4 \
  --output /tmp/degree21-k4-support.json

python research-notes/p6-chart-correspondence/degree21_k4_jet_transport_audit.py \
  research-notes/p6-chart-correspondence/lower_face_supports.json \
  --k 4 \
  --output /tmp/degree21-k4-jet-transport.json

python research-notes/p6-chart-correspondence/degree21_r4_hamiltonian_audit.py \
  research-notes/p6-chart-correspondence/degree21_lower_face_full_gauge.json \
  --output /tmp/degree21-r4-hamiltonian.json

python -m unittest discover \
  -s research-notes/p6-chart-correspondence \
  -p 'test_*wall_shear*.py' -v

python -m unittest discover \
  -s research-notes/p6-chart-correspondence \
  -p 'test_degree21_k4_support_audit.py' -v
```

The six new test modules contain thirty-two exact regression tests.


Additional commands:

```bash
python research-notes/p6-chart-correspondence/wall_shear_master_covariance.py \
  --k 4 --cutoff 15 \
  --output /tmp/wall-master-covariance.json

python research-notes/p6-chart-correspondence/degree21_k4_overlap_saturation.py \
  --k 4 --cutoff 15 \
  --output /tmp/degree21-k4-overlap.json
```


## 13. Exact residue-dual transport

The wall transition on a coefficient density of pole order \(p\) has the
pairing-preserving contragredient

\&#91;
U\epsilon_{m,l}
 =\sum_q\binom{p-m-2l-1}{q}\lambda^q
 \epsilon_{m-q(2k-1),l+qk}.
\&#93;

It satisfies \(U^\mathsf TT=I\).  The formula has been checked on every basis
vector of the 114-dimensional `P`, 180-dimensional `Q`, and 300-dimensional
equation-density wall saturations.  Hence left-null obstruction functionals
and forcing pairings transport exactly through the ambient wall chain map.

## 14. Triple-overlap core

Through layer 15, \(T_\lambda\) is quadratic in \(\lambda\).  The
three-chart intersection at parameters `0`, `1`, and `-1` is therefore the
subspace stable under every wall parameter.  Its exact dimensions are

\&#91;
\dim E^{\mathrm{core}}=68,
\qquad
\dim W^{\mathrm{core}}=206.
\&#93;

A single pairwise overlap has dimensions 89 and 216.  Thus 21 deformation
directions and 10 equation directions pass one overlap but fail the
triple-overlap test.

## 15. Operation commutator and cyclic parameter line

Transporting the maximal support-admissible layer-four source field across the
wall forces a layer-eleven bracket whose action contains nonzero `P` exponent
5 and `Q` exponent 9 terms.  The old layer-eleven windows omit both.  This is
an exact required adjacent-chart operation term.

For the `F_2` quotient `u=z^5`, a `k=4` wall parameter must have `C_5`
character four.  If it is treated as an invariant scalar, the first return to
the original character occurs only at wall order five.  Reconciling the bare
layer-seven wall with a layer-four associated-graded direction would also
require normal weight `-3`; the resulting necessary bidegree is `(-3,4 mod
5)`.  This is localized chart data, not ordinary fixed-chart gauge.


## 16. Parameter weight is necessary but not sufficient

Assigning weight \(w\) to the wall parameter changes the bookkeeping layer
from \(r=2k-1\) to \(r+w\).  If the bare source pair is left unchanged, its
ordinary weighted-divergence defect becomes

\&#91;
(fz^2)' +(r+w-5)gz^2=wz^{2-k}.
\&#93;

For `k=4` and target layer four, \(w=-3\), so the defect is

\&#91;
-3z^{-2}\ne0.
\&#93;

Thus reweighting alone cannot identify the bare wall tangent with a
\(D_4\)-kernel class.  Keeping \(f=2z^{-3}\) uniquely restores the layer-four
identity with

\&#91;
g=-2z^{-4}.
\&#93;

The resulting candidate associated-graded action is

\&#91;
a_4=6z^{-3}p+2z^{-2}p',
\qquad
b_4=10z^{-2}q+2z^{-1}q'.
\&#93;

It exits the old layer-four window through principal parts
`A={-3,-2,-1}`, `B={-2,-1}`.  A complete repair must construct the
Rees/Euler mechanism that produces this correction and match its tangent line
to the archived residual quotient.
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_OVERLAP_THEOREM.md`

<pre><code class="language-markdown">
# Exact wall-shear overlap and master-equation covariance

**Status:** exact ambient Laurent-jet theorem and degree-21 finite-window
calculation. This constructs a genuine transported-window chart pair. It does
not yet identify the complete-chain presentation stabilizer or prove that the
transported coefficient space is the intended monomial Newton chart.

## 1. Density transport

Let

\&#91;
t'=t(1+h),\qquad z'=z(1+h)^2,\qquad
h=\lambda t^{2k-1}z^{-k}.
\&#93;

For a coefficient density with pole order \(p\), define

\&#91;
T^{(p)}_{k,\lambda}(t^nz^j)
=
\sum_{q\ge0}
\binom{n-p+2j}{q}\lambda^q
t^{n+q(2k-1)}z^{j-qk}.
\&#93;

On any finite normal cutoff this is a finite exact sum. It satisfies

\&#91;
T^{(p)}_{k,\lambda}T^{(p)}_{k,\mu}
=
T^{(p)}_{k,\lambda+\mu},
\qquad
(T^{(p)}_{k,\lambda})^{-1}=T^{(p)}_{k,-\lambda}.
\&#93;

## 2. Exact nonlinear master covariance

Write

\&#91;
\mathcal R_{\alpha,\beta}(A,B)
=
\alpha AB_z-\beta A_zB
+t(A_zB_t-A_tB_z)-z^2.
\&#93;

The coefficient pairs \(A,B\) have pole orders \(\alpha,\beta\). The residual
is a coefficient density of pole order

\&#91;
\gamma=\alpha+\beta-1.
\&#93;

Exact pullback of the determinant two-form gives

\&#91;
\boxed{
\mathcal R_{\alpha,\beta}
\left(T^{(\alpha)}_{k,\lambda}A,
      T^{(\beta)}_{k,\lambda}B\right)
=
T^{(\gamma)}_{k,\lambda}
\mathcal R_{\alpha,\beta}(A,B).
}
\&#93;

Differentiating at any base pair gives the full cumulative-jet chain map

\&#91;
D_{T(A,B)}\mathcal R\circ
\left(T^{(\alpha)}\oplus T^{(\beta)}\right)
=
T^{(\gamma)}\circ D_{(A,B)}\mathcal R.
\&#93;

This supplies the previously missing equation-space map for the ambient wall
overlap, including all lower-triangular normal-layer mixing.

## 3. A canonical transported-window chart pair

Let \(E_0\) be the archived full degree-21 coefficient window through layer
15 and let \(W_0\) be the complete support of its nonlinear master residual.
For nonzero \(\lambda\), put

\&#91;
E_\lambda=T_E(\lambda)E_0,\qquad
W_\lambda=T_W(\lambda)W_0.
\&#93;

Then

\&#91;
\mathcal R(E_\lambda)\subseteq W_\lambda
\&#93;

exactly. Thus \((E_0,W_0)\) and \((E_\lambda,W_\lambda)\) form a genuine
finite-dimensional ambient Laurent-jet chart pair.

The exact dimensions are:

| space | old dimension | minimal wall saturation | added |
| --- | ---: | ---: | ---: |
| \(P\)-coefficients | 61 | 114 | 53 |
| \(Q\)-coefficients | 125 | 180 | 55 |
| total deformation space \(E\) | 186 | 294 | 108 |
| equation density \(W\) | 257 | 300 | 43 |

For every tested nonzero parameter—and, by chainwise diagonal rescaling, for
every nonzero parameter—the old and transported spaces satisfy:

| space | intersection | sum | new independent directions |
| --- | ---: | ---: | ---: |
| \(P\) | 15 | 107 | 46 |
| \(Q\) | 74 | 176 | 51 |
| total \(E\) | 89 | 283 | 97 |
| \(W\) | 216 | 298 | 41 |

The deformation increment \(97=46+51\) is exactly the previously observed
first-order coefficient-wall exit rank. A single transported chart does not
span the whole orbit saturation: it misses 11 deformation coordinates and 2
equation coordinates that occur as independent second-order wall terms.
However,

\&#91;
\boxed{
E^{\mathrm{sat}}=E_0+E_1+E_{-1},
\qquad
W^{\mathrm{sat}}=W_0+W_1+W_{-1}.
}
\&#93;

This gives an exact three-chart finite overlap model.

## 4. Filtered conjugacy cannot lower seven to four

For \(k=4\), the infinitesimal generator has exact \(t\)-adic degree \(7\).
Let \(C\) be a filtration-preserving automorphism with filtration-preserving
inverse and invertible associated-graded map. If \(N\) has nonzero principal
symbol in degree seven, then

\&#91;
\sigma_7(CNC^{-1})
=
\operatorname{gr}(C)\sigma_7(N)\operatorname{gr}(C)^{-1}
\ne0.
\&#93;

Hence \(CNC^{-1}\) still has degree seven. Therefore the displayed wall shear
cannot become a normal layer-four tangent through a filtration-preserving
conjugacy. Any reconciliation must use a filtration-changing birational
coordinate map, assign degree \(-3\) to the wall parameter, or correct one of
the labels.

## 5. An explicit false obstruction removed by the wall arc

Take

\&#91;
A_0=z+\frac32z^2,\qquad B_0=z^2+z^3.
\&#93;

It satisfies

\&#91;
2A_0B_0'-3A_0'B_0=z^2.
\&#93;

The exact \(k=4\), \(\lambda=1\) wall transform through layer 15 is

\&#91;
A=A_0+3t^7z^{-2}+\frac32t^{14}z^{-6},
\&#93;

\&#91;
B=B_0+t^7(z^{-2}+3z^{-1})+3t^{14}z^{-5}.
\&#93;

The layer-seven correction lies in the kernel. At layer 14,

\&#91;
D_{14}(a_{14},b_{14})
=
-6z^{-5}+27z^{-4},
\&#93;

while the quadratic forcing from the layer-seven correction is

\&#91;
\Phi_{14}
=
6z^{-5}-27z^{-4}.
\&#93;

They cancel exactly. Setting the second wall correction to zero creates a
nonzero residual even though the full chart transition is an exact solution.
This is a small exact model of the logical error behind a
zero-new-parameter obstruction slice.

## 6. What remains

The construction solves the ambient coefficient and equation transport
problem. It does not yet determine:

- the intrinsic complete-chain fixed-presentation stabilizer;
- the intended adjacent monomial Newton window;
- the filtration-changing map, if any, connecting the public layer-four
  residual to the \(k=4\) wall;
- the actual `F_2` attachment matrices.

The next useful export is the real adjacent-chart normalization map. It can be
tested against the transported-window space above instead of discarding wall
overflow terms.


## 7. Dual and triple-overlap continuation

The exact obstruction-dual map is

\&#91;
U\epsilon_{m,l}
 =\sum_q\binom{p-m-2l-1}{q}\lambda^q
 \epsilon_{m-q(2k-1),l+qk},
\qquad U^\mathsf TT=I.
\&#93;

Forcing pairings and left-null obstruction spaces therefore transport exactly.

The pairwise deformation overlap has dimension 89, whereas the all-parameter
core detected by the charts `0`, `1`, and `-1` has dimension 68.  The
corresponding equation dimensions are 216 and 206.  Thus triple-overlap
compatibility imposes 21 additional deformation conditions and 10 additional
equation conditions beyond one pairwise transition.

The layer-four support-admissible field also acquires a compulsory
layer-eleven commutator term under the wall.  Finally, in the `F_2` gap-five
quotient the wall parameter is a character-four eigenparameter; scalar cyclic
descent sees its first return only at order five.
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_DUAL_TRIPLE_OVERLAP.md`

<pre><code class="language-markdown">
# Wall-shear dual transport and triple-overlap theorem

**Status:** exact finite Laurent-jet theorem through normal layer 15 for the
stored degree-21 support. The theorem supplies coefficient, equation,
obstruction-dual, forcing, inverse, and triple-overlap transport for the
ambient wall atlas. It does not identify the intrinsic complete-chain
stabilizer or prove that the transported Laurent windows are the intended
monomial Newton charts.

## 1. Contragredient residue transport

For a coefficient density of pole order `p`, write

\&#91;
e_{n,j}=t^{n-p}z^j.
\&#93;

The exact `k`-wall transport is

\&#91;
T_{k,\lambda}^{(p)}e_{n,j}
 =\sum_{q\ge0}
 \binom{n-p+2j}{q}\lambda^q
 e_{n+q(2k-1),j-qk}.
\&#93;

Let \(\epsilon_{n,j}\) denote the coefficient dual. At fixed normal layer it
is represented by the residue principal part

\&#91;
\epsilon_{n,j}(w)
 =\operatorname {Res}_{z=0}
   z^{-j-1}w_n(z)\,dz.
\&#93;

The dual functional in the transported chart must satisfy

\&#91;
\langle U_{k,\lambda}^{(p)}\ell,
        T_{k,\lambda}^{(p)}w\rangle
 =\langle\ell,w\rangle.
\&#93;

Since \(T_{k,\lambda}^{-1}=T_{k,-\lambda}\), one has

\&#91;
U_{k,\lambda}^{(p)}
 =\left(T_{k,\lambda}^{(p),-1}\right)^\mathsf T.
\&#93;

A direct coefficient calculation gives the closed formula

\&#91;
\boxed{
U_{k,\lambda}^{(p)}\epsilon_{m,l}
 =\sum_{q\ge0}
 \binom{p-m-2l-1}{q}\lambda^q
 \epsilon_{m-q(2k-1),l+qk}.
}
\&#93;

Indeed, the coefficient before applying the elementary binomial identity is

\&#91;
(-1)^q\binom{m-p+2l+q}{q}
 =\binom{p-m-2l-1}{q}.
\&#93;

The implementation checks \(U^\mathsf TT=I\) on every basis vector of the
complete layer-15 saturations:

| density | saturated dimension | maximum primal terms | maximum dual terms |
| --- | ---: | ---: | ---: |
| `P`, pole order 2 | 114 | 3 | 3 |
| `Q`, pole order 3 | 180 | 3 | 3 |
| equation residual, pole order 4 | 300 | 3 | 3 |

Thus every finite obstruction functional and forcing pairing transports
exactly. In particular, if

\&#91;
D_\lambda T_E=T_WD_0,
\qquad \ell^\mathsf TD_0=0,
\&#93;

then

\&#91;
\ell_\lambda=T_W^{-\mathsf T}\ell
\&#93;

satisfies

\&#91;
\ell_\lambda^\mathsf TD_\lambda=0.
\&#93;

For \(\Phi_\lambda=T_W\Phi\),

\&#91;
\boxed{
\langle\ell_\lambda,\Phi_\lambda\rangle
 =\langle\ell,\Phi\rangle.
}
\&#93;

This is the exact residue/forcing transport required by a chart theorem at
the ambient Laurent-jet level.

## 2. Pairwise overlap is not triple overlap

For `k=4`, the wall shift is seven. Through layer 15,

\&#91;
N_4^3=0,
\qquad
T_\lambda=I+\lambda N_4+\frac{\lambda^2}{2}N_4^2.
\&#93;

Let \(E_0\) be the old coefficient window. A vector common to the charts
with parameters \(0,1,-1\) lies in every transported chart. To see this,
project \(T_\lambda v\) to the coordinates outside \(E_0\). The result is a
polynomial of degree at most two in \(\lambda\). If it vanishes at
\(0,1,-1\), it vanishes identically.

Consequently,

\&#91;
\boxed{
E_0\cap E_1\cap E_{-1}
 =\{v\in E_0:T_\lambda v\in E_0\text{ for every }\lambda\}.
}
\&#93;

This is the maximal all-parameter stable core of the old window. The same
statement holds for the equation-density space.

The exact dimensions are:

| space | old | one pairwise overlap | all-parameter core | pairwise-only |
| --- | ---: | ---: | ---: | ---: |
| `P` | 61 | 15 | 8 | 7 |
| `Q` | 125 | 74 | 60 | 14 |
| total deformation `E` | 186 | 89 | 68 | 21 |
| equation density `W` | 257 | 216 | 206 | 10 |

Thus a two-chart check leaves 21 deformation directions and 10 equation
directions that fail the third-chart condition.

The all-parameter stability constraints split as follows:

| space | first-order external rank | extra rank from `N^2` | total |
| --- | ---: | ---: | ---: |
| `P` | 46 | 7 | 53 |
| `Q` | 51 | 14 | 65 |
| total `E` | 97 | 21 | 118 |
| `W` | 41 | 10 | 51 |

These are source-constraint ranks. The corresponding numbers of new ambient
target directions are smaller:

| space | from `N` | new directions from `N^2` | total saturation increment |
| --- | ---: | ---: | ---: |
| `P` | 46 | 7 | 53 |
| `Q` | 51 | 4 | 55 |
| total `E` | 97 | 11 | 108 |
| `W` | 41 | 2 | 43 |

The difference is important: multiple independent source constraints can
land in the same external coefficient coordinate. Counting overflow
monomials alone does not count triple-overlap conditions.

The eight `P` monomials stable under the entire wall orbit are

\&#91;
(0,1),\ (2,0),\ (2,4),\ (2,5),\ (3,4),\
(9,0),\ (9,1),\ (10,0),
\&#93;

where each pair is `(normal layer, z exponent)`. The implementation records
the analogous 60-dimensional `Q` core and 206-dimensional equation core.

## 3. Exact cocycle

On the stable core, every wall transport remains in the old finite window,
and

\&#91;
T_{b-c}T_{a-b}=T_{a-c},
\qquad T_{-\lambda}=T_\lambda^{-1}.
\&#93;

Therefore the three-chart ambient atlas satisfies the required inverse and
triple-overlap cocycle identities exactly. This is stronger than checking one
transition square, but weaker than a complete-chain chart theorem because the
intrinsic monomial charts and their admissible operation groups remain
unidentified.

## 4. Reproduction

```bash
python research-notes/p6-chart-correspondence/wall_shear_dual_transport.py \
  --k 4 --cutoff 15 \
  --output /tmp/wall-shear-dual.json

python research-notes/p6-chart-correspondence/degree21_k4_triple_overlap.py \
  --k 4 --cutoff 15 \
  --output /tmp/degree21-k4-triple-overlap.json
```
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_REES_FLOW.md`

<pre><code class="language-markdown">
# The corrected layer-four candidate is a Kummer Hamiltonian flow

**Status:** exact coordinate conversion and formal-flow calculation. This
strengthens the Rees-weight audit. It does not construct the missing
complete-chain chart.

## 1. Back to the original affine coordinates

The degree-21 coordinate dictionary is

\&#91;
t=x^4y,\qquad z=x^7y^2.
\&#93;

The unique corrected layer-four pair from the Rees-weight audit is

\&#91;
V=t^4\left(2z^{-3}\partial_z-2z^{-4}t\partial_t\right).
\&#93;

Writing

\&#91;
u=\frac{\delta t}{t},\qquad v=\frac{\delta z}{z},
\&#93;

the logarithmic coordinate equations are

\&#91;
4\frac{\delta x}{x}+\frac{\delta y}{y}=u,
\qquad
7\frac{\delta x}{x}+2\frac{\delta y}{y}=v.
\&#93;

Here

\&#91;
u=-2M,\qquad v=2M,\qquad
M=t^4z^{-4}=x^{-12}y^{-4}.
\&#93;

Consequently

\&#91;
\boxed{
V=-6x^{-11}y^{-4}\partial_x
  +22x^{-12}y^{-3}\partial_y.
}
\&#93;

Its ordinary divergence is zero.

## 2. Hamiltonian form

With the convention

\&#91;
D_H=H_y\partial_x-H_x\partial_y,
\&#93;

the field is Hamiltonian for

\&#91;
\boxed{H=2x^{-11}y^{-3}.}
\&#93;

On Laurent monomials,

\&#91;
V(x^ay^b)=(-6a+22b)x^{a-12}y^{b-4}.
\&#93;

In particular,

\&#91;
V(H)=0,
\qquad
V(M)=-16M^2.
\&#93;

The iterates of \(x\) have nonzero leading coefficient

\&#91;
V^n(x)=
\left(\prod_{j=0}^{n-1}(-6-16j)\right)
 x^{1-12n}y^{-4n},
\&#93;

so this Laurent derivation is not locally nilpotent.

## 3. Exact formal flow

Solving \(\dot M=-16M^2\) gives

\&#91;
M_s=\frac{M}{1+16sM}.
\&#93;

Put

\&#91;
R^8=1+16sM.
\&#93;

Then the exact flow is

\&#91;
\boxed{
 x_s=xR^{-3},\qquad
 y_s=yR^{11},\qquad
 t_s=tR^{-1},\qquad
 z_s=zR.
}
\&#93;

As a formal power series in \(s\), the binomial root \(R\) exists uniquely
with constant term one. Thus the corrected candidate is formally integrable.


## 4. The degree-eight quotient linearizes the flow

Set

\&#91;
\boxed{
H=2x^{-11}y^{-3}=\frac{2}{tz},
\qquad
Q=x^{12}y^4=\left(\frac zt\right)^4=M^{-1}.
}
\&#93;

Then

\&#91;
V(H)=0,
\qquad
V(Q)=16.
\&#93;

Thus on the quotient function field,

\&#91;
\boxed{H_s=H,\qquad Q_s=Q+16s.}
\&#93;

The exponent matrix of the monomial map \((x,y)\mapsto(H/2,Q)\) is

\&#91;
\begin{pmatrix}
-11&amp;-3\\
12&amp;4
\end{pmatrix},
\&#93;

with determinant \(-8\). Hence

\&#91;
&#91;K(x,y):K(H,Q)&#93;=8
\&#93;

generically. Explicitly,

\&#91;
x^8=\frac{16}{H^4Q^3},
\qquad
y^8=\frac{H^{12}Q^{11}}{4096}.
\&#93;

The Kummer root in the original flow is precisely

\&#91;
R^8=\frac{Q+16s}{Q}.
\&#93;

So the corrected field is not mysterious: it is an ordinary translation on
a degree-eight monomial quotient chart. The eighth-root extension is exactly
the inverse lattice-index obstruction to lifting that translation back to
\((x,y)\).


In the adjacent blowdown variables used by the stored proposition,

\&#91;
u=(xy)^{-1},\qquad v=y,
\&#93;

these quotient coordinates are

\&#91;
H=2u^{11}v^8,
\qquad
Q=u^{-12}v^{-8}.
\&#93;

Therefore

\&#91;
\boxed{K(H,Q)=K(u,v^8).}
\&#93;

The degree-eight quotient is exactly the \(\mu_8\)-quotient of the adjacent
blowdown chart.  The corrected field descends to this quotient, while the bare
`k=4` operation is the translation \(v\mapsto v+s\), which is not the same
quotient operation.  This isolates a precise missing lift in the public
correspondence claim.


Because

\&#91;
Q=\left(\frac zt\right)^4
\&#93;

has normal \(t\)-exponent \(-4\), translation in \(Q\) naturally has the
missing layer-four label.  This gives the strongest current repaired
correspondence candidate:

&gt; match the stored layer-four residual to the pullback of the quotient
&gt; translation \(Q\mapsto Q+16s\), not to the bare layer-seven translation
&gt; \(v\mapsto v+s\).

The scalar `16` is a parameter normalization.  What remains is an exact
coefficientwise comparison with the archived residual representative.

## 5. It is not a same-field rational chart operation

Over \(K(x,y,s)\), the radicand is

\&#91;
1+16sx^{-12}y^{-4}.
\&#93;

After multiplication by the Laurent unit \(x^{12}y^4\), its non-monomial
factor is the prime

\&#91;
x^{12}y^4+16s.
\&#93;

The radicand has valuation one at this prime. An eighth power has valuation
divisible by eight. Therefore the radicand is not an eighth power in
\(K(x,y,s)\), and the generic flow requires the degree-eight Kummer
extension

\&#91;
K(x,y,s)\subset K(x,y,s)(R),
\qquad R^8=1+16sM.
\&#93;

Hence the corrected field cannot be identified with an ordinary rational
one-parameter coordinate change on the same function field.

## 6. Compatibility with the F2 cyclic character

For the `F_2` quotient, \(z\) has `C_5` character one and the wall parameter
has character four. Both \(H\) and \(Q\) have character four, so the quotient
translation \(Q\mapsto Q+16s\) is equivariant. Since

\&#91;
M=t^4z^{-4}
\&#93;

has character one, \(sM\) is invariant modulo five. The Kummer radicand and
root equation are therefore compatible with cyclic descent. The independent
eighth-root extension nevertheless remains.

This gives a sharper alternative:

- the bare `k=4` wall is the polynomial translation \(y\mapsto y+s\) and
  occurs at normal layer seven;
- the corrected layer-four candidate is Hamiltonian and formally integrable,
  but algebraically lives on an eighth-root Kummer cover;
- identifying it with a complete-chain rechart requires a root-stack or
  filtration-changing construction, not a same-field polynomial wall shear.
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/F2_CYCLIC_WALL_DESCENT.md`

<pre><code class="language-markdown">
# Cyclic descent of a wall parameter in the F2 quotient

**Status:** exact character and filtration bookkeeping. This identifies the
parameter line required for an equivariant wall family. It does not supply
the missing `F_2` normal support windows or prove that the `k=4` wall is an
allowed complete-chain transition for `F_2`.

## 1. Character shift

Let the lattice quotient be

\&#91;
u=z^g,
\&#93;

with deck action

\&#91;
z\longmapsto\zeta z,
\qquad \zeta^g=1,
\&#93;

and assume the normal parameter is fixed. The order-\(q\) term in the
`k`-wall transport contains

\&#91;
\lambda^q z^{-qk}.
\&#93;

If \(\lambda\) is treated as an invariant scalar, the coefficient character
changes by

\&#91;
\chi_j\longmapsto\chi_{j-qk}.
\&#93;

Thus scalar wall transport mixes the cyclic character sectors.

An equivariant family instead requires

\&#91;
\boxed{
\lambda\longmapsto\zeta^k\lambda.
}
\&#93;

Then

\&#91;
\lambda^qz^{j-qk}
\longmapsto
\zeta^{qk+j-qk}\lambda^qz^{j-qk}
 =\zeta^j\lambda^qz^{j-qk},
\&#93;

so each original character sector is preserved over the eigenparameter
line.

## 2. Scalar descent sees only a return-order power

If the wall parameter must itself be invariant, the first order returning to
the original character is

\&#91;
q_0=\frac{g}{\gcd(g,k)}.
\&#93;

For `F_2`,

\&#91;
g=5,
\qquad k=4,
\&#93;

so

\&#91;
\boxed{q_0=5.}
\&#93;

The unweighted normal shift per wall order is seven, hence the first scalar
return occurs at normal shift

\&#91;
\boxed{5\cdot7=35.}
\&#93;

Equivalently, the invariant quotient parameter is locally represented by

\&#91;
\mu=\lambda^5.
\&#93;

Plain averaging in the coefficient space discards the intermediate
noninvariant wall terms. It therefore does not commute with recharting unless
the eigenparameter line is included in the descent datum.

## 3. Necessary bidegree for a layer-four reconciliation

The bare `k=4` wall starts at normal layer seven. If one tries to interpret
its first term as a layer-four rechart direction, the unique necessary normal
weight of \(\lambda\) is

\&#91;
\boxed{\operatorname{wt}_t(\lambda)=4-7=-3.}
\&#93;

Combined with cyclic equivariance in the `F_2` gap-five cover, the required
parameter bidegree would be

\&#91;
\boxed{
(\operatorname{wt}_t,\chi_{C_5})(\lambda)=(-3,4).
}
\&#93;

With this bookkeeping, one wall order has weighted normal degree four and the
first scalar return \(\lambda^5\) has weighted degree

\&#91;
5\cdot4=20.
\&#93;

The negative normal weight is significant. Such a parameter is not an
ordinary coordinate of the nonnegative `t`-adic Rees deformation base. It is
a localized or chart-moving parameter. Therefore a layer-four repair along
these lines would itself prove that the operation is a rechart rather than
fixed-chart gauge—but the corresponding Rees/groupoid construction still has
to be supplied.


## 4. Weight alone does not restore the layer operator

There is an additional compatibility condition.  The bare wall pair

\&#91;
f=2z^{-3},\qquad g=z^{-4}
\&#93;

is a kernel field for \(D_7\), not \(D_4\).  Reassigning the parameter weight
without changing the field gives

\&#91;
(fz^2)' +(4-5)gz^2=-3z^{-2}.
\&#93;

Thus the bidegree `(-3,4)` is necessary bookkeeping but not a complete
repair.  With the same horizontal component, the unique layer-four vertical
component is

\&#91;
g=-2z^{-4}.
\&#93;

A valid descent theorem must construct the Rees/Euler mechanism that produces
this correction and then transport its operation image across the chart
atlas.

## 5. Consequence for the `F_2` attachment problem

The exact order-520 recurrence uses cyclic invariance, but a wall transition
must be descended together with its parameter line. There are two distinct
questions:

1. solve the invariant coefficient recurrence in one fixed presentation;
2. glue presentations using eigenparameters and then descend the entire
   chart groupoid.

The first cannot replace the second. A scalar Reynolds operator sees only
powers at the return order and can miss the intermediate chart data required
for exact gluing.

## 6. Reproduction

```bash
python research-notes/p6-chart-correspondence/f2_cyclic_wall_descent.py \
  --gap 5 --k 4 --requested-layer 4 \
  --output /tmp/f2-cyclic-wall-descent.json
```
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/wall_shear_master_covariance.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact covariance of the normal-boundary master equation under wall shears.

For

    t' = t(1+h),  z' = z(1+h)^2,
    h = lambda * t^(2k-1) * z^(-k),

a coefficient density of pole order ``p`` is transported by

    T_p(t^n z^j)
      = sum_q binom(n-p+2j,q) lambda^q
          t^(n+q(2k-1)) z^(j-qk).

The determinant master residual has density pole order
``alpha + beta - 1``.  The module verifies, exactly over Q,

    R(T_alpha A, T_beta B)
      = T_(alpha+beta-1) R(A,B),

as well as the differentiated chain-map square and an explicit second-order
wall arc.  No computer-algebra dependency is required.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

Exponent = tuple&#91;int, int&#93;
Series = dict&#91;Exponent, Fraction&#93;


def q(value: Any) -&gt; Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise TypeError("booleans are not rational coefficients")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"unsupported rational coefficient {value!r}")


def scalar_text(value: Fraction) -&gt; str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def generalized_binomial(exponent: int, order: int) -&gt; Fraction:
    if order &lt; 0:
        return Fraction(0)
    value = Fraction(1)
    for index in range(order):
        value *= Fraction(exponent - index, index + 1)
    return value


def clean(series: Mapping&#91;Exponent, Fraction&#93;) -&gt; Series:
    return {key: value for key, value in series.items() if value}


def add(*series: Mapping&#91;Exponent, Fraction&#93;) -&gt; Series:
    result: defaultdict&#91;Exponent, Fraction&#93; = defaultdict(Fraction)
    for item in series:
        for key, value in item.items():
            result&#91;key&#93; += value
    return clean(result)


def scale(series: Mapping&#91;Exponent, Fraction&#93;, scalar: Fraction | int) -&gt; Series:
    scalar = q(scalar)
    return clean({key: scalar * value for key, value in series.items()})


def multiply(
    left: Mapping&#91;Exponent, Fraction&#93;,
    right: Mapping&#91;Exponent, Fraction&#93;,
    *,
    cutoff: int,
) -&gt; Series:
    result: defaultdict&#91;Exponent, Fraction&#93; = defaultdict(Fraction)
    for (left_layer, left_power), left_value in left.items():
        for (right_layer, right_power), right_value in right.items():
            layer = left_layer + right_layer
            if layer &lt;= cutoff:
                result&#91;(layer, left_power + right_power)&#93; += (
                    left_value * right_value
                )
    return clean(result)


def derivative_z(series: Mapping&#91;Exponent, Fraction&#93;) -&gt; Series:
    return clean(
        {
            (layer, power - 1): value * power
            for (layer, power), value in series.items()
            if power
        }
    )


def t_derivative(series: Mapping&#91;Exponent, Fraction&#93;) -&gt; Series:
    """Return ``t * partial_t(series)``."""

    return clean(
        {
            (layer, power): value * layer
            for (layer, power), value in series.items()
            if layer
        }
    )


def master(
    A: Mapping&#91;Exponent, Fraction&#93;,
    B: Mapping&#91;Exponent, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    cutoff: int,
) -&gt; Series:
    """The scalar master expression before subtracting ``Psi=z^2``."""

    return add(
        scale(multiply(A, derivative_z(B), cutoff=cutoff), alpha),
        scale(multiply(derivative_z(A), B, cutoff=cutoff), -beta),
        multiply(derivative_z(A), t_derivative(B), cutoff=cutoff),
        scale(
            multiply(t_derivative(A), derivative_z(B), cutoff=cutoff),
            -1,
        ),
    )


def residual(
    A: Mapping&#91;Exponent, Fraction&#93;,
    B: Mapping&#91;Exponent, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    cutoff: int,
) -&gt; Series:
    return add(
        master(A, B, alpha=alpha, beta=beta, cutoff=cutoff),
        {(0, 2): Fraction(-1)},
    )


def linearization(
    A: Mapping&#91;Exponent, Fraction&#93;,
    B: Mapping&#91;Exponent, Fraction&#93;,
    a: Mapping&#91;Exponent, Fraction&#93;,
    b: Mapping&#91;Exponent, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    cutoff: int,
) -&gt; Series:
    return add(
        master(a, B, alpha=alpha, beta=beta, cutoff=cutoff),
        master(A, b, alpha=alpha, beta=beta, cutoff=cutoff),
    )


def transport(
    series: Mapping&#91;Exponent, Fraction&#93;,
    *,
    pole_order: int,
    k: int,
    parameter: Fraction | int,
    cutoff: int,
) -&gt; Series:
    """Pull a primed coefficient density back to the unprimed wall chart."""

    if k &lt; 1:
        raise ValueError("k must be positive")
    parameter = q(parameter)
    shift = 2 * k - 1
    result: defaultdict&#91;Exponent, Fraction&#93; = defaultdict(Fraction)
    for (layer, power), value in series.items():
        wall_order = 0
        while layer + wall_order * shift &lt;= cutoff:
            coefficient = generalized_binomial(
                layer - pole_order + 2 * power,
                wall_order,
            )
            if coefficient:
                result&#91;
                    (
                        layer + wall_order * shift,
                        power - wall_order * k,
                    )
                &#93; += value * coefficient * parameter**wall_order
            wall_order += 1
    return clean(result)


def extract_layer(series: Mapping&#91;Exponent, Fraction&#93;, layer: int) -&gt; dict&#91;int, Fraction&#93;:
    return {
        power: value
        for (current_layer, power), value in series.items()
        if current_layer == layer
    }


def polynomial_series(polynomial: Mapping&#91;int, Fraction&#93;, layer: int = 0) -&gt; Series:
    return {(layer, power): value for power, value in polynomial.items() if value}


def determinant_layer(
    A0: Mapping&#91;int, Fraction&#93;,
    B0: Mapping&#91;int, Fraction&#93;,
    a: Mapping&#91;int, Fraction&#93;,
    b: Mapping&#91;int, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    layer: int,
) -&gt; dict&#91;int, Fraction&#93;:
    """The universal linear layer operator in scalar-coefficient form."""

    A = polynomial_series(A0)
    B = polynomial_series(B0)
    aa = polynomial_series(a)
    bb = polynomial_series(b)
    result = add(
        scale(multiply(aa, derivative_z(B), cutoff=0), alpha - layer),
        scale(multiply(B, derivative_z(aa), cutoff=0), -beta),
        scale(multiply(A, derivative_z(bb), cutoff=0), alpha),
        scale(multiply(bb, derivative_z(A), cutoff=0), layer - beta),
    )
    return extract_layer(result, 0)


def series_json(series: Mapping&#91;Exponent, Fraction&#93;) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        {
            "layer": layer,
            "z_exponent": power,
            "coefficient": scalar_text(value),
        }
        for (layer, power), value in sorted(series.items())
    &#93;


def polynomial_json(polynomial: Mapping&#91;int, Fraction&#93;) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        {"z_exponent": power, "coefficient": scalar_text(value)}
        for power, value in sorted(polynomial.items())
    &#93;


def verify_covariance(
    A: Mapping&#91;Exponent, Fraction&#93;,
    B: Mapping&#91;Exponent, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    k: int,
    parameter: Fraction,
    cutoff: int,
) -&gt; bool:
    transformed_A = transport(
        A,
        pole_order=alpha,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    transformed_B = transport(
        B,
        pole_order=beta,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    left = residual(
        transformed_A,
        transformed_B,
        alpha=alpha,
        beta=beta,
        cutoff=cutoff,
    )
    right = transport(
        residual(A, B, alpha=alpha, beta=beta, cutoff=cutoff),
        pole_order=alpha + beta - 1,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    return left == right


def toy_wall_arc(*, k: int = 4, cutoff: int = 15) -&gt; dict&#91;str, Any&#93;:
    """A nontrivial exact face whose wall arc needs a second-order correction."""

    alpha, beta = 2, 3
    A0: Series = {(0, 1): Fraction(1), (0, 2): Fraction(3, 2)}
    B0: Series = {(0, 2): Fraction(1), (0, 3): Fraction(1)}
    if residual(A0, B0, alpha=alpha, beta=beta, cutoff=cutoff):
        raise AssertionError("the toy face does not satisfy Psi=z^2")

    transformed_A = transport(
        A0, pole_order=alpha, k=k, parameter=1, cutoff=cutoff
    )
    transformed_B = transport(
        B0, pole_order=beta, k=k, parameter=1, cutoff=cutoff
    )
    if residual(
        transformed_A,
        transformed_B,
        alpha=alpha,
        beta=beta,
        cutoff=cutoff,
    ):
        raise AssertionError("the exact wall arc does not solve the master equation")

    shift = 2 * k - 1
    second_layer = 2 * shift
    A0_poly = extract_layer(A0, 0)
    B0_poly = extract_layer(B0, 0)
    a_first = extract_layer(transformed_A, shift)
    b_first = extract_layer(transformed_B, shift)
    a_second = extract_layer(transformed_A, second_layer)
    b_second = extract_layer(transformed_B, second_layer)

    first_linear = determinant_layer(
        A0_poly,
        B0_poly,
        a_first,
        b_first,
        alpha=alpha,
        beta=beta,
        layer=shift,
    )
    second_linear = determinant_layer(
        A0_poly,
        B0_poly,
        a_second,
        b_second,
        alpha=alpha,
        beta=beta,
        layer=second_layer,
    )
    quadratic = extract_layer(
        master(
            polynomial_series(a_first, shift),
            polynomial_series(b_first, shift),
            alpha=alpha,
            beta=beta,
            cutoff=cutoff,
        ),
        second_layer,
    )
    cancellation = add(
        polynomial_series(second_linear),
        polynomial_series(quadratic),
    )

    return {
        "face": {
            "A0": polynomial_json(A0_poly),
            "B0": polynomial_json(B0_poly),
        },
        "first_nonzero_layer": shift,
        "second_wall_layer": second_layer,
        "first_correction": {
            "a": polynomial_json(a_first),
            "b": polynomial_json(b_first),
            "linear_image": polynomial_json(first_linear),
            "kernel_verified": not first_linear,
        },
        "second_correction": {
            "a": polynomial_json(a_second),
            "b": polynomial_json(b_second),
            "linear_image": polynomial_json(second_linear),
            "quadratic_forcing": polynomial_json(quadratic),
            "cancellation_verified": not cancellation,
        },
        "zero_second_correction_slice": {
            "residual": polynomial_json(quadratic),
            "inconsistent_with_exact_wall_arc": bool(quadratic),
        },
    }


def build_report(*, k: int, cutoff: int, parameter: Fraction) -&gt; dict&#91;str, Any&#93;:
    alpha, beta = 2, 3
    sample_A: Series = {
        (0, 1): Fraction(1),
        (0, 2): Fraction(2),
        (1, 0): Fraction(3),
        (4, 3): Fraction(1, 2),
    }
    sample_B: Series = {
        (0, 2): Fraction(1),
        (0, 3): Fraction(1),
        (2, -1): Fraction(2),
        (5, 4): Fraction(-1),
    }
    sample_a: Series = {(0, 0): Fraction(2), (3, 2): Fraction(-1)}
    sample_b: Series = {(1, 1): Fraction(3), (4, -2): Fraction(1)}

    transformed_A = transport(
        sample_A,
        pole_order=alpha,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    transformed_B = transport(
        sample_B,
        pole_order=beta,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    transformed_a = transport(
        sample_a,
        pole_order=alpha,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    transformed_b = transport(
        sample_b,
        pole_order=beta,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    left_linear = linearization(
        transformed_A,
        transformed_B,
        transformed_a,
        transformed_b,
        alpha=alpha,
        beta=beta,
        cutoff=cutoff,
    )
    right_linear = transport(
        linearization(
            sample_A,
            sample_B,
            sample_a,
            sample_b,
            alpha=alpha,
            beta=beta,
            cutoff=cutoff,
        ),
        pole_order=alpha + beta - 1,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )

    group_left = transport(
        transport(
            sample_A,
            pole_order=alpha,
            k=k,
            parameter=Fraction(2, 3),
            cutoff=cutoff,
        ),
        pole_order=alpha,
        k=k,
        parameter=Fraction(-1, 5),
        cutoff=cutoff,
    )
    group_right = transport(
        sample_A,
        pole_order=alpha,
        k=k,
        parameter=Fraction(7, 15),
        cutoff=cutoff,
    )

    return {
        "schema_version": 1,
        "name": "wall-shear master-equation covariance",
        "alpha": alpha,
        "beta": beta,
        "equation_density_pole_order": alpha + beta - 1,
        "k": k,
        "normal_layer_shift": 2 * k - 1,
        "cutoff": cutoff,
        "parameter": scalar_text(parameter),
        "transport_formula": (
            "T_p(t^n z^j)=sum_q binom(n-p+2j,q) lambda^q "
            "t^(n+q(2k-1)) z^(j-qk)"
        ),
        "master_covariance": (
            "R(T_alpha A,T_beta B)=T_(alpha+beta-1)R(A,B)"
        ),
        "master_covariance_verified": verify_covariance(
            sample_A,
            sample_B,
            alpha=alpha,
            beta=beta,
            k=k,
            parameter=parameter,
            cutoff=cutoff,
        ),
        "linearized_chain_map_verified": left_linear == right_linear,
        "additive_group_law_verified": group_left == group_right,
        "rhs_z_squared_fixed": transport(
            {(0, 2): Fraction(1)},
            pole_order=alpha + beta - 1,
            k=k,
            parameter=parameter,
            cutoff=cutoff,
        )
        == {(0, 2): Fraction(1)},
        "filtered_conjugacy_boundary": {
            "statement": (
                "A filtration-preserving conjugacy with invertible associated "
                "graded map preserves the principal shift 2k-1."
            ),
            "k4_shift": 7 if k == 4 else None,
            "can_become_layer_four_by_filtered_conjugacy": (
                False if k == 4 else None
            ),
        },
        "toy_exact_wall_arc": toy_wall_arc(k=k, cutoff=cutoff),
    }


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--cutoff", type=int, default=15)
    parser.add_argument("--parameter", default="1")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)

    report = build_report(
        k=args.k,
        cutoff=args.cutoff,
        parameter=Fraction(args.parameter),
    )
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_jet_transport_audit.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Build the exact first-order k=4 transport on the stored full support.

For a normal basis monomial

    e_(n,j) = t^(n-alpha) z^j,

the derivative at ``lambda=0`` of ``Y -&gt; Y+lambda X^(-k)`` is

    N_k e_(n,j) = (n-alpha+2j) e_(n+2k-1,j-k).

This script applies that formula to every basis monomial in the archived full
support.  It separates internal entries, exits through a coefficient-window
wall, terms beyond the finite stored cutoff, and zero entries.  It also reports
the powers of the projected sparse operator on the old window.

The ambient exact transport is ``exp(lambda N_k)``: after each application the
coefficient drops by one, so

    N_k^q e_(n,j)
      = (n-alpha+2j)_(q) e_(n+q(2k-1),j-qk),

where ``(a)_(q)`` is the falling factorial.  The projected old-window matrix is
a diagnostic only; a genuine chart transition needs the adjacent support
window rather than discarding the reported overflow.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Mapping, Sequence


BasisElement = tuple&#91;int, int&#93;


def full_layers(document: Mapping&#91;str, Any&#93;) -&gt; dict&#91;int, Mapping&#91;str, Any&#93;&#93;:
    cases = document.get("cases")
    if not isinstance(cases, list):
        raise ValueError("support document has no cases list")
    full = next(
        (case for case in cases if isinstance(case, Mapping) and case.get("label") == "full"),
        None,
    )
    if not isinstance(full, Mapping):
        raise ValueError("support document has no full case")
    layers = full.get("layers")
    if not isinstance(layers, list):
        raise ValueError("full support case has no layers list")
    result: dict&#91;int, Mapping&#91;str, Any&#93;&#93; = {}
    for layer in layers:
        if not isinstance(layer, Mapping) or not isinstance(layer.get("r"), int):
            raise ValueError("invalid full support layer")
        result&#91;int(layer&#91;"r"&#93;)&#93; = layer
    return result


def component_supports(
    layers: Mapping&#91;int, Mapping&#91;str, Any&#93;&#93;, component: str
) -&gt; dict&#91;int, list&#91;int&#93;&#93;:
    if component not in {"P", "Q"}:
        raise ValueError("component must be P or Q")
    key = "a_support" if component == "P" else "b_support"
    result: dict&#91;int, list&#91;int&#93;&#93; = {}
    for normal_layer, layer in sorted(layers.items()):
        values = layer.get(key, &#91;&#93;)
        if not isinstance(values, list) or not all(
            isinstance(value, int) and not isinstance(value, bool) for value in values
        ):
            raise ValueError(f"invalid {key} at layer {normal_layer}")
        result&#91;normal_layer&#93; = list(values)
    return result


def projected_operator(
    supports: Mapping&#91;int, Sequence&#91;int&#93;&#93;, pole_order: int, k: int
) -&gt; tuple&#91;list&#91;BasisElement&#93;, dict&#91;BasisElement, tuple&#91;BasisElement, int&#93;&#93;&#93;:
    basis = &#91;
        (normal_layer, exponent)
        for normal_layer in sorted(supports)
        for exponent in supports&#91;normal_layer&#93;
    &#93;
    basis_set = set(basis)
    shift = 2 * k - 1
    operator: dict&#91;BasisElement, tuple&#91;BasisElement, int&#93;&#93; = {}
    for normal_layer, exponent in basis:
        coefficient = normal_layer - pole_order + 2 * exponent
        target = (normal_layer + shift, exponent - k)
        if coefficient != 0 and target in basis_set:
            operator&#91;(normal_layer, exponent)&#93; = (target, coefficient)
    return basis, operator


def projected_power_entries(
    basis: Sequence&#91;BasisElement&#93;,
    operator: Mapping&#91;BasisElement, tuple&#91;BasisElement, int&#93;&#93;,
    power: int,
) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    if power &lt; 1:
        raise ValueError("power must be positive")
    entries: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    for source in basis:
        current = source
        coefficient = 1
        for _ in range(power):
            image = operator.get(current)
            if image is None:
                break
            current, factor = image
            coefficient *= factor
        else:
            entries.append(
                {
                    "source_layer": source&#91;0&#93;,
                    "source_exponent": source&#91;1&#93;,
                    "target_layer": current&#91;0&#93;,
                    "target_exponent": current&#91;1&#93;,
                    "coefficient": coefficient,
                }
            )
    return entries


def component_report(
    supports: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    component: str,
    pole_order: int,
    k: int,
) -&gt; dict&#91;str, Any&#93;:
    maximum_layer = max(supports)
    shift = 2 * k - 1
    internal: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    window_exit: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    beyond_cutoff: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    zero: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;

    for source_layer in sorted(supports):
        for source_exponent in supports&#91;source_layer&#93;:
            coefficient = source_layer - pole_order + 2 * source_exponent
            target_layer = source_layer + shift
            target_exponent = source_exponent - k
            entry = {
                "source_layer": source_layer,
                "source_exponent": source_exponent,
                "coefficient": coefficient,
                "target_layer": target_layer,
                "target_exponent": target_exponent,
            }
            if coefficient == 0:
                zero.append(entry)
            elif target_layer &gt; maximum_layer:
                beyond_cutoff.append(entry)
            elif target_exponent in supports.get(target_layer, &#91;&#93;):
                internal.append(entry)
            else:
                window_exit.append(entry)

    basis, operator = projected_operator(supports, pole_order, k)
    projected_powers: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    power = 1
    while True:
        entries = projected_power_entries(basis, operator, power)
        projected_powers.append(
            {
                "power": power,
                "rank": len(entries),
                "entries": entries,
            }
        )
        if not entries:
            break
        power += 1
        if power &gt; len(basis) + 1:
            raise AssertionError("projected operator did not become nilpotent")

    def layer_counts(entries: Sequence&#91;Mapping&#91;str, Any&#93;&#93;) -&gt; list&#91;dict&#91;str, int&#93;&#93;:
        counts = Counter(int(entry&#91;"source_layer"&#93;) for entry in entries)
        return &#91;
            {"source_layer": normal_layer, "count": counts&#91;normal_layer&#93;}
            for normal_layer in sorted(counts)
        &#93;

    return {
        "component": component,
        "pole_order": pole_order,
        "domain_dimension": len(basis),
        "maximum_stored_layer": maximum_layer,
        "first_order_internal_rank": len(internal),
        "first_order_internal_entries": internal,
        "window_exit_count": len(window_exit),
        "window_exit_by_source_layer": layer_counts(window_exit),
        "window_exit_entries": window_exit,
        "beyond_cutoff_count": len(beyond_cutoff),
        "beyond_cutoff_by_source_layer": layer_counts(beyond_cutoff),
        "beyond_cutoff_entries": beyond_cutoff,
        "zero_entry_count": len(zero),
        "zero_entries": zero,
        "projected_operator_powers": projected_powers,
        "projected_nilpotence_index": projected_powers&#91;-1&#93;&#91;"power"&#93;,
    }


def analyze(document: Mapping&#91;str, Any&#93;, k: int) -&gt; dict&#91;str, Any&#93;:
    if not isinstance(k, int) or isinstance(k, bool) or k &lt; 1:
        raise ValueError("k must be a positive integer")
    layers = full_layers(document)
    p_report = component_report(
        component_supports(layers, "P"),
        component="P",
        pole_order=2,
        k=k,
    )
    q_report = component_report(
        component_supports(layers, "Q"),
        component="Q",
        pole_order=3,
        k=k,
    )
    return {
        "schema_version": 1,
        "name": "degree-21 full-window infinitesimal wall transport",
        "k": k,
        "normal_layer_shift": 2 * k - 1,
        "basis_formula": (
            "N_k e_(n,j)=(n-alpha+2j)e_(n+2k-1,j-k)"
        ),
        "ambient_exponential_formula": (
            "F_lambda^*=exp(lambda N_k), with "
            "N_k^q e_(n,j)=(n-alpha+2j)_(q)e_(n+q(2k-1),j-qk)"
        ),
        "components": &#91;p_report, q_report&#93;,
        "total_domain_dimension": (
            p_report&#91;"domain_dimension"&#93; + q_report&#91;"domain_dimension"&#93;
        ),
        "total_first_order_internal_rank": (
            p_report&#91;"first_order_internal_rank"&#93;
            + q_report&#91;"first_order_internal_rank"&#93;
        ),
        "total_window_exit_count": (
            p_report&#91;"window_exit_count"&#93; + q_report&#91;"window_exit_count"&#93;
        ),
        "total_beyond_cutoff_count": (
            p_report&#91;"beyond_cutoff_count"&#93; + q_report&#91;"beyond_cutoff_count"&#93;
        ),
        "total_zero_entry_count": (
            p_report&#91;"zero_entry_count"&#93; + q_report&#91;"zero_entry_count"&#93;
        ),
        "interpretation": (
            "The internal matrix is only the projection to the old fixed-chart "
            "window. The window-exit entries must be transported into an "
            "explicit adjacent-chart basis; deleting them is not a chart "
            "correspondence theorem."
        ),
    }


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("supports", type=Path)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)

    try:
        document = json.loads(args.supports.read_text(encoding="utf-8"))
        if not isinstance(document, Mapping):
            raise ValueError("support input must be a JSON object")
        result = analyze(document, args.k)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_overlap_saturation.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Construct the minimal finite transported-window overlap for degree 21.

The old full-support coefficient spaces are closed under neither the ``k=4``
wall generator nor its exponential.  This program constructs the smallest
layer-15 Laurent support containing the old space and closed under that
generator.  It then compares the old chart with one transported chart and
with the two opposite transported charts.

All ranks are exact over Q and use only the Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from wall_shear_master_covariance import generalized_binomial

BasisElement = tuple&#91;int, int&#93;
Support = dict&#91;int, list&#91;int&#93;&#93;
Matrix = list&#91;list&#91;Fraction&#93;&#93;


def full_support_fixture() -&gt; dict&#91;str, Support&#93;:
    p_supports: Support = {
        0: list(range(1, 9)),
        1: list(range(1, 9)),
        2: list(range(0, 9)),
    }
    for layer in range(3, 11):
        p_supports&#91;layer&#93; = list(range(0, 11 - layer))
    for layer in range(11, 16):
        p_supports&#91;layer&#93; = &#91;&#93;

    q_supports: Support = {
        0: list(range(2, 13)),
        1: list(range(2, 13)),
        2: list(range(1, 13)),
        3: list(range(0, 13)),
    }
    for layer in range(4, 16):
        q_supports&#91;layer&#93; = list(range(0, 16 - layer))
    return {"P": p_supports, "Q": q_supports}


def basis_from_support(support: Mapping&#91;int, Sequence&#91;int&#93;&#93;) -&gt; list&#91;BasisElement&#93;:
    return sorted(
        (layer, power)
        for layer, powers in support.items()
        for power in powers
    )


def saturate(
    support: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    pole_order: int,
    k: int,
    cutoff: int,
) -&gt; list&#91;BasisElement&#93;:
    shift = 2 * k - 1
    result = set(basis_from_support(support))
    while True:
        additions: set&#91;BasisElement&#93; = set()
        for layer, power in result:
            coefficient = layer - pole_order + 2 * power
            target = (layer + shift, power - k)
            if coefficient and target&#91;0&#93; &lt;= cutoff:
                additions.add(target)
        new = additions - result
        if not new:
            return sorted(result)
        result.update(new)


def matrix_rank(matrix: Matrix) -&gt; int:
    if not matrix:
        return 0
    rows = &#91;row&#91;:&#93; for row in matrix&#93;
    columns = len(rows&#91;0&#93;)
    if any(len(row) != columns for row in rows):
        raise ValueError("ragged matrix")
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows&#91;row&#93;&#91;column&#93;),
            None,
        )
        if pivot is None:
            continue
        rows&#91;pivot_row&#93;, rows&#91;pivot&#93; = rows&#91;pivot&#93;, rows&#91;pivot_row&#93;
        scale = rows&#91;pivot_row&#93;&#91;column&#93;
        rows&#91;pivot_row&#93; = &#91;value / scale for value in rows&#91;pivot_row&#93;&#93;
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows&#91;row&#93;&#91;column&#93;
            if factor:
                rows&#91;row&#93; = &#91;
                    value - factor * pivot_value
                    for value, pivot_value in zip(rows&#91;row&#93;, rows&#91;pivot_row&#93;)
                &#93;
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def horizontal_join(left: Matrix, right: Matrix) -&gt; Matrix:
    if len(left) != len(right):
        raise ValueError("row counts do not agree")
    return &#91;a + b for a, b in zip(left, right)&#93;


def external_transport_matrix(
    old_basis: Sequence&#91;BasisElement&#93;,
    saturated_basis: Sequence&#91;BasisElement&#93;,
    *,
    pole_order: int,
    k: int,
    parameter: Fraction,
    cutoff: int,
) -&gt; tuple&#91;list&#91;BasisElement&#93;, Matrix&#93;:
    old_set = set(old_basis)
    external = &#91;element for element in saturated_basis if element not in old_set&#93;
    external_index = {element: index for index, element in enumerate(external)}
    matrix = &#91;
        &#91;Fraction(0) for _ in range(len(old_basis))&#93;
        for _ in range(len(external))
    &#93;
    shift = 2 * k - 1
    for column, (layer, power) in enumerate(old_basis):
        wall_order = 1
        while layer + wall_order * shift &lt;= cutoff:
            target = (
                layer + wall_order * shift,
                power - wall_order * k,
            )
            coefficient = generalized_binomial(
                layer - pole_order + 2 * power,
                wall_order,
            )
            if target in external_index and coefficient:
                matrix&#91;external_index&#91;target&#93;&#93;&#91;column&#93; += (
                    coefficient * parameter**wall_order
                )
            wall_order += 1
    return external, matrix


def rational_text(value: Fraction) -&gt; str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def matrix_digest(matrix: Matrix) -&gt; str:
    payload = &#91;
        &#91;rational_text(value) for value in row&#93;
        for row in matrix
    &#93;
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":"), sort_keys=False).encode()
    ).hexdigest()


def added_by_layer(
    old_basis: Sequence&#91;BasisElement&#93;,
    saturated_basis: Sequence&#91;BasisElement&#93;,
) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    old = set(old_basis)
    grouped: defaultdict&#91;int, list&#91;int&#93;&#93; = defaultdict(list)
    for layer, power in saturated_basis:
        if (layer, power) not in old:
            grouped&#91;layer&#93;.append(power)
    return &#91;
        {"layer": layer, "z_exponents": sorted(powers), "count": len(powers)}
        for layer, powers in sorted(grouped.items())
    &#93;


def analyze_space(
    name: str,
    support: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    pole_order: int,
    k: int,
    cutoff: int,
) -&gt; dict&#91;str, Any&#93;:
    old_basis = basis_from_support(support)
    saturated_basis = saturate(
        support,
        pole_order=pole_order,
        k=k,
        cutoff=cutoff,
    )
    external, plus = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(1),
        cutoff=cutoff,
    )
    _, minus = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(-1),
        cutoff=cutoff,
    )
    _, twice = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(2),
        cutoff=cutoff,
    )
    external_rank = matrix_rank(plus)
    if matrix_rank(twice) != external_rank:
        raise AssertionError("nonzero wall parameters changed the overlap rank")
    opposite_rank = matrix_rank(horizontal_join(plus, minus))

    old_dimension = len(old_basis)
    saturated_dimension = len(saturated_basis)
    sum_dimension = old_dimension + external_rank
    intersection_dimension = old_dimension - external_rank
    opposite_span_dimension = old_dimension + opposite_rank

    return {
        "name": name,
        "pole_order": pole_order,
        "old_dimension": old_dimension,
        "saturated_dimension": saturated_dimension,
        "added_dimension": saturated_dimension - old_dimension,
        "one_nonzero_transported_chart": {
            "external_increment": external_rank,
            "intersection_dimension": intersection_dimension,
            "sum_dimension": sum_dimension,
            "saturation_defect": saturated_dimension - sum_dimension,
            "rank_constant_for_nonzero_parameters_verified_at": &#91;"1", "2", "-1"&#93;,
        },
        "base_plus_opposite_charts": {
            "span_dimension": opposite_span_dimension,
            "spans_minimal_saturation": (
                opposite_span_dimension == saturated_dimension
            ),
        },
        "added_basis_by_layer": added_by_layer(old_basis, saturated_basis),
        "external_basis_dimension": len(external),
        "positive_external_matrix_sha256": matrix_digest(plus),
        "negative_external_matrix_sha256": matrix_digest(minus),
    }


def master_support(
    p_supports: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    q_supports: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    alpha: int,
    beta: int,
    cutoff: int,
) -&gt; Support:
    result: defaultdict&#91;int, set&#91;int&#93;&#93; = defaultdict(set)
    for left_layer, left_powers in p_supports.items():
        for right_layer, right_powers in q_supports.items():
            layer = left_layer + right_layer
            if layer &gt; cutoff:
                continue
            for left_power in left_powers:
                for right_power in right_powers:
                    coefficient = (
                        alpha * right_power
                        - beta * left_power
                        + right_layer * left_power
                        - left_layer * right_power
                    )
                    if coefficient:
                        result&#91;layer&#93;.add(left_power + right_power - 1)
    result&#91;0&#93;.add(2)
    return {
        layer: sorted(powers)
        for layer, powers in sorted(result.items())
    }


def support_summary(support: Mapping&#91;int, Sequence&#91;int&#93;&#93;) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        {
            "layer": layer,
            "minimum_exponent": min(powers) if powers else None,
            "maximum_exponent": max(powers) if powers else None,
            "dimension": len(powers),
            "contiguous": (
                not powers
                or len(powers) == max(powers) - min(powers) + 1
            ),
        }
        for layer, powers in sorted(support.items())
    &#93;


def analyze(*, k: int = 4, cutoff: int = 15) -&gt; dict&#91;str, Any&#93;:
    alpha, beta = 2, 3
    supports = full_support_fixture()
    p_report = analyze_space(
        "P coefficients",
        supports&#91;"P"&#93;,
        pole_order=alpha,
        k=k,
        cutoff=cutoff,
    )
    q_report = analyze_space(
        "Q coefficients",
        supports&#91;"Q"&#93;,
        pole_order=beta,
        k=k,
        cutoff=cutoff,
    )
    equation_support = master_support(
        supports&#91;"P"&#93;,
        supports&#91;"Q"&#93;,
        alpha=alpha,
        beta=beta,
        cutoff=cutoff,
    )
    equation_report = analyze_space(
        "master-equation density",
        equation_support,
        pole_order=alpha + beta - 1,
        k=k,
        cutoff=cutoff,
    )

    deformation_old = p_report&#91;"old_dimension"&#93; + q_report&#91;"old_dimension"&#93;
    deformation_saturated = (
        p_report&#91;"saturated_dimension"&#93; + q_report&#91;"saturated_dimension"&#93;
    )
    deformation_external = (
        p_report&#91;"one_nonzero_transported_chart"&#93;&#91;"external_increment"&#93;
        + q_report&#91;"one_nonzero_transported_chart"&#93;&#91;"external_increment"&#93;
    )
    deformation_intersection = (
        p_report&#91;"one_nonzero_transported_chart"&#93;&#91;"intersection_dimension"&#93;
        + q_report&#91;"one_nonzero_transported_chart"&#93;&#91;"intersection_dimension"&#93;
    )
    deformation_sum = deformation_old + deformation_external
    opposite_span = (
        p_report&#91;"base_plus_opposite_charts"&#93;&#91;"span_dimension"&#93;
        + q_report&#91;"base_plus_opposite_charts"&#93;&#91;"span_dimension"&#93;
    )

    report = {
        "schema_version": 1,
        "name": "degree-21 k=4 transported-window overlap",
        "alpha": alpha,
        "beta": beta,
        "k": k,
        "normal_layer_shift": 2 * k - 1,
        "cutoff": cutoff,
        "interpretation": (
            "E_lambda=T_E(lambda)E_0 and W_lambda=T_W(lambda)W_0 form an "
            "exact ambient Laurent-jet chart pair. They are not yet proved "
            "to be the complete-chain monomial adjacent chart or its "
            "presentation stabilizer."
        ),
        "deformation_space": {
            "old_dimension": deformation_old,
            "saturated_dimension": deformation_saturated,
            "added_dimension": deformation_saturated - deformation_old,
            "one_nonzero_transported_chart": {
                "external_increment": deformation_external,
                "intersection_dimension": deformation_intersection,
                "sum_dimension": deformation_sum,
                "saturation_defect": deformation_saturated - deformation_sum,
            },
            "base_plus_opposite_charts": {
                "span_dimension": opposite_span,
                "spans_minimal_saturation": (
                    opposite_span == deformation_saturated
                ),
            },
            "components": &#91;p_report, q_report&#93;,
        },
        "equation_space": equation_report,
        "old_equation_support": support_summary(equation_support),
        "filtered_conjugacy_consequence": {
            "principal_shift": 2 * k - 1,
            "statement": (
                "Conjugation by a filtration-preserving automorphism with "
                "invertible associated graded map preserves this principal "
                "shift. For k=4 it cannot produce a layer-four tangent."
            ),
        },
    }

    expected = {
        "deformation_old": 186,
        "deformation_saturated": 294,
        "deformation_external": 97,
        "deformation_intersection": 89,
        "deformation_sum": 283,
        "equation_old": 257,
        "equation_saturated": 300,
        "equation_external": 41,
        "equation_intersection": 216,
        "equation_sum": 298,
    }
    actual = {
        "deformation_old": deformation_old,
        "deformation_saturated": deformation_saturated,
        "deformation_external": deformation_external,
        "deformation_intersection": deformation_intersection,
        "deformation_sum": deformation_sum,
        "equation_old": equation_report&#91;"old_dimension"&#93;,
        "equation_saturated": equation_report&#91;"saturated_dimension"&#93;,
        "equation_external": equation_report&#91;
            "one_nonzero_transported_chart"
        &#93;&#91;"external_increment"&#93;,
        "equation_intersection": equation_report&#91;
            "one_nonzero_transported_chart"
        &#93;&#91;"intersection_dimension"&#93;,
        "equation_sum": equation_report&#91;
            "one_nonzero_transported_chart"
        &#93;&#91;"sum_dimension"&#93;,
    }
    if k == 4 and cutoff == 15 and actual != expected:
        raise AssertionError({"expected": expected, "actual": actual})
    return report


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--cutoff", type=int, default=15)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    report = analyze(k=args.k, cutoff=args.cutoff)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_triple_overlap.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact pairwise and triple-overlap structure of the k=4 wall atlas.

Through normal layer 15, the k=4 transport has degree at most two in the wall
parameter because its layer shift is seven.  Thus

    T_lambda = I + lambda*N + lambda^2*N^2/2.

A vector in the old window and in two distinct nonzero transported windows is
therefore in the old window for every wall parameter exactly when the
external parts of both ``N`` and ``N^2`` vanish.  This module computes that
stable all-parameter core for the stored degree-21 P, Q, and equation windows.

The calculation distinguishes two ranks:

* new ambient target coordinates generated by N and N^2;
* independent source constraints imposed by requiring those external terms
  to vanish.

They need not agree because different source combinations may hit the same
external coordinate.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from degree21_k4_overlap_saturation import (
    basis_from_support,
    external_transport_matrix,
    full_support_fixture,
    horizontal_join,
    master_support,
    matrix_rank,
    saturate,
)
from wall_shear_master_covariance import generalized_binomial

BasisElement = tuple&#91;int, int&#93;
Matrix = list&#91;list&#91;Fraction&#93;&#93;


def vertical_join(top: Matrix, bottom: Matrix) -&gt; Matrix:
    if top and bottom and len(top&#91;0&#93;) != len(bottom&#91;0&#93;):
        raise ValueError("column counts do not agree")
    return &#91;*top, *bottom&#93;


def power_external_matrix(
    old_basis: Sequence&#91;BasisElement&#93;,
    saturated_basis: Sequence&#91;BasisElement&#93;,
    *,
    pole_order: int,
    k: int,
    power: int,
    cutoff: int,
) -&gt; Matrix:
    old_set = set(old_basis)
    external = &#91;item for item in saturated_basis if item not in old_set&#93;
    external_index = {item: index for index, item in enumerate(external)}
    matrix: Matrix = &#91;
        &#91;Fraction(0) for _ in range(len(old_basis))&#93;
        for _ in range(len(external))
    &#93;
    shift = 2 * k - 1
    for column, (layer, exponent) in enumerate(old_basis):
        target = (layer + power * shift, exponent - power * k)
        if target not in external_index or target&#91;0&#93; &gt; cutoff:
            continue
        coefficient = Fraction(1)
        initial = layer - pole_order + 2 * exponent
        for index in range(power):
            coefficient *= initial - index
        if coefficient:
            matrix&#91;external_index&#91;target&#93;&#93;&#91;column&#93; = coefficient
    return matrix


def full_orbit_safe_basis(
    old_basis: Sequence&#91;BasisElement&#93;,
    *,
    pole_order: int,
    k: int,
    cutoff: int,
) -&gt; list&#91;BasisElement&#93;:
    old_set = set(old_basis)
    shift = 2 * k - 1
    result: list&#91;BasisElement&#93; = &#91;&#93;
    for layer, exponent in old_basis:
        initial = layer - pole_order + 2 * exponent
        power = 1
        coefficient = Fraction(initial)
        safe = True
        while layer + power * shift &lt;= cutoff:
            if coefficient and (
                layer + power * shift,
                exponent - power * k,
            ) not in old_set:
                safe = False
                break
            power += 1
            coefficient *= initial - (power - 1)
        if safe:
            result.append((layer, exponent))
    return result


def by_layer(basis: Sequence&#91;BasisElement&#93;) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    layers: dict&#91;int, list&#91;int&#93;&#93; = {}
    for layer, exponent in basis:
        layers.setdefault(layer, &#91;&#93;).append(exponent)
    return &#91;
        {
            "layer": layer,
            "z_exponents": sorted(exponents),
            "dimension": len(exponents),
        }
        for layer, exponents in sorted(layers.items())
    &#93;


def component_report(
    name: str,
    support: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    pole_order: int,
    k: int,
    cutoff: int,
) -&gt; dict&#91;str, Any&#93;:
    old_basis = basis_from_support(support)
    saturated_basis = saturate(
        support,
        pole_order=pole_order,
        k=k,
        cutoff=cutoff,
    )
    _, pair_matrix_one = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(1),
        cutoff=cutoff,
    )
    _, pair_matrix_two = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(2),
        cutoff=cutoff,
    )
    _, pair_matrix_minus = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(-1),
        cutoff=cutoff,
    )
    first = power_external_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        power=1,
        cutoff=cutoff,
    )
    second = power_external_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        power=2,
        cutoff=cutoff,
    )
    first_constraint_rank = matrix_rank(first)
    all_constraint_rank = matrix_rank(vertical_join(first, second))
    first_target_rank = first_constraint_rank
    all_target_rank = matrix_rank(horizontal_join(first, second))
    pairwise_rank = matrix_rank(pair_matrix_one)
    if not (
        matrix_rank(pair_matrix_two)
        == matrix_rank(pair_matrix_minus)
        == pairwise_rank
    ):
        raise AssertionError("pairwise overlap rank depends on nonzero parameter")

    pairwise_dimension = len(old_basis) - pairwise_rank
    stable_core_dimension = len(old_basis) - all_constraint_rank
    safe_basis = full_orbit_safe_basis(
        old_basis,
        pole_order=pole_order,
        k=k,
        cutoff=cutoff,
    )
    if len(safe_basis) != stable_core_dimension:
        raise AssertionError(
            {
                "name": name,
                "safe_basis": len(safe_basis),
                "stable_core_dimension": stable_core_dimension,
            }
        )

    return {
        "name": name,
        "pole_order": pole_order,
        "old_dimension": len(old_basis),
        "saturated_dimension": len(saturated_basis),
        "transport_degree_in_lambda": 2,
        "pairwise_overlap_dimension": pairwise_dimension,
        "stable_all_parameter_core_dimension": stable_core_dimension,
        "pairwise_only_dimension": pairwise_dimension - stable_core_dimension,
        "first_order_external_constraint_rank": first_constraint_rank,
        "second_order_incremental_constraint_rank": (
            all_constraint_rank - first_constraint_rank
        ),
        "total_stability_constraint_rank": all_constraint_rank,
        "first_order_new_target_rank": first_target_rank,
        "second_order_incremental_target_rank": (
            all_target_rank - first_target_rank
        ),
        "total_new_target_rank": all_target_rank,
        "stable_core_is_coordinate_span": True,
        "stable_core_basis_by_layer": by_layer(safe_basis),
        "three_chart_test": (
            "Membership in charts lambda=0,1,-1 is equivalent to membership "
            "in every transported chart through the stated cutoff."
        ),
    }


def analyze(*, k: int = 4, cutoff: int = 15) -&gt; dict&#91;str, Any&#93;:
    if 3 * (2 * k - 1) &lt;= cutoff:
        raise ValueError("this report assumes transport degree at most two")
    supports = full_support_fixture()
    equation_support = master_support(
        supports&#91;"P"&#93;,
        supports&#91;"Q"&#93;,
        alpha=2,
        beta=3,
        cutoff=cutoff,
    )
    p_report = component_report(
        "P coefficients",
        supports&#91;"P"&#93;,
        pole_order=2,
        k=k,
        cutoff=cutoff,
    )
    q_report = component_report(
        "Q coefficients",
        supports&#91;"Q"&#93;,
        pole_order=3,
        k=k,
        cutoff=cutoff,
    )
    w_report = component_report(
        "equation density",
        equation_support,
        pole_order=4,
        k=k,
        cutoff=cutoff,
    )

    deformation = {
        key: p_report&#91;key&#93; + q_report&#91;key&#93;
        for key in (
            "old_dimension",
            "saturated_dimension",
            "pairwise_overlap_dimension",
            "stable_all_parameter_core_dimension",
            "pairwise_only_dimension",
            "first_order_external_constraint_rank",
            "second_order_incremental_constraint_rank",
            "total_stability_constraint_rank",
            "first_order_new_target_rank",
            "second_order_incremental_target_rank",
            "total_new_target_rank",
        )
    }
    expected = {
        "old_dimension": 186,
        "saturated_dimension": 294,
        "pairwise_overlap_dimension": 89,
        "stable_all_parameter_core_dimension": 68,
        "pairwise_only_dimension": 21,
        "first_order_external_constraint_rank": 97,
        "second_order_incremental_constraint_rank": 21,
        "total_stability_constraint_rank": 118,
        "first_order_new_target_rank": 97,
        "second_order_incremental_target_rank": 11,
        "total_new_target_rank": 108,
    }
    if k == 4 and cutoff == 15 and deformation != expected:
        raise AssertionError({"expected": expected, "actual": deformation})

    return {
        "schema_version": 1,
        "name": "degree-21 k=4 pairwise and triple wall overlap",
        "k": k,
        "normal_layer_shift": 2 * k - 1,
        "cutoff": cutoff,
        "transport_polynomial": "T_lambda=I+lambda*N+lambda^2*N^2/2",
        "components": &#91;p_report, q_report&#93;,
        "deformation_space": deformation,
        "equation_space": w_report,
        "triple_overlap_theorem": (
            "Because the external component of T_lambda v is a polynomial "
            "of degree at most two, vanishing at lambda=0,1,-1 forces it to "
            "vanish identically.  Thus the three-chart intersection is the "
            "maximal old-window subspace stable under all wall parameters."
        ),
        "cocycle": (
            "On this stable core, T_(b-c) T_(a-b)=T_(a-c) for all chart "
            "parameters a,b,c, with exact inverse T_(-lambda)."
        ),
        "interpretation": (
            "A two-chart support check leaves 21 deformation directions and "
            "10 equation directions that fail the third-chart test.  Triple "
            "overlap compatibility is therefore a genuine additional gate, "
            "not a formal consequence of one transition square."
        ),
    }


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--cutoff", type=int, default=15)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    report = analyze(k=args.k, cutoff=args.cutoff)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

[Back to Lane 9](plane-chart-correspondence-global-attachment.md)
