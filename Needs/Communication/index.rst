Module A — Publish/Subscribe Messaging
========================================

.. toctree::
   :maxdepth: 1

   process_description
   feature/index
   component/index

.. note::
   ``unit design/`` and ``unit test/`` live under ``component/`` (see
   :doc:`component/index`), not here — this toctree previously pointed
   at ``unit design/unit_a_001`` and ``unit test/index`` directly at the
   module level, which don't exist at that path (the real files are
   nested one level deeper, under ``component/``); those two lines were
   stale, fixed by removing them here and wiring both into
   ``component/index.rst`` instead, matching how
   ``diagnostics/component/index.rst`` already does it.

.. note::
   The Module A Safety User Manual lives under published documentation,
   not here — see ``doc/manuals/safety/safety_user_manual.rst`` (built
   standalone via ``build_safety_manual_pdf.sh`` /
   ``.github/workflows/safety_user_manual_pdf.yml``). A duplicate copy
   previously lived at this path (``safety_user_manual.rst``, identical
   content) and has been removed — traceability content belongs in
   ``Needs/``, published manuals belong in ``doc/``, not both.
