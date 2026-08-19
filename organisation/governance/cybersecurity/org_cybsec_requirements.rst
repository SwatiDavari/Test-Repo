Clause 5 — Organizational Cybersecurity Management
=======================================================

These requirements apply at the **organization level** — independent
of any single product or project — per ISO/SAE 21434 Clause 5
(Organizational Cybersecurity Management). They are prerequisites
that must exist before any product-level cybersecurity work (TARA,
cybersecurity goals, cybersecurity requirements) can be considered
valid.

Cybersecurity Governance
----------------------------

.. org_req:: Cybersecurity governance policy
   :id: ORG_CYBERSEC_GOVERNANCE_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ISO21434_5_4_1

   The organization shall establish cybersecurity governance,
   including a cybersecurity policy, cybersecurity rules, and
   assigned responsibilities, that applies across all projects
   independent of any single product.

Cybersecurity Culture
--------------------------

.. org_req:: Cybersecurity culture policy
   :id: ORG_CYBERSEC_CULTURE_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ISO21434_5_4_2

   The organization shall establish and maintain a cybersecurity
   culture in which personnel are competent, aware of cybersecurity
   risks relevant to their role, and encouraged to report suspected
   vulnerabilities or weaknesses without fear of blame.

Information Sharing
------------------------

.. org_req:: Cybersecurity information sharing process
   :id: ORG_CYBERSEC_INFOSHARE_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ISO21434_5_4_3

   The organization shall define a process for sharing
   cybersecurity-relevant information (e.g., vulnerabilities, threat
   intelligence, lessons learned) across projects and, where
   appropriate, with external parties such as suppliers and
   Cybersecurity Incident Response Teams.

Cybersecurity Management System
------------------------------------

.. org_req:: Cybersecurity management system definition
   :id: ORG_CSMS_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ISO21434_5_4_4

   The organization shall define and maintain a cybersecurity
   management system (CSMS) describing roles, responsibilities, and
   processes for achieving cybersecurity across all projects, aligned
   with the organization's quality management system.

.. org_req:: Project-independent tailoring rules
   :id: ORG_CSMS_002
   :version: 1.0.0
   :status: proposed
   :derives_from: ORG_CSMS_001

   The organization shall define rules for tailoring the
   cybersecurity lifecycle to a specific project, based on
   Cybersecurity Assurance Level (CAL), project scope, and reuse of
   existing cybersecurity elements (including off-the-shelf and
   legacy components).

Tool Management
-------------------

.. org_req:: Cybersecurity tool management
   :id: ORG_CYBERSEC_TOOL_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ISO21434_5_4_5

   The organization shall establish a process for qualifying and
   managing the tools used to support cybersecurity activities (e.g.,
   static analysis, fuzzing, vulnerability scanning), including
   maintaining confidence in tool output relied upon for cybersecurity
   decisions.

Information Security Management
------------------------------------

.. org_req:: Information security management alignment
   :id: ORG_ISM_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ISO21434_5_4_6

   The organization shall protect cybersecurity-relevant information
   (e.g., TARA results, vulnerability data, cryptographic material)
   through an information security management process, consistent
   with its need for confidentiality, integrity, and availability.

Organizational Cybersecurity Audit
---------------------------------------

.. org_req:: Cybersecurity audit — audit, assessment, review
   :id: ORG_CYBERSEC_AUDIT_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ISO21434_5_4_7

   The organization shall perform, independent of any single project,
   organizational cybersecurity audits to confirm that the
   cybersecurity management system is suitable and effectively
   applied.

Continuous Cybersecurity Monitoring
----------------------------------------

.. org_req:: Continuous cybersecurity monitoring process
   :id: ORG_CYBERSEC_MONITORING_001
   :version: 1.0.0
   :status: proposed
   :derives_from: ORG_CSMS_001

   The organization shall establish a process to monitor for new
   cybersecurity vulnerabilities and events after release, evaluate
   their relevance, and feed findings back into the cybersecurity
   lifecycle (including potential TARA updates at platform or product
   level).
