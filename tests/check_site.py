"""Check navigation, publication fragments and URL prefixes in the built demo."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids = set()
        self.duplicates = set()
        self.links = []
        self.current = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if value := attrs.get("id"):
            if value in self.ids:
                self.duplicates.add(value)
            self.ids.add(value)
        for attr in ("href", "src"):
            if value := attrs.get(attr):
                self.links.append(value)
        if attrs.get("aria-current") == "page":
            self.current.append(attrs.get("href"))


def validate(root, base):
    paths = ["index.html", "publications/index.html", "projects/index.html"]
    pages = {name: Page((root / name).read_text(encoding="utf-8")) for name in paths}
    errors = []
    references = set()
    for name, page in pages.items():
        url = base + "/" + name.removesuffix("index.html")
        if page.current != [url]:
            errors.append(f"{name}: incorrect current-page marker: {page.current}")
        if page.duplicates:
            errors.append(f"{name}: duplicate IDs: {sorted(page.duplicates)}")
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.netloc or parsed.scheme:
                continue
            resolved = urlsplit(urljoin(url, link))
            if not resolved.path.startswith(base + "/"):
                errors.append(f"{name}: outside base path: {link}")
                continue
            target = unquote(resolved.path.removeprefix(base + "/"))
            if not target or target.endswith("/"):
                target += "index.html"
            if not (root / target).is_file():
                errors.append(f"{name}: missing file: {link}")
            elif resolved.fragment:
                destination = pages.get(target) or Page((root / target).read_text(encoding="utf-8"))
                if unquote(resolved.fragment) not in destination.ids:
                    errors.append(f"{name}: missing fragment: {link}")
                if target == "publications/index.html" and name == "index.html":
                    references.add(resolved.fragment)
    if len(references) < 2:
        errors.append("Expected both research group and paper anchors from the homepage.")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Verified {len(pages)} pages and {len(references)} homepage publication links at {base or '/'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("base", nargs="?", default="")
    args = parser.parse_args()
    validate(args.root, args.base.rstrip("/"))
