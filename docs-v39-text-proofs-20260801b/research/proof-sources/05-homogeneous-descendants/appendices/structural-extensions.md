---
title: "Text proof source — 05-homogeneous-descendants/appendices/structural-extensions.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `b57041e8e8baacbb59bcaaee1bc988e0ea7d33b09a80e3745941769d61c75704` · 11,216 bytes

## Exact label anchors

<a id="label-sec-one-cover"></a>
- `sec:one-cover` — source line 6
<a id="label-prop-rees-presentation"></a>
- `prop:rees-presentation` — source line 14
<a id="label-eq-quotient-cubic"></a>
- `eq:quotient-cubic` — source line 109
<a id="label-eq-nonproperness-polynomial"></a>
- `eq:nonproperness-polynomial` — source line 119
<a id="label-sec-all-order-rays"></a>
- `sec:all-order-rays` — source line 130
<a id="label-thm-inverse-ray-family"></a>
- `thm:inverse-ray-family` — source line 141
<a id="label-eq-positive-cn"></a>
- `eq:positive-cn` — source line 200
<a id="label-thm-all-order-laplacian"></a>
- `thm:all-order-laplacian` — source line 210
<a id="label-sec-moving-flag"></a>
- `sec:moving-flag` — source line 239
<a id="label-prop-not-strongly-nilpotent"></a>
- `prop:not-strongly-nilpotent` — source line 244
<a id="label-lem-self-dual-extension"></a>
- `lem:self-dual-extension` — source line 264
<a id="label-sec-robust-compression"></a>
- `sec:robust-compression` — source line 311
<a id="label-eq-quartic-obstruction-general"></a>
- `eq:quartic-obstruction-general` — source line 324
<a id="label-prop-compression-family"></a>
- `prop:compression-family` — source line 341

## Complete source

~~~tex




\section{One cover in several normal forms}
\label{sec:one-cover}

The reductions below do more than transport a collision: after adjoining purely
transcendental variables, they preserve the function-field extension induced by
the original map.  Thus the cubic, symmetric, and square-zero descendants are
presentations of the same generically three-sheeted cover.

\begin{proposition}[Rees presentation of the rank-sensitive suspension]
\label{prop:rees-presentation}
Let $K=X+Q+C$, let $C=Bq$, and let
\[
G(X,w,t)=\bigl(X+tQ(X)+t^2Bw,\;w-q(X),\;t\bigr).
\]
Define triangular automorphisms
\[
S(X,v,t)=(X,v+q(X),t),\qquad
T(Y,v,t)=(Y-t^2Bv,v,t).
\]
Then
\[
T\circ G\circ S=(K_t\times\id)(X,v,t),
\qquad
K_t(X)=X+tQ(X)+t^2C(X)=t^{-1}K(tX).
\]
Consequently, after inverting $t$, the function-field extension induced by $G$
is obtained from that induced by $K$ by adjoining independent transcendental
variables.  In particular, generic degree and geometric monodromy are
preserved.
\end{proposition}

\begin{proof}
Direct substitution gives
\[
G(X,v+q(X),t)
 =\bigl(X+tQ(X)+t^2Bv+t^2C(X),v,t\bigr),
\]
and the target shear $T$ removes $t^2Bv$.  Over $k(t)$ the change of variables
$U=tX$ identifies $K_t$ with $K$.
\end{proof}

\begin{proposition}[The symmetric double is a stable presentation]
Let $F=X+H$ be Keller and put
\[
\Phi_F(x,y)=\bigl(F(x),JF(x)^Ty\bigr).
\]
Then the polynomial automorphism
\[
S_F(x,y)=\bigl(x,JF(x)^Ty\bigr)
\]
satisfies
\[
\Phi_F=(F\times\id)\circ S_F.
\]
Hence the symmetric double, and therefore its linear gradient twist, induces
the same function-field extension as $F$ after adjoining $\dim F$ independent
variables.
\end{proposition}

\begin{proof}
Since $\det JF=1$, the inverse matrix $JF^{-T}$ has polynomial entries, so $S_F$
is a polynomial automorphism.
\end{proof}

