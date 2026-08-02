# Formal effectivity of the quadratic cubic-frame modulus

## Statement and scope

Let `R` be a commutative `Q`-algebra.  For `alpha,q in R`, put

\[
A_\alpha(c)=c(1+\alpha c),\qquad
B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\]

and let `F_{alpha,q}=G_{A_alpha,B_alpha,q}` be the corresponding cubic-frame
Keller map.  Write

\[
\delta=q'-q.
\]

The theorem below has two levels.

1. It gives an exact existence and degree criterion in the framed
   root-translation groupoid over an arbitrary coefficient ring.
2. For the pointed arcs `alpha=s` over `C[[s]]`, it proves a genuinely
   unframed statement: all Artin truncations are compatibly ordinarily
   left-right equivalent, but the two complete families are not even stably
   polynomially left-right equivalent.

Thus the stable left-right groupoid fails formal effectivity at the
quadratic modulus.  The quantitative degree lower bound is framed; the
non-effectivity conclusion and complexity divergence are unrestricted.

Two published results frame the argument.  The complete stable
`q`-classification of the nonzero-`alpha` fibers is the load-bearing input for
generic-fiber nonexistence; the existing all-order coefficientwise formal
source triviality is overlapping background that the explicit calculation
below sharpens.  The new content is the exact orbit cokernel and annihilator
law, the sharp framed degree staircase, nonalgebraizability over `C[[s]]`,
divergence of unrestricted stable-equivalence complexity, and the diagonal
obstruction for algebraic moduli.

## 1. Root-translation identity

For `phi(c) in c R[c]`, define

\[
\Theta_\phi(x,y,z)=
\left(x,\ y+\phi(c),\ z-3\frac{\phi(c)}x\right).
\]

It is polynomial because

\[
\frac cx=2-3xy-x^2z.
\]

It fixes `c`, shifts the marked root coordinate `t` to `t+phi(c)`, and has
inverse `Theta_{-phi}`.  Put

\[
\ell_\phi=3A\phi^2+2B\phi,
\qquad
\eta_\phi=A\phi^3+B\phi^2,
\]

and define the triangular target automorphism

\[
\Xi_\phi(a,b,c)=
\left(
 a-\frac12\phi(c)b-\frac12\eta_\phi(c),
 b+\ell_\phi(c),
 c
\right).
\]

Direct expansion of the shifted cubic gives

\[
\boxed{
G_{A,B+3A\phi}=\Xi_\phi\circ G_{A,B}\circ\Theta_\phi.
}
\]

## 2. Exact Artin effectivity criterion

### Theorem 2.1 — annihilator and degree law

For an integer `D>=0`, there is a `c`-fixed framed root translation of
`c`-degree at most `D` from `F_{alpha,q}` to `F_{alpha,q'}` if and only if

\[
\boxed{\delta\alpha^{D+2}=0.}
\]

When this condition holds, the translation is unique and equals

\[
\boxed{
\phi_D(c)=
\frac\delta3\alpha^2c
\sum_{j=0}^{D-1}(-\alpha c)^j,
}
\]

where the sum is empty when `D=0`.  Before imposing the annihilator
condition, its exact residual is

