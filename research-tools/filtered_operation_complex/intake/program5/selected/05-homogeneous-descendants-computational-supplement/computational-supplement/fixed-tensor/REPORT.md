# Five mathematical attacks on the cubic-homogeneous reduction

## Scope and status

The starting point is the exact 19-dimensional cubic-homogeneous map

\[
G(Z)=Z+H(Z),\qquad
Z=(x,y,z,a,b,c,d,q,s,h,k,w_1,\ldots,w_7,t),
\]

constructed from the normalized 11-dimensional degree-three representative

\[
K(X)=X+K_2(X)+K_3(X),\qquad K_3=Bq,
\]

where the coordinate span of the cubic part has dimension seven.  All claims
below are over characteristic zero unless a finite field is explicitly named.

The five attacks have different outcomes:

| Attack | Outcome |
|---:|---|
| 1. Minimal dimension, beginning with \(N=5\) | Global problem still open; collision normalized, search reduced to three Jordan types, and a natural 25-parameter boundary ansatz is pruned exactly |
| 2. Rank-compressed suspension | General theorem proved; the present representative gives \(11+7+1=19\); a nonzero cubic-jet cohomology class is exhibited |
| 3. Jordan and degeneration structure | Complete: \(JH\) has generic Jordan type \((18,1)\), with an explicit cyclic vector and kernel vector; all nonzero slices are conjugate and the zero slice is triangular |
| 4. Symmetric/Hessian reduction | Complete explicit 38-dimensional quartic; generic Hessian type \((35,2,1)\); an infinite closed-form sequence of nonzero Zhao Laplacian coefficients is obtained |
| 5. Constrained Drużkowski rank | Exact lower bound 39 and exact upper bound 110; the new 110-dimensional square-zero pairing improves the preceding 135-dimensional construction |

The strongest new formulas are

\[
(JH)^{17}e_t
=18t^{15}x^9y^5z^2v_2,
\]

\[
\operatorname{Jord}_{\operatorname{Frac}\mathbb Q[Z]}(JH)=(18,1),
\]

\[
\operatorname{Jord}(\operatorname{Hess}\mathcal Q)=(35,2,1),
\]

and, for every \(r\ge2\), with \(m=2r-3\),

\[
\boxed{
\partial_{u_1}\Delta^m\!\left(\mathcal Q^{m+1}\right)(\bar W)
=
\frac{(2r-3)!(2r-2)!}{16}\binom{2r}{r}\ne0.
}
\]

Here \(\mathcal Q\) is the explicit quartic in 38 variables defined in
Attack 4.

---

# 1. Attack on the minimal dimension \(N=5\)

## 1.1 No collision is collinear

Let

\[
F(x)=x+H(x),
\]

where \(H\) is cubic homogeneous and \(JH(x)\) is nilpotent.  Suppose
\(F(a)=F(\lambda a)\), with \(a\ne0\).  Homogeneity gives

\[
(1-\lambda)a+(1-\lambda^3)H(a)=0.
\]

If \(\lambda^3\ne1\), then

\[
H(a)=-\frac{1}{1+\lambda+\lambda^2}a.
\]

Euler's identity gives

\[
JH(a)a=3H(a),
\]

so \(a\) is an eigenvector of \(JH(a)\) with a nonzero eigenvalue, a
contradiction.  If \(\lambda^3=1\) and \(\lambda\ne1\), the original equation
forces \(a=0\), again a contradiction.

Thus any two distinct colliding points are linearly independent.  In
particular, \(F^{-1}(0)=\{0\}\).

## 1.2 Midpoint normalization

Write a collision as

\[
a=u+v,\qquad b=u-v.
\]

The vectors \(u,v\) are independent.  Write \(H(x)=T(x,x,x)\) with \(T\)
symmetric in the three input slots.  Then

\[
H(u+v)-H(u-v)=6T(u,u,v)+2T(v,v,v)
=2JH(u)v+2H(v).
\]

