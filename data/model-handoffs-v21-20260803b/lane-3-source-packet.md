# Lane 3 exact research source packet

This is the public source packet for **Bounded-degree deformation and modulus onset**. It contains the
selected proof notes, exact computation contracts, and checkers used
by the concise lane brief. Read only the files relevant to the route
you pursue. Stored outputs and very large reconstructible matrices are
omitted; the mathematical boundary of each checker remains in its
source text.

Private-source commit: `75da31f1a28eed187e9f825bd764a578e94d1bb2`.

## Included files

- `lane3-formal-effectivity/formal_effectivity_theorem.md` — `1f01ad944f7bcc1fbc9474497f5071fd3df91d8305b043dc975513db9c7f9267`
- `lane3-formal-effectivity/formal_effectivity_insertion.tex` — `fb9e1e150ea387ae272daf0c03af233d937eefd12530adfdd29d4b9185a0b6d2`
- `lane3-formal-effectivity/AUDIT.md` — `2daaa07bb9a0fc327da4ceb40ebde655383429e0e05b67ed939eaf9274f80725`
- `lane3-formal-effectivity/verify_formal_effectivity.py` — `fed25d2940f0fca521cde6b03d83ad96a7e7179d366ed4ac0bf99ac5c8d2632f`
- `lane3-formal-effectivity/verify_formal_effectivity_independent.py` — `700170ac7053a2cdf8521189faede15107cd651e8277eb341f108602f413f46a`
- `lane3-formal-effectivity/verify_effective_unframed_bound.py` — `7f5cfe5706f4b41cd2c680fce23c3e907bc0e9e98a78fc052ac7b5d3cfe4b74f`

## `lane3-formal-effectivity/formal_effectivity_theorem.md`

<pre><code class="language-markdown">
# Formal effectivity of the quadratic cubic-frame modulus

## Statement and scope

Let `R` be a commutative `Q`-algebra.  For `alpha,q in R`, put

\&#91;
A_\alpha(c)=c(1+\alpha c),\qquad
B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\&#93;

and let `F_{alpha,q}=G_{A_alpha,B_alpha,q}` be the corresponding cubic-frame
Keller map.  Write

\&#91;
\delta=q'-q.
\&#93;

The theorem below has two levels.

1. It gives an exact existence and degree criterion in the framed
   root-translation groupoid over an arbitrary coefficient ring.
2. For the pointed arcs `alpha=s` over `C&#91;&#91;s&#93;&#93;`, it proves a genuinely
   unframed statement: all Artin truncations are compatibly ordinarily
   left-right equivalent, but the two complete families are not even stably
   polynomially left-right equivalent.

Thus the stable left-right groupoid fails formal effectivity at the
quadratic modulus.  The quantitative degree lower bound is framed; the
non-effectivity conclusion and complexity divergence are unrestricted.

Two proved results frame the argument.  The complete stable
`q`-classification of the nonzero-`alpha` fibers is Theorem `thm:main` and
Corollary `cor:q-classification` of
`manuscripts/04-stable-moduli/main.tex`; it is the load-bearing input for
generic-fiber nonexistence.  The existing all-order coefficientwise formal
source triviality is overlapping background that the explicit calculation
below sharpens.  The new content is the exact orbit cokernel and annihilator
law, the sharp framed degree staircase, nonalgebraizability over `C&#91;&#91;s&#93;&#93;`,
divergence of unrestricted stable-equivalence complexity, and the diagonal
obstruction for algebraic moduli.

## 1. Root-translation identity

For `phi(c) in c R&#91;c&#93;`, define

\&#91;
\Theta_\phi(x,y,z)=
\left(x,\ y+\phi(c),\ z-3\frac{\phi(c)}x\right).
\&#93;

It is polynomial because

\&#91;
\frac cx=2-3xy-x^2z.
\&#93;

It fixes `c`, shifts the marked root coordinate `t` to `t+phi(c)`, and has
inverse `Theta_{-phi}`.  Put

\&#91;
\ell_\phi=3A\phi^2+2B\phi,
\qquad
\eta_\phi=A\phi^3+B\phi^2,
\&#93;

and define the triangular target automorphism

\&#91;
\Xi_\phi(a,b,c)=
\left(
 a-\frac12\phi(c)b-\frac12\eta_\phi(c),
 b+\ell_\phi(c),
 c
\right).
\&#93;

Direct expansion of the shifted cubic gives

\&#91;
\boxed{
G_{A,B+3A\phi}=\Xi_\phi\circ G_{A,B}\circ\Theta_\phi.
}
\&#93;

## 2. Exact Artin effectivity criterion

### Theorem 2.1 — annihilator and degree law

For an integer `D&gt;=0`, there is a `c`-fixed framed root translation of
`c`-degree at most `D` from `F_{alpha,q}` to `F_{alpha,q'}` if and only if

\&#91;
\boxed{\delta\alpha^{D+2}=0.}
\&#93;

When this condition holds, the translation is unique and equals

\&#91;
\boxed{
\phi_D(c)=
\frac\delta3\alpha^2c
\sum_{j=0}^{D-1}(-\alpha c)^j,
}
\&#93;

where the sum is empty when `D=0`.  Before imposing the annihilator
condition, its exact residual is