\[
\boxed{
B_{\alpha,q'}-B_{\alpha,q}-3A_\alpha\phi_D
=(-1)^D\delta\alpha^{D+2}c^{D+2}.
}
\]

If

\[
N=\min\{n\ge2:\delta\alpha^n=0\}
\]

exists, then `N=2` means that the two frames already agree and the unique
translation is zero.  For `N>=3`, the unique translation has exact
`c`-degree `N-2`.  If no such `N` exists, there is no polynomial framed
translation.

### Proof

The coefficient equation is

\[
3c(1+\alpha c)\phi(c)=\delta\alpha^2c^2.
\]

Multiplication by `c` is injective in `R[c]`, so this is equivalent to

\[
3(1+\alpha c)\phi(c)=\delta\alpha^2c.
\]

Write

\[
\phi(c)=p_1c+\cdots+p_Dc^D.
\]

Coefficient comparison gives

\[
3p_1=\delta\alpha^2,
\qquad
p_i=-\alpha p_{i-1}\quad(2\le i\le D),
\qquad
\alpha p_D=0.
\]

Hence

\[
p_i=\frac\delta3(-1)^{i-1}\alpha^{i+1}.
\]

The terminal equation is exactly `delta*alpha^(D+2)=0`, and all coefficients
are forced, proving existence and uniqueness.  Multiplying the finite
geometric series by `1+alpha*c` gives the displayed residual.  If `N>=3` is minimal, the coefficient of `c^(N-2)` is a unit multiple of
`delta*alpha^(N-1)`, which is nonzero; hence the degree is exactly `N-2`.
For `N=2`, the frames already coincide and `phi=0`.

### Proposition 2.2 — the exact orbit cokernel

The framed coefficient quotient has a one-line module description.  Let

\[
\mu_\alpha:cR[c]\longrightarrow c^2R[c],
\qquad
\phi\longmapsto 3A_\alpha\phi.
\]

After dividing the source by `c`, the target by `c^2`, and the map by the
unit three,

\[
\boxed{
\operatorname{coker}(\mu_\alpha)
\simeq R[c]/(1+\alpha c).
}
\]

The difference between the `q'`- and `q`-frames is represented by

\[
\boxed{
\frac{\delta}{3}\alpha^2\bmod(1+\alpha c).
}
\]

For `R=C[[s]]` and `alpha=s`, evaluation at `c=-1/s` gives

\[
R[c]/(1+sc)\simeq R[1/s]=\mathbb C((s)).
\]

The obstruction class is nonzero when `q!=q'`, but multiplication by `s` is
invertible on the entire cokernel.  Hence every quotient modulo `s^M`, and
the `s`-adic completion of the cokernel, is zero.  The finite geometric
series in Theorem 2.1 is exactly the degree-filtered Neumann expansion of the
inverse of `1+sc`.

## 3. Ramification law over truncated DVRs

Let

\[
R_M=\mathbb C[s]/(s^M)
\]

and suppose

\[
\alpha=s^eu(s),\qquad u(0)\ne0,
\]

with `1<=e<M`.  For `q!=q'`, `delta` is a unit and the nilpotence index of
`alpha` is `ceil(M/e)`.  Theorem 2.1 gives the exact complexity

\[
\boxed{
D_M=\max\left(0,\left\lceil\frac Me\right\rceil-2\right).
}
\]

Equivalently, a framed translation of `c`-degree at most `D` can identify
the two ramified arcs modulo `s^M` exactly when

\[
M\le e(D+2).
\]

For the unramified pointed arc `alpha=s`,

\[
\boxed{D_M=M-2\qquad(M\ge3).}
\]

The optimal residual after allowing degree `D` is the single staircase term

\[
\boxed{
(-1)^D(q'-q)s^{D+2}c^{D+2}.
}
\]

Increasing the allowed degree by one kills this obstruction and moves it one
step northeast, from `(s^(D+2),c^(D+2))` to
`(s^(D+3),c^(D+3))`; there is no terminal finite obstruction.

For `D>=1`, the canonical source and target automorphisms have exact ordinary
degrees

\[
\boxed{
\deg\Theta_{\phi_D}=4D,
\qquad
\deg\Xi_{\phi_D}=D+1.
}
\]

Indeed, `c(x,y,z)` has degree four, the top `c^D` coefficient of `phi_D` is
nonzero, and the target term `phi_D(c)b` has degree `D+1`.  Nilpotence forces
all other triangular target corrections to have degree at most `D`.

## 4. Residual affine frame changes do not improve the law

Assume now that `R` is local, `alpha` belongs to its maximal ideal, and
`delta` is a unit.  Consider an affine transformation of the normalized
conductor chart

\[
C=uc+v,\qquad T=\nu t+h(c),
\]

with `u,nu,kappa` units, satisfying

\[
A_\alpha(C)\nu=\kappa A_\alpha(c),
\]

\[
B_{\alpha,q'}(C)+3A_\alpha(C)h(c)
=\kappa B_{\alpha,q}(c).
\]

Then

\[
\boxed{
v=0,\quad \kappa=1,\quad \nu u=1,\quad
\alpha(u-1)=0,
}
\]

and

\[
\boxed{
h(c)=\frac{q-q'}{3u}\frac{\alpha^2c}{1+\alpha c}.}
\]

Consequently the minimal `c`-degree is again the integer in Theorem 2.1.

To prove this, the constant term of the first frame equation is
`v*(1+alpha*v)=0`.  The second factor is a unit, so `v=0`.  Comparing the
`c` and `c^2` coefficients gives `nu*u=kappa` and `alpha*(u-1)=0`.  The
constant term of the second frame equation gives `kappa=1`; its linear term
gives `h(0)=0`.  The relation `alpha*(u-1)=0` makes
`A_alpha(uc)=u*A_alpha(c)` and `B_alpha,q'(uc)=B_alpha,q'(c)`, leaving the
displayed root-translation equation.  Multiplication by the unit `u^(-1)`
cannot lower its exact degree.

## 5. Formal completion does not commute with bounded degree

Fix `q!=q'`, put `alpha=s`, and let

\[
\mathcal I_D(M)
\]

be the set of `c`-fixed framed isomorphisms over `R_M` whose root translation
has `c`-degree at most `D`.  Theorem 2.1 gives

\[
\mathcal I_D(M)\ne\varnothing
\quad\Longleftrightarrow\quad
M\le D+2.
\]

For every `M`, the union over `D` contains the unique translation

\[
\phi_M(c)=\frac{q'-q}{3}s^2c
\sum_{j=0}^{M-3}(-sc)^j,
\]

and these translations are compatible under `R_(M+1) -> R_M`.  Therefore

\[
\boxed{
\varprojlim_M\ \varinjlim_D\mathcal I_D(M)
\ne\varnothing,
\qquad
\varinjlim_D\ \varprojlim_M\mathcal I_D(M)
=\varnothing.
}
\]

More precisely, the first set is a singleton and is represented by

\[
\boxed{
\widehat\phi(c)=
\frac{q'-q}{3}\frac{s^2c}{1+sc}
=\frac{q'-q}{3}
\sum_{j\ge0}(-1)^js^{j+2}c^{j+1}.
}
\]

It belongs to

\[
c\,\mathbb C[c][[s]]
=\varprojlim_M cR_M[c],
\]

but not to

\[
c\,\mathbb C[[s]][c],
\]

because its `c`-degree is unbounded.  Thus the compatible system defines a coefficientwise `s`-adic formal
left-right equivalence in `C[x,y,z][[s]]`, but not a polynomial equivalence
over the complete base `C[[s]]`.

## 6. Full stable left-right non-effectivity

### Theorem 6.1 — all Artin truncations agree, the complete families do not

Let

\[
\mathcal F_q=F_{s,q}
\]

be viewed as a polynomial Keller map over `R=C[[s]]`.  If `q!=q'`, then:

1. for every `M>=1`, the reductions
   `mathcal F_q mod s^M` and `mathcal F_q' mod s^M` are ordinarily
   polynomially left-right equivalent;
2. the equivalences can be chosen compatibly in `M`;
3. `mathcal F_q` and `mathcal F_q'` are not stably polynomially left-right
   equivalent over `C[[s]]`.

Hence the natural map

\[
\operatorname{Isom}^{\rm stable}_{\mathbb C[[s]]}
(\mathcal F_q,\mathcal F_{q'})
\longrightarrow
\varprojlim_M
\operatorname{Isom}^{\rm stable}_{R_M}
(\mathcal F_q\bmod s^M,\mathcal F_{q'}\bmod s^M)
\]

has empty source and nonempty target.

### Proof

For `M<=2` the two frames are equal.  For `M>=3`, use the compatible
translations `phi_M` above and the exact root-translation identity.  This
proves the first two assertions without stabilization.

Suppose a stable polynomial left-right equivalence existed over `C[[s]]`.
After passing to the fraction field `C((s))` and then to an algebraic closure
`L`, it would give a stable equivalence of the generic fibers.  The diagonal
scaling of the cubic frame normalizes the nonzero coefficient `alpha=s` to
`alpha=1`, carrying the two generic fibers to the normalized members `G_q`
and `G_q'` over `L`.

This already contradicts the published classification over `C`; no separate
field-extension version of that theorem is needed.  Fix the stabilization
dimension and the finite degrees of the four polynomial automorphisms and
inverse automorphisms occurring in the alleged equivalence.  Their
coefficients form an `L`-point of an affine scheme of finite type over `C`,
cut out by the composition-inverse equations and the left-right equality.  A
nonempty finite-type scheme over the algebraically closed field `C` has a
`C`-point.  Such a point would be a stable polynomial equivalence between
`G_q` and `G_q'` over `C`, which the complete `q`-classification forbids when
`q!=q'`.  This is the required contradiction.

The formal isomorphism supplied by `widehat phi` does not contradict this
argument: its coordinate functions lie in the completed ring
`C[x,y,z][[s]]`, not in the polynomial ring `C[[s]][x,y,z]`.

### Theorem 6.2 — effective unrestricted complexity lower bound

For an ordinary or stable polynomial left-right equivalence over

\[
R_M=\mathbb C[s]/(s^M),
\]

define its complexity to be

\[
\max\{m,\deg\Phi,\deg\Phi^{-1},\deg\Psi,\deg\Psi^{-1}\},
\]

where `m` is the stabilization dimension.  Let `kappa_M(q,q')` be the
minimum complexity of an equivalence between the two `M`-th truncations.
Then

\[
\boxed{
\kappa_M(q,q')
\ge \frac{\log\log M}{\log 4}
     -O(\log\log\log M),
}
\]

and in particular

\[
\boxed{
\liminf_{M\to\infty}
\frac{\kappa_M(q,q')}{\log\log M}\ge\frac1{\log4}.}
\]

A finite version is the following.  If there is an equivalence using exactly
`m` stabilization variables, and all four automorphisms have degree at most
`b>=1`, put

\[
n=3+m,\qquad
T(n,b)=\binom{n+b}{n},\qquad
N(n,b)=4nT(n,b),
\]

\[
d_b=\max\{b+1,11\}.
\]

Then

\[
\boxed{
M\le 2b\bigl(N(n,b)+1\bigr)d_b^{N(n,b)}.}
\]

Consequently, for fixed stabilization dimension `m`, if `b_(M,m)` is the
least common degree bound for the equivalence and its inverses and
`n=3+m`, then

\[
\boxed{
\liminf_{M\to\infty}
\frac{b_{M,m}}{(\log M/\log\log M)^{1/n}}
\ge\left(\frac{n!}{4}\right)^{1/n}.}
\]

In particular, ordinary equivalences satisfy

\[
b_{M,0}\ge
\left(\frac32\frac{\log M}{\log\log M}\right)^{1/3}(1-o(1)).
\]

### Proof

Fix `m,b`.  Introduce coefficient variables for four polynomial maps

\[
\Phi,\Phi^{-1},\Psi,\Psi^{-1}:\mathbb A^n\to\mathbb A^n
\]

of degree at most `b`.  There are

\[
N=4n\binom{n+b}{n}
\]

coefficient variables.  The two-sided inverse equations and the stable
left-right identity define an affine scheme `E_(m,b)` over `C[s]`.  Every
defining equation `f_i` has

\[
\deg_Xf_i\le d_b,
\qquad
\deg_sf_i\le2b.
\]

The first estimate follows because composition-inverse coefficients have
degree at most `b+1` in the unknown coefficients and the family has ordinary
degree eleven.  For the second, the coefficients of `F_q` have `s`-degree at
most two, and a degree-`b` monomial in its coordinates has `s`-degree at most
`2b`.

The generic fiber of `E_(m,b)` is empty.  Otherwise, after algebraic extension
of `C(s)` and diagonal normalization of `s`, it would give a stable
equivalence between `G_q` and `G_q'`.  With `m,b` fixed, that is a point of a
finite-type scheme over the algebraically closed field `C`; nonemptiness
after field extension would give a complex point, contradicting the complete
stable `q`-classification.

A dimension-count incidence argument replaces the defining equations by
`N+1` constant complex linear combinations `g_0,...,g_N` that still have no
common zero over the algebraic closure of `C(s)`.  Indeed, for a fixed point
`x`, the nonzero vector `(f_i(x))` imposes one independent linear equation on
each of `N+1` rows of combination coefficients.  The bad incidence therefore
has dimension at most one less than the parameter space.  Since `C` is
infinite, the required generic tuple can be chosen with constant complex
entries.

The parametric effective Nullstellensatz of D'Andrea--Krick--Sombra then gives
`0 != alpha_(m,b)(s) in C[s]` in the ideal of the `g_j`, with

\[
\deg_s\alpha_{m,b}
\le\sum_{\ell=0}^{N}
\left(\prod_{j\ne\ell}\deg_Xg_j\right)\deg_sg_\ell
\le2b(N+1)d_b^N.
\]

An `R_M`-point annihilates the `g_j`, hence annihilates `alpha_(m,b)`.  Thus

\[
M\le\operatorname{ord}_s\alpha_{m,b}
\le\deg_s\alpha_{m,b},
\]

which proves the finite bound.

For fixed `n`,

\[
N(n,b)=\frac4{(n-1)!}b^n+O_n(b^{n-1}),
\]

so

\[
\log H(m,b)=\frac4{(n-1)!}b^n\log b+O_n(b^n).
\]

Asymptotic inversion gives the fixed-stabilization statement.  For unrestricted
complexity at most `B`, use

\[
N\le32(B+3)4^B,\qquad d_b\le B+11,
\]

to obtain

\[
M\le2B\bigl(32(B+3)4^B+1\bigr)
(B+11)^{32(B+3)4^B}.
\]

Taking two logarithms gives

\[
\log\log M\le B\log4+O(\log B),
\]

and the asserted unrestricted rate follows.

The explicit framed equivalences still give the much larger upper bound

\[
\kappa_M(q,q')\le4M-8\qquad(M\ge3).
\]

The remaining open problem is the sharp **linear** unframed lower rate, not
mere divergence or effectivity.

The formal non-effectivity argument is not specific to a DVR.  Let `R` be an integral
`C`-algebra, complete and separated for the `alpha`-adic topology, with
`alpha` a nonzero nonunit, and keep `q,q' in C` distinct.  Then the reductions
modulo `alpha^M` are compatibly ordinarily left-right equivalent with exact
framed degree `M-2`, while the complete maps over `R` are not stably
equivalent.  Indeed, strictness of the powers of the nonunit `alpha` gives
the degree assertion, and nonexistence follows after passing to an algebraic
closure of `Frac(R)` and applying the same finite-type descent to the
published complex classification.  Thus the effectivity failure is intrinsic
to a nonnilpotent parameter becoming nilpotent on every infinitesimal
quotient, not to the particular coordinate `s`.

## 7. Consequence for algebraic moduli stacks

### Corollary 7.1 — affine finite-presentation diagonals are impossible

No algebraic stack can model this stable polynomial left-right groupoid near
the two arcs while simultaneously having an affine diagonal locally of
finite presentation and representing its isomorphisms exactly.

Indeed, suppose such a stack `X` existed and let `x_q,x_q' in X(C[[s]])` be
the two objects.  The isomorphism space

\[
I=\operatorname{Isom}_X(x_q,x_q')
\]

would be affine and of finite presentation over `C[[s]]`, say `I=Spec A`.
For a finitely presented algebra,

\[
\operatorname{Hom}(A,\mathbb C[[s]])
\simeq
\varprojlim_M
\operatorname{Hom}(A,R_M).
\]

The compatible Artin isomorphisms would therefore produce a
`C[[s]]`-point of `I`, contradicting Theorem 6.1.

This obstruction concerns the **diagonal**, not merely separatedness of a
coarse orbit space.  A moduli construction can avoid it only by changing the
morphism notion, retaining degree or boundary data, or leaving the class of
stacks with affine finitely presented diagonal.

## 8. Lane 3 interpretation

The theorem gives a precise bridge between bounded deformation theory and
the stable `q`-modulus:

- every finite Artin neighborhood of the degree-seven point forgets `q` in
  the unrestricted polynomial left-right groupoid;
- a degree filtration recovers information progressively, with the exact law
  `M <= D+2`;
- the obstruction does not die—it moves to higher `s`-order and higher
  `c`-degree;
- the compatible limit is a formal automorphism of unbounded spatial degree;
- global stable separation is recovered on the generic fiber by the deleted
  boundary value `B(-1/s)=q+2`.

Thus `q` is neither a tangent character nor a finite Kuranishi obstruction.
It is a failure of bounded-degree effectivity supported at a divisor escaping
from the formal neighborhood.
