#!/usr/bin/env python3
"""Verify discoverability rules in a completed MkDocs build."""

from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
import sys
from urllib.parse import urljoin
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE_URL = "https://nmonson1.github.io/guide-to-jacobian-conjecture/"


def digest(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_url(path: str) -> str:
    source = Path(path)
    if source.name == "index.md":
        parent = source.parent.as_posix()
        return "" if parent == "." else f"{parent}/"
    return f"{source.with_suffix('').as_posix()}/"


def output_file(site: Path, url: str) -> Path:
    return site / url / "index.html" if url else site / "index.html"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", type=Path)
    args = parser.parse_args()
    site = args.site_dir.resolve()
    reviews = json.loads(
        (ROOT / "editorial" / "reviews.json").read_text(encoding="utf-8")
    )["pages"]
    failures: list[str] = []
    approved_urls: set[str] = set()

    for path, record in sorted(reviews.items()):
        url = page_url(path)
        approved = (
            record["status"] == "approved"
            and record.get("reviewed_sha256") == digest(DOCS / path)
        )
        listed = approved and path != "review/index.md"
        if listed:
            approved_urls.add(url)
        built = output_file(site, url)
        if not built.is_file():
            failures.append(f"missing built page: {url or '/'}")
            continue
        html = built.read_text(encoding="utf-8")
        expected_robots = "index, follow" if listed else "noindex, nofollow"
        if f'content="{expected_robots}"' not in html:
            failures.append(f"{url or '/'}: expected robots {expected_robots}")
        if not approved and 'class="editorial-state"' not in html:
            failures.append(f"{url or '/'}: missing editorial draft banner")
        if approved and 'class="editorial-state"' in html:
            failures.append(f"{url or '/'}: approved page still has draft banner")

    search_path = site / "search" / "search_index.json"
    try:
        search = json.loads(search_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"cannot read filtered search index: {exc}")
    else:
        found = {
            str(entry.get("location", "")).split("#", 1)[0]
            for entry in search.get("docs", [])
        }
        if not found.issubset(approved_urls):
            failures.append(
                "search includes unapproved URLs: "
                + ", ".join(sorted(found - approved_urls))
            )
        if approved_urls - found:
            failures.append(
                "search omits approved URLs: " + ", ".join(sorted(approved_urls - found))
            )

    review_status_path = site / "review" / "status.json"
    try:
        review_status = json.loads(review_status_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"cannot read review/status.json: {exc}")
    else:
        recorded = {page["path"] for page in review_status.get("pages", [])}
        if recorded != set(reviews):
            failures.append("review/status.json does not contain exactly the source pages")

    if not (site / "review" / "all-pages-search-index.json").is_file():
        failures.append("review-only full search index was not produced")

    sitemap_path = site / "sitemap.xml"
    if sitemap_path.is_file():
        tree = ElementTree.parse(sitemap_path)
        namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
        locations = {
            (node.text or "")
            for node in tree.findall(f".//{{{namespace}}}loc")
        }
        expected = {urljoin(SITE_URL, url) for url in approved_urls}
        if locations != expected:
            failures.append(
                f"sitemap mismatch: expected {len(expected)} URLs, found {len(locations)}"
            )
        compressed = site / "sitemap.xml.gz"
        if not compressed.is_file():
            failures.append("compressed sitemap is missing")
        else:
            with gzip.open(compressed, "rb") as handle:
                if handle.read() != sitemap_path.read_bytes():
                    failures.append(
                        "compressed sitemap does not match filtered sitemap.xml"
                    )
    elif approved_urls:
        failures.append("sitemap is missing despite approved pages")

    if failures:
        print("Built-site checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)
    print(
        f"Built-site checks passed for {len(reviews)} public pages; "
        f"{len(approved_urls)} exact versions are listed."
    )


if __name__ == "__main__":
    main()
