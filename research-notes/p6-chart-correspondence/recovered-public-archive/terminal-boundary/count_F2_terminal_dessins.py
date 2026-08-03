#!/usr/bin/env python3
"""Exact ambient and lattice-compatible dessin counts for the F2 corner.

The fractional uniformizing passport is
    (5^6), (3^10), (15,1^15), degree 30.
The polynomial lattice gap is five, so a genuine complete-chain face must be
a C5 pullback of the quotient passport
    (5,1), (3^2), (3,1^3), degree 6.

The script:
  * implements Murnaghan--Nakayama from scratch;
  * reproduces the known degree-21 count 5 as a regression check;
  * computes the F2 weighted Hurwitz number 133/15;
  * enumerates the C5 and C3 quotient dessins exactly;
  * concludes that the ambient degree-30 passport has 11 connected classes:
        8 with trivial automorphism group,
        2 with automorphism C3,
        1 with automorphism C5;
  * concludes that exactly the unique C5-symmetric class is compatible with
    the polynomial lattice gap;
  * verifies explicit quotient Belyi formulas for the symmetric classes.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial
import json
from pathlib import Path
from typing import Iterable

import sympy as sp


@lru_cache(None)
def partitions(n: int, max_part: int | None = None) -> tuple[tuple[int, ...], ...]:
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        return ((),)
    out: list[tuple[int, ...]] = []
    for first in range(max_part, 0, -1):
        for tail in partitions(n - first, min(first, n - first)):
            out.append((first,) + tail)
    return tuple(out)


@lru_cache(None)
def irrep_dimension(lam: tuple[int, ...]) -> int:
    n = sum(lam)
    hooks = 1
    for i, row in enumerate(lam):
        for j in range(row):
            below = sum(1 for later in lam[i + 1 :] if later > j)
            hooks *= row - j + below
    return factorial(n) // hooks


@lru_cache(None)
def removable_rim_hooks(lam: tuple[int, ...], k: int) -> tuple[tuple[tuple[int, ...], int], ...]:
    length = len(lam)
    target = sum(lam) - k
    if target < 0:
        return ()
    candidates: list[tuple[int, ...]] = []

    def rec(i: int, previous: int, remaining: int, rows: list[int]) -> None:
        if i == length:
            if remaining == 0:
                nu = tuple(rows)
                while nu and nu[-1] == 0:
                    nu = nu[:-1]
                candidates.append(nu)
            return
        max_value = min(previous, lam[i], remaining)
        for value in range(max_value, -1, -1):
            rest = remaining - value
            capacity = sum(min(value, lam[j]) for j in range(i + 1, length))
            if rest <= capacity:
                rec(i + 1, value, rest, rows + [value])

    rec(0, 10**9, target, [])
    result: list[tuple[tuple[int, ...], int]] = []
    for nu in candidates:
        extended = nu + (0,) * (length - len(nu))
        cells = {
            (i, j)
            for i, (outer, inner) in enumerate(zip(lam, extended))
            for j in range(inner + 1, outer + 1)
        }
        if len(cells) != k or not cells:
            continue
        stack = [next(iter(cells))]
        seen: set[tuple[int, int]] = set()
        while stack:
            cell = stack.pop()
            if cell in seen:
                continue
            seen.add(cell)
            i, j = cell
            for neighbour in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if neighbour in cells and neighbour not in seen:
                    stack.append(neighbour)
        if seen != cells:
            continue
        if any(
            (i + 1, j) in cells and (i, j + 1) in cells and (i + 1, j + 1) in cells
            for i, j in cells
        ):
            continue
        height = len({i for i, _ in cells})
        result.append((nu, -1 if height % 2 == 0 else 1))
    return tuple(result)


@lru_cache(None)
def character(lam: tuple[int, ...], mu: tuple[int, ...]) -> int:
    if not mu:
        return 1 if not lam else 0
    if sum(lam) != sum(mu):
        return 0
    if all(part == 1 for part in mu):
        return irrep_dimension(lam)
    return sum(
        sign * character(nu, mu[1:])
        for nu, sign in removable_rim_hooks(lam, mu[0])
    )


def z_class(mu: tuple[int, ...]) -> int:
    counts = Counter(mu)
    result = 1
    for cycle_length, multiplicity in counts.items():
        result *= cycle_length**multiplicity * factorial(multiplicity)
    return result


def weighted_hurwitz(n: int, mus: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]) -> tuple[Fraction, Fraction]:
    character_sum = Fraction(0)
    for lam in partitions(n):
        values = [character(lam, mu) for mu in mus]
        if all(values):
            character_sum += Fraction(values[0] * values[1] * values[2], irrep_dimension(lam))
    weighted = Fraction(factorial(n), z_class(mus[0]) * z_class(mus[1]) * z_class(mus[2])) * character_sum
    return character_sum, weighted


# Small exact permutation utilities for the quotient-dessin counts.
def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(p)
    for i, image in enumerate(p):
        result[image] = i
    return tuple(result)


def conjugate(h: tuple[int, ...], p: tuple[int, ...]) -> tuple[int, ...]:
    return compose(compose(h, p), inverse(h))


def cycle_type(p: tuple[int, ...]) -> tuple[int, ...]:
    seen = [False] * len(p)
    cycles: list[int] = []
    for i in range(len(p)):
        if seen[i]:
            continue
        j, size = i, 0
        while not seen[j]:
            seen[j] = True
            size += 1
            j = p[j]
        cycles.append(size)
    return tuple(sorted(cycles, reverse=True))


def permutation_from_cycles(cycles: list[tuple[int, ...]], n: int) -> tuple[int, ...]:
    p = list(range(n))
    for cycle in cycles:
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            p[source] = target
    return tuple(p)


def cycles_on_set(points: Iterable[int]) -> Iterable[tuple[int, ...]]:
    points = tuple(sorted(points))
    first = points[0]
    for tail in permutations(points[1:]):
        yield (first,) + tail


def class_5_1() -> Iterable[tuple[int, ...]]:
    for subset in combinations(range(6), 5):
        for cycle in cycles_on_set(subset):
            yield permutation_from_cycles([cycle], 6)


def class_5_5() -> Iterable[tuple[int, ...]]:
    for tail in combinations(range(1, 10), 4):
        first_block = (0,) + tail
        second_block = tuple(i for i in range(10) if i not in first_block)
        for c1 in cycles_on_set(first_block):
            for c2 in cycles_on_set(second_block):
                yield permutation_from_cycles([c1, c2], 10)


def centralizer_of_canonical_cycle(n: int, length: int) -> list[tuple[int, ...]]:
    sigma = permutation_from_cycles([tuple(range(length))], n)
    powers = [tuple(range(n))]
    for _ in range(1, length):
        powers.append(compose(sigma, powers[-1]))
    fixed = tuple(range(length, n))
    result: list[tuple[int, ...]] = []
    for power in powers:
        for fixed_permutation in permutations(fixed):
            h = list(power)
            for source, target in zip(fixed, fixed_permutation):
                h[source] = target
            result.append(tuple(h))
    return result


def quotient_orbit_count(
    n: int,
    sigma0_class: Iterable[tuple[int, ...]],
    sigma1: tuple[int, ...],
    sigma_infinity_type: tuple[int, ...],
) -> tuple[int, list[int]]:
    centralizer = centralizer_of_canonical_cycle(n, next(c for c in cycle_type(sigma1) if c > 1))
    sigma1_inverse = inverse(sigma1)
    selected: set[tuple[int, ...]] = set()
    for sigma0 in sigma0_class:
        sigma_infinity = compose(inverse(sigma0), sigma1_inverse)
        if cycle_type(sigma_infinity) == sigma_infinity_type:
            selected.add(sigma0)
    stabilizers: list[int] = []
    while selected:
        representative = next(iter(selected))
        orbit = {conjugate(h, representative) for h in centralizer}
        orbit &= selected
        stabilizers.append(len(centralizer) // len(orbit))
        selected -= orbit
    return len(stabilizers), stabilizers


def verify_symmetric_quotient_maps() -> dict[str, str]:
    x, alpha = sp.symbols("x alpha")

    # Unique degree-6 C5 quotient.
    phi5_num = x * (x - 1) ** 5
    phi5_den = (x**2 - sp.Rational(5, 3) * x + sp.Rational(5, 9)) ** 3
    diff5 = sp.expand(phi5_num - phi5_den)
    assert sp.degree(diff5, x) == 3
    assert sp.gcd(sp.Poly(phi5_den, x), sp.Poly(phi5_num, x)).degree() == 0
    assert sp.gcd(sp.Poly(diff5, x), sp.Poly(sp.diff(diff5, x), x)).degree() == 0

    # Two degree-10 C3 quotients, represented by the four roots of a reciprocal
    # quartic modulo alpha <-> alpha^{-1}.
    field_poly = alpha**4 - 5 * alpha**3 + 15 * alpha**2 - 5 * alpha + 1
    u = -sp.Rational(5, 3) * (alpha + 1)
    v = sp.Rational(5, 9) * (alpha**2 + 5 * alpha + 1)
    w = sp.Rational(5, 81) * (alpha + 1) * (alpha**2 - 16 * alpha + 1)
    R = x**3 + u * x**2 + v * x + w
    phi3_num = (x - 1) ** 5 * (x - alpha) ** 5
    phi3_den = x * R**3

    def reduce_alpha(expr: sp.Expr) -> sp.Expr:
        result = 0
        polynomial = sp.Poly(sp.expand(expr), x)
        for exponent in range(polynomial.degree() + 1):
            coefficient = polynomial.coeff_monomial(x**exponent)
            reduced = sp.rem(sp.Poly(coefficient, alpha, domain=sp.QQ), sp.Poly(field_poly, alpha, domain=sp.QQ)).as_expr()
            result += reduced * x**exponent
        return sp.expand(result)

    diff3 = reduce_alpha(phi3_num - phi3_den)
    assert sp.degree(diff3, x) == 5
    checks = {
        "R_squarefree": sp.resultant(R, sp.diff(R, x), x),
        "R_avoids_zero": sp.resultant(R, x, x),
        "R_avoids_one": sp.resultant(R, x - 1, x),
        "R_avoids_alpha": sp.resultant(R, x - alpha, x),
        "third_fiber_squarefree": sp.resultant(diff3, sp.diff(diff3, x), x),
        "third_fiber_disjoint_from_zero_fiber": sp.resultant(diff3, phi3_num, x),
    }
    for value in checks.values():
        numerator = sp.together(value).as_numer_denom()[0]
        assert sp.gcd(sp.Poly(numerator, alpha, domain=sp.QQ), sp.Poly(field_poly, alpha, domain=sp.QQ)).degree() == 0
    assert sp.factor(field_poly) == field_poly
    assert sp.discriminant(field_poly, alpha) != 0

    return {
        "C5_quotient": "x(x-1)^5/(x^2-(5/3)x+5/9)^3",
        "C3_parameter_polynomial": "alpha^4-5alpha^3+15alpha^2-5alpha+1",
        "C3_quotient": "(x-1)^5(x-alpha)^5/[x(x^3+u x^2+v x+w)^3]",
        "u": "-(5/3)(alpha+1)",
        "v": "(5/9)(alpha^2+5alpha+1)",
        "w": "(5/81)(alpha+1)(alpha^2-16alpha+1)",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    # Regression check: the degree-21 passport from the earlier calculation.
    s21, h21 = weighted_hurwitz(
        21,
        ((2,) * 10 + (1,), (3,) * 7, (17,) + (1,) * 4),
    )
    assert s21 == Fraction(31104, 19019) and h21 == 5

    s30, h30 = weighted_hurwitz(
        30,
        ((5,) * 6, (3,) * 10, (15,) + (1,) * 15),
    )
    assert s30 == Fraction(20503125, 12971816)
    assert h30 == Fraction(133, 15)

    c5_classes, c5_stabilizers = quotient_orbit_count(
        6,
        class_5_1(),
        permutation_from_cycles([(0, 1, 2)], 6),
        (3, 3),
    )
    c3_classes, c3_stabilizers = quotient_orbit_count(
        10,
        class_5_5(),
        permutation_from_cycles([(0, 1, 2, 3, 4)], 10),
        (3, 3, 3, 1),
    )
    assert (c5_classes, c5_stabilizers) == (1, [1])
    assert (c3_classes, c3_stabilizers) == (2, [1, 1])

    # Every nontrivial automorphism group is C3 or C5.  Quotient enumeration
    # gives n3=2 and n5=1.  The weighted count determines n1.
    n3, n5 = 2, 1
    n1 = h30 - Fraction(n3, 3) - Fraction(n5, 5)
    assert n1.denominator == 1 and n1 == 8
    total = int(n1) + n3 + n5
    assert total == 11

    formulas = verify_symmetric_quotient_maps()
    payload = {
        "degree21_regression": {"character_sum": str(s21), "weighted_count": str(h21)},
        "F2_uniformizing_degree30": {
            "passport": ["(5^6)", "(3^10)", "(15,1^15)"],
            "character_sum": str(s30),
            "weighted_hurwitz_count": str(h30),
            "classes_with_trivial_automorphism": int(n1),
            "classes_with_C3_automorphism": n3,
            "classes_with_C5_automorphism": n5,
            "total_connected_dessin_classes": total,
        },
        "F2_lattice_quotient_degree6": {
            "passport": ["(5,1)", "(3^2)", "(3,1^3)"],
            "weighted_hurwitz_count": "1",
            "connected_classes": c5_classes,
            "automorphism_stabilizers": c5_stabilizers,
            "lattice_compatible_ambient_classes": 1,
        },
        "symmetric_quotient_formulas": formulas,
    }
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    print("the 11 degree-30 classes are ambient; the lattice gap selects the unique C5 pullback")
    print("all character, quotient-orbit, and symmetric-map checks passed")


if __name__ == "__main__":
    main()
