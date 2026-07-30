"""Independent exact Murnaghan--Nakayama checks for Program 6.

No data from the paper's certificate archive are used.  The script computes
weighted three-point Hurwitz numbers in S_n from the Frobenius character
formula, with characters evaluated by the Murnaghan--Nakayama rule.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial
from typing import Iterable, Tuple

Partition = Tuple[int, ...]


@lru_cache(None)
def partitions_with_bound(n: int, max_part: int) -> Tuple[Partition, ...]:
    if n == 0:
        return ((),)
    if max_part <= 0:
        return ()
    result = []
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions_with_bound(n - first, first):
            result.append((first,) + rest)
    return tuple(result)


def partitions(n: int) -> Tuple[Partition, ...]:
    return partitions_with_bound(n, n)


def contains(lam: Partition, mu: Partition) -> bool:
    rows = max(len(lam), len(mu))
    return all(
        (mu[i] if i < len(mu) else 0) <= (lam[i] if i < len(lam) else 0)
        for i in range(rows)
    )


def border_strip_height(lam: Partition, mu: Partition) -> int | None:
    cells = {
        (row, col)
        for row, length in enumerate(lam)
        for col in range(mu[row] if row < len(mu) else 0, length)
    }
    if not cells:
        return None

    seen = {next(iter(cells))}
    stack = list(seen)
    while stack:
        row, col = stack.pop()
        for neighbor in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ):
            if neighbor in cells and neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    if len(seen) != len(cells):
        return None

    for row, col in cells:
        if {
            (row, col),
            (row + 1, col),
            (row, col + 1),
            (row + 1, col + 1),
        } <= cells:
            return None

    return len({row for row, _ in cells}) - 1


@lru_cache(None)
def border_strip_removals(lam: Partition, size: int) -> Tuple[Tuple[Partition, int], ...]:
    remaining = sum(lam) - size
    if remaining < 0:
        return ()
    result = []
    for mu in partitions(remaining):
        if contains(lam, mu):
            height = border_strip_height(lam, mu)
            if height is not None:
                result.append((mu, height))
    return tuple(result)


@lru_cache(None)
def character(lam: Partition, cycle_type: Partition) -> int:
    if not cycle_type:
        return int(sum(lam) == 0)
    first = cycle_type[0]
    return sum(
        (-1) ** height * character(mu, cycle_type[1:])
        for mu, height in border_strip_removals(lam, first)
    )


def representation_dimension(lam: Partition) -> int:
    n = sum(lam)
    hook_product = 1
    for row, row_length in enumerate(lam):
        for col in range(row_length):
            below = sum(1 for lower_row in lam[row + 1 :] if lower_row > col)
            hook_product *= row_length - col + below
    return factorial(n) // hook_product


def centralizer_size(cycle_type: Iterable[int]) -> int:
    multiplicities = Counter(cycle_type)
    result = 1
    for length, multiplicity in multiplicities.items():
        result *= length**multiplicity * factorial(multiplicity)
    return result


def conjugacy_class_size(cycle_type: Partition) -> int:
    return factorial(sum(cycle_type)) // centralizer_size(cycle_type)


def weighted_hurwitz_number(
    class_0: Partition, class_1: Partition, class_infinity: Partition
) -> Fraction:
    n = sum(class_0)
    if sum(class_1) != n or sum(class_infinity) != n:
        raise ValueError("cycle types must have the same degree")

    character_sum = Fraction(0)
    for lam in partitions(n):
        character_sum += Fraction(
            character(lam, class_0)
            * character(lam, class_1)
            * character(lam, class_infinity),
            representation_dimension(lam),
        )

    prefactor = Fraction(
        conjugacy_class_size(class_0)
        * conjugacy_class_size(class_1)
        * conjugacy_class_size(class_infinity),
        factorial(n) ** 2,
    )
    return prefactor * character_sum


CASES = {
    "F2 degree 6": ((5, 1), (3, 3), (3, 1, 1, 1), Fraction(1)),
    "one-step degree 10": ((3, 3, 3, 1), (2, 2, 2, 2, 2), (8, 1, 1), Fraction(1)),
    "two-step degree 9": ((2, 2, 2, 2, 1), (3, 3, 3), (7, 1, 1), Fraction(1)),
    "F24 degree 9": ((4, 4, 1), (3, 3, 3), (5, 1, 1, 1, 1), Fraction(2)),
    "one-step degree 16": (
        (3, 3, 3, 3, 3, 1),
        (2, 2, 2, 2, 2, 2, 2, 2),
        (13, 1, 1, 1),
        Fraction(2),
    ),
    "degree 21 lower face": (
        (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1),
        (3, 3, 3, 3, 3, 3, 3),
        (17, 1, 1, 1, 1),
        Fraction(5),
    ),
    "ambient degree 30": (
        (5, 5, 5, 5, 5, 5),
        (3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
        (15,) + (1,) * 15,
        Fraction(133, 15),
    ),
}


def main() -> None:
    for name, (c0, c1, cinfinity, expected) in CASES.items():
        actual = weighted_hurwitz_number(c0, c1, cinfinity)
        assert actual == expected, (name, actual, expected)
        print(f"{name}: {actual}")


if __name__ == "__main__":
    main()