The collision equation becomes

\[
\boxed{v+JH(u)v+H(v)=0}
\]

or, using Euler,

\[
\boxed{\left(I+JH(u)+\frac13JH(v)\right)v=0.}
\]

After linear conjugation one can take \(u=e_1\), \(v=e_2\).  If

\[
A=JH(u),\quad B=6T(u,v,\cdot),\quad C=JH(v),
\]

then the restriction of the Jacobian to the collision plane is the quadratic
nilpotent pencil

\[
\boxed{JH(su+tv)=s^2A+stB+t^2C,}
\]

and the collision condition is

\[
\boxed{(I+A+C/3)v=0.}
\]

This is the most economical matrix formulation of the five-dimensional
problem.

## 1.3 Only three generic Jordan types remain

A five-dimensional counterexample cannot have \(\operatorname{rank}JH\le2\),
while nilpotence gives \(\operatorname{rank}JH\le4\).  Therefore its generic
rank is three or four.  The only possible generic nilpotent Jordan types are

\[
\boxed{(5),\qquad(4,1),\qquad(3,2).}
\]

Thus a classification can be split into three finite algebraic cases.

## 1.4 Direct coefficient system

A cubic map in five variables has

\[
5\binom{7}{3}=175
\]

scalar coefficients.  The normalized collision contributes five linear
equations.  In characteristic zero, nilpotence of the \(5\times5\) matrix
\(JH\) is equivalent to

\[
\operatorname{tr}(JH^k)=0,\qquad k=1,\ldots,5.
\]

Before eliminating redundancies, the numbers of coefficient equations are

\[
\binom{2k+4}{4}=15,70,210,495,1001,
\]

for a total of 1791.  A blind Gröbner-basis attack on this system is not the
recommended first move.  The quadratic pencil and the three Jordan strata
should be imposed first.

## 1.5 The first unresolved square-zero pairing boundary

A natural 25-parameter subproblem is obtained from a \(5\times5\) matrix
\(C\).  Put

\[
\phi(x)=x-x^{*3}
\]

and

\[
\boxed{
H_C(x)=Cx^{*3}-(Cx)^{*3}
=\phi(Cx)-C\phi(x).
}
\]

Equivalently, take

\[
B=[I\ C],\qquad D=\begin{bmatrix}-C\\I\end{bmatrix}.
\]

Then \(BD=0\), and

\[
H_C(x)=B(Dx)^{*3}.
\]

The corresponding 10-dimensional matrix \(A=DB\) satisfies

\[
A^2=0,\qquad \operatorname{rank}A=5.
\]

Thus this ansatz sits exactly at the first rank beyond the elementary
low-rank boundary for square-zero power-linear maps.

Its Jacobian is

\[
\frac13JH_C(x)
=C\operatorname{diag}(x^2)
-\operatorname{diag}((Cx)^2)C.
\]

Writing \(\Delta_C=\operatorname{diag}(c_{11},\ldots,c_{55})\), the trace-one
condition is exactly

\[
\boxed{C^T\Delta_C C=\Delta_C.}
\]

For zero diagonal, the trace-square identity becomes

\[
\boxed{
\operatorname{tr}\left((JH_C/3)^2\right)
=2\sum_{i<j}c_{ij}c_{ji}
\bigl(x_j^2-(Cx)_i^2\bigr)
\bigl(x_i^2-(Cx)_j^2\bigr).
}
\]

It is therefore controlled by reciprocal directed edges in the support graph
of \(C\).

### Exact sparse obstruction

Normalize the collision to \(F_C(e_1)=F_C(e_2)\) and assume \(C\) has zero
diagonal.  If \(f(t)=t-t^3\), the first two collision coordinates give

\[
f(c_{12})=f(c_{21})=1.
\]

Hence \(c_{12},c_{21}\ne0\), and neither is \(\pm1\).

