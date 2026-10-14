"""Audit generated educational HTML for SEO metadata and heading regressions.

Historical issues are reported without editing page content. With --baseline,
only unrecognized findings cause CI to fail. Does not access the network.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_title = False
        self.title_text = []
        self.descriptions = []
        self.robots = []
        self.canonicals = []
        self.h1_count = 0
        self.has_main = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            name = attributes.get("name", "").lower()
            if name == "description":
                self.descriptions.append(attributes.get("content", "").strip())
            elif name == "robots":
                self.robots.append(attributes.get("content", "").lower())
        elif tag == "link" and "canonical" in attributes.get("rel", "").lower().split():
            self.canonicals.append(attributes.get("href", "").strip())
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "main" and attributes.get("id") == "main-content":
            self.has_main = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)

    @property
    def title(self):
        return " ".join("".join(self.title_text).split())


def route_for(file):
    route = "/" + file.as_posix()
    if route.endswith("/index.html"):
        return route[:-10]
    return route


def audit(site_root, site_url="https://easystatisticsacademy.com"):
    site_root = Path(site_root)
    sitemap = site_root / "sitemap.xml"
    indexed = set()
    if sitemap.is_file():
        root = ElementTree.fromstring(sitemap.read_text(encoding="utf-8"))
        indexed = {node.text for node in root.iter()
                   if node.tag.endswith("}loc") and node.text}

    findings = []
    seen_titles = {}
    for file in sorted(site_root.rglob("*.html")):
        doc = Document()
        doc.feed(file.read_text(encoding="utf-8", errors="replace"))
        if not doc.has_main:  # Raw verification/utility files are not educational pages.
            continue
        relative = file.relative_to(site_root)
        route = route_for(relative)
        canonical = site_url.rstrip("/") + route

        def issue(code):
            findings.append({"source": relative.as_posix(), "reason": code})

        if not doc.title:
            issue("missing-title")
        if len(doc.descriptions) != 1 or not doc.descriptions[0]:
            issue("missing-or-empty-description")
        if len(doc.canonicals) != 1:
            issue("missing-or-duplicate-canonical")
        elif doc.canonicals[0] != canonical:
            issue("canonical-mismatch")
        if doc.h1_count == 0:
            issue("missing-h1")
        elif doc.h1_count > 1:
            issue("multiple-h1")

        noindex = any("noindex" in value.split(",") or
                      "noindex" in value.replace(",", " ").split()
                      for value in doc.robots)
        # The dedicated 404 route should never be indexed.
        if route == "/404.html" and not noindex:
            issue("404-missing-noindex")
        if sitemap.is_file():
            if noindex and canonical in indexed:
                issue("noindex-in-sitemap")
            elif not noindex and route != "/404.html" and canonical not in indexed:
                issue("indexable-not-in-sitemap")
        if not noindex and doc.title:
            key = doc.title.casefold()
            if key in seen_titles:
                issue("duplicate-title")
                findings.append({"source": seen_titles[key], "reason": "duplicate-title"})
            else:
                seen_titles[key] = relative.as_posix()

    return sorted({(x["source"], x["reason"]) for x in findings})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("_site"))
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--max-reported", type=int, default=60)
    args = parser.parse_args()

    findings = audit(args.site)
    signatures = sorted(source + "|" + reason for source, reason in findings)
    accepted = set(json.loads(args.baseline.read_text(encoding="utf-8"))) if args.baseline else set()
    new = [item for item in signatures if item not in accepted]
    counts = Counter(reason for _, reason in findings)
    print(f"SEO audit: {len(findings)} findings; reasons: {dict(counts)}")
    if args.baseline:
        print(f"SEO baseline entries: {len(accepted)}; new findings: {len(new)}")
    for item in signatures[:max(args.max_reported, 0)]:
        print("SEO_FINDING: " + item)
    if len(signatures) > args.max_reported:
        print(f"... {len(signatures)-args.max_reported} additional SEO findings omitted")
    print("SEO_SIGNATURES_JSON=" + json.dumps(signatures, ensure_ascii=False))
    if args.baseline and new:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
