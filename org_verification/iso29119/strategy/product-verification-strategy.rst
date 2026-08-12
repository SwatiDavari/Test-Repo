Organizational Test Strategy Template
===========================================

.. note::
   This file previously contained a byte-identical copy of
   ``test/test-strategy/product-verification-strategy.rst``, including
   product-specific requirement IDs (``SYSR_OTA_010`` etc.) that don't
   exist anywhere in this repo — the wrong content for an
   organization-level template, which by definition must not be tied to
   any one product. Rewritten below as the generic template
   ``ORG_TESTSTRATEGY_001`` actually requires; see
   :doc:`../organizational_requirements` for that requirement's text.

Purpose
-------

This is the organization-level test strategy **template** referenced by
``ORG_TESTSTRATEGY_001`` — the structure every project tailors into its
own project-level test strategy (see, for example,
``test/test-strategy/product-verification-strategy.rst``). It defines
test levels, generic entry/exit criteria, and a defect classification
scheme; it does not itself reference any product's requirements.

Test Levels
-----------

- **Unit** — verifies a single component in isolation (see
  ``source/<lang>/tests/``).
- **Integration** — verifies interaction between components within one
  module.
- **System** — verifies system-level requirements end to end against a
  built product image, independent of any single component's internal
  structure.

Generic Entry Criteria
------------------------

- The item under test builds successfully.
- Test basis (the requirements the test level verifies) is approved.
- Test environment and tooling are available.

Generic Exit Criteria
------------------------

- All planned test cases for the level have been executed.
- No open defect above the project's defined severity threshold.
- Results are recorded in a test completion report.

Defect Classification Scheme
--------------------------------

- **Critical** — safety-relevant or blocks release.
- **Major** — functional defect, workaround exists.
- **Minor** — cosmetic or non-blocking.
