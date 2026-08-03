# Lane 8: Plane Newton queue and terminal certificates

## Problem and scope

The normalized Newton reduction for a hypothetical plane Keller
counterexample repeatedly chooses a Newton face, passes to its primitive
exponent lattice, normalizes its face equation, introduces deficiency layers,
and branches when coefficients or pivots vanish. Lane 8 asks for a finite
directed acyclic graph proving that this routing is exhaustive and reaches
exact terminal theorems.

A plane Keller map is a polynomial map `(P,Q):A^2->A^2` with nonzero
constant Jacobian determinant; a counterexample would be noninvertible.

For maximum coordinate degree below `125`, the routing is now complete: the
published reduction leaves two normalized `(8,28)` support roots, and an
exact direct calculation makes both roots empty. The next queue node is the
first degree-`125` complete-chain family, historically called `F_2`.

## Setup and notation

A queue node records `(support, valuation, chart, equations, open locus)`. An
edge records one exhaustive operation: face selection, primitive-lattice
quotient, saturation plus its complementary chart, normalization, deficiency
layer, coefficient branch, or rechart. A terminal node links to a theorem or
certificate for exactly its stored system.

For the solved below-`125` case, the two normalized support families have
Newton polygons

```text
truncated P: (0,0),(1,0),(8,14),(8,16)
truncated Q: (0,0),(2,1),(12,21),(12,24)
full P:      the truncated P vertices plus (0,8)
full Q:      the truncated Q vertices plus (0,12).
```

Each support consists of every lattice point in the displayed polygon. Its
deficiency is `j-2i+2` for `P` and `j-2i+3` for `Q`. The exact public
[raw-support reconstruction input](lane-8-reconstruction-input.md) contains
the field relations and complete program that turns these supports into the
lower-face and deficiency-layer equations.

The common degree-21 face has

```text
tau(z)=z*q(z)^2/p(z)^3,
passport (2^10 1),(3^7),(17 1^4).
```

The *three-dessin framework* is the comparison of the three Belyi maps
obtained from the primitive logarithmic-derivative face equations for the
coordinate pair and Jacobian relation. The degree-21 divisor data exclude
that simultaneous framework, not the two Newton supports themselves.

The first case not covered by the strict below-`125` result is

```text
F_2: A_0=(5,20), A'_0=(1,0), A_1=(7/5,2), (m,n)=(3,5).
```

The initial edge has primitive direction `(rho,sigma)=(5,-1)`. In
`z=x^(1/5)y` its leading forms are `x^3 p(z)` and `x^5 q(z)`, with
`p=R^3`, `q=R^5`, `deg R=20`; polynomial support forces
`R(z)=S(z^5)` with `deg S=4`. The selected root of `R` has multiplicity
two. At the terminal face the primitive direction is `(25,-17)` and

```text
5*p*q - 3*z*p*q' + 5*z*p'*q = 1.
```

The lattice gap is five. In `u=z^5`, the unique normalized quotient is

```text
pbar = 1-u,
qbar = 1/5-(3/5)u+(9/25)u^2,
phi_6(u) = u(u-1)^5/(u^2-(5/3)u+5/9)^3,
passport (5,1), (3^2), (3,1^3).
```

These data fix both endpoint faces. They do not yet fix the normalized
Newton polygons and two-point normal-layer windows between them.

## Reusable mathematics

A primitive face equation is an exact logarithmic derivative and gives a
Belyi map with passport determined by face exponents. Passing to the
primitive exponent lattice can lower the cover degree. The first five
quotient problems have degrees `6,10,9,9,16` and class counts `1,1,1,2,2`.
For the degree-21 face there are exactly five normalized maps in one quintic
Galois orbit, all with monodromy `A_21`. Units: [`JCG-34B30410`](../working-mathematics/units/JCG-34B30410.md),
[`JCG-2B32290C`](../working-mathematics/units/JCG-2B32290C.md), [`RMU-8E7E56B5`](../working-mathematics/units/RMU-8E7E56B5.md).

The direct two-root theorem is [`RMU-6D8E0013`](../working-mathematics/units/RMU-6D8E0013.md). Its conventional proof is
[`manuscripts/06-plane-boundary/appendices/degree-twenty-one-certificates.tex`](../proof-sources/06-plane-boundary/appendices/degree-twenty-one-certificates.md)
at `thm:degree21-two-support-closure`, and its self-contained exact packet is
[`research-notes/lane8-full-root-closure-20260803-v1/`](lane-8-source-packet.md). It proves:

- the vertex-saturated truncated support is empty in characteristic zero;
- the full support has two exhaustive paths after its layer-four square: the
  closed path loses required top vertices, while the open path normalizes to
  fifteen exact equations whose six-equation projection is the existing
  empty compact toric terminal; and
- neither path uses the separately stored layer-five-through-seven
  transformed system [`RMU-6D8E0012`](../working-mathematics/units/RMU-6D8E0012.md).

