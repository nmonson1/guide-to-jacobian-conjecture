# Continuation of the explicit cubic-homogeneous and Drużkowski attacks

## Status

This continuation starts from the exact 19-dimensional cubic-homogeneous map
\(G=I+H\) and the 11-dimensional degree-three representative in the preceding
bundles.

The main new conclusions are:

\[
\boxed{\operatorname{wrank}(H)\ge 52}
\]

for ordinary simultaneous vector-Waring rank, and consequently

\[
\boxed{52\le N_{\mathrm{pair}}\le 110}
\]

for the full-rank square-zero pairing problem attached to this fixed
19-dimensional tensor.

The rank-six cubic jet is now accompanied by a 13-term exact obstruction
functional, and the first nontrivial three-row sparse square-zero search class
is excluded exactly for the fixed coordinate collision.

| Direction | Previous state | New state |
|---:|---:|---:|
| Fixed-tensor Waring lower bound | \(40\) | \(\boxed{52}\) |
| Fixed-tensor square-zero pairing interval | \(40\le N\le110\) | \(\boxed{52\le N\le110}\) |
| Rank-six jet obstruction | rank \(3144/3145\) computation | 13-term functional \(\Lambda_4\) |
| Scalar monomial quadratic shifts | one example known | all \(605\) checked; unique |
| Three-row sparse \(N=5\) class | finite-field sampling | exact graph-orbit exclusion |
| Independent verification | SymPy | custom `Fraction` verifier added |

These are exact, model-relative statements.  They do not prove a global
minimum for cubic-homogeneous or Drużkowski counterexamples.

---

# 1. A 52-cube lower bound

Let \(V=\mathbb Q^{19}\), and define

\[
W=\operatorname{span}\left\{
\frac{\partial H_i}{\partial Z_j}:1\le i,j\le19
\right\}
\subseteq\operatorname{Sym}^2(V^*).
\]

Exact row reduction gives

\[
\boxed{\dim W=39.}
\]

Suppose

\[
H(Z)=\sum_{\nu=1}^R b_\nu\,\ell_\nu(Z)^3.
\]

Put

\[
U=\operatorname{span}\{\ell_\nu^2\}\subseteq\operatorname{Sym}^2(V^*).
\]

Differentiation gives \(W\subseteq U\).

## 1.1 A 12-dimensional zero block

In the coordinate order

\[
Z=(x,y,z,a,b,c,d,q,s,h,k,w_1,\ldots,w_7,t),
\]

let

\[
A=\langle z,c,q,s,k,w_1,\ldots,w_7\rangle.
\]

Then

\[
\dim A=12
\]

and every quadratic in \(W\) restricts to zero on \(A\):

\[
\boxed{W|_A=0.}
\]

Equivalently, all 78 \(A\)-\(A\) coefficient columns of the derivative
matrix vanish identically.

## 1.2 The Waring forms span all of \(V^*\)

If \(v\in V\) is annihilated by every \(\ell_\nu\), then

\[
JH(Z)v
=
3\sum_\nu b_\nu\,\ell_\nu(Z)^2\ell_\nu(v)
=0.
\]

For the explicit \(H\), the coefficient matrix of the system

\[
JH(Z)v=0
\]

has size \(125\times19\), rank 19, and an explicit \(19\times19\) minor of
determinant

\[
18.
\]

Therefore

\[
\boxed{\bigcap_\nu\ker\ell_\nu=0}
\]

and the \(\ell_\nu\) span \(V^*\).

Their restrictions to \(A\) consequently span \(A^*\).  Twelve independent
linear forms have twelve independent squares, so the image of

\[
U\longrightarrow\operatorname{Sym}^2(A^*)
\]

has dimension at least 12.  Since this restriction kills \(W\),

\[
\dim(U/W)\ge12.
\]

Thus

\[
\dim U\ge39+12=51.
\]

This already gives \(R\ge51\).

## 1.3 Equality \(51\) is impossible

Assume for contradiction that \(R\le51\).  The preceding inequalities force

\[
R=\dim U=51
\]

and the restriction image has dimension exactly 12.

Choose a basis

\[
\alpha_1,\ldots,\alpha_{12}
\]

of \(A^*\) among the restricted forms \(\ell_\nu|_A\).  Their squares are a
basis of the 12-dimensional restriction image.  If

\[
\alpha=\sum_jc_j\alpha_j
\]

and \(\alpha^2\) lies in the span of the \(\alpha_j^2\), every cross
coefficient \(c_ic_j\) vanishes.  Hence \(\alpha\) is proportional to one of
the \(\alpha_j\).

Therefore all restricted Waring forms lie on twelve lines.  Grouping the
squares by these lines shows that the mixed projection

\[
\mathcal C=
\operatorname{pr}_{B^*\otimes A^*}(W),
\qquad
V=B\oplus A,\quad \dim B=7,
\]