\begin{proposition}[A full-rank square-zero pairing is stably right-equivalent]
Suppose
\[
H(z)=B(Dz)^{*3},\qquad BD=0,
\]
where $B:W\to V$ is surjective and $D:V\to W$ is injective.  Put $A=DB$ and
$F_A(w)=w+(Aw)^{*3}$.  Choose a right inverse $C$ of $B$ and write
$W=C(V)\oplus E$, where $E=\ker B$.  Set
\[
\rho(z)=(Dz)^{*3}-CH(z)\in E.
\]
In the coordinates $w=Cz+\eta$, one has
\[
F_A(z,\eta)=\bigl(G(z),\eta+\rho(z)\bigr),
\qquad G=I+H.
\]
Precomposition by $(z,\eta)\mapsto(z,\eta-\rho(z))$ therefore changes $F_A$
into $G\times\id_E$.
\end{proposition}

\subsection{The quotient cubic and its monodromy}

For the original three-variable map, write its target coordinates as
$(\xi,\eta,\zeta)$.  The source has the grading
$\mathrm{wt}(x,y,z)=(1,-1,-2)$, and the target weights are $(-2,-1,1)$.
Put
\[
\nu=xy,\qquad v=x^2z,\qquad r=1+\nu,
\qquad c=2-3\nu-v,\qquad q=cr,
\]
and form the target invariants
\[
A=\xi\zeta^2,\qquad B=\eta\zeta.
\]
A direct calculation gives
\[
A=q^2+cq-q^3,\qquad B=4q+2c-3q^2.
\]
Eliminating $c$ yields the cubic
\begin{equation}
\label{eq:quotient-cubic}
q^3-2q^2+Bq-2A=0.
\end{equation}
Its discriminant is
\[
-4\bigl(27A^2-18AB+16A+B^3-B^2\bigr)
 =-4\zeta^2\mathscr N(\xi,\eta,\zeta),
\]
where
\begin{equation}
\label{eq:nonproperness-polynomial}
\mathscr N(\xi,\eta,\zeta)
 =27\xi^2\zeta^2-18\xi\eta\zeta+16\xi
  +\eta^3\zeta-\eta^2.
\end{equation}
The quadratic polynomial in $A$ inside the discriminant has discriminant
$-4(3B-4)^3$, hence is not a square over $\mathbb Q(B)$.  Together with the
generic irreducibility of \eqref{eq:quotient-cubic}, this gives geometric
monodromy $S_3$.

\section{A two-parameter family of all-order inverse rays}
\label{sec:all-order-rays}

Let $e_x,e_y,e_{w_1},e_t$ refer to the indicated coordinates of the
$19$-variable cubic map, and for $\alpha,\beta\in\mathbb Q$ put
\[
Y_{\alpha,\beta}
 =\alpha e_x+e_y+\beta e_{w_1}+e_t.
\]
Let $\widehat G^{-1}_0$ denote the formal inverse branch at the origin.

\begin{theorem}[Exact inverse-ray family]
\label{thm:inverse-ray-family}
For all $\alpha,\beta$,
\[
\bigl(\widehat G^{-1}_0(sY_{\alpha,\beta})\bigr)_x
 =\frac{(1-2\alpha s^4+2\beta s^6)^{-1/2}-1}{s^3},
\]
where the square root is the branch with constant term $1$.
\end{theorem}

\begin{proof}
The $t$-coordinate gives $t=s$, and the $w$-coordinates give
$w=q(X)+s\beta e_1$.  Therefore
\[
K(sX)=s^2(\alpha e_x+e_y)-s^4\beta e_x.
\]
After applying the linear normalization and eliminating the stable auxiliary
coordinates, this is the original three-variable target curve
\[
(\xi,\eta,\zeta)
  =\bigl(0,s^2,2\alpha s^2-2\beta s^4\bigr).
\]
On the local branch above $\xi=0$, write
\[
R=(1+xy)^2z+y^2(4+3xy).
\]
The equation $\xi=(1+xy)R=0$ gives $R=0$, and then $\eta=y=s^2$.  With
$r=1+xy$, the third component simplifies to
\[
\zeta=\frac{1-r^{-2}}{y}.
\]
Thus
\[
r=(1-y\zeta)^{-1/2}
  =(1-2\alpha s^4+2\beta s^6)^{-1/2},
\]
and the original $x$-coordinate is $(r-1)/s^2$.  Since the original source is
$sX$, division by $s$ gives the formula.
\end{proof}

