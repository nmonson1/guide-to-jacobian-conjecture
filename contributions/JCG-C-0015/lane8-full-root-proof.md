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

\[
K_0=\mathbf Q[u]/(m(u)),\qquad
m(u)=u^5-u^4+3u^3+3u^2+26.
\]

The replay verifies that the reduction of `m` modulo `67` is irreducible by a
Rabin test. Since `m` is monic and primitive, this is an irreducibility witness
over \(\mathbf Q\).

For the valuation

\[
\nu(x^a y^b)=-2a+b,
\]
put \(z=xy^2\). Both support roots have initial forms

\[
P_0=xp(z),\qquad Q_0=x^2yq(z),
\]
with \(\deg p=7\), \(\deg q=10\). Direct differentiation gives

\[
[P_0,Q_0]
=x^2\bigl(pq+2zpq'-3zp'q\bigr).
\]

Hence the normalized bracket condition forces

\[
pq+2zpq'-3zp'q=1. \tag{2.1}
\]

The exact relation fixture reconstructs all coefficients of `p` and `q` in
\(K_0\). The replay checks all eighteen coefficients of (2.1), not merely a
numerical embedding.

## 3. Raw support and triangular layer equation

Set

\[
t=y,\qquad z=xy^2,
\]

and write

\[
P=t^{-2}A(z,t),\qquad Q=t^{-3}B(z,t).
\]

Because \(\det \partial(z,t)/\partial(x,y)=t^2\), the equation
\([P,Q]=x^2\) becomes

\[
2AB_z-3A_zB+t(A_zB_t-A_tB_z)=z^2. \tag{3.1}
\]

Write

\[
A=\sum_{r\ge0}t^rA_r(z),\qquad
B=\sum_{r\ge0}t^rB_r(z).
\]

The coefficient of \(t^r\) in the left side is

\[
E_r=
\sum_{i+j=r}
\left((2-i)A_iB_j'+(j-3)A_i'B_j\right). \tag{3.2}
\]

The terms involving the new pair \((A_r,B_r)\) form the fixed
\(K_0\)-linear map

\[
\mathscr D_r(A_r,B_r)=
(2-r)A_rB_0'-3A_r'B_0
+2A_0B_r'+(r-3)A_0'B_r. \tag{3.3}
\]

All remaining terms depend only on lower layers. Thus each stage consists of
exact linear algebra over the fixed field \(K_0\), followed by compatibility
polynomials in previously introduced kernel parameters.

For a monomial \(x^a y^b\), its deficiencies are

\[
d_P(a,b)=b-2a+2,\qquad d_Q(a,b)=b-2a+3. \tag{3.4}
\]

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

\[
X,Y,U,V,W,D
\]

of weights

\[
1,1,2,2,2,3.
\]

The two coordinates `U,D` represent the two split origin vertices. The replay
checks that they do not occur in any compatibility equation. The effective
obstruction variables are therefore

\[
X,Y,V,W
\]

with weights \(1,1,2,2\).

There are fourteen monomials of weighted degree four:

\[
\begin{gathered}
X^4,X^3Y,X^2Y^2,XY^3,Y^4,\\
X^2V,XYV,Y^2V,X^2W,XYW,Y^2W,V^2,VW,W^2.
\end{gathered}
\]

Adjoin to the eighteen layer-four equations the seven layer-three equations
multiplied by `X` and by `Y`. The resulting `32 x 14` Macaulay matrix has rank
`14` over \(K_0\). Its independently reconstructed selected-minor digest is

```text
8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059
```

Thus the obstruction ideal contains every weighted-degree-four monomial. In
particular

\[
X^4,Y^4,V^2,W^2\in I,
\]

so

\[
X,Y,V,W\in\sqrt I. \tag{4.1}
\]

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

\[
(t_{1,0},t_{1,1},U,t_{2,1},t_{2,2},D,t_{3,1},t_{3,2},t_{4,0})
\]

of weights

\[
(1,1,2,2,2,3,3,3,4). \tag{5.1}
\]

Again `U,D` are the split origin-vertex parameters and do not occur in any
compatibility equation.

The two nonzero layer-four compatibility polynomials are scalar multiples of
one polynomial. After unit normalization, that polynomial is

\[
L^2,
\qquad
L=t_{2,2}-\alpha t_{1,1}^2, \tag{5.2}
\]

for an explicitly reconstructed nonzero \(\alpha\in K_0\).

### Scheme versus reduced support

The scheme cut out at layer four contains the double hyperplane

\[
\operatorname{Spec}K_0[\mathbf t]/(L^2).
\]

It is not replaced scheme-theoretically by \((L)\). For the theorem sought
here, however, the target statement is geometric emptiness, and

\[
V(L^2)=V(L)
\]

as sets over an algebraic closure. The queue therefore stores two separate
nodes:

1. the nonreduced square scheme, carrying the multiplicity information; and
2. its reduced support, used only for point-set routing.

No claim about equality of schemes is made.

## 6. Exact-support complements and normalization

