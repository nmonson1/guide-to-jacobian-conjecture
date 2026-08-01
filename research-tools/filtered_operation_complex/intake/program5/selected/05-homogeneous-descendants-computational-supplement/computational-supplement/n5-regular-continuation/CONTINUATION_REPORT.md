# First-normal obstruction in the five-dimensional regular Jordan stratum

## Scope and status

Let

\[
F(x)=x+H(x),\qquad H\colon k^5\to k^5
\]

be cubic homogeneous, with nilpotent Jacobian \(JH\).  This note continues the
analysis of a putative collision

\[
F(v+u)=F(v)
\]

whose collision line carries the everywhere-regular nilpotent Jordan type
\((5)\).

The previous line-level calculation produced a smooth \(11\)-adic family of
regular nilpotent quadratic pencils satisfying the line integrability and
collision equations.  The new result is that the displayed family **cannot
extend even to first normal order for the Jacobian—equivalently, through
normal degree two for the cubic tensor**.
The obstruction is already the fifth linearized characteristic identity.

This is not yet a characteristic-zero exclusion of the entire regular
Jordan stratum.  It eliminates:

* the complete \(\mathbf Z_{11}\)-residue disk through the explicit smooth
  point;
* every \(\mathbf F_7\)-rational and every \(\mathbf F_{11}\)-rational point
  in the full-kernel/osculating chart;
* the corresponding good-reduction local branches.

Algebraic points over finite extensions, bad-reduction points, and the
kernel-span strata of dimensions three and four remain open.

---

## 1. Collision-line data

Put \(P=\langle u,v\rangle\).  On this plane write

\[
M(s,t)=JH(su+tv)=s^2A+stB+t^2C.
\]

If \(H(x)=T(x,x,x)\), with \(T\) symmetric in its three inputs, then

\[
A=3T(-,u,u),\qquad B=6T(-,u,v),\qquad C=3T(-,v,v).
\]

Tensor symmetry and the collision give

\[
Bu=2Av,\qquad Bv=2Cu,
\]

and

\[
u+\frac13Au+Av+Cu=0.
\]

The previous computation found an eight-parameter full-kernel chart for
quadratic pencils that are regular nilpotent on all of \(\mathbf P^1\), and
an explicit smooth point over \(\mathbf F_{11}\):

\[
a=(8,7,1,7,2,9,0,1),
\]

\[
u=(7,6,3,10,4),\qquad v=(8,9,7,9,1).
\]

Its line equations have a nonsingular \(15\times15\) Jacobian minor, and it
lifts to a one-dimensional \(\mathbf Z_{11}\)-family.  The issue addressed
here is whether those line data can be the restriction of a globally
nilpotent polynomial Jacobian.

---

## 2. First-normal extension equations

Choose coordinates after a linear conjugation so that

\[
u=e_0,\qquad v=e_1.
\]

Let \(n_0,n_1,n_2\) be a basis of a complementary three-space.  For each
normal direction define

\[
N_r(s,t)=\left.\frac{d}{d\epsilon}
JH(su+tv+\epsilon n_r)\right|_{\epsilon=0}.
\]

Since \(H\) is cubic, \(N_r\) is a matrix pencil linear in \((s,t)\):

\[
N_r(s,t)=sP_r+tQ_r.
\]

Symmetry of the cubic tensor fixes the first two columns:

\[
P_r u=2A n_r,\qquad P_r v=B n_r,
\]

\[
Q_r u=B n_r,\qquad Q_r v=2C n_r.
\]

The remaining normal columns are described by the coefficients

\[
T_i(p,n_r,n_q),
\qquad
0\le i\le4,
\quad p\in\{u,v\},
\quad 0\le r\le q\le2.
\]

There are exactly

\[
5\cdot2\cdot\binom{4}{2}=60
\]

such unknowns.

Global nilpotence of \(JH\) implies, for every normal direction and
\(k=1,\ldots,5\),

\[
\boxed{\operatorname{tr}\bigl(M(s,t)^{k-1}N_r(s,t)\bigr)=0.}
\]

In characteristic zero this is the derivative of
\(\operatorname{tr}(JH^k)=0\), divided by \(k\).  The same formulation is
valid in characteristic \(p>5\).

The polynomial in this box has degree \(2k-1\), hence \(2k\) homogeneous
coefficients.  Thus one obtains per normal direction

\[
2+4+6+8+10=30
\]

linear equations, and 90 equations in total.

---

## 3. Exact obstruction at the smooth \(\mathbf F_{11}\) point

After the collision-adapted change of basis, the line matrices are

