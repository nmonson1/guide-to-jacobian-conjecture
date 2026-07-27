#!/usr/bin/env python3
"""Validate the publication boundary and source tree for the Living Guide."""

from __future__ import annotations

import hashlib
import io
import json
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader

from generate_living_guide_v1 import (
    MANUSCRIPTS_DATA_DIR,
    PUBLICATION_DATA_DIR,
    PUBLIC_DOCS_DIR,
    SITE_STATE,
    TECHNICAL_MATERIALS_DATA_DIR,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / PUBLIC_DOCS_DIR
DATA = ROOT / "data" / PUBLICATION_DATA_DIR
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".html", ".css", ".js", ".txt"}
FORBIDDEN_STRINGS = {
    "/fss/",
    "/home/",
    "file://",
    "chatgpt.com/share",
    "JCG-CLAIM-",
    "JC-CAN-",
    "JC-PKG-",
    "SRC-JCG-",
    "conversation_id",
    "message_id",
    "occurrence_id",
    "private_locator",
    "archive_locator",
    "artifact_group_id",
    "sources/chatgpt-",
    "conversation-turn-index",
}
FORBIDDEN_PATTERNS = {
    "UUID": re.compile(
        r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-"
        r"[0-9a-f]{4}-[0-9a-f]{12}\b",
        re.IGNORECASE,
    ),
    "private snapshot": re.compile(r"\bsnapshot [0-9a-f]{12,}", re.IGNORECASE),
}
REQUIRED_NAV = ("Start", "Counterexample", "Geometry", "Plane Case", "Research", "About")
REQUIRED_RESULT_HEADINGS = (
    "## The central idea",
    "## For a first reading",
    "## Precise statement",
    "## Manuscripts and external links",
    "## Evidence, review, and detailed credit",
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _check_sensitive(text: str, label: str, failures: list[str]) -> None:
    lowered = text.casefold()
    for needle in FORBIDDEN_STRINGS:
        if needle.casefold() in lowered:
            failures.append(f"{label}: forbidden publication marker {needle!r}")
    for name, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(text):
            failures.append(f"{label}: forbidden {name}")


def _check_local_links(path: Path, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    targets += re.findall(r'href="([^"]+)"', text)
    for raw in targets:
        target = raw.split("#", 1)[0]
        if (
            not target
            or "://" in target
            or target.startswith(("mailto:", "#", "javascript:"))
        ):
            continue
        candidate = (path.parent / target).resolve()
        if target.endswith("/") and not candidate.exists():
            candidate = (path.parent / target.rstrip("/")).with_suffix(".md").resolve()
        if not candidate.exists():
            failures.append(
                f"{path.relative_to(ROOT)}: missing local link target {target!r}"
            )


def _pdf_text(reader: PdfReader) -> str:
    metadata = " ".join(str(value) for value in (reader.metadata or {}).values())
    return metadata + "\n" + "\n".join(
        page.extract_text() or "" for page in reader.pages
    )


def _check_zip(path: Path, failures: list[str]) -> None:
    with zipfile.ZipFile(path) as archive:
        for member in archive.infolist():
            member_path = Path(member.filename)
            if member_path.is_absolute() or ".." in member_path.parts:
                failures.append(f"{path.name}: unsafe archive member {member.filename!r}")
                continue
            if member.is_dir():
                continue
            payload = archive.read(member)
            suffix = member_path.suffix.lower()
            label = f"{path.name}:{member.filename}"
            if suffix in TEXT_SUFFIXES or suffix in {".py", ".tex", ".sage", ".m2"}:
                try:
                    _check_sensitive(payload.decode("utf-8"), label, failures)
                except UnicodeDecodeError:
                    failures.append(f"{label}: text payload is not UTF-8")
            elif suffix == ".pdf":
                _check_sensitive(_pdf_text(PdfReader(io.BytesIO(payload))), label, failures)


def main() -> int:
    failures: list[str] = []
    export = json.loads((DATA / "public-export.json").read_text(encoding="utf-8"))
    manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
    counts = export["counts"]
    expected_counts = {
        key: value
        for key, value in SITE_STATE["expected_counts"].items()
        if key
        not in {
            "pages_by_release_state",
            "pages_by_manuscript_coverage",
        }
    }
    for key, expected in expected_counts.items():
        if counts.get(key) != expected:
            failures.append(
                f"publication manifest: expected {key}={expected}, "
                f"found {counts.get(key)!r}"
            )
    if counts.get("pages_by_release_state") != SITE_STATE[
        "expected_counts"
    ]["pages_by_release_state"]:
        failures.append("publication manifest: release-state counts changed")
    if counts.get("pages_by_manuscript_coverage") != SITE_STATE[
        "expected_counts"
    ]["pages_by_manuscript_coverage"]:
        failures.append("publication manifest: manuscript-coverage counts changed")

    for entry in manifest["files"]:
        path = DATA / entry["path"]
        if not path.is_file() or _sha256(path) != entry["sha256"]:
            failures.append(f"publication digest mismatch: {entry['path']}")

    pages = {page["slug"]: page for page in export["pages"]}
    programs = export["research_programs"]
    draft_slugs = {
        slug
        for slug, page in pages.items()
        if page["release_state"] == "draft_public"
    }
    program_slugs = {
        slug for program in programs for slug in program["page_slugs"]
    }
    missing_program = sorted(draft_slugs - program_slugs)
    if missing_program:
        failures.append(
            "draft pages without a manuscript program: "
            + ", ".join(missing_program)
        )

    result_files = sorted((DOCS / "results").glob("*.md"))
    technical_files = sorted((DOCS / "technical").glob("*.md"))
    program_files = sorted((DOCS / "research/programs").glob("*.md"))
    expected_grouped = SITE_STATE["expected_counts"]["grouped_pages"]
    expected_technical = SITE_STATE["expected_counts"]["technical_records"]
    expected_programs = SITE_STATE["expected_counts"]["research_programs"]
    if len(result_files) != expected_grouped:
        failures.append(
            f"expected {expected_grouped} generated result pages, "
            f"found {len(result_files)}"
        )
    if len(technical_files) != expected_technical:
        failures.append(
            f"expected {expected_technical} generated technical pages, "
            f"found {len(technical_files)}"
        )
    if len(program_files) != expected_programs:
        failures.append(
            f"expected {expected_programs} research-program pages, "
            f"found {len(program_files)}"
        )

    for path in result_files:
        slug = path.stem
        page = pages.get(slug)
        if page is None:
            failures.append(f"{path.relative_to(ROOT)}: no publication record")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in REQUIRED_RESULT_HEADINGS:
            if heading not in text:
                failures.append(f"{path.relative_to(ROOT)}: missing {heading!r}")
        for field in (
            "statement",
            "credited_to",
            "evidence_present",
            "source_treatment",
            "manuscript_coverage",
            "connections",
        ):
            if field not in page:
                failures.append(f"{slug}: missing publication field {field}")
        if not page.get("credited_to"):
            failures.append(f"{slug}: public credit treatment is empty")
        if "The public working manuscript is the current source" in text:
            failures.append(f"{slug}: legacy blanket manuscript-source claim remains")
        coverage = page.get("manuscript_coverage", {})
        source_forms = {
            source.get("source_form")
            for source in page.get("source", [])
            if isinstance(source, dict)
        }
        program_manuscript_is_source = coverage.get("status") in {
            "complete",
            "manuscript_attached",
        }
        expected_working_manuscript = (
            "working manuscript" in source_forms
            or program_manuscript_is_source
        )
        if (
            "working manuscript" in page.get("source_form", [])
        ) != expected_working_manuscript:
            failures.append(
                f"{slug}: working-manuscript source form disagrees with "
                "its independent sources and audited program coverage"
            )
        if page.get("source_treatment") not in text:
            failures.append(f"{slug}: source coverage treatment is not rendered")
        if (
            "assets/manuscripts/" not in text
            and "](http://" not in text
            and "](https://" not in text
        ):
            failures.append(f"{slug}: no public manuscript or external source")
        _check_local_links(path, failures)

    for path in technical_files:
        text = path.read_text(encoding="utf-8")
        if "robots: noindex, nofollow" not in text:
            failures.append(f"{path.relative_to(ROOT)}: missing permanent noindex")
        if "search:\n  exclude: true" not in text:
            failures.append(f"{path.relative_to(ROOT)}: not excluded from search")
        _check_local_links(path, failures)

    for path in (
        list(DOCS.glob("*.md"))
        + program_files
        + list((DOCS / "story-v1").glob("*.md"))
        + list((DOCS / "claim").glob("*.md"))
        + list((DOCS / "claim-v3").glob("*.md"))
        + list((DOCS / "topic-v1").glob("*.md"))
        + list((DOCS / "topic-v1.2").glob("*.md"))
    ):
        _check_local_links(path, failures)

    scan_roots = (
        DOCS,
        DATA,
        ROOT / "data" / MANUSCRIPTS_DATA_DIR,
        ROOT / "data" / TECHNICAL_MATERIALS_DATA_DIR,
        ROOT / "overrides",
    )
    scanned = 0
    for scan_root in scan_roots:
        for path in scan_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            scanned += 1
            _check_sensitive(
                path.read_text(encoding="utf-8"),
                str(path.relative_to(ROOT)),
                failures,
            )

    manuscript_manifest = json.loads(
        (ROOT / "data" / MANUSCRIPTS_DATA_DIR / "manifest.json").read_text(
            encoding="utf-8"
        )
    )
    expected_manuscripts = SITE_STATE["manuscripts"]["expected_count"]
    if manuscript_manifest.get("manuscript_count") != expected_manuscripts:
        failures.append(
            f"manuscript manifest: expected {expected_manuscripts} manuscripts"
        )
    for item in manuscript_manifest["manuscripts"]:
        path = DOCS / "assets/manuscripts" / item["filename"]
        if not path.is_file() or _sha256(path) != item["sha256"]:
            failures.append(f"manuscript digest mismatch: {item['filename']}")
            continue
        reader = PdfReader(path)
        if len(reader.pages) != item["pages"]:
            failures.append(f"manuscript page-count mismatch: {item['filename']}")
        _check_sensitive(_pdf_text(reader), item["filename"], failures)

    materials_manifest = json.loads(
        (
            ROOT
            / "data"
            / TECHNICAL_MATERIALS_DATA_DIR
            / "manifest.json"
        ).read_text(encoding="utf-8")
    )
    if materials_manifest.get("artifact_count") != SITE_STATE[
        "technical_materials"
    ]["expected_count"]:
        failures.append("technical-material manifest: artifact count changed")
    materials_page = DOCS / "research/materials.md"
    if not materials_page.is_file():
        failures.append("technical-material landing page is missing")
        materials_text = ""
    else:
        materials_text = materials_page.read_text(encoding="utf-8")
    for program in materials_manifest["programs"]:
        program_page = DOCS / "research/programs" / f"{program['slug']}.md"
        program_text = program_page.read_text(encoding="utf-8")
        for artifact in program["artifacts"]:
            path = DOCS / "assets/technical-materials" / artifact["filename"]
            if not path.is_file() or _sha256(path) != artifact["sha256"]:
                failures.append(
                    f"technical-material digest mismatch: {artifact['filename']}"
                )
                continue
            if artifact["filename"] not in materials_text:
                failures.append(
                    f"technical-material landing page omits {artifact['filename']}"
                )
            if artifact["filename"] not in program_text:
                failures.append(
                    f"{program['slug']}: program page omits {artifact['filename']}"
                )
            if path.suffix.lower() == ".zip":
                _check_zip(path, failures)
            elif path.suffix.lower() == ".pdf":
                reader = PdfReader(path)
                if len(reader.pages) != artifact["pages"]:
                    failures.append(
                        f"technical-note page-count mismatch: {artifact['filename']}"
                    )
                _check_sensitive(_pdf_text(reader), artifact["filename"], failures)

    mkdocs_text = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    if f"docs_dir: {PUBLIC_DOCS_DIR}" not in mkdocs_text:
        failures.append("mkdocs.yml: wrong versioned docs_dir")
    for label in REQUIRED_NAV:
        if not re.search(rf"^\s*-\s+{re.escape(label)}\s*:", mkdocs_text, re.MULTILINE):
            failures.append(f"mkdocs.yml: missing navigation section {label!r}")
    if re.search(r"^\s*-\s+(Results|Technical|Claims)\s*:", mkdocs_text, re.MULTILINE):
        failures.append("mkdocs.yml: deep registry layer appears in navigation")
    if "mathjax@3.2.2/es5/tex-mml-chtml.js" not in mkdocs_text:
        failures.append("mkdocs.yml: MathJax is not pinned to 3.2.2")
    expected_date = (
        datetime.fromisoformat(SITE_STATE["updated_at"])
        .strftime("%d %B %Y")
        .lstrip("0")
        + ", Pacific time"
    )
    if expected_date not in mkdocs_text:
        failures.append("mkdocs.yml: Pacific-time update label is missing")

    override = (ROOT / "overrides/main.html").read_text(encoding="utf-8")
    if '<meta name="robots" content="noindex, nofollow">' not in override:
        failures.append("override: global noindex is missing")
    robots = (DOCS / "robots.txt").read_text(encoding="utf-8")
    if "Disallow: /" not in robots:
        failures.append("robots.txt: site-wide disallow is missing")

    css = (DOCS / "assets/stylesheets/extra.css").read_text(encoding="utf-8")
    for marker in (
        '[data-md-color-scheme="jacobian-dark"]',
        ":focus-visible",
        "@media (prefers-reduced-motion: reduce)",
        "@media screen and (max-width: 620px)",
        "font-size: 0.7rem",
    ):
        if marker not in css:
            failures.append(f"stylesheet: accessibility marker {marker!r} missing")

    if failures:
        print("Public-site checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(
        f"Public-site checks passed: {counts['grouped_pages']} grouped pages, "
        f"{counts['technical_records']} hidden technical records, "
        f"{len(manuscript_manifest['manuscripts'])} manuscripts, "
        f"{materials_manifest['artifact_count']} technical artifacts, "
        f"{scanned} text files scanned."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
