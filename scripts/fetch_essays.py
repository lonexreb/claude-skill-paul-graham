#!/usr/bin/env python3
"""
Refresh the Paul Graham essay manifest from paulgraham.com/articles.html.

Outputs a JSON file with {title, url, slug} for every essay on the index
page. Does NOT scrape essay bodies — this script exists only to keep the
URL/title index in sync with the live site for future curation passes.

Usage:
    python3 scripts/fetch_essays.py
    python3 scripts/fetch_essays.py --output path/to/manifest.json

Requires: requests, beautifulsoup4
    pip install requests beautifulsoup4
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print(
        "Missing dependencies. Install with: pip install requests beautifulsoup4",
        file=sys.stderr,
    )
    sys.exit(1)


ARTICLES_INDEX = "https://www.paulgraham.com/articles.html"
DEFAULT_OUTPUT = (
    Path(__file__).resolve().parent.parent
    / "skills"
    / "paul-graham"
    / "references"
    / "_essays-manifest.json"
)


def fetch_articles_index(url: str = ARTICLES_INDEX, timeout: int = 30) -> str:
    headers = {
        "User-Agent": (
            "claude-skill-paul-graham/0.1 (+https://github.com/lonexreb/"
            "claude-skill-paul-graham) index-refresh"
        )
    }
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text


def parse_essays(html: str, base_url: str = ARTICLES_INDEX) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    essays: list[dict] = []
    seen: set[str] = set()

    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].strip()
        title = anchor.get_text(strip=True)
        if not title:
            continue
        # Only keep links that look like individual essays (.html files)
        # on the same domain, not navigation/anchors/feeds.
        if not href.endswith(".html"):
            continue
        if href in {"articles.html", "index.html"}:
            continue
        if href.startswith("#") or href.startswith("mailto:"):
            continue

        absolute = urljoin(base_url, href)
        if absolute in seen:
            continue
        seen.add(absolute)

        slug = href.rsplit("/", 1)[-1].removesuffix(".html")
        essays.append({"title": title, "url": absolute, "slug": slug})

    return essays


def write_manifest(essays: list[dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": ARTICLES_INDEX,
        "count": len(essays),
        "essays": essays,
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output JSON path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--url",
        default=ARTICLES_INDEX,
        help="Articles index URL (default: paulgraham.com/articles.html)",
    )
    args = parser.parse_args(argv)

    try:
        html = fetch_articles_index(args.url)
    except requests.RequestException as exc:
        print(f"Failed to fetch {args.url}: {exc}", file=sys.stderr)
        return 1

    essays = parse_essays(html, base_url=args.url)
    if not essays:
        print("Warning: no essays parsed. Index page layout may have changed.", file=sys.stderr)
        return 2

    write_manifest(essays, args.output)
    print(f"Wrote {len(essays)} essays to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