The same calculation explains the singularities: along this curve,
\[
\mathscr N(0,s^2,2\alpha s^2-2\beta s^4)
 =-s^4(1-2\alpha s^4+2\beta s^6).
\]
Thus the algebraic singularities of the inverse ray are precisely its
intersections with the discriminant/nonproperness hypersurface.

Let $\mathcal G=I+\nabla\mathcal Q$ be the $38$-variable gradient descendant,
and put
\[
W_{\alpha,\beta}=T^{-1}(Y_{\alpha,\beta},0).
\]
For $n\ge0$ define
\[
c_n(\alpha,\beta)
 =[u^n](1-2\alpha u^2-2\beta u^3)^{-1/2}.
\]
For $n\ge2$ one has the finite sum
\begin{equation}
\label{eq:positive-cn}
c_n(\alpha,\beta)
 =\sum_{k=\lceil n/3\rceil}^{\lfloor n/2\rfloor}
 2^{-k}\binom{2k}{k}\binom{k}{n-2k}
 \alpha^{3k-n}\beta^{n-2k}.
\end{equation}
In particular, $c_n(\alpha,\beta)>0$ for positive rational
$\alpha,\beta$.

\begin{theorem}[Nonvanishing at every Laplacian order]
\label{thm:all-order-laplacian}
For every $m\ge1$ and every positive rational $\alpha,\beta$,
\[
\partial_{u_1}\Delta^m\bigl(\mathcal Q^{m+1}\bigr)
   (W_{\alpha,\beta})
 =2^{m-1}m!(m+1)!\,c_{m+3}(\alpha,\beta)>0.
\]
Thus the same quartic violates the eventual-vanishing condition at every
order, not merely along an infinite parity class.
\end{theorem}

\begin{proof}
The first coordinate of the inverse gradient ray is half the first coordinate
in Theorem~\ref{thm:inverse-ray-family}.  If
\[
(1-2\alpha u^2+2\beta u^3)^{-1/2}=\sum d_nu^n,
\]
then $d_n=(-1)^nc_n(\alpha,\beta)$.  Compare the coefficient of $s^{2m+3}$
with Zhao's inversion formula for $P=-\mathcal Q$:
\[
R_m=\frac{1}{2^m m!(m+1)!}\Delta^m(P^{m+1}).
\]
The two signs cancel, giving the displayed positive formula.
\end{proof}

The central-binomial formula in the earlier draft is the boundary case
$(\alpha,\beta)=(1/2,0)$.  Turning on $\beta$ fills the parity gaps.

\section{The nilpotent flag moves}
\label{sec:moving-flag}

Let $A(Z)=JH(Z)$ for the $19$-variable cubic tensor.

\begin{proposition}[A two-point obstruction to strong nilpotence]
\label{prop:not-strongly-nilpotent}
Although $A(Z)$ is nilpotent for every $Z$, the family is not strongly
nilpotent and is not simultaneously strictly triangularizable.  Indeed,
\[
A(e_d)A(e_t)|_{\langle e_{w_3},e_{w_6}\rangle}
 =\begin{pmatrix}-1&1\\2&-2\end{pmatrix},
\]
and all other entries of the product vanish.  Hence
\[
\chi_{A(e_d)A(e_t)}(\lambda)=\lambda^{18}(\lambda+3).
\]
\end{proposition}

This gives a concrete form of the distinction between pointwise nilpotence and
a common nilpotent flag: the generic matrix is almost regular nilpotent, but
its Jordan flag twists with the base point.

\subsection{A self-dual extension lemma}

\begin{lemma}[Isotropic terminal vector]
\label{lem:self-dual-extension}
Let $A$ have Jordan type $(m,1)$, let
$\ker A=\langle v_1,v_2\rangle$, and suppose
$\operatorname{im}A^{m-1}=\langle v_2\rangle$.  Let $L=L^T$ and
\[
N=\begin{pmatrix}A&0\\L&A^T\end{pmatrix}.
\]
Define the symmetric form
\[
\beta(u,v)=u^TLv\qquad(u,v\in\ker A).
\]
If $\beta$ has rank one with radical $\langle v_2\rangle$, if
$N^{2m-2}\ne0$, and if $\beta(v_2,v_2)=0$, then $N$ has Jordan type
$(2m-1,2,1)$.
\end{lemma}