is invariant under the twelve coordinate projectors in the
\(\alpha_j\)-basis.

Define its right stabilizer algebra

\[
\mathcal E=
\left\{
T\in\operatorname{End}(A^*):
(I_{B^*}\otimes T)\mathcal C\subseteq\mathcal C
\right\}.
\]

Under equality, \(\mathcal E\) would contain a conjugate of the full diagonal
algebra \(\mathbb Q^{12}\).  Its commutant would then be contained in that
diagonal algebra and could contain no nonzero nilpotent.

The exact tensor gives instead

\[
\dim\mathcal C=24,
\qquad
\dim\mathcal E=62,
\qquad
\dim\mathcal E'=7,
\]

and the matrix

\[
N=E_{5,0}\in\operatorname{End}(A^*)
\]

satisfies

\[
N\ne0,\qquad N^2=0,\qquad NT=TN
\quad\text{for every }T\in\mathcal E.
\]

This contradiction rules out equality.

Hence

\[
\boxed{\operatorname{wrank}(H)\ge52.}
\]

## 1.4 Maximality of the 12-dimensional zero block

The following member of \(W\),

\[
q_*=
-\frac13\left(
3ac-3bt+3bz+3ds-3dy+3hk-3hx+3qy
-12tw_1-130tw_3+3tw_4-62tw_6-42tw_7+3x^2
\right),
\]

has symmetric matrix rank 13.  A specified \(13\times13\) principal minor
has determinant

\[
-\frac1{256}.
\]

Over an algebraic closure, a rank-13 quadratic form on a 19-dimensional
space has maximal totally isotropic dimension

\[
(19-13)+\left\lfloor\frac{13}{2}\right\rfloor=12.
\]

Thus the displayed \(A\) is maximal for the common-isotropic-subspace
method.  The improvement \(51\to52\) comes from the equality geometry, not
from finding a larger zero block.

## 1.5 Pairing consequence

Every full-rank square-zero Gorni--Zampieri representation

\[
H(Z)=B(DZ)^{*3},
\qquad
BD=0,
\]

is in particular a vector-Waring decomposition with one cube per row of
\(D\).  The existing exact 110-form construction therefore satisfies the
updated interval

\[
\boxed{52\le N_{\mathrm{pair}}\le110.}
\]

This is a lower bound for pairings of this fixed \(19\)-dimensional tensor,
not for arbitrary direct Drużkowski counterexamples.

Verifier: `attack7_waring52.py`.

---

# 2. The rank-six jet and its compact quartic obstruction

Write the normalized 11-dimensional map as

\[
K=I+Q+C.
\]

The quadratic triangular conjugacy

\[
P_2=-d^2e_a
\]

lowers the cubic-coordinate span from seven to six.  The exact conjugate has
quartic part

\[
\begin{aligned}
(D_4)_z&=d^3z+3d^2y^2,\\
(D_4)_a&=x^2y^2,\\
(D_4)_c&=-2d^3z-6d^2y^2.
\end{aligned}
\]

For a cubic vector field \(P_3\), the next homological correction is

\[
\delta_Q(P_3)=[Q,P_3]=JQ\,P_3-JP_3\,Q.
\]

## 2.1 A 13-term functional

For a quartic vector field \(R\), define

\[
\begin{aligned}
\Lambda_4(R)=&
[x^2y^2]R_a
+4[x^2ac]R_a
-\frac{20}{3}[x^2as]R_a
+9[x^2qk]R_a\\
&+3[xchk]R_a
-\frac12[xd^2q]R_a
-7[xshk]R_a
+\frac43[y^2ah]R_a\\
&-\frac12[ybch]R_a
-[ydhk]R_a
+\frac83[za^2h]R_a
+25[aqhk]R_a\\
&-2[dqhk]R_d.
\end{aligned}
\]

Exact coefficient extraction over all

\[
11\binom{13}{3}=3146
\]

cubic monomial vector fields gives

\[
\boxed{\Lambda_4([Q,P_3])=0\quad\text{for every }P_3,}
\]

while

\[
\boxed{\Lambda_4(D_4)=1.}
\]

Therefore

\[
\boxed{D_4\notin\operatorname{im}\delta_Q.}
\]

The restricted homological matrix has size \(13\times3146\), rank 12, and
the augmented matrix has rank 13.  Deleting any one of its thirteen rows
leaves rank 12.  Thus the support is a minimal circuit.

This is a compact, auditable replacement for the earlier full
\(3144/3145\) rank comparison.

Verifier: `attack8_quartic_functional.py`.

## 2.2 Exhaustion of scalar monomial triangular shifts

Consider

\[
P_2=\lambda m e_r,
\]

where \(m\) is a quadratic monomial not involving \(X_r\).  There are

\[
11\binom{11}{2}=605
\]

