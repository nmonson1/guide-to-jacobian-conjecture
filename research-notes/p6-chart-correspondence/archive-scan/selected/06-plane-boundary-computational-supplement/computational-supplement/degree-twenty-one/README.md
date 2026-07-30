# Exact computational ledger for the open (8,28) case

## Truncated support
- P lattice points: 25
- Q lattice points: 47
- Raw variables: 72
- Nonzero coefficient equations in `[P,Q]-x^2`: 92

| r | domain | output | rank | kernel | cokernel |
|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 5 | 4 | 3 | 1 |
| 2 | 7 | 5 | 4 | 3 | 1 |
| 3 | 7 | 5 | 4 | 3 | 1 |
| 4 | 7 | 5 | 3 | 4 | 2 |
| 5 | 7 | 5 | 4 | 3 | 1 |
| 6 | 7 | 5 | 4 | 3 | 1 |
| 7 | 7 | 5 | 4 | 3 | 1 |
| 8 | 5 | 5 | 3 | 2 | 2 |
| 9 | 4 | 5 | 4 | 0 | 1 |
| 10 | 4 | 5 | 4 | 0 | 1 |
| 11 | 2 | 3 | 2 | 0 | 1 |
| 12 | 1 | 0 | 0 | 1 | 0 |

First nonlinear left-cokernel pairings: `['14*(A0 + A1 + A2)**2/3']`

### Truncated regular fan
| ray | self-int | support max P | support max Q | Kbar label |
|---|---:|---:|---:|---:|
| `(0, -1)` | -2 | 0 | 0 | -1 |
| `(1, -2)` | -1 | 1 | 0 | 1 |
| `(1, -1)` | -3 | 1 | 1 | 2 |
| `(2, -1)` | -1 | 2 | 3 | 5 |
| `(1, 0)` | 0 | 8 | 12 | 3 |
| `(-2, 1)` | 0 | 0 | 0 | -5 |
| `(-1, 0)` | -2 | 0 | 0 | -3 |

## Full support
- P lattice points: 61
- Q lattice points: 125
- Raw variables: 186
- Nonzero coefficient equations in `[P,Q]-x^2`: 302

| r | domain | output | rank | kernel | cokernel |
|---:|---:|---:|---:|---:|---:|
| 1 | 9 | 7 | 5 | 4 | 2 |
| 2 | 11 | 8 | 6 | 5 | 2 |
| 3 | 13 | 9 | 7 | 6 | 2 |
| 4 | 15 | 10 | 7 | 8 | 3 |
| 5 | 17 | 11 | 9 | 8 | 2 |
| 6 | 19 | 12 | 10 | 9 | 2 |
| 7 | 21 | 13 | 11 | 10 | 2 |
| 8 | 21 | 14 | 11 | 10 | 3 |
| 9 | 13 | 15 | 13 | 0 | 2 |
| 10 | 14 | 16 | 14 | 0 | 2 |
| 11 | 13 | 15 | 13 | 0 | 2 |
| 12 | 13 | 14 | 12 | 1 | 2 |

First nonlinear left-cokernel pairings: `['22*(A0 + A1 + A2 + A3)**2/3', '-8*(A0 + A1 + A2 + A3)**2/3']`

### Full regular fan
| ray | self-int | support max P | support max Q | Kbar label |
|---|---:|---:|---:|---:|
| `(0, -1)` | -2 | 0 | 0 | -1 |
| `(1, -2)` | -1 | 1 | 0 | 1 |
| `(1, -1)` | -3 | 1 | 1 | 2 |
| `(2, -1)` | -1 | 2 | 3 | 5 |
| `(1, 0)` | -1 | 8 | 12 | 3 |
| `(-1, 1)` | 0 | 8 | 12 | -2 |
| `(-1, 0)` | -1 | 0 | 0 | -3 |

## Exact deeper reduction

- ODE quartic: `2048*y**4 - 512*y**3 + 320*y**2 - 240*y + 195`
- Separant discriminant: `12837954459480883200`
- Compatibility: `-a**5 + 6*a**2*c*e - 6*a*b**2*e - 6*a*b*c**2 + 6*b**3*c=0`
- Forced coefficient: `d2=-(-2*G + 6*a*b**2 + 3*a*u)/a**3`
- Eliminant: `-72*G*u**4 + 24*L*a**5*u**2 + a**13 - 24*a**7*b*u**2 + 144*a*b**2*u**4 + 36*a*u**5=0`


## Boundary-graph correction and Three-dessin test

For a toric ray `v`, the divisor valuation is the **minimum** of `<m,v>` on the support; the support maximum is not the valuation.  On the common regular refinement, both Newton cases have the same negative-label chain

`-1 -- -3 -- -5 -- -2`

with source self-intersections `-2,-2,-1,-1` and valuation pairs

| label | source ray | `(v(P),v(Q))` | behavior |
|---:|---|---|---|
| -1 | `(0,-1)` | `(-16,-24)=8(-2,-3)` | point on target `-5` |
| -3 | `(-1,0)` | `(-8,-12)=4(-2,-3)` | point on target `-5` |
| -5 | `(-2,1)` | `(-2,-3)` | degree-21 map onto target `-5` |
| -2 | `(-1,1)` | `(-1,-1)` | degree-1 map onto target `-2` |

On the `-5` divisor put `z=XY^2`.  The face polynomials are

`P_face=X p(z)`, `Q_face=X^2 Y q(z)`, with `deg p=7`, `deg q=10`.
The coefficient of the lowest toric weight in `[P,Q]=X^2` is

`p q + 2 z p q' - 3 z p' q = 1`.

Consequently

`tau=Q^2/P^3|_{E_-5}=z q^2/p^3`,  `tau'=q/p^4`,

so `tau` is a degree-21 Belyi map with passport

`(2^10 1), (3^7), (17 1^4)`.

Borisov's Three-dessin framework requires degree 16 on its core `-5` component.  Therefore neither open `(8,28)` Newton polygon can realize Three-dessin.  The same calculation gives the new conditional bound `mu >= 21` for the generic degree of a counterexample in this Newton case.

## Exact dessin count for the forced degree-21 face map

The Frobenius character formula for the three conjugacy classes

`2^10 1`, `3^7`, `17 1^4`

gives an ordered-triple count equal to `5 * 21!`.  Every such triple is transitive: an orbit outside the 17-cycle would consist of points fixed by the third permutation; on such an orbit the order-2 and order-3 permutations would be mutual inverses and hence both trivial, impossible because the order-3 permutation has no fixed points.  The deck group is trivial because the unique ramification-17 point and the unique unramified point over the zero-fiber are fixed, while any remaining scaling order would have to divide both 7 and 10.  Therefore there are exactly **five** connected dessins, and hence five lower-face Belyi maps up to the residual source scaling.
