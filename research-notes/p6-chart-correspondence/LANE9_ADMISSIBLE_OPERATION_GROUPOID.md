# Lane 9 admissible operations: fixed charts, rechart arrows, and stabilizers

**Status:** structural clarification for the Lane 9 attachment problem.  This
note defines the smallest object that the public data force.  It does not
identify the missing complete-chain approximate-root generator table.

## 1. Three spaces that must not be identified

For a chart presentation `c`, let

```text
E_c  = coefficient/deformation space,
W_c  = determinant-equation density space,
D_c:E_c -> W_c,
A_c  = ambient filtered divergence-free Laurent derivations,
Theta_c:A_c -> E_c.
```

The public ambient calculation determines `A_c`, `Theta_c`, and transport on
finite Laurent windows.  A complete-chain presentation supplies additional
nonlinear equations or an ideal `I_c`.  Its fixed-presentation operation Lie
algebra is

```text
g_c^fix={X in A_c : X is tangent to I_c}.                    (1.1)
```

The infinitesimal stabilizer is

```text
s_c=ker(Theta_c restricted to g_c^fix).                      (1.2)
```

A chart change `a:c->d` is different data.  Its infinitesimal direction lies
in a rechart module `R_a`, together with transport maps

```text
T_a^E:E_c -> E_d,
T_a^W:W_c -> W_d,
T_a^A:A_c -> A_d,                                            (1.3)
```

satisfying the action and determinant squares whenever the transition is an
actual admissible chart arrow.  An element of `R_a` is not automatically an
element of `g_c^fix`, and it must not be quotiented as fixed-chart gauge merely
because it kills the ambient determinant equation.

## 2. The correct categorical object

The admissible operation datum is a filtered groupoid representation, or
equivalently an objectwise Lie-algebra system with arrow modules:

```text
c |-> g_c^fix,
a:c->d |-> (T_a^A,T_a^E,T_a^W,R_a).                         (2.1)
```

It must satisfy:

1. `D_d T_a^E=T_a^W D_c`;
2. `T_a^E Theta_c=Theta_d T_a^A` on transported fixed operations;
3. support, equation-density, adjoint, and forcing windows move together;
4. pairwise and triple compositions satisfy the chart cocycle;
5. transported operation spaces and rechart modules are closed under the
   relevant adjoint action and Lie brackets.

Thus the phrase `g_adm` is best read as the objectwise Lie part of (2.1), not
as one unrestricted Laurent Lie algebra containing every chart arrow.

## 3. What can be constructed from the public packet

Let

```text
g_c^known = Lie closure of the verified fixed-presentation generators,
g_c^supp  = all divergence-free Laurent derivations whose action stays in
            the declared finite support window.
```

For the true but unpublished complete-chain operation algebra one has the
rigorous sandwich

```text
g_c^known <= g_c^fix <= g_c^supp.                            (3.1)
```

The affine-polynomial source fields form a useful diagnostic subspace, but
are not known to be either a lower or upper bound for `g_c^fix`.

For the degree-21 lower face, the image ranks through layers one to four are

| operation model | image ranks |
|---|---:|
| determinant kernel / maximal support-admissible Laurent image | `(2,3,3,1)` |
| affine-polynomial diagnostic | `(2,3,2,1)` |
| recorded verified complete-chain input | `(1,1,2,0)` |

At layer four, therefore, the public fixed-presentation data leave exactly two
logical possibilities: the true image rank is zero or one.  The corrected
Kummer tangent does not decide between them, because its action has principal
parts outside the old layer-four window and belongs to a chart-arrow problem,
not directly to the old fixed-chart operation space.

The **minimal forced admissible system** is obtained by taking the intersection
of all systems (2.1) that

- contain the verified fixed-presentation generators;
- contain the verified ordinary monomial arrows;
- contain the corrected Kummer quotient arrow only when the chart category is
  enlarged accordingly;
- preserve the nonlinear support constraints;
- are closed under transport and brackets.

