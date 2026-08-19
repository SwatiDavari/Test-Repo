Safety User Manual — Module A (Communication Manager)
========================================================

.. note::

   This page is the Sphinx-Needs equivalent of the
   ``Qorix_SafetyUserManual.docx`` template previously hand-maintained per
   module. The narrative sections (Introduction, Reference Documents,
   Conventions) stay as plain reStructuredText — only the traceable
   content (safety features, recommendations, restrictions) is modeled as
   needs, so it links directly into the existing FSR/TSR chain instead of
   living as an unlinked Word table. See ``needs_types_definition.rst`` for
   the ``safefeat`` / ``rec`` / ``res`` directive definitions this page
   uses, and the root ``STANDARDS.md`` for how this maps to ISO 26262-6.

Revision History
-----------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 15 15 20

   * - Version
     - Change Description
     - Prepared/Modified By
     - Approved By
     - Date of Approval
   * - 1.0.0
     - Initial Sphinx-Needs version, migrated from
       ``Qorix_SafetyUserManual.docx`` v1.2.0
     - <name>
     - <name>
     - <yyyy-mm-dd>

Introduction
-------------

Purpose and Scope
~~~~~~~~~~~~~~~~~~

This document provides the safety features of the Communication Manager
(Module A) and its use in the context of a safety-related system. It
describes user responsibilities for safe integration of Module A in
safety systems, in order to maintain the assigned safety integrity level.

Module A is implemented according to the recommendations of ISO 26262 for
ASIL D, as a Safety Element out of Context (SEooC) within QORIX Classic.

This document is additional to the Module A Integration User Manual and
covers only safety-relevant information.

Acronyms, Abbreviations and Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 20 70

   * - Sl. No.
     - Acronym
     - Description
   * - 1
     - ASIL
     - Automotive Safety Integrity Level
   * - 2
     - DFMEA
     - Design Failure Mode and Effect Analysis
   * - 3
     - FFI
     - Freedom From Interference
   * - 4
     - SEooC
     - Safety Element out of Context
   * - 5
     - SUM
     - Safety User Manual

Reference Documents
---------------------

Controlling Documents/Artifacts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 70 20

   * - Sl. No.
     - Title
     - Version
   * - 1
     - Qorix_CP_ModuleA_SoftwareRequirementSpecification.xlsx
     - <x.y.z>
   * - 2
     - Qorix_CP_ModuleA_DesignFailureModeAndEffectsAnalysis.xlsx
     - <x.y.z>

Reference Documents
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 70 20

   * - Sl. No.
     - Title
     - Version
   * - 1
     - ISO 26262-6
     - 2018
   * - 2
     - ISO 26262-7
     - 2018

About QORIX Classic — Module A
---------------------------------

Safety Architecture
~~~~~~~~~~~~~~~~~~~~

Module A (Communication Manager) implements a publish-subscribe messaging
layer (``COMP_A_001``) whose safety behavior is governed by
``FSR_001``/``TSR_001`` — see :need:`TSR_001` for the technical safety
concept this feature realizes.

.. safefeat:: Subscriber Authorization Enforcement
   :id: SAFEFEAT_A_001
   :version: 1.0.0
   :status: approved
   :links: TSR_001
   :rationale: Prevents actuation from messages delivered to an
      unauthorized subscriber, which could otherwise trigger an
      unintended actuation (see SG_001).
   :use_case: Any deployment where Module A delivers messages to
      safety-relevant application instances.
   :dependency: Requires the platform's identity/token service to be
      configured and reachable at startup.

   The Communication Manager rejects message delivery to any subscriber
   whose authorization token has not been validated for the current
   session.

Safety Interfaces
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Module API
     - Supported Safety Feature
   * - ``Subscribe()``
     - :need:`SAFEFEAT_A_001`
   * - ``Publish()``
     - :need:`SAFEFEAT_A_001`

Safety Configurations
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 20 35 20

   * - Config Parameter Name
     - Supported Safety Feature
     - Recommended Values
     - Dependencies
   * - ``AuthTokenRequired``
     - :need:`SAFEFEAT_A_001`
     - ``True`` (default) — subscriber authorization is enforced;
       ``False`` — authorization check is bypassed (not permitted at
       ASIL D)
     - None

Operational Safety
--------------------

Assumption of Use
~~~~~~~~~~~~~~~~~~~

This section specifies recommendations and restrictions, along with
probable mitigations, to be considered at the time of module
integration. The impacts listed are the potential effects of
non-adherence to the recommended action.

Recommendation
^^^^^^^^^^^^^^^^

.. rec:: Configure the identity service before first Subscribe() call
   :id: REC_A_001
   :version: 1.0.0
   :status: approved
   :links: SAFEFEAT_A_001
   :input_reference: FSR_001
   :req_type: Configuration
   :actions: Ensure the platform identity/token service is configured
      and reachable before the first ``Subscribe()`` call.
   :impact: A late-configured identity service causes early
      ``Subscribe()`` calls to be rejected, delaying application
      startup.

   Recommended integration order for the identity/token service
   relative to Module A startup.

Restrictions
^^^^^^^^^^^^^^

.. res:: Do not disable AuthTokenRequired at ASIL D
   :id: RES_A_001
   :version: 1.0.0
   :status: approved
   :links: SAFEFEAT_A_001
   :input_reference: SG_001
   :req_type: Configuration
   :actions: Keep ``AuthTokenRequired`` set to ``True`` in any ASIL D
      integration.
   :impact: Disabling this setting removes the safety mechanism that
      ``SG_001`` and ``FSR_001`` depend on, invalidating the safety case
      for this configuration.

   ``AuthTokenRequired`` must remain enabled in any ASIL D deployment of
   Module A.

QORIX Support System
-----------------------

Please contact Qorix for any queries:

Email: AutosarSupport@qorix.ai

Website: https://www.qorix.ai/
