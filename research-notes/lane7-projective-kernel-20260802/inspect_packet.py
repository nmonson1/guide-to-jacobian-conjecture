#!/usr/bin/env python3
"""Smoke-check the extracted Lane 7 matrices and print their exact schema."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def matrix_shape(value: object) -> tuple[int, int] | None:
    if not isinstance(value, list) or not value:
        return None
    if not all(isinstance(row, list) for row in value):
        return None
    widths = {len(row) for row in value}
    if len(widths) != 1:
        raise ValueError(f"ragged matrix with row widths {sorted(widths)}")
    return len(value), widths.pop()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()

    residual_path = args.directory / "collision_residual_matrix_M.json"
    factorization_path = args.directory / "Hv10_split_matrix_factorization.json"
    residual = json.loads(residual_path.read_text(encoding="utf-8"))
    factorization = json.loads(factorization_path.read_text(encoding="utf-8"))

    print("residual keys:", sorted(residual))
    print("factorization keys:", sorted(factorization))
    for label, payload in (("residual", residual), ("factorization", factorization)):
        for key, value in payload.items():
            shape = matrix_shape(value)
            if shape is not None:
                print(f"{label}.{key}: matrix {shape[0]}x{shape[1]}")
            elif isinstance(value, str):
                print(f"{label}.{key}: string length {len(value)}")
            elif isinstance(value, (int, float, bool)) or value is None:
                print(f"{label}.{key}: {value!r}")
            elif isinstance(value, dict):
                print(f"{label}.{key}: object keys {sorted(value)}")
            elif isinstance(value, list):
                print(f"{label}.{key}: list length {len(value)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
