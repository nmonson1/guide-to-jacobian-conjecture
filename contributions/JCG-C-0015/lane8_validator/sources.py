"""Source-pin and public-fixture validation."""
from __future__ import annotations

import json
from typing import Any

from .common import (
    CONTRIBUTION_DIR,
    REPOSITORY_ROOT,
    extract_fenced_json,
    extract_fenced_text,
    git_blob_sha1,
    require,
    sha256_file,
    source_by_id,
)


def validate_sources(manifest: dict[str, Any]) -> None:
    reconstruction = source_by_id(manifest, "SRC-L8-RECONSTRUCTION")
    reconstruction_path = REPOSITORY_ROOT / reconstruction["path"]
    require(reconstruction_path.is_file(), f"missing {reconstruction_path}")
    require(sha256_file(reconstruction_path) == reconstruction["sha256"],
            "Lane 8 reconstruction packet SHA-256 mismatch")

    source_packet = source_by_id(manifest, "SRC-L8-SOURCE-PACKET")
    source_packet_path = REPOSITORY_ROOT / source_packet["path"]
    require(source_packet_path.is_file(), f"missing {source_packet_path}")
    require(sha256_file(source_packet_path) == source_packet["sha256"],
            "Lane 8 source packet SHA-256 mismatch")

    appendix = source_by_id(manifest, "SRC-PROGRAM6-APPENDIX")
    appendix_path = REPOSITORY_ROOT / appendix["path"]
    require(appendix_path.is_file(), f"missing {appendix_path}")
    require(git_blob_sha1(appendix_path) == appendix["git_blob_sha"],
            "Program 6 theorem source Git blob SHA mismatch")
    appendix_text = appendix_path.read_text(encoding="utf-8")
    for label in appendix["labels"]:
        require(f"\\label{{{label}}}" in appendix_text, f"missing Program 6 label {label}")
    require("4,6,8,9,10,11" in appendix_text.replace(" ", ""),
            "Program 6 source does not expose the six archived indices")

    reconstruction_text = reconstruction_path.read_text(encoding="utf-8")
    public_relations = extract_fenced_json(reconstruction_text, "Exact quintic-field relations")
    fixture_path = CONTRIBUTION_DIR / "fixtures" / "belyi_exact_field_relations.json"
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    require(sha256_file(fixture_path) == manifest["replay"]["fixture_relations_sha256"],
            "trimmed exact-relations fixture SHA-256 mismatch")
    require(fixture["minimal_polynomial"] == public_relations["minimal_polynomial"],
            "fixture/public minimal polynomial mismatch")
    require(fixture["relations"] == public_relations["relations"],
            "fixture/public exact relation mismatch")

    helper_path = CONTRIBUTION_DIR / "fixtures" / "quintic_field_fast.py"
    helper = helper_path.read_text(encoding="utf-8")
    public_helper = extract_fenced_text(reconstruction_text, "Exact quintic-field helper", "python")
    require(sha256_file(helper_path) == manifest["replay"]["fixture_field_helper_sha256"],
            "exact field-helper fixture SHA-256 mismatch")
    require(helper == public_helper, "fixture/public exact field helper mismatch")
