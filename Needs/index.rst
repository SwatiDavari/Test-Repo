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
while verifying the SYS_001 fix end-to-end with a real build; see
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
   :caption: Communication

   communication/index

.. toctree::
   :maxdepth: 1
   :caption: Diagnostics

   diagnostics/index

.. toctree::
   :maxdepth: 1
   :caption: Cybersecurity

   cybersecurity/index

.. toctree::
   :maxdepth: 1
   :caption: Functional Safety

   functionalsafety/index

.. toctree::
   :maxdepth: 1
   :caption: Quality

   quality/index
