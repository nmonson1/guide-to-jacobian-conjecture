"""Shared validation utilities and indexed-manifest loader."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

CONTRIBUTION_DIR = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = CONTRIBUTION_DIR.parents[1]


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def extract_fenced_text(page: str, heading: str, language: str) -> str:
    marker = f"## {heading}"
    start = page.find(marker)
    require(start >= 0, f"missing heading {marker!r}")
    opening = re.search(rf"```{re.escape(language)}\s*\n", page[start:])
    require(opening is not None, f"missing {language} fence after {marker!r}")
    content_start = start + opening.end()
    content_end = page.find("\n```", content_start)
    require(content_end >= 0, f"unterminated fence after {marker!r}")
    return page[content_start:content_end].rstrip("\n") + "\n"


def extract_fenced_json(page: str, heading: str) -> dict[str, Any]:
    return json.loads(extract_fenced_text(page, heading, "json"))


def load_indexed_manifest(path: Path) -> dict[str, Any]:
    def resolve(value: Any) -> Any:
        if isinstance(value, dict) and set(value) == {"$include"}:
            relative = value["$include"]
            require(isinstance(relative, str), "fragment include must be a path")
            loaded = json.loads((CONTRIBUTION_DIR / relative).read_text(encoding="utf-8"))
            return resolve(loaded)
        if isinstance(value, dict):
            return {key: resolve(item) for key, item in value.items()}
        if isinstance(value, list):
            return [resolve(item) for item in value]
        return value

    index = json.loads(path.read_text(encoding="utf-8"))
    includes = index.pop("includes", None)
    if includes is None:
        return resolve(index)

    manifest = dict(index)
    for key, value in includes.items():
        if key == "stages":
            require(isinstance(value, list), "manifest stage includes must be a list")
            manifest[key] = [
                resolve(json.loads((CONTRIBUTION_DIR / relative).read_text(encoding="utf-8")))
                for relative in value
            ]
        else:
            require(isinstance(value, str), f"manifest include {key} must be a path")
            manifest[key] = resolve(
                json.loads((CONTRIBUTION_DIR / value).read_text(encoding="utf-8"))
            )
    return manifest


def source_by_id(manifest: dict[str, Any], source_id: str) -> dict[str, Any]:
    matches = [source for source in manifest["sources"] if source["id"] == source_id]
    require(len(matches) == 1, f"expected one source {source_id}, found {len(matches)}")
    return matches[0]


def stage_by_id(manifest: dict[str, Any], stage_id: str) -> dict[str, Any]:
    matches = [stage for stage in manifest["stages"] if stage["id"] == stage_id]
    require(len(matches) == 1, f"expected one stage {stage_id}, found {len(matches)}")
    return matches[0]


def run_replay(output_dir: Path) -> dict[str, Any]:
    command = [
        sys.executable,
        str(CONTRIBUTION_DIR / "independent_raw_support_replay.py"),
        "--output",
        str(output_dir),
        "--summary-only",
    ]
    completed = subprocess.run(
        command,
        cwd=REPOSITORY_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=300,
        check=False,
    )
    require(completed.returncode == 0, "independent replay failed:\n" + completed.stdout[-8000:])
    summary_path = output_dir / "summary.json"
    require(summary_path.is_file(), "independent replay did not write summary.json")
    return json.loads(summary_path.read_text(encoding="utf-8"))
