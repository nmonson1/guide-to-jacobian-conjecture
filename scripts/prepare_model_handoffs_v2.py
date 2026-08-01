#!/usr/bin/env python3
"""Prepare a write-once handoff release with one compiler-owned v2 marker."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LANE_SLUG = "homogeneous-realization-compression"
ARGUMENT_ID = "ARG-RMU5D8E0003-FINITE-PLANE"
OLD_ARGUMENT = """A separate exact rank-six plane calculation is now complete through the first
intrinsic obstruction.  Generic finite slopes do not lift cubically.  The
rational exceptional slope `r=4` is intrinsically obstructed at cubic order.
The two conjugate slopes

```text
r = 4 + 4 sqrt(-3),   r = 4 - 4 sqrt(-3)
```

have 17-dimensional cubic-lift fibres but each has an intrinsic quartic
obstruction; the exact coefficient-span certificate pairs to `-1152` at one
conjugate and transfers by field conjugation.  These statements classify the
selected finite plane only, not the full 15-dimensional finite row-base fibre
or the infinity fibre."""
MARKER = f"<!-- retained-math-v2-selection:{ARGUMENT_ID} -->"
OLD_PRIORITY = """3. Extend the selected-plane calculation to the complete finite row-base
   fibre and the infinity fibre, retaining all cubic-lift parameters before
   computing the next Kuranishi map.
4. Impose the separate compression functional and the full moving target and
   stable gauges.
5. Seek a conceptual lower bound from collision monoliths or the `sl/sp`
   dichotomy that depends on the cover rather than one presentation."""
NEW_PRIORITY = """3. Impose the separate compression functional and the full moving target and
   stable gauges.
4. Seek a conceptual lower bound from collision monoliths or the `sl/sp`
   dichotomy that depends on the cover rather than one presentation."""
FORBIDDEN = ("/fss/", "/home/", "chatgpt.com/share", "INTAKE-", "sandbox:/")


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _validate_public(text: str, *, source: Path) -> None:
    lowered = text.casefold()
    found = [item for item in FORBIDDEN if item.casefold() in lowered]
    if found:
        raise ValueError(f"{source}: forbidden public markers: {found}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    base = args.base_dir.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    base_manifest_path = base / "manifest.json"
    base_manifest = _load(base_manifest_path)
    if base_manifest.get("brief_count") != 16:
        raise ValueError("base release must contain sixteen handoffs")
    if base_manifest.get("primary_entrypoint_count") != 10:
        raise ValueError("base release must contain ten primary entrypoints")

    prepared: list[tuple[str, bytes, dict[str, Any]]] = []
    for item in base_manifest["briefs"]:
        source = base / item["source"]
        payload = source.read_bytes()
        if len(payload) != item["bytes"] or _sha256(payload) != item["sha256"]:
            raise ValueError(f"base source does not match manifest: {source}")
        text = payload.decode("utf-8")
        if item["program_slug"] == LANE_SLUG:
            if text.count(OLD_ARGUMENT) != 1:
                raise ValueError("Lane 6 copied argument did not match exactly once")
            if text.count(OLD_PRIORITY) != 1:
                raise ValueError("Lane 6 copied task did not match exactly once")
            text = text.replace(OLD_ARGUMENT, MARKER).replace(
                OLD_PRIORITY, NEW_PRIORITY
            )
        elif "retained-math-v2-selection:" in text:
            raise ValueError(f"unexpected v2 marker in {source}")
        _validate_public(text, source=source)
        rendered = text.encode("utf-8")
        prepared.append(
            (
                item["source"],
                rendered,
                {
                    **item,
                    "sha256": _sha256(rendered),
                    "bytes": len(rendered),
                    "words": len(text.split()),
                },
            )
        )

    output.mkdir()
    for name, payload, _ in prepared:
        with (output / name).open("xb") as handle:
            handle.write(payload)
    manifest = {
        "schema_version": 3,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "base_release": {
            "release_id": base_manifest["release_id"],
            "manifest_sha256": _sha256(base_manifest_path.read_bytes()),
        },
        "brief_count": len(prepared),
        "primary_entrypoint_count": sum(
            bool(item["primary_entrypoint"]) for _, _, item in prepared
        ),
        "retained_math_v2_markers": [
            {
                "program_slug": LANE_SLUG,
                "argument_id": ARGUMENT_ID,
            }
        ],
        "briefs": [item for _, _, item in prepared],
    }
    manifest_payload = (
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    with (output / "manifest.json").open("xb") as handle:
        handle.write(manifest_payload)
    print(
        json.dumps(
            {
                "output_dir": str(output),
                "release_id": args.release_id,
                "brief_count": len(prepared),
                "primary_entrypoint_count": manifest["primary_entrypoint_count"],
                "manifest_sha256": _sha256(manifest_payload),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
