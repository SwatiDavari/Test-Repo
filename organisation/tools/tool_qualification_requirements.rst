Tool Qualification Requirements
====================================

These requirements apply at the **organization level** — independent of
any single product or project — per ISO 26262 Part 8 Clause 11
(Confidence in the Use of Software Tools) and ASPICE SUP.8 (Configuration
Management) / SUP.1 (Quality Assurance). They are prerequisites for
trusting any tool's output in a safety- or cybersecurity-relevant
development or verification chain.

Tool Register
-----------------

.. org_req:: Organizational tool register
   :id: ORG_TOOLREG_001
   :status: draft
   :standard: ISO 26262-8 clause 11.4.2 (Tool Identification) / ASPICE SUP.8

   The organization shall maintain a register of every tool used in the
   development or verification of safety- or cybersecurity-relevant work
   products, identifying each tool's name, version, intended use, and the
   toolchain step it belongs to (build, static analysis, traceability,
   test execution).

   The actual register lives in :doc:`tool_register` — one entry per
   tool invoked by a CI workflow under ``.github/workflows/`` or by
   ``.pre-commit-config.yaml``.

Tool Confidence Level Determination
-----------------------------------------

.. org_req:: Tool confidence level determination
   :id: ORG_TOOLQUAL_001
   :status: draft
   :derives_from: ORG_TOOLREG_001
   :standard: ISO 26262-8 clause 11.4.5-11.4.7 (Tool Confidence Level)

   For every tool in the register, the organization shall determine its
   Tool Impact (TI) and Tool error Detection (TD) classification and
   derive the resulting Tool Confidence Level (TCL1-TCL3). Tools
   classified TCL2 or TCL3 shall have documented qualification evidence
   (e.g. evaluation of tool development process, or validation per
   ISO 26262-8 clause 11.4.9) before their output is relied upon in a
   safety- or cybersecurity-relevant chain.

Tool Version Control
-------------------------

.. org_req:: Tool version pinning
   :id: ORG_TOOLCFG_001
   :status: draft
   :derives_from: ORG_TOOLREG_001
   :standard: ASPICE SUP.8 Configuration Management

   The organization shall pin the version of every qualified tool
   (compiler, Sphinx-Needs, CI runner image) used in a safety- or
   cybersecurity-relevant chain under configuration management, so a
   qualified tool's version cannot change for a project without a
   deliberate, tracked update.

Re-qualification on Tool Change
-------------------------------------

.. org_req:: Tool re-verification on version change
   :id: ORG_TOOLQA_001
   :status: draft
   :derives_from: ORG_TOOLQUAL_001
   :standard: ASPICE SUP.1 Quality Assurance

   When a qualified tool's pinned version changes, the organization
   shall re-verify that the tool's qualification evidence still applies
   to the new version before the change is adopted in a safety- or
   cybersecurity-relevant chain.
