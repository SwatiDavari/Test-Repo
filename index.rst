Qorix Engineering Processes
===========================

This is the root-level documentation project for Qorix Engineering Processes. It covers
organizational governance and project process; the product traceability
graph (system/feature/component/unit requirements, safety chain) lives in
``needs/`` as a **separate** Sphinx project — build it independently from
inside ``needs/`` (``sphinx-build -b html . _build``). See ``STANDARDS.md``
for how each folder maps onto ASPICE / ISO 15288 / ISO 26262 / ISO 29119
terminology. Published documentation lives under ``doc/`` (``manuals/``,
``tutorials/``, ``reference/``, ``release_notes/``, ``errata/`` — see
``doc/README.md``); it's plain Markdown, not part of this Sphinx build.

.. note::
   **2026-08-21: switched from Furo to sphinx-immaterial** (briefly via
   pydata-sphinx-theme first) to match the navigation flow of Qorix's
   Performance Documentation site — top navbar generated from this page's
   top-level toctree entries, each pointing at one section landing page
   whose *own* toctree drives that section's secondary sidebar. This
   replaces the previous Furo-specific workaround (Furo's sidebar always
   rendered at full depth regardless of ``:maxdepth:``, so every child
   page used to be listed flat here instead of nested in its own
   section's landing page). pydata-sphinx-theme got the same navigation
   structure working first; sphinx-immaterial was chosen over it after a
   side-by-side comparison on this content, for its search/dark-mode/
   polish. Content is unchanged — only where each page is linked from and
   which theme renders it.

   **Known, pre-existing gap, not introduced by this change**:
   ``organisation/governance/index``, ``organisation/strategy/index``, and
   ``organisation/common_framework/index`` below don't resolve locally.
   ``organisation/`` is gitignored and populated at build time from a
   sibling ``Org_processes`` repo by ``scripts/sync_org_content.sh`` (see
   that script and ``.gitignore``) — neither this checkout nor
   ``.github/workflows/docs.yml``/``ci-needs.yml`` currently run it, so
   these three sections build as broken links today regardless of theme.
   Previously this showed up as ~20 separate "unknown document" warnings
   (one per file that used to be listed directly here); collapsing each
   section down to its one real landing-page reference doesn't fix the
   underlying gap, just reduces the noise to one clear warning per
   missing section instead of one per file that was never there.

   **2026-08-21: added Score (score.dev) doc-site UX patterns.** Score's
   docs (docs.score.dev) run on Docusaurus, a different stack from this
   Sphinx + sphinx-needs setup — kept the traceability tooling and only
   pulled over what maps onto sphinx-immaterial's actual, verified feature
   flags: the pencil/eye icons next to each page title now link to
   "edit this page" / "view page source" on GitHub (``edit_uri`` was
   previously empty, which silently disabled both), search now offers
   autocomplete-style suggestions, and long pages get a back-to-top
   button. The Qorix palette (see ``_static/custom.css``) was checked
   against WCAG contrast: white on the navy header is 13.95:1, and the
   purple link/accent color on white body text is 7.97:1 — both comfortably
   above the 4.5:1 AA minimum for normal text.

   **Not implemented, and why**: Score's breadcrumb trail and per-page
   "N minute read" are Docusaurus features with no equivalent in this
   sphinx-immaterial fork — no ``navigation.path``/breadcrumb template
   exists in the installed package. A "last updated" date (which
   sphinx-immaterial does support, via ``html_last_updated_fmt``) was
   deliberately left off too: GitHub Actions' checkout resets every
   file's modification time to the CI run's checkout moment, so it would
   show today's date on every single page regardless of when that page
   was actually last edited — worse than not showing a date at all.
   Getting a real per-page date would need a custom extension reading
   git log per file, which needs a non-shallow checkout; flagging as a
   possible follow-up rather than building it half-right.

.. toctree::
   :maxdepth: 1

   getting_started
   organisation/governance/index
   organisation/strategy/index
   organisation/common_framework/index
   management/index
   integration test/index
   decision records/decision_register
   needs_types_definition