\[
A=\begin{pmatrix}
6&4&0&10&2\\
6&1&0&9&10\\
8&0&0&6&2\\
3&8&0&5&2\\
3&6&0&1&10
\end{pmatrix},
\]

\[
B=\begin{pmatrix}
8&8&1&4&7\\
2&5&2&6&9\\
0&2&5&4&4\\
5&4&6&9&7\\
1&8&10&3&6
\end{pmatrix},
\]

\[
C=\begin{pmatrix}
4&0&5&1&3\\
8&1&6&6&6\\
1&8&5&6&10\\
2&6&0&0&2\\
4&7&9&1&1
\end{pmatrix}
\quad\text{over }\mathbf F_{11}.
\]

### 3.1 First four identities

The identities for \(k=1,2,3,4\) give exactly 60 equations in the 60
first-normal tensor coefficients.  Their coefficient matrix has

\[
\boxed{\det=3\pmod{11}.}
\]

They therefore determine the entire first-normal jet uniquely.

### 3.2 Fifth identity

After substituting that unique solution, the fifth identity leaves three
binary forms of degree nine, one for each normal direction.  Their coefficient
rows are

\[
\begin{pmatrix}
5&8&9&1&9&2&2&1&3&1\\
2&2&6&2&4&6&1&7&2&5\\
9&5&9&8&5&3&4&6&3&8
\end{pmatrix}.
\]

This matrix has rank three; its first three columns have determinant

\[
\boxed{2\pmod{11}}.
\]

Equivalently, among the full 90 equations there is an augmented
\(61\times61\) minor with determinant

\[
\boxed{1\pmod{11}}.
\]

Hence the first-normal system is inconsistent:

\[
\boxed{\operatorname{rank}(L)=60,
\qquad
\operatorname{rank}([L\mid b])=61.}
\]

No symmetric cubic tensor extending these line data can have nilpotent
Jacobian even to first order transverse to the line.

### 3.3 Consequence for the Hensel family

Both displayed determinants are units in \(\mathbf Z_{11}\).  They remain
units under every \(11\)-adic deformation with the same reduction.  Therefore
**the entire smooth \(\mathbf Z_{11}\)-residue disk through the previously
constructed line point is excluded**, not merely the central residue point.

This corrects the interpretation of the previous line-level result: that
Hensel family is a genuine family of collision-line solutions, but none of
its members can be a global Keller tensor.

---

## 4. Coordinate-free 175-variable verification

A vector-valued symmetric cubic tensor in dimension five has

\[
5\binom{7}{3}=175
\]

coefficients.

The restrictions

\[
3T(-,u,u)=A,
\qquad
6T(-,u,v)=B,
\qquad
3T(-,v,v)=C
\]

give 75 displayed equations but rank only 65, exactly because the line
integrability identities account for ten dependencies.

Add all first-normal characteristic equations in the five ambient basis
directions.  Exact arithmetic gives:

\[
\begin{array}{c|c|c}
\text{system}&\text{coefficient rank}&\text{augmented rank}\\ \hline
\text{line restrictions}&65&65\\
\text{restrictions plus }k\le4&125&125\\
\text{restrictions plus }k\le5&125&126.
\end{array}
\]

The nullity after \(k\le4\) is

\[
175-125=50,
\]

which is precisely the number of pure-normal coefficients

\[
5\binom{5}{3}=50.
\]

Thus the first four identities determine every tensor coefficient visible through first normal order of the Jacobian; only the pure-normal cubic
part remains free.  The fifth-identity contradiction is independent of those
50 coefficients.

This establishes the invariant statement

\[
\boxed{
\text{the displayed line data do not extend to a nilpotent Jacobian}
\text{ to first normal order (equivalently, no compatible cubic tensor mod }I_P^3\text{).}
}
\]

---

## 5. Exhaustive rational-point checks in the full-kernel chart

The eight-parameter chart was exhaustively enumerated projectively over two
characteristics greater than five.  For every parameter point with invertible
chart matrix, the 15 line equations were solved; only line kernels containing
an independent collision pair were retained.  The regularity test was then
applied, followed by the exact 90-equation first-normal rank test.

### Over \(\mathbf F_7\)

\[
\begin{array}{c|r}
\text{projective parameter points}&960800\\
\det T\ne0&806344\\
\text{points with collision-line solution}&6\\
\text{geometrically regular}&6\\
\text{first-normal extensions}&0.
\end{array}
\]

### Over \(\mathbf F_{11}\)

\[
\begin{array}{c|r}
\text{projective parameter points}&21435888\\
\det T\ne0&19324668\\
\text{points with collision-line solution}&11\\
\text{geometrically regular}&11\\
\text{first-normal extensions}&0.
\end{array}
\]

