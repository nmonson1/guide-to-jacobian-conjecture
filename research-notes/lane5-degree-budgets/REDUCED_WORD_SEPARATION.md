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

## Reduced-word separation theorem

Let \(D\ge0\), let \(C\subseteq B\) be a graded subalgebra, and suppose

\[
C\cap B_{\le D}=k\oplus kq\oplus kr,
\]

where \(q,r\) are homogeneous of distinct weights. Let
\(\delta_1,\ldots,\delta_t\) be homogeneous locally nilpotent derivations of
shifts \(d_1,\ldots,d_t\), and put

\[
\Phi=\exp(\delta_t)\cdots\exp(\delta_1).
\]

For the fixed ordered word, define \(\mathcal A_D\subset\mathbf N^t\) to be
the finite set of multiindices \(\alpha\) for which

\[
\delta_1^{\alpha_1}\cdots\delta_t^{\alpha_t}
\]

is nonzero on at least one element of \(B_{\le D}\). Suppose

\[
\left|\sum_{j=1}^t(\alpha_j-\beta_j)d_j\right|>3D
\tag{1}
\]

for every distinct \(\alpha,\beta\in\mathcal A_D\). If, for some index \(j\),

\[
\delta_jq\notin C,\qquad \delta_jr\notin C,
\tag{2}
\]

then

\[
\boxed{\Phi(C)\cap B_{\le D}=k.}
\]

### Proof

Take \(h\in\Phi(C)\cap B_{\le D}\) and set \(g=\Phi^{-1}h\in C\). Expanding
the ordered inverse word gives the finite sum

\[
g=\sum_{\alpha\in\mathcal A_D}
  \frac{(-1)^{|\alpha|}}{\alpha_1!\cdots\alpha_t!}
  \delta_1^{\alpha_1}\cdots\delta_t^{\alpha_t}h.
\tag{3}
\]

All weights occurring in \(B_{\le D}\) lie in \([-D,2D]\), an interval of
width \(3D\). The \(\alpha\)-summand in (3) has weights in

\[
[-D,2D]+\alpha\cdot d.
\]

Condition (1) makes these intervals pairwise disjoint. Since \(C\) is graded
and \(g\in C\), every summand in (3) belongs to \(C\). The zero-multiindex
summand gives \(h\in C\cap B_{\le D}\), so

\[
h=a+bq+cr.
\]

The \(e_j\)-summand gives \(\delta_jh\in C\). Its two nonconstant terms
\(b\delta_jq\) and \(c\delta_jr\) have distinct weights, so gradedness puts
each in \(C\). Condition (2) forces \(b=c=0\). Thus \(h\in k\). \(\square\)

The set \(\mathcal A_D\) is finite: apply the finitely many ordered
exponentials successively to a basis of the finite-dimensional space
\(B_{\le D}\); local nilpotence makes every expansion finite.

## Arbitrarily long commuting compositions

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
\tag{4}
\]

for every nonzero \(\gamma\in\mathbf Z^t\) with
\(\|\gamma\|_1\le2D\). A convenient sufficient condition, after ordering the
shifts, is

\[
|d_1|>3D,\qquad
|d_r|>2D\sum_{s<r}|d_s|+3D\quad(r\ge2).
\tag{5}
\]

For Lane 5, the common-fiber witnesses from the pure-monomial theorem show
that \(m_r\partial_{x_i}Q\) and \(m_r\partial_{x_i}R\) are outside \(S\) for
every monomial used there. Hence (4), or the stronger condition (5), gives

\[
\boxed{
\exp\!\left(\sum c_rm_r\partial_{x_i}\right)(S)\cap B_{\le6}=k.
}
\]

This covers words of arbitrary length, not merely a fixed finite scan.

For example, if

\[
17\le N_1<N_2<\cdots<N_t
\]

and

\[
N_r+2>12\sum_{s<r}(N_s+2)+18\qquad(r\ge2),
\]

then for all nonzero \(c_r\),

\[
z\longmapsto z+\sum_{r=1}^t c_rx^{N_r}
\]

satisfies

\[
\Phi(S)\cap B_{\le6}=k.
\]

Thus compositions of arbitrarily many commuting nonlinear shears cannot lower
the orbit degree to six when their torus shifts are superincreasing.

## A genuinely noncommuting two-step family

Let

\[
\delta_1=y^N\partial_x,\qquad
\delta_2=z^M\partial_y,
\]

and

\[
\Phi_{N,M}=\exp(\delta_2)\exp(\delta_1).
\]

The derivations do not commute. On coordinates,

\[
\Phi_{N,M}(x,y,z)
 =\bigl(x+(y+z^M)^N,\ y+z^M,\ z\bigr).
\]

Their shifts are

\[
d_1=N+1,\qquad d_2=2M-1.
\]

For \(h\in B_{\le6}\), the expansion of
\(\Phi_{N,M}^{-1}h=\exp(-\delta_1)\exp(-\delta_2)h\) uses only

\[
0\le\alpha_1\le6,\qquad0\le\alpha_2\le6.
\]

Indeed, \(\delta_2\) is applied first and does not increase the degree in
\(x\), after which \(\delta_1\) can act at most six times.

Assume

\[
N\ge18,\qquad M\ge3N+13.
\tag{6}
\]

Then

\[
d_1>18,\qquad d_2>6d_1+18.
\]

For distinct \(\alpha,\beta\in\{0,\ldots,6\}^2\), if
\(\alpha_2=\beta_2\), their shift difference has magnitude at least
\(d_1>18\). Otherwise it has magnitude at least

\[
d_2-6d_1>18.
\]

Thus condition (1) holds. The exact common-fiber witness already used for the
one-step theorem gives

\[
y^N\partial_xQ,\ y^N\partial_xR,
\ z^M\partial_yQ,\ z^M\partial_yR\notin S
\]

for all \(N,M\ge2\). The reduced-word theorem therefore yields

\[
\boxed{
\Phi_{N,M}(S)\cap B_{\le6}=k
\qquad(N\ge18,\ M\ge3N+13).
}
\]

This is an infinite theorem for genuinely noncommuting, nested triangular
source automorphisms. Arbitrary affine source transformations applied after
\(\Phi_{N,M}\) preserve the conclusion.

## Scope and next target

The theorem covers:

- arbitrarily long commuting monomial-shear words with separated shifts;
- general finite reduced words satisfying the exact support-separation
  condition (1);
- an explicit infinite noncommuting triangular family.

It does not yet control words whose different Taylor multiindices have nearby
or equal total torus shifts. Those resonant reduced words are the next finite
or geometric frontier.
