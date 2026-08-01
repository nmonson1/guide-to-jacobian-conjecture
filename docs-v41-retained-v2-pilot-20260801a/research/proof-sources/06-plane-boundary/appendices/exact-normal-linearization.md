---
title: "Text proof source — 06-plane-boundary/appendices/exact-normal-linearization.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/06-plane-boundary/appendices/exact-normal-linearization.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `6e97f0a19cbeb06c71d065248090400c9de54cdb30085c7444e9b9b25d7ff69f` · 12,167 bytes

## Exact label anchors

<a id="label-app-exact-normal-linearization"></a>
- `app:exact-normal-linearization` — source line 2
<a id="label-eq-exact-w"></a>
- `eq:exact-W` — source line 21
<a id="label-eq-exact-t"></a>
- `eq:exact-T` — source line 25
<a id="label-eq-exact-h"></a>
- `eq:exact-H` — source line 30
<a id="label-thm-exact-normal-linearization"></a>
- `thm:exact-normal-linearization` — source line 41
<a id="label-eq-exact-inverse"></a>
- `eq:exact-inverse` — source line 45
<a id="label-eq-exact-linear-equation"></a>
- `eq:exact-linear-equation` — source line 53
<a id="label-eq-exact-wedge-left"></a>
- `eq:exact-wedge-left` — source line 80
<a id="label-eq-exact-wedge-right"></a>
- `eq:exact-wedge-right` — source line 84
<a id="label-cor-decoupled-normal-orders"></a>
- `cor:decoupled-normal-orders` — source line 102
<a id="label-eq-decoupled-normal-orders"></a>
- `eq:decoupled-normal-orders` — source line 110
<a id="label-eq-exact-linear-leading"></a>
- `eq:exact-linear-leading` — source line 138
<a id="label-eq-support-map-a"></a>
- `eq:support-map-A` — source line 153
<a id="label-eq-support-map-b"></a>
- `eq:support-map-B` — source line 156
<a id="label-eq-support-kuranishi"></a>
- `eq:support-kuranishi` — source line 161
<a id="label-rem-conductor-limitation"></a>
- `rem:conductor-limitation` — source line 190
<a id="label-eq-828-exact"></a>
- `eq:828-exact` — source line 217
<a id="label-prop-828-layer-injectivity"></a>
- `prop:828-layer-injectivity` — source line 225
<a id="label-eq-828-cokernel-dimension"></a>
- `eq:828-cokernel-dimension` — source line 239
<a id="label-eq-828-degree-identity"></a>
- `eq:828-degree-identity` — source line 265
<a id="label-rem-828-structural-prediction"></a>
- `rem:828-structural-prediction` — source line 292
<a id="label-prop-finite-jet-realization"></a>
- `prop:finite-jet-realization` — source line 323
<a id="label-q-filtered-finite-jet-realization"></a>
- `q:filtered-finite-jet-realization` — source line 362

## Complete source

~~~tex
\section{Exact normal linearization and finite-jet realization}
\label{app:exact-normal-linearization}

The layer operator of \cref{sec:normal-complex} is the differential of an
exact formal normal form.  This removes one apparent source of difficulty:
on a single smooth boundary component, before Newton-support conditions are
imposed, the normal orders do not interact nonlinearly.

\subsection{An exact change of variables}

Let \(K=k(E)\) be the function field of the boundary curve, equipped with
the differential \(d=d_E\), and work in \(K[[s]]\).  Retain the notation
\[
S=\alpha+\beta,\qquad M_0=A_0B_0,
\qquad
\omega=\alpha\,d\log B_0-\beta\,d\log A_0
       =\frac{\Psi}{M_0}\,dz.
\]
For units \(A=A_0+O(s)\) and \(B=B_0+O(s)\), define
\begin{equation}
\label{eq:exact-W}
W=\frac{M_0}{AB}\in1+sK[[s]],
\end{equation}
\begin{equation}
\label{eq:exact-T}
T=sW^{1/S}\in s+s^2K[[s]],
\end{equation}
and
\begin{equation}
\label{eq:exact-H}
H=\frac1S\left[
\alpha\log\left(\frac{B}{B_0}\right)
-\beta\log\left(\frac{A}{A_0}\right)
\right]\in sK[[s]].
\end{equation}
The fractional power and logarithms are the unique formal series with the
displayed constant terms.  Since \(T=s+O(s^2)\), it has a unique formal
inverse.