The truncated-only unit [`RMU-6D8E0010`](../working-mathematics/units/RMU-6D8E0010.md) remains a valid weaker result. The
stored adjacent terminal [`RMU-6D8E0012`](../working-mathematics/units/RMU-6D8E0012.md) also remains exact, but unattached:
the former bare-`k=4` bridge is false because that shear begins at layer
seven, not layer four. It is no longer a dependency of the below-`125`
proof.

Combining [`RMU-6D8E0013`](../working-mathematics/units/RMU-6D8E0013.md) with the published reduction gives
[`RMU-6D8E0014`](../working-mathematics/units/RMU-6D8E0014.md): no characteristic-zero plane Keller counterexample has
maximum coordinate degree strictly below `125`. The imported steps are
Guccione--Guccione--Horruitiner--Valqui, Theorem 2.1, Proposition 4.1,
Proposition 4.3 and Corollary 5.7. No novelty or priority claim is made for
this bound.

The older 7,121-row minor is not retained as a theorem because its source
does not establish that the target basis is complete. Branchwise and direct
support certificates are the preferred terminal interfaces.

### Incomplete proof strategy: terminal descent or complexity reduction

> **Status: idea for a proof, but not fully proved.** This is a research
> strategy, not a theorem and not a proof of the planar Jacobian conjecture.

Starting from a hypothetical minimal plane Keller counterexample, the
proposed route runs an exhaustive normalized Newton queue to a terminal
complete-chain system. The missing global theorem would show that every
terminal system either fails simultaneous finite polynomial support in
adjacent boundary charts or is induced by an admissible polynomial
approximate-root operation that strictly lowers Newton complexity.

Exact calculations rule out several direct affine-plane, polynomial-graph,
linear-target and low-parameter Hessian descents of displayed known
higher-dimensional examples. They do not exhaust all descents, prove the
global terminal dichotomy, or prove termination. See [`RMU-6D8E0011`](../working-mathematics/units/RMU-6D8E0011.md) and
[`research-notes/planar-descent-no-go-20260802-v1/README.md`](lane-8-source-packet.md).

## Exact live problem

Construct the first post-bound queue root for the degree-`125` family `F_2`.
Starting from the exact two endpoint faces above, propagate the complete
standard Newton rectangle through the distinguished double-root shear,
return to the quotient coordinate `u=z^5`, and determine every intervening
normalized support, open coefficient, and finite two-point normal-layer
window. Every discarded support point must follow from an explicit corner
inequality or the gap-five lattice congruence. This is a finite
support-normalization problem; it does not ask for the unavailable global
`F_2` attachment or for a new proof of the solved below-`125` result.

## Tasks and deliverables

### P6-L8A — Degree-125 `F_2` support propagation

Status: ready.

Inputs: all exact `F_2` corner, direction, common-power, double-root,
terminal ODE, quotient-map and passport data displayed above;
[`manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md`](lane-8-source-packet.md);
[`next_complete_chain_queue.json`](lane-8-source-packet.md) in the same directory; and its exact
checkers [`verify_F2_degree125_seed.py`](lane-8-source-packet.md), [`terminal_primary_belyi.py`](lane-8-source-packet.md) and
[`terminal_face_rigidity.py`](lane-8-source-packet.md). The degree-21 reconstruction packet
is an example of the required node format, not an input to the `F_2`
mathematics.

Deliverable: the complete list of normalized support polygons from the
initial `(5,20)` edge through the terminal `(7/5,2)` face, with the monomial
coordinate change at each edge, exact support inequalities and congruences,
all required nonzero coefficients, and the induced source and target spaces
for each normal layer. If the endpoint data do not determine a unique
intermediate support, return the finite alternatives and the exact first
underdetermined choice rather than selecting one implicitly.

### P6-L8B — Machine-readable replay

Status: local CAS task; blocked on P6-L8A.

Deliverable: encode the accepted support nodes and deterministic coordinate
edges with content hashes, replay the corner/lattice checks, and enumerate
each finite layer window from the stated inequalities.

### P6-L8C — Normal-layer obstruction at degree 125

Status: blocked on P6-L8A and P6-L8B.

Deliverable: build the determinant-layer operators and residue adjoints on
the recovered two-point windows and locate the first nonzero obstruction, or
prove exact solvability through a stated order while retaining every fresh
kernel parameter.

## Scope cautions

- A terminal unit ideal proves only its pinned system.
- Use the primitive exponent lattice, not a larger fractional cover.
- Saturation requires routing its complementary boundary chart.
- The below-`125` conclusion is a proof assembly: the finite Newton reduction
  is imported from the cited paper, while the two final support exclusions
  and their exact replays are internal.
- [`RMU-6D8E0011`](../working-mathematics/units/RMU-6D8E0011.md) is an incomplete proof strategy; its replayed local no-go
  calculations do not establish its global terminal-descent dichotomy.
- [`RMU-6D8E0012`](../working-mathematics/units/RMU-6D8E0012.md) certifies its stored equations, but it is not needed for and
  should not be inserted into the direct below-`125` proof.
- The displayed degree-six quotient determines the reduced terminal face,
  not the intervening Newton supports or a global two-sided attachment.
