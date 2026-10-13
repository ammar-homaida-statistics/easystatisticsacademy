"""Audit generated site-local navigation links, fragments, and local assets.

No network requests. By default, report legacy defects without failing CI.
Use --baseline FILE to fail only for findings absent from a reviewed baseline.
Use --strict to fail on every finding. Run after the Jekyll build.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import posixpath
from urllib.parse import unquote, urljoin, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        if tag in ("a", "area") and attrs.get("href") is not None:
            self.refs.append((self.getpos()[0], "href", attrs["href"]))
        if tag in ("script", "img", "iframe", "source") and attrs.get("src"):
            self.refs.append((self.getpos()[0], "src", attrs["src"]))
        if tag == "link" and attrs.get("href") and (
            "stylesheet" in attrs.get("rel", "").split() or attrs.get("rel") == "icon"
        ):
            self.refs.append((self.getpos()[0], "href", attrs["href"]))


def audit(root, site_url="https://easystatisticsacademy.com"):
    root = Path(root)
    base = urlsplit(site_url)
    parsed_pages = {}
    for file in sorted(root.rglob("*.html")):
        parser = Links()
        parser.feed(file.read_text(encoding="utf-8", errors="replace"))
        parsed_pages[file.relative_to(root).as_posix()] = parser

    findings = []
    for source, page in parsed_pages.items():
        route = "/" + source
        if route.endswith("/index.html"):
            route = route[:-10]
        origin = site_url.rstrip("/") + route
        for line, attribute, raw in page.refs:
            link = raw.strip()
            if not link or link == "#" or link.startswith(("javascript:", "mailto:", "tel:", "data:")):
                continue
            target = urlsplit(urljoin(origin, link))
            if target.scheme not in ("http", "https") or target.netloc != base.netloc:
                continue
            target_path = unquote(target.path)
            if "\x00" in target_path or "\\" in target_path:
                continue
            normalized = posixpath.normpath(target_path)
            if target_path.endswith("/") and normalized != "/":
                normalized += "/"
            dest = (normalized.lstrip("/") + "index.html"
                    if normalized.endswith("/") else normalized.lstrip("/"))
            if not dest:
                dest = "index.html"
            if dest not in parsed_pages and not (root / dest).is_file():
                findings.append({
                    "source": source, "line": line, "target": link,
                    "reason": "missing-page-or-asset",
                })
            elif target.fragment and attribute == "href" and dest in parsed_pages:
                fragment = unquote(target.fragment)
                if fragment not in parsed_pages[dest].ids:
                    # IDs generated dynamically by JS cannot be verified from HTML.
                    findings.append({
                        "source": source, "line": line, "target": link,
                        "reason": "missing-static-anchor",
                    })
    return sorted(findings, key=lambda x: (x["source"], x["line"], x["target"], x["reason"]))


def signature(issue):
    return "|".join((issue["source"], issue["target"], issue["reason"]))


def main():
    arg = argparse.ArgumentParser(description=__doc__)
    arg.add_argument("--site", type=Path, default=Path("_site"))
    arg.add_argument("--baseline", type=Path)
    arg.add_argument("--strict", action="store_true")
    arg.add_argument("--max-reported", type=int, default=60)
    args = arg.parse_args()
    issues = audit(args.site)
    baseline = set()
    if args.baseline:
        baseline = set(json.loads(args.baseline.read_text(encoding="utf-8")))
    new_issues = [issue for issue in issues if signature(issue) not in baseline]
    counts = Counter(issue["reason"] for issue in issues)
    print(f"Internal link audit: {len(issues)} findings; by type: {dict(counts)}")
    if args.baseline:
        print(f"Baseline entries: {len(baseline)}; new findings: {len(new_issues)}")
    for issue in issues[:max(0, args.max_reported)]:
        print(f"{issue['source']}:{issue['line']}: {issue['reason']}: {issue['target']}")
    if len(issues) > args.max_reported:
        print(f"... {len(issues)-args.max_reported} additional findings omitted from log")
    # GitHub Actions output can be searched for exact signatures.
    print("AUDIT_SIGNATURES_JSON=" + json.dumps(sorted(set(map(signature, issues))),
                                             ensure_ascii=False))
    if args.strict or (args.baseline and new_issues):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
