# Obligation 2: The representable coefficient-level degeneration stack

> **Status:** unrefereed, AI-assisted research note; no independent review recorded.  
> **Scope:** Program 4 normalized cubic-frame coefficient spaces. The statements do not identify the construction with the fppf orbit quotient or the full unrigidified stable left-right stack.

[Back to the six-obligation index](index.md)


## 2.1 The fixed multigraded graph algebra

Let

\[
S_N=\mathcal O(Y_N)
\]

and let

\[
\delta=\det Z=(-1)^Nq_N.
\]

On

\[
U_N=D(\delta)\subset Y_N,
\]

`\Theta_N` is invertible. Hence the source coefficients `(q_i,r_j)` are rational functions on `Y_N`, regular on `U_N`.

More explicitly,

\[
P=Z^{-N}Y
=\frac{\operatorname{adj}(Z)^N Y}{\delta^N}.
\]

Thus every source coefficient has an explicit polynomial numerator and the single denominator `delta^N`. This gives a uniform concrete presentation of all graph generators.

For each `0\le d<N`, put `m=N-d` and form the source-tail vector

\[
x_d=
(q_{d+1},\ldots,q_N;
 r_{N-1},\ldots,r_d).
\]

Give its entries the **internal direction weights**

\[
w_d=(1,2,\ldots,m;\,m+1,m,\ldots,2).
\]

Because `q_N` occurs in every root-tail vector and is invertible on `U_N`, no vector `x_d` vanishes identically there. Thus `x_d` defines a rational map

\[
\phi_d:Y_N\dashrightarrow\mathbb P(w_d)
\]

whose domain contains `U_N`.

Introduce one grading variable `t_d` for every `d`. Define the multigraded algebra

\[
\mathcal R_N
=
S_N\bigl[
 x_{d,i}t_d^{w_{d,i}}
 :0\le d<N
\bigr]
\subset
S_N[\delta^{-1}][t_0,\ldots,t_{N-1}].
\]

Equivalently, `\mathcal R_N` is the image of a multigraded polynomial algebra over `S_N`; hence it is finitely generated. Define the stacky multi-Proj

\[
\mathfrak G_N
=
\operatorname{MultiProj}^{\mathrm{st}}_{Y_N}(\mathcal R_N).
\]

Concretely, it is the closure of the graph of

\[
\Phi_N=(\phi_0,\ldots,\phi_{N-1})
\]

inside

\[
Y_N\times
\prod_{d=0}^{N-1}\mathbb P(w_d),
\]

with the weighted projective factors retained as stacks.

No normalization is part of the definition.

### Explicit `N=3` instance

For

\[
Z=
\begin{pmatrix}
0&0&-q_3\\
1&0&-q_2\\
0&1&-q_1
\end{pmatrix},
\qquad
P=Z^{-3}Y,
\]

write

\[
p_i=\frac{n_i}{q_3^3}.
\]

The exact numerators are

\[
\begin{aligned}
n_0={}&2q_1q_2q_3y_0-q_1q_3^2y_1-q_2^3y_0
      +q_2^2q_3y_1-q_2q_3^2y_2-q_3^2y_0,\\
n_1={}&q_1^2q_3y_0-q_1q_2^2y_0+q_1q_2q_3y_1
      -q_1q_3^2y_2+q_2q_3y_0-q_3^2y_1,\\
n_2={}&q_1q_3y_0-q_2^2y_0+q_2q_3y_1-q_3^2y_2.
\end{aligned}
\]

The three direct factors are

\[
\phi_2=[q_3:p_0]\in\mathbb P(1,2),
\]

\[
\phi_1=[q_2:q_3:p_0:p_1]\in\mathbb P(1,2,3,2),
\]

and

\[
\phi_0=[q_1:q_2:q_3:p_0:p_1:p_2]
\in\mathbb P(1,2,3,4,3,2).
\]

At the generic one-root wall `q_3=0`, with `q_2` a unit,

