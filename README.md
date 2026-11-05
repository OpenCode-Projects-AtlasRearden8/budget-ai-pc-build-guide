# The Budget AI PC Guide

*A friendly manual for building an affordable, used-parts PC that runs AI locally — plain English, budget ceilings, no hype.*

By **Asdale Dynamics, LLC** — the plain-English AI education folks behind *The Massive AI Manual* and [dylanasdale.github.io](https://dylanasdale.github.io). This project teaches the **hardware** side of local AI: what each part does, what it should cost, the quiet-vs-fast tradeoff, how RAM and VRAM decide which models can run, and what to do on Ollama install day. It is deliberately **distinct from** the local-AI handbook project, which covers *daily usage* of local AI rather than the machine it lives on.

Everything in these manuals is education only: we explain categories, tradeoffs, and ranges — never "buy this exact product," and never a word aimed at selling you something.

## Read the guide

The manuals live in [`docs/`](docs/), generated into a small static HTML site in [`site/`](site/). Start with [docs/index.md](docs/index.md), which points you through the chapters in order:

1. Try your old laptop first (the honest money-saver)
2. What each part does — eight parts, plain English
3. How much to spend — part-by-part price ceilings, three total budgets
4. Quiet or fast? — the silence-vs-speed tradeoff
5. RAM and VRAM, explained — the numbers that decide everything
6. The shopping worksheet — print it, fill it, refuse red flags
7. Build day and first boot — assembly order and checklists
8. Ollama install day — your first local model
9. Keeping it healthy — the five-minute monthly routine
10. Glossary — every term, defined once

## Build the website locally

This project is fully local: the site builds offline with one small Python script, no frameworks and no downloads.

```bash
# one-time dependency (pure-Python, small, no network calls at build time)
python3 -m pip install markdown

# build docs/ -> site/
python3 build.py

# build + verify (link checks, page completeness, credits present)
python3 build.py --check

# build + preview in your browser at http://localhost:8000
python3 build.py --serve
```

Run the test suite with:

```bash
python3 -m unittest discover -s . -p "test_*.py" -v
```

## Project layout

```
docs/     the manuals (Markdown, the source of truth)
site/     generated HTML — safe to delete, rebuilt by build.py
build.py  the site builder (markdown -> HTML, nav, link checks)
test_build.py  unit tests for the builder
LICENSE   MIT (Copyright (c) 2026 Asdale Dynamics, LLC)
```

The generated `site/` folder is plain HTML — copy it to a USB stick, open it directly in a browser, or drop it on any static host. No JavaScript, no third-party requests, no analytics.

## Who it's for

People who want local AI on a real budget: beginners turning one idea into one machine, nurses and small-business owners and tinkerers who'd rather understand the parts than trust a sales page. If you want the friendly plain-English approach to *using* AI tools (agents, MCP, privacy, automation — not hardware), that lives in the other Asdale Dynamics manuals.

## License

MIT — free to read, share, adapt, and build on. © Asdale Dynamics, LLC. No API keys, no personal data, no telemetry: everything here runs and builds offline.
