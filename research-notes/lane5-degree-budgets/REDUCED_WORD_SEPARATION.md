# Reduced-word weight separation for Lane 5

## Setup

Let

\[
B=k[x,y,z],\qquad S=k[P,Q,R]\subset B,
\]

where \(k\) has characteristic zero and

\[
\begin{aligned}
P&=(1+xy)^3z+y^2(1+xy)(4+3xy),\\
Q&=y+3x(1+xy)^2z+3xy^2(4+3xy),\\
R&=2x-3x^2y-x^3z.
\end{aligned}
\]

Use the source-torus grading

\[
w(x)=-1,\qquad w(y)=1,\qquad w(z)=2.
\]

Then \(S\) is graded, with

\[
w(P)=2,\qquad w(Q)=1,\qquad w(R)=-1,
\]

and the exact standard-filtration certificate gives

\[
S\cap B_{\le6}=\operatorname{span}_k\{1,Q,R\}.
\]

A derivation \(\delta\) is **homogeneous of shift** \(d\) if
\(\delta(B_n)\subseteq B_{n+d}\) for every weight space \(B_n\).
Every monomial elementary derivation

\[
\delta=c m\,\partial_{x_i},\qquad
m\in k[x_j,x_k],
\]

is locally nilpotent and homogeneous of shift

\[
d=w(m)-w(x_i).
\]

## Taylor no-return theorem

Let \(V\subseteq B\) be torus-stable and supported in a weight interval
\([a,b]\) of width \(W=b-a\). Let \(C\subseteq B\) be a graded subalgebra,
let \(\delta_1,\ldots,\delta_t\) be homogeneous locally nilpotent derivations
of shifts \(d_1,\ldots,d_t\), and put

\[
\Phi=\exp(\delta_t)\cdots\exp(\delta_1).
\]

For this ordered word and this finite-dimensional \(V\), let
\(\mathcal A_V\subset\mathbf N^t\) be the finite set of multiindices
\(\alpha\) for which

\[
\delta_1^{\alpha_1}\cdots\delta_t^{\alpha_t}
\]

is nonzero on some element of \(V\). If

\[
|\alpha\cdot d|>W
\tag{1}
\]

for every nonzero \(\alpha\in\mathcal A_V\), then

\[
\boxed{\Phi(C)\cap V\subseteq C\cap V.}
\tag{2}
\]

### Proof

Take \(h\in\Phi(C)\cap V\) and put \(g=\Phi^{-1}h\in C\). The ordered
Taylor expansion is finite:

\[
g=\sum_{\alpha\in\mathcal A_V}
  \frac{(-1)^{|\alpha|}}{\alpha_1!\cdots\alpha_t!}
  \delta_1^{\alpha_1}\cdots\delta_t^{\alpha_t}h.
\tag{3}
\]

The zero-multiindex term is \(h\), supported in \([a,b]\). Every nonzero
\(\alpha\)-term is supported in the translated interval
\([a,b]+\alpha\cdot d\), which is disjoint from \([a,b]\) by (1). Hence the
weight components of \(g\) inside \([a,b]\) are exactly the components of
\(h\). Since \(g\in C\) and \(C\) is graded, those components lie in \(C\),
so \(h\in C\cap V\). \(\square\)

This strictly extends the one-sided weight-window lemma: positive and negative
shifts may be mixed, provided no nonzero ordered Taylor word returns to the
original window.

The set \(\mathcal A_V\) is finite because \(V\) is finite dimensional and
the ordered derivations are locally nilpotent.

## Exactness under full Taylor separation

Assume now

\[
C\cap B_{\le D}=k\oplus kq\oplus kr,
\]

where \(q,r\) are homogeneous of distinct weights. Suppose the stronger
condition

\[
| (\alpha-\beta)\cdot d |>3D
\tag{4}
\]

holds for every distinct \(\alpha,\beta\in\mathcal A_{B_{\le D}}\). If, for
some \(j\),

\[
\delta_jq\notin C,\qquad \delta_jr\notin C,
\tag{5}
\]

then

\[
\boxed{\Phi(C)\cap B_{\le D}=k.}
\]

Indeed, (4) separates every Taylor multiindex block in (3). Gradedness of
\(C\) puts each block in \(C\), including the zero block, so
\(h=a+bq+cr\). The \(e_j\)-block gives \(\delta_jh\in C\). Its
\(q\)- and \(r\)-parts have distinct weights, and (5) forces \(b=c=0\).

## Arbitrarily long commuting compositions with mixed signs

Fix one target coordinate \(x_i\). Let

\[
\delta_r=c_r m_r\partial_{x_i}\qquad(1\le r\le t)
\]

with \(c_r\ne0\), where each \(m_r\) is a monomial in the other two
coordinates. These derivations commute, and

