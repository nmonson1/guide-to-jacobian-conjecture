# The quartic endgame beyond the marked local chart

Lane 4 · 2026-08-03

## Scope

Finish the degree-four Keller case by connecting the exact marked local
$F_4$ calculation to the historical $Q_4$–$F_4$ coefficient system and
then routing every complement in the quartic case tree.

## Setup and definitions

The quartic reduction has candidate minimum degrees $4,5,6,7$. Its terminal
leaves include curve-normalization, binary-ramification, target-span, and
marked Hilbert--Burch (HB) charts. In the regular marked $(3,4)$ HB chart,
$F_4$ denotes the highest-$z$, $D_6$-compatible weighted-inflection
normal form. The historical $Q_4$–$F_4$ block is a separate coefficient
presentation whose equivalence to that marked chart must be proved, not
assumed.

## Results to use

- The degree $4$–$7$ case tree and its listed terminal leaf certificates
  are exact under their recorded open conditions; terminal leaves alone do
  not prove that every parent is covered.
- In the regular marked HB chart, the generic and reduced highest-$z$ normals
  are exact. The rigid nonzero $z^2D_5$ coefficient is

  \[
  \Omega_5=-\lambda^3xu
  =-\frac{\lambda^3}{3}x(x^2+3xy+3y^2).
  \]

  On the reduced branches $\ell=x$ and $\ell=y$, it is respectively
  $-x^3/3$ and $2y^3/3$. The boundary values
  $\tau=0,1/3$ route to fixed-factor or high-ramification branches.
- This local theorem does not identify its chart scheme-theoretically with
  historical $Q_4$–$F_4$, reproduce the two $104/3$ $D_6$ anchors, or
  cover the historical denominator, rank-minor, resonance, resultant, and
  endpoint divisors.
- A complete $F_4$ input contract is specified but no complete instance is
  present. It requires $q_4$, $P,Q,R$, every $H_3,H_2,L$ coefficient,
  gauge removals, the total open product $S$, complement routes, determinant
  convention, and exact samples.
- One recovered historical local-chart instance is exact. It supplies $q_4$,
  $P,Q,R$, the encoded lower forms $A,B$, one normal solution, six vanishing
  $D_6$ remainders, and four pure-$z^2$ $D_5$ resultants. Their reported
  boundary factor has residual primitive gcd one, and the two samples at
  $\tau=3$ give $\Xi(1,1)=-5/54,5/54$. The complete contract rejects this
  instance because the unrestricted lower forms, gauges, complement routes,
  remaining cancellation variables, and characteristic-zero saturation
  certificate are absent.

## Example: the reduced marked branches

The values $-x^3/3$ and $2y^3/3$ are examples of the exact local theorem
after choosing $\ell=x$ or $\ell=y$. They are not a global $Q_4$–$F_4$
contract and do not close a missing complement elsewhere in the case tree.

The recovered historical chart is a second exact example. Its primitive
resultant gcd closes only the four displayed coefficients on the declared
open; it is not a full-system unit-ideal certificate.

## Live problem

Construct the first complete coefficient-level equivalence between the
historical $Q_4$–$F_4$ block and the regular marked HB chart, including
every inverted factor and an explicit route for each zero locus.

## Tasks

### L4-T1 — Instantiate the complete Q4–F4 contract

Inputs: the [contract specification](lane-4-source-packet.md),
the [recovered partial chart](lane-4-source-packet.md),
its [machine-readable instance](lane-4-source-packet.md),
the [marked-chart theorem](lane-4-source-packet.md),
its [exact replay](lane-4-source-packet.md),
and [low-degree TeX](../proof-sources/02-low-degree/main.md).

Deliverable: a schema-valid complete instance, forward and inverse coefficient
maps, reproduction of $\Omega_5$ and both $104/3$ anchors, the total open
factor $S$, and one named child for every irreducible factor of $S=0$.

Dependencies: a fixed determinant sign convention and the historical gauge
normalization.

Limits: the exact local theorem is already complete under its hypotheses; the
task is the missing presentation equivalence and coverage, not a rederivation
of that theorem.

### L4-T2 — Close the first unsupported case-tree edge

Inputs: the [quartic case tree](lane-4-source-packet.md)
and the instantiated contract from L4-T1.

Deliverable: a proof that the selected parent is the union of its recorded
children, or an explicit coefficient point in the omitted constructible locus.

Dependencies: L4-T1 when the edge enters $F_4$.

Limits: closing a terminal leaf does not establish the parent-to-child union.

Alternative connections: a determinantal-carrier comparison with Lane 7 is
welcome if it keeps all chart opens explicit.

## Limits

The present $F_4$ theorem is an exact local theorem under stated hypotheses.
The complete $Q_4$–$F_4$ contract and global case-tree coverage are missing.

## Direct sources

- [Retained complete-contract question RMU-2D4E0014](../working-mathematics/units/RMU-2D4E0014.md)
- [Retained partial-chart result RMU-2D4E0015](../working-mathematics/units/RMU-2D4E0015.md)
- [Quartic ramification TeX](../proof-sources/02-low-degree/appendices/quartic-frontier-and-ramification.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-4-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