This intersection exists objectwise and gives a well-defined lower-bound
system.  Equality with the true complete-chain system is precisely the
missing generator/classification theorem.

## 4. The layer-eleven closure is an arrow-module condition

A general support-admissible layer-four source field is

```text
f4=c0+c1*z+z^2,
g4=2*c0*z^-1+3*c1+4*z.
```

The bare `k=4` wall begins at layer seven with

```text
f7=2*z^-3,
g7=z^-4.
```

Their bracket is the layer-eleven field

```text
f11=18*c0*z^-4+30*c1*z^-3+42*z^-2,
g11= 6*c0*z^-5+ 5*c1*z^-4.                  (4.1)
```

On the degree-21 leading face it produces unavoidable top terms

```text
336*lead(A0)*z^5,
504*lead(B0)*z^9.                             (4.2)
```

The stored layer-eleven old-chart window has no `P` coefficient and only `Q`
exponents `0,...,4`.  Hence the bracket cannot be represented by the old
fixed-chart module.  Closure requires a target-chart rechart coordinate at
layer eleven.  This is evidence for the arrow-module part of (2.1), not a
reason to enlarge old fixed-chart gauge indiscriminately.

## 5. Discrete deck stabilizer versus infinitesimal stabilizer

For the corrected quotient coordinates

```text
H=2*u^11*v^8,
Q=u^-12*v^-8,
```

one has

```text
K(H,Q)=K(u,v^8).
```

The cover has deck group scheme

```text
mu_8:(u,v)->(u,zeta*v).                                      (5.1)
```

This is the **discrete Kummer deck stabilizer**.  In characteristic zero,

```text
Lie(mu_8)=0.                                                  (5.2)
```

Therefore (5.1) does not supply a nonzero infinitesimal fixed-presentation
stabilizer in (1.2).  The original complete-chain infinitesimal stabilizer
remains unknown until its generator table and action map are published.

The candidate quotient should consequently be described by two separate
entries:

```text
discrete deck stabilizer: mu_8,
infinitesimal Kummer deck stabilizer: 0.                       (5.3)
```

## 6. Kummer arrows and cocycles

On the quotient, the corrected flow is the strict translation

```text
tau_s(H,Q)=(H,Q+16*s),
tau_s tau_t=tau_(s+t).                                       (6.1)
```

A lift to the cover requires

```text
R_s(Q)^8=(Q+16*s)/Q.                                         (6.2)
```

In the formal completion at `s=0`, the unique root with constant term one
makes the lift strict.  Over the generic algebraic field, root choices form a
`mu_8` torsor, and compositions are well defined only up to the corresponding
`mu_8` cocycle.  Accordingly:

- the quotient chart has a strict additive arrow group;
- the formal rooted chart has a strict identity-branch lift;
- the generic algebraic rooted chart is a Kummer groupoid with discrete
  `mu_8` isotropy.

This is the precise category in which support and residue transport must keep
all eight character modules.  Forgetting seven character blocks does not
produce an ordinary complete-chain overlap.

## 7. Consequences for the checklist

The public data support the following statements and no stronger ones:

1. the maximal support-admissible Laurent module is an exact **outer bound**;
2. the published complete-chain operations generate an exact **lower bound**;
3. ordinary affine polynomial fields are an incomparable diagnostic model;
4. the corrected layer-four Kummer direction is a rechart arrow, not an old
   fixed-chart gauge vector;
5. its discrete presentation/deck stabilizer is `mu_8`, with zero
   infinitesimal deck stabilizer;
6. the true nonlinear complete-chain stabilizer and operation algebra remain
   missing inputs;
7. any global atlas theorem must transport objectwise operation algebras,
   arrow modules, stabilizers, supports, adjoints, and forcing terms as one
   cocyclic system.

GPT-5.6 Pro assisted with the categorical formulation and its specialization
to the exact Lane 9 calculations.  This note is unrefereed and should be
checked before manuscript integration.
