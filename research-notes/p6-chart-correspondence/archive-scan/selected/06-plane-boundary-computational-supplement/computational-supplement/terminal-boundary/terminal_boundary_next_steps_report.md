# Next research cycle for the terminal boundary-gluing program

**Date:** 22 July 2026
**Status:** exact algebra and finite character computations; no claim of a proof of the plane Jacobian conjecture.

## Executive result

The first post-125 terminal complete-chain problems are much smaller than their fractional uniformizing covers suggest.  For a final type-I.b corner, the complete-chain lattice gap forces the face polynomials to descend through a cyclic quotient.  The relevant Belyi cover has degree

\[
D=\frac{mnb}{g},\qquad g=\operatorname{gap}(\rho,\ell),
\]

not the ambient degree \(mnb\).  Its passport is

\[
\left(n^{(mb-1)/g},\frac ng\right),\qquad
\left(m^{nb/g}\right),\qquad
\left(\frac{(m+n)b-1}{g},1^{D-\frac{(m+n)b-1}{g}}\right).
\]

For the first five complete-chain cases at maximum degrees \(125,126,126,128,132\), the numbers of relevant connected covers are

\[
1,\quad1,\quad1,\quad2,\quad2.
\]

The explicit maps through maximum degree 128 are infinitesimally rigid modulo the single source-rescaling symmetry.  Consequently the next obstruction calculations can be formulated entirely in the normal-neighborhood jets over rigid reduced boundary covers.

## 1. Universal terminal-primary equation

For terminal faces

\[
P_E=x^{1-k/\ell}y\,p(z),\qquad
Q_E=x^{k/\ell}q(z),\qquad
z=x^{-\sigma/\rho}y,
\]

the type-I.b corner relation gives

\[
\boxed{npq-mzpq'+nzp'q=1.}
\]

The fractional ratio

\[
\tau(z)=z^n\frac{p(z)^n}{q(z)^m}
\]

satisfies

\[
\tau'(z)=z^{n-1}\frac{p(z)^{n-1}}{q(z)^{m+1}}.
\]

This produces the ambient passport

\[
(n^{mb}),\qquad(m^{nb}),\qquad
((m+n)b-1,1^{mnb-(m+n)b+1}).
\]

## 2. Lattice-gap quotient theorem

Polynomial lattice support gives

\[
p(z)=\bar p(u),\qquad q(z)=\bar q(u),\qquad u=z^g,
\]

where

\[
g=\frac{\rho}{\gcd(\rho,\ell)}.
\]

The quotient equation is

\[
\boxed{
N\bar p\bar q-mu\bar p\bar q'+nu\bar p'\bar q=\frac1g,
\qquad N=\frac ng.
}
\]

The quotient map

\[
\bar\tau(u)=u^N\frac{\bar p(u)^n}{\bar q(u)^m}
\]

has the degree and passport in the executive result, and

\[
\tau(z)=\bar\tau(z^g).
\]

Every triple with the quotient passport is transitive.  An orbit not meeting the unique long cycle of the third permutation would be fixed by that permutation, forcing the first two restrictions to be inverse.  Their cycle lengths would then agree, contradicting coprimality of \(m,n\) and the fact that \(N\mid n\).

## 3. First exact quotient queue

| Case | gap \(g\) | ambient degree | quotient degree | quotient passport | connected classes |
|---|---:|---:|---:|---|---:|
| \(F_2\), max 125 | 5 | 30 | 6 | \((5,1),(3^2),(3,1^3)\) | 1 |
| one-step max 126 | 3 | 30 | 10 | \((3^3,1),(2^5),(8,1^2)\) | 1 |
| two-step max 126 | 2 | 18 | 9 | \((2^4,1),(3^3),(7,1^2)\) | 1 |
| \(F_{24}\), max 128 | 4 | 36 | 9 | \((4^2,1),(3^3),(5,1^4)\) | 2 |
| one-step max 132 | 3 | 48 | 16 | \((3^5,1),(2^8),(13,1^3)\) | 2 |

The ambient degree-30 passport for \(F_2\) has eleven connected classes, but only the unique \(C_5\)-symmetric class descends through \(u=z^5\).

## 4. Explicit reduced covers

### 4.1 Maximum degree 125

\[
\bar p=1-u,
\qquad
\bar q=\frac15-\frac35u+\frac9{25}u^2,
\]

and, up to target scaling,

\[
\boxed{
\bar\tau(u)=
\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
}
\]

### 4.2 One-step maximum degree 126

Put

\[
P=u^3+u^2+\frac5{12}u+\frac1{18},
\]

\[
Q=u^5+\frac32u^4+u^3+\frac13u^2+\frac5{96}u+\frac1{576}.
\]

Then

\[
uP^3-Q^2=-\frac{36u^2+28u+9}{2985984}.
\]

The quotient equation is obtained with \(\bar p=18P\), \(\bar q=192Q\).

### 4.3 Two-step maximum degree 126

\[
\bar p=1+\frac{20}{3}u+24u^2+\frac{288}{7}u^3+\frac{288}{7}u^4,
\]

