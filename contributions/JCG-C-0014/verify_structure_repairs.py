#!/usr/bin/env python3
"""Validate finite arithmetic and fail-closed contracts for Lane 4 repairs.

This checker tests the combinatorial skeleton of the two structural proofs,
the regression example for the relative-closure shortcut, and the machine-
readable shape required before an F4 elimination can be accepted. It is not
a proof of the geometric inputs and does not solve Q4-F4.
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
STRUCTURAL_PATH = ROOT / "structural-repairs.tex"
CONTRACT_PATH = ROOT / "F4_INPUT_CONTRACT.md"
SCHEMA_PATH = ROOT / "f4-contract.schema.json"


def fail(message: str) -> None:
    raise AssertionError(message)


def validate_leading_image_degree_leaves() -> tuple[tuple[int, int, int], ...]:
    leaves = tuple(
        sorted(
            (e, k, g)
            for e in range(2, 5)
            for k in range(1, 5)
            for g in range(0, 5)
            if g + e * k == 4
        )
    )
    expected = ((2, 1, 2), (2, 2, 0), (3, 1, 1), (4, 1, 0))
    if leaves != expected:
        fail(f"unexpected leading-image leaves: {leaves}")
    return leaves


def validate_relative_closure_regression() -> None:
    X, t = sp.symbols("X t")
    polynomial = sp.Poly(X**2 - t, X, domain=sp.QQ.frac_field(t))
    if not polynomial.is_irreducible:
        fail("X^2-t unexpectedly reducible over Q(t)")

    text = STRUCTURAL_PATH.read_text(encoding="utf-8")
    for marker in (
        "relative algebraic closure does not prove properness",
        "[x^2:y^2:0]",
        "degree-two map",
        "choosing the normalization",
    ):
        if marker not in text:
            fail(f"relative-closure warning lacks marker: {marker}")


def validate_weighted_composite_table() -> tuple[tuple[int, int, int, int], ...]:
    rows: list[tuple[int, int, int, int]] = []
    for g in range(0, 4):
        n = 4 - g
        for e in range(2, n + 1):
            if n % e == 0:
                rows.append((g, n, e, n // e))
    result = tuple(sorted(rows))
    expected = (
        (0, 4, 2, 2),
        (0, 4, 4, 1),
        (1, 3, 3, 1),
        (2, 2, 2, 1),
    )
    if result != expected:
        fail(f"unexpected n=e*d table: {result}")
    return result


def validate_coprime_valuation_fourth_power() -> None:
    # Any finite support of nonnegative c_xi summing to 3 contains an odd term.
    for length in range(1, 6):
        for values in itertools.product(range(4), repeat=length):
            if sum(values) != 3:
                continue
            if not any(value % 2 == 1 for value in values):
                fail(f"sum-three valuation vector has no odd entry: {values}")

    # For odd c, the divisibility 4 | c*m forces 4 | m.
    for c in (1, 3):
        for m in range(1, 17):
            if (c * m) % 4 == 0 and m % 4 != 0:
                fail(f"odd valuation coefficient does not force 4|m: c={c}, m={m}")

    # If every component multiplicity is divisible by four and the total
    # weighted degree is four, the only possibility is one linear component
    # of multiplicity four.
    possibilities: set[tuple[tuple[int, int], ...]] = set()
    atoms = [(m, degree) for m in (4,) for degree in range(1, 5)]
    for length in range(1, 5):
        for choice in itertools.combinations_with_replacement(atoms, length):
            if sum(m * degree for m, degree in choice) == 4:
                possibilities.add(choice)
    if possibilities != {((4, 1),)}:
        fail(f"unexpected fourth-power fiber possibilities: {possibilities}")


def validate_fixed_component_nonconstant_ratio() -> None:
    bad = []
    for multiplicity in (1, 2, 3):
        if (3 * multiplicity) % 4 == 0:
            bad.append(multiplicity)
    if bad:
        fail(f"4*r=3*mu has a small fixed-factor solution: {bad}")


def validate_schema() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        fail("unexpected JSON Schema dialect")
    required = set(schema.get("required", []))
    expected = {
        "schema_version",
        "branch_id",
        "status",
        "provenance",
        "coefficient_field",
        "symbols",
        "leading_data",
        "lower_layers",
        "chart",
        "determinant_contract",
        "sample_reconstructions",
    }
    if required != expected:
        fail(f"F4 schema top-level contract changed: {required ^ expected}")
    if schema["properties"]["status"].get("const") != "complete":
        fail("F4 schema must reject incomplete instances")
    if schema["properties"]["branch_id"].get("const") != "Q4-F4":
        fail("F4 schema is attached to the wrong branch")
    return len(required)


def validate_f4_contract_boundary() -> None:
    text = CONTRACT_PATH.read_text(encoding="utf-8")
    required_markers = (
        "deliberately fail-closed",
        "do **not** publish",
        "does not manufacture an `F4` checker",
        "solve `D6` as a module",
        "test all `D5` cancellations in the cokernel",
        "saturation certificate",
        "A coefficient obstruction obtained after setting any allowed component",
        "Finite-field computations",
    )
    for marker in required_markers:
        if marker not in text:
            fail(f"F4 input contract lacks marker: {marker}")


def main() -> int:
    leaves = validate_leading_image_degree_leaves()
    validate_relative_closure_regression()
    composite_rows = validate_weighted_composite_table()
    validate_coprime_valuation_fourth_power()
    validate_fixed_component_nonconstant_ratio()
    schema_keys = validate_schema()
    validate_f4_contract_boundary()

    print("lane4 structural repair validation: PASS")
    print(
        "leading_image_degree_leaves="
        + ";".join(f"({e},{k},{g})" for e, k, g in leaves)
    )
    print("relative_closure_regression=degree-2 map detected")
    print(f"four_loci_composite_rows={len(composite_rows)}")
    print("coprime_valuation_fourth_power=PASS")
    print("fixed_component_nonconstant_ratio=excluded for multiplicities 1,2,3")
    print(f"f4_schema_required_blocks={schema_keys}")
    print("f4_contract_status=awaiting complete exact input instance")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"lane4 structural repair validation: FAIL: {exc}", file=sys.stderr)
        raise