such triangular monomial directions.

A fixed \(7\times7\) cubic-coordinate minor has determinant \(-36\) at
\(\lambda=0\).  For 583 directions its exceptional polynomial is constant.
The remaining 22 directions yield 27 rational exceptional roots.  Full
exact rank at every root gives only one rank-six case:

\[
\boxed{P_2=-d^2e_a.}
\]

Thus the successful jet shift is unique in this entire scalar monomial
triangular class, and it is precisely the shift detected by the nonzero
quartic obstruction above.

Verifier: `attack9_monomial_shifts.py`.

## 2.3 Independent target cleanup in the natural low-degree model

After the conjugacy, the exact output coordinates \(d,q,h,k\) have degree at
most two.  Quadratic target corrections built from these four outputs form a
ten-dimensional space and cannot create terms above degree four.

Their quartic images are linearly independent.  Exact calculation shows:

* \((D_4)_z\) is outside this quartic image;
* \((D_4)_c=-2(D_4)_z\) is outside it;
* \((D_4)_a=x^2y^2\) has the unique preimage \(-Y_d^2\).

Applying that unique correction removes the \(a\)-quartic but raises the
cubic-coordinate span back from six to seven.

Hence the rank-six jet cannot be promoted by this entire natural class of
independent quadratic target automorphisms.

Verifier: `attack11_target_cleanup.py`.

What remains open is substantially broader:

* non-monomial quadratic source conjugacies;
* independent source and target transformations outside the low-degree
  triangular model;
* one or more stable contractible pairs;
* changing the degree-three representative before applying the shift.

---

# 3. Exact exclusion of the first three-row sparse \(N=5\) class

Consider the square-zero two-matrix family

\[
H_{C,Q}(z)=C\left((Qz)^{*3}-Qz^{*3}\right).
\]

After normalizing a signed-permutation baseline, take

\[
Q=I+R,
\]

where \(R\) has exactly three active rows and one nonzero off-diagonal entry
in each active row.  This section imposes the coordinate collision

\[
F(e_0)=F(e_1).
\]

The result is model-relative because a general linear normalization of an
arbitrary collision need not preserve coordinatewise cubes or the sparse
shape of \(Q\).

## 3.1 Trace-one support lemma

For one edge \(i\to j\) with coefficient \(r\),

\[
U=(z_i+r z_j)^3-z_i^3-rz_j^3.
\]

If the corresponding column of the compressed coefficient matrix is \(b\),
its contribution to the trace is

\[
\frac{\partial U}{\partial z_i}b_i+
\frac{\partial U}{\partial z_j}b_j.
\]

The coefficients of \(z_i^2\) and \(z_iz_j\) are

\[
3rb_j,
\qquad
6rb_i+6r^2b_j.
\]

For \(r\ne0\), trace-one therefore forces

\[
\boxed{b_i=b_j=0.}
\]

## 3.2 Graph classification

If the three support edges use at most four vertices, the map is a
triangular extension of a cubic-homogeneous core in dimension at most four.

Suppose all five vertices occur.  There are 180 support patterns with three
distinct source rows.  The collision and trace-one lemma force:

* one edge \(u\to0\), \(u\in\{2,3,4\}\);
* one edge \(v\to1\), \(v\in\{2,3,4\}\);
* \(u\ne v\).

Exactly 30 patterns remain.  Under swapping \(0,1\) and permuting
\(2,3,4\), they form three orbits:

\[
\begin{array}{c|c}
A&(0\to2,\ 3\to0,\ 4\to1),\\
B&(2\to0,\ 3\to0,\ 4\to1),\\
C&(2\to0,\ 3\to1,\ 4\to2).
\end{array}
\]

## 3.3 Trace-square contradictions

Write the three edge coefficients as \(\alpha,\beta,\gamma\).

### Orbit A

The collision forces

\[
\beta^2\ne1,\qquad\gamma^2\ne1.
\]

After solving trace-one and collision, the coefficient of
\(z_1^2z_3^2\) in \(\operatorname{tr}(JH/3)^2\) is

\[
\boxed{\frac{18}{\beta^2-1}},
\]

which cannot vanish.

### Orbit C

The collision forces

\[
\alpha^2\ne1,\qquad\beta^2\ne1.
\]

The coefficient of \(z_0^2z_1^2\) is identically

\[
\boxed{18}.
\]

### Orbit B

The collision forces \(\gamma^2\ne1\) and excludes the case in which both
\(\alpha^2=\beta^2=1\).

If \(\alpha^2\ne1\) and \(\beta^2\ne1\), two trace-square coefficients force,
for the entry \(B_{1,1}\),

\[
B_{1,1}=0
\]

and simultaneously

\[
(\beta^3-\beta)B_{1,1}=1.
\]

If \(\alpha=\pm1\), the coefficient of \(z_0z_1^2z_3\) is

