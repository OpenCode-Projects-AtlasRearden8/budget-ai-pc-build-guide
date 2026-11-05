"""Unit tests for the Budget AI PC Guide site builder.

Run with:  python3 -m unittest discover -s . -p "test_*.py" -v
"""

import pathlib
import tempfile
import unittest

import build as build_mod


class TestLinkRewriting(unittest.TestCase):
    def setUp(self):
        # point the module's DOCS at a scratch dir
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.orig_docs = build_mod.DOCS
        build_mod.DOCS = self.tmp
        for name in ("alpha.md", "beta.md"):
            (self.tmp / name).write_text(f"# {name} some text", encoding="utf-8")

    def tearDown(self):
        build_mod.DOCS = self.orig_docs

    def test_internal_md_link_rewritten_to_html(self):
        body = "see [the beta page](beta.md) and [anchored](alpha.md#section)."
        out, errors = build_mod.rewrite_links(body, "test.md")
        self.assertIn('(beta.html)', out)
        self.assertIn('(alpha.html#section)', out)
        self.assertEqual(errors, [])

    def test_missing_link_reported(self):
        out, errors = build_mod.rewrite_links("see [x](nope.md)", "test.md")
        self.assertEqual(out, "see [x](nope.md)")
        self.assertEqual(len(errors), 1)
        self.assertIn("nope.md", errors[0])

    def test_external_links_left_alone(self):
        body = "read [the docs](https://example.com/page.md)"
        out, errors = build_mod.rewrite_links(body, "test.md")
        self.assertEqual(out, body)
        self.assertEqual(errors, [])

    def test_non_md_target_flagged(self):
        _, errors = build_mod.rewrite_links("see [x](folder)", "test.md")
        self.assertEqual(len(errors), 1)

    def test_links_inside_code_fences_left_alone(self):
        body = "```\n[clicked](alpha.md)\n```"
        out, errors = build_mod.rewrite_links(body, "test.md")
        self.assertEqual(out, body)
        self.assertEqual(errors, [])


class TestMarkdownAndTitles(unittest.TestCase):
    def test_heading_becomes_h1_heading(self):
        html = build_mod.render_markdown("# Hello\n\nBody text.")
        self.assertIn(">Hello</h1>", html)
        self.assertIn("<p>Body text.</p>", html)

    def test_bold_italic_code(self):
        html = build_mod.render_markdown("a **loud** *quiet* `base`")
        self.assertIn("<strong>loud</strong>", html)
        self.assertIn("<em>quiet</em>", html)
        self.assertIn("<code>base</code>", html)

    def test_fenced_code_block(self):
        html = build_mod.render_markdown("```\nx = 1\n```")
        self.assertIn("<pre>", html)
        self.assertIn("x = 1", html)

    def test_table(self):
        html = build_mod.render_markdown(
            "| a | b |\n|---|---|\n| 1 | 2 |"
        )
        self.assertIn("<table>", html)

    def test_doc_title_extracted_from_first_heading(self):
        self.assertEqual(
            build_mod.doc_title_of("# The Price Guide\n\nbody"),
            "The Price Guide",
        )
        self.assertEqual(build_mod.doc_title_of("no heading"), "")


class TestPageShell(unittest.TestCase):
    def test_shell_contains_nav_and_credit(self):
        html = build_mod.page_shell(
            "index.md", "<h1>hi</h1>", "Title"
        )
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn('href="old-laptop-first.html"', html)
        self.assertIn("Asdale Dynamics, LLC", html)
        self.assertIn("</html>", html)

    def test_active_page_marked(self):
        html = build_mod.page_shell("glossary.md", "<h1>hi</h1>", "Title")
        self.assertIn('href="glossary.html" class="active"', html)


class TestDocsIntegrity(unittest.TestCase):
    """Integration-ish checks over the real docs/ folder."""

    def test_all_pages_present(self):
        for name in build_mod.PAGES:
            self.assertTrue(
                (build_mod.DOCS / name).is_file(), f"missing {name}"
            )

    def test_real_build_passes_check(self):
        issues = build_mod.build()
        real_errors = [i for i in issues if not i.startswith("link:")]
        self.assertEqual(real_errors, [])
        built = {name: (build_mod.DOCS / name).read_text(encoding="utf-8")
                 for name in build_mod.PAGES}
        problems = build_mod.verify(built)
        self.assertEqual(problems, [], str(problems))

    def test_every_md_file_is_in_reading_order(self):
        on_disk = sorted(p.name for p in build_mod.DOCS.glob("*.md"))
        self.assertEqual(
            sorted(build_mod.PAGES), on_disk, "PAGES list and docs/ disagree"
        )

    def test_each_doc_links_to_something_else(self):
        for name in build_mod.PAGES:
            text = (build_mod.DOCS / name).read_text(encoding="utf-8")
            if name != "index.md":
                self.assertRegex(
                    text, r"\]\([a-z-]+\.md", f"{name} has no cross-links"
                )


if __name__ == "__main__":
    unittest.main()
