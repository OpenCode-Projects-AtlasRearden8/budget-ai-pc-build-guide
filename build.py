#!/usr/bin/env python3
"""Static site builder for the Budget AI PC Guide.

Turns the Markdown manuals in docs/ into a small, self-contained static
HTML site in site/. No internet required, no frameworks, no tracking.

Usage:
    python3 build.py            build the site into site/
    python3 build.py --check    build, then verify links and structure
    python3 build.py --serve    build, then serve site/ at http://localhost:8000

Education-only project by Asdale Dynamics, LLC (MIT licensed).
"""

from __future__ import annotations

import argparse
import http.server
import pathlib
import re
import shutil
import sys

try:
    import markdown
except ImportError:  # friendly, actionable error instead of a traceback
    print(
        "error: the 'markdown' package is required.\n"
        "Install it with:  python3 -m pip install markdown",
        file=sys.stderr,
    )
    raise SystemExit(2)

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

# Reading order defines both the sidebar nav and the build order.
PAGES = [
    "index.md",
    "old-laptop-first.md",
    "parts-explained.md",
    "price-targets.md",
    "silent-vs-speed.md",
    "ram-and-vram.md",
    "shopping-worksheet.md",
    "first-boot-checklist.md",
    "ollama-install-day.md",
    "upkeep.md",
    "glossary.md",
]

TITLE = "The Budget AI PC Guide"
TAGLINE = "Run local AI on a used-parts PC — plain English, budget ceilings, no hype."
FOOTER = (
    "© Asdale Dynamics, LLC — education only, no product endorsements. "
    "This site is generated locally and works offline."
)

# --------------------------------------------------------------------------
# Markdown rendering
# --------------------------------------------------------------------------

_MD_EXTENSIONS = ["extra", "toc"]


def render_markdown(text: str) -> str:
    """Markdown -> HTML body (no page shell)."""
    return markdown.markdown(text, extensions=_MD_EXTENSIONS)


# --------------------------------------------------------------------------
# Link rewriting and validation
# --------------------------------------------------------------------------

_MD_LINK = re.compile(r"(\[[^\]]*\]\()(?P<target>[^)#]+)(?P<anchor>#[^)]*)?\)")


def rewrite_links(body: str, source_name: str) -> tuple[str, list[str]]:
    """Rewrite docs/*.md links to sibling .html pages; return (body, errors).

    Fenced code blocks are left untouched — links inside them are meant
    to display as literal text.
    """
    errors: list[str] = []

    def _replace(match: re.Match) -> str:
        target = match.group("target").strip()
        anchor = match.group("anchor") or ""
        if re.match(r"^[a-z]+://", target):
            return match.group(0)
        resolved = target
        if not resolved.endswith(".md"):
            errors.append(f"{source_name}: bad internal link target {target!r}")
            return match.group(0)
        page = (DOCS / resolved).resolve()
        if not page.is_file():
            errors.append(f"{source_name}: missing linked file {target!r}")
            return match.group(0)
        return f"{match.group(1)}{resolved[:-3]}.html{anchor})"

    chunks = re.split(r"(```.*?```)", body, flags=re.DOTALL)
    for i, chunk in enumerate(chunks):
        if chunk.startswith("```"):
            continue  # verbatim code block: do not rewrite
        chunks[i] = _MD_LINK.sub(_replace, chunk)
    rewritten = "".join(chunks)
    return rewritten, errors


# --------------------------------------------------------------------------
# Page shell
# --------------------------------------------------------------------------

