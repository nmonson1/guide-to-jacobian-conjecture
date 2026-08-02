# Coefficient transport for elementary Lane 5 shears

Let `S=k[P,Q,R]` be the displayed image subalgebra in `B=k[x,y,z]`, over a
characteristic-zero field. The source torus

```text
T_lambda(x,y,z) = (lambda^(-1)*x, lambda*y, lambda^2*z)
```

acts equivariantly on the displayed map:

```text
T_lambda(P,Q,R) = (lambda^2*P, lambda*Q, lambda^(-1)*R).
```

Consequently `T_lambda(S)=S`, and `T_lambda` preserves every ordinary-degree
piece of `B`.

For a monomial elementary shear `E_(i,m,c)` sending the coordinate `X_i` to
`X_i+c*m`, write `w(x)=-1`, `w(y)=1`, and `w(z)=2`. Direct conjugation gives

```text
T_lambda^(-1) E_(i,m,c) T_lambda
  = E_(i,m,c*lambda^(w(X_i)-w(m))).
```

If `w(X_i)-w(m)` is nonzero, then over an algebraic closure every nonzero
coefficient `c` is conjugate to coefficient one. Since both the subalgebra and
the degree filtration are transported by `T_lambda`, the coefficient-one
fiber certificate proves the same exact degree-six intersection for every
`c!=0`. The conclusion descends to the original characteristic-zero field.

For the six scanned shear directions the weight differences are

| Shear | Weight difference |
| --- | ---: |
| `z -> z+c*x^N` | `N+2` |
| `y -> y+c*x^N` | `N+1` |
| `x -> x+c*y^N` | `-N-1` |
| `z -> z+c*y^N` | `2-N` |
| `y -> y+c*z^N` | `1-2N` |
| `x -> x+c*z^N` | `-1-2N` |

Thus among exponents `2<=N<=8`, the only coefficient that cannot be normalized
by this torus is the resonant family

```text
z -> z+c*y^2.
```

The zero coefficient is the identity and is covered by the standard-source
theorem. Therefore the 42 coefficient-one certificates extend to **all
coefficients** except possibly nonzero coefficients in this one resonant
family.

## Generic resonant coefficient

For `E_c:z->z+c*y^2`, the transformed common-fiber evaluation matrix on
`B_{<=6}` has entries polynomial in `c`. Use the 82 rational rows and 82 pivot
columns selected by the coefficient-one certificate. Their determinant is a
polynomial

```text
Delta(c) in Q[c]
```

of degree at most 126, the sum of the `z`-exponents of the selected source
monomials. The modular certificate gives

```text
Delta(1) = 640259 mod 1000003,
```

so `Delta` is not the zero polynomial.

For every `c` with `Delta(c)!=0`, the evaluation-difference matrix has rank at
least 82. On the other hand, both `1` and

```text
E_c(R) = R-c*x^3*y^2
```

belong to the exact kernel and are linearly independent; hence the rank is at
most 82. Therefore

```text
E_c(S) intersect B_{<=6} = span{1,E_c(R)}
```

for all but at most 126 coefficients over an algebraic closure, counted with
multiplicity. In particular, the generated algebra has transcendence degree
one for Zariski-generic `c`.

At `c=0`, the standard theorem gives `span{1,Q,R}`. Determining the finite
nonzero exceptional set requires either an exact gcd/Bézout certificate for
several maximal minors or a structural argument; a zero of this chosen minor
need not be a rank-drop coefficient.

## Affine source closure

The standard theorem also transports under every affine source automorphism
`L`, because `L(B_{<=6})=B_{<=6}`. Thus

```text
L(S) intersect B_{<=6} = span{1,L(Q),L(R)}.
```

This covers the entire affine source group exactly. It remains far short of a
classification of arbitrary compositions of nonlinear elementary shears or
wild source automorphisms.
