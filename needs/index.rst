Qorix Engineering Processes — Needs
====================================

Product traceability graph for this repo: system, feature, component, and
unit requirements, plus the safety chain (safety goal / FSR / TSR). This is
a **separate** Sphinx-needs project from the repo root (see ``../conf.py``
and ``../README.md``) — organizational governance content
(``org_req``/``risk``/``problem``/``change``/``exception``/``tool``/
``infra``) lives there, not here.

``master_doc`` was set to ``index`` without this file existing, which made
every build of this project — including the ``-W`` hard-gated build in
``.github/workflows/ci-needs.yml`` — crash with "Sphinx is unable to load
the master document," regardless of any need content. Found and fixed
while verifying the sys_msgdisc_001 fix end-to-end with a real build; see
README.md's "Known gaps" for how this was found.

Found while verifying the named-link change below with a real ``-W``
build (not previously caught): this toctree only wired in
``systemslifecycle/index`` plus one document each from Communication and
Diagnostics, so every other real page in this project — both modules'
own ``index.rst``, ``cybersecurity/``, ``functionalsafety/``,
``quality/``, the three pre-requirements pages, and
``needs_types_definition.rst`` — was building but unreachable from here,
which fails ``-W`` on ``toc.not_included`` for each one. Fixed below by
wiring in the module-level index pages (which already cascade down to
their own children) instead of individual leaf documents, plus the
pages that had no parent at all.

**Reorganized 2026-08-21: grouped by discipline instead of by product
module.** The captions below used to be module-first (``Communication``,
``Diagnostics``, ``Cybersecurity``, ``Functional Safety`` as five flat
siblings). They're now discipline-first, following the same Project
Level / discipline grouping used by Qorix's own Performance
Documentation site (Project Management / Quality / Roles / Safety /
Security, with product detail nested inside, not listed alongside):
``communication/`` and ``diagnostics/`` moved under a new ``software/``
discipline (both are ASPICE SWE.1-3 product requirement chains —
"Software" in that framework's terms); ``functionalsafety/`` renamed to
``safety/``; ``cybersecurity/`` renamed to ``security/``. ``systemslifecycle/``
(Systems Engineering, SYS.1-5) and ``quality/`` stay top-level, same as
before — they were already their own disciplines, not product modules.
No need IDs changed; this is a folder/toctree move only. See
``README.md``'s "Need ID naming convention" section and this project's
autosar/eclipse-score conversion notes for the ID scheme itself.

**2026-08-21: switched to sphinx-immaterial** (see ``conf.py``), after
first trying pydata-sphinx-theme, to match the Performance Documentation
site's navbar-driven look and feel — sphinx-immaterial was picked after a
side-by-side comparison on this project's real content for its sharper
UI (instant search, dark mode, sticky tabs). Unlike pydata-sphinx-theme's
navbar-nav (which turns each top-level toctree *entry* into its own tab
using that entry's own page title — so a caption with more than one
entry, like ``Software`` with two, would leak the first child's title
into the tab instead of showing "Software"), sphinx-immaterial's tabs
correctly group by ``:caption:``. ``software/index.rst`` was still added
as a real landing page for that discipline — it's a better structure on
its own merits regardless of theme, not just a workaround.

**2026-08-21: added Score (score.dev) doc-site UX patterns** — see
``../index.rst`` for the full rationale, the WCAG contrast numbers for
the Qorix palette, and what was deliberately left out (breadcrumbs,
per-page reading time) and why. Same ``conf.py`` changes apply here:
working edit/view-source icons (``edit_uri`` now points at
``edit/main/needs`` — this project's srcdir is ``needs/``, not the repo
root, so the prefix has to be explicit or the generated GitHub link
404s), search suggestions, and a back-to-top button.

.. toctree::
   :hidden:

   needs_types_definition

.. toctree::
   :maxdepth: 1
   :caption: Pre-requirements input

   stakeholder-needs
   business-needs
   operational-needs

.. toctree::
   :maxdepth: 2
   :caption: System

   systemslifecycle/index

.. toctree::
   :maxdepth: 1
   :caption: Software

   software/index

.. toctree::
   :maxdepth: 1
   :caption: Safety

   safety/index

.. toctree::
   :maxdepth: 1
   :caption: Security

   security/index

.. toctree::
   :maxdepth: 1
   :caption: Quality

   quality/index