_CSS = """
:root {
  --ink: #1f2328;
  --muted: #59616b;
  --line: #d8dee6;
  --bg: #fbf9f4;
  --card: #ffffff;
  --accent: #2a6f6f;
  --accent-soft: #e8f2f0;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font: 17px/1.65 Georgia, "Times New Roman", serif;
  color: var(--ink);
  background: var(--bg);
}
.wrap { display: grid; grid-template-columns: 260px 1fr; min-height: 100vh; }
nav.sidebar {
  border-right: 1px solid var(--line);
  padding: 1.5rem 1.25rem 3rem;
  background: #f3f0e8;
  font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
}
nav.sidebar .brand {
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--accent);
  margin-bottom: .25rem;
}
nav.sidebar .tagline { font-size: .8rem; color: var(--muted); margin-bottom: 1.25rem; }
nav.sidebar ol { list-style: none; margin: 0; padding: 0; counter-reset: ch; }
nav.sidebar li { margin: .15rem 0; counter-increment: ch; }
nav.sidebar a {
  display: block; padding: .3rem .55rem; border-radius: 6px;
  color: var(--ink); text-decoration: none; font-size: .9rem;
}
nav.sidebar a::before { content: counter(ch) ". "; color: var(--muted); font-size: .8rem; }
nav.sidebar a.active, nav.sidebar a:hover {
  background: var(--accent); color: #fff;
}
nav.sidebar a.active::before, nav.sidebar a:hover::before { color: #cfe3e1; }
nav.sidebar .back { margin-top: 1.5rem; font-size: .8rem; }
nav.sidebar .back a { color: var(--muted); }
main {
  max-width: 52rem;
  padding: 2.5rem 3rem 4rem;
}
header.sitetitle { border-bottom: 1px solid var(--line); padding-bottom: 1rem; margin-bottom: 2rem; }
header.sitetitle h1 { font-size: 1.5rem; margin: 0; color: var(--accent); }
header.sitetitle p { margin: .3rem 0 0; color: var(--muted); font-size: .95rem; }
main h2 { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 1.35rem; margin-top: 2.2rem; border-bottom: 1px solid var(--line);
  padding-bottom: .25rem; }
main h3 { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 1.1rem; margin-top: 1.6rem; }
main blockquote {
  margin: 1.2rem 0; padding: .7rem 1.1rem;
  background: var(--accent-soft); border-left: 4px solid var(--accent);
  font-style: italic;
}
main code {
  font: .88rem/1.4 "SFMono-Regular", Consolas, "Liberation Mono", monospace;
  background: #f0ede4; padding: .1em .35em; border-radius: 4px;
}
main pre { background: #2c2f33; color: #e6e6e6; padding: 1rem 1.25rem;
  border-radius: 8px; overflow-x: auto; line-height: 1.55; }
main pre code { background: none; color: inherit; padding: 0; font-size: .85rem; }
main table { border-collapse: collapse; width: 100%; margin: 1.2rem 0;
  font-size: .93rem; }
main th, main td { border: 1px solid var(--line); padding: .45rem .65rem;
  text-align: left; }
main th { background: #f0ede4; }
main a { color: var(--accent); }
main hr { border: none; border-top: 1px solid var(--line); margin: 2.5rem 0 1.5rem; }
footer.pagefoot {
  margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--line);
  color: var(--muted); font-size: .85rem;
  font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
}
@media (max-width: 900px) {
  .wrap { grid-template-columns: 1fr; }
  nav.sidebar { border-right: none; border-bottom: 1px solid var(--line); }
  main { padding: 1.5rem 1.25rem 3rem; }
}
"""


def page_shell(source_name: str, body: str, doc_title: str) -> str:
    """Wrap a rendered Markdown body in the site template."""
    first = PAGES[0]
    nav_items = []
    for i, name in enumerate(PAGES, start=1):
        if name == "index.md":
            label, href = "Start here", "index.html"
            prefix = ""
        else:
            label = name[:-3].replace("-", " ")
            href = name[:-3] + ".html"
            prefix = f"{i - 1}. "
        active = " class=\"active\"" if name == source_name else ""
        nav_items.append(
            f'      <li><a href="{href}"{active}>{prefix}{label}</a></li>'
        )
    nav = "\n".join(nav_items)
    last = i  # pages count, from the loop
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{doc_title} — {TITLE}</title>
<meta name="description" content="{TAGLINE}">
<style>{_CSS}</style>
</head>
<body>
<div class="wrap">
  <nav class="sidebar">
    <div class="brand">{TITLE}</div>
    <div class="tagline">{TAGLINE}</div>
    <ol>
{nav}
    </ol>
    <div class="back"><a href="index.html">← back to start ({last} chapters)</a></div>
  </nav>
  <main>
    <header class="sitetitle">
      <h1>{TITLE}</h1>
      <p>A friendly, budget-first guide from <strong>Asdale Dynamics, LLC</strong>. Education only.</p>
    </header>
{body}
    <footer class="pagefoot">{FOOTER}</footer>
  </main>