If \(C\) has no other reciprocal pair, the trace-square formula has a single
nonzero product.  Its vanishing would force either
\((Cx)_1=\pm x_2\) or \((Cx)_2=\pm x_1\), contradicting
\(f(c_{12})=f(c_{21})=1\).

If the total support is at most four, there can be only one additional
reciprocal pair.  If it is disjoint from \(\{1,2\}\), the trace polynomial
splits into disjoint variable blocks and the first block must vanish by
itself, giving the same contradiction.  If it shares vertex 1 or 2, the
collision equation on the third vertex forces the reverse coefficient to be
\(\pm1\), so its trace-square summand vanishes identically and again cannot
cancel the \(\{1,2\}\) summand.

Therefore:

\[
\boxed{
\text{No zero-diagonal }H_C\text{ with the normalized collision and }
|\operatorname{supp}C|\le4\text{ is Keller.}
}
\]

The verifier also exhausts the corresponding finite-field boxes over
\(\mathbb F_5\) and \(\mathbb F_7\); no survivor occurs.

### Status of Attack 1

The global \(N=5\) problem is not resolved.  It has, however, been reduced to:

1. three generic Jordan strata;
2. a nilpotent quadratic matrix pencil with one explicit vector equation;
3. a 25-parameter square-zero boundary ansatz with exact first obstructions.

A realistic next computation is a stratum-by-stratum elimination for the
pencil \(s^2A+stB+t^2C\), followed by the tensor-integrability equations.

---

# 2. Rank-compressed suspension

## 2.1 General theorem

Let

\[
K(X)=X+Q(X)+C(X):\mathbb A^n\to\mathbb A^n,
\]

where \(Q\) is quadratic homogeneous and \(C\) is cubic homogeneous.  Put

\[
r=\dim\operatorname{span}\{C_1,\ldots,C_n\}.
\]

Choose a basis \(q=(q_1,\ldots,q_r)^T\) and a matrix \(B\in M_{n\times r}\)
such that

\[
C=Bq.
\]

Define

\[
\widetilde K(X,w)
=\bigl(X+Q(X)+Bw,\ w-q(X)\bigr).
\]

With

\[
S(X,w)=(X,w-q(X)),
\]

\[
T(U,V)=(U+BV,V),
\]

one has the exact stable-equivalence identity

\[
\boxed{
\widetilde K
=T\circ(K\times\operatorname{id}_r)\circ S.
}
\]

Adjoin one homogenizing coordinate and set

\[
\boxed{
G(X,w,t)
=\bigl(X+tQ(X)+t^2Bw,\ w-q(X),\ t\bigr).
}
\]

Its nonlinear part is cubic homogeneous.  The Jacobian determinant has the
small Schur-complement certificate

\[
\begin{aligned}
\det JG
&=\det
\begin{pmatrix}
I+tJQ&t^2B\\
-Jq&I
\end{pmatrix}\\
&=\det\bigl(I+tJQ+t^2BJq\bigr)\\
&=\det JK(tX).
\end{aligned}
\]

Thus if \(K\) is Keller with determinant one, so is \(G\).  Since the
nonlinear part of \(G\) is cubic homogeneous, replacing \(Z\) by \(sZ\)
shows that all characteristic coefficients of \(JH(Z)\) vanish; hence
\(JH\) is nilpotent.

The dimension is

\[
\boxed{n+r+1.}
\]

For a fixed \(K\), this is optimal within this factorized suspension model:
any such suspension must use at least \(r\) cubic auxiliary coordinates.

## 2.2 Application to the present map

For the normalized 11-dimensional representative,

\[
n=11,
\qquad
r=7.
\]

Therefore

\[
\boxed{N=11+7+1=19.}
\]

This motivates the stable complexity

\[
\mu(F_0)
=
\min_K\left(
\dim K+
\dim\operatorname{span}\{(K_3)_i\}
\right),
\]

where \(K\) ranges over normalized degree-at-most-three representatives
stably equivalent to the base map.  The present construction proves