\[
\bar q=\frac12+5u+12u^2+18u^3.
\]

### 4.4 Family \(F_{24}\), maximum degree 128

There are two conjugate maps over \(\mathbf Q(\sqrt6)\):

\[
\bar p_\varepsilon
=1+u+\left(\frac13+\varepsilon\frac{\sqrt6}{18}\right)u^2,
\]

\[
\bar q_\varepsilon
=\frac14+\frac58u
+\left(\frac25+\varepsilon\frac{\sqrt6}{40}\right)u^2
+\left(\frac{17}{160}+\varepsilon\frac{11\sqrt6}{480}\right)u^3,
\qquad\varepsilon=\pm1.
\]

## 5. Reduced-cover tangent calculation

Fix the constant terms and linearize

\[
\mathcal F(p,q)=Npq-mupq'+nup'q.
\]

The differential is

\[
\mathscr L(\alpha,\beta)
=N(\alpha q+p\beta)
-mu(\alpha q'+p\beta')
+nu(\alpha'q+p'\beta).
\]

The source scaling \(u\mapsto(1+\epsilon)u\) gives the kernel vector

\[
(\alpha,\beta)=(up',uq').
\]

For every explicit map above, the exact matrix has full target rank and this is its entire kernel.

| Map | degrees \((\deg p,\deg q)\) | rank | target dimension | nonzero maximal minor |
|---|---:|---:|---:|---|
| max 125 | \((1,2)\) | 2 | 2 | \(-36/5\) |
| one-step max 126 | \((3,5)\) | 7 | 7 | \(2090188800\) |
| two-step max 126 | \((4,3)\) | 6 | 6 | \(37791360/7\) |
| \(F_{24},-\) | \((2,3)\) | 4 | 4 | \(99/20-153\sqrt6/40\) |
| \(F_{24},+\) | \((2,3)\) | 4 | 4 | \(99/20+153\sqrt6/40\) |

After quotienting source scaling, the reduced-cover coefficient points are isolated and reduced.

## 6. Universal normal-boundary pieces

The determinant-preserving normal expansion has layer operator

\[
\mathscr D_r^{\alpha,\beta}(a,b)
=(\alpha-r)a\,dB_0-\beta B_0\,da
+\alpha A_0\,db+(r-\beta)b\,dA_0,
\]

and residue adjoint

\[
(\mathscr D_r^{\alpha,\beta})^\vee(\lambda)=
\left(
\beta B_0d\lambda+(\alpha+\beta-r)\lambda dB_0,
-\alpha A_0d\lambda+(r-\alpha-\beta)\lambda dA_0
\right).
\]

For line-bundle windows

\[
H^0\mathcal O(d_A)\oplus H^0\mathcal O(d_B)
\longrightarrow H^0\mathcal O(d_W),
\]

the virtual obstruction excess is

\[
\epsilon=d_W-d_A-d_B-1.
\]

The certified \((8,28)\) support has \(\epsilon_r=r-1\).

A general resonance-removal calculation also forces the secondary boundary cover.  For contact data \((a,e)\), \(e>a^2\), put \(\delta=e-a^2\) and

\[
H_{a,e}(s)=\frac1e\,{}_2F_1\!\left(-a,1;1-\frac ea;s\right).
\]

Then

\[
W_{a,e}(s)=\frac{(s-1)^\delta H_{a,e}(s)^a}{s^e}
\]

is a degree-\(e\) Belyi map with passport

\[
(a^a,\delta),\qquad(e),\qquad(a+1,1^{e-a-1}).
\]

This includes the degree-17 secondary map arising from \((a,e)=(4,17)\).

## 7. What this accomplishes for the full-proof program

The first post-125 problem is no longer an eleven-dessin search.  It is one normal-neighborhood Kuranishi problem over a rigid degree-six cover, with a prescribed \(C_5\)-equivariant lattice structure.  The same architecture then applies to one degree-ten cover, one degree-nine cover, and a pair of conjugate degree-nine covers.

The exact one-layer descent lemma says that vanishing of the high-pole adjoint residues is equivalent to lowering a single Newton window.  The remaining global theorem is to make these layerwise reductions compatible and integrate them into one allowable approximate-root transformation.

A sufficient dichotomy is:

> For every terminal complete-chain model, either the Newton-bounded boundary Kuranishi zero scheme is empty, or every zero induces a strict descent of complete-chain complexity.

With a complete boundary deformation functor, this dichotomy would rule out a minimal counterexample.

## 8. Immediate unresolved calculation

For the \(F_2\) chain, one must still propagate the **full** Newton supports through the approximate-root shears and the quotient \(u=z^5\).  The complete-chain table fixes the terminal face but does not by itself determine every normal-layer monomial window.  The next exact deliverable is therefore:

1. the two-point line-bundle window table for the \(F_2\) normal coefficients;
2. the corresponding adjoint pole jumps;
3. the first nonlinear residue obstruction;
4. either a nonzero gluing norm or an explicit compatible Newton descent.

Until those windows are derived and the resulting Kuranishi problem is solved, this program is not a proof of the plane Jacobian conjecture.
