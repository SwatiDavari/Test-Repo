Product Test Cases
=====================

.. note::
   This file previously used an unregistered ``.. test_case::``
   directive (no ``test_case`` need type is registered in this or any
   ``conf.py`` in this repo — that's an ``Unknown directive type`` build
   error, not just a warning, and Sphinx silently dropped the whole block
   from the published page) and described verifying nonexistent
   ``SYSR_OTA_010``/``SYSR_OTA_SAFE_014`` requirements for a ``PROD_X``
   product. Rewritten below as plain narrative, matching the convention
   already used by the sibling ``test-strategy`` and ``test-reports``
   files in this folder — and pointed at requirements that actually exist
   in this repo. The ID ``TC_SYS_STARTUP_001`` is kept because
   ``test/test-suites/SUITE_RELEASE_SMOKE.yml`` already references it.

``TC_SYS_STARTUP_001`` — system-level startup verification for
``SYS_001``: with the entry condition in
``test/test-conditions/TCOND_STARTUP_001.yml`` satisfied, confirm both of
``SYS_001``'s features come up correctly — the Communication module
(``FEAT_A_001``) establishes its publish-subscribe channel and the
Diagnostics module (``FEAT_Z_001``) completes service registration —
following the steps recorded in
``test/test-procedures/PROC_SYS_STARTUP_001.yml``.

Owner: validation team. Status: approved.

.. note::
   ``test/test-conditions/TCOND_STARTUP_001.yml`` and
   ``test/test-procedures/PROC_SYS_STARTUP_001.yml`` still describe the
   old OTA-update scenario (signal-router, logging-service, firmware
   flashing) rather than this test case's actual subject — they're
   referenced here by ID for consistency with
   ``test/test-suites/SUITE_RELEASE_SMOKE.yml``, not because their own
   content has been corrected yet. That rewrite is a separate, larger
   pass across ``test/test-basis/``, ``test-conditions/``,
   ``test-procedures/``, ``test-suites/``, ``executions/``, and
   ``test-reports/`` — flagged here as a known gap, not silently fixed.
