"""MkDocs editorial gating for public drafts and approved guide pages."""

from __future__ import annotations

import gzip
import hashlib
import html
import json
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from xml.etree import ElementTree

from mkdocs.exceptions import ConfigurationError
from mkdocs.plugins import event_priority

ALLOWED_STATUSES = {"unread", "needs_revision", "approved"}
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REVIEWS_FILE = ROOT / "editorial" / "reviews.json"
NAVIGATION_FILE = ROOT / "editorial" / "navigation.json"

_state: dict[str, dict[str, Any]] = {}
_titles: dict[str, str] = {}
_review_page_path = "review/index.md"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def effective_status(record: dict[str, Any], current_hash: str) -> str:
    if record.get("status") != "approved":
        return str(record.get("status"))
    return (
        "approved"
        if record.get("reviewed_sha256") == current_hash
        else "changed_since_review"
    )


def page_url(path: str) -> str:
    source = Path(path)
    if source.name == "index.md":
        parent = source.parent.as_posix()
        return "" if parent == "." else f"{parent}/"
    return f"{source.with_suffix('').as_posix()}/"


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigurationError(f"Cannot load {path.relative_to(ROOT)}: {exc}") from exc


def load_editorial_state() -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    reviews = _load_json(REVIEWS_FILE)
    navigation = _load_json(NAVIGATION_FILE)
    records = reviews.get("pages")
    if not isinstance(records, dict):
        raise ConfigurationError("editorial/reviews.json must contain a pages object")

    markdown_paths = {
        path.relative_to(DOCS).as_posix() for path in DOCS.rglob("*.md")
    }
    ledger_paths = set(records)
    missing = sorted(markdown_paths - ledger_paths)
    stale = sorted(ledger_paths - markdown_paths)
    if missing or stale:
        messages = []
        if missing:
            messages.append("missing review records: " + ", ".join(missing))
        if stale:
            messages.append("review records for missing pages: " + ", ".join(stale))
        raise ConfigurationError("; ".join(messages))

    state: dict[str, dict[str, Any]] = {}
    for path in sorted(markdown_paths):
        record = records[path]
        if not isinstance(record, dict) or record.get("status") not in ALLOWED_STATUSES:
            raise ConfigurationError(
                f"{path}: status must be one of {sorted(ALLOWED_STATUSES)}"
            )
        current_hash = sha256_file(DOCS / path)
        status = effective_status(record, current_hash)
        state[path] = {
            **record,
            "sha256": current_hash,
            "effective_status": status,
            "approved": status == "approved",
            "url": page_url(path),
            "in_navigation": True,
        }

    placed: set[str] = set()
    sections = navigation.get("sections")
    if not isinstance(sections, list):
        raise ConfigurationError("editorial/navigation.json must contain sections")
    for section in sections:
        for page in section.get("pages", []):
            path = page.get("path")
            title = page.get("title")
            in_navigation = page.get("nav", True)
            if path not in state or not isinstance(title, str):
                raise ConfigurationError(f"invalid navigation entry: {page!r}")
            if not isinstance(in_navigation, bool):
                raise ConfigurationError(f"{path}: nav must be true or false")
            if path in placed:
                raise ConfigurationError(f"duplicate navigation entry: {path}")
            placed.add(path)
            state[path]["in_navigation"] = in_navigation

    review = navigation.get("review_page", {})
    review_path = review.get("path")
    if review_path not in state:
        raise ConfigurationError("navigation review_page must name a tracked page")
    if state[review_path]["approved"]:
        raise ConfigurationError("the review workspace must remain unlisted")
    state[review_path]["in_navigation"] = False

    unplaced = markdown_paths - placed - {review_path}
    if unplaced:
        raise ConfigurationError(
            "pages missing from hand-authored placement: "
            + ", ".join(sorted(unplaced))
        )
    return state, navigation


@event_priority(100)
def on_config(config: Any) -> Any:
    global _state, _titles, _review_page_path
    _state, navigation = load_editorial_state()
    _titles = {}
    nav = []
    for section in navigation["sections"]:
        pages = []
        for page in section["pages"]:
            path = page["path"]
            _titles[path] = page["title"]
            if _state[path]["approved"] and _state[path]["in_navigation"]:
                pages.append({page["title"]: path})
        if pages:
            nav.append({section["title"]: pages})

    review = navigation["review_page"]
    _review_page_path = review["path"]
    _titles[_review_page_path] = review["title"]
    config["nav"] = nav
    config.setdefault("extra", {})["has_approved_pages"] = any(
        record["approved"]
        for path, record in _state.items()
        if path != _review_page_path
    )
    return config


