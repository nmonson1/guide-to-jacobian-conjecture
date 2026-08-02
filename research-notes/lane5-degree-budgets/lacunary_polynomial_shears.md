# High-weight polynomial-shear composition theorem

Let

```text
S = k[P,Q,R] subset B = k[x,y,z]
```

for the displayed Keller map, over a characteristic-zero field. Give `B` the
source-torus grading

```text
wt(x)=-1,  wt(y)=1,  wt(z)=2.
```

Then `S` is graded, with

```text
wt(P)=2,  wt(Q)=1,  wt(R)=-1,
```

while `B_{<=6}` is supported on `[-6,12]`, a weight interval of width 18.

This note proves a composition theorem for arbitrary finite polynomial shears
supported outside that weight window. No lacunarity or separation among the
individual monomials is required.

## Theorem

Fix distinct coordinates `x_i,x_j`. Let

```text
f(x_j) = a_0+a_1*x_j + sum_{N in E} c_N*x_j^N,
```

where `E` is finite, every `N>=2`, and every displayed `c_N` is nonzero. Put

```text
D_N = x_j^N partial_{x_i},
e_N = N*wt(x_j)-wt(x_i).
```

Assume the nonlinear shifts are all on one side of the degree-six window:

```text
e_N >= 19 for every N in E,
```

or

```text
e_N <= -19 for every N in E.
```

If `E` is nonempty and `sigma_f` is the source shear

```text
x_i -> x_i+f(x_j),
```

then

```text
sigma_f(S) intersect B_{<=6} = k.
```

Thus an arbitrary number of same-direction high-weight elementary shears,
with arbitrary coefficients and arbitrarily close exponents, cannot expose a
nonconstant image-algebra element of source degree at most six.

## Proof

The affine part `a_0+a_1*x_j` commutes with the nonlinear shear and preserves
`B_{<=6}`. It can therefore be removed. Write

```text
D_f = sum_{N in E} c_N D_N,
sigma_f = exp(D_f).
```

Take

```text
g in sigma_f(S) intersect B_{<=6}
```

and decompose `g=sum_w g_w` into torus weights, where `-6<=w<=12`.
Since each `D_N` lowers the exponent of the same coordinate `x_i`, the
expansion of `sigma_f^(-1)(g)` stops after total derivative order six.

### Positive shifts

Suppose every `e_N>=19`. Every term involving at least one derivative has
weight at least

```text
-6+19=13,
```

whereas every zero-order term `g_w` has weight at most 12. Since
`sigma_f^(-1)(g)` lies in the graded algebra `S`, each `g_w` lies in `S`.
The standard filtration theorem gives

```text
g in S intersect B_{<=6} = span{1,Q,R}.
```

Write `g=a+bQ+dR`, and let `e_0` be the smallest shift occurring in `f`.
If `d!=0`, the unique lowest-weight nonzero derivative term in
`sigma_f^(-1)(g)` is

```text
-d*c_0*D_0(R),       of weight -1+e_0.
```

Every other first-order term has larger weight, and every higher-order term
has weight at least `-1+2e_0`. Hence `D_0(R)` would belong to `S`.

If `d=0` but `b!=0`, the unique lowest derivative term is

```text
-b*c_0*D_0(Q),       of weight 1+e_0,
```

so `D_0(Q)` would belong to `S`.

### Negative shifts

Suppose every `e_N<=-19`, and let `e_0` be the largest shift, meaning the one
closest to zero. Derivative terms have weight at most

```text
12-19=-7,
```

so they cannot collide with zero-order weights, which are at least -6. Again
`g` belongs to `span{1,Q,R}`.

If `b!=0`, the unique highest-weight derivative term is

```text
-b*c_0*D_0(Q),       of weight 1+e_0.
```

After `b=0`, a nonzero `d` would make

```text
-d*c_0*D_0(R),       of weight -1+e_0,
```

the unique highest derivative term. Thus a nonconstant `g` again forces one
of `D_0(Q),D_0(R)` to lie in `S`.

### Exact common-fiber obstruction

The three rational source points

```text
u = (-12,  1/11,  -8/11)
v = (-10,  1/11, -14/11)
w = ( 22, -1/22, 65/484)
```

have the common image

```text
F(u)=F(v)=F(w)=(0,1/11,-1320).
```

Their derivative values are

```text
             Q_x          Q_y          Q_z       R_x       R_y    R_z
u       -684/1331      7753/121      -36/121    3550/11    -432   1728
v        750/1331     -8219/121      -30/121    4282/11    -300   1000
w        -3/242              4             0       -187   -1452 -10648
```

For each of the six coordinate directions and every `N>=2`, multiplying the
relevant derivative column by `x_j^N` gives unequal values on this common
fiber. Therefore

```text
D_N(Q) notin S,       D_N(R) notin S.
```

The contradictions above force `b=d=0`. Hence `g` is constant.

## Concrete thresholds

The theorem applies to every polynomial whose nonlinear support is contained
in the indicated tail:

```text
z -> z+f(x):   every nonlinear exponent N>=17
y -> y+f(x):   every nonlinear exponent N>=18
x -> x+f(y):   every nonlinear exponent N>=18
z -> z+f(y):   every nonlinear exponent N>=21
y -> y+f(z):   every nonlinear exponent N>=10
x -> x+f(z):   every nonlinear exponent N>=9.
```

The coefficients and the number of terms are unrestricted.

## Resonant-plus-tail corollary

The weight-zero shear

```text
z -> z+a*y^2
```

preserves the torus grading and commutes with every shear `z->z+c_N*y^N`.
The exact resonant certificate gives its degree-six intersection as
`span{1,sigma_a(R)}`. Repeating the proof above with this graded intermediate
algebra shows:

```text
z -> z+a_0+a_1*y+a_2*y^2 + sum_{N>=21} c_N*y^N
```

has degree-six intersection `k` whenever the high tail is nonzero. If the
high tail vanishes, the exact resonant theorem applies.

## Relation to the single-shear theorem

For a one-term polynomial, the theorem recovers the infinite structural tails
of `all_elementary_monomial_shears.py`. The finite exact certificates fill the
remaining exponents. Together they prove every single monomial shear; the
present theorem additionally closes arbitrary finite compositions inside each
high-weight same-direction tail.

## Remaining scope

Closely spaced low-weight polynomial terms and noncommuting shear directions
can produce weight collisions inside the interval `[-6,12]`. They are not
covered here. These are now the first genuine composition cases.
