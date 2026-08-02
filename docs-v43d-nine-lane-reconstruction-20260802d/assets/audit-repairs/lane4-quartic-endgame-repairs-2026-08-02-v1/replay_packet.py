#!/usr/bin/env python3
"""Replay the exact Lane 4 checks shipped in this packet.

The default suite is deliberately compact.  ``--full`` adds every named
x^2/xy conic branch and the broader rational-cubic calculations.  The slow
nodal full-matrix calculation is available through ``--include-slow``; its
constant maximal minor is already checked by the default suite.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Check:
    name: str
    cwd: Path
    argv: tuple[str, ...]
    needles: tuple[str, ...]
    timeout: int = 300


def py(path: Path, *args: str) -> tuple[str, ...]:
    return (sys.executable, str(path), *args)


CONIC = ROOT / "checks" / "conic"
RC = ROOT / "checks" / "rational-cubic"

COMPACT: list[Check] = [
    Check(
        "z2-conic",
        ROOT,
        py(ROOT / "checks" / "z2_conic_independent_check.py"),
        ("PASS: the z^2 conic orbit forces det(L)=0",),
        180,
    ),
    Check(
        "conic-terminal-identities",
        CONIC,
        py(CONIC / "verify_terminal_identities.py"),
        ("PASS: all quoted terminal factor identities hold over Q.",),
        120,
    ),
    Check(
        "high-ramification-r4-r5",
        ROOT,
        py(ROOT / "checks" / "high-ramification" / "verify_r4_high_ramification.py"),
        ("PASS: every exact algebraic gate", "PASS: the r=5 branch"),
        240,
    ),
    Check(
        "tau-minus-one",
        ROOT,
        py(ROOT / "checks" / "tau-minus-one" / "verify_tau_minus_one.py"),
        ("PASS: every primitive tau=-1 nonzero-normal chart is excluded exactly.",),
        240,
    ),
    Check(
        "rational-cubic-transverse-cusp",
        RC,
        py(RC / "transverse_after_translation.py", "cusp"),
        ("detL reduced 0",),
        120,
    ),
    Check(
        "rational-cubic-nodal-constant-minor",
        RC,
        py(RC / "node_h2z_pivotminor.py"),
        ("det 12582912",),
        240,
    ),
]

CONIC_CASES = [
    "x2-scalar",
    "x2-semisimple",
    "x2-nilpotent-1",
    "x2-nilpotent-2",
    "x2-second-normal-p",
    "x2-second-normal-q",
    "xy-scalar",
    "xy-anti-scalar",
    "xy-second-normal-axis",
    "xy-second-normal-open",
]

FULL_EXTRA: list[Check] = [
    Check(
        "rational-cubic-transverse-node",
        RC,
        py(RC / "transverse_after_translation.py", "node"),
        ("detL reduced 0",),
        120,
    ),
    Check(
        "rational-cubic-cusp-fiber-terminal",
        RC,
        py(RC / "cusp_fiber_q_branch.py"),
        ("(1, 3, 1) -6", "solutions 0"),
        180,
    ),
    Check(
        "rational-cubic-cusp-generic-terminal",
        RC,
        py(RC / "cusp_generic_q_d5.py"),
        ("(1, 3, 1) -6", "(0, 4, 1) 6"),
        180,
    ),
    Check(
        "rational-cubic-nodal-marked-family",
        RC,
        py(RC / "node_marked_lambda_d7.py"),
        ("PURE 0", "PURE 3", "PURE 5"),
        300,
    ),
    *[
        Check(
            f"conic-{case}",
            CONIC,
            py(CONIC / "run_replays.py", case),
            (f"PASS {case}",),
            360,
        )
        for case in CONIC_CASES
    ],
    *[
        Check(
            f"rational-cubic-d8-{kind}-{position}",
            RC,
            py(RC / "explore_rational_cubic_d8.py", kind, position),
            ("rank",),
            180,
        )
        for kind in ("cusp", "node")
        for position in ("transverse", "fiber")
    ],
    *[
        Check(
            f"rational-cubic-d7-{kind}-{position}",
            RC,
            py(RC / "explore_rational_cubic_d7.py", kind, position),
            ("rank",),
            180,
        )
        for kind in ("cusp", "node")
        for position in ("transverse", "fiber")
    ],
    *[
        Check(
            f"rational-cubic-custom-{case}",
            RC,
            py(RC / "explore_rational_cubic_custom2.py", case),
            ("D8 rank", "D7"),
            240,
        )
        for case in ("cusp-smooth", "cusp-generic", "node-smooth")
    ],
    Check(
        "rational-cubic-cusp-fiber-r0",
        RC,
        py(RC / "cusp_fiber_d6.py", "r0"),
        ("terms",),
        180,
    ),
    Check(
        "rational-cubic-cusp-fiber-r1",
        RC,
        py(RC / "cusp_fiber_d6.py", "r1"),
        ("(1, 3, 2) 3/2",),
        180,
    ),
    *[
        Check(
            f"rational-cubic-cusp-smooth-{branch}",
            RC,
            py(RC / "cusp_smooth_d6_fast.py", branch),
            (("branch " + branch) if branch != "zero" else "branch zero",),
            180,
        )
        for branch in ("zero", "a", "b")
    ],
    Check(
        "rational-cubic-cusp-smooth-q",
        RC,
        py(RC / "cusp_smooth_q_branch.py"),
        ("(0, 4, 1) -6",),
        180,
    ),
    Check(
        "rational-cubic-cusp-generic-q-d6",
        RC,
        py(RC / "cusp_generic_q_d6.py"),
        ("terms",),
        180,
    ),
    Check(
        "rational-cubic-node-marked-h2z",
        RC,
        py(RC / "node_marked_h2z.py"),
        ("rank",),
        240,
    ),
    Check(
        "rational-cubic-node-marked-binary",
        RC,
        py(RC / "node_marked_binary_d7.py"),
        ("piv (", "c17 0"),
        240,
    ),
]

SLOW: list[Check] = [
    Check(
        "rational-cubic-node-full-h2z-matrix",
        RC,
        py(RC / "node_h2z_fullmatrix.py"),
        ("12582912",),
        420,
    )
]


def run(check: Check, output_dir: Path) -> bool:
    print(f"[RUN] {check.name}", flush=True)
    started = time.monotonic()
    try:
        proc = subprocess.run(
            check.argv,
            cwd=check.cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=check.timeout,
            check=False,
        )
        output = proc.stdout
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or "") + (exc.stderr or "")
        (output_dir / f"{check.name}.out").write_text(output, encoding="utf-8")
        print(f"[FAIL] {check.name}: timeout after {check.timeout}s")
        return False

    elapsed = time.monotonic() - started
    (output_dir / f"{check.name}.out").write_text(output, encoding="utf-8")
    missing = [needle for needle in check.needles if needle not in output]
    if proc.returncode != 0 or missing:
        print(
            f"[FAIL] {check.name}: returncode={proc.returncode}; "
            f"missing={missing!r}; elapsed={elapsed:.2f}s"
        )
        return False
    print(f"[PASS] {check.name} ({elapsed:.2f}s)")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="run the broader branch suite")
    parser.add_argument(
        "--include-slow",
        action="store_true",
        help="also run the approximately two-minute nodal full-matrix calculation",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "fresh-replay",
        help="directory for fresh combined outputs",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    checks = list(COMPACT)
    if args.full:
        checks.extend(FULL_EXTRA)
    if args.include_slow:
        checks.extend(SLOW)

    failures: list[str] = []
    overall = time.monotonic()
    for check in checks:
        if not run(check, args.output_dir):
            failures.append(check.name)

    elapsed = time.monotonic() - overall
    if failures:
        print(f"FAILED {len(failures)} / {len(checks)} checks in {elapsed:.2f}s")
        for name in failures:
            print(f"  - {name}")
        return 1
    print(f"PASS: {len(checks)} exact Lane 4 checks completed in {elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