\[
\frac{36\beta}{\beta^2-1}\ne0.
\]

If \(\beta=\pm1\), the coefficient of \(z_0z_1^2z_2\) is

\[
\frac{36\alpha}{\alpha^2-1}\ne0.
\]

Thus every generic and exceptional branch is excluded.

Consequently:

\[
\boxed{
\text{No cover-all-five, three-row, one-edge-per-row member of this
coordinate-collision ansatz is Keller.}
}
\]

Combining this with the known invertibility of cubic-homogeneous Keller maps
in dimensions at most four excludes the corresponding smaller-support
cores as counterexamples.

Verifier: `attack10_three_row_exact.py`.

## 3.4 Corrected finite-field check

The earlier structured \(\mathbb F_5\) experiment used edge coefficients
\(\pm1\).  That was vacuous for the chosen coordinate collision because

\[
r^3-r=0\qquad(r=0,\pm1)
\]

and hence those edges contributed nothing to the collision vector.  The
earlier “no affine \(C\)-space” count should not be treated as evidence.

The corrected exhaustive search runs every nonzero coefficient

\[
r\in\mathbb F_5^*=\{1,2,3,4\}
\]

on the 30 graph patterns that survive the linear constraints.  It produces:

\[
528
\]

affine records, each of dimension four, hence

\[
528\cdot5^4=330000
\]

compressed coefficient matrices.  Testing nilpotence at all

\[
5^5-1=3124
\]

nonzero points gives:

\[
\boxed{0\text{ survivors}.}
\]

This finite-field computation is now consistent with, but weaker than, the
characteristic-zero graph-orbit proof.

Files:
`generate_three_row_f5.py`, `exhaust_three_row_f5.cpp`,
`three_row_records_f5.bin`.

---

# 4. Corrections to the preceding report

Two points from the preceding exploratory stage required correction.

## 4.1 The proposed \(N=40\) “almost diagonal invariance”

The prior report derived an extra condition
\(B\operatorname{diag}(c)D=0\) for a hypothetical 40-form equality case and
suggested it might constrain \(\operatorname{im}D\).  In the equality setup,
the resulting diagonal is proportional to the identity, so this condition
does not add information beyond \(BD=0\).

That proposed follow-up obstruction is withdrawn.

The valid lower bound \(40\) from the Veronese intersection remains correct,
but it is now superseded by the independent \(52\)-cube argument above.

## 4.2 The old \(\{\pm1\}\) structured finite-field search

As explained in §3.4, it was vacuous for the normalized coordinate collision.
It has been replaced by the all-nonzero exhaustive search and by an exact
characteristic-zero argument.

---

# 5. Verification

The following final scripts all run successfully:

| Script | Main checks |
|---:|---|
| `attack7_waring52.py` | \(W\), zero block, constant kernel, stabilizer, commutant |
| `attack8_quartic_functional.py` | all 3146 homological basis vectors; 13-row circuit |
| `attack9_monomial_shifts.py` | all 605 scalar monomial triangular shifts |
| `attack10_three_row_exact.py` | graph classification and all coefficient branches |
| `attack11_target_cleanup.py` | all ten natural low-output quadratic target corrections |
| `verify_small_certificates.py` | independent `Fraction`-only matrix verification |
| `generate_three_row_f5.py` + C++ | corrected 330000-candidate exhaustive search |

The custom verifier does not import SymPy.  It checks serialized sparse
rational matrices for:

* derivative-space rank and a determinant-648 minor;
* the 12-dimensional zero block;
* constant-kernel rank and determinant-18 minor;
* the rank-13 quadratic and determinant \(-1/256\);
* the 13-row quartic circuit;
* the 62-dimensional stabilizer and its commuting square-zero element.

---

# 6. Updated open problems

The next mathematically sharp problems are:

1. **Rule out equality \(52\).**
   For \(R=52\), the restriction image has dimension 12 or 13.  This is a
   small Veronese-completion problem with one additional quadratic direction.

2. **Solve the full quadratic rank-six incidence problem.**
   Find all \(P_2\) with
   \[
   \operatorname{rank}\operatorname{span}(C+[Q,P_2])\le6
   \]
   and then impose the linear obstruction
   \[
   \Lambda_4(D_4(P_2))=0.
   \]

3. **Add one contractible stable pair to the homological complex.**
   Determine whether the quartic cokernel class dies after one stabilization.

4. **Move to the next sparse \(N=5\) graph class.**
   The first surviving possibilities have either four active rows or at
   least two off-diagonal entries in one of the three active rows.

5. **Improve the 110-form upper bound.**
   The new interval
   \[
   52\le N_{\mathrm{pair}}\le110
   \]
   is still broad; the \(t\)-graded tensor structure remains the most
   plausible source of a smaller decomposition.