\[
n_0=-q_2^3y_0.
\]

The coarse first factor is therefore locally

\[
[q_3^5:n_0],
\]

which recovers the exponent `N+2=5` directly from the bounded orbit map.

## Theorem 2.1 — Representability, properness, and base change

The stack `\mathfrak G_N` represents the following functor. An object over a scheme `T` is:

1. a morphism `T -> Y_N`, i.e. a bounded quotient-coefficient family;
2. for every `d`, an invertible sheaf `L_d` on `T`;
3. sections
   \[
   u_{d,i}\in\Gamma(T,L_d^{\otimes w_{d,i}})
   \]
   which do not vanish simultaneously for fixed `d`;
4. all homogeneous relations in the fixed kernel defining `\mathcal R_N`.

The stack is algebraic, finite type, separated, and proper over `Y_N`. Its pullback as this fixed represented object commutes with arbitrary base change.

### Proof

A weighted projective stack represents a line bundle together with weighted sections that are not all zero. The product of the weighted projective stacks therefore represents items 2 and 3. The homogeneous kernel relations cut out a closed substack, proving representability and finite type.

Each weighted projective stack is proper and separated over the base. Hence a closed substack of their product over `Y_N` is proper and separated over `Y_N`.

Finally, relative Proj of a fixed graded algebra commutes with pullback. The same argument applies one grading at a time to the multigraded construction. ∎

### Base-change qualification

For an arbitrary morphism `T -> Y_N`, the pullback

\[
\mathfrak G_N\times_{Y_N}T
\]

represents the pullback of the fixed homogeneous equations. It need not equal a **newly recomputed schematic closure** of the graph over `T` when the pullback of `U_N` is empty or not schematically dense.

If `T` is flat over `Y_N`, or more generally if the generic graph remains schematically dense and no new torsion is introduced, the two descriptions agree. The represented functor, however, is defined for every base change.

This is the reason normalization and “recompute the image after every base change” are excluded from the primary definition.

## 2.2 Stack stabilizers

A local weighted blowup with functions `x_i` of positive weights `w_i` has stack presentation

\[
\left[
\left(
\operatorname{Spec}
A[\tau,u_1,\ldots,u_r]/(x_i-\tau^{w_i}u_i)
\setminus V(u_1,\ldots,u_r)
\right)
/\mathbb G_m
\right],
\]

with

\[
\lambda\cdot\tau=\lambda^{-1}\tau,
\qquad
\lambda\cdot u_i=\lambda^{w_i}u_i.
\]

At a geometric exceptional point whose nonzero coordinates have indices `J`, the stabilizer is

\[
\mu_{\gcd\{w_j:j\in J\}}.
\]

Thus roots of unity are retained as inertia. If one later introduces ordered subclusters, permutations of equal subclusters should likewise be recorded as finite stack structure rather than silently divided out.

The residual coefficient-scaling `G_m` acts on `\mathfrak G_N` with its original absolute coefficient weights. The framed quotient is

\[
[\mathfrak G_N/\mathbb G_m].
\]

It is Deligne-Mumford only on loci where the residual stabilizer is finite. Without such a restriction the natural all-boundary quotient is Artin.

## 2.3 One-root regression

At a one-root wall, write

\[
y=\epsilon^Ns,
\]

where `epsilon` is the escaping-root parameter and `s` is the weight-two gauge. The weighted point is

\[
[\epsilon:s]\in\mathbb P(1,2).
\]

On the chart `epsilon != 0`, its coarse invariant is

\[
\frac{s}{\epsilon^2}
=
\frac{y}{\epsilon^{N+2}}.
\]

The coarse graph closure is therefore

\[
\operatorname{Bl}_{(\epsilon^{N+2},y)}
\operatorname{Spec}B[\epsilon,y],
\]

which is exactly the Program 4 one-root model. The stacky version additionally retains the `\mu_2` stabilizer on the pure weight-two point.

---