\[
\boxed{\mu(F_0)\le18.}
\]

An 18-dimensional homogeneous descendant would follow from any representative
with \(\dim K+r(K)\le17\).

## 2.3 A nonzero cubic-jet class

Let \(K=X+Q+C\).  Under a quadratic near-identity conjugacy
\(X\mapsto X+P_2(X)\), the cubic jet changes by

\[
C\longmapsto C+[Q,P_2],
\]

where

\[
[Q,P_2]=JQ\,P_2-JP_2\,Q.
\]

For the fifth coordinate, corresponding to the variable \(b\), one has
\(Q_b=0\).  Define a linear functional on scalar cubics by

\[
\Lambda(f)
=[x^2y]f+\frac13[x^2k]f+\frac13[xzh]f-2[dhk]f.
\]

An exact coefficient computation gives

\[
\boxed{
\Lambda([Q,P_2]_b)=0
\quad\text{for every quadratic }P_2,
}
\]

while

\[
C_b=3x^2y,
\qquad
\boxed{\Lambda(C_b)=3.}
\]

Thus the cubic jet is not entirely removable by quadratic formal conjugacy.
This is a genuine cohomological obstruction.  It does **not** yet prove that
the cubic coordinate-span rank cannot drop from seven to six under a more
general nonlinear stable equivalence.

---

# 3. Jordan structure and degeneration

## 3.1 Two exact kernel vectors

Use the coordinate ordering

\[
Z=(x,y,z,a,b,c,d,q,s,h,k,w_1,\ldots,w_7,t).
\]

Set

\[
E=xy(c+2z)+d^2z+3dy^2.
\]

Two exact vectors in \(\ker JH\) are

\[
\boxed{
v_1
=2tx\,e_h+2tz\,e_k+(xk+zh)e_{w_1},
}
\]

and

\[
\boxed{
v_2
=-txy\,e_a-t(dz+3y^2)e_s-Ee_{w_3}+2Ee_{w_6}+xyz\,e_{w_7}.
}
\]

They are generically independent, so

\[
\operatorname{rank}JH\le17.
\]

At the all-ones specialization, \(JH\) has rank 17, proving equality over the
fraction field.

## 3.2 Explicit cyclic vector

Let \(e_t\) be the last coordinate vector.  Iterating only this column gives

\[
\boxed{
(JH)^{17}e_t
=18t^{15}x^9y^5z^2v_2.
}
\]

The right side is nonzero.  Since \(JH\) is nilpotent on a 19-dimensional
space and has a two-dimensional kernel, its largest Jordan block has size at
most 18.  Therefore its nilpotency index is exactly 18.

At the all-ones specialization, the ranks are

\[
17,16,15,\ldots,1,0
\]

for powers one through eighteen.  Moreover,

\[
\mathcal B=
(e_t,JHe_t,\ldots,(JH)^{17}e_t,v_1)
\]

specializes to a basis with determinant

\[
1952152956156672.
\]

Consequently \(\mathcal B\) is a basis over the rational function field and

\[
\boxed{
JH\sim J_{18}(0)\oplus[0].
}
\]

That is, the generic Jordan type is exactly

\[
\boxed{(18,1).}
\]

## 3.3 One-parameter degeneration

Let

\[
\widetilde K(X,w)
=(X+K_2(X)+Bw,w-q(X))
\]

and define

\[
S_\tau(X,w)=(\tau X,\tau^3w).
\]

For \(\tau\ne0\), the \(t=\tau\) slice of the homogeneous map is

\[
G_\tau(X,w)
=(X+\tau K_2(X)+\tau^2Bw,w-q(X)),
\]

and one has the exact conjugacy

\[
\boxed{
G_\tau=S_\tau^{-1}\widetilde K S_\tau.
}
\]

At \(\tau=0\),

\[
\boxed{
G_0(X,w)=(X,w-q(X)),
}
\]

