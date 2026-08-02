# Lane 4 global quartic case tree — structural audit draft

## Status of this draft

This document supplies the global *mathematical routing* from the leading
target span to the named terminal strata. It incorporates the repaired
leading-image factorization, the repaired four-locus proof, the `R=0`
argument, the homogeneous centralizer lemma, all seven conic exclusions, and
the proper rational-cubic exclusion.

It does **not** yet certify the proof-to-code correspondence inside every
computer-assisted terminal leaf.  The repeated-root part of ramification
four is supplied here by a new projective proof and exact checker.  The main
remaining concentration is the degree-three ramification family, where the
public v5 programs close every named chart but a complete independent
proof-to-code crosswalk is still absent.

## Priority convention

The loci overlap. To obtain a genuine tree rather than a cover, assign a map
to the first applicable branch in this order:

1. zero cubic normal layer `R=0`;
2. binary leading data `P,Q,R in k[x,y]`;
3. genuinely nonbinary quadratic-source data;
4. primitive coprime fourth-power data;
5. genuinely nonbinary fixed-component data.

Inside the binary branch, assign fixed factors before fourth-power and
ramification branches, and assign zero minors before defining the common
ramification degree. This convention is ownership only; it does not assert
that the underlying geometric loci are disjoint.

## Complete structural tree

```text
quartic Keller map F = LX + H2 + H3 + H4
|
+-- rho4 = 1
|   `-- rank-one theorem -> automorphism
|
+-- rho4 = 3
|   |
|   +-- leading image a conic
|   |   `-- seven parabolic factor orbits -> all excluded
|   |
|   +-- leading image a proper rational cubic
|   |   `-- cusp/node, transverse/marked factors -> all excluded
|   |
|   `-- leading image a proper rational quartic
|       `-- frontier types (3,(1,2)) and (2,(2,2)) -> excluded
|
`-- rho4 = 2
    |
    +-- normalize H4=(P,Q,0), P,Q independent quartics
    |   and put R=(H3)3
    |
    +-- R=0
    |   `-- quadratic-coordinate + plane reduction -> automorphism
    |
    `-- R != 0 and Jac(P,Q,R)=0
        |
        +-- P,Q,R binary in two source forms
        |   |
        |   +-- G=gcd(P,Q) nonconstant
        |   |   +-- deg G=3: squarefree / 2+1 / triple line
        |   |   +-- deg G=2: quadratic fixed-factor divisor tree
        |   |   `-- deg G=1: two residual-cubic orbits + exceptional divisors
        |   |
        |   `-- gcd(P,Q)=1
        |       |
        |       +-- U,V,or W zero -> zero-minor theorem
        |       |
        |       +-- pencil contains a fourth power
        |       |   `-- binary / quadratic-source / aligned exit
        |       |
        |       `-- U,V,W nonzero; r=deg gcd(U,V,W)
        |           +-- r=0 -> regular theorem
        |           +-- r=1 -> simple-ramification theorem
        |           +-- r=2 -> double-ramification theorem
        |           +-- r=3
        |           |   +-- HB type (2,5) -> fourth-power boundary
        |           |   `-- HB type (3,4) -> v5 degree-three chart family
        |           +-- r=4
        |           |   +-- residual u,v dependent -> algebraic exclusion
        |           |   +-- residual u,v independent; w square -> gcd contradiction
        |           |   `-- residual u,v independent; w reduced
        |           |       +-- common quartic Gamma squarefree -> normal kernel zero
        |           |       `-- Gamma repeated-root incidence
        |           |           +-- nonprimitive component -> gcd(P,Q)>1 exit
        |           |           `-- rational-conic component + endpoints + 2+2 divisor
        |           `-- r=5 -> aligned cube/fourth-power exclusion
        |
        +-- genuinely nonbinary composite intermediate field
        |   `-- only n=4=(e,d)=(2,2)
        |       +-- binary degeneration -> binary branch
        |       +-- fixed-component degeneration -> fixed branch
        |       `-- no-fixed genuinely nonbinary locus -> nine-chart exclusion
        |
        +-- composition-primitive, gcd(P,Q)=1, nonbinary
        |   `-- valuation forces a fourth-power pencil member
        |       `-- binary / quadratic-source / aligned exit
        |
        `-- composition-primitive, gcd(P,Q)=G nonconstant, nonbinary
            +-- deg G=2 -> corrected fixed-component valuation
            `-- deg G=1 -> aligned / binary / residual-pole branch
                `-- homogeneous cubic centralizer + determinant equation -> contradiction
```

