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
   already used by the sibling ``teststrategy`` and ``testreports``
   files in this folder — and pointed at requirements that actually exist
   in this repo. The ID ``TC_SYS_STARTUP_001`` is kept because
   ``test suites/suite_release_smoke.yml`` already references it.

``TC_SYS_STARTUP_001`` — system-level startup verification for
``sys_msgdisc_001``: with the entry condition in
``test conditions/tcond_startup_001.yml`` satisfied, confirm both of
``sys_msgdisc_001``'s features come up correctly — the Communication module
(``feat_a_001``) establishes its publish-subscribe channel and the
Diagnostics module (``feat_z_001``) completes service registration —
following the steps recorded in
``test procedures/proc_sys_startup_001.yml``.

Owner: validation team. Status: approved.

.. note::
   **2026-08-22: resolved the dangling references flagged below (kept
   for history).** ``test conditions/tcond_startup_001.yml`` and
   ``test procedures/proc_sys_startup_001.yml`` didn't actually exist
   anywhere in this repo (confirmed against full git history) — there
   was no old OTA-scenario content to correct, only a reference to files
   that had never been created. Created both, with real
   startup-verification content matching this test case's actual
   subject (``sys_msgdisc_001``/``feat_a_001``/``feat_z_001``). Also corrected
   ``test basis/basis.yml`` in the same pass, which did exist but still
   carried the same stale ``SYSR_*`` placeholder IDs referenced above —
   now lists ``sys_msgdisc_001``/``feat_a_001``/``feat_z_001`` instead.

   *Original note, now resolved*: ``test conditions/tcond_startup_001.yml``
   and ``test procedures/proc_sys_startup_001.yml`` still described the
   old OTA-update scenario (signal-router, logging-service, firmware
   flashing) rather than this test case's actual subject — referenced
   here by ID for consistency with ``test suites/suite_release_smoke.yml``,
   not because their own content had been corrected yet. That rewrite
   was flagged as a known gap, not silently fixed — now done, together
   with ``test basis/basis.yml``.

.. note::
   **2026-08-22, separately:** the entry condition/procedure text above
   also still said plain ``SYS_001`` in a few places — that ID is not
   actually defined anywhere in ``needs/`` (confirmed by scanning every
   ``:id:`` in the project); the real system-level need is
   ``sys_msgdisc_001`` (see ``needs/systemslifecycle/index.rst``).
   Corrected here and in ``test strategy/product-verification-strategy.rst``
   and ``test basis/basis.yml``.
