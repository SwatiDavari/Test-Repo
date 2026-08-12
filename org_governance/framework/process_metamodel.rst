Enterprise Process Meta-Model
=================================

This diagram is the versioned, git-tracked replacement for an external
whiteboard sketch of the same idea: how a **project-level process**
(this repo's tailored instance, right) relates to the **org-level
process description** (the enterprise framework, left) that governs it.

Both sides follow the same shape — a Workflow produces a Workproduct,
which fulfills Guidance (Method / Guideline / Template / Checklist) and
either contains Definitions/Requirements (project side) or satisfies
Standard Requirements (org side) traced back to external Standards
(ASPICE / ISO 26262 / ISO 21434 / ISO 29119). The org side additionally
publishes the two documents every contributor actually starts from —
``getting_started.rst`` and this framework's own concept page.

.. uml:: process_metamodel.puml

Reading the actors
-------------------

- **Contributor** — authors a ``Contribution`` (commit/PR) and executes
  the project-level workflow.
- **Committer** — verifies, approves, and releases a ``DOCUMENT`` work
  product; also executes the org-level workflow (governance-area
  generator) when a new governance area is added.
- **Process Development Community** — defines the org-level workflow,
  including RASIC roles, and is codeowner of it.
- **Line Manager** — codeowner of the org-level Guidance set.
- **AI Project Assistant** — the role this session has been operating
  in: uses ``TOOLS``, creates Reports & Guidance, uses the ``Repo``.

This is intentionally *not* derived from any external project's process
repository (see the "Standards" node — external standards are cited as
references, not as the parent this framework inherits from). A project
that must additionally satisfy an external body's process records that
reconciliation in ``management/exceptions/``, per
:doc:`../index`.