## Why the span-two split is exhaustive

Write `P=GA`, `Q=GB`, `gcd(A,B)=1`, and `n=deg A=deg B`. The weighted
one-variable field construction gives
\[
n=ed,
\]
where `e` is the composition degree of the reduced pencil through the
intermediate rational field.

After the binary branch has been removed, the composite possibilities are
\[
\begin{array}{c|c|c}
\deg G&n&(e,d)\\ \hline
0&4&(4,1),(2,2)\\
1&3&(3,1)\\
2&2&(2,1).
\end{array}
\]
Every `d=1` case is binary after valuation along the fixed components; the
only genuinely nonbinary composite case is `(e,d)=(2,2)`.

In the primitive nonbinary case, `G=1` gives the fourth-power fiber by the
nonnegative coprime valuation sum. If `G != 1`, the generic-divisor valuation
forces every nonbinary component of `G` onto a special fiber, giving the
fixed-component branch. Thus no sixth structural locus remains.

## Leaf ownership and evidence status

| ID | Leaf | Owner | Current status after this continuation |
| --- | --- | --- | --- |
| S1 | `rho4=1` | rank-one theorem | reader proof |
| S2 | conic image, seven factor orbits | original four-orbit theorem + conic completion packet | reader proof plus exact scripts; second CAS still desirable |
| S3 | proper rational cubic | rational-cubic continuation packet | reader proof plus exact scripts; second CAS still desirable |
| S4 | proper rational quartic | frontier appendix | reader proof, subject to its preclassification |
| B0 | `R=0` | repaired quadratic-coordinate route | reader proof, same plane-theorem citation dependency |
| B1 | genuinely nonbinary `(2,2)` | nine normalized charts | chart-complete claim; proof-to-code audit pending |
| B2 | binary fixed factors `deg G=1,2,3` | fixed-factor packets | exact chart replays; proof-to-code audit pending |
| B3 | coprime binary `r<=2` | ramification filtration | reader/computer-assisted proofs as stated |
| B4 | coprime binary `r=3` | v5 chart family | all named charts replay publicly; this packet independently reconstructs the full `tau=-1` divisor; the remaining proof-code crosswalk and second-lineage review are pending |
| B5 | coprime binary `r=4` | high-ramification theorem in this packet | candidate reader proof plus exact projective-incidence checker; no imported complete-specialization assertion remains |
| B6 | coprime binary `r=5` | high-ramification theorem | reader algebraic proof |
| B7 | fourth-power member | edge proposition | routing proof; overlap exits must be preserved |
| B8 | nonbinary fixed components | corrected valuation + centralizer repair | reader proof after inserting homogeneous cubic centralizer lemma |
| B9 | zero minor | edge proposition + repaired `R=0` route | reader proof, same plane-theorem dependency |

## Remaining theorem-level gates

The structural tree itself now has an owner for every branch. The remaining
work before asserting `D_min >= 5` is concentrated in evidence attachment:

1. map every `r=3` Hilbert--Burch chart and every exceptional divisor to a
   source theorem and a specific v5 program group;
2. independently reconstruct the remaining exceptional `r=3` divisors
   (`tau^2+1=0`, `c=0`, dependent syzygies, and the quadratic-exceptional
   pencil), or audit the existing implementations line by line;
3. complete the proof-to-code crosswalk for the quadratic-source and fixed-
   factor terminal packets;
4. verify the exact per-coordinate low-degree plane theorem formulation used
   by the triangular reductions; and
5. obtain specialist human review of the new structural and chart proofs.

Items 1--3 are the remaining publication-level attachment gates. Item 4 is a
citation/hypothesis gate. Item 5 is an evidence-quality gate.
