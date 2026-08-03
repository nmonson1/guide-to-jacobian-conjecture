---
title: "Text proof source — 01-cubic-incidence/code/verify_ade_matrix_factorizations.py"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `c85a7462c73f776676897468ff3d421efb7d1b828fa84b1fd90c400cf225cb71` · 3,423 bytes

## Complete source

~~~python
#!/usr/bin/env python3
"""Exact symbolic replay for the transverse ADE templates in the Lane 1 repair.

Checks:
  * A_(3r-1) order-three matrix factorizations and ideal presentations;
  * the A_(r-1) degree-three cyclic-cover invariant equations;
  * the two E6 order-three ideals and their matrix factorizations;
  * the explicit D4 -> E6 cyclic-cover invariant equation.
"""

from __future__ import annotations

import argparse
import sys

import sympy as sp


def zero_matrix(matrix: sp.Matrix) -> bool:
    return matrix.applyfunc(sp.expand) == sp.zeros(*matrix.shape)


def verify_a_type(r: int) -> None:
    if r < 1:
        raise ValueError("r must be positive")

    u, v, z, U, V = sp.symbols("u v z U V")
    n = 3 * r
    f = u * v - z**n

    for j in (r, 2 * r):
        phi = sp.Matrix([[v, -(z**j)], [-(z ** (n - j)), u]])
        psi = sp.Matrix([[u, z**j], [z ** (n - j), v]])
        if not zero_matrix(phi * psi - f * sp.eye(2)):
            raise AssertionError(f"A-type left factorization failed: r={r}, j={j}")
        if not zero_matrix(psi * phi - f * sp.eye(2)):
            raise AssertionError(f"A-type right factorization failed: r={r}, j={j}")

        generators = sp.Matrix([[u, z**j]])
        if (generators * phi).applyfunc(sp.expand) != sp.Matrix([[f, 0]]):
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


def verify_e6() -> None:
    x, y, z, s, t = sp.symbols("x y z s t")
    ii = sp.I
    f = x**2 + y**3 + z**4
    a = x + ii * z**2
    b = x - ii * z**2

    for name, left, right in (("J+", a, b), ("J-", b, a)):
        phi = sp.Matrix([[right, -y], [y**2, left]])
        psi = sp.Matrix([[left, y], [-y**2, right]])
        if not zero_matrix(phi * psi - f * sp.eye(2)):
            raise AssertionError(f"E6 left factorization failed for {name}")
        if not zero_matrix(psi * phi - f * sp.eye(2)):
            raise AssertionError(f"E6 right factorization failed for {name}")
        generators = sp.Matrix([[left, y]])
        if (generators * phi).applyfunc(sp.expand) != sp.Matrix([[f, 0]]):
            raise AssertionError(f"E6 ideal presentation failed for {name}")

    cover = s**3 + t**3 - 2 * ii * z**2
    x_inv = (s**3 - t**3) / 2
    y_inv = s * t
    pullback = sp.expand(x_inv**2 + y_inv**3 + z**4)
    conjugate = s**3 + t**3 + 2 * ii * z**2
    if sp.expand(4 * pullback - cover * conjugate) != 0:
        raise AssertionError("D4 -> E6 invariant identity failed")

    print("PASS E6: both order-three ideals, matrix factorizations, and D4 cyclic cover")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=12)
    args = parser.parse_args(argv)
    if args.max_r < 1:
        parser.error("--max-r must be positive")

    for r in range(1, args.max_r + 1):
        verify_a_type(r)
    verify_e6()
    print("ALL LANE-1 TRANSVERSE ADE CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
~~~

[Back to the text-source index](../../index.md)
