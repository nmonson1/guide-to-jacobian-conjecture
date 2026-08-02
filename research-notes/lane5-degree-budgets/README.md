# Lane 5 degree-six filtration and elementary-shear theorems

This directory studies the displayed three-variable Keller map

```text
A0 = 1 + x*y
P  = A0^3*z + y^2*A0*(4+3*x*y)
Q  = y + 3*x*A0^2*z + 3*x*y^2*(4+3*x*y)
R  = 2*x - 3*x^2*y - x^3*z
```

and the embedded algebra `S=k[P,Q,R]` inside `B=k[x,y,z]`, over a
characteristic-zero field.

The results below concern degree at most six. They do not yet cover arbitrary
mixed-sign compositions or wild source automorphisms.

## Theorem A: standard and affine source coordinates

In the displayed coordinates,

```text
S intersect B_{<=6} = span_k{1,Q,R}.
```

Consequently

```text
k[S intersect B_{<=6}] = k[Q,R],
```

which has transcendence degree two.

Every affine source automorphism preserves `B_{<=6}`. Therefore, for every
affine automorphism `L`,

```text
L(S) intersect B_{<=6} = span_k{1,L(Q),L(R)}.
```

The standard certificate uses all 84 source monomials of degree at most six
and 81 exact rational common-fiber difference rows. The selected `81 x 81`
minor is nonzero modulo `1000003`, with determinant `214012`. The exact kernel
vectors are `1`, `Q`, and `R`.

Replay:

```bash
python3 standard_filtration_certificate.py
```

## Theorem B: every single elementary monomial source shear

Let `i` and `j` be distinct source coordinates, let `N>=2`, and let `c` be any
scalar. Define

```text
sigma(x_i) = x_i + c*x_j^N
```

and fix the third coordinate. Then

```text
sigma(S) intersect B_{<=6}
```

is exactly:

```text
span{1,Q,R}              if c=0;

span{1,sigma(R)}         if c!=0 and deg sigma(R)<=6;

k                         if c!=0 and deg sigma(R)>6.
```

In particular, for every such shear,

```text
trdeg k[sigma(S) intersect B_{<=6}] <= 2,
```

and for every nontrivial shear the transcendence degree is at most one.
Therefore no single elementary monomial source shear can expose three
algebraically independent target functions of degree at most six.

The nonconstant cases are precisely

| Shear | Exponents retaining `sigma(R)` |
| --- | --- |
| `z -> z+c*x^N` | `N=2,3` |
| `y -> y+c*x^N` | `N=2,3,4` |
| `z -> z+c*y^N` | `N=2,3` |
| `y -> y+c*z^N` | `N=2,3,4` |

The two shears changing `x` always have intersection `k` when `c!=0`.

Replay the complete theorem with

```bash
python3 all_elementary_monomial_shears.py
```

The verifier checks 81 finite exponent/direction cases, the exact resonant
coefficient family, and the structural infinite tails.

## Proof architecture for Theorem B

### 1. Finite exact range

For coefficient one, exact rational common-fiber matrices certify all
exponents below the weight-separation thresholds:

```text
z+x^N:  2 <= N <= 16
y+x^N:  2 <= N <= 17
x+y^N:  2 <= N <= 17
z+y^N:  2 <= N <= 20
y+z^N:  2 <= N <= 9
x+z^N:  2 <= N <= 8
```

There are 81 cases. Ten have rank 82 and the displayed kernel
`span{1,sigma(R)}`; the other 71 have rank 83 and only constants in the
kernel. Every modular minor is backed by exact rational rows.

### 2. Torus-weight separation for every larger exponent

The source torus has weights

```text
wt(x)=-1,  wt(y)=1,  wt(z)=2,
```

while `P,Q,R` have weights `2,1,-1`. The space `B_{<=6}` has weights in
`[-6,12]`, of width 18.

Write a shear as `exp(cD)`, where `D=x_j^N partial_{x_i}` is a homogeneous
locally nilpotent derivation of weight `e`. If `|e|>18` and

```text
g in exp(cD)(S) intersect B_{<=6},
```

then `exp(-cD)g` belongs to the graded algebra `S`. Distinct terms
`D^m(g_w)` have distinct torus weights because the input weights differ by at
most 18 while each nonzero step changes weight by more than 18. Hence every
weight component `g_w` already lies in `S`. Theorem A gives

```text
g in span{1,Q,R}.
```

If the `Q` or `R` coefficient were nonzero, the same separated-weight
argument would force `D(Q)` or `D(R)` to lie in `S`.

The three points

```text
u = (-12,  1/11,  -8/11)
v = (-10,  1/11, -14/11)
w = ( 22, -1/22, 65/484)
```

all map to

```text
(P,Q,R) = (0,1/11,-1320).
```

Their exact derivative values show, for each of the six shear directions and
every exponent, that neither `D(Q)` nor `D(R)` is constant on this fiber.
Thus neither lies in `S`. Only constants survive.

The resulting sharp structural thresholds are

```text
z+x^N: N>=17      y+x^N: N>=18      x+y^N: N>=18
z+y^N: N>=21      y+z^N: N>=10      x+z^N: N>=9.
```

Together with the finite certificates, these cover every `N>=2`.

### 3. All nonzero coefficients

Conjugation by the source torus rescales the coefficient of every elementary
monomial shear except

