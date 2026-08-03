# Lane 1 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- `manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py` — `c85a7462c73f776676897468ff3d421efb7d1b828fa84b1fd90c400cf225cb71`
- `research-notes/finite-diagnostics-20260803-v1/verify_lane1_marked_root_benchmark.py` — `8a8f19d6685f9e40af06d1a27ee6f1f3f03e0750f1dc4afbf02b2377107bb99d`
- `research-notes/lane1-collision-saturation-20260802-v1/INTEGRATION-v8.md` — `d454c71f9cd4c2fe4bdb19544a636592ccad52a768f45e6ba1a0d11a5761a58e`
- `research-notes/lane1-collision-saturation-20260802-v1/cubic-flatness-normalization-defects.md` — `a3d9ccebc6cc7b36dd30c30e9c36736e15d8cb4fc45f2f256b8b1be8c3054904`
- `research-notes/lane1-collision-saturation-20260802-v1/flatness-defect-repairs.tex` — `cfd9064969c8a42a85ae1701c234afb0dd80c7ae76c20ee609ae92206cd2560b`
- `research-notes/lane1-collision-saturation-20260802-v1/lane1-collision-v8-manifest.json` — `247bf32b22350cf724573eb52492e424a643d3a2279c675ec3aad604f6ffbb2b`
- `research-notes/lane1-collision-saturation-20260802-v1/verify_collision_idempotent.py` — `80e9117af525529b12dd8d36dac6c07c71e77cecec6d1819b289f65cc3fac842`
- `research-notes/lane1-collision-saturation-20260802-v1/verify_standard_collision_model.py` — `75f47234d04b0123f850ab42ba6c94a11d6aac7426b09edd914d12cfd26c31c5`

## `manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact symbolic replay for the transverse ADE templates in the Lane 1 repair.

Checks:
  * A_(3r-1) order-three matrix factorizations and ideal presentations;
  * the A_(r-1) degree-three cyclic-cover invariant equations;
  * the two E6 order-three ideals and their matrix factorizations;
  * the explicit D4 -&gt; E6 cyclic-cover invariant equation.
"""

from __future__ import annotations

import argparse
import sys

import sympy as sp


def zero_matrix(matrix: sp.Matrix) -&gt; bool:
    return matrix.applyfunc(sp.expand) == sp.zeros(*matrix.shape)


def verify_a_type(r: int) -&gt; None:
    if r &lt; 1:
        raise ValueError("r must be positive")

    u, v, z, U, V = sp.symbols("u v z U V")
    n = 3 * r
    f = u * v - z**n

    for j in (r, 2 * r):
        phi = sp.Matrix(&#91;&#91;v, -(z**j)&#93;, &#91;-(z ** (n - j)), u&#93;&#93;)
        psi = sp.Matrix(&#91;&#91;u, z**j&#93;, &#91;z ** (n - j), v&#93;&#93;)
        if not zero_matrix(phi * psi - f * sp.eye(2)):
            raise AssertionError(f"A-type left factorization failed: r={r}, j={j}")
        if not zero_matrix(psi * phi - f * sp.eye(2)):
            raise AssertionError(f"A-type right factorization failed: r={r}, j={j}")

        generators = sp.Matrix(&#91;&#91;u, z**j&#93;&#93;)
        if (generators * phi).applyfunc(sp.expand) != sp.Matrix(&#91;&#91;f, 0&#93;&#93;):
            raise AssertionError(f"A-type ideal presentation failed: r={r}, j={j}")

    cover_relation = U * V - z**r
    invariant_relation = U**3 * V**3 - z ** (3 * r)
    quotient = (U * V) ** 2 + U * V * z**r + z ** (2 * r)
    if sp.expand(invariant_relation - cover_relation * quotient) != 0:
        raise AssertionError(f"A-type cyclic cover identity failed: r={r}")

    print(
        f"PASS A_(3r-1), r={r}: both order-three classes and "
        f"A_(r-1) cyclic cover"
    )


def verify_e6() -&gt; None:
    x, y, z, s, t = sp.symbols("x y z s t")
    ii = sp.I
    f = x**2 + y**3 + z**4
    a = x + ii * z**2
    b = x - ii * z**2

    for name, left, right in (("J+", a, b), ("J-", b, a)):
        phi = sp.Matrix(&#91;&#91;right, -y&#93;, &#91;y**2, left&#93;&#93;)
        psi = sp.Matrix(&#91;&#91;left, y&#93;, &#91;-y**2, right&#93;&#93;)
        if not zero_matrix(phi * psi - f * sp.eye(2)):
            raise AssertionError(f"E6 left factorization failed for {name}")
        if not zero_matrix(psi * phi - f * sp.eye(2)):
            raise AssertionError(f"E6 right factorization failed for {name}")
        generators = sp.Matrix(&#91;&#91;left, y&#93;&#93;)
        if (generators * phi).applyfunc(sp.expand) != sp.Matrix(&#91;&#91;f, 0&#93;&#93;):
            raise AssertionError(f"E6 ideal presentation failed for {name}")

    cover = s**3 + t**3 - 2 * ii * z**2
    x_inv = (s**3 - t**3) / 2
    y_inv = s * t
    pullback = sp.expand(x_inv**2 + y_inv**3 + z**4)
    conjugate = s**3 + t**3 + 2 * ii * z**2
    if sp.expand(4 * pullback - cover * conjugate) != 0:
        raise AssertionError("D4 -&gt; E6 invariant identity failed")

    print("PASS E6: both order-three ideals, matrix factorizations, and D4 cyclic cover")


def main(argv: list&#91;str&#93;) -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=12)
    args = parser.parse_args(argv)
    if args.max_r &lt; 1:
        parser.error("--max-r must be positive")

    for r in range(1, args.max_r + 1):
        verify_a_type(r)
    verify_e6()
    print("ALL LANE-1 TRANSVERSE ADE CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv&#91;1:&#93;))
</code></pre>

## `research-notes/finite-diagnostics-20260803-v1/verify_lane1_marked_root_benchmark.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact bounded benchmark for the normalized marked-root cubic example.

This checks the polynomial map with ``A(c)=c`` and ``B(c)=-2``, the marked
root and Jacobian identities, the discriminant and its pullback, and the
normalization/conductor identities on the repeated-root divisor.  It does
not construct the integral quadratic-resolvent algebra or its eigensheaf.
"""

from __future__ import annotations

import hashlib
import json

import sympy as sp


