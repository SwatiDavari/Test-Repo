Changelog
============

Dated history of structural/theme changes to this documentation site.
Split out of ``index.rst`` on 2026-08-21 so that page stays short — see
each dated entry below for the full rationale behind a given change.

2026-08-21: four top-level entries
------------------------------------

Collapsed the root sidebar to four top-level entries — Organization,
Product / Program, Decision Records, User Guide — per a request for one
main menu each, everything else nested as collapsible sub-menus.

"Product / Program" is new — see :doc:`product/index` for what moved
under it (management, a new architecture placeholder, this repo's own
``testing/`` folder, source, this project's needs types, and a link into
``needs/``) and its own disclosed divergences from the original sketch.

"User Guide" is new too, and is a link into ``needs/user_guide/`` — see
that project's own ``needs/user_guide/index.rst`` (a separate Sphinx
project; not cross-referenceable from here) for why the product/safety
user manuals live there now instead of under ``doc/``.

The previously-broken ``integration test/index`` toctree entry is
removed (that folder no longer exists on disk — still showing as
deleted, uncommitted, in ``git status``; unresolved, flagging separately
rather than guessing whether to restore it).

2026-08-21: single "Organization" entry
-------------------------------------------

Collapsed three separate top-level entries (``organisation/governance/
index``, ``organisation/strategy/index``, ``organisation/common_framework/
index``) into one: ``organisation/index``, a new landing page added
directly in org-processes, per a request to make the top nav show one
"Organization" entry with everything else nested underneath as
collapsible sub-menus.

Getting there required going back into org-processes and converting its
remaining prose-link pages (``governance/framework/index.rst``,
``strategy/index.rst``) to real toctrees, and adding toctree entries for
two previously-orphaned sections that had no parent at all
(``governance/policies/`` — three policy pages that existed on disk but
weren't linked from anywhere; ``testing/index.rst``,
``infrastructure/index.rst``, and ``learning_management/index.rst`` —
new landing pages, the latter two honest placeholders since those
folders hold no real content yet). See :doc:`organisation/index`'s own
note for the divergences between this structure and the original
sketch.

2026-08-21: organisation/ populated in CI
---------------------------------------------

``.github/workflows/docs.yml`` and ``ci-needs.yml`` check out the real
``org-processes`` repo (https://github.com/SwatiDavari/org-processes)
and run ``scripts/sync_org_content.sh`` before building. Verified
against that repo's actual content: the ``needs/`` project's
``-W``-gated build (``ci-needs.yml``) dropped from 5 warnings to 1 once
the real ``org_req`` IDs (``ORG_SMS_001``, ``ORG_CYBERSEC_TOOL_001``,
``ORG_TOOLCFG_001``, ``ORG_TOOLQUAL_001``) became resolvable — the one
warning left is unrelated, a pre-existing broken ``verifies`` link
inside this repo's own communication module.

This still only runs automatically in CI. Building this project locally
still needs a local checkout of ``org-processes`` and a manual run of
``scripts/sync_org_content.sh`` first — see ``getting_started.rst``.

2026-08-21: switched from Furo to sphinx-immaterial
--------------------------------------------------------

Briefly via pydata-sphinx-theme first, to match the navigation flow of
Qorix's Performance Documentation site — top navbar generated from this
page's top-level toctree entries, each pointing at one section landing
page whose *own* toctree drives that section's secondary sidebar. This
replaces the previous Furo-specific workaround (Furo's sidebar always
rendered at full depth regardless of ``:maxdepth:``, so every child page
used to be listed flat here instead of nested in its own section's
landing page). pydata-sphinx-theme got the same navigation structure
working first; sphinx-immaterial was chosen over it after a side-by-side
comparison on this content, for its search/dark-mode/polish. Content is
unchanged — only where each page is linked from and which theme renders
it.

2026-08-21: added Score (score.dev) doc-site UX patterns
-------------------------------------------------------------

Score's docs (docs.score.dev) run on Docusaurus, a different stack from
this Sphinx + sphinx-needs setup — kept the traceability tooling and
only pulled over what maps onto sphinx-immaterial's actual, verified
feature flags: the pencil/eye icons next to each page title now link to
"edit this page" / "view page source" on GitHub (``edit_uri`` was
previously empty, which silently disabled both), search now offers
autocomplete-style suggestions, and long pages get a back-to-top button.
The Qorix palette (see ``_static/custom.css``) was checked against WCAG
contrast: white on the navy header is 13.95:1, and the purple
link/accent color on white body text is 7.97:1 — both comfortably above
the 4.5:1 AA minimum for normal text.

**Not implemented, and why**: Score's breadcrumb trail and per-page "N
minute read" are Docusaurus features with no equivalent in this
sphinx-immaterial fork — no ``navigation.path``/breadcrumb template
exists in the installed package. A "last updated" date (which
sphinx-immaterial does support, via ``html_last_updated_fmt``) was
deliberately left off too: GitHub Actions' checkout resets every file's
modification time to the CI run's checkout moment, so it would show
today's date on every single page regardless of when that page was
actually last edited — worse than not showing a date at all. Getting a
real per-page date would need a custom extension reading git log per
file, which needs a non-shallow checkout; flagging as a possible
follow-up rather than building it half-right.