\begin{theorem}[Exact normal linearization]
\label{thm:exact-normal-linearization}
The transformation
\eqref{eq:exact-W}--\eqref{eq:exact-H} is formally invertible, with
\begin{equation}
\label{eq:exact-inverse}
s=TW^{-1/S},\qquad
A=A_0W^{-\alpha/S}e^{-H},\qquad
B=B_0W^{-\beta/S}e^H.
\end{equation}
After regarding \(H\) and \(W\) as series in \(T\), the full determinant
equation \eqref{eq:master} is equivalent to the linear equation
\begin{equation}
\label{eq:exact-linear-equation}
\boxed{
\left(Sd+d\log M_0\,T\partial_T\right)H
=
\omega\left(1-\frac1S T\partial_T\right)(W-1).}
\end{equation}
\end{theorem}

\begin{proof}
The inverse formulas follow by solving the two linear equations in
\(\log(A/A_0)\) and \(\log(B/B_0)\).  Put
\[
P=s^{-\alpha}A,\qquad Q=s^{-\beta}B.
\]
Then \eqref{eq:exact-inverse} gives
\[
P=T^{-\alpha}A_0e^{-H},\qquad
Q=T^{-\beta}B_0e^H.
\]
In the coordinates \((z,T)\), direct logarithmic differentiation gives
\begin{align}
dP\wedge dQ
={}&T^{-S-1}M_0\bigl(
\alpha\,d\log B_0-\beta\,d\log A_0+S\,dH\notag\\
&\hspace{42mm}
+d\log M_0\,T\partial_TH
\bigr)\wedge dT.
\label{eq:exact-wedge-left}
\end{align}
On the other hand, differentiating \(s=TW^{-1/S}\) at fixed \(z\) gives
\begin{equation}
\label{eq:exact-wedge-right}
s^{-S-1}\,dz\wedge ds
=T^{-S-1}\left(W-\frac TS\partial_TW\right)dz\wedge dT.
\end{equation}
Equation \eqref{eq:master} is precisely
\[
dP\wedge dQ=s^{-S-1}\Psi(z)\,dz\wedge ds.
\]
Substitute \eqref{eq:exact-wedge-left} and
\eqref{eq:exact-wedge-right}, and cancel the order-zero identity
\[
M_0\left(\alpha\,d\log B_0-\beta\,d\log A_0\right)
=\Psi(z)\,dz.
\]
The result is \eqref{eq:exact-linear-equation}.
\end{proof}

\begin{corollary}[Decoupled normal orders]
\label{cor:decoupled-normal-orders}
Write
\[
H=\sum_{r\ge1}h_rT^r,\qquad
W=1+\sum_{r\ge1}w_rT^r.
\]
Then the full determinant equation is equivalent to the independent family
\begin{equation}
\label{eq:decoupled-normal-orders}
\boxed{
S\left(d+\frac rS\,d\log M_0\right)h_r
=\frac{S-r}{S}w_r\omega
\qquad(r\ge1).}
\end{equation}
At resonance \(r=S\), this becomes
\[
d(M_0h_S)=0.
\]
Consequently, over \(K\) and without sparse support restrictions, solutions
at the separate normal orders assemble uniquely into one formal solution in
the \((H,W,T)\)-coordinates.
\end{corollary}

\begin{proof}
Take the coefficient of \(T^r\) in
\eqref{eq:exact-linear-equation}.  Formal invertibility then gives the last
assertion.
\end{proof}

The relation with \cref{prop:gauge-normal-form} is exact.  If
\[
u_r=\frac{a_r}{A_0},\qquad v_r=\frac{b_r}{B_0},\qquad
\xi_r=u_r+v_r,\qquad \eta_r=\alpha v_r-\beta u_r,
\]
then triangularity of the change of variables gives
\begin{equation}
\label{eq:exact-linear-leading}
h_r=\frac{\eta_r}{S}+\text{lower-layer terms},
\qquad
w_r=-\xi_r+\text{lower-layer terms}.
\end{equation}
The homogeneous part of \eqref{eq:decoupled-normal-orders} is therefore the
gauge normal form of the universal layer operator.

\subsection{The nonlinear support map}

