Communication Manager — Component
=======================================

Register of component-level (``comp``) design for the Communication
module — one file per module, not one file per component.

.. comp:: Communication Manager Architecture
   :id: COMP_A_001
   :version: 1.0.0
   :status: proposed
   :asil: ASIL B
   :satisfies: FEAT_A_001, FEAT_COM_ARCH_001, FEAT_COM_ARCH_002, FEAT_COM_ARCH_003, FEAT_COM_IFC_001, FEAT_COM_IFC_002, FEAT_COM_IFC_003, FEAT_COM_IFC_004, FEAT_COM_IFC_005, FEAT_COM_IFC_006, FEAT_COM_IFC_007, FEAT_COM_IFC_008, FEAT_COM_IFC_009, FEAT_COM_IFC_010, FEAT_COM_IFC_011, FEAT_COM_IFC_012, FEAT_COM_SAFETY_001, FEAT_COM_SAFETY_002, FEAT_COM_SAFETY_003, FEAT_COM_SAFETY_004, FEAT_COM_SAFETY_005, FEAT_COM_PERF_001, FEAT_COM_BINDING_001, FEAT_COM_BINDING_002, FEAT_COM_BINDING_003, FEAT_COM_BINDING_004, FEAT_COM_BINDING_005, FEAT_COM_BINDING_006, FEAT_COM_BINDING_007, FEAT_COM_BINDING_008, FEAT_COM_VM_001, FEAT_COM_VM_002, FEAT_COM_PERF_002, FEAT_COM_PERF_003, FEAT_COM_PERF_004, FEAT_COM_PERF_005, FEAT_COM_PERF_006, FEAT_COM_PERF_007, FEAT_COM_PERF_008, FEAT_COM_PERF_009, FEAT_COM_PERF_010, FEAT_COM_PERF_011, FEAT_COM_PERF_012, FEAT_COM_DEPLOY_001, FEAT_COM_TRACE_001, FEAT_COM_ACL_001, FEAT_COM_ACL_002, FEAT_COM_ACL_003, FEAT_COM_ACL_004, FEAT_COM_SAFETY_006, FEAT_COM_IPC_001, FEAT_COM_IPC_002, FEAT_COM_IPC_003, FEAT_COM_IPC_004, FEAT_COM_SOMEIP_001, FEAT_COM_SOMEIP_002, FEAT_COM_SOMEIP_003, FEAT_COM_SOMEIP_004, FEAT_COM_SOMEIP_005
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4

   Defines the structural decomposition of the communication manager into
   proxy, skeleton, and binding layers.

   .. note::
      ``:satisfies:`` extended (originally just ``FEAT_A_001``) to every
      requirement imported in :doc:`../feature/requirements/index`
      (Communication, IPC, and SOME/IP Gateway alike), because the
      eclipse-score source satisfies all of them from this one
      architecture element (``feat__com_communication`` /
      ``feat_arc_sta__com__communication``) — the source's own architecture
      tier is this shallow, not a modeling shortcut introduced here. See
      the "Cross-cutting observations" section of the project's
      ``eclipse_score_communication_traceability_reference.md``.

.. comp:: Communication User Interface
   :id: COMP_COM_USERIFC_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_IFC_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: eclipse-score/score docs/features/communication -- logic_arc_int__communication__user (source safety: ASIL_B, source security: YES)

   The public, binding-agnostic user-facing interface (Proxy/Skeleton) that
   the Communication Manager architecture exposes to producers and
   consumers. Source: eclipse-score ``architecture/index.rst``, "Interface
   Description" — fulfils ``feat_req__com__interfaces`` (converted here as
   ``FEAT_COM_IFC_001``, "Communication Interfaces").

   No ``:asil:`` set here: this is a newly-imported architecture element
   with no HARA outcome of its own in this project (only ``COMP_A_001``
   carries the real safety-chain ASIL — see ``SG_001``/``FSR_001``/
   ``TSR_001``).

