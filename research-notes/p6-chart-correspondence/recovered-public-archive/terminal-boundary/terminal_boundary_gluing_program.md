# From the degree-21 boundary obstruction to a terminal gluing–descent program

**Status:** The layer, adjoint, index, resonance, hypergeometric, derivative, passport, and filtered-descent statements below are proved. The terminal gluing–descent dichotomy is conjectural. This is not a proof of the plane Jacobian conjecture.

## 1. Universal determinant complex

For

\[
\alpha A B_z-\beta A_zB+s(A_zB_s-A_sB_z)=\Psi(z),
\]

with \(A=A_0+\sum_{r\ge1}s^ra_r\) and \(B=B_0+\sum_{r\ge1}s^rb_r\), the new order-\(r\) coefficients enter through

\[
\mathscr D_r^{\alpha,\beta}(a,b)
=(\alpha-r)a\,dB_0-\beta B_0\,da
+\alpha A_0\,db+(r-\beta)b\,dA_0.
\]

Its residue adjoint is

\[
(\mathscr D_r^{\alpha,\beta})^\vee(\lambda)=
\left(
\beta B_0d\lambda+(\alpha+\beta-r)\lambda dB_0,
-\alpha A_0d\lambda+(r-\alpha-\beta)\lambda dA_0
\right).
\]

For a map

\[
H^0\mathcal O(d_A)\oplus H^0\mathcal O(d_B)\to H^0\mathcal O(d_W)
\]

on \(\mathbf P^1\), the virtual target-minus-domain dimension is

\[
\epsilon=d_W-d_A-d_B-1.
\]

For the certified full \((8,28)\) support, \(d_A=10-r\), \(d_B=15-r\), and \(d_W=25-r\), hence

\[
\epsilon_r=r-1.
\]

## 2. Contact-degree formula and universal secondary Belyi transport

Suppose the common-power exponents are coprime integers \(m,n\), with

\[
v_E(P)=-m,\quad v_E(Q)=-n,\qquad
v_D(P)=-ma,\quad v_D(Q)=-na.
\]

Choose \(c,d\) with \(dn-cm=1\), put \(\pi=P^c/Q^d\), \(\tau=Q^m/P^n\), and suppose the normalized bracket is \([P,Q]=x^\kappa\) in a toric chart with \(x=t^{-1}\) up to an \(s\)-unit. Comparing the \(t\)-orders in \(d\pi\wedge d\tau\) gives

\[
\boxed{e=a(m+n)-\kappa-1}.
\]

For the certified case, \((m,n,a,\kappa)=(2,3,4,2)\), hence \(e=17\).

Now let \(a,e\in\mathbf N\) with \(e>a^2\), and put \(\delta=e-a^2\). After removing all resonant target shears, assume

\[
\pi=t^a\frac{s}{s-1}+O(t^{a+1})
\]

and the first nonzero boundary-volume term forces

\[
e c'h-a c h'=-(s-1)^{-a-2},\qquad c=\frac{s}{s-1}.
\]

Then

\[
h=\frac{H_{a,e}(s)}{(s-1)^a},
\]

where

\[
H_{a,e}(s)=\sum_{k=0}^a
\frac{a^k a!}{(a-k)!\prod_{j=0}^k(e-aj)}s^k
=\frac1e\,{}_2F_1\left(-a,1;1-\frac ea;s\right).
\]

It obeys

\[
a s(s-1)H'+(e-a^2s)H=1,
\]

is squarefree, and satisfies \(H(0)=1/e\), \(H(1)=1/\delta\).

The exceptional ratio

\[
W_{a,e}(s)=\frac{(s-1)^\delta H_{a,e}(s)^a}{s^e}
\]

is a degree-\(e\) Belyi map with

\[
W_{a,e}'(s)=\frac{(s-1)^{\delta-1}H_{a,e}(s)^{a-1}}{s^{e+1}}
\]

and passport

\[
(a^a\,\delta),\qquad(e),\qquad(a+1\,1^{e-a-1}).
\]

For \((a,e)=(4,17)\),

\[
H_{4,17}=\frac{195+240s+320s^2+512s^3+2048s^4}{3315},
\]

recovering the degree-17 secondary map in the current boundary package.

## 3. Exact one-layer descent lemma

Let \(D:U\to V\) and let \(V_{\le m}\subset V\) be a smaller Newton/pole window. For \(\Phi\in V\), the following are equivalent:

1. there is \(u\in U\) with \(\Phi-Du\in V_{\le m}\);
2. every \(\lambda\in(\operatorname{im}D)^\perp\cap(V_{\le m})^\perp\) satisfies \(\lambda(\Phi)=0\).

In the boundary complex, these \(\lambda\)'s are precisely the high-pole adjoint residue classes. Therefore vanishing high-pole residues *does* lower a single Newton window. The missing step is to make the reductions compatible across all normal layers and integrate them to one allowable approximate-root transformation.