\[
\exp(\delta_t)\cdots\exp(\delta_1)
 =\exp\!\left(\sum_{r=1}^t\delta_r\right)
\]

sends

\[
x_i\longmapsto x_i+\sum_{r=1}^t c_rm_r.
\]

On \(B_{\le D}\), only multiindices with \(|\alpha|\le D\) occur. Therefore
it is enough that

\[
|\gamma\cdot d|>3D
\tag{6}
\]

for every nonzero \(\gamma\in\mathbf Z^t\) with
\(\|\gamma\|_1\le2D\). A convenient sufficient condition, after ordering the
shifts by construction, is

\[
|d_1|>3D,\qquad
|d_r|>2D\sum_{s<r}|d_s|+3D\quad(r\ge2).
\tag{7}
\]

For Lane 5, the common-fiber witnesses from the pure-monomial theorem show
that \(m_r\partial_{x_i}Q\) and \(m_r\partial_{x_i}R\) are outside \(S\) for
every nonzero monomial in the other two source coordinates. Hence (6), or the
stronger condition (7), gives

\[
\boxed{
\exp\!\left(\sum c_rm_r\partial_{x_i}\right)(S)\cap B_{\le6}=k.
}
\]

This is especially useful for mixed positive/negative shift support, which is
not covered by the one-sided high-weight semigroup theorem.

For example, use the target coordinate \(y\). The shifts of
\(z^M\partial_y\) and \(x^N\partial_y\) are respectively \(2M-1\) and
\(-N-1\). The alternating superincreasing shifts

\[
19,-247,3211,-41743
\]

are realized by

\[
y\longmapsto y+c_1z^{10}+c_2x^{246}+c_3z^{1606}+c_4x^{41742}.
\]

For arbitrary nonzero coefficients, its transformed image algebra has only
constants in degree at most six. The construction continues to arbitrary word
length by the recurrence (7).

## A genuinely mixed-sign noncommuting family

Let

\[
\delta_1=x^N\partial_y,\qquad
\delta_2=y^M\partial_z,
\]

and

\[
\Psi_{N,M}=\exp(\delta_1)\exp(\delta_2).
\]

The derivations do not commute and have shifts of opposite signs. On
coordinates,

\[
\Psi_{N,M}(x,y,z)
 =\bigl(x,\ y+x^N,\ z+(y+x^N)^M\bigr).
\]

Their shifts are

\[
d_1=-N-1,\qquad d_2=M-2.
\]

For \(h\in B_{\le6}\), the expansion of
\(\Psi_{N,M}^{-1}h=\exp(-\delta_2)\exp(-\delta_1)h\) uses only

\[
0\le\alpha_1\le6,\qquad0\le\alpha_2\le6.
\]

Indeed, \(\delta_1\) is applied first and does not increase the degree in
\(z\), after which \(\delta_2\) can act at most six times.

Assume

\[
N\ge18,\qquad M\ge21,
\]

and impose the finite arithmetic nonresonance condition

\[
|a(N+1)-b(M-2)|>18
\quad\text{for every }1\le a,b\le6.
\tag{8}
\]

For distinct \(\alpha,\beta\in\{0,\ldots,6\}^2\), a shift collision can only
occur when the two coefficient differences have the same sign. Condition (8)
then gives (4); opposite signs add the two magnitudes, while a zero coefficient
leaves a multiple of \(N+1\) or \(M-2\), both greater than 18.

A simple sufficient subfamily is

\[
M\ge21,\qquad N\ge6M+6,
\]

because then \(N+1-6(M-2)>18\). The exact common-fiber witness already used
for the one-step theorem gives

\[
x^N\partial_yQ,\ x^N\partial_yR,
\ y^M\partial_zQ,\ y^M\partial_zR\notin S
\]

for all \(N,M\ge2\). The reduced-word theorem therefore yields

\[
\boxed{
\Psi_{N,M}(S)\cap B_{\le6}=k
\qquad\text{whenever (8) holds}.
}
\]

This is an infinite theorem for genuinely noncommuting triangular words with
both positive and negative torus shifts. It lies outside both one-sided
high-weight subgroups. Arbitrary affine source transformations applied after
\(\Psi_{N,M}\) preserve the conclusion.

## Scope and next target

The theorem covers:

- arbitrary finite reduced words satisfying the Taylor no-return condition
  (1), with exactness under the stronger separation condition (4);
- arbitrarily long commuting polynomial shears with mixed-sign,
  superincreasing support;
- an explicit infinite noncommuting mixed-sign triangular family.

It does not yet control words whose ordered Taylor shifts return to or overlap
the degree-six weight window. Those resonant mixed-sign reduced words are the
next finite or geometric frontier.
