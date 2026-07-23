#!/usr/bin/env python3
"""Check public HTTP links, distinguishing failures from bot-blocked responses."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
BLOCKED_CODES = {401, 403, 429}


def json_urls(value: Any) -> list[str]:
    if isinstance(value, dict):
        result: list[str] = []
        for item in value.values():
            result.extend(json_urls(item))
        return result
    if isinstance(value, list):
        result = []
        for item in value:
            result.extend(json_urls(item))
        return result
    if isinstance(value, str) and value.startswith(("http://", "https://")):
        return [value]
    return []


def collect_urls(root: Path) -> list[str]:
    urls: set[str] = set()
    for path in sorted((root / "docs").rglob("*.md")):
        urls.update(MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")))
    for path in sorted((root / "data/claims-v2").rglob("*.json")):
        urls.update(json_urls(json.loads(path.read_text(encoding="utf-8"))))
    return sorted(urls)


def request(url: str, timeout: float) -> tuple[str, str, int | None, str]:
    headers = {"User-Agent": "GJC-link-audit/1.0 (+https://github.com/nmonson1/guide-to-jacobian-conjecture)"}
    for method in ("HEAD", "GET"):
        try:
            request_object = urllib.request.Request(url, headers=headers, method=method)
            with urllib.request.urlopen(request_object, timeout=timeout) as response:
                return url, "ok", response.status, response.geturl()
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in {400, 405, 501}:
                continue
            if exc.code in BLOCKED_CODES:
                return url, "blocked", exc.code, str(exc)
            return url, "failed", exc.code, str(exc)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            if method == "HEAD":
                continue
            return url, "failed", None, str(exc)
    return url, "failed", None, "no response"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()
    urls = collect_urls(args.root.resolve())
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = sorted(
            executor.map(lambda url: request(url, args.timeout), urls),
            key=lambda item: item[0],
        )
    report = {
        "checked": len(results),
        "ok": [item[0] for item in results if item[1] == "ok"],
        "blocked": [
            {"url": item[0], "status": item[2], "detail": item[3]}
            for item in results
            if item[1] == "blocked"
        ],
        "failed": [
            {"url": item[0], "status": item[2], "detail": item[3]}
            for item in results
            if item[1] == "failed"
        ],
    }
    if args.json_output:
        if args.json_output.exists():
            parser.error(f"refusing to overwrite {args.json_output}")
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    for item in report["failed"]:
        print(f"FAILED {item['status'] or '-'} {item['url']} — {item['detail']}", file=sys.stderr)
    for item in report["blocked"]:
        print(f"BLOCKED {item['status']} {item['url']}")
    print(
        f"Checked {report['checked']} links: {len(report['ok'])} reachable, "
        f"{len(report['blocked'])} bot-blocked, {len(report['failed'])} failed."
    )
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