The exact linearization does not preserve the polynomial Newton windows.
Indeed, the inverse formulas give universal triangular expressions
\begin{align}
\frac{a_r}{A_0}
&=-h_r-\frac{\alpha}{S}w_r
+F_{A,r}(h_{<r},w_{<r}),\label{eq:support-map-A}\\
\frac{b_r}{B_0}
&=h_r-\frac{\beta}{S}w_r
+F_{B,r}(h_{<r},w_{<r}),\label{eq:support-map-B}
\end{align}
where the \(F_{\bullet,r}\) are polynomials in lower normal orders.
If \(U_{A,r},U_{B,r}\subset K\) are the permitted coefficient windows, set
\begin{equation}
\label{eq:support-kuranishi}
\begin{aligned}
\kappa_r(H,W)&=(\kappa_{A,r},\kappa_{B,r}),\\
\kappa_{A,r}
&=\left[
A_0\!\left(-h_r-\frac{\alpha}{S}w_r+F_{A,r}\right)
\right]_{K/U_{A,r}},\\
\kappa_{B,r}
&=\left[
B_0\!\left(h_r-\frac{\beta}{S}w_r+F_{B,r}\right)
\right]_{K/U_{B,r}}.
\end{aligned}
\end{equation}
Then the original Newton-support condition is exactly
\(\kappa_r(H,W)=0\) for all \(r\).

For every finite \(N\), the change from the first \(N\) pairs
\((a_r,b_r)\) to the first \(N\) pairs \((h_r,w_r)\) is a triangular
polynomial automorphism of jet spaces.  Its diagonal block is
\[
(u_r,v_r)\longmapsto
\left(\frac{\alpha v_r-\beta u_r}{S},-(u_r+v_r)\right),
\]
whose determinant is \(1\).  Thus a stored finite boundary system may be
conjugated into the exact coordinates without changing its scheme.  The
determinant equations become linear; the nonlinear information moves into
the triangular support map \(\kappa=(\kappa_r)\).

\begin{remark}[What the conductor does not prove]
\label{rem:conductor-limitation}
Normalization and conductor quotients can make lattice descent finite when
a semigroup is not saturated.  They do not force an infinite supported
formal series to terminate polynomially.  In the full \((8,28)\) chart the
toric coordinate change is unimodular and the relevant high-order
cross-sections are complete integer intervals.  The decisive obstruction is
therefore a finite-window and finite-jet realization problem, not merely a
hole in a normalized semigroup.
\end{remark}

\subsection{The full \texorpdfstring{\((8,28)\)}{(8,28)} layer maps}

For the degree-\(21\) lower face of
\cref{app:degree-twenty-one}, put
\[
\alpha=2,\qquad\beta=3,\qquad S=5,\qquad
A_0=zp,\qquad B_0=z^2q.
\]
The face equation \eqref{eq:degree21-face} gives
\[
M_0=z^3pq,\qquad
\Omega=2A_0\,dB_0-3B_0\,dA_0=z^2\,dz,
\qquad
\omega=\frac{dz}{zpq}.
\]
The exact equation \eqref{eq:exact-linear-equation} is
\begin{equation}
\label{eq:828-exact}
5H_z+
T\left(\frac3z+\frac{p'}p+\frac{q'}q\right)H_T
=
\frac1{zpq}\left(W-\frac T5W_T-1\right).
\end{equation}

\begin{proposition}[Injectivity of the terminal layer maps]
\label{prop:828-layer-injectivity}
Assume \(p,q\) satisfy \eqref{eq:degree21-face}.  For \(r\ge5\), let
\[
a\in k[z]_{\le10-r},\qquad
b\in k[z]_{\le15-r},
\]
where a negative degree bound means the zero space.  Then
\[
\mathscr D_r^{2,3}(a,b)=0
\quad\Longrightarrow\quad
a=b=0.
\]
In particular, for \(5\le r\le11\),
\begin{equation}
\label{eq:828-cokernel-dimension}
\dim\operatorname{coker}\mathscr D_r^{2,3}=r-1.
\end{equation}
\end{proposition}

\begin{proof}
At \(r=5\), put
\[
C=2A_0b-3B_0a.
\]
By resonance,
\(\mathscr D_5(a,b)=dC\).  If this vanishes, then \(C\) is constant; both
terms are divisible by \(z\), so \(C=0\).  Hence
\[
2pb=3zqa.
\]
Equation \eqref{eq:degree21-face} implies
\(\gcd(p,zq)=1\), so \(p\mid a\).  Since
\(\deg a\le5<7=\deg p\), one has \(a=0\), and then \(b=0\).

