# One-sided high-weight noncommuting composition theorem

Let

```text
S=k[P,Q,R] subset B=k[x,y,z]
```

for the displayed Keller map, with source-torus weights

```text
wt(x)=-1,  wt(y)=1,  wt(z)=2.
```

Then `S` is graded, `P,Q,R` have weights `2,1,-1`, and `B_{<=6}` is supported
on the interval `[-6,12]`.

## Main theorem

Let

```text
Phi = exp(c_m D_m) ... exp(c_1 D_1)
```

be any finite ordered composition, where every `c_i` is nonzero and every
`D_i` is a homogeneous locally nilpotent derivation of torus weight `e_i`.
The derivations need not commute and may change different coordinates.

Assume either

```text
e_i >= 19 for every i
```

or

```text
e_i <= -19 for every i.
```

Then

```text
Phi(S) intersect B_{<=6}
  subset S intersect B_{<=6}
  = span_k{1,Q,R}.
```

Consequently

```text
trdeg k[Phi(S) intersect B_{<=6}] <= 2.
```

Thus no one-sided high-weight composition can produce a degree-at-most-six
target coordinate frame. This is a genuine noncommuting composition theorem,
not a finite scan.

## Proof

Take

```text
g in Phi(S) intersect B_{<=6}
```

and decompose it into torus weights:

```text
g = sum_{w=-6}^{12} g_w.
```

Expand `Phi^(-1)(g)`. Its zero-order terms are precisely the `g_w`. Every
other term is obtained by applying a nonempty word in the `D_i`; its weight is
the input weight plus the sum of the weights of that word.

If all `e_i>=19`, every nonzero word has weight at least

```text
-6+19=13.
```

If all `e_i<=-19`, every nonzero word has weight at most

```text
12-19=-7.
```

In either case, no derivative word has a weight in `[-6,12]`. Since
`Phi^(-1)(g)` belongs to the graded algebra `S`, its weight components in that
interval—exactly the `g_w`—belong to `S`. Hence

```text
g in S intersect B_{<=6}.
```

The standard exact certificate identifies the latter space with
`span{1,Q,R}`, proving the theorem.

Notice what is not used: commutativity, a factorization normal form, uniqueness
of an extremal shift, or any bound on the number of factors.

## Elementary-monomial corollary

For

```text
D=x_j^N partial_{x_i},
```

one has

```text
e=N*wt(x_j)-wt(x_i).
```

Therefore any finite ordered composition of elementary monomial shears is
covered when all factors are chosen from one of the following two one-sided
sets.

### Negative side

```text
z -> z+c*x^N,   N>=17
y -> y+c*x^N,   N>=18
```

### Positive side

```text
x -> x+c*y^N,   N>=18
z -> z+c*y^N,   N>=21
y -> y+c*z^N,   N>=10
x -> x+c*z^N,   N>=9
```

Factors from the same side may be mixed in any order, may repeat weights, and
need not commute. Coefficients are arbitrary.

## Exact-intersection refinement

The main theorem gives the Lane 5 obstruction without deciding which of
`Q,R` survive. A sharper conclusion is available when the extremal
first-order layer is nondegenerate.

In the positive case let `e_0=min e_i`; in the negative case let
`e_0=max e_i`. Put

```text
D_* = sum_{e_i=e_0} c_i D_i.
```

If

```text
D_*(Q) notin S,       D_*(R) notin S,
```

then

```text
Phi(S) intersect B_{<=6}=k.
```

Indeed, after the main theorem write `g=a+bQ+dR`. On the positive side a
nonzero `d` isolates `D_*(R)` at the lowest derivative weight; after `d=0`, a
nonzero `b` isolates `D_*(Q)`. On the negative side the same argument uses the
highest derivative weight in the reverse order.

For a unique extremal elementary monomial derivation, the exact three-point
common fiber proves both nonmembership conditions, so the intersection is
`k`. Repeated extremal weights reduce to a finite linear-independence problem
in the quotient by fiber-constant polynomials.

## Scope

The theorem permits arbitrary noncommuting compositions but requires all
nonlinear weight shifts to lie strictly on the same side of the degree-six
window. Mixed positive/negative sequences and factors with weights in
`[-18,18]` remain the first uncontrolled composition regimes.