</div>
</body>
</html>
"""


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------


def doc_title_of(markdown_text: str, fallback: str = "") -> str:
    match = re.match(r"\s*#\s+(.+)", markdown_text)
    return match.group(1).strip() if match else fallback


def build() -> list[str]:
    """Build the whole site. Returns a list of error strings (empty = OK)."""
    errors: list[str] = []
    issues: list[str] = []

    for name in PAGES:
        path = DOCS / name
        if not path.is_file():
            errors.append(f"missing source doc: {name}")
    if errors:
        return errors

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()

    for name in PAGES:
        raw = (DOCS / name).read_text(encoding="utf-8")
        title = doc_title_of(raw, name[:-3].replace("-", " "))
        body, link_issues = rewrite_links(raw, name)
        issues += [f"link: {e}" for e in link_issues]
        html_body = render_markdown(body)
        page = page_shell(name, html_body, title)
        out = SITE / (name[:-3] + ".html")
        out.write_text(page, encoding="utf-8")

    # a tiny plain copy of the README, for people who end up in site/ first
    (SITE / "README.txt").write_text(
        "This HTML site was generated from the Markdown manuals in docs/ "
        "by build.py\nin the Budget AI PC Guide project. "
        "© Asdale Dynamics, LLC — education only.\n",
        encoding="utf-8",
    )
    return issues


# --------------------------------------------------------------------------
# Verification
# --------------------------------------------------------------------------


def verify(built_pages: dict[str, str]) -> list[str]:
    """Post-build sanity checks. Returns problems found (empty = OK)."""
    problems: list[str] = []

    for name in PAGES:
        out = SITE / (name[:-3] + ".html")
        if not out.is_file():
            problems.append(f"missing built page: {out.name}")
            continue
        content = out.read_text(encoding="utf-8")
        for required in ("<title>", "</body>", "</html>"):
            if required not in content:
                problems.append(f"incomplete page: {out.name} (missing {required})")
        if "Asdale Dynamics" not in content:
            problems.append(f"missing credit on: {out.name}")
        for bad in ("TODO", "FIXME"):
            if bad in built_pages.get(name, ""):
                problems.append(f"placeholder {bad!r} left in {name}")

    # every nav link must resolve to a built page
    for name in PAGES:
        page_text = (SITE / (name[:-3] + ".html")).read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"]+\.html)"', page_text):
            if href.startswith("http"):
                continue
            if not (SITE / href).is_file():
                problems.append(f"{name}: nav/link -> missing {href}")

    return problems


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the Budget AI PC Guide site.")
    parser.add_argument(
        "--check", action="store_true", help="build, then run sanity checks"
    )
    parser.add_argument(
        "--serve", action="store_true", help="build, then serve site/ on :8000"
    )
    args = parser.parse_args(argv)

    if not DOCS.is_dir():
        print(f"error: {DOCS} not found (run this from the project folder)", file=sys.stderr)
        return 2

    issues = build()
    if any(i.startswith("link:") for i in issues):
        print("link problems:", file=sys.stderr)
        for i in issues:
            if i.startswith("link:"):
                print("  " + i, file=sys.stderr)
        return 1
    if issues:
        for i in issues:
            print("note:", i)

    pages_built = {name: (DOCS / name).read_text(encoding="utf-8") for name in PAGES}
    print(f"built {len(PAGES)} pages into {SITE.name}/")

    if args.check:
        problems = verify(pages_built)
        if problems:
            print("check FAILED:", file=sys.stderr)
            for p in problems:
                print("  " + p, file=sys.stderr)
            return 1
        print(f"check passed: pages complete, links resolve, credits present.")

    if args.serve:
        print("serving site/ at http://localhost:8000  (Ctrl+C to stop)")
        http.server.HTTPServer(
            ("127.0.0.1", 8000),
            lambda *h: http.server.SimpleHTTPRequestHandler(
                *h, directory=str(SITE)
            ),
        ).serve_forever()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