Now suppose \(r>5\), and set
\[
C=2A_0b-3B_0a,\qquad E=A_0b+B_0a.
\]
The gauge formula and \(\mathscr D_r(a,b)=0\) give
\begin{equation}
\label{eq:828-degree-identity}
E
=zpq\left(
C\frac{M_0'}{M_0}+\frac5{r-5}C'
\right).
\end{equation}
If \(C\ne0\) and \(d=\deg C\), the right side has degree exactly
\(d+17\): its leading coefficient contains the nonzero factor
\[
20+\frac{5d}{r-5}.
\]
On the other hand,
\[
\deg E\le
\max\{\deg A_0+\deg b,\deg B_0+\deg a\}
\le23-r.
\]
Thus \(d\le6-r\).  This is impossible for \(r\ge7\); for \(r=6\) it
forces \(d=0\), whereas \(C\) is divisible by \(z\).  Hence \(C=0\), and
the coprimality and degree argument above again gives \(a=b=0\).

For \(5\le r\le11\), \cref{prop:index} applies to the stated full-support
windows and gives the target-minus-domain dimension \(r-1\).
Injectivity proves \eqref{eq:828-cokernel-dimension}.
\end{proof}

\begin{remark}[Comparison with the archived terminal equations]
\label{rem:828-structural-prediction}
For the archived terminal specialization, the exact residue replay gives
ordinary cokernel dimensions \(5,6,7\) at layers \(6,7,8\), but the
specialized nonlinear forcing has only
\[
4,\quad5,\quad6,
\]
nonzero compatibility pairings.  Every pairing is recovered as
\(\operatorname{Res}_0(\lambda(-\Phi_r))\) for an explicit left-null
principal part.  After imposing the recorded normalization, the distinct
surviving equations have layer counts \(1,3,5,6\) at \(r=5,6,7,8\);
these fifteen polynomials agree coefficientwise with the archived system.
Thus the residue origin of the archived equations is an exact
computer-assisted theorem in the original layer coordinates.

What has not been checked is a term-by-term conjugation of this normalized
system into the new \((H,W,T)\)-coordinates.  That comparison concerns the
triangular support map, normalization directions, and admissible
approximate-root action; it is not needed for the residue reconstruction
just stated.
\end{remark}

\subsection{Ordinary finite jets are polynomially realizable}

Full algebraization of an infinite formal series is stronger than is needed
to lower a lexicographically ordered boundary complexity.  The first
weight at which a leading datum is cancelled is determined by a finite jet.
For unrestricted local area-preserving coordinates, such finite jets have
no algebraization obstruction.

\begin{proposition}[Finite-jet realization]
\label{prop:finite-jet-realization}
Let \(k\) be an infinite field of characteristic zero, and let
\(\widehat\phi\in\operatorname{Aut}k[[x,y]]\) fix the origin and satisfy
\(\det J\widehat\phi=1\).  For every \(N\), there is a polynomial
automorphism \(\phi_N\in\operatorname{Aut}k[x,y]\), with
\(\det J\phi_N=1\), whose \(N\)-jet agrees with that of
\(\widehat\phi\).  It may be chosen as a finite composition of linear
\(\mathrm{SL}_2(k)\) maps and polynomial shears.
\end{proposition}

\begin{proof}
Match the linear part first.  Inductively, suppose the first unmatched
homogeneous term has degree \(n\):
\[
(x,y)+(f_n,g_n)+O(\mathfrak m^{n+1}).
\]
The Jacobian-one condition gives
\(\partial_xf_n+\partial_yg_n=0\), so for a homogeneous binary form
\(K_{n+1}\),
\[
(f_n,g_n)=(\partial_yK_{n+1},-\partial_xK_{n+1}).
\]
Over an infinite field, powers of linear forms span the binary forms of
each degree.  Write
\[
K_{n+1}=\sum_i c_i\ell_i^{\,n+1},
\qquad \ell_i=a_ix+b_iy.
\]
The Hamiltonian flow of each summand is the exact polynomial shear
\[
(x,y)\longmapsto
(x,y)+c_i(n+1)\ell_i^n(b_i,-a_i),
\]
because \(\ell_i\) is constant in the direction \((b_i,-a_i)\).  Composing
these shears matches the degree-\(n\) discrepancy and changes only higher
degrees.  Induction through degree \(N\) proves the claim.
\end{proof}

\begin{question}[Filtered finite-jet realization]
\label{q:filtered-finite-jet-realization}
\Cref{prop:finite-jet-realization} concerns the full local
Jacobian-one automorphism group.  The approximate-root operations allowed
by a complete chain form a smaller valuation-filtered subgroup.  The
remaining realization problem is therefore the finite family of maps
\[
\operatorname{gr}_r\mathcal G_{\mathrm{approx}}
\longrightarrow
\operatorname{gr}_r\mathcal G_{\mathrm{formal}},
\]
where the two groups denote admissible polynomial approximate-root
operations and formal complexity-lowering operations, respectively.
Surjectivity through the first complexity-dropping weight realizes the
drop; a failure of surjectivity produces a canonical finite obstruction.
\end{question}
~~~

[Back to the text-source index](../../index.md)