def public_approved_urls(
    state: dict[str, dict[str, Any]], review_page_path: str
) -> set[str]:
    """Return indexed approved URLs, including contextual pages."""
    return {
        record["url"]
        for path, record in state.items()
        if path != review_page_path and record["approved"]
    }


def _review_list_html() -> str:
    items = []
    for path, record in _state.items():
        if path == _review_page_path:
            continue
        status = record["effective_status"]
        label = status.replace("_", " ")
        if not record["in_navigation"]:
            label += " · contextual"
        items.append(
            "<li>"
            f'<a href="../{html.escape(record["url"], quote=True)}">'
            f'{html.escape(_titles.get(path, path))}</a>'
            f"<code>{html.escape(path)}</code>"
            f'<span class="review-status review-status--{status}">{label}</span>'
            "</li>"
        )
    return '<ul class="review-list">' + "".join(items) + "</ul>"


def on_page_markdown(markdown: str, page: Any, config: Any, files: Any) -> str:
    del config, files
    path = page.file.src_uri
    record = _state[path]
    status = record["effective_status"]
    page.meta["editorial_status"] = status
    page.meta["robots"] = (
        "index, follow"
        if record["approved"] and path != _review_page_path
        else "noindex, nofollow"
    )

    if path == _review_page_path:
        marker = (
            '<div id="review-pages" aria-describedby="review-count">'
            "Loading the review index…</div>"
        )
        markdown = markdown.replace(
            marker,
            '<div id="review-pages" aria-describedby="review-count">'
            + _review_list_html()
            + "</div>",
        )
    if record["approved"]:
        return markdown

    messages = {
        "changed_since_review": (
            "This page changed after its last approval. It remains public for "
            "review, but is not included in navigation, search, or the sitemap."
        ),
        "needs_revision": (
            "This page is being revised. It remains public for review, but is not "
            "included in navigation, search, or the sitemap."
        ),
        "unread": (
            "This editorial draft is public for review, but has not yet been read "
            "by the guide's owner. It is not included in navigation, search, or "
            "the sitemap."
        ),
    }
    return (
        f'<aside class="editorial-state" data-editorial-status="{status}">'
        f'<strong>Editorial status: {status.replace("_", " ")}.</strong> '
        f'{messages[status]}</aside>\n\n{markdown}'
    )


def _filter_search(site_dir: Path, approved_urls: set[str]) -> None:
    search_file = site_dir / "search" / "search_index.json"
    if not search_file.exists():
        return
    payload = json.loads(search_file.read_text(encoding="utf-8"))
    review_dir = site_dir / "review"
    review_dir.mkdir(parents=True, exist_ok=True)
    (review_dir / "all-pages-search-index.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    payload["docs"] = [
        entry
        for entry in payload.get("docs", [])
        if str(entry.get("location", "")).split("#", 1)[0] in approved_urls
    ]
    search_file.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def _filter_sitemap(site_dir: Path, site_url: str, approved_urls: set[str]) -> None:
    sitemap = site_dir / "sitemap.xml"
    if not sitemap.exists():
        return
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ElementTree.register_namespace("", namespace)
    tree = ElementTree.parse(sitemap)
    root = tree.getroot()
    allowed = {urljoin(site_url, url) for url in approved_urls}
    for node in list(root):
        location = node.find(f"{{{namespace}}}loc")
        if location is None or (location.text or "") not in allowed:
            root.remove(node)
    tree.write(sitemap, encoding="utf-8", xml_declaration=True)
    compressed = site_dir / "sitemap.xml.gz"
    if compressed.exists():
        with gzip.open(compressed, "wb") as handle:
            handle.write(sitemap.read_bytes())


@event_priority(-100)
def on_post_build(config: Any) -> None:
    site_dir = Path(config["site_dir"])
    approved_urls = public_approved_urls(_state, _review_page_path)
    _filter_search(site_dir, approved_urls)
    _filter_sitemap(site_dir, str(config.get("site_url", "")), approved_urls)

    status_payload = {
        "schema_version": 1,
        "pages": [
            {
                "path": path,
                "title": _titles.get(path, path),
                "status": record["status"],
                "effective_status": record["effective_status"],
                "reviewed_at": record.get("reviewed_at"),
                "url": record["url"],
                "approved": record["approved"],
                "in_navigation": record["in_navigation"],
            }
            for path, record in _state.items()
        ],
    }
    review_dir = site_dir / "review"
    review_dir.mkdir(parents=True, exist_ok=True)
    (review_dir / "status.json").write_text(
        json.dumps(status_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
