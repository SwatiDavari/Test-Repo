ISO/IEC/IEEE 29119 — Organizational Test Process Requirements
====================================================================

These requirements apply at the **organization level** — independent of
any single product or project — per ISO/IEC/IEEE 29119-2 (Test Processes).
They are prerequisites for the project-level test work under ``test/``
(test basis, conditions, design, procedures, cases, suites, reports).

.. note::
   This file previously contained a duplicate copy of
   ``organisation/governance/functionalsafety/org_fusa_requirements.rst`` (ISO 26262
   organizational safety content, byte-identical) — clearly the wrong
   standard for a file under ``organisation/testing/iso29119/``. Replaced
   with real ISO 29119 organizational test-process content below.

Test Policy
---------------

.. org_req:: Organizational test policy
   :id: ORG_TESTPOLICY_001
   :version: 1.0.0
   :status: draft
   :standard: ISO/IEC/IEEE 29119-2 — Organizational Test Process

   The organization shall define and maintain a test policy stating its
   overall test objectives, the role of testing in the development
   lifecycle, and the minimum test process expected of every project,
   independent of project-specific test strategy choices.

Organizational Test Strategy
---------------------------------

.. org_req:: Organizational test strategy
   :id: ORG_TESTSTRATEGY_001
   :version: 1.0.0
   :status: draft
   :derives_from: ORG_TESTPOLICY_001
   :standard: ISO/IEC/IEEE 29119-2 — Organizational Test Process

   The organization shall define a standard test strategy template
   (test levels, generic entry/exit criteria, defect classification
   scheme) that each project tailors into its own project-level test
   strategy (see ``test/teststrategy/``).

Tester Competence
---------------------

.. org_req:: Tester competence and training
   :id: ORG_TESTCOMP_001
   :version: 1.0.0
   :status: draft
   :derives_from: ORG_TESTPOLICY_001

   The organization shall ensure personnel performing test design,
   execution, and reporting activities have the necessary qualification,
   training, and experience, and shall maintain records of this
   competence — mirroring the safety competence requirement
   (``ORG_COMPETENCE_001``) but scoped to the test discipline.

Test Documentation Standards
---------------------------------

.. org_req:: Organizational test documentation standard
   :id: ORG_TESTDOC_001
   :version: 1.0.0
   :status: draft
   :derives_from: ORG_TESTSTRATEGY_001

   The organization shall define the required test documentation set
   (test plan, test design, test case specification, test procedure,
   test execution log, test completion report) per ISO/IEC/IEEE 29119-3,
   and each project's ``test/`` folder shall populate that set rather
   than inventing its own document types.

Independent Test Function
------------------------------

.. org_req:: Independence of test execution from development
   :id: ORG_TESTINDEPENDENCE_001
   :version: 1.0.0
   :status: draft
   :derives_from: ORG_TESTPOLICY_001

   The organization shall define the minimum degree of independence
   required between those who develop a work product and those who test
   it, scaled to the risk/criticality of the item under test (aligning
   with the safety-relevant independence expectations already established
   for ASIL-rated work under ISO 26262).

Continuous Improvement
---------------------------

.. org_req:: Test process metrics and improvement
   :id: ORG_TESTMETRICS_001
   :version: 1.0.0
   :status: draft
   :derives_from: ORG_TESTSTRATEGY_001

   The organization shall collect test process metrics (e.g. defect
   detection percentage, test coverage, orphan/untested-requirement
   count) across projects and use them to improve the organizational
   test strategy and policy over time. This is the organizational
   counterpart to the project-level metrics tracked in
   ``Needs/quality/metrics/``.