\begin{proof}
Projection of $\ker N$ to its first factor identifies its image with
$\operatorname{rad}\beta$, and each fiber is $\ker A^T$.  Thus
$\dim\ker N=2+1=3$.  The lower-left block of $N^{2m-1}$ is the sole possible
term
\[
(A^T)^{m-1}LA^{m-1},
\]
which vanishes because the terminal line is isotropic.  The preceding power
does not vanish:
\[
N^{2m-2}\ne0.
\]
Thus the nilpotency index is \(2m-1\).  The operator acts on a space of
dimension \(2m+2\) and has three blocks.  Its largest block has size
\(2m-1\), so its partition is \((2m-1,2,1)\).
\end{proof}

For the present tensor, exact differentiation gives
\[
D^2H[v_1,v_1]=-4t^3xz\,e_x,
\qquad
D^2H[v_1,v_2]=D^2H[v_2,v_2]=0.
\]
Hence the form induced by
$L=\operatorname{Hess}_x(y^TH(x))$ has rank one on $\ker A$, with radical
$\langle v_2\rangle$.  The previously verified nonzero entry of $N^{34}$
then applies Lemma~\ref{lem:self-dual-extension} with $m=18$ and explains the
partition $(35,2,1)$ as a one-box degeneration of maximal chain gluing.

\section{A robust equivariant compression obstruction}
\label{sec:robust-compression}

The normalized $11$-variable map is equivariant for the weights
\[
(1,-1,-2,0,1,-2,0,-1,-2,2,-1)
\]
on $(x,y,z,a,b,c,d,q,s,h,k)$.  Let $\mathfrak X_2^{(0)}$ be the space of
weight-preserving quadratic vector fields; exact counting gives
$\dim\mathfrak X_2^{(0)}=115$.

For a quadratic formal coordinate change $I+P$, the cubic jet is
$C+[Q,P]$.  Its quartic term is
\begin{equation}
\label{eq:quartic-obstruction-general}
\mathcal O_4(P)
 =[C,P]+\frac12D^2Q[P,P]-JP[Q,P]-\frac12D^2P[Q,Q].
\end{equation}

Put
\[
\Sigma_{-2}=\langle
 y^2,qy,ky,az,dz,ac,as,cd,ds,q^2,kq,k^2
\rangle
\]
and
\[
P_\sigma=-d^2e_a+\sigma e_s\qquad(\sigma\in\Sigma_{-2}).
\]

\begin{proposition}[A positive-dimensional obstructed compression family]
\label{prop:compression-family}
For every $\sigma\in\Sigma_{-2}$, the cubic jet
$C+[Q,P_\sigma]$ is supported only in the six output coordinates
$x,y,z,b,c,s$, and therefore has coordinate-span rank at most six.  Nevertheless,
\[
\Lambda_4\bigl(\mathcal O_4(P_\sigma)\bigr)=1.
\]
Hence no cubic source correction removes the quartic term anywhere in this
$12$-parameter formal family.  Excluding the two monomials involving $s$
gives a $10$-parameter family of actual triangular polynomial automorphisms.
\end{proposition}

A larger exact calculation gives the following natural slice.  Let
\[
\begin{aligned}
\mathscr S=\{P\in\mathfrak X_2^{(0)}:\;&
(C+[Q,P])_a=(C+[Q,P])_d=(C+[Q,P])_q=0,\\
&
(C+[Q,P])_h=(C+[Q,P])_k=0\}.
\end{aligned}
\]
Then $\mathscr S$ is a nonempty affine space of dimension $20$, and
\[
\Lambda_4(\mathcal O_4(P))=1\qquad(P\in\mathscr S).
\]
The tangent space at $P_0=-d^2e_a$ to the equivariant rank-at-most-six locus has
dimension $22$; the two extra directions are precisely the infinitesimal
weight-preserving target changes that add the surviving $y$-row to the $q$-
and $k$-rows.  Thus $\mathscr S$ is the expected $20$-dimensional transverse
slice modulo linear target reparametrization.

This changes the interpretation of the obstruction: cubic compression is not
isolated or difficult.  It occurs in a family, while a secondary quartic class
is constant and nonzero across the family.
~~~

[Back to the text-source index](../../index.md)
