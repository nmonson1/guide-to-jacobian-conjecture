"""Load and verify the sanitized public-site release pointer."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_site_state(root: Path) -> dict[str, Any]:
    path = root / "site-state.json"
    state = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "schema_version",
        "release_id",
        "updated_at",
        "timezone",
        "publication",
        "claim_graph",
        "manuscripts",
        "technical_materials",
        "model_briefs",
        "docs_dir",
        "expected_counts",
    }
    if state.get("schema_version") != 1 or set(state) != required:
        raise ValueError(f"invalid site-state structure: {path}")
    if state["timezone"] != "America/Los_Angeles":
        raise ValueError("site-state dates must use America/Los_Angeles")
    for key in (
        "publication",
        "claim_graph",
        "manuscripts",
        "technical_materials",
        "model_briefs",
    ):
        component = state[key]
        manifest = root / "data" / component["data_dir"] / "manifest.json"
        if not manifest.is_file():
            raise ValueError(f"missing {key} manifest: {manifest}")
        found = _sha256(manifest)
        if found != component["manifest_sha256"]:
            raise ValueError(
                f"{key} manifest digest mismatch: "
                f"expected {component['manifest_sha256']}, found {found}"
            )
    return state
