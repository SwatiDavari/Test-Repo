Automotive SPICE — Organizational Quality Assurance Requirements
=====================================================================

These requirements apply at the **organization level** — independent
of any single product or project — per Automotive SPICE SUP.1 (Quality
Assurance) and the organization's adopted Process Reference and
Assessment Model (see :doc:`../aspice/org_aspice_requirements`,
``ORG_ASPICE_PRM_001``). They are prerequisites that must exist before
any product-level quality assurance work (audits, non-conformance
handling, capability assessment) can be considered valid.

Target Capability Level Policy
------------------------------------

.. org_req:: Target capability level per process
   :id: ORG_QUALITY_CL_POLICY_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ORG_ASPICE_PRM_001

   The organization shall define the target Capability Level
   (0-5, per the PAM rating scale N/P/L/F) required for each process
   in scope by default, and the conditions under which a project may
   be required to reach a higher level (e.g., safety- or
   cybersecurity-relevant projects).

Quality Assurance Process Definition
------------------------------------------

.. org_req:: Independent quality assurance process (SUP.1)
   :id: ORG_QUALITY_SUP1_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ORG_ASPICE_PRM_001

   The organization shall define an organization-wide Quality
   Assurance process (SUP.1) that is independent of the project team
   being assessed, including how non-conformances are raised,
   escalated, tracked to closure, and reported to management.

Competence Management
--------------------------

.. org_req:: Process assessor and quality engineer competence
   :id: ORG_QUALITY_COMPETENCE_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ORG_QUALITY_SUP1_001

   The organization shall ensure personnel performing process
   assessments or quality assurance activities have the necessary
   qualification (e.g., intacs-certified Competent/Principal
   Assessor), training, and experience, and shall maintain records of
   this competence.

Process Assessment & Improvement Program
----------------------------------------------

.. org_req:: Periodic process appraisal program
   :id: ORG_QUALITY_APPRAISAL_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ORG_QUALITY_CL_POLICY_001

   The organization shall run periodic internal or external process
   appraisals against the adopted PAM, track capability level trends
   across projects, and maintain an organization-level process
   improvement roadmap based on the findings.

Tailoring Rules
-------------------

.. org_req:: Project-independent tailoring rules
   :id: ORG_QUALITY_TAILORING_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ORG_ASPICE_PRM_001

   The organization shall define rules for tailoring the process
   reference model to a specific project, based on project size,
   criticality (e.g., ASIL/CAL relevance), and reuse of existing
   process assets.

Safety & Cybersecurity Interface
--------------------------------------

.. org_req:: Process quality alignment with safety and cybersecurity
   :id: ORG_QUALITY_SAFETY_INTERFACE_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ORG_QUALITY_SUP1_001

   The organization's Automotive SPICE quality assurance activities
   shall be defined so their evidence (e.g., process appraisal
   results, non-conformance records) can directly support ISO 26262
   confirmation measures (:doc:`../functionalsafety/org_fusa_requirements`,
   ``ORG_CONFIRMATION_001``) and ISO/SAE 21434 organizational
   cybersecurity audits, avoiding duplicate or conflicting evidence
   trails.