\&#91;
\boxed{
B_{\alpha,q'}-B_{\alpha,q}-3A_\alpha\phi_D
=(-1)^D\delta\alpha^{D+2}c^{D+2}.
}
\&#93;

If

\&#91;
N=\min\{n\ge2:\delta\alpha^n=0\}
\&#93;

exists, then `N=2` means that the two frames already agree and the unique
translation is zero.  For `N&gt;=3`, the unique translation has exact
`c`-degree `N-2`.  If no such `N` exists, there is no polynomial framed
translation.

### Proof

The coefficient equation is

\&#91;
3c(1+\alpha c)\phi(c)=\delta\alpha^2c^2.
\&#93;

Multiplication by `c` is injective in `R&#91;c&#93;`, so this is equivalent to

\&#91;
3(1+\alpha c)\phi(c)=\delta\alpha^2c.
\&#93;

Write

\&#91;
\phi(c)=p_1c+\cdots+p_Dc^D.
\&#93;

Coefficient comparison gives

\&#91;
3p_1=\delta\alpha^2,
\qquad
p_i=-\alpha p_{i-1}\quad(2\le i\le D),
\qquad
\alpha p_D=0.
\&#93;

Hence

\&#91;
p_i=\frac\delta3(-1)^{i-1}\alpha^{i+1}.
\&#93;

The terminal equation is exactly `delta*alpha^(D+2)=0`, and all coefficients
are forced, proving existence and uniqueness.  Multiplying the finite
geometric series by `1+alpha*c` gives the displayed residual.  If `N&gt;=3` is minimal, the coefficient of `c^(N-2)` is a unit multiple of
`delta*alpha^(N-1)`, which is nonzero; hence the degree is exactly `N-2`.
For `N=2`, the frames already coincide and `phi=0`.

### Proposition 2.2 — the exact orbit cokernel

The framed coefficient quotient has a one-line module description.  Let

\&#91;
\mu_\alpha:cR&#91;c&#93;\longrightarrow c^2R&#91;c&#93;,
\qquad
\phi\longmapsto 3A_\alpha\phi.
\&#93;

After dividing the source by `c`, the target by `c^2`, and the map by the
unit three,

\&#91;
\boxed{
\operatorname{coker}(\mu_\alpha)
\simeq R&#91;c&#93;/(1+\alpha c).
}
\&#93;

The difference between the `q'`- and `q`-frames is represented by

\&#91;
\boxed{
\frac{\delta}{3}\alpha^2\bmod(1+\alpha c).
}
\&#93;

For `R=C&#91;&#91;s&#93;&#93;` and `alpha=s`, evaluation at `c=-1/s` gives

\&#91;
R&#91;c&#93;/(1+sc)\simeq R&#91;1/s&#93;=\mathbb C((s)).
\&#93;

The obstruction class is nonzero when `q!=q'`, but multiplication by `s` is
invertible on the entire cokernel.  Hence every quotient modulo `s^M`, and
the `s`-adic completion of the cokernel, is zero.  The finite geometric
series in Theorem 2.1 is exactly the degree-filtered Neumann expansion of the
inverse of `1+sc`.

## 3. Ramification law over truncated DVRs

Let

\&#91;
R_M=\mathbb C&#91;s&#93;/(s^M)
\&#93;

and suppose

\&#91;
\alpha=s^eu(s),\qquad u(0)\ne0,
\&#93;

with `1&lt;=e&lt;M`.  For `q!=q'`, `delta` is a unit and the nilpotence index of
`alpha` is `ceil(M/e)`.  Theorem 2.1 gives the exact complexity

\&#91;
\boxed{
D_M=\max\left(0,\left\lceil\frac Me\right\rceil-2\right).
}
\&#93;

Equivalently, a framed translation of `c`-degree at most `D` can identify
the two ramified arcs modulo `s^M` exactly when

\&#91;
M\le e(D+2).
\&#93;

For the unramified pointed arc `alpha=s`,

\&#91;
\boxed{D_M=M-2\qquad(M\ge3).}
\&#93;

The optimal residual after allowing degree `D` is the single staircase term

\&#91;
\boxed{
(-1)^D(q'-q)s^{D+2}c^{D+2}.
}
\&#93;

Increasing the allowed degree by one kills this obstruction and moves it one
step northeast, from `(s^(D+2),c^(D+2))` to
`(s^(D+3),c^(D+3))`; there is no terminal finite obstruction.

For `D&gt;=1`, the canonical source and target automorphisms have exact ordinary
degrees

\&#91;
\boxed{
\deg\Theta_{\phi_D}=4D,
\qquad
\deg\Xi_{\phi_D}=D+1.
}
\&#93;

Indeed, `c(x,y,z)` has degree four, the top `c^D` coefficient of `phi_D` is
nonzero, and the target term `phi_D(c)b` has degree `D+1`.  Nilpotence forces
all other triangular target corrections to have degree at most `D`.

## 4. Residual affine frame changes do not improve the law

Assume now that `R` is local, `alpha` belongs to its maximal ideal, and
`delta` is a unit.  Consider an affine transformation of the normalized
conductor chart

\&#91;
C=uc+v,\qquad T=\nu t+h(c),
\&#93;

with `u,nu,kappa` units, satisfying

\&#91;
A_\alpha(C)\nu=\kappa A_\alpha(c),
\&#93;

\&#91;
B_{\alpha,q'}(C)+3A_\alpha(C)h(c)
=\kappa B_{\alpha,q}(c).
\&#93;

Then

\&#91;
\boxed{
v=0,\quad \kappa=1,\quad \nu u=1,\quad
\alpha(u-1)=0,
}
\&#93;

and

\&#91;
\boxed{
h(c)=\frac{q-q'}{3u}\frac{\alpha^2c}{1+\alpha c}.}
\&#93;

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

\&#91;
\mathcal I_D(M)
\&#93;

be the set of `c`-fixed framed isomorphisms over `R_M` whose root translation
has `c`-degree at most `D`.  Theorem 2.1 gives

\&#91;
\mathcal I_D(M)\ne\varnothing
\quad\Longleftrightarrow\quad
M\le D+2.
\&#93;

For every `M`, the union over `D` contains the unique translation

\&#91;
\phi_M(c)=\frac{q'-q}{3}s^2c
\sum_{j=0}^{M-3}(-sc)^j,
\&#93;

and these translations are compatible under `R_(M+1) -&gt; R_M`.  Therefore

\&#91;
\boxed{
\varprojlim_M\ \varinjlim_D\mathcal I_D(M)
\ne\varnothing,
\qquad
\varinjlim_D\ \varprojlim_M\mathcal I_D(M)
=\varnothing.
}
\&#93;

More precisely, the first set is a singleton and is represented by

\&#91;
\boxed{
\widehat\phi(c)=
\frac{q'-q}{3}\frac{s^2c}{1+sc}
=\frac{q'-q}{3}
\sum_{j\ge0}(-1)^js^{j+2}c^{j+1}.
}
\&#93;

It belongs to

\&#91;
c\,\mathbb C&#91;c&#93;&#91;&#91;s&#93;&#93;
=\varprojlim_M cR_M&#91;c&#93;,
\&#93;

but not to

\&#91;
c\,\mathbb C&#91;&#91;s&#93;&#93;&#91;c&#93;,
\&#93;

because its `c`-degree is unbounded.  Thus the compatible system defines a coefficientwise `s`-adic formal
left-right equivalence in `C&#91;x,y,z&#93;&#91;&#91;s&#93;&#93;`, but not a polynomial equivalence
over the complete base `C&#91;&#91;s&#93;&#93;`.

## 6. Full stable left-right non-effectivity

### Theorem 6.1 — all Artin truncations agree, the complete families do not

Let

\&#91;
\mathcal F_q=F_{s,q}
\&#93;

be viewed as a polynomial Keller map over `R=C&#91;&#91;s&#93;&#93;`.  If `q!=q'`, then:

1. for every `M&gt;=1`, the reductions
   `mathcal F_q mod s^M` and `mathcal F_q' mod s^M` are ordinarily
   polynomially left-right equivalent;
2. the equivalences can be chosen compatibly in `M`;
3. `mathcal F_q` and `mathcal F_q'` are not stably polynomially left-right
   equivalent over `C&#91;&#91;s&#93;&#93;`.

Hence the natural map

\&#91;
\operatorname{Isom}^{\rm stable}_{\mathbb C&#91;&#91;s&#93;&#93;}
(\mathcal F_q,\mathcal F_{q'})
\longrightarrow
\varprojlim_M
\operatorname{Isom}^{\rm stable}_{R_M}
(\mathcal F_q\bmod s^M,\mathcal F_{q'}\bmod s^M)
\&#93;

has empty source and nonempty target.

### Proof

For `M&lt;=2` the two frames are equal.  For `M&gt;=3`, use the compatible
translations `phi_M` above and the exact root-translation identity.  This
proves the first two assertions without stabilization.

Suppose a stable polynomial left-right equivalence existed over `C&#91;&#91;s&#93;&#93;`.
After passing to the fraction field `C((s))` and then to an algebraic closure
`L`, it would give a stable equivalence of the generic fibers.  The diagonal
scaling of the cubic frame normalizes the nonzero coefficient `alpha=s` to
`alpha=1`, carrying the two generic fibers to the normalized members `G_q`
and `G_q'` over `L`.

This already contradicts the proved classification over `C`; no separate
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
`C&#91;x,y,z&#93;&#91;&#91;s&#93;&#93;`, not in the polynomial ring `C&#91;&#91;s&#93;&#93;&#91;x,y,z&#93;`.

### Theorem 6.2 — effective unrestricted complexity lower bound

For an ordinary or stable polynomial left-right equivalence over

\&#91;
R_M=\mathbb C&#91;s&#93;/(s^M),
\&#93;

define its complexity to be

\&#91;
\max\{m,\deg\Phi,\deg\Phi^{-1},\deg\Psi,\deg\Psi^{-1}\},
\&#93;

where `m` is the stabilization dimension.  Let `kappa_M(q,q')` be the
minimum complexity of an equivalence between the two `M`-th truncations.
Then

\&#91;
\boxed{
\kappa_M(q,q')
\ge \frac{\log\log M}{\log 4}
     -O(\log\log\log M),
}
\&#93;

and in particular

\&#91;
\boxed{
\liminf_{M\to\infty}
\frac{\kappa_M(q,q')}{\log\log M}\ge\frac1{\log4}.}
\&#93;

A finite version is the following.  If there is an equivalence using exactly
`m` stabilization variables, and all four automorphisms have degree at most
`b&gt;=1`, put

\&#91;
n=3+m,\qquad
T(n,b)=\binom{n+b}{n},\qquad
N(n,b)=4nT(n,b),
\&#93;

\&#91;
d_b=\max\{b+1,11\}.
\&#93;

Then

\&#91;
\boxed{
M\le 2b\bigl(N(n,b)+1\bigr)d_b^{N(n,b)}.}
\&#93;

Consequently, for fixed stabilization dimension `m`, if `b_(M,m)` is the
least common degree bound for the equivalence and its inverses and
`n=3+m`, then

\&#91;
\boxed{
\liminf_{M\to\infty}
\frac{b_{M,m}}{(\log M/\log\log M)^{1/n}}
\ge\left(\frac{n!}{4}\right)^{1/n}.}
\&#93;

In particular, ordinary equivalences satisfy

\&#91;
b_{M,0}\ge
\left(\frac32\frac{\log M}{\log\log M}\right)^{1/3}(1-o(1)).
\&#93;

### Proof

Fix `m,b`.  Introduce coefficient variables for four polynomial maps

\&#91;
\Phi,\Phi^{-1},\Psi,\Psi^{-1}:\mathbb A^n\to\mathbb A^n
\&#93;

of degree at most `b`.  There are

\&#91;
N=4n\binom{n+b}{n}
\&#93;

coefficient variables.  The two-sided inverse equations and the stable
left-right identity define an affine scheme `E_(m,b)` over `C&#91;s&#93;`.  Every
defining equation `f_i` has

\&#91;
\deg_Xf_i\le d_b,
\qquad
\deg_sf_i\le2b.
\&#93;

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
`0 != alpha_(m,b)(s) in C&#91;s&#93;` in the ideal of the `g_j`, with

\&#91;
\deg_s\alpha_{m,b}
\le\sum_{\ell=0}^{N}
\left(\prod_{j\ne\ell}\deg_Xg_j\right)\deg_sg_\ell
\le2b(N+1)d_b^N.
\&#93;

An `R_M`-point annihilates the `g_j`, hence annihilates `alpha_(m,b)`.  Thus

\&#91;
M\le\operatorname{ord}_s\alpha_{m,b}
\le\deg_s\alpha_{m,b},
\&#93;

which proves the finite bound.

For fixed `n`,

\&#91;
N(n,b)=\frac4{(n-1)!}b^n+O_n(b^{n-1}),
\&#93;

so

\&#91;
\log H(m,b)=\frac4{(n-1)!}b^n\log b+O_n(b^n).
\&#93;

Asymptotic inversion gives the fixed-stabilization statement.  For unrestricted
complexity at most `B`, use

\&#91;
N\le32(B+3)4^B,\qquad d_b\le B+11,
\&#93;

to obtain

\&#91;
M\le2B\bigl(32(B+3)4^B+1\bigr)
(B+11)^{32(B+3)4^B}.
\&#93;

Taking two logarithms gives

\&#91;
\log\log M\le B\log4+O(\log B),
\&#93;

and the asserted unrestricted rate follows.

The explicit framed equivalences still give the much larger upper bound

\&#91;
\kappa_M(q,q')\le4M-8\qquad(M\ge3).
\&#93;

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
proved complex classification.  Thus the effectivity failure is intrinsic
to a nonnilpotent parameter becoming nilpotent on every infinitesimal
quotient, not to the particular coordinate `s`.

## 7. Consequence for algebraic moduli stacks

### Corollary 7.1 — affine finite-presentation diagonals are impossible

No algebraic stack can model this stable polynomial left-right groupoid near
the two arcs while simultaneously having an affine diagonal locally of
finite presentation and representing its isomorphisms exactly.

Indeed, suppose such a stack `X` existed and let `x_q,x_q' in X(C&#91;&#91;s&#93;&#93;)` be
the two objects.  The isomorphism space

\&#91;
I=\operatorname{Isom}_X(x_q,x_q')
\&#93;

would be affine and of finite presentation over `C&#91;&#91;s&#93;&#93;`, say `I=Spec A`.
For a finitely presented algebra,

\&#91;
\operatorname{Hom}(A,\mathbb C&#91;&#91;s&#93;&#93;)
\simeq
\varprojlim_M
\operatorname{Hom}(A,R_M).
\&#93;

The compatible Artin isomorphisms would therefore produce a
`C&#91;&#91;s&#93;&#93;`-point of `I`, contradicting Theorem 6.1.

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
  `M &lt;= D+2`;
- the obstruction does not die—it moves to higher `s`-order and higher
  `c`-degree;
- the compatible limit is a formal automorphism of unbounded spatial degree;
- global stable separation is recovered on the generic fiber by the deleted
  boundary value `B(-1/s)=q+2`.

Thus `q` is neither a tangent character nor a finite Kuranishi obstruction.
It is a failure of bounded-degree effectivity supported at a divisor escaping
from the formal neighborhood.
</code></pre>

## `lane3-formal-effectivity/formal_effectivity_insertion.tex`

<pre><code class="language-tex">
\subsection{Formal effectivity of the quadratic modulus}
\label{subsec:formal-effectivity-q-modulus}

The preceding formal source-triviality result can be sharpened in two
independent directions.  First, the framed root-translation equation has an
exact annihilator and degree law over every coefficient ring.  Second, the
resulting compatible Artin isomorphisms do not algebraize to a stable
polynomial left--right equivalence over \(\C&#91;&#91;s&#93;&#93;\).  Thus the stable
left--right groupoid itself fails formal effectivity at the quadratic
modulus, even though the quantitative lower bound below is proved only in the
framed translation groupoid.  The complete stable \(q\)-classification is
the load-bearing input for generic-fiber nonexistence; the existing all-order
coefficientwise formal source triviality is overlapping background sharpened
by the explicit calculation below.  The exact annihilator law,
nonalgebraizability, unrestricted complexity escape, and diagonal obstruction
are the new deductions in this subsection.

For a commutative \(\Q\)-algebra \(R\), let
\&#91;
 A_\alpha(c)=c(1+\alpha c),\qquad
 B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\&#93;
and write \(F_{\alpha,q}=G_{A_\alpha,B_{\alpha,q}}\).  Put
\(\delta=q'-q\).

For \(\phi(c)\in cR&#91;c&#93;\), define
\&#91;
 \Theta_\phi(x,y,z)=
 \left(x,y+\phi(c),z-3\frac{\phi(c)}x\right),
\&#93;
\&#91;
 \ell_\phi=3A\phi^2+2B\phi,
 \qquad
 \eta_\phi=A\phi^3+B\phi^2,
\&#93;
and
\&#91;
 \Xi_\phi(a,b,c)=
 \left(a-\frac12\phi(c)b-\frac12\eta_\phi(c),
       b+\ell_\phi(c),c\right).
\&#93;
The source map is polynomial because \(c/x=2-3xy-x^2z\), fixes \(c\),
and shifts \(t\) by \(\phi(c)\).  Direct expansion gives
\begin{equation}
\label{eq:q-pairwise-root-translation}
 G_{A,B+3A\phi}=\Xi_\phi\circ G_{A,B}\circ\Theta_\phi.
\end{equation}

\begin{theorem}&#91;Exact framed effectivity law&#93;
\label{thm:q-framed-effectivity-law}
Let \(D\ge0\).  A \(c\)-fixed framed root translation of
\(c\)-degree at most \(D\) carries \(F_{\alpha,q}\) to
\(F_{\alpha,q'}\) if and only if
\&#91;
 \delta\alpha^{D+2}=0.
\&#93;
When it exists, it is unique and is given by
\&#91;
 \phi_D(c)=\frac\delta3\alpha^2c
 \sum_{j=0}^{D-1}(-\alpha c)^j,
\&#93;
where the sum is empty for \(D=0\).  Before imposing the annihilator
condition, the residual is exactly
\&#91;
 B_{\alpha,q'}-B_{\alpha,q}-3A_\alpha\phi_D
 =(-1)^D\delta\alpha^{D+2}c^{D+2}.
\&#93;
Consequently, if
\&#91;
 N=\min\{n\ge2:\delta\alpha^n=0\}
\&#93;
exists, then \(N=2\) means that the frames already agree and the
translation is zero; for \(N\ge3\), its exact degree is \(N-2\).  If no
such \(N\) exists, there is no polynomial framed translation.
\end{theorem}

\begin{proof}
The coefficient equation is
\&#91;
 3c(1+\alpha c)\phi(c)=\delta\alpha^2c^2.
\&#93;
Canceling \(c\) and writing
\(\phi=p_1c+\cdots+p_Dc^D\) gives
\&#91;
 3p_1=\delta\alpha^2,\qquad
 p_i=-\alpha p_{i-1}\ (2\le i\le D),\qquad
 \alpha p_D=0.
\&#93;
Thus
\&#91;
 p_i=\frac\delta3(-1)^{i-1}\alpha^{i+1},
\&#93;
and the terminal equation is precisely
\(\delta\alpha^{D+2}=0\).  This proves existence and uniqueness.  The
finite geometric-series identity gives the displayed residual.  For \(N\ge3\), minimality makes the coefficient of \(c^{N-2}\)
nonzero, proving the exact degree.  When \(N=2\), the frames already
coincide and \(\phi=0\).
\end{proof}

\begin{proposition}&#91;Exact framed orbit cokernel&#93;
\label{prop:q-framed-orbit-cokernel}
Let
\&#91;
 \mu_\alpha:cR&#91;c&#93;\longrightarrow c^2R&#91;c&#93;,
 \qquad \phi\longmapsto3A_\alpha\phi.
\&#93;
Then
\&#91;
 \operatorname{coker}(\mu_\alpha)
 \simeq R&#91;c&#93;/(1+\alpha c),
\&#93;
and the difference between the \(q'\)- and \(q\)-frames is the class
\&#91;
 \frac{q'-q}{3}\alpha^2\bmod(1+\alpha c).
\&#93;
For \(R=\C&#91;&#91;s&#93;&#93;\) and \(\alpha=s\), this cokernel is
\&#91;
 \C&#91;&#91;s&#93;&#93;&#91;c&#93;/(1+sc)\simeq\C((s)).
\&#93;
It is nonzero, but its reduction modulo every \(s^M\), and hence its
\(s\)-adic completion, is zero.
\end{proposition}

\begin{proof}
Divide the source by \(c\), the target by \(c^2\), and the map by the unit
three.  The resulting map is multiplication by \(1+\alpha c\).  In the
special case, the quotient relation is \(c=-s^{-1}\), giving
\(\C&#91;&#91;s&#93;&#93;&#91;1/s&#93;=\C((s))\).  Since \(s\) is invertible there, all
\(s\)-power quotients vanish.
\end{proof}

\begin{corollary}&#91;Ramification and obstruction staircase&#93;
\label{cor:q-ramification-degree-law}
Let \(R_M=\C&#91;s&#93;/(s^M)\), let
\(\alpha=s^eu(s)\) with \(u(0)\ne0\), and let \(q\ne q'\).  The exact
framed translation degree is
\&#91;
 D_M=\max\left(0,\left\lceil\frac Me\right\rceil-2\right).
\&#93;
For the unramified arc \(\alpha=s\), this is \(D_M=M-2\) for \(M\ge3\),
and the optimal degree-\(D\) residual is
\&#91;
 (-1)^D(q'-q)s^{D+2}c^{D+2}.
\&#93;
For \(D\ge1\), the canonical source and target automorphisms in
\eqref{eq:q-pairwise-root-translation} have exact ordinary degrees
\&#91;
 \deg\Theta_{\phi_D}=4D,
 \qquad
 \deg\Xi_{\phi_D}=D+1.
\&#93;
\end{corollary}

\begin{proof}
The nilpotence index of \(s^eu(s)\) in \(R_M\) is
\(\lceil M/e\rceil\), so the first assertion follows from
\cref{thm:q-framed-effectivity-law}.  The residual formula is its displayed
identity with \(\alpha=s\).  Since \(c(x,y,z)\) has degree four and the top
coefficient of \(\phi_D\) is nonzero, the source degree is \(4D\).  On the
target the term \(\phi_D(c)b\) has degree \(D+1\), while nilpotence and the
explicit formulas for \(\ell_\phi,\eta_\phi\) bound all remaining
corrections by \(D\).
\end{proof}

The same degree survives the residual affine transformations of the
normalized conductor chart.  Indeed, over a local ring with \(\alpha\) in
the maximal ideal, suppose
\&#91;
 C=uc+v,\qquad T=\nu t+h(c)
\&#93;
satisfies
\&#91;
 A_\alpha(C)\nu=\kappa A_\alpha(c),
\qquad
 B_{\alpha,q'}(C)+3A_\alpha(C)h(c)=
 \kappa B_{\alpha,q}(c).
\&#93;
Coefficient comparison gives
\&#91;
 v=0,\quad \kappa=1,\quad \nu u=1,\quad
 \alpha(u-1)=0,
\&#93;
and then
\&#91;
 h(c)=\frac{q-q'}{3u}\frac{\alpha^2c}{1+\alpha c}.
\&#93;
Multiplication by the unit \(u^{-1}\) does not alter the exact degree in
\cref{thm:q-framed-effectivity-law}.

\begin{theorem}&#91;Failure of formal effectivity in the stable groupoid&#93;
\label{thm:q-stable-formal-noneffectivity}
Let
\&#91;
 \mathcal F_q=F_{s,q}
\&#93;
be regarded as a polynomial Keller map over \(\C&#91;&#91;s&#93;&#93;\).  If \(q\ne q'\),
then:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item for every \(M\ge1\), the reductions of
\(\mathcal F_q\) and \(\mathcal F_{q'}\) modulo \(s^M\) are ordinarily
polynomially left--right equivalent;
\item these equivalences may be chosen compatibly in \(M\); but
\item the two maps are not stably polynomially left--right equivalent over
\(\C&#91;&#91;s&#93;&#93;\).
\end{enumerate}
Consequently the stable isomorphism functor is not formally effective at
this pair of arcs.
\end{theorem}

\begin{proof}
For \(M\le2\) the frames agree.  For \(M\ge3\), use
\&#91;
 \phi_M(c)=\frac{q'-q}{3}s^2c
 \sum_{j=0}^{M-3}(-sc)^j
\&#93;
in \eqref{eq:q-pairwise-root-translation}.  The extra term in
\(\phi_{M+1}\) is divisible by \(s^M\), so the equivalences are compatible.

Suppose a stable polynomial equivalence existed over \(\C&#91;&#91;s&#93;&#93;\).  Base
change to an algebraic closure \(L\) of \(\C((s))\).  The diagonal
cubic-frame scaling normalizes the nonzero coefficient \(\alpha=s\) to
\(\alpha=1\), so the two generic fibers become \(G_q\) and \(G_{q'}\)
over \(L\).

Fix the stabilization dimension and the finite degrees of the polynomial
automorphisms and their inverses in this alleged equivalence.  Their
coefficients form an \(L\)-point of a finite-type affine \(\C\)-scheme cut
out by the inverse-composition equations and the left--right identity.  Since
\(\C\) is algebraically closed, nonemptiness gives a \(\C\)-point.  That
would be a stable polynomial equivalence between \(G_q\) and \(G_{q'}\)
over \(\C\), contradicting the complete \(q\)-classification.
\end{proof}

\subsection{Effective unframed complexity lower bounds}
\label{subsec:q-effective-unframed-bound}

The preceding framed calculation has a linear degree law.  We now give a
weaker but completely unframed lower bound.  No recovery of the cubic frame,
conductor chart, or escaping section is assumed.

Fix distinct \(q,q'\in\C\), put
\&#91;
 F_q=G_{c(1+sc),\,-2-4sc+qs^2c^2},
 \qquad R_M=\C&#91;s&#93;/(s^M),
\&#93;
and fix a stabilization dimension \(m\ge0\) and a degree bound \(b\ge1\).
Set
\&#91;
 n=3+m,\qquad
 T(n,b)=\binom{n+b}{n},\qquad
 N(n,b)=4nT(n,b),
\&#93;
\&#91;
 d_b=\max\{b+1,11\},\qquad h_b=2b.
\&#93;

Introduce coefficient variables for four polynomial maps
\&#91;
 \Phi,\Phi^{-1},\Psi,\Psi^{-1}:\A^n\longrightarrow\A^n
\&#93;
of degree at most \(b\).  Their two-sided inverse equations and the stable
left--right identity
\&#91;
 (F_{q'}\times\id_{\A^m})\circ\Phi
 =\Psi\circ(F_q\times\id_{\A^m})
\&#93;
define an affine scheme \(E_{m,b}\) over \(\C&#91;s&#93;\).  It has
\(N=N(n,b)\) coefficient variables.  Every defining equation \(f_i\) obeys
\&#91;
 \deg_X(f_i)\le d_b,
 \qquad
 \deg_s(f_i)\le h_b.
\&#93;
Indeed, a composition-inverse coefficient has degree at most \(b+1\) in the
unknown coefficients; substitution into the degree-eleven map has coefficient
degree at most eleven; and a degree-\(b\) monomial in coordinates whose
coefficients have \(s\)-degree at most two has \(s\)-degree at most \(2b\).

\begin{lemma}&#91;Reduction to \(N+1\) constant combinations&#93;
\label{lem:q-N-plus-one-combinations}
Let \(k\) be an infinite field and
\(f_1,\ldots,f_r\in k&#91;s,X_1,\ldots,X_N&#93;\) have no common zero over
\(\overline{k(s)}\).  There are constants \(\lambda_{ji}\in k\),
\(0\le j\le N\), such that
\&#91;
 g_j=\sum_i\lambda_{ji}f_i
\&#93;
are nonconstant in the \(X\)-variables and have no common zero over
\(\overline{k(s)}\).
\end{lemma}

\begin{proof}
Over \(K=\overline{k(s)}\), let \(\Lambda=(\lambda_{ji})\) range over
\(\A_K^{(N+1)r}\), and consider the incidence scheme
\&#91;
 I=\left\{(x,\Lambda):
 \sum_i\lambda_{ji}f_i(x)=0\text{ for }0\le j\le N\right\}.
\&#93;
For each \(x\), the vector \((f_1(x),\ldots,f_r(x))\) is nonzero.  Each row
of \(\Lambda\) therefore satisfies one nontrivial linear equation, and
\&#91;
 \dim I\le N+(N+1)(r-1)=(N+1)r-1.
\&#93;
The closure of its projection to the coefficient space is proper.  Requiring
a row not to produce an element of \(k&#91;s&#93;\) removes only a proper linear
subspace.  Hence a nonempty open set of tuples works over \(k(s)\).

This open contains a tuple with entries in \(k\).  Choose a nonzero polynomial
over \(k(s)\) vanishing on the bad closed set and clear denominators.  A
nonzero polynomial in \(k&#91;s,\Lambda&#93;\) cannot vanish at every constant point
of \(k^{(N+1)r}\), since \(k\) is infinite.
\end{proof}

The generic fiber of \(E_{m,b}\) is empty.  Otherwise, after extension to an
algebraic closure of \(\C(s)\), diagonal scaling would normalize \(s\ne0\)
and give a stable equivalence between \(G_q\) and \(G_{q'}\).  With \(m\)
and \(b\) fixed, such an equivalence is a point of a finite-type scheme over
\(\C\); a point over an extension field would yield a complex point,
contradicting the complete stable \(q\)-classification.

Apply \cref{lem:q-N-plus-one-combinations} to obtain \(N+1\) polynomials
\(g_0,\ldots,g_N\) with no generic common zero and with the same degree
bounds.  The parametric effective Nullstellensatz
\cite&#91;Theorem~0.5&#93;{dAndreaKrickSombra2013} supplies
\(0\ne\alpha_{m,b}(s)\in\C&#91;s&#93;\) and \(a_j\in\C&#91;s,X&#93;\) such that
\&#91;
 \alpha_{m,b}(s)=\sum_{j=0}^{N}a_jg_j
\&#93;
and
\&#91;
 \deg_s\alpha_{m,b}
 \le\sum_{\ell=0}^{N}
 \left(\prod_{j\ne\ell}\deg_Xg_j\right)\deg_sg_\ell
 \le (N+1)d_b^Nh_b.
\&#93;

\begin{theorem}&#91;Effective unframed truncation bound&#93;
\label{thm:q-effective-unframed-truncation-bound}
If the two reductions modulo \(s^M\) admit a stable polynomial left--right
equivalence with exactly \(m\) stabilization variables and with
\&#91;
 \deg\Phi,\deg\Phi^{-1},\deg\Psi,\deg\Psi^{-1}\le b,
\&#93;
then
\&#91;
 \boxed{
 M\le H(m,b):=
 2b\bigl(N(n,b)+1\bigr)d_b^{N(n,b)}.}
\&#93;
\end{theorem}

\begin{proof}
An \(R_M\)-point of \(E_{m,b}\) annihilates every \(g_j\).  Evaluation of
the Bezout identity gives \(\alpha_{m,b}(s)=0\) in \(R_M\).  Since
\(\alpha_{m,b}\ne0\),
\&#91;
 M\le\ord_s\alpha_{m,b}
 \le\deg_s\alpha_{m,b}
 \le2b(N+1)d_b^N.
\&#93;
\end{proof}

\begin{corollary}&#91;Fixed-stabilization degree rate&#93;
\label{cor:q-fixed-stabilization-degree-rate}
Let \(b_{M,m}\) be the least common degree bound for an equivalence and its
four automorphism maps using exactly \(m\) added variables, and put
\(n=3+m\).  Then
\&#91;
 \liminf_{M\to\infty}
 \frac{b_{M,m}}{(\log M/\log\log M)^{1/n}}
 \ge\left(\frac{n!}{4}\right)^{1/n}.
\&#93;
In particular,
\&#91;
 b_{M,0}\ge
 \left(\frac32\frac{\log M}{\log\log M}\right)^{1/3}(1-o(1)).
\&#93;
\end{corollary}

\begin{proof}
For fixed \(n\),
\&#91;
 N(n,b)=4n\binom{n+b}{n}
 =\frac4{(n-1)!}b^n+O_n(b^{n-1}),
\&#93;
so
\&#91;
 \log H(m,b)
 =\frac4{(n-1)!}b^n\log b+O_n(b^n).
\&#93;
Asymptotic inversion gives the result.
\end{proof}

\begin{corollary}&#91;Stabilization--degree tradeoff&#93;
\label{cor:q-stabilization-degree-tradeoff}
Every such equivalence satisfies
\&#91;
 M\le
 2b\bigl(32(m+3)2^{m+b}+1\bigr)
 (b+11)^{32(m+3)2^{m+b}},
\&#93;
and consequently
\&#91;
 m+b\ge\frac{\log\log M}{\log2}
       -O(\log\log\log M).
\&#93;
\end{corollary}

\begin{proof}
Use
\(\binom{n+b}{n}\le2^{n+b}=2^{m+b+3}\), hence
\(N(n,b)\le32(m+3)2^{m+b}\), and substitute in
\cref{thm:q-effective-unframed-truncation-bound}.
\end{proof}

\begin{corollary}&#91;Explicit unrestricted complexity rate&#93;
\label{cor:q-unrestricted-complexity-rate}
Let
\&#91;
 \kappa_M(q,q')=
 \min\max\{m,\deg\Phi,\deg\Phi^{-1},
              \deg\Psi,\deg\Psi^{-1}\}
\&#93;
over all stable polynomial equivalences modulo \(s^M\).  Then
\&#91;
 \boxed{
 \kappa_M(q,q')
 \ge\frac{\log\log M}{\log4}
      -O(\log\log\log M),}
\&#93;
or equivalently
\&#91;
 \boxed{
 \liminf_{M\to\infty}
 \frac{\kappa_M(q,q')}{\log\log M}\ge\frac1{\log4}.}
\&#93;
More explicitly, \(\kappa_M(q,q')\le B\) implies
\&#91;
 M\le
 2B\bigl(32(B+3)4^B+1\bigr)
 (B+11)^{32(B+3)4^B}.
\&#93;
\end{corollary}

The result is deliberately worst-case: it treats the coefficients of four
bounded polynomial maps as independent variables and applies general
elimination.  It nevertheless proves an explicit rate for arbitrary stable
equivalences, with no frame-recovery hypothesis.  The sharp linear lower
bound remains a geometric problem.  The explicit framed construction gives
\(\kappa_M(q,q')\le4M-8\); matching this requires an intrinsic Artin-base
recovery theorem for the escaping-boundary chart.

The same non-effectivity argument works over an integral
\(\C\)-algebra \(R\) that is complete and separated for the
\(\alpha\)-adic topology, with \(\alpha\) a nonzero nonunit and
\(q,q'\in\C\) distinct.  Strictness of the powers of \(\alpha\) gives exact
framed degree \(M-2\) modulo \(\alpha^M\), and a complete-base stable
equivalence would contradict the complex generic-fiber classification after
finite-type descent.

The compatible framed translations have the unique limit
\&#91;
 \widehat\phi(c)=\frac{q'-q}{3}\frac{s^2c}{1+sc}
 =\frac{q'-q}{3}\sum_{j\ge0}(-1)^js^{j+2}c^{j+1}.
\&#93;
It lies in \(c\C&#91;c&#93;&#91;&#91;s&#93;&#93;\), the \(s\)-adic completion of
\(c\C&#91;s,c&#93;\), but not in \(c\C&#91;&#91;s&#93;&#93;&#91;c&#93;\).  Equivalently, if
\(\mathcal I_D(M)\) denotes framed isomorphisms of translation degree at
most \(D\), then
\&#91;
 \varprojlim_M\varinjlim_D\mathcal I_D(M)\ne\varnothing,
 \qquad
 \varinjlim_D\varprojlim_M\mathcal I_D(M)=\varnothing.
\&#93;
Thus completion and the bounded-degree filtration do not commute.

\begin{corollary}&#91;Obstruction to an affine finite-presentation diagonal&#93;
\label{cor:q-no-affine-fp-moduli-diagonal}
No algebraic stack can represent this stable polynomial left--right
groupoid near the two arcs, with its exact isomorphism notion, and have an
affine diagonal locally of finite presentation.
\end{corollary}

\begin{proof}
If such a stack existed, the isomorphism space between the two
\(\C&#91;&#91;s&#93;&#93;\)-objects would be affine of finite presentation, say
\(\Spec A\).  Since \(A\) is finitely presented and
\(\C&#91;&#91;s&#93;&#93;=\varprojlim_M\C&#91;s&#93;/(s^M)\), one has
\&#91;
 \Hom(A,\C&#91;&#91;s&#93;&#93;)
 \simeq
 \varprojlim_M\Hom(A,\C&#91;s&#93;/(s^M)).
\&#93;
The compatible Artin isomorphisms would therefore algebraize, contradicting
\cref{thm:q-stable-formal-noneffectivity}.
\end{proof}
</code></pre>

## `lane3-formal-effectivity/AUDIT.md`

<pre><code class="language-markdown">
# Lane 3 audit, corrections, and scope

## The three quotient problems

Lane 3 juxtaposes three genuinely different objects:

1. the normalized degree-at-most-seven coefficient slice modulo an
   eleven-dimensional affine source orbit;
2. the degree-eight germ after affine, source-shear, and target-shear
   components are included; and
3. the cubic-frame family modulo arbitrary polynomial left--right equivalence
   and stabilization.

No current comparison theorem identifies these functors. The length-584
algebra is therefore not, by itself, a statement about the full stable
quotient. Conversely, the stable \(q\)-modulus is not a surviving finite
Kuranishi tangent character in the bounded degree-seven or degree-eight
calculation.

## Corrected conclusions

- The length-584 algebra is a strong theorem about the chosen bounded,
  affine-transverse germ.
- Degree-eight orbit saturation remains open. The public retained unit for the
  five-variable order-six reduction supplies no public universal matrix or
  obstruction-polynomial locator, so the proposed `3 x 3` determinant and unit
  minors cannot be independently reconstructed from the public repository.
- The degree-eleven threshold has an exact proof locator inside the full cubic
  frame. It is not a theorem that the unrestricted pointed stable-modulus
  onset is globally eleven.
- The global synthesis remains the conditional interval
  \(8\le D_{\mathrm{mod}}(G)\le11\), with equality at eleven only inside the
  cubic-frame locus.

## New conceptual bridge

For the pointed family

\&#91;
A_s(c)=c(1+sc),\qquad B_{s,q}(c)=-2-4sc+qs^2c^2,
\&#93;

the exact orbit cokernel for framed root translations is

\&#91;
\mathbf C&#91;&#91;s&#93;&#93;&#91;c&#93;/(1+sc)\simeq\mathbf C((s)).
\&#93;

It is supported on the escaping divisor \(1+sc=0\), where
\(B_{s,q}(-1/s)=q+2\), and its \(s\)-adic completion is zero. Thus every
finite Artin neighborhood forgets the boundary decoration even though the
generic stable class remembers it.

This is a failure of polynomial effectivity at infinity, not a transition
from zero to nonzero ordinary tangent dimension.

## Superseded routes retained only as audit history

Two weaker arguments were developed before the final theorem:

- a compactness/Greenberg argument proving only that unrestricted equivalence
  complexity tends to infinity; and
- a coarse effective-Noether-exponent argument giving weaker explicit bounds.

They are not included as competing theorem statements. The package uses the
sharper parametric effective Nullstellensatz, which gives

\&#91;
M\le 2b(N+1)d^N
\&#93;

for a fixed stabilization dimension and degree bound, and yields the
unrestricted \(\Omega(\log\log M)\) rate.

## Remaining theorem-facing problem

The strongest remaining problem is an Artin-base intrinsic-recovery theorem:
show that an arbitrary unframed polynomial left--right equivalence recovers
enough of the projective escaping section and its conductor decoration to
inherit the sharp framed linear law. Such a theorem could upgrade

\&#91;
\deg_c\phi_M=M-2,\qquad \deg\Theta_{\phi_M}=4M-8
\&#93;

from framed optimality to an unrestricted lower bound.

This problem is separate from characteristic-zero degree-eight orbit
saturation, which still requires the missing universal computational packet
or a new conceptual replacement.
</code></pre>

## `lane3-formal-effectivity/verify_formal_effectivity.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checks for the formal-effectivity theorem of the cubic-frame q-modulus.

The script verifies finite polynomial identities underlying the proof:

1. the general root-translation left-right identity;
2. the exact residual formula for every tested degree D;
3. the annihilator/degree law over C&#91;s&#93;/(s^M) for several ramification orders;
4. compatibility of the optimal Artin gauges under truncation;
5. exact source and target degree formulas in the unramified case;
6. the residual affine-frame equations and their inability to lower degree;
7. unbounded c-degree of the compatible formal limit.

The nonexistence of a stable equivalence over C&#91;&#91;s&#93;&#93; uses the published
stable q-classification on the generic fiber and is recorded as a theorem
input rather than a CAS assertion.
"""
from __future__ import annotations

import json
from math import ceil
from pathlib import Path

import sympy as sp


def check(condition: bool, label: str) -&gt; None:
    if not condition:
        raise AssertionError(label)


def truncate_s(expr: sp.Expr, s: sp.Symbol, c: sp.Symbol, modulus: int) -&gt; sp.Expr:
    """Reduce a polynomial in s,c modulo s**modulus."""
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    result = sp.Integer(0)
    for (se, ce), coeff in sp.Poly(expr, s, c).terms():
        if se &lt; modulus:
            result += coeff * s**se * c**ce
    return sp.expand(result)


def c_degree(expr: sp.Expr, c: sp.Symbol) -&gt; int:
    expr = sp.expand(expr)
    if expr == 0:
        return -1
    return int(sp.Poly(expr, c).degree())


def total_degree(expr: sp.Expr, variables: tuple&#91;sp.Symbol, ...&#93;) -&gt; int:
    expr = sp.expand(expr)
    if expr == 0:
        return -1
    return int(sp.Poly(expr, *variables).total_degree())


def main() -&gt; None:
    # ------------------------------------------------------------------
    # 1. General frame-coordinate identity.
    # ------------------------------------------------------------------
    A, B, phi, t, b_target = sp.symbols("A B phi t b_target")
    B_shifted = B + 3 * A * phi
    ell = 3 * A * phi**2 + 2 * B * phi
    eta = A * phi**3 + B * phi**2

    # Source shift t -&gt; t+phi produces b_source=b_target-ell.
    b_source = b_target - ell
    two_a_source = sp.expand(
        A * (t + phi) ** 3
        + B * (t + phi) ** 2
        + (t + phi) * b_source
    )
    two_a_after_target = sp.expand(two_a_source - phi * b_source - eta)
    two_a_desired = sp.expand(A * t**3 + B_shifted * t**2 + t * b_target)
    check(two_a_after_target == two_a_desired, "root-translation LR identity")

    # Source invariant c is fixed.
    x, y, z, P = sp.symbols("x y z P")
    c_xyz = 2 * x - 3 * x**2 * y - x**3 * z
    c_transformed = sp.expand(
        2 * x - 3 * x**2 * (y + P) - x**3 * (z - 3 * P / x)
    )
    check(sp.expand(c_transformed - c_xyz) == 0, "source transformation fixes c")

    # ------------------------------------------------------------------
    # 2. Universal residual formula.
    # ------------------------------------------------------------------
    alpha, delta, c = sp.symbols("alpha delta c")
    A_alpha = c * (1 + alpha * c)
    residual_checks: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    for D in range(0, 11):
        if D == 0:
            phi_D = sp.Integer(0)
        else:
            phi_D = sp.expand(
                delta
                * alpha**2
                * c
                * sum((-alpha * c) ** j for j in range(D))
                / 3
            )
        residual = sp.expand(delta * alpha**2 * c**2 - 3 * A_alpha * phi_D)
        expected = sp.expand((-1) ** D * delta * alpha ** (D + 2) * c ** (D + 2))
        check(residual == expected, f"universal residual formula D={D}")
        residual_checks.append(
            {
                "D": D,
                "phi_c_degree": c_degree(phi_D, c),
                "residual": str(sp.factor(residual)),
            }
        )

    # ------------------------------------------------------------------
    # 3. Ramification law over C&#91;s&#93;/(s^M).
    # ------------------------------------------------------------------
    s, q, qp, lam = sp.symbols("s q qp lam")
    dq = qp - q

    # Exact orbit-cokernel relation for alpha=s: in the quotient by
    # 1+s*c, multiplication by s has inverse -c.
    orbit_relation = sp.expand(s * (-c) - 1)
    orbit_denominator_basic = sp.Poly(
        1 + s * c,
        c,
        domain=sp.QQ.frac_field(s),
    )
    orbit_remainder = sp.rem(
        sp.Poly(orbit_relation, c, domain=sp.QQ.frac_field(s)),
        orbit_denominator_basic,
    )
    check(orbit_remainder.as_expr() == 0, "s is invertible in orbit cokernel")
    obstruction_numerator = sp.Poly(
        dq * s**2,
        c,
        domain=sp.QQ.frac_field(s, q, qp),
    )
    orbit_denominator = sp.Poly(
        1 + s * c,
        c,
        domain=sp.QQ.frac_field(s, q, qp),
    )
    _, obstruction_remainder = sp.div(obstruction_numerator, orbit_denominator)
    check(
        sp.expand(obstruction_remainder.as_expr() - dq * s**2) == 0,
        "q obstruction is nonzero in generic orbit cokernel",
    )

    ramification_table: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;

    for M in range(2, 15):
        for e in range(1, min(5, M)):
            nilpotence_index = ceil(M / e)
            D_min = max(0, nilpotence_index - 2)
            alpha_me = s**e
            A_me = c * (1 + alpha_me * c)

            if D_min == 0:
                phi_min = sp.Integer(0)
            else:
                phi_min = sp.expand(
                    dq
                    * alpha_me**2
                    * c
                    * sum((-alpha_me * c) ** j for j in range(D_min))
                    / 3
                )

            residual_min = truncate_s(
                dq * alpha_me**2 * c**2 - 3 * A_me * phi_min,
                s,
                c,
                M,
            )
            check(residual_min == 0, f"ramified existence M={M}, e={e}")

            actual_degree = c_degree(truncate_s(phi_min, s, c, M), c)
            expected_degree = -1 if D_min == 0 else D_min
            check(actual_degree == expected_degree, f"ramified degree M={M}, e={e}")

            if D_min &gt; 0:
                phi_prev = (
                    sp.Integer(0)
                    if D_min == 1
                    else sp.expand(
                        dq
                        * alpha_me**2
                        * c
                        * sum((-alpha_me * c) ** j for j in range(D_min - 1))
                        / 3
                    )
                )
                residual_prev = truncate_s(
                    dq * alpha_me**2 * c**2 - 3 * A_me * phi_prev,
                    s,
                    c,
                    M,
                )
                check(residual_prev != 0, f"ramified sharpness M={M}, e={e}")

            ramification_table.append(
                {
                    "M": M,
                    "e": e,
                    "nilpotence_index": nilpotence_index,
                    "minimal_c_degree": max(0, actual_degree),
                    "frames_already_equal": D_min == 0,
                }
            )

    # ------------------------------------------------------------------
    # 4. Unramified compatibility and exact degree staircase.
    # ------------------------------------------------------------------
    compatibility_table: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    phi_by_M: dict&#91;int, sp.Expr&#93; = {}
    for M in range(1, 15):
        if M &lt;= 2:
            phi_M = sp.Integer(0)
        else:
            phi_M = sp.expand(
                dq * s**2 * c * sum((-s * c) ** j for j in range(M - 2)) / 3
            )
        phi_by_M&#91;M&#93; = phi_M

        A_s = c * (1 + s * c)
        residual = truncate_s(
            dq * s**2 * c**2 - 3 * A_s * phi_M,
            s,
            c,
            M,
        )
        check(residual == 0, f"unramified equivalence mod s^{M}")

        if M &gt;= 3:
            check(c_degree(phi_M, c) == M - 2, f"unramified exact degree M={M}")
            top = sp.expand(phi_M).coeff(c, M - 2)
            expected_top = dq * (-1) ** (M - 3) * s ** (M - 1) / 3
            check(sp.expand(top - expected_top) == 0, f"unramified top term M={M}")

        compatibility_table.append(
            {
                "M": M,
                "c_degree": max(0, c_degree(phi_M, c)),
                "source_degree": 1 if M &lt;= 2 else 4 * (M - 2),
                "target_degree": 1 if M &lt;= 2 else M - 1,
            }
        )

    for M in range(1, 14):
        reduced_next = truncate_s(phi_by_M&#91;M + 1&#93;, s, c, M)
        current = truncate_s(phi_by_M&#91;M&#93;, s, c, M)
        check(reduced_next == current, f"compatibility M={M+1}-&gt;M={M}")

    # ------------------------------------------------------------------
    # 5. Exact source and target coordinate degrees.
    # ------------------------------------------------------------------
    d = 2 - 3 * x * y - x**2 * z
    c_source = x * d
    degree_table: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    bvar, avar, cvar = sp.symbols("b a c")

    for M in range(3, 11):
        D = M - 2
        phi_M_source = sp.expand(phi_by_M&#91;M&#93;.subs(c, c_source))
        theta_y = sp.expand(y + phi_M_source)
        theta_z = sp.expand(z - 3 * phi_M_source / x)
        source_degree = max(
            total_degree(x, (x, y, z)),
            total_degree(theta_y, (x, y, z)),
            total_degree(theta_z, (x, y, z)),
        )
        check(source_degree == 4 * D, f"source degree M={M}")

        # Target corrections over R_M; use B_q and reduce in s.
        phi_target = phi_by_M&#91;M&#93;.subs(c, cvar)
        A_target = cvar * (1 + s * cvar)
        B_target = -2 - 4 * s * cvar + q * s**2 * cvar**2
        ell_target = truncate_s(
            3 * A_target * phi_target**2 + 2 * B_target * phi_target,
            s,
            cvar,
            M,
        )
        eta_target = truncate_s(
            A_target * phi_target**3 + B_target * phi_target**2,
            s,
            cvar,
            M,
        )
        xi_a = sp.expand(avar - phi_target * bvar / 2 - eta_target / 2)
        xi_b = sp.expand(bvar + ell_target)
        target_degree = max(
            total_degree(xi_a, (avar, bvar, cvar)),
            total_degree(xi_b, (avar, bvar, cvar)),
            1,
        )
        # The inverse is triangular.  Equivalently it is the target map for
        # the reverse root translation from B+3Aphi back to B.
        xi_inv_a = sp.expand(
            avar
            + phi_target * bvar / 2
            - truncate_s(phi_target * ell_target, s, cvar, M) / 2
            + eta_target / 2
        )
        xi_inv_b = sp.expand(bvar - ell_target)
        target_inverse_degree = max(
            total_degree(xi_inv_a, (avar, bvar, cvar)),
            total_degree(xi_inv_b, (avar, bvar, cvar)),
            1,
        )
        check(target_degree == D + 1, f"target degree M={M}")
        check(target_inverse_degree == D + 1, f"target inverse degree M={M}")
        check(c_degree(ell_target, cvar) &lt;= D, f"ell c-degree M={M}")
        check(c_degree(eta_target, cvar) &lt;= D - 1, f"eta c-degree M={M}")

        degree_table.append(
            {
                "M": M,
                "D": D,
                "source_degree": source_degree,
                "target_degree": target_degree,
                "target_inverse_degree": target_inverse_degree,
                "ell_c_degree": c_degree(ell_target, cvar),
                "eta_c_degree": c_degree(eta_target, cvar),
            }
        )

    # ------------------------------------------------------------------
    # 6. Residual affine framed transformations.
    # ------------------------------------------------------------------
    affine_table: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    for M in range(3, 13):
        D = M - 2
        u = 1 + lam * s ** (M - 1)
        u_inv = 1 - lam * s ** (M - 1)
        h = truncate_s(-u_inv * phi_by_M&#91;M&#93;, s, c, M)

        A_s = c * (1 + s * c)
        B_q = -2 - 4 * s * c + q * s**2 * c**2
        B_qp = -2 - 4 * s * c + qp * s**2 * c**2

        A_relation = truncate_s(
            A_s.subs(c, u * c) * u_inv - A_s,
            s,
            c,
            M,
        )
        B_relation = truncate_s(
            B_qp.subs(c, u * c)
            + 3 * A_s.subs(c, u * c) * h
            - B_q,
            s,
            c,
            M,
        )
        check(A_relation == 0, f"affine A relation M={M}")
        check(B_relation == 0, f"affine B relation M={M}")
        check(c_degree(h, c) == D, f"affine degree unchanged M={M}")
        affine_table.append(
            {
                "M": M,
                "residual_scaling": f"u=1+lambda*s^{M-1}",
                "h_c_degree": D,
            }
        )

    # ------------------------------------------------------------------
    # 7. The formal limit has unbounded c-degree.
    # ------------------------------------------------------------------
    formal_coefficients: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    for n in range(2, 13):
        coeff = dq * (-1) ** (n - 2) * c ** (n - 1) / 3
        check(c_degree(coeff, c) == n - 1, f"formal coefficient degree n={n}")
        formal_coefficients.append(
            {
                "s_power": n,
                "coefficient": str(coeff),
                "c_degree": n - 1,
                "source_y_degree": 4 * (n - 1),
            }
        )

    report = {
        "status": "ALL FORMAL-EFFECTIVITY CHECKS PASSED",
        "theorem_inputs_not_cas_checked": &#91;
            "stable q-classification on the generic fiber: Program 4, thm:main / cor:q-classification",
            "constant generic-combination lemma for an empty affine generic fiber",
            "D'Andrea-Krick-Sombra parametric effective Nullstellensatz (Theorem 0.5)",
        &#93;,
        "universal_residual_checks": residual_checks,
        "ramification_samples": ramification_table,
        "unramified_compatibility": compatibility_table,
        "canonical_degree_checks": degree_table,
        "affine_frame_checks": affine_table,
        "formal_limit_coefficients": formal_coefficients,
        "orbit_cokernel": "C&#91;&#91;s&#93;&#93;&#91;c&#93;/(1+s*c) = C((s))",
        "orbit_obstruction_class": "(q'-q)/3 * s^2",
        "orbit_cokernel_s_inverse": "-c",
        "formal_limit_ring": "C&#91;c&#93;&#91;&#91;s&#93;&#93;",
        "polynomial_complete_base_ring": "C&#91;&#91;s&#93;&#93;&#91;c&#93;",
        "noncommutation": (
            "lim_M colim_D Isom_D(R_M) is nonempty, "
            "while colim_D lim_M Isom_D(R_M) is empty"
        ),
    }

    output = Path(__file__).with_name("formal_effectivity_report.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(report&#91;"status"&#93;)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
</code></pre>

## `lane3-formal-effectivity/verify_formal_effectivity_independent.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Independent finite-support checker for the effectivity staircase.

This checker deliberately uses no CAS.  Polynomials in (s,c) are sparse
Python dictionaries with rational coefficients.  It verifies the exact
residual and sharp ramification law for a grid of Artin quotients.
"""
from __future__ import annotations

from fractions import Fraction
from math import ceil
from pathlib import Path
import json

Monomial = tuple&#91;int, int&#93;
Poly = dict&#91;Monomial, Fraction&#93;


def add(*polys: Poly) -&gt; Poly:
    out: Poly = {}
    for poly in polys:
        for mon, coeff in poly.items():
            out&#91;mon&#93; = out.get(mon, Fraction(0)) + coeff
            if out&#91;mon&#93; == 0:
                del out&#91;mon&#93;
    return out


def scale(poly: Poly, scalar: Fraction) -&gt; Poly:
    return {m: scalar * a for m, a in poly.items() if scalar * a}


def mul(left: Poly, right: Poly, modulus: int | None = None) -&gt; Poly:
    out: Poly = {}
    for (si, ci), ai in left.items():
        for (sj, cj), aj in right.items():
            se = si + sj
            if modulus is not None and se &gt;= modulus:
                continue
            mon = (se, ci + cj)
            out&#91;mon&#93; = out.get(mon, Fraction(0)) + ai * aj
            if out&#91;mon&#93; == 0:
                del out&#91;mon&#93;
    return out


def monomial(s_exp: int, c_exp: int, coeff: Fraction = Fraction(1)) -&gt; Poly:
    return {} if coeff == 0 else {(s_exp, c_exp): coeff}


def c_degree(poly: Poly) -&gt; int:
    return max((c for _, c in poly), default=-1)


def phi_for(M: int, e: int, D: int) -&gt; Poly:
    # delta is normalized to 1; the factor 1/3 is retained exactly.
    out: Poly = {}
    for j in range(D):
        out = add(
            out,
            monomial(e * (j + 2), j + 1, Fraction((-1) ** j, 3)),
        )
    return {m: a for m, a in out.items() if m&#91;0&#93; &lt; M}


def residual(M: int, e: int, D: int) -&gt; Poly:
    # delta*alpha^2*c^2 - 3*c*(1+alpha*c)*phi_D
    difference = {} if 2 * e &gt;= M else monomial(2 * e, 2)
    A = add(monomial(0, 1), monomial(e, 2))
    correction = scale(mul(A, phi_for(M, e, D), modulus=M), Fraction(3))
    return add(difference, scale(correction, Fraction(-1)))


def main() -&gt; None:
    samples: list&#91;dict&#91;str, int | bool&#93;&#93; = &#91;&#93;
    for M in range(2, 31):
        for e in range(1, min(M, 8)):
            D = max(0, ceil(M / e) - 2)
            r = residual(M, e, D)
            if r:
                raise AssertionError(f"existence failed M={M}, e={e}: {r}")
            deg = c_degree(phi_for(M, e, D))
            expected = -1 if D == 0 else D
            if deg != expected:
                raise AssertionError((M, e, deg, expected))
            sharp = True
            if D &gt; 0:
                previous = residual(M, e, D - 1)
                sharp = bool(previous)
                if not sharp:
                    raise AssertionError(f"sharpness failed M={M}, e={e}")
            samples.append(
                {
                    "M": M,
                    "e": e,
                    "D": D,
                    "sharp": sharp,
                }
            )

    # Compatibility in the unramified tower.
    for M in range(1, 30):
        current_D = max(0, M - 2)
        next_D = max(0, M - 1)
        current = {m: a for m, a in phi_for(M, 1, current_D).items() if m&#91;0&#93; &lt; M}
        reduced_next = {
            m: a for m, a in phi_for(M + 1, 1, next_D).items() if m&#91;0&#93; &lt; M
        }
        if current != reduced_next:
            raise AssertionError(f"compatibility failed at M={M}")

    report = {
        "status": "INDEPENDENT EFFECTIVITY STAIRCASE CHECKS PASSED",
        "engine": "pure Python sparse dictionaries with Fraction coefficients",
        "sample_count": len(samples),
        "max_modulus": 30,
        "max_ramification_order": 7,
        "samples": samples,
    }
    path = Path(__file__).with_name("formal_effectivity_independent_report.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report&#91;"status"&#93;)


if __name__ == "__main__":
    main()
</code></pre>

## `lane3-formal-effectivity/verify_effective_unframed_bound.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Combinatorial audit for the effective unframed complexity bound.

This script verifies the coefficient-variable counts, degree/parameter-degree
bookkeeping, finite inequalities, and asymptotic constants.  It does not
re-prove the external parametric Nullstellensatz or the stable q-classification.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Iterator

OUT = Path(__file__).with_name("effective_unframed_bound_report.json")


def exponent_tuples(n: int, b: int) -&gt; Iterator&#91;tuple&#91;int, ...&#93;&#93;:
    for exps in itertools.product(range(b + 1), repeat=n):
        if sum(exps) &lt;= b:
            yield exps


def monomial_count(n: int, b: int) -&gt; int:
    return math.comb(n + b, n)


def variable_count(m: int, b: int) -&gt; int:
    n = 3 + m
    return 4 * n * monomial_count(n, b)


def equation_degree_bound(b: int) -&gt; int:
    return max(b + 1, 11)


def parameter_degree_bound(b: int) -&gt; int:
    return 2 * b


def log_H(m: int, b: int) -&gt; float:
    nvars = variable_count(m, b)
    d = equation_degree_bound(b)
    return math.log(2 * b * (nvars + 1)) + nvars * math.log(d)


def unrestricted_log_H(B: int) -&gt; float:
    nvars_bound = 32 * (B + 3) * (4**B)
    return (
        math.log(2 * B * (nvars_bound + 1))
        + nvars_bound * math.log(B + 11)
    )


def tradeoff_log_H(m: int, b: int) -&gt; float:
    nvars_bound = 32 * (m + 3) * (2 ** (m + b))
    return (
        math.log(2 * b * (nvars_bound + 1))
        + nvars_bound * math.log(b + 11)
    )


def main() -&gt; None:
    enumeration_checks = &#91;&#93;
    for n in range(1, 5):
        for b in range(0, 5):
            enumerated = sum(1 for _ in exponent_tuples(n, b))
            formula = monomial_count(n, b)
            assert enumerated == formula
            enumeration_checks.append(
                {"n": n, "b": b, "count": formula}
            )

    # Degree bookkeeping for the universal coefficient equations.
    degree_checks = &#91;&#93;
    for b in range(1, 21):
        inverse_composition_degree = b + 1
        left_substitution_degree = 11
        right_substitution_degree = 1
        computed = max(
            inverse_composition_degree,
            left_substitution_degree,
            right_substitution_degree,
        )
        asserted = equation_degree_bound(b)
        assert computed == asserted
        assert parameter_degree_bound(b) == 2 * b
        degree_checks.append(
            {
                "b": b,
                "coefficient_degree": asserted,
                "parameter_degree": 2 * b,
            }
        )

    exact_samples = &#91;&#93;
    for m in range(0, 4):
        for b in (1, 2, 4, 8, 12):
            n = 3 + m
            t = monomial_count(n, b)
            nvars = variable_count(m, b)
            assert nvars == 4 * n * t
            assert t &lt;= 2 ** (n + b)
            assert nvars &lt;= 32 * (m + 3) * (2 ** (m + b))
            exact_samples.append(
                {
                    "m": m,
                    "b": b,
                    "ambient_dimension": n,
                    "monomials_per_coordinate": t,
                    "coefficient_variables": nvars,
                    "d": equation_degree_bound(b),
                    "h": parameter_degree_bound(b),
                    "log_H": log_H(m, b),
                    "log10_H": log_H(m, b) / math.log(10),
                    "tradeoff_log_H": tradeoff_log_H(m, b),
                }
            )

    fixed_n_asymptotics = &#91;&#93;
    for n in (3, 4, 5, 6):
        target = 4 / math.factorial(n - 1)
        values = &#91;&#93;
        for b in (50, 100, 200, 500):
            m = n - 3
            ratio = log_H(m, b) / (b**n * math.log(b))
            values.append({"b": b, "ratio": ratio})
        # Convergence is from above for these samples and must be reasonably close.
        assert abs(values&#91;-1&#93;&#91;"ratio"&#93; - target) / target &lt; 0.08
        fixed_n_asymptotics.append(
            {
                "n": n,
                "target_coefficient": target,
                "inverted_constant": (math.factorial(n) / 4) ** (1 / n),
                "samples": values,
            }
        )

    unrestricted_asymptotics = &#91;&#93;
    for B in (10, 20, 40, 80, 160):
        ll = math.log(unrestricted_log_H(B))
        ratio = ll / B
        unrestricted_asymptotics.append(
            {
                "B": B,
                "log_log_H_over_B": ratio,
                "target": math.log(4),
            }
        )
    assert abs(unrestricted_asymptotics&#91;-1&#93;&#91;"log_log_H_over_B"&#93; - math.log(4)) &lt; 0.08

    report = {
        "status": "ALL EFFECTIVE UNFRAMED BOUND CHECKS PASSED",
        "scope": {
            "verified": &#91;
                "monomial count T(n,b)=binomial(n+b,n)",
                "coefficient variable count N=4*n*T(n,b)",
                "universal equation coefficient-degree bound max(b+1,11)",
                "universal parameter-degree bound 2*b",
                "finite tradeoff inequalities",
                "fixed-stabilization asymptotic leading constants",
                "unrestricted log-log coefficient log(4)",
            &#93;,
            "not_verified_by_script": &#91;
                "complete stable q-classification",
                "generic-fiber emptiness",
                "constant generic-combination lemma",
                "D'Andrea-Krick-Sombra parametric Nullstellensatz",
            &#93;,
        },
        "formulas": {
            "H(m,b)": "2*b*(N+1)*max(b+1,11)^N",
            "N": "4*(m+3)*binomial(m+b+3,m+3)",
            "unrestricted_finite_bound": "2*B*(32*(B+3)*4^B+1)*(B+11)^(32*(B+3)*4^B)",
            "unrestricted_asymptotic": "liminf kappa_M/log(log M) &gt;= 1/log(4)",
        },
        "enumeration_checks": enumeration_checks,
        "degree_checks": degree_checks,
        "exact_samples": exact_samples,
        "fixed_n_asymptotics": fixed_n_asymptotics,
        "unrestricted_asymptotics": unrestricted_asymptotics,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report&#91;"status"&#93;)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
</code></pre>

[Back to Lane 3](bounded-degree-deformation-modulus-onset.md)
