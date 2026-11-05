# Status: Budget AI PC Guide

**Last updated:** November 5, 2026 — working, tested, committed.

## What was built

A complete beginner manual for building an affordable **used-parts PC that runs local AI**, in a warm plain-English voice, plus a small Python script that renders the manuals into a self-contained static HTML site. Education-only throughout: no product endorsements, no affiliate or sales angle, no secrets or personal data anywhere.

**Eleven Markdown manuals** in `docs/` (the source of truth):

| Doc | What it covers |
|---|---|
| `index.md` | Orientation: what running AI locally means, reading order, promises |
| `old-laptop-first.md` | Honest "test your existing machine before spending" advice |
| `parts-explained.md` | All 8 parts in plain English, with the "graphics card = thinking engine" framing |
| `price-targets.md` | Part-by-part price ceilings, three total budgets ($300 / $450–500 / $700–800), red flags |
| `silent-vs-speed.md` | The noise/heat/performance tradeoff, fan buying, power-limit trick |
| `ram-and-vram.md` | RAM vs VRAM, the 0.6 GB-per-billion-parameter rule, offloading explained |
| `shopping-worksheet.md` | Fill-in worksheet, red-flag checklist, seller questions |
| `first-boot-checklist.md` | Assembly order, grounding, the two classic mistakes, power-on checks |
| `ollama-install-day.md` | Installing Ollama, first model pull, expectations, chat interfaces |
| `upkeep.md` | Monthly 5-minute routine (dust, updates, backups), failure flowchart |
| `glossary.md` | Every term defined once, in reading order |

**One static-site builder** — `build.py`:

- Renders `docs/*.md` → `site/*.html` in reading order with a sidebar nav
- Rewrites internal `.md` links to `.html` (skipping fenced code blocks)
- Full CSS embedded in each page: works offline, no JS, no external requests
- `--check` mode: link resolution, page completeness, credit presence
- `--serve` mode: local preview at `http://localhost:8000`

**Supporting files:** `README.md` (credits Asdale Dynamics, LLC), `LICENSE` (MIT, "Copyright (c) 2026 Asdale Dynamics, LLC"), `test_build.py` (16 unit tests).

## How to run it

```bash
python3 -m pip install markdown   # one-time dependency (pure Python)
python3 build.py                  # build site/
python3 build.py --check          # build + verify
python3 build.py --serve          # build + preview at http://localhost:8000
python3 -m unittest discover -s . -p "test_*.py" -v   # test suite
```

## Verification results (all green)

- `python3 build.py --check` → **built 11 pages into site/; check passed** (pages complete, links resolve, credits present)
- `python3 -m unittest` → **16 tests OK** (link rewriting incl. code-fence skipping, markdown rendering, nav shell, real-build integration, docs coverage)
- `python3 build.py --serve` smoke-tested → HTTP 200 on `/index.html` and `/glossary.html`
- Manual inspection confirmed tables, fenced code blocks, and emphasis render correctly; no raw markdown artifacts in output

## Known gaps / honest limitations

- **Price figures are ranges, not quotes.** They're framings ("ceilings to refuse to cross"), not live market data, and are USD-oriented. Intentional — the used market changes weekly; updating them would make them false.
- **No specific hardware is endorsed by design.** Readers get *classes* and *characteristics* to shop for, not model names. That's a deliberate editorial choice, not an oversight.
- **Markdown dependency:** the builder needs the `pip`-installable `markdown` package. There's a friendly error message if it's missing, but no bundled fallback renderer.
- **Plain HTML only:** no site search, no dark mode, no print stylesheet. Fine for a 11-page offline guide.
- **No screenshots/images.** The hardware chapters describe physical steps textually; photos would help the assembly chapter but weren't part of this build.
- `site/` is regenerated on each build (`build.py` wipes and rewrites it), so changes to `docs/` must be followed by a rebuild.

## Identity notes

- All commits made with the existing local git identity (Dylan Asdale), plain messages, no co-author trailers; nothing pushed, no remotes.
- No secrets, API keys, or personal data in any file.
