User Guide
=============

Customer-facing product documentation: the general product user manual
and the ISO 26262-6 Safety User Manual for Module A. Lives inside this
(``needs/``) project rather than the repo root because the Safety User
Manual's traceable content (``safefeat``/``rec``/``res``) is modeled as
real needs linking into this project's own FSR/TSR/safety-goal chain —
see ``needs_types_definition.rst``.

**2026-08-21: moved here from ``doc/manuals/`` at the repo root.** Both
pages previously lived there and were picked up by the *root* project's
Sphinx build by accident (nothing excluded ``doc/`` from its source
scan), which doesn't register ``safefeat``/``rec``/``res`` — every build
of the root project threw "Unknown directive type" errors on
``safety_user_manual.rst``, and both pages sat outside any toctree
either way. Moving them here fixes both problems at once: they use a
schema that's actually registered, and their ``:links:``/``:need:``
references (``TSR_001``, ``SG_001``, ``FSR_001``, ``COMP_A_001``) now
resolve against real needs already defined elsewhere in this project.

The Pandoc-to-PDF pipeline for ``user_manual.rst``
(``.github/workflows/user_manual_pdf.yml``) moved with it — see that
workflow and ``doc/README.md`` at the repo root.

.. toctree::
   :maxdepth: 1

   user_manual
   safety/safety_user_manual
