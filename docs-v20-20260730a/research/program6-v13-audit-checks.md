---
title: "Program 6 v13 independent small checks"
description: "Independent exact checks for the low-dimensional calculations audited in the Program 6 v13 correction note."
---

<p class="claim-tag">Program 6 · independent audit checks</p>
# Program 6 v13 independent small checks

<p class="dek">Small exact calculations independently reimplemented during the v13 audit.</p>

!!! warning "Boundary"
    These scripts do not replay the 7,121-row Macaulay certificate, the 296-point toric archive, the branch reduction, or the upstream Newton exhaustiveness argument.

## Scripts

- [Hurwitz character counts](../assets/audit-repairs/program6-independent-audit-checks/hurwitz_counts.py)
- [Explicit symbolic identities, ranks, minors, and kernels](../assets/audit-repairs/program6-independent-audit-checks/explicit_symbolic_checks.py)
- [Quintic-field arithmetic](../assets/audit-repairs/program6-independent-audit-checks/quintic_arithmetic.py)
- [Python requirements](../assets/audit-repairs/program6-independent-audit-checks/requirements.txt)
- [Archive README](../assets/audit-repairs/program6-independent-audit-checks/README.md)

## Captured outputs

- [Hurwitz counts output](../assets/audit-repairs/program6-independent-audit-checks/hurwitz_counts.out)
- [Explicit symbolic checks output](../assets/audit-repairs/program6-independent-audit-checks/explicit_symbolic_checks.out)
- [Quintic arithmetic output](../assets/audit-repairs/program6-independent-audit-checks/quintic_arithmetic.out)

The computations independently reproduce:

- quotient Hurwitz counts \(1,1,1,2,2\);
- the degree-21 passport weighted count \(5\);
- the ambient degree-30 weighted count \(133/15\);
- all five displayed quotient face identities;
- the two explicit polynomial identities in Section 3;
- tangent ranks \(2,7,6,4,4\), the displayed maximal minors, and the scaling kernels;
- irreducibility, discriminant, and the five simple roots modulo 2053 of the displayed quintic coefficient field.

[Back to the correction note](program6-v13-corrigendum.md)