which is triangular.  Hence the family degenerates from degree-three,
noninjective Keller maps for every \(\tau\ne0\) to a polynomial automorphism at
\(\tau=0\).  A collision of \(\widetilde K\) transports to one of \(G_\tau\)
by \(S_\tau^{-1}\); the \(X\)-coordinates scale as \(\tau^{-1}\) and the
\(w\)-coordinates as \(\tau^{-3}\).  The disappearing sheets therefore escape
to infinity with explicit valuations.

---

# 4. The 38-dimensional Hessian-nilpotent quartic

## 4.1 Symmetric doubling

Starting from \(G(x)=x+H(x)\) on \(\mathbb A^{19}\), define

\[
\Phi(x,y)=\bigl(G(x),JG(x)^Ty\bigr).
\]

Its Jacobian is block lower triangular:

\[
J\Phi=
\begin{pmatrix}
JG&0\\
*&JG^T
\end{pmatrix},
\]

so

\[
\det J\Phi=(\det JG)^2=1.
\]

Let

\[
T(u,v)=\left(u+iv,\frac{u-iv}{2}\right).
\]

The scalar \(2\times2\) block of \(T\) satisfies

\[
TT^T=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Therefore

\[
\mathcal G=T^{-1}\Phi T
=I+\nabla\mathcal Q,
\]

where the explicit homogeneous quartic is

\[
\boxed{
\mathcal Q(u,v)
=\frac12(u-iv)^TH(u+iv).
}
\]

Its expanded form has 724 nonzero monomials over \(\mathbb Q(i)\) and is
included as `quartic38.txt`.

If \(G(a)=G(b)\), then

\[
\Phi(a,0)=\Phi(b,0),
\]

and hence

\[
\boxed{
\mathcal G(T^{-1}(a,0))
=\mathcal G(T^{-1}(b,0)).
}
\]

Thus the collision is explicit.

## 4.2 Generic Hessian Jordan type

The nonlinear Jacobian before the twist is

\[
N=
\begin{pmatrix}
A&0\\
L&A^T
\end{pmatrix},
\qquad
A=JH(x),
\]

where

\[
L=J_x(A(x)^Ty)
=\operatorname{Hess}_x(y^TH(x)).
\]

The Hessian of \(\mathcal Q\) is similar to \(N\).

The exact kernel vectors from Attack 3 satisfy the stronger directional
identities

\[
\boxed{
D^2H[v_1,v_2]=0,
\qquad
D^2H[v_2,v_2]=0.
}
\]

Since \(\ker A=\langle v_1,v_2\rangle\) generically, these identities show
that \(Lv_2\) is orthogonal to \(\ker A\), hence belongs to
\(\operatorname{im}A^T\).  Besides the two vectors
\((0,q)\), \(q\in\ker A^T\), the block matrix \(N\) therefore has a third
kernel vector with first component \(v_2\).  Thus

\[
\operatorname{rank}N\le35.
\]

At the all-ones specialization with \(y=(1,\ldots,1)\), exact arithmetic gives

\[
\operatorname{rank}N=35.
\]

For powers of a block triangular matrix,

\[
(N^k)_{21}
=\sum_{j=0}^{k-1}(A^T)^jLA^{k-1-j}.
\]

Since \(A^{18}=0\), the only possible term in \((N^{35})_{21}\) is

\[
(A^T)^{17}LA^{17}.
\]

The image of \(A^{17}\) is spanned by \(v_2\), and
\(D^2H[v_2,v_2]=0\), so this term vanishes.  Hence

\[
N^{35}=0.
\]

At the same all-ones specialization,

\[
(N^{34})_{38,19}=648\ne0.
\]

Therefore the generic Hessian nilpotency index is 35.  Rank 35 means that a
38-dimensional nilpotent matrix has three Jordan blocks; the largest has size
35, and the remaining two dimensions must be partitioned as 2 and 1.  Thus

\[
\boxed{
\operatorname{Jord}(\operatorname{Hess}\mathcal Q)=(35,2,1).
}
\]

## 4.3 An explicit inverse ray

Let the base target be

\[
(P,Q,R)=(0,\rho,\rho)
\]

and put

\[
\eta=\sqrt{1-\rho^2}.
\]

The inverse branch at the origin is

\[
\boxed{
 x(\rho)=\frac{\eta^{-1}-1}{\rho},
\qquad
 y(\rho)=\rho,
\qquad
 z(\rho)=-\rho^2\eta(\eta+3).
}
\]

It satisfies the three base equations exactly.  The lift to the 11-dimensional
map is obtained by

\[
\begin{aligned}
d&=xy,&h&=x^2,&k&=-xz,\\
b&=-3x^2y,&c&=-xyz-3y^2-2z,&a&=-x^2y^2,\\
q&=3x(2xyz+3y^2+2z),&&&
 s&=y(3x^2yz+6xy^2+6xz+7y).
\end{aligned}
\]

The last eight outputs then vanish identically.

Let

\[
\bar Y=(1/2,1,0,\ldots,0,1)\in\mathbb Q^{19},
\]

where the final entry is the homogenizing coordinate.  Stable equivalence and
homogeneity give

\[
\boxed{
(G^{-1}(s\bar Y))_1
=\frac{x(s^2)}{s}
=\sum_{r\ge1}\frac1{4^r}\binom{2r}{r}s^{4r-3}.
}
\]

For the symmetric map, put

\[
\bar W=T^{-1}(\bar Y,0)
=\left(\frac{\bar Y}{2},-\frac{i\bar Y}{2}\right).
\]

Then

\[
\boxed{
(\mathcal G^{-1}(s\bar W))_{u_1}
=\frac12\sum_{r\ge1}
\frac1{4^r}\binom{2r}{r}s^{4r-3}.
}
\]

The first term, \(s/4\), is the identity term.  Every subsequent displayed
coefficient is nonzero.

## 4.4 Infinite nonvanishing for Zhao's Laplacian expressions

Set

\[
P=-\mathcal Q,
\]

so that

\[
\mathcal G=I-\nabla P.
\]

For a Hessian-nilpotent potential, the inversion potential has homogeneous
terms

\[
R_m=
\frac{1}{2^m m!(m+1)!}
\Delta^m(P^{m+1}).
\]

The degree of \(\nabla R_m\) is \(2m+3\).  Comparing with the inverse ray,
set

\[
m=2r-3,
\qquad r\ge2.
\]

Then \(m+1=2r-2\) is even, so

\[
P^{m+1}=\mathcal Q^{m+1}.
\]

Coefficient comparison gives the closed formula

\[
\boxed{
\partial_{u_1}
\Delta^{2r-3}\left(\mathcal Q^{2r-2}\right)(\bar W)
=
\frac{(2r-3)!(2r-2)!}{16}\binom{2r}{r}.
}
\]

It is nonzero for every \(r\ge2\).  The first value is

\[
\boxed{
\partial_{u_1}\Delta(\mathcal Q^2)(\bar W)=\frac34.
}
\]

Thus the 38-dimensional quartic supplies not merely an abstract failure of
eventual vanishing, but an explicit infinite sequence of nonzero Laplacian
coefficients.

---

# 5. Constrained Drużkowski rank

## 5.1 Catalecticant lower bound

Consider a vector Waring decomposition

\[
H(z)=\sum_{\nu=1}^R b_\nu\ell_\nu(z)^3,
\qquad
b_\nu\in\mathbb Q^{19},
\quad
\ell_\nu\in(\mathbb Q^{19})^*.
\]

Every first derivative is in the span of the squares \(\ell_\nu^2\):

\[
\partial_jH_i
=3\sum_\nu (b_\nu)_i(\ell_\nu)_j\ell_\nu^2.
\]

Consequently

\[
R\ge
\dim\operatorname{span}\{\partial_jH_i:1\le i,j\le19\}.
\]

The exact \(361\times190\) derivative catalecticant has rank

\[
\boxed{39.}
\]

Therefore every vector Waring decomposition, and in particular every
full-rank square-zero pairing of this fixed \(H\), needs at least 39 cubes.

## 5.2 A 110-dimensional exact pairing

The elementary identities for \(ab^2\) and \(abc\), after sign
coalescence, give an initial 134-form decomposition.  Its cube-evaluation
matrix has rank 117 and nullity 17.

Each output coefficient vector can be adjusted by a vector in this
17-dimensional nullspace without changing \(H\).  A rank-16 flat containing
24 of the 134 coefficient rows was found and then checked exactly.  These 24
forms can be zeroed simultaneously.  On the remaining 110 forms:

\[
\operatorname{rank}W_S=109,
\]

so there is one cube relation.  That relation also has zero first moment
against the linear-form matrix and is independent of the 18 nonzero output
rows.  Using it as the nineteenth, zero-output row gives matrices

\[
B\in M_{19\times110}(\mathbb Q),
\qquad
D\in M_{110\times19}(\mathbb Q)
\]

with

\[
\boxed{
\operatorname{rank}B=
\operatorname{rank}D=19,
\qquad
BD=0,
\qquad
H(z)=B(Dz)^{*3}.
}
\]

Set

\[
\boxed{A=DB\in M_{110}(\mathbb Q).}
\]

Then

\[
\boxed{
A^2=0,
\qquad
\operatorname{rank}A=19,
\qquad
\operatorname{corank}A=91.
}
\]

A right inverse \(C\) of \(B\) gives the exact pairing identity

\[
\boxed{
B\bigl(Cz+(ACz)^{*3}\bigr)=z+H(z)=G(z).
}
\]

The collision is transported by the same kernel-translation formula used in
the earlier pairing.

The diagonal-scaled Jacobian correction has nilpotency index 19.  The matrix
is not D-nilpotent: the principal minor on indices \(\{1,8\}\) is

\[
\boxed{\det A[\{1,8\},\{1,8\}]=\frac1{576}.}
\]

The complexity tuple is

\[
\boxed{
C(A)=(110,19,91,19,3812,53).
}
\]

This replaces the previous 135-dimensional upper bound.  Combining it with
the catalecticant gives

\[
\boxed{
39\le N_{\mathrm{pair}}\le110
}
\]

for the full-rank square-zero pairing problem attached to this fixed
19-dimensional tensor.  Neither endpoint is claimed globally sharp.

---

# What is now proved, and what remains open

## Proved in this package

1. The rank-compressed suspension theorem and its \(19\)-dimensional
   application.
2. A nonzero cubic-jet obstruction for the normalized 11-dimensional map.
3. An explicit generic Jordan basis for \(JH\), with type \((18,1)\).
4. The exact nonzero-slice conjugacy and triangular special fiber.
5. An explicit 38-dimensional homogeneous quartic with Hessian type
   \((35,2,1)\), collision, and infinite nonzero Laplacian sequence.
6. An exact catalecticant lower bound of 39.
7. An exact 110-dimensional square-zero Drużkowski pairing.

## Still open

1. Whether a cubic-homogeneous counterexample exists in dimension 5, or in
   any dimension from 5 through 18.
2. Whether \(\mu(F_0)\) is strictly less than 18.
3. Whether the seven-dimensional cubic span can be reduced to six by a
   nonlinear stable equivalence.
4. The exact constrained Waring/pairing rank between 39 and 110.
5. Whether a direct Drużkowski representative can beat every pairing-based
   construction.

---

# Running the certificates

```bash
./run_all.sh
```

The scripts use exact SymPy arithmetic.  The finite-field searches in Attack 1
are exhaustive only in the explicitly stated sparse boxes.  No numerical
calculation is used to establish a characteristic-zero identity.