For each of the 17 surviving line points:

* the 15-by-10 line system has rank nine, so the collision pair is unique
  projectively;
* the gcd of all affine \(4\times4\) minors of \(M(1,t)\) is one;
* the matrix \(C=M(0,1)\) has rank four;
* the first-normal coefficient and augmented ranks are \((60,61)\).

Thus every listed pencil has Jordan type \((5)\) at every geometric point of
\(\mathbf P^1\), not just at rational points.

### Characteristic five is deliberately excluded

For \(k=5\), differentiation gives a factor of five.  In characteristic five,
\(\operatorname{tr}(M^4N)=0\) is not equivalent to the derivative of the fifth
characteristic identity.  Accordingly, no \(\mathbf F_5\) enumeration is used
as evidence in this note.

### What the finite-field checks prove and do not prove

They rigorously exclude all rational points of the displayed full-kernel chart
over \(\mathbf F_7\) and \(\mathbf F_{11}\), and all characteristic-zero local
branches with good reduction to those points.

They do **not** exclude:

* points defined only over finite extensions of \(\mathbf F_7\) or
  \(\mathbf F_{11}\);
* characteristic-zero points with bad reduction at both primes;
* boundary points with singular chart matrix;
* the kernel-span-three and kernel-span-four strata.

Therefore this is strong arithmetic evidence for a universal obstruction in
the full-kernel stratum, but not yet a characteristic-zero classification
theorem.

---

## 6. Geometric interpretation of the obstruction

At a regular nilpotent matrix, the nilpotent cone is cut transversely by the
five characteristic invariants.  Along the collision line, a first-normal
matrix pencil must lie in the tangent space to that cone at every point.

For the explicit line data, the first four linearized invariants determine the
normal tensor jet.  The fifth invariant—equivalently the linearized
determinant—then produces a nonzero covariant

\[
\Omega\in N_P^*\otimes H^0(\mathbf P^1,\mathcal O(9)).
\]

At the displayed point, \(\Omega\) has rank three as a map from the
three-dimensional normal space.  Across every enumerated \(\mathbf F_7\)- and
\(\mathbf F_{11}\)-rational point, the corresponding affine system is likewise
inconsistent.

The natural next theorem is:

> **Proposed full-kernel obstruction.**  On the regular collision-line
> solution curve in the full-kernel chart, the covariant \(\Omega\) is nowhere
> zero.

A proof would eliminate the entire full-kernel regular Jordan stratum in
characteristic zero.  It should be sought by describing the line-solution
curve and \(\Omega\) invariantly, rather than by expanding the 175-variable
global Keller system.

---

## 7. Current status of the five-dimensional problem

The previous result showed that regular collision-line solutions exist.  The
new result sharply localizes their failure:

\[
\boxed{
\begin{aligned}
&\text{regular collision-line data exist smoothly in characteristic zero;}\\
&\text{the explicit smooth component fails at first normal order;}\\
&\text{all rational full-kernel chart points over }\mathbf F_7,\mathbf F_{11}
  \text{ fail similarly.}
\end{aligned}}
\]

This does not yet prove that no five-dimensional cubic-homogeneous
counterexample exists.  The unresolved cases are:

1. algebraic points of the full-kernel chart not detected over the two base
   fields;
2. the kernel-span-four stratum;
3. the balanced kernel-span-three stratum;
4. the other generic Jordan types \((4,1)\) and \((3,2)\).

The most promising next step is an exact description of the full-kernel line
curve and the zero scheme of \(\Omega\).  If \(\Omega\) is nowhere zero, the
regular type-\((5)\) analysis should then move to the kernel-span-four and
kernel-span-three boundary strata.

---

## 8. Verification files

* `verify_first_normal_transformed.py` — 60-by-60 determinant, 61-by-61
  augmented determinant, and degree-nine residual.
* `verify_first_normal_coordinatefree.py` — invariant 175-variable rank
  calculation.
* `verify_f11_hensel.py` — the previous smooth line-level Hensel certificate.
* `check_f7_candidates_exact.py`, `check_f11_candidates_exact.py` — exact
  first-normal ranks for all listed rational chart points.
* `check_candidate_geometry.py` — geometric regularity and uniqueness of the
  collision pair.
* `FULL_KERNEL_ENUMERATION_LOG.txt` — exhaustive chart counts.

All certificate calculations are exact.  The two small obstruction verifiers
use only integer arithmetic; the geometric gcd check uses SymPy over finite
fields.
