# Weight-separated polynomial-shear composition theorem

Let

```text
S = k[P,Q,R] subset B = k[x,y,z]
```

for the displayed Keller map, over a characteristic-zero field. Give `B` the
source-torus grading

```text
wt(x)=-1,  wt(y)=1,  wt(z)=2.
```

Then `S` is graded, with `wt(P)=2`, `wt(Q)=1`, and `wt(R)=-1`, while
`B_{<=6}` is supported on the weight interval `[-6,12]`, of width 18.

This note extends the single-monomial theorem to an infinite class of genuine
compositions.

## Exact separation condition

Fix distinct coordinates `x_i,x_j`. Let

```text
f(x_j) = sum_{nu=1}^r c_nu*x_j^(N_nu),
```

where every displayed coefficient is nonzero and every `N_nu>=2`. Put

```text
D_nu = x_j^(N_nu) partial_{x_i},
e_nu = N_nu*wt(x_j)-wt(x_i).
```

The derivations commute and

```text
sigma_f = exp(sum c_nu D_nu)
```

is the polynomial shear `x_i -> x_i+f(x_j)`.

Call the weight list **six-step 18-separated** if

```text
abs(sum_nu (alpha_nu-beta_nu)*e_nu) > 18
```

for every two distinct multiindices `alpha,beta in N^r` satisfying

```text
sum alpha_nu <= 6,   sum beta_nu <= 6.
```

## Theorem

If the weight list is six-step 18-separated, then

```text
sigma_f(S) intersect B_{<=6} = k.
```

Thus no such finite composition of commuting elementary monomial shears can
expose even one nonconstant element of the image algebra in source degree at
most six.

## Proof

Take

```text
g in sigma_f(S) intersect B_{<=6}
```

and decompose it into torus weights:

```text
g = sum_w g_w,       -6 <= w <= 12.
```

Since every `D_nu` lowers the exponent of the same coordinate `x_i`, any
iterated derivative of total order greater than six annihilates `g`. Hence

```text
sigma_f^(-1)(g)
 = sum_w sum_{|alpha|<=6}
   (-1)^|alpha| c^alpha/alpha! D^alpha(g_w).
```

The term indexed by `(w,alpha)` has weight

```text
w + sum alpha_nu e_nu.
```

The separation condition says that distinct pairs `(w,alpha)` have distinct
weights: a collision would make the difference of the two shift sums have
absolute value at most `12-(-6)=18`.

Now `sigma_f^(-1)(g)` belongs to the graded algebra `S`. Therefore each term
in the displayed expansion belongs to `S` separately. Taking `alpha=0` gives

```text
g_w in S
```

for every `w`, and hence

```text
g in S intersect B_{<=6} = span{1,Q,R}.
```

Write `g=a+bQ+dR`. For each `nu`, the first-order terms

```text
b D_nu(Q),       d D_nu(R)
```

also occupy distinct weights and therefore belong to `S` whenever the
corresponding coefficient is nonzero.

The exact common fiber

```text
u = (-12,  1/11,  -8/11)
v = (-10,  1/11, -14/11)
w = ( 22, -1/22, 65/484)
```

satisfies

```text
F(u)=F(v)=F(w)=(0,1/11,-1320).
```

Direct differentiation gives

```text
             Q_x          Q_y          Q_z       R_x       R_y    R_z
u       -684/1331      7753/121      -36/121    3550/11    -432   1728
v        750/1331     -8219/121      -30/121    4282/11    -300   1000
w        -3/242              4             0       -187   -1452 -10648
```

Multiplying the relevant derivative column by `x_j^(N_nu)` shows, in each of
the six coordinate directions and for every `N_nu>=2`, that neither
`D_nu(Q)` nor `D_nu(R)` is constant on this fiber. Therefore neither belongs
to `S`. It follows that `b=d=0`, so `g` is constant. This proves the theorem.

## Easily checked superlacunary condition

Order the nonzero shifts so that

```text
abs(e_1) < abs(e_2) < ... < abs(e_r).
```

The exact separation condition follows from the simpler recursive bounds

```text
abs(e_1) > 18,
abs(e_s) > 18 + 6*sum_{t<s} abs(e_t)     for s>=2.
```

Indeed, for distinct `alpha,beta`, let `s` be the largest index where they
differ. Then

```text
abs(sum (alpha-beta)e)
 >= abs(e_s) - 6*sum_{t<s} abs(e_t)
 > 18.
```

Consequently every same-direction polynomial shear whose monomial weights
are superlacunary in this sense satisfies

```text
sigma_f(S) intersect B_{<=6}=k.
```

For a one-term polynomial this recovers the structural tails of the complete
single-shear theorem. For several terms it gives a genuine composition result,
with arbitrary nonzero coefficients and no bound on the number of terms.

## Scope

The derivations here commute because every term changes the same coordinate
by a polynomial in the same other coordinate. The proof does not cover
noncommuting elementary shears, closely spaced weight shifts, or wild source
automorphisms. Those are the remaining composition frontiers.