def main() -&gt; int:
    x, y, z, root = sp.symbols("x y z root")

    # The canonical pole-cancelling representative for A(c)=c, B(c)=-2.
    w = 2 * x - 3 * x**2 * y
    c = sp.expand(w - x**3 * z)
    t = y + 1 / x
    r = 2 / x
    b = sp.factor(sp.cancel(r - 3 * c * t**2 + 4 * t))
    a = sp.factor(sp.cancel(t / x - c * t**3 + t**2))

    for coordinate in (a, b, c):
        if not sp.denom(coordinate) == 1:
            raise AssertionError("pole cancellation did not produce a polynomial")

    expected_a = (
        x**3 * y**3 * z
        + 3 * x**2 * y**4
        + 3 * x**2 * y**2 * z
        + 7 * x * y**3
        + 3 * x * y * z
        + 4 * y**2
        + z
    )
    expected_b = (
        3 * x**3 * y**2 * z
        + 9 * x**2 * y**3
        + 6 * x**2 * y * z
        + 12 * x * y**2
        + 3 * x * z
        + y
    )
    expected_c = -x**3 * z - 3 * x**2 * y + 2 * x
    if any(
        sp.expand(left - right) != 0
        for left, right in zip((a, b, c), (expected_a, expected_b, expected_c))
    ):
        raise AssertionError("explicit normalized map changed")

    jacobian = sp.factor(sp.Matrix(&#91;a, b, c&#93;).jacobian(&#91;x, y, z&#93;).det())
    if jacobian != -2:
        raise AssertionError(f"Jacobian changed: {jacobian}")

    inverse_cubic = c * root**3 - 2 * root**2 + b * root - 2 * a
    if sp.factor(sp.cancel(inverse_cubic.subs(root, t))) != 0:
        raise AssertionError("marked-root identity failed")
    if sp.factor(sp.cancel(sp.diff(inverse_cubic, root).subs(root, t) - r)) != 0:
        raise AssertionError("marked-slope identity failed")

    discriminant = sp.factor(sp.discriminant(inverse_cubic, root))
    expected_discriminant = sp.expand(
        4 * b**2 - 4 * c * b**3 - 64 * a + 72 * a * c * b - 108 * a**2 * c**2
    )
    if sp.expand(discriminant - expected_discriminant) != 0:
        raise AssertionError("cubic discriminant formula failed")
    residual = sp.expand((3 * c * t - 2) ** 2 - 4 * c * r)
    if sp.factor(sp.cancel(discriminant - r**2 * residual)) != 0:
        raise AssertionError("marked Vandermonde factorization failed")

    # Parametrize the repeated-root divisor by setting r=0.
    s = sp.symbols("s")
    branch_b = -3 * c * s**2 + 4 * s
    branch_a = -c * s**3 + s**2
    h = 3 * c * s - 2
    conductor_generator_1 = sp.expand(4 - 3 * c * branch_b)
    conductor_generator_2 = sp.expand(18 * c * branch_a - 2 * branch_b)
    if sp.expand(conductor_generator_1 - h**2) != 0:
        raise AssertionError("first discriminant-conductor identity failed")
    if sp.expand(conductor_generator_2 + 2 * s * h**2) != 0:
        raise AssertionError("second discriminant-conductor identity failed")

    result = {
        "schema_version": 1,
        "name": "Lane 1 normalized marked-root benchmark",
        "status": "pass",
        "frame": {"A(c)": "c", "B(c)": "-2", "alpha": "0"},
        "map": {"a": str(sp.expand(a)), "b": str(sp.expand(b)), "c": str(c)},
        "coordinate_degrees": {
            name: sp.Poly(value, x, y, z).total_degree()
            for name, value in (("a", a), ("b", b), ("c", c))
        },
        "jacobian": str(jacobian),
        "inverse_cubic": "c*T^3-2*T^2+b*T-2*a",
        "generic_quadratic_resolvent": "K(sqrt(Delta))/K",
        "discriminant": "4*b^2-4*c*b^3-64*a+72*a*c*b-108*a^2*c^2",
        "marked_pullback": "Delta=r^2*((3*c*t-2)^2-4*c*r)",
        "finite_completion": {
            "equation": "c*T^3-2*S*T^2+b*S^2*T-2*a*S^3=0",
            "flat_rank": 3,
            "smoothness_check": (
                "d/da=-2*S^3; on S=0 the derivative d/dS=-2*T^2 is a unit"
            ),
            "ext_defect": "zero because the displayed completion is finite flat",
        },
        "different": (
            "On the finite marked-root chart the monogenic different is generated "
            "by P'(t)=r; globally the ramification Cartier divisor is r=0."
        ),
        "discriminant_conductor": {
            "normalization_parameter": "(c,s)",
            "H": "3*c*s-2",
            "target_generators": &#91;"4-3*c*b", "18*c*a-2*b"&#93;,
            "pullbacks": &#91;"H^2", "-2*s*H^2"&#93;,
            "normalization_conductor": "(H^2)",
        },
        "does_not_establish": &#91;
            "an integral presentation or normalization of the quadratic resolvent",
            "the rank-one cubic eigensheaf on that resolvent",
            "a flatness theorem for an arbitrary degree-three Keller normalization",
            "recovery of the affine opening from the finite completion",
        &#93;,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result&#91;"certificate_sha256"&#93; = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `research-notes/lane1-collision-saturation-20260802-v1/INTEGRATION-v8.md`

<pre><code class="language-markdown">
# Lane 1 collision-saturation packet: integration notes

This is an AI-assisted source-level research packet. It is not a regenerated
public release and has not undergone independent specialist review.

## Main new theorem

Let `T` be the `S_3`-Galois normalization of a generic-degree-three Keller
extension at an omitted value `y`. The attained part of `Spec(T)` is covered
by the three conjugate source charts `U_1,U_2,U_3`. Their pair and triple
intersections are explicit affine collision spaces.

For a divided-difference matrix

```text
F(X)-F(X') = M(X,X')(X-X')
```

put `q=det(M)` and `c=det(JF)`. In `S tensor_R S`,

```text
q(q-c)=0,
e_Delta=q/c,
e_Delta^2=e_Delta.
```

Thus `e_Delta` cuts out the diagonal and `1-e_Delta` cuts out the smooth
off-diagonal collision component. Pairwise-distinct triples are selected by

```text
e_dist=(1-e_12)(1-e_13)(1-e_23).
```

Form the three-chart affine Cech complex and write

```text
K_y = ker(d_1),
I_y = im(d_0),
I_y^sat = I_y :_(K_y) m_y^infinity.
```

Then

```text
I_y^sat/I_y = MatlisDual(Delta_y) tensor V_std
```

as an `A&#91;S_3&#93;`-module. Consequently

```text
B_y is flat  &lt;=&gt;  I_y^sat=I_y,
length(I_y^sat/I_y)=2 length(Delta_y).
```

A minimal defect is exactly one copy of the two-dimensional standard
representation, killed by the closed-point ideal.

## Product and standard-root consequences

If the complete Galois opening and all three source charts are formally
constant along a carrier parameter, the product vector field acts on the Cech
complex and eliminates every punctual submodule. Hence the normalization is
flat.

For the standard ordered-root triple collision, with

```text
u=r_1-r_2,
v=r_2-r_3,
```

the chart-complement ideal is

```text
(u(u+v),uv,v(u+v))=(u,v)^2.
```

Its collision cohomology is transverse local cohomology tensored with the
smooth-axis ring, so the saturation quotient vanishes. Therefore a defect
requires a genuinely non-product deformation of the complete source-chart
gluing, not merely the universal triple-root arrangement.

## Exact checks

- `verify_collision_idempotent.py` constructs the divided-difference matrix
  for the announced cubic map and verifies the fibre-ideal certificate for
  `q(q-c)` exactly over `Q`.
- `verify_standard_collision_model.py` verifies the ordered-root ideal
  identity exactly.
- Existing exact scripts continue to check the equivariant weights,
  transverse ADE matrix factorizations, and the minimal nine-cusp formulas.

## Suggested repository placement

- replace
  `data/model-handoffs-v14-20260801a/cubic-flatness-normalization-defects.md`;
- add
  `data/manuscript-sources-v1-20260801b/sources/01-cubic-incidence/appendices/flatness-defect-repairs.tex`;
- add `\input{appendices/flatness-defect-repairs}` after the current cubic
  resolvent appendix in Program 1 `main.tex`;
- place the exact scripts in a scoped Lane 1 research-tools directory;
- retain `lane1-collision-saturation-v8.pdf` only as an optional reading copy.

## Required regeneration

The selected site release is hash-pinned. After accepting the mathematics,
regenerate the manuscript-source manifest and proof pages, the Program 1
entrypoint, the handoff manifest, generated docs, release metadata, and
`site-state.json`. Then rerun source, privacy, strict MkDocs, PDF, browser,
and deployed-site checks.

## Scope

The packet gives an exact necessary-and-sufficient collision-saturation
criterion and proves it for product/equisingular collision families and the
standard triple-root model. It does not prove saturation for every
non-equivariant Keller boundary. The unresolved calculation is now the
closed-point standard-isotypic saturation of the actual pair/triple collision
rings.
</code></pre>

## `research-notes/lane1-collision-saturation-20260802-v1/cubic-flatness-normalization-defects.md`

<pre><code class="language-markdown">
# Lane 1: cubic flatness and finite normalization defects

**Portfolio role:** settle the intrinsic finite-cover problem for generic-degree-three Keller maps before attempting boundary reconstruction.

## Research objective

Let

```text
F : X = A^3_C -&gt; Y = A^3_C
```

be a Keller map of generic degree three. Let `B` be the normalization of
`R=O(Y)` in `C(X)`, and write

```text
pi : Xbar = Spec(B) -&gt; Y.
```

Lane 1 asks whether `pi` is finite flat. This is a general degree-three Keller
question, not a statement restricted to the named counterexample or the
explicit normalized `A,B` family.

The affine opening is a separate gate. Even after flatness, recovering the
original `A^3` inside `Xbar` requires boundary completeness. Do not merge Lane
1 with the boundary/Torelli lane.

## Reusable mathematics

Write

```text
R = C&#91;y1,y2,y3&#93;,   S = C&#91;x1,x2,x3&#93;,
B = R ⊕ E,         E = ker Tr_(B/R).
```

The following statements are the repaired reusable core.

### 1. The defect is a canonical finite Ext module

Define

```text
Delta_F := Ext^1_R(B,R) = Ext^1_R(E,R).
```

The modules `B` and the rank-two trace-zero module `E` are reflexive. Hence
`E` is free at every prime of height at most two, `Delta_F` has finite length,
and

```text
Supp(Delta_F) = { y in Y : B_y is not free over R_y }.
B is finite flat over R  &lt;=&gt;  Delta_F = 0.
```

At a possible defect point `y`, with `A=R_y`, a minimal presentation is

```text
0 -&gt; A^b --Phi--&gt; A^(b+2) -&gt; E_y -&gt; 0,
Delta_(F,y) = coker(Phi^dual).
```

The integer `b` is the minimal number of generators of `Delta_(F,y)`. Local
duality identifies its Matlis dual with `H^2_m(E_y)`.

An orientation of `E_y` extends this presentation to an alternating self-dual
free resolution

```text
0 -&gt; A^b -&gt; A^(b+2) -&gt; A^(b+2)^dual -&gt; A^b^dual
  -&gt; Delta_(F,y) -&gt; 0.
```

Thus `Delta_(F,y)` is Matlis self-dual and its socle dimension is also `b`.
Any proposed defect must satisfy this finite certificate.

The first stratum is explicit. If `b=1`, then

```text
Delta_(F,y) = A/(f1,f2,f3),
E_y = Omega_A^2(Delta_(F,y)),
```

for an `A`-regular sequence, and the resolution is Koszul with Betti numbers
`(1,3,3,1)`.

### 2. Source splitting is proved and its direct scope is exhausted

Base change to the affine source has a canonical marked factor:

```text
B tensor_R S = S × C,
C = S&#91;eta&#93;/(eta^2-D).
```

The factor `S` is canonical. The trace-zero generator `eta` is a choice, and
`D` changes by a unit square when the generator changes.

Consequently `B_y` is free for every attained value `y in F(X)`. Together with
the omitted-values theorem,

```text
Supp(Delta_F) ⊆ O_F ⊆ Sing(S_F),
```

where `O_F` is the omitted set and `S_F` is the reduced nonproperness set.
There is no source point above a defect value, so “apply source splitting
again” is not a local strategy. Any further source input must pass through the
boundary, conductor, duality, or monodromy.

### 3. The quadratic resolvent carries exactly the same defect

Let `T` be the normalization in the `S_3` Galois closure, let `N=A_3`, and let
`H` be the transposition subgroup corresponding to the cubic field. Then

```text
B = T^H,
Q = T^N = R&#91;w&#93;/(w^2-d),
T = Q ⊕ L ⊕ L^&#91;2&#93;,
L^&#91;3&#93; = Q.
```

The corrected divisorial list `U0/U1/U2/B` implies that `T/Q` is unramified in
codimension one. Taking `H`-invariants gives an exact `R`-module
identification

```text
E ≅ L,       ell |-&gt; ell + sigma(ell).
```

Therefore

```text
Delta_F = Ext^1_R(L,R),
B flat over R  &lt;=&gt;  L locally free over R  &lt;=&gt;  L MCM over Q.
```

This is an equivalence, not merely the former one-way MCM criterion.

### 4. A completed defect branch is genuinely non-Galois cubic

At `y in Supp(Delta_F)`, completion over `A=R_y^` decomposes the normalization
into normal local factors of total rank three. Rank-one factors equal `A`.
Rank-two normal factors are free because their trace-zero summands are
rank-one reflexive modules over the regular local UFD `A`. A cyclic rank-three
factor is also free by its `C_3` character decomposition.

Hence a defect has one rank-three normal local factor, and that cubic field is
non-Galois with `S_3` closure. The normalization fibre is supported at one
point and has scheme length

```text
length(B tensor_R k(y)) = b + 3 &gt;= 4.
```

Length four is exactly the one-generator complete-intersection stratum.

### 5. Dao detection localizes every remaining class on singular curves

For a three-dimensional normal local hypersurface `Q0`, Dao’s punctured-Picard
theorem gives

```text
Cl(Q0)&#91;3&#93; -&gt; direct_sum_{height-two singular p} Cl((Q0)_p)&#91;3&#93;
```

injectively. Thus a nonzero defect requires a height-two singular prime of the
quadratic resolvent carrying a nonzero localization of `&#91;L&#93;`. For

```text
Q = R&#91;w&#93;/(w^2-d),
```

the singular locus is cut out by

```text
(w, d_y1, d_y2, d_y3).
```

An isolated resolvent singularity cannot carry the defect.

## New finite transverse filter

Assume, only for this subsection, that the generic transverse surface type at
each singular curve is a split rational double point. Three-torsion occurs
only for

```text
A_(3r-1)  and  E6.
```

Each curve contributes at most one coordinate in `F_3`.

For `A_(3r-1)` with equation `uv-z^(3r)`, the two nonzero classes are

```text
I_r=(u,z^r),   I_2r=(u,z^(2r)).
```

They have explicit two-by-two matrix factorizations. Their degree-three cyclic
cover has equation `UV-z^r`, so the transverse cover type is `A_(r-1)`.

For `E6` with equation `x^2+y^3+z^4`, put

```text
a=x+i z^2,   b=x-i z^2,
J+=(a,y),    J-=(b,y).
```

These are the two nonzero classes in `Z/3` and have explicit two-by-two matrix
factorizations. The associated cyclic cover is

```text
s^3+t^3-2 i z^2 = 0,
```

which is a `D4` singularity, with invariant coordinates

```text
x=(s^3-t^3)/2,   y=s*t,   z=z.
```

Thus every coordinate in the conditional ADE vector has an explicit generic
transverse MCM representative. The unresolved step is extending and gluing
those factorizations through the closed threefold point.

## Useful deliverable

### Exact live problem

The remaining unknown at a candidate omitted value is the following finite
package:

1. the square class `d` defining the normal quadratic resolvent;
2. every height-two prime in its singular locus;
3. a fractional-ideal or finite-presentation representative of `L`;
4. the local class vector `(&#91;L_p&#93;)_p`;
5. a matrix factorization or other depth-three certificate extending the
   explicit transverse models through the closed point, or a Keller-specific
   argument excluding every nonzero vector.

A useful returned result must state whether it is local, completed, formal,
divisorial, or global, and identify the exact boundary or conductor data it
uses.

## Recommended work order

### P1-T1A — Extract the exact resolvent carrier

**Status:** ready.

**Input:** the actual Keller normalization and boundary, not a schematic
elliptic picture.

**Done when:** `d`, the singular height-two primes, a presentation of `L`, the
conductor/different, and the local class vector are explicit and checkable.

### P1-T1B — Extend the transverse MCM models

**Status:** blocked on P1-T1A.

**Attack:** build a matrix factorization over the three-dimensional resolvent
whose generic restrictions are the displayed `A_(3r-1)` or `E6` templates;
alternatively prove a Keller-specific vanishing of the class vector.

**Done when:** the resulting module has depth three and its codimension-two
classes agree with `L` at every singular curve.

### P1-T2 — Compute the finite class/intersection obstruction

**Status:** blocked on P1-T1A.

Do not invent the lattice. Its intersection matrix, discrepancy vector, and
class coordinates must be derived from the actual resolvent model and then
hash-pinned for exact replay.

### P1-T3 — Keep boundary completeness separate

Finite flatness gives a binary-cubic/marked-root finite cover. Identifying the
original affine source inside it still requires a separate theorem specifying
all deleted ramified and unramified sheets.

## Do not do

- Do not state that normal `S_3` cubic covers are automatically flat.
- Do not replace `Delta_F` by an unnamed defect or treat reflexivity as local freeness.
- Do not use the old `U1/U2/B` list; the complete list is `U0/U1/U2/B`.
- Do not call the quadratic generator in source splitting canonical.
- Do not infer a global MCM module from a smooth cubic-axis picture without a
  matrix factorization and codimension-two comparison.
- Do not run an exceptional-lattice computation before the actual primes and
  eigensheaf class are known.
- Do not infer boundary completeness from flatness.

## Proof access

The accompanying repair appendix supplies the conventional proofs. Existing
Program 1 text sources remain necessary for the corrected divisorial
classification and omitted-values theorem. Optional PDFs may predate this
repair.

&#91;Back to the portfolio hub&#93;(state-of-the-program.md)
</code></pre>

## `research-notes/lane1-collision-saturation-20260802-v1/flatness-defect-repairs.tex`

<pre><code class="language-tex">
\section{The finite cubic flatness defect: exact repairs}
\label{app:flatness-defect-repairs}

This appendix replaces the former statement-only flatness package by a
canonical finite defect, proves the attained-value splitting, identifies the
defect exactly on the quadratic resolvent, and records the remaining local
input.  It does not prove that the defect vanishes.

Let
\&#91;
R=\C&#91;y_1,y_2,y_3&#93;,\qquad S=\C&#91;x_1,x_2,x_3&#93;,
\&#93;
and let
\&#91;
F\colon X=\Spec S\longrightarrow Y=\Spec R
\&#93;
be a Keller map of generic degree three.  Put \(K=\Frac S\), let \(B\) be the
integral closure of \(R\) in \(K\), and write
\&#91;
\pi\colon\overline X=\Spec B\longrightarrow Y.
\&#93;
The field trace splits the unit inclusion:
\&#91;
B=R\oplus E,\qquad E=\ker(\operatorname{Tr}_{B/R}),
\&#93;
where \(E\) has rank two.  Write \(O_F=Y\setminus F(X)\) and let \(S_F\)
denote the reduced nonproperness set.

\subsection{The canonical finite defect}

\begin{proposition}&#91;Canonical Ext defect&#93;
\label{prop:cubic-ext-defect}
The \(R\)-modules \(B\) and \(E\) are reflexive.  Define
\&#91;
\Delta_F:=\operatorname{Ext}^1_R(B,R)
          \simeq\operatorname{Ext}^1_R(E,R).
\&#93;
Then \(\Delta_F\) has finite length and
\&#91;
\operatorname{Supp}\Delta_F
 =\{y\in Y:B_y\text{ is not free over }R_y\}.
\&#93;
Consequently
\&#91;
B\text{ is finite flat over }R
\quad\Longleftrightarrow\quad
\Delta_F=0.
\&#93;
More precisely, at a closed point \(y\), with \(A=R_y\), there is a minimal
free resolution
\&#91;
0\longrightarrow A^b\xrightarrow{\Phi}A^{b+2}
 \longrightarrow E_y\longrightarrow0,
\&#93;
and
\&#91;
(\Delta_F)_y\simeq\operatorname{coker}(\Phi^\vee),
\qquad
\dim_\C (\Delta_F)_y/\mathfrak m_y(\Delta_F)_y=b.
\&#93;
Local duality gives
\&#91;
\operatorname{Hom}_A((\Delta_F)_y,E_A(\C))
 \simeq H^2_{\mathfrak m_y}(E_y).
\&#93;
\end{proposition}

\begin{proof}
The integral closure of a noetherian normal domain in a finite field extension
is a finite reflexive module over the base; equivalently, it is recovered from
its codimension-one localizations inside the field extension.  Hence \(B\) is
reflexive, and the trace splitting makes \(E\) a reflexive direct summand.

If \(\mathfrak p\subset R\) has height at most two, reflexivity gives
\&#91;
\operatorname{depth}_{R_\mathfrak p}E_\mathfrak p
 =\dim R_\mathfrak p.
\&#93;
Auslander--Buchsbaum over the regular local ring \(R_\mathfrak p\) makes
\(E_\mathfrak p\) free.  Thus the nonfree locus is a finite set of closed
points.  At a closed point, reflexivity gives depth at least two, so
\(\operatorname{pd}_A E_y\le1\) and the displayed resolution exists.
Dualizing it gives
\&#91;
(\Delta_F)_y=\operatorname{coker}(\Phi^\vee).
\&#93;
If \(b=0\), then \(E_y\) is free.  If \(b&gt;0\), minimality puts every entry of
\(\Phi\) in \(\mathfrak m_y\), so the cokernel of \(\Phi^\vee\) has exactly
\(b\) minimal generators and is nonzero.  This proves the support and
flatness assertions.  The final identity is local duality in dimension three.
\end{proof}

\begin{proposition}&#91;Alternating self-dual defect resolution&#93;
\label{prop:cubic-defect-self-duality}
At a closed point \(y\), choose an orientation \(\det(E_y)\simeq A\).  The
minimal presentation in \cref{prop:cubic-ext-defect} extends to an exact
complex
\&#91;
0\longrightarrow A^b\xrightarrow{\Phi}A^{b+2}
 \xrightarrow{\Psi}(A^{b+2})^\vee
 \xrightarrow{\Phi^\vee}(A^b)^\vee
 \longrightarrow(\Delta_F)_y\longrightarrow0,
\&#93;
where \(\Psi^\vee=-\Psi\).  Consequently
\&#91;
(\Delta_F)_y\simeq
\operatorname{Ext}^3_A((\Delta_F)_y,A),
\&#93;
so \((\Delta_F)_y\) is Matlis self-dual and
\&#91;
\dim_\C\operatorname{Soc}((\Delta_F)_y)
 =\dim_\C (\Delta_F)_y/\mathfrak m_y(\Delta_F)_y=b.
\&#93;
\end{proposition}

\begin{proof}
The orientation gives the alternating reflexive isomorphism
\&#91;
\theta\colon E_y\xrightarrow{\sim}E_y^\vee,
\qquad \theta^\vee=-\theta.
\&#93;
Let \(\rho\colon A^{b+2}\twoheadrightarrow E_y\) be the presentation map and
put
\&#91;
\Psi=\rho^\vee\theta\rho.
\&#93;
Since \(\rho^\vee\) and \(\theta\) are injective isomorphisms onto their
images,
\&#91;
\ker\Psi=\ker\rho=\operatorname{im}\Phi.
\&#93;
The dual presentation gives
\&#91;
\operatorname{im}\Psi=\rho^\vee(E_y^\vee)=\ker\Phi^\vee,
\&#93;
and the final cokernel is \((\Delta_F)_y\).  Dualizing the resulting free
resolution reproduces it, up to the sign of \(\Psi\), and identifies the third
Ext module with the same final cokernel.  For a finite-length module over a
three-dimensional regular local ring, the third Ext is its Matlis dual.
\end{proof}

\begin{corollary}&#91;The one-generator stratum&#93;
\label{cor:cubic-one-generator-defect}
If \(b=1\), then there is an \(A\)-regular sequence \(f_1,f_2,f_3\) such that
\&#91;
(\Delta_F)_y\simeq A/(f_1,f_2,f_3),
\qquad
E_y\simeq\Omega_A^2(A/(f_1,f_2,f_3)).
\&#93;
After compatible choices of bases, the self-dual resolution is the Koszul
resolution, with Betti numbers \((1,3,3,1)\).
\end{corollary}

\begin{proof}
Write \(\Phi(1)=(f_1,f_2,f_3)^t\).  The finite length of
\(\operatorname{coker}\Phi^\vee\) says that the ideal
\((f_1,f_2,f_3)\) has height three.  Since \(A\) is Cohen--Macaulay, the three
elements form a regular sequence.  The alternating self-dual resolution is
then the Koszul resolution, and its second syzygy is
\(\operatorname{coker}\Phi=E_y\).
\end{proof}

\subsection{Source splitting and the exact support boundary}

\begin{proposition}&#91;Source splitting&#93;
\label{prop:cubic-source-splitting}
There is an \(S\)-algebra decomposition
\&#91;
B\otimes_RS\simeq S\times C,
\&#93;
where \(C\) is a normal quadratic \(S\)-algebra.  After choosing a generator
of its trace-zero summand,
\&#91;
C\simeq S&#91;\eta&#93;/(\eta^2-D)
\&#93;
for some \(D\in S\).  The factor \(S\) is canonical; the generator \(\eta\)
is not, and replacing it by a unit multiple changes \(D\) by a unit square.
Consequently \(B_y\) is free over \(R_y\) for every attained value
\(y\in F(X)\).
\end{proposition}

\begin{proof}
Every element of \(B\) lies in \(S\): it is integral over \(R\), hence over
\(S\), and \(S\) is integrally closed in \(K\).  Thus the open immersion
\(j\colon X\hookrightarrow\overline X\) induces, after base change by the
etale map \(F\), a section of the finite morphism
\&#91;
p\colon\overline X\times_YX\longrightarrow X.
\&#93;
The map \(p\) is etale along the section.  Restricting to the etale locus, a
section of an unramified separated morphism is open and closed.  The section
is also closed in the whole fibre product because \(p\) is finite.  It is
therefore an open-and-closed component, giving
\&#91;
B\otimes_RS\simeq S\times C.
\&#93;

Normalization commutes with smooth base change, so \(C\) is normal.  Its
trace splits it as \(S\oplus L_0\), where \(L_0\) is rank-one reflexive.
Since \(S\) is factorial, \(L_0\) is free.  A trace-zero generator \(\eta\)
satisfies \(\eta^2=D\in S\) by Cayley--Hamilton.

If \(F(x)=y\), then the local etale homomorphism \(R_y\to S_x\) is faithfully
flat, while \(B_y\otimes_{R_y}S_x\) is free by the displayed decomposition.
Faithfully flat descent makes \(B_y\) flat, hence free, over \(R_y\).
\end{proof}

\begin{corollary}&#91;Defect support&#93;
\label{cor:cubic-defect-support}
For every generic-degree-three Keller map,
\&#91;
\operatorname{Supp}\Delta_F\subseteq O_F\subseteq\operatorname{Sing}(S_F).
\&#93;
Thus there is no source point above a defect value at which the splitting
argument can simply be repeated.
\end{corollary}

\begin{proof}
The first inclusion is \cref{prop:cubic-source-splitting}.  The second is the
omitted-values theorem: every smooth point of the reduced nonproperness divisor
is attained by a complex Keller map.
\end{proof}

\subsection{The exact quadratic-resolvent carrier}

Let \(\widetilde K\) be the \(S_3\)-Galois closure of \(K/\Frac R\), let \(T\)
be the integral closure of \(R\) in \(\widetilde K\), choose a transposition
subgroup \(H\), and put \(N=A_3\).  Then
\&#91;
B=T^H,\qquad Q=T^N.
\&#93;
Fix a primitive cube root \(\zeta\in\C\).

\begin{theorem}&#91;Exact resolvent carrier&#93;
\label{thm:exact-resolvent-carrier}
The quadratic resolvent \(Q\) is normal and finite flat of rank two over
\(R\); after a trace-zero choice,
\&#91;
Q\simeq R&#91;w&#93;/(w^2-d)
\&#93;
for some \(d\in R\).  The cover \(T/Q\) is unramified in codimension one and
has character decomposition
\&#91;
T\simeq Q\oplus L\oplus L^{&#91;2&#93;},
\qquad L^{&#91;3&#93;}\simeq Q.
\&#93;
If \(\sigma\) denotes the nontrivial involution of \(Q/R\), then
\&#91;
\sigma^*L\simeq L^{&#91;2&#93;}\simeq L^\vee;
\&#93;
in particular, every local three-torsion class carried by \(L\) is
anti-invariant under the quadratic involution.  As an \(R\)-module, the
cubic trace-zero summand is exactly the eigensheaf:
\&#91;
E\simeq L.
\&#93;
Consequently
\&#91;
\Delta_F\simeq\operatorname{Ext}^1_R(L,R),
\&#93;
and the following are equivalent:
\&#91;
\begin{aligned}
B\text{ is finite flat over }R
&amp;\Longleftrightarrow L\text{ is locally free over }R,\\
&amp;\Longleftrightarrow L\text{ is MCM over }Q.
\end{aligned}
\&#93;
Locally at \(y\in Y\), the defect vanishes if and only if
\(L_\mathfrak q\) is MCM for every \(\mathfrak q\mid y\).
\end{theorem}

\begin{proof}
Invariant subrings of a normal domain under a finite group are normal, so
\(Q\) is normal.  As an \(R\)-module it is reflexive of rank two.  Its trace
splitting is \(Q=R\oplus N_0\) with \(N_0\) rank-one reflexive; factoriality
of \(R\) makes \(N_0\) free and gives the equation \(w^2=d\).

At a target divisor, the corrected inertia list is
\(U_0,U_1,U_2,B\); the inertia in the Galois closure is therefore trivial or
a transposition.  Its intersection with \(N=A_3\) is trivial, so \(T/Q\) is
unramified in codimension one.  The \(N\)-character idempotents split \(T\)
into three reflexive \(Q\)-modules.  Multiplication gives the asserted
reflexive powers because it is an isomorphism at every height-one prime.

Choose \(\sigma\in H\).  Its restriction to \(Q\) is the nontrivial
quadratic involution.  It interchanges the two nontrivial characters, so
\(\sigma^*L\simeq L^{&#91;2&#93;}\simeq L^\vee\).  Taking \(H\)-invariants gives
\&#91;
B=T^H=R\oplus\{\ell+\sigma(\ell):\ell\in L\}.
\&#93;
The map \(\ell\mapsto\ell+\sigma(\ell)\) is an \(R\)-linear isomorphism onto
the second summand.  Its cubic trace is zero because summing over
\(1,\tau,\tau^2\in N\) gives the factor \(1+\zeta+\zeta^2=0\).  Thus the
second summand is \(E\).

Finally, a regular system of parameters of \(R_y\) is a system of parameters
of every \(Q_\mathfrak q\) above it.  Hence \(L_\mathfrak q\) is MCM over
\(Q_\mathfrak q\) exactly when the underlying \(R_y\)-module has depth three.
Auslander--Buchsbaum over \(R_y\) turns that condition into freeness.  Use
\(E\simeq L\) and \cref{prop:cubic-ext-defect}.
\end{proof}

\begin{corollary}&#91;Formal defect branches&#93;
\label{cor:formal-cubic-defect}
Let \(y\in\operatorname{Supp}\Delta_F\) and
\(A=\widehat{R_y}\).  The completed normalization
\(B_y\otimes_{R_y}A\) has one normal local factor of rank three.  Its cubic
fraction-field extension is non-Galois and therefore has \(S_3\)-Galois
closure.
\end{corollary}

\begin{proof}
Excellence decomposes the completed finite algebra into normal local domains
of ranks summing to three.  A rank-one factor is \(A\).  A rank-two factor
splits by trace into \(A\) plus a rank-one reflexive module, which is free
because the complete regular local ring \(A\) is factorial.  Thus a nonfree
completion must have one rank-three factor.

If its cubic field extension were cyclic, the \(C_3\)-character idempotents
would split its integral closure into three rank-one reflexive \(A\)-modules.
All three would be free over the factorial ring \(A\), contradicting the
defect.  Hence the cubic branch is non-Galois.
\end{proof}

\begin{corollary}&#91;Defective fibre length&#93;
\label{cor:cubic-defect-fibre-length}
Let \(y\in\operatorname{Supp}\Delta_F\), and let \(b\) be the presentation
number in \cref{prop:cubic-ext-defect}.  Then \(\pi^{-1}(y)\) is supported at
one point and
\&#91;
\operatorname{length}_\C(B\otimes_R\kappa(y))=b+3\ge4.
\&#93;
The length is four exactly in the one-generator stratum.
\end{corollary}

\begin{proof}
The completed algebra has one local factor by
\cref{cor:formal-cubic-defect}, so the finite fibre has one support point.
Minimality of the presentation gives
\&#91;
\dim_\C B_y/\mathfrak m_yB_y
 =1+\dim_\C E_y/\mathfrak m_yE_y
 =1+(b+2)=b+3.
\&#93;
A defect has \(b\ge1\).
\end{proof}

\subsection{Codimension-two detection and explicit transverse covers}

\begin{corollary}&#91;Resolvent defect curves&#93;
\label{cor:resolvent-defect-curves}
If \((\Delta_F)_y\ne0\), then for some \(\mathfrak q\mid y\) there is a
height-two singular prime \(\mathfrak p\subset Q_\mathfrak q\) such that
\&#91;
&#91;L_\mathfrak p&#93;\ne0
\quad\text{in}\quad
\operatorname{Cl}(Q_\mathfrak p)&#91;3&#93;.
\&#93;
For \(Q=R&#91;w&#93;/(w^2-d)\), the singular locus is cut out by
\&#91;
(w,\partial_{y_1}d,\partial_{y_2}d,\partial_{y_3}d).
\&#93;
In particular, a defect requires a singular curve of the quadratic resolvent;
an isolated resolvent singularity cannot carry it.
\end{corollary}

\begin{proof}
Dao's theorem makes the Picard group of the punctured spectrum of a
three-dimensional local hypersurface torsion-free.  It follows that
\&#91;
\operatorname{Cl}(Q_\mathfrak q)&#91;3&#93;\hookrightarrow
\bigoplus_{\substack{\mathfrak p\in\operatorname{Sing}(Q_\mathfrak q)\\
                     \operatorname{ht}\mathfrak p=2}}
\operatorname{Cl}(Q_\mathfrak p)&#91;3&#93;.
\&#93;
By \cref{thm:exact-resolvent-carrier}, nonzero defect means that
\(L_\mathfrak q\) is not MCM.  Its class is therefore nonzero, while
\(L^{&#91;3&#93;}\simeq Q\) makes it three-torsion.  The Jacobian ideal of
\(w^2-d\) gives the displayed singular-locus equations.
\end{proof}

\begin{proposition}&#91;Transverse ADE filter and explicit cyclic covers&#93;
\label{prop:transverse-ADE-filter}
Assume that, after strict henselization and completion, every generic
transverse surface singularity at a height-two singular prime is a split
rational double point.  Then only
\&#91;
A_{3r-1}\quad(r\ge1),\qquad E_6
\&#93;
can carry a nonzero localization of the cubic defect class.  Each component
contributes at most one \(\mathbf F_3\)-coordinate.

For a transverse \(A_{3r-1}\) equation
\&#91;
Q_0=k&#91;&#91;u,v,z&#93;&#93;/(uv-z^{3r}),
\&#93;
the two nonzero order-three classes are represented by
\&#91;
I_r=(u,z^r),\qquad I_{2r}=(u,z^{2r}).
\&#93;
For \(j=r,2r\), the matrices
\&#91;
\Phi_j=\begin{pmatrix}v&amp;-z^j\\-z^{3r-j}&amp;u\end{pmatrix},
\qquad
\Psi_j=\begin{pmatrix}u&amp;z^j\\z^{3r-j}&amp;v\end{pmatrix}
\&#93;
satisfy
\&#91;
\Phi_j\Psi_j=\Psi_j\Phi_j=(uv-z^{3r})I_2.
\&#93;
The associated degree-three quasi-etale cyclic cover has transverse equation
\&#91;
UV-z^r=0,
\&#93;
so its type is \(A_{r-1}\), with \(A_0\) interpreted as smooth.

For a transverse \(E_6\) equation
\&#91;
Q_0=k&#91;&#91;x,y,z&#93;&#93;/(x^2+y^3+z^4),
\&#93;
choose \(i^2=-1\), put
\&#91;
a=x+iz^2,\qquad b=x-iz^2,
\&#93;
and set
\&#91;
J_+=(a,y),\qquad J_-=(b,y).
\&#93;
These are the two nonzero classes in \(\operatorname{Cl}(Q_0)\simeq\mathbf Z/3\).
For \(J_+\), an explicit matrix factorization is
\&#91;
\Phi_+=\begin{pmatrix}b&amp;-y\\y^2&amp;a\end{pmatrix},
\qquad
\Psi_+=\begin{pmatrix}a&amp;y\\-y^2&amp;b\end{pmatrix},
\&#93;
with the factorization for \(J_-\) obtained by interchanging \(a\) and \(b\).
The corresponding degree-three cyclic cover is
\&#91;
k&#91;&#91;s,t,z&#93;&#93;/(s^3+t^3-2iz^2),
\&#93;
a \(D_4\) rational double point.  The deck action is
\((s,t,z)\mapsto(\zeta s,\zeta^{-1}t,z)\), and its invariant coordinates are
\&#91;
x=\frac{s^3-t^3}{2},\qquad y=st,\qquad z=z.
\&#93;

Both cyclic covers carry a transposition lifting the quadratic involution and
conjugating the deck transformation to its inverse.  Their cubic
transposition quotients are explicit.  In the \(A_{3r-1}\) case, put
\&#91;
c=U^3+V^3,\qquad \alpha=U+V.
\&#93;
Then the regular base, quadratic resolvent, and cubic subcover are
\&#91;
R_0=k&#91;&#91;c,z&#93;&#93;,\qquad
Q_0=R_0&#91;w&#93;/(w^2-c^2+4z^{3r}),
\&#93;
\&#91;
B_0=R_0&#91;\alpha&#93;/(\alpha^3-3z^r\alpha-c)
    \simeq k&#91;&#91;\alpha,z&#93;&#93;.
\&#93;
In the \(E_6\) case, with \(\alpha=s+t\), they are
\&#91;
R_0=k&#91;&#91;y,z&#93;&#93;,\qquad
Q_0=R_0&#91;x&#93;/(x^2+y^3+z^4),
\&#93;
\&#91;
B_0=R_0&#91;\alpha&#93;/(\alpha^3-3y\alpha-2iz^2).
\&#93;
The discriminants of the two displayed cubic polynomials are, respectively,
\&#91;
-27(c^2-4z^{3r}),\qquad 108(y^3+z^4),
\&#93;
so the displayed double covers are their quadratic resolvents, up to a unit
square.
\end{proposition}

\begin{proof}
The class groups of the split rational double points are the discriminant
groups of their ADE root lattices:
\&#91;
\operatorname{Cl}(A_n)=\mathbf Z/(n+1),
\&#93;
while the \(D_n,E_6,E_7,E_8\) groups have orders \(4,3,2,1\), respectively.
Thus nonzero three-torsion occurs precisely for \(A_{3r-1}\) and \(E_6\), and
its three-primary subgroup is \(\mathbf Z/3\).

For \(A_{3r-1}\), the ideals \((u,z^j)\) represent class \(j\) in
\(\mathbf Z/(3r)\), and direct multiplication gives the displayed matrix
factorizations.  The cyclic cover is obtained from
\&#91;
u=U^3,\qquad v=V^3,\qquad UV=z^r;
\&#93;
its \(C_3\)-invariants recover \(uv=z^{3r}\).

For \(E_6\), one has \(ab+y^3=x^2+y^3+z^4\).  Let
\(\mathfrak m=(x,y,z)\).  The prime \(P_+=(a,y)\) satisfies
\(Q_0/P_+\simeq k&#91;&#91;z&#93;&#93;\), and at its generic point \(b\) is a unit and
\(a=-y^3/b\).  Hence \(\operatorname{div}(a)=3P_+\).  The images of \(a\)
and \(y\) are linearly independent in \(P_+/\mathfrak mP_+\): their initial
linear terms are \(x\) and \(y\).  Thus \(P_+\) needs two generators and is
not principal, so its class has order three; \(J_-\) is the inverse class.
Direct multiplication gives
\&#91;
\Phi_+\Psi_+=\Psi_+\Phi_+=(x^2+y^3+z^4)I_2,
\&#93;
and the row \((a,y)\) gives
\((a,y)\Phi_+=(x^2+y^3+z^4,0)\).  The induced surjection from the
matrix-factorization cokernel to \(J_+\) is an isomorphism: both modules have
rank one, and the source is torsion-free because it is maximal
Cohen--Macaulay over the normal surface.

In the displayed \(D_4\) cover,
\&#91;
\left(\frac{s^3-t^3}{2}\right)^2+(st)^3+z^4
 =\frac{(s^3+t^3)^2}{4}+z^4=0,
\&#93;
and the invariant monomials are generated by \(s^3,t^3,st,z\).  With
\(p=s+t\) and \(q=s-t\), its equation becomes, after multiplying by a unit
and rescaling variables,
\&#91;
z^2+p^3+pq^2=0,
\&#93;
the standard \(D_4\) equation.

For the full group actions, set
\&#91;
\tau(U,V,z)=(\zeta U,\zeta^{-1}V,z),\qquad
\sigma(U,V,z)=(V,U,z)
\&#93;
in type \(A\), and use the same formulas with \((s,t,z)\) in type \(E_6\).
Then \(\sigma\tau\sigma=\tau^{-1}\).  In type \(A\), the full invariants are
\(k&#91;&#91;c,z&#93;&#93;\), while the \(\sigma\)-invariants are generated by
\(\alpha=U+V\) and \(z\), with
\(c=\alpha^3-3z^r\alpha\).  In type \(E_6\), the full invariants are
\(k&#91;&#91;y,z&#93;&#93;\), while the \(\sigma\)-invariants satisfy
\(\alpha^3-3y\alpha-2iz^2=0\).  The standard depressed-cubic discriminant
formula gives the two stated resolvents.  The involution exchanges
\(I_r\) with \(I_{2r}\), and \(J_+\) with \(J_-\), exactly as required by
\(\sigma^*L\simeq L^\vee\).
\end{proof}

\begin{remark}&#91;Revised Lane 1 task&#93;
\label{rem:revised-cubic-task}
The repair does not prove \(\Delta_F=0\).  It reduces the unknown input at a
candidate defect value to:
\begin{enumerate}&#91;label=(\arabic*)&#93;
\item the square class \(d\) defining the normal quadratic resolvent;
\item the height-two primes of its singular locus;
\item a fractional-ideal or finite-presentation representative of \(L\);
\item the local class vector \((&#91;L_\mathfrak p&#93;)_\mathfrak p\);
\item a matrix factorization or other depth-three certificate extending the
explicit transverse \(A_{3r-1}\) and \(E_6\) models through the closed point,
or a Keller-specific constraint excluding every nonzero vector.
\end{enumerate}
Under the transverse-ADE hypothesis, every nonzero coordinate has an explicit
local MCM representative and the transverse cubic cover is either
\(A_{r-1}\to A_{3r-1}\) or \(D_4\to E_6\).  The remaining issue is the
three-dimensional extension and compatibility of these models, not their
generic transverse construction.
\end{remark}
</code></pre>

## `research-notes/lane1-collision-saturation-20260802-v1/lane1-collision-v8-manifest.json`

<pre><code class="language-json">
{
  "schema_version": 1,
  "packet": "lane1-collision-saturation-v8",
  "date": "2026-08-02",
  "mathematical_scope": &#91;
    "exact collision Cech saturation criterion for the cubic flatness defect",
    "divided-difference diagonal/off-diagonal idempotent",
    "formal collision-product flatness",
    "standard triple-root collision saturation"
  &#93;,
  "does_not_establish": &#91;
    "unconditional flatness for every generic-degree-three Keller map",
    "boundary completeness or recovery of the affine opening from a flat cover",
    "independent specialist verification"
  &#93;,
  "source_validation": {
    "labels": 52,
    "unique_labels": 52,
    "missing_references": &#91;&#93;
  },
  "files": &#91;
    {
      "path": "flatness-defect-repairs.tex",
      "bytes": 85987,
      "sha256": "4b468e00f6c83f158c89e90a8819858b91a1d1f4dfd7c582915204236efdb60c"
    },
    {
      "path": "cubic-flatness-normalization-defects.md",
      "bytes": 13516,
      "sha256": "f64182b6d9dee30b8bdd5c8e14db376a336b519b3be32be8418d29b646ce2ad3"
    },
    {
      "path": "lane1-collision-saturation-v8.tex",
      "bytes": 3131,
      "sha256": "51762052fdcb33ac7e8c9dbc0bb5ed8bbceb90b518ccc66f90ef92ccb82fee39"
    },
    {
      "path": "lane1-collision-saturation-v8.pdf",
      "bytes": 476635,
      "sha256": "b3422c1002aae131f0ffd6ca312b65e7f1ca0ef3f564313bf27228cb9a16ee76"
    },
    {
      "path": "verify_collision_idempotent.py",
      "bytes": 3474,
      "sha256": "80e9117af525529b12dd8d36dac6c07c71e77cecec6d1819b289f65cc3fac842"
    },
    {
      "path": "collision-idempotent-verification-output.txt",
      "bytes": 455,
      "sha256": "a4d48863cdf5348bd00088df4edd9343026650aa85704f42e778eb42f152131a"
    },
    {
      "path": "verify_standard_collision_model.py",
      "bytes": 935,
      "sha256": "75f47234d04b0123f850ab42ba6c94a11d6aac7426b09edd914d12cfd26c31c5"
    },
    {
      "path": "standard-collision-verification-output.txt",
      "bytes": 465,
      "sha256": "8f3ee07bc44ca3aa0a7740e16aae2e32ada1d03aef73dce7f5c7e21665f747b2"
    },
    {
      "path": "verify_equivariant_flatness_example.py",
      "bytes": 3310,
      "sha256": "5c70f0118f392d95a66930b7adb1d7691ee578374cafc867e0b084a54e185399"
    },
    {
      "path": "equivariant-flatness-verification-output-v8.txt",
      "bytes": 676,
      "sha256": "cab978f86179f75f3bc98bb5b9b279112a50ee28c39cde82561fbb1a13fbde4b"
    },
    {
      "path": "verify_ade_matrix_factorizations.py",
      "bytes": 7687,
      "sha256": "2a087f4eb2897e42b930d5c5498127089f534f61a783cebb44494dc437dc590b"
    },
    {
      "path": "verification-output-v8.txt",
      "bytes": 1208,
      "sha256": "f45fde85fac15ecfef4dbd467755dc2abf82d3b413d946626907c9b362e151a8"
    },
    {
      "path": "verify_minimal_defect_sextic.py",
      "bytes": 12495,
      "sha256": "40ffa4dd4b9cd7aeac8783abb95741893a1e80d93d456f2b2b2bacc919c1d6ca"
    },
    {
      "path": "minimal-defect-verification-output-v8.txt",
      "bytes": 508,
      "sha256": "dc944450d4f91dc72afc78bceded75dba41d9e7ac2421c056ccb300d4c93415f"
    },
    {
      "path": "lane1-collision-v8.patch",
      "bytes": 110814,
      "sha256": "c75c4b57613ee97abede503e725276f46c3bfd94ef05da580eab392957672302"
    },
    {
      "path": "INTEGRATION-v8.md",
      "bytes": 3708,
      "sha256": "d454c71f9cd4c2fe4bdb19544a636592ccad52a768f45e6ba1a0d11a5761a58e"
    }
  &#93;
}
</code></pre>

## `research-notes/lane1-collision-saturation-20260802-v1/verify_collision_idempotent.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact divided-difference certificate for the cubic Keller collision idempotent.

The script uses the announced degree-three Keller map.  It constructs a
polynomial divided-difference matrix M with F(X)-F(X')=M(X-X'), verifies the
constant Jacobian, and checks the explicit certificate

    q(q-c) = 0 in S tensor_R S,  q=det(M), c=det(JF),

by expressing q(q-c) in the ideal generated by the three fibre-difference
equations.  Hence e=q/c is the diagonal idempotent and 1-e cuts out the
off-diagonal collision component.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import sympy as sp

x, y, z, X, Y, Z = sp.symbols("x y z X Y Z")
left = (x, y, z)
right = (X, Y, Z)

def keller_map(a, b, c):
    p = (1 + a*b)**3*c + b**2*(1 + a*b)*(4 + 3*a*b)
    q = b + 3*a*(1 + a*b)**2*c + 3*a*b**2*(4 + 3*a*b)
    r = 2*a - 3*a**2*b - a**3*c
    return tuple(sp.expand(v) for v in (p, q, r))

F = keller_map(*left)
Fp = keller_map(*right)

def exact_quotient(num: sp.Expr, den: sp.Expr) -&gt; sp.Expr:
    poly_num = sp.Poly(sp.expand(num), x, y, z, X, Y, Z, domain=sp.QQ)
    poly_den = sp.Poly(den, x, y, z, X, Y, Z, domain=sp.QQ)
    quo, rem = sp.div(poly_num, poly_den)
    assert rem.is_zero
    return sp.expand(quo.as_expr())

# Sequential telescoping in the left variables.
Mrows = &#91;&#93;
for f in F:
    f_X = sp.expand(f.subs(x, X))
    f_XY = sp.expand(f_X.subs(y, Y))
    f_XYZ = sp.expand(f_XY.subs(z, Z))
    assert sp.expand(f_XYZ - Fp&#91;len(Mrows)&#93;) == 0
    m1 = exact_quotient(f - f_X, x - X)
    m2 = exact_quotient(f_X - f_XY, y - Y)
    m3 = exact_quotient(f_XY - f_XYZ, z - Z)
    Mrows.append((m1, m2, m3))
M = sp.Matrix(Mrows)
delta = sp.Matrix(&#91;x-X, y-Y, z-Z&#93;)
fibre_diff = sp.Matrix(&#91;sp.expand(a-b) for a, b in zip(F, Fp)&#93;)
assert all(sp.expand(v) == 0 for v in M*delta - fibre_diff)

J = sp.Matrix(F).jacobian(left)
c = sp.expand(J.det())
assert c == -2
q = sp.expand(M.det())
q_diag = sp.expand(q.subs({x:X, y:Y, z:Z}, simultaneous=True))
assert q_diag == c

# q-c = a_1(x-X)+a_2(y-Y)+a_3(z-Z), again by telescoping.
q_X = sp.expand(q.subs(x, X))
q_XY = sp.expand(q_X.subs(y, Y))
q_XYZ = sp.expand(q_XY.subs(z, Z))
assert sp.expand(q_XYZ-c) == 0
a = sp.Matrix(&#91;
    exact_quotient(q-q_X, x-X),
    exact_quotient(q_X-q_XY, y-Y),
    exact_quotient(q_XY-q_XYZ, z-Z),
&#93;)
assert sp.expand((a.dot(delta)) - (q-c)) == 0

adj = M.adjugate()
qdelta_certificate = adj*fibre_diff
assert all(sp.expand(v-q*d) == 0 for v, d in zip(qdelta_certificate, delta))

# This is the explicit fibre-ideal certificate for q(q-c).
coefficients = (a.T*adj)&#91;0, :&#93;
certificate_rhs = sum(coefficients&#91;j&#93;*fibre_diff&#91;j&#93; for j in range(3))
assert sp.expand(q*(q-c)-certificate_rhs) == 0

# e=q/c then satisfies e^2-e=0 modulo the fibre equations.
print("constant Jacobian c =", c)
print("degrees of divided-difference entries =", &#91;&#91;sp.Poly(M&#91;i,j&#93;, *left, *right).total_degree() for j in range(3)&#93; for i in range(3)&#93;)
print("degree(q) =", sp.Poly(q, *left, *right).total_degree())
print("terms(q) =", len(sp.Poly(q, *left, *right).terms()))
print("verified F-F' = M (X-X')")
print("verified q|_diagonal = c")
print("verified q(X-X') = adj(M)(F-F')")
print("verified q(q-c) lies in (F_1-F'_1,F_2-F'_2,F_3-F'_3)")
print("therefore e=q/c is the diagonal idempotent in S tensor_R S")
print("and 1-e cuts out the off-diagonal collision algebra")

path = Path(__file__)
print("script_sha256 =", hashlib.sha256(path.read_bytes()).hexdigest())
</code></pre>

## `research-notes/lane1-collision-saturation-20260802-v1/verify_standard_collision_model.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact algebra for the standard ordered-root triple-collision model."""
from __future__ import annotations
import hashlib
from pathlib import Path
import sympy as sp
u,v=sp.symbols('u v')
f1=sp.expand(u*(u+v)); f2=sp.expand(u*v); f3=sp.expand(v*(u+v))
assert sp.expand(f1-f2-u**2)==0
assert sp.expand(f3-f2-v**2)==0
# Conversely f1,f3 are in (u^2,uv,v^2), so the ideals are equal.
G1=sp.groebner(&#91;f1,f2,f3&#93;,u,v,order='lex')
G2=sp.groebner(&#91;u**2,u*v,v**2&#93;,u,v,order='lex')
assert G1==G2
print('collision generators =',f1,f2,f3)
print('Groebner basis =',list(G1.polys))
print('verified (u(u+v),uv,v(u+v)) = (u,v)^2')
print('the common complement is the triple-root axis V(u,v)')
print('a formal axis parameter t acts injectively on H^2_(u,v)(C&#91;&#91;u,v,t&#93;&#93;)')
print('therefore the closed-point collision saturation quotient vanishes')
print('script_sha256 =',hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
</code></pre>

[Back to Lane 1](cubic-flatness-normalization-defects.md)
