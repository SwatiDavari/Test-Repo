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
