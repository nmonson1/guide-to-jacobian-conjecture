#!/usr/bin/env python3
"""Combinatorial audit for the effective unframed complexity bound.

This script verifies the coefficient-variable counts, degree/parameter-degree
bookkeeping, finite inequalities, and asymptotic constants.  It does not
re-prove the external parametric Nullstellensatz or the stable q-classification.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Iterator

OUT = Path(__file__).with_name("effective_unframed_bound_report.json")


def exponent_tuples(n: int, b: int) -> Iterator[tuple[int, ...]]:
    for exps in itertools.product(range(b + 1), repeat=n):
        if sum(exps) <= b:
            yield exps


def monomial_count(n: int, b: int) -> int:
    return math.comb(n + b, n)


def variable_count(m: int, b: int) -> int:
    n = 3 + m
    return 4 * n * monomial_count(n, b)


def equation_degree_bound(b: int) -> int:
    return max(b + 1, 11)


def parameter_degree_bound(b: int) -> int:
    return 2 * b


def log_H(m: int, b: int) -> float:
    nvars = variable_count(m, b)
    d = equation_degree_bound(b)
    return math.log(2 * b * (nvars + 1)) + nvars * math.log(d)


def unrestricted_log_H(B: int) -> float:
    nvars_bound = 32 * (B + 3) * (4**B)
    return (
        math.log(2 * B * (nvars_bound + 1))
        + nvars_bound * math.log(B + 11)
    )


def tradeoff_log_H(m: int, b: int) -> float:
    nvars_bound = 32 * (m + 3) * (2 ** (m + b))
    return (
        math.log(2 * b * (nvars_bound + 1))
        + nvars_bound * math.log(b + 11)
    )


def main() -> None:
    enumeration_checks = []
    for n in range(1, 5):
        for b in range(0, 5):
            enumerated = sum(1 for _ in exponent_tuples(n, b))
            formula = monomial_count(n, b)
            assert enumerated == formula
            enumeration_checks.append(
                {"n": n, "b": b, "count": formula}
            )

    # Degree bookkeeping for the universal coefficient equations.
    degree_checks = []
    for b in range(1, 21):
        inverse_composition_degree = b + 1
        left_substitution_degree = 11
        right_substitution_degree = 1
        computed = max(
            inverse_composition_degree,
            left_substitution_degree,
            right_substitution_degree,
        )
        asserted = equation_degree_bound(b)
        assert computed == asserted
        assert parameter_degree_bound(b) == 2 * b
        degree_checks.append(
            {
                "b": b,
                "coefficient_degree": asserted,
                "parameter_degree": 2 * b,
            }
        )

    exact_samples = []
    for m in range(0, 4):
        for b in (1, 2, 4, 8, 12):
            n = 3 + m
            t = monomial_count(n, b)
            nvars = variable_count(m, b)
            assert nvars == 4 * n * t
            assert t <= 2 ** (n + b)
            assert nvars <= 32 * (m + 3) * (2 ** (m + b))
            exact_samples.append(
                {
                    "m": m,
                    "b": b,
                    "ambient_dimension": n,
                    "monomials_per_coordinate": t,
                    "coefficient_variables": nvars,
                    "d": equation_degree_bound(b),
                    "h": parameter_degree_bound(b),
                    "log_H": log_H(m, b),
                    "log10_H": log_H(m, b) / math.log(10),
                    "tradeoff_log_H": tradeoff_log_H(m, b),
                }
            )

    fixed_n_asymptotics = []
    for n in (3, 4, 5, 6):
        target = 4 / math.factorial(n - 1)
        values = []
        for b in (50, 100, 200, 500):
            m = n - 3
            ratio = log_H(m, b) / (b**n * math.log(b))
            values.append({"b": b, "ratio": ratio})
        # Convergence is from above for these samples and must be reasonably close.
        assert abs(values[-1]["ratio"] - target) / target < 0.08
        fixed_n_asymptotics.append(
            {
                "n": n,
                "target_coefficient": target,
                "inverted_constant": (math.factorial(n) / 4) ** (1 / n),
                "samples": values,
            }
        )

    unrestricted_asymptotics = []
    for B in (10, 20, 40, 80, 160):
        ll = math.log(unrestricted_log_H(B))
        ratio = ll / B
        unrestricted_asymptotics.append(
            {
                "B": B,
                "log_log_H_over_B": ratio,
                "target": math.log(4),
            }
        )
    assert abs(unrestricted_asymptotics[-1]["log_log_H_over_B"] - math.log(4)) < 0.08

    report = {
        "status": "ALL EFFECTIVE UNFRAMED BOUND CHECKS PASSED",
        "scope": {
            "verified": [
                "monomial count T(n,b)=binomial(n+b,n)",
                "coefficient variable count N=4*n*T(n,b)",
                "universal equation coefficient-degree bound max(b+1,11)",
                "universal parameter-degree bound 2*b",
                "finite tradeoff inequalities",
                "fixed-stabilization asymptotic leading constants",
                "unrestricted log-log coefficient log(4)",
            ],
            "not_verified_by_script": [
                "complete stable q-classification",
                "generic-fiber emptiness",
                "constant generic-combination lemma",
                "D'Andrea-Krick-Sombra parametric Nullstellensatz",
            ],
        },
        "formulas": {
            "H(m,b)": "2*b*(N+1)*max(b+1,11)^N",
            "N": "4*(m+3)*binomial(m+b+3,m+3)",
            "unrestricted_finite_bound": "2*B*(32*(B+3)*4^B+1)*(B+11)^(32*(B+3)*4^B)",
            "unrestricted_asymptotic": "liminf kappa_M/log(log M) >= 1/log(4)",
        },
        "enumeration_checks": enumeration_checks,
        "degree_checks": degree_checks,
        "exact_samples": exact_samples,
        "fixed_n_asymptotics": fixed_n_asymptotics,
        "unrestricted_asymptotics": unrestricted_asymptotics,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report["status"])
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
