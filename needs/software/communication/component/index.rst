Communication Manager — Component
=======================================

Register of component-level (``comp``) design for the Communication
module — one file per module, not one file per component.

.. comp:: Communication Manager Architecture
   :id: comp_a_001
   :version: 1.0.0
   :status: proposed
   :asil: ASIL B
   :satisfies: feat_a_001, feat_com_arch_001, feat_com_arch_002, feat_com_arch_003, feat_com_ifc_001, feat_com_ifc_002, feat_com_ifc_003, feat_com_ifc_004, feat_com_ifc_005, feat_com_ifc_006, feat_com_ifc_007, feat_com_ifc_008, feat_com_ifc_009, feat_com_ifc_010, feat_com_ifc_011, feat_com_ifc_012, feat_com_safety_001, feat_com_safety_002, feat_com_safety_003, feat_com_safety_004, feat_com_safety_005, feat_com_perf_001, feat_com_binding_001, feat_com_binding_002, feat_com_binding_003, feat_com_binding_004, feat_com_binding_005, feat_com_binding_006, feat_com_binding_007, feat_com_binding_008, feat_com_vm_001, feat_com_vm_002, feat_com_perf_002, feat_com_perf_003, feat_com_perf_004, feat_com_perf_005, feat_com_perf_006, feat_com_perf_007, feat_com_perf_008, feat_com_perf_009, feat_com_perf_010, feat_com_perf_011, feat_com_perf_012, feat_com_deploy_001, feat_com_trace_001, feat_com_acl_001, feat_com_acl_002, feat_com_acl_003, feat_com_acl_004, feat_com_safety_006, feat_com_ipc_001, feat_com_ipc_002, feat_com_ipc_003, feat_com_ipc_004, feat_com_someip_001, feat_com_someip_002, feat_com_someip_003, feat_com_someip_004, feat_com_someip_005
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4

   Defines the structural decomposition of the communication manager into
   proxy, skeleton, and binding layers.

   .. note::
      ``:satisfies:`` extended (originally just ``feat_a_001``) to every
      requirement imported in :doc:`../feature/requirements/index`
      (Communication, IPC, and SOME/IP Gateway alike), because the
      eclipse-score source satisfies all of them from this one
      architecture element (``feat__com_communication`` /
      ``feat_arc_sta__com__communication``) — the source's own architecture
      tier is this shallow, not a modeling shortcut introduced here. See
      the "Cross-cutting observations" section of the project's
      ``eclipse_score_communication_traceability_reference.md``.

.. comp:: Communication User Interface
   :id: comp_com_userifc_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_ifc_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: eclipse-score/score docs/features/communication -- logic_arc_int__communication__user (source safety: ASIL_B, source security: YES)

   The public, binding-agnostic user-facing interface (Proxy/Skeleton) that
   the Communication Manager architecture exposes to producers and
   consumers. Source: eclipse-score ``architecture/index.rst``, "Interface
   Description" — fulfils ``feat_req__com__interfaces`` (converted here as
   ``feat_com_ifc_001``, "Communication Interfaces").

   No ``:asil:`` set here: this is a newly-imported architecture element
   with no HARA outcome of its own in this project (only ``comp_a_001``
   carries the real safety-chain ASIL — see ``sg_001``/``fsr_001``/
   ``tsr_001``).

.. comp:: IPC Dynamic Architecture
   :id: comp_com_ipc_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_deploy_001
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
      ``feat_com_deploy_001``, "Deployment configuration at runtime"), not an
      IPC-specific one. Reproduced as-is — this cross-link is faithful to
      the source, not a transcription error.

      No ``:asil:`` set, for the same reason as ``comp_com_userifc_001``.

.. toctree::
   :maxdepth: 1

   requirements/index
   integration_test_cases
   unit design/units
   unit test/index

.. comp:: ara::com Core Paradigms and Versioning
   :id: comp_com_paradigm_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_ifc_012, feat_com_ifc_008
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 3 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 3 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Protocol Compliance and Static Connection
   :id: comp_com_someip_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_someip_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 7 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 7 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Service Discovery Protocol
   :id: comp_com_sd_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_someip_005
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 18 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 18 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Message Accumulation and Execution Context
   :id: comp_com_msgctx_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_someip_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 5 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 5 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Handling of Events and Triggers
   :id: comp_com_evttrig_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_ifc_002, feat_com_someip_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 18 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 18 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: IAM Access Control Configuration
   :id: comp_com_iam_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_acl_001, feat_com_acl_002
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 8 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 8 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: IAM Remote Access Control Detail
   :id: comp_com_iamremote_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_acl_003, feat_com_acl_004
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 10 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 10 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: Secure Channels and Network-Layer Security (SOME/IP)
   :id: comp_com_secchan_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_safety_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 7 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 7 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: Secure Transport Protocols -- SecOC and TLS (SOME/IP)
   :id: comp_com_sectrans_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_safety_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 22 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 22 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: E2E Protection Paradigm
   :id: comp_com_e2e_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_someip_002, feat_com_someip_004
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 8 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 8 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: E2E Protection Detail -- Events
   :id: comp_com_e2eevt_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_someip_002
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 20 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 20 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: E2E Protection Detail -- Methods
   :id: comp_com_e2emeth_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_someip_004
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 44 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 44 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: Communication Interfaces -- Core ara::com API
   :id: comp_com_coreapi_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_ifc_001, feat_com_ifc_002, feat_com_ifc_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 48 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 48 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: ara::com Interface Behavior Detail
   :id: comp_com_apidetail_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_ifc_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 4 requirement(s), see :doc:`../../unit design/units`

   AUTOSAR Adaptive Platform Communication Management SWS topic grouping introduced to hold the 4 detailed-design requirement(s) below as ``unit::`` needs, imported from the attached AUTOSAR_AP_SWS_CommunicationManagement.pdf.

.. comp:: SOME/IP Payload Serialization and Method/Field Handling (compressed reference)
   :id: comp_com_serdes_001
   :version: 1.0.0
   :status: draft
   :satisfies: feat_com_someip_003
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- 166 requirements in SWS 7.4.1.7, 7.4.1.8 and 7.4.1.9.* compressed into 10 representative entries below (see note)

   Per-field-type SOME/IP method/field handling (SWS 7.4.1.7, 7.4.1.8 -- 64 requirements) and wire-format serialization rules (SWS 7.4.1.9 and its subsections -- 102 requirements, one per data-type byte-encoding rule) were compressed into the 10 representative ``unit::`` needs below rather than converted 1:1, per an explicit scoping decision (too granular for a requirements register; full detail remains in the standard itself).