## 4. Conditional full-proof theorem

A sufficient global statement is:

> For every terminal complete-chain model, either its Newton-bounded boundary Kuranishi zero scheme is empty, or every zero produces a standard Keller pair of strictly smaller complete-chain complexity.

Together with completeness of the boundary Kuranishi functor, this would prove the plane Jacobian conjecture by minimal counterexample descent.

## 5. Next test queue

| Priority | Complete-chain data | \((m,n)\) | maximum degree |
|---:|---|---:|---:|
| 1 | \(F_2: (5,20)\to(7/5,2)\) | \((3,5)\) | 125 |
| 2 | \((7,35)\to(19/7,5)\) | \((2,3)\) | 126 |
| 3 | \((12,30)\to(16/3,10)\to(11/6,3)\) | \((3,2)\) | 126 |
| 4 | \(F_{24}: (8,24)\to(14/4,6)\to(19/8,3)\) | \((3,4)\) | 128 |
| 5 | \((11,33)\to(19/4,8)\) | \((2,3)\) | 132 |

The first meaningful universality test is \(F_2\): it is the first candidate at 125, has a one-step complete chain, and changes the degree ratio from the current \((2,3)\)-type geometry.

## 6. Lattice-gap terminal-primary reduction

For every type-I.b final corner in the orientation of equation (3.17), the fractional terminal faces satisfy

\[
npq-mzpq'+nzp'q=1.
\]

The ambient uniformizing map

\[
\tau=z^n p^n/q^m
\]

has degree \(mnb\).  However, if

\[
g=\operatorname{gap}(\rho,\ell),
\]

then polynomial lattice support forces

\[
p(z)=\bar p(z^g),\qquad q(z)=\bar q(z^g).
\]

Writing \(u=z^g\) and \(N=n/g\), the actual quotient equation is

\[
N\bar p\bar q-mu\bar p\bar q'+nu\bar p'\bar q=\frac1g,
\]

and

\[
\bar\tau=u^N\bar p^n/\bar q^m
\]

has degree \(mnb/g\) and passport

\[
\left(n^{(mb-1)/g},N\right),\qquad
\left(m^{nb/g}\right),\qquad
\left(\frac{(m+n)b-1}{g},1^{\frac{mnb-(m+n)b+1}{g}}\right).
\]

This is the finite Hurwitz problem relevant to the complete-chain corner; the ambient degree-\(mnb\) cover is its cyclic \(g\)-pullback.

For the first cases in the queue:

| Case | \(g\) | quotient degree | quotient passport | classes |
|---|---:|---:|---|---:|
| \(F_2\), max 125 | 5 | 6 | \((5,1),(3^2),(3,1^3)\) | 1 |
| one-step max 126 | 3 | 10 | \((3^3,1),(2^5),(8,1^2)\) | 1 |
| two-step max 126 | 2 | 9 | \((2^4,1),(3^3),(7,1^2)\) | 1 |
| \(F_{24}\), max 128 | 4 | 9 | \((4^2,1),(3^3),(5,1^4)\) | 2 |
| one-step max 132 | 3 | 16 | \((3^5,1),(2^8),(13,1^3)\) | 2 |

The important correction is the first row.  The ambient \(F_2\) degree-30 passport has eleven dessin classes, but the gap-five lattice condition selects only its unique \(C_5\)-symmetric pullback.  The actual reduced boundary map is the unique degree-six map

\[
\bar\tau(u)\doteq
\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
\]

Thus the next universality test is a single \(C_5\)-equivariant normal-neighborhood computation, not eleven unrelated degree-30 calculations.  Exact maps for the two degree-126 rows and the two conjugate \(F_{24}\) rows are given in `terminal_primary_belyi_reduction.md`.


## 7. Reduced terminal covers are rigid in the first explicit cases

For the quotient equation

\[
N\bar p\bar q-mu\bar p\bar q'+nu\bar p'\bar q=\frac1g,
\]

the fixed-constant linearization is

\[
\mathscr L(\alpha,\beta)
=N(\alpha\bar q+\bar p\beta)
-mu(\alpha\bar q'+\bar p\beta')
+nu(\alpha'\bar q+\bar p'\beta).
\]

Exact matrices for the degree-6, degree-10, degree-9, and the two conjugate degree-9 quotient maps have full target rank and one-dimensional kernel

\[
\ker\mathscr L=\operatorname{Span}\{(u\bar p',u\bar q')\}.
\]

Thus the reduced-cover coefficient scheme is smooth only along source rescaling; after quotienting by that rescaling, each map is a reduced isolated point.  This removes one potential source of hidden moduli from the next boundary calculations.  The first post-125 test can therefore be organized as a normal-jet Kuranishi problem over a rigid reduced degree-six cover.

The result does not yet identify the full boundary deformation functor with a product of the reduced Hurwitz point and the normal-jet complex.  The next structural theorem should prove this etale splitting, or explicitly identify the cross-terms that obstruct it.
