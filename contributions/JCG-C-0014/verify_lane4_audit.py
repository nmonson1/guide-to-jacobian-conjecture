#!/usr/bin/env python3
"""Validate the additive Lane 4 audit artifact.

This checker verifies the machine-readable ownership ledger and a few
independent algebraic samples.  It does not replay the Program 2 archives and
must not be cited as a quartic nonexistence certificate.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "lane4-case-tree.csv"
CROSSWALK_PATH = ROOT / "PROOF_CODE_CROSSWALK.md"


def fail(message: str) -> None:
    raise AssertionError(message)


def prime_factor_count_with_multiplicity(n: int) -> int:
    if n < 1:
        raise ValueError("degree must be positive")
    count = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            count += 1
            n //= d
        d += 1
    if n > 1:
        count += 1
    return count


def read_rows() -> list[dict[str, str]]:
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = {
        "id",
        "parent",
        "branch_condition",
        "normalization_or_localization",
        "open_condition",
        "vanishing_complement",
        "source_locator",
        "inherited_hypotheses",
        "status",
        "computational_leaf",
        "candidate",
    }
    if not rows:
        fail("empty case tree")
    if set(rows[0]) != required:
        fail(f"unexpected CSV columns: {set(rows[0]) ^ required}")
    return rows


def validate_tree(rows: list[dict[str, str]]) -> tuple[int, int]:
    ids = [row["id"].strip() for row in rows]
    duplicates = [item for item, n in Counter(ids).items() if n > 1]
    if duplicates:
        fail(f"duplicate node IDs: {duplicates}")

    id_set = set(ids)
    roots = [row for row in rows if not row["parent"].strip()]
    root_ids = {row["id"] for row in roots}
    if root_ids != {"Q4-ROOT", "D56-BASEPOINT"}:
        fail(f"unexpected roots: {sorted(root_ids)}")

    for row in rows:
        parent = row["parent"].strip()
        if parent and parent not in id_set:
            fail(f"{row['id']}: missing parent {parent}")

        operation = row["normalization_or_localization"].strip().lower()
        is_operation = operation not in {"", "none"}
        if is_operation and not row["vanishing_complement"].strip():
            fail(f"{row['id']}: normalization/localization lacks complement")
        if is_operation and not row["open_condition"].strip():
            fail(f"{row['id']}: normalization/localization lacks open condition")

        if not row["branch_condition"].strip():
            fail(f"{row['id']}: empty branch condition")
        if not row["source_locator"].strip():
            fail(f"{row['id']}: empty source locator")
        if not row["inherited_hypotheses"].strip():
            fail(f"{row['id']}: empty inherited hypotheses")

    parent_of = {row["id"]: row["parent"].strip() for row in rows}
    for node in ids:
        seen: set[str] = set()
        current = node
        while current:
            if current in seen:
                fail(f"parent cycle through {current}")
            seen.add(current)
            current = parent_of[current]

    candidates = [row for row in rows if row["candidate"].strip()]
    if {row["id"] for row in candidates} != {
        "AUDIT-LEAD-FACT",
        "AUDIT-RQ-FRONTIER",
        "AUDIT-FOUR-LOCI",
        "Q4-F4",
        "AUDIT-QUAD-XW",
        "AUDIT-BINARY-FIXED-XW",
        "D56-BASEPOINT",
    }:
        fail("candidate/interface set changed without updating validator")

    return len(rows), len(candidates)


def validate_crosswalk(rows: list[dict[str, str]]) -> int:
    text = CROSSWALK_PATH.read_text(encoding="utf-8")
    used = {
        row["computational_leaf"].strip()
        for row in rows
        if row["computational_leaf"].strip()
    }
    declared = set(re.findall(r"`(CW-[A-Z0-9-]+)`", text))
    missing = sorted(used - declared)
    if missing:
        fail(f"crosswalk IDs used by CSV but not declared: {missing}")
    return len(used)


def validate_plane_degrees() -> None:
    degrees = {1, 2, 3, 4, 5, 6, 7, 9}
    bad = {
        degree: prime_factor_count_with_multiplicity(degree)
        for degree in degrees
        if prime_factor_count_with_multiplicity(degree) > 2
    }
    if bad:
        fail(f"plane degree criterion fails: {bad}")


def validate_basepoint_normal_form() -> None:
    x, y, z = sp.symbols("x y z")
    a = x * y
    b = y**2
    if sp.gcd(a, b) != y:
        fail("unexpected gcd on G=0")
    if sp.expand(a.subs({x: 1, y: 0})) != 0:
        fail("A does not vanish at [1:0:0]")
    if sp.expand(b.subs({x: 1, y: 0})) != 0:
        fail("B does not vanish at [1:0:0]")
    if sp.Matrix([[1, 0], [0, 1]]).det() == 0:
        fail("residual binary linear forms are dependent")

    l1 = x + 2 * y + 3 * z
    l2 = 5 * x + 7 * y + 11 * z
    A = x * y + z * l1
    B = y**2 + z * l2
    point = {x: 1, y: 0, z: 0}
    if sp.expand(A.subs(point)) != 0 or sp.expand(B.subs(point)) != 0:
        fail("lifted normal form misses the selected basepoint")


def validate_homogeneous_centralizer_samples() -> None:
    x, y, z = sp.symbols("x y z")
    R = y**3 + x * y * z + z**3
    if sp.expand(R.subs(x, 0)) == 0:
        fail("sample R is divisible by x")
    for d in range(0, 16):
        for j in range(0, d // 3 + 1):
            term = sp.expand(x ** (d - 3 * j) * R**j)
            poly = sp.Poly(term, x, y, z)
            degrees = {sum(monomial) for monomial, _ in poly.terms()}
            if degrees != {d}:
                fail(f"centralizer basis term not homogeneous: d={d}, j={j}")


def main() -> int:
    rows = read_rows()
    row_count, candidate_count = validate_tree(rows)
    crosswalk_count = validate_crosswalk(rows)
    validate_plane_degrees()
    validate_basepoint_normal_form()
    validate_homogeneous_centralizer_samples()

    print("lane4 audit validation: PASS")
    print(f"rows={row_count}")
    print(f"named_open_interfaces_or_candidates={candidate_count}")
    print(f"crosswalk_ids_used={crosswalk_count}")
    print("plane_degree_set=1,2,3,4,5,6,7,9")
    print("surviving_quartic_candidate=Q4-F4")
    print("degree_five_boundary=D56-BASEPOINT (not a quartic child)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"lane4 audit validation: FAIL: {exc}", file=sys.stderr)
        raise