.. comp:: IPC Dynamic Architecture
   :id: COMP_COM_IPC_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_DEPLOY_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: eclipse-score/score docs/features/communication -- feat_arc_dyn__communication__ipc (source safety: ASIL_B, source security: YES)

   Dynamic-architecture element for the IPC sub-feature (shared-memory
   control/data-segment split and message-passing notification behavior).
   Source: eclipse-score ``ipc/architecture/index.rst``, "Dynamic
   Architecture".

   .. note::
      In the source, this need is filed under the IPC sub-feature folder
      but ``:fulfils:`` a *top-level* Communication requirement
      (``feat_req__com__depl_config_runtime``, converted here as
      ``FEAT_COM_DEPLOY_001``, "Deployment configuration at runtime"), not an
      IPC-specific one. Reproduced as-is — this cross-link is faithful to
      the source, not a transcription error.

      No ``:asil:`` set, for the same reason as ``COMP_COM_USERIFC_001``.

.. toctree::
   :maxdepth: 1

   requirements/index
   integration_test_cases
   unit design/units
   unit test/index

.. comp:: ara::com Core Paradigms and Versioning
   :id: COMP_COM_PARADIGM_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_IFC_012, FEAT_COM_IFC_008
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 3 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 3 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Protocol Compliance and Static Connection
   :id: COMP_COM_SOMEIP_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SOMEIP_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 7 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 7 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Service Discovery Protocol
   :id: COMP_COM_SD_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SOMEIP_005
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 18 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 18 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Message Accumulation and Execution Context
   :id: COMP_COM_MSGCTX_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SOMEIP_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 5 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 5 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Handling of Events and Triggers
   :id: COMP_COM_EVTTRIG_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_IFC_002, FEAT_COM_SOMEIP_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 18 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 18 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: IAM Access Control Configuration
   :id: COMP_COM_IAM_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_ACL_001, FEAT_COM_ACL_002
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 8 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 8 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: IAM Remote Access Control Detail
   :id: COMP_COM_IAMREMOTE_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_ACL_003, FEAT_COM_ACL_004
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 10 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 10 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: Secure Channels and Network-Layer Security (SOME/IP)
   :id: COMP_COM_SECCHAN_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SAFETY_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 7 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 7 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: Secure Transport Protocols -- SecOC and TLS (SOME/IP)
   :id: COMP_COM_SECTRANS_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SAFETY_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 22 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 22 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: E2E Protection Paradigm
   :id: COMP_COM_E2E_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SOMEIP_002, FEAT_COM_SOMEIP_004
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 8 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 8 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: E2E Protection Detail -- Events
   :id: COMP_COM_E2EEVT_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SOMEIP_002
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 20 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 20 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: E2E Protection Detail -- Methods
   :id: COMP_COM_E2EMETH_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SOMEIP_004
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 44 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 44 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: Communication Interfaces -- Core ara::com API
   :id: COMP_COM_COREAPI_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_IFC_001, FEAT_COM_IFC_002, FEAT_COM_IFC_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 48 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 48 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: ara::com Interface Behavior Detail
   :id: COMP_COM_APIDETAIL_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_IFC_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 4 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 4 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Payload Serialization and Method/Field Handling (compressed reference)
   :id: COMP_COM_SERDES_001
   :version: 1.0.0
   :status: draft
   :satisfies: FEAT_COM_SOMEIP_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 166 requirements in SWS 7.4.1.7, 7.4.1.8 and 7.4.1.9.* compressed into 10 representative entries below (see note)

   Per-field-type SOME/IP method/field handling (SWS 7.4.1.7, 7.4.1.8 -- 64 requirements) and wire-format serialization rules (SWS 7.4.1.9 and its subsections -- 102 requirements, one per data-type byte-encoding rule) were compressed into the 10 representative ``unit::`` needs below rather than converted 1:1, per an explicit scoping decision (too granular for a requirements register; full detail remains in the standard itself).
