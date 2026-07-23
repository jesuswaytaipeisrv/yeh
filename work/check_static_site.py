#!/usr/bin/env python3
"""Static validation for the archived site before GitHub Pages deployment."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


BASE_URL = "https://jesuswaytaipeisrv.github.io/yeh/"
ATTRIBUTE_RE = re.compile(r'(?:src|href)=["\']([^"\']+)', re.IGNORECASE)


def local_target(page: Path, docs: Path, value: str) -> Path | None:
    if value.startswith(("#", "mailto:", "tel:", "javascript:", "data:", "//")):
        return None
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if path.startswith("/yeh/"):
        return docs / path.removeprefix("/yeh/")
    if path.startswith("/"):
        return docs.parent / path.lstrip("/")
    return page.parent / path


def main() -> int:
    docs = Path(sys.argv[1] if len(sys.argv) > 1 else "docs").resolve()
    errors: list[str] = []
    primary_pages = sorted(
        page
        for page in docs.rglob("*.html")
        if page.relative_to(docs).parts[0] != "2"
    )

    for page in primary_pages:
        source = page.read_text(encoding="utf-8")
        relative = page.relative_to(docs)
        checks = {
            "canonical": len(re.findall(r'<link\s+rel=["\']canonical["\']', source, re.I)),
            "og:url": len(re.findall(r'<meta\s+property=["\']og:url["\']', source, re.I)),
            "static stylesheet": source.count("static-overrides.css"),
        }
        for label, count in checks.items():
            if count != 1:
                errors.append(f"{relative}: {label} 數量應為 1，實際為 {count}")

        forbidden = {
            "Weebly 留言 iframe": "showCommentForm",
            "Weebly 投影片": "wSlideshow.render",
            "錯誤背景網址": "&quot;/uploads/",
            "可提交表單": "<form",
        }
        for label, needle in forbidden.items():
            if needle.lower() in source.lower():
                errors.append(f"{relative}: 仍含有{label}")

        for meta_name in ("og:image", "og:url"):
            for tag in re.findall(
                rf'<meta\s+property=["\']{re.escape(meta_name)}["\'][^>]+>', source, re.I
            ):
                if "fanfanyeh.net" in tag or "editmysite.com" in tag:
                    errors.append(f"{relative}: {meta_name} 仍依賴舊站或 Weebly")

        for value in ATTRIBUTE_RE.findall(source):
            target = local_target(page, docs, value)
            if target is not None and not target.exists():
                errors.append(f"{relative}: 本地引用缺檔 {value}")

    redirects = list((docs / "2" / "post").rglob("*.html"))
    if len(redirects) != 18:
        errors.append(f"舊文章轉址頁應為 18，實際為 {len(redirects)}")

    sitemap = docs / "sitemap.xml"
    if not sitemap.exists():
        errors.append("缺少 sitemap.xml")
    else:
        sitemap_source = sitemap.read_text(encoding="utf-8")
        if sitemap_source.count("<url>") != 25:
            errors.append("sitemap.xml 應包含 25 個正式網址")
        if BASE_URL not in sitemap_source:
            errors.append("sitemap.xml 未使用目前 GitHub Pages 正式網址")

    robots = (docs / "robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {BASE_URL}sitemap.xml" not in robots:
        errors.append("robots.txt 的 Sitemap 網址不正確")

    if errors:
        print("static validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "static validation passed: "
        f"primary_pages={len(primary_pages)}, redirects={len(redirects)}, sitemap_urls=25"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