```text
z -> z+c*y^2.
```

Thus, after extension to an algebraic closure, every nonzero coefficient in
the nonresonant cases is conjugate to coefficient one. The intersection
statement then descends to the original characteristic-zero field.

### 4. Exact resonant family

The shear `z -> z+c*y^2` preserves the source torus grading. Split
`B_{<=6}` into its 19 weight spaces. Each has dimension at most eight.

The file `resonant_weight_certificate.json` supplies 33 exact rational
determinantal minors. Their gcds in `Q[c]` are:

```text
1  in every weight except weight 1;
c  in weight 1.
```

The weight-zero kernel is always generated by `1`; the weight-minus-one
kernel is generated by

```text
sigma_c(R) = R - c*x^3*y^2.
```

At `c=0`, weight one additionally contains `Q`, as in Theorem A. At every
`c!=0`, its rank is full. Hence

```text
sigma_c(S) intersect B_{<=6}
  = span{1,sigma_c(R)}
```

for every nonzero `c`, with no exceptional coefficients.

Replay this component alone with

```bash
python3 resonant_weight_certificate.py
```

## Theorem C: arbitrary one-sided high-weight source words

Let `U_+` be the semigroup generated by exponentials of homogeneous locally
nilpotent source derivations of torus weight at least `19`, and let `U_-` be
the corresponding semigroup of weights at most `-19`. Then, for every

```text
sigma in U_+ union U_-,
```

one has

```text
sigma(S) intersect B_{<=6}
  subset span{1,Q,R}.
```

Thus the generated algebra has transcendence degree at most two. Word length,
coefficients, order, and coordinate direction are unrestricted, and the
factors need not commute.

The proof is a general weight-window lemma. If a graded subalgebra `A` is
acted on by a word of homogeneous locally nilpotent derivations whose weights
all exceed the width of a finite weight window on the same side, then every
nonzero derivative word leaves that window. For
`g in sigma(A) intersect V`, the in-window components of `sigma^(-1)(g)` are
therefore exactly the components of `g`; gradedness forces them into `A`.

The theorem covers arbitrary noncommuting words in the positive generators

```text
x -> x+c*y^N,   N>=18;
z -> z+c*y^N,   N>=21;
y -> y+c*z^N,   N>=10;
x -> x+c*z^N,   N>=9,
```

or arbitrary words in the negative generators

```text
z -> z+c*x^N,   N>=17;
y -> y+c*x^N,   N>=18.
```

It also permits arbitrary interleaving with the resonant weight-zero shears
`z -> z+a*y^2`. After normal-ordering those factors to the right, the exact
resonant theorem gives transcendence degree at most two when the total
resonant parameter is zero and at most one otherwise. An arbitrary affine
source post-factor preserves all conclusions.

Complete proof:

```text
one_sided_high_weight_semigroup.md
```

This strictly extends the same-direction polynomial-tail theorem in
`lacunary_polynomial_shears.md`: noncommuting coordinate directions are now
allowed.

## Certificate and proof files

```text
standard_filtration_certificate.py
standard_filtration_certificate.json

elementary_shear_scan.py
elementary_shear_scan.json

resonant_weight_certificate.py
resonant_weight_certificate.json

all_elementary_monomial_shears.py
all_elementary_monomial_shears.json

lacunary_polynomial_shears.md
one_sided_high_weight_semigroup.md
```

The first pair proves Theorem A. The older bounded shear pair remains a compact
42-case checkpoint. The resonant pair proves the complete one-parameter
weight-preserving family. The all-elementary pair combines the expanded
81-case finite certificate with the weight-separation proof. The final two
notes prove same-direction and arbitrary-direction high-weight composition
theorems.

## Filtered differential obstruction

For an embedded inclusion `iota:A=k[u1,u2,u3] -> B`, a source automorphism
`sigma`, and a degree bound `D`, set

```text
F_D^sigma A = {a in A : deg sigma(iota(a)) <= D}.
```

For a basis `f1,...,fm`, define `J_D^sigma` as the ideal of the `3 x 3`
minors of

```text
(partial fi / partial uj).
```

This ideal is basis independent. In characteristic zero:

1. `J_D^sigma=0` exactly when the generated algebra has transcendence degree
   at most two.
2. If `F_D^sigma A` contains a polynomial coordinate frame, then
   `J_D^sigma=A`.
3. Therefore properness of `J_D^sigma` obstructs a degree-`D` target frame.

The elementary-shear theorem proves the stronger condition `J_6^sigma=0` for
every single elementary monomial source shear. Theorem C proves the same
condition for every one-sided high-weight source word.

## Structural limits

No exhaustive filtration of `k[x1,x2,x3]` by finite-dimensional vector spaces
can be literally invariant under every polynomial automorphism. If one finite
piece contains `x1`, invariance under

```text
x1 -> x1+x2^N
```

would put all powers `x2^N` in that same piece.

Likewise, every degree budget obtained from a finite family of normalized
divisorial valuations is diluted to zero by triangular source shears. A
successful full-orbit theory must use a genuinely global boundary object, an
infinite valuation system, or a non-degree-increasing canonicalization.

The remaining Lane 5 gap is confined more sharply: it consists of nonlinear
words containing low-weight factors, mixed positive/negative high-weight
factors whose derivative weights can return to the degree-six window, and the
possible wild part of `Aut(k[x,y,z])`.