On the reduced support \(L=0\), the required top-vertex coefficients become

\[
[P]_{(8,16)}=c_Pt_{1,1}^2,
\qquad
[Q]_{(12,24)}=c_Qt_{1,1}^3, \tag{6.1}
\]

where the replay verifies \(c_P,c_Q\in K_0^\times\).

Therefore the exhaustive split

\[
V(L)=V(L,t_{1,1})\ \cup\ \bigl(V(L)\cap D(t_{1,1})\bigr) \tag{6.2}
\]

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

\[
\begin{aligned}
U_*&=U/t_{1,1}^2,& D_*&=D/t_{1,1}^3,\\
x&=t_{1,0}/t_{1,1},& a&=t_{2,1}/t_{1,1}^2,\\
b&=t_{3,1}/t_{1,1}^3,& c&=t_{3,2}/t_{1,1}^3,\\
d&=t_{4,0}/t_{1,1}^4.
\end{aligned} \tag{6.3}
\]

The inverse formulas are

\[
\begin{aligned}
U&=t_{1,1}^2U_*,&D&=t_{1,1}^3D_*,\\
t_{1,0}&=t_{1,1}x,&t_{2,1}&=t_{1,1}^2a,\\
t_{2,2}&=\alpha t_{1,1}^2,&t_{3,1}&=t_{1,1}^3b,\\
t_{3,2}&=t_{1,1}^3c,&t_{4,0}&=t_{1,1}^4d.
\end{aligned} \tag{6.4}
\]

The replay verifies that every compatibility polynomial is weighted
homogeneous of its layer number with respect to (5.1). Substitution of (6.4)
therefore factors a nonzero power of `t1_1` from each equation. Consequently,
on the open child, the **layer-through-eight necessary-condition locus** is
isomorphic to

\[
(\mathbf G_m)^3_{U_*,D_*,t_{1,1}}
\times V(F_0,\ldots,F_{14})\subset
(\mathbf G_m)^3\times\mathbf A^5_{x,a,b,c,d}. \tag{6.5}
\]

Every exact full-support solution maps to (6.5); equation (6.5) is not a
parameterization of the forgotten higher-deficiency coefficients. The
weight-one coordinate `t1_1` also makes the corresponding scaling action free;
no finite stabilizer or quotient-descent issue is hidden in the early-layer
cross-section.

## 7. Reconstruction of the fifteen equations

Continuing (3.2) through layer eight, substituting (6.3), and removing only
nonzero scalar duplicates gives

\[
1,3,5,6
\]

distinct equations of weights

\[
5,6,7,8,
\]

respectively. In the replay order these are

\[
F_0,F_1,\ldots,F_{14}\in K_0[x,a,b,c,d].
\]

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

\[
I_{15}=(F_0,\ldots,F_{14})
\]

and

\[
J_6=(F_4,F_6,F_8,F_9,F_{10},F_{11}). \tag{8.1}
\]

The current Program 6 residue-provenance proposition identifies exactly these
zero-based indices. The independent replay selects the same six equations
from its reconstructed ordered list and obtains canonical digest

```text
e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a
```

Because the generators of `J6` are literally among the generators of `I15`,

\[
J_6\subset I_{15}
\quad\Longrightarrow\quad
V(I_{15})\subset V(J_6). \tag{8.2}
\]

The imported compact toric terminal theorem states

\[
V(J_6)(\overline{K_0})=\varnothing. \tag{8.3}
\]

Its recorded proof uses the good fiber `(p,u)=(2053,216)`, mixed volume `296`,
`344` proper toric faces (`270` monomial and `74` saturated-unit faces), and
invertibility of multiplication by `F4`, with determinant `682` modulo `2053`.
The five split-embedding determinant residues are

\[
682,116,337,242,740,
\]

with norm product `51` modulo `2053`.

Combining (8.2) and (8.3) gives

\[
V(I_{15})(\overline{K_0})=\varnothing.
\]

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

\[
Y'=Y+\lambda X^{-k}
\]

in lower-face coordinates \(t=Y\), \(z=XY^2\), one has \(X=z/t^2\), hence

\[
Y'=t+\lambda(t^2/z)^k=t(1+h),
\qquad
h=\lambda t^{2k-1}z^{-k}, \tag{9.1}
\]

and

\[
z'=X(Y')^2=z(1+h)^2. \tag{9.2}
\]

For `k=4`, the first nonzero normal term has order

\[
2k-1=7. \tag{9.3}
\]

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

\[
\max(\deg P,\deg Q)<125.
\]

Polynomial invertibility descends along the faithfully flat extension from a
characteristic-zero base field to its algebraic closure: an isomorphism of the
base-changed affine coordinate algebras, together with its unique inverse, is
fpqc descent data. Thus it is sufficient to exclude the normalized loci over
algebraic closures.

This corollary is a proof assembly with explicit imports. It is not a new
priority claim for the `125` bound, an independent reconstruction of the
literature reduction, or a substitute for specialist review of the imported
toric theorem.
