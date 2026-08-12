Organizational Project-Enabling Processes — Requirements
===============================================================

All six processes from ISO/IEC/IEEE 15288 clause 6.2, in clause order.
Each process is decomposed one org_req per lettered outcome (6.2.x.2 a,
b, c, ...) — the same decomposition already used by
:doc:`../../org_tools/tool_qualification_requirements` for tool
qualification, and by Infrastructure Management below. Decomposing per
outcome, instead of one org_req asserting a whole process at once, is
what makes it possible to say plainly that a process is *partly* met —
some outcomes satisfied, others not — rather than rounding the whole
process up to "Satisfied" or down to "Gap." Every status below was
checked against real content in this repo, not assumed; where a
requirement (an ``org_req`` or ``:need:``) exists but no evidence shows
it has actually been carried out, that is called "Partial," not
"Satisfied."

Life Cycle Model Management (6.2.1)
----------------------------------------

Purpose, per the standard: define, maintain, and keep available the
organization's life cycle policies, processes, models, and procedures,
so projects can draw on them rather than invent their own, using
methods and tools with a track record.

.. org_req:: Policies and procedures for managing and deploying life cycle models are established (outcome a)
   :id: ORG_LCM_001
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.1.2, outcome a

   The organization shall establish and maintain policies and
   procedures for how its life cycle models and processes are defined,
   deployed, and kept current across projects — governance for the
   model, not just the model's content.

   **Partial, disclosed rather than closed here:** :doc:`../framework/lifecycle_model`
   states which life cycle this organization actually runs — the
   ASPICE stage chain plus the ISO 26262 safety chain, tied to the
   milestones in :doc:`../../management/planning/project-plan` — and how
   a project may tailor it. That page *is* the life cycle model. What's
   missing is the policy layer above it: who may change it, on what
   cadence, under what approval. Today it's edited like any other doc
   page, with no distinct governance of its own.

.. org_req:: Responsibility, accountability, and authority for life cycle models are defined (outcome b)
   :id: ORG_LCM_002
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.1.2, outcome b

   The organization shall name who is responsible, accountable, and
   authorized for its life cycle policies, processes, models, and
   procedures.

   **Gap, disclosed rather than closed here:** :doc:`../framework/process_metamodel`
   names generic roles (Contributor, Committer, Line Manager, Process
   Development Community), but none of them is mapped specifically to
   owning the life cycle model or deciding its tailoring.

.. org_req:: Life cycle models and processes are assessed (outcome c)
   :id: ORG_LCM_003
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.1.2, outcome c

   The organization shall periodically assess the life cycle models
   and processes it uses, to confirm they remain suitable, adequate,
   and effective.

   **Gap, disclosed rather than closed here:** :need:`ORG_ASPICE_APPRAISAL_001`
   requires a periodic appraisal program against the adopted PAM — but
   it is a requirement, not a record. No appraisal of this
   organization's life cycle model has actually taken place yet.

.. org_req:: Prioritized life cycle model improvements are implemented (outcome d)
   :id: ORG_LCM_004
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.1.2, outcome d

   The organization shall prioritize and implement improvements to its
   life cycle models, processes, and procedures identified through
   assessment.

   **Gap, disclosed rather than closed here:** there is no improvement
   backlog or change record for the life cycle model to point at —
   unsurprising, since outcome (c) above (assessment) hasn't happened
   either, so there is nothing yet to improve from.

Infrastructure Management (6.2.2)
----------------------------------------

Purpose, per the standard: provide the infrastructure and services
projects need throughout the life cycle — the facilities, tools, and
communications/IT assets the organization's business runs on.

Decomposed into the standard's own four outcomes (6.2.2.2 a–d), the same
way :doc:`../../org_tools/tool_qualification_requirements` decomposes
tool qualification — each outcome gets its own requirement instead of
one requirement asserting all four at once.

.. org_req:: Infrastructure requirements are defined (outcome a)
   :id: ORG_INFRA_001
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.2.2, outcome a

   The organization shall define what every project actually needs from
   its infrastructure — before that infrastructure is acquired, not
   inferred from it afterward.

   What the current workflows imply but never state outright: CI compute
   must run Ubuntu-based images capable of Bazel, CMake/CTest, the Rust
   toolchain, Node 20, and Python 3.11/3.12 (per
   :doc:`../../org_tools/tool_register`); docs hosting must serve static
   HTML with public read access and support a Sphinx-Needs build.

   **Gap, disclosed rather than closed here:** those requirements are
   *implied* by the workflow files, not written down anywhere as an
   actual requirements statement. If a workflow started needing, say, a
   GPU runner or a larger disk, there's no requirement it would be
   checked against — only the workflow file itself, discovered by
   trial and error.

.. org_req:: Infrastructure elements are identified and specified (outcome b)
   :id: ORG_INFRA_002
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.2.2, outcome b

   The organization shall identify each infrastructure element and
   specify it (what it is, who provides it, what depends on it).

   **Satisfied** — see :doc:`infra_register`, migrated the same way
   :doc:`../../org_tools/tool_register` was: real elements, not invented
   ones.

.. org_req:: Infrastructure elements are developed or acquired (outcome c)
   :id: ORG_INFRA_003
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.2.2, outcome c

   The organization shall develop or acquire each infrastructure element
   per its specification, and record which path was taken and why.

   What's actually true today: every element in :doc:`infra_register` was
   *acquired* (SaaS — GitHub Actions, GitHub Pages) or is a checked-in
   config file; nothing was purpose-built in-house.

   **Gap, disclosed rather than closed here:** no record of *why*
   SaaS-over-self-hosted was chosen — it reads as the default, not a
   decision anyone made and wrote down.

.. org_req:: Infrastructure is available (outcome d)
   :id: ORG_INFRA_004
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.2.2, outcome d

   The organization shall ensure its infrastructure is available when
   projects need it, and know when it isn't.

   **Gap, disclosed rather than closed here:** every element in
   :doc:`infra_register` depends entirely on its provider's own SLA
   (GitHub's). This organization runs no independent availability
   monitoring, has no backup/DR plan, and has no incident process for an
   infrastructure outage. Marking this "satisfied" would overstate what
   exists — there is no org-level activity here at all yet, only
   inherited vendor uptime.

Portfolio Management (6.2.3)
----------------------------------------

Purpose, per the standard: start and sustain enough of the right
projects to meet the organization's strategic objectives — committing
funding and resources, granting the authority to run them, and
continually re-checking whether each still justifies that investment.

The standard gives this process seven outcomes, more than any other
6.2.x process — reflecting that portfolio management spans a project's
whole life, from being proposed to being closed.

.. org_req:: Business opportunities and investments are qualified and prioritized (outcome a)
   :id: ORG_PORTFOLIO_001
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.3.2, outcome a

   The organization shall qualify candidate ventures, investments, or
   necessities against its strategic objectives, and prioritize among
   them.

   **Partial, disclosed rather than closed here:** :doc:`../../org_strategy/strategy`
   (vision, business objectives, engineering principles) and
   :doc:`../../org_strategy/roadmap` (platform-evolution phases) describe
   the direction the organization wants to move in. Neither is a record
   of qualifying or ranking competing opportunities against each other —
   there is only one direction described, not several weighed against
   it.

.. org_req:: Projects are identified (outcome b)
   :id: ORG_PORTFOLIO_002
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.3.2, outcome b

   The organization shall identify the projects it is running.

   **Partial, disclosed rather than closed here:** the one-repo-per-project
   model in :doc:`../framework/architecture` implies more than one
   product repo can exist side by side, and in practice two do (this
   repo and Test_Dashboard). That's an informal identification by the
   fact that the repos exist — there is no formal register that lists
   them as a tracked portfolio.

.. org_req:: Resources and budgets are allocated per project (outcome c)
   :id: ORG_PORTFOLIO_003
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.3.2, outcome c

   The organization shall allocate resources and budget to each project
   it runs.

   **Gap, disclosed rather than closed here:** no budget or
   resource-allocation record exists anywhere in this repo for either
   product repo.

.. org_req:: Project management responsibilities, accountability, and authorities are defined (outcome d)
   :id: ORG_PORTFOLIO_004
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.3.2, outcome d

   The organization shall define who manages each project, and who is
   accountable and authorized for it.

   **Gap, disclosed rather than closed here:** nothing states who
   authorized this repo (or Test_Dashboard) as a project, or who holds
   portfolio-level accountability for it — as distinct from the
   generic contributor/committer roles :doc:`../framework/process_metamodel`
   names for day-to-day work.

.. org_req:: Projects meeting their agreement and stakeholder requirements are sustained (outcome e)
   :id: ORG_PORTFOLIO_005
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.3.2, outcome e

   The organization shall confirm which of its projects are meeting
   their agreement and stakeholder requirements, and continue investing
   in them.

   **Gap, disclosed rather than closed here:** no portfolio review of
   ongoing viability has ever been recorded for either product repo.

.. org_req:: Projects not meeting requirements are redirected or terminated (outcome f)
   :id: ORG_PORTFOLIO_006
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.3.2, outcome f

   The organization shall redirect or terminate projects that are not
   meeting their agreement or stakeholder requirements.

   **Gap, disclosed rather than closed here:** no redirection or
   termination decision has ever been recorded — there being no
   portfolio review (outcome e) to trigger one.

.. org_req:: Completed projects are closed (outcome g)
   :id: ORG_PORTFOLIO_007
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.3.2, outcome g

   The organization shall close projects once their agreements are
   complete and stakeholder requirements are satisfied.

   **Gap, disclosed rather than closed here:** neither product repo has
   been closed, and there is no defined meaning of "closed" for one at
   the portfolio level to check against.

Human Resource Management (6.2.4)
----------------------------------------

Purpose, per the standard: keep the organization supplied with the
human resources it needs and maintain their competence, consistent
with business needs.

.. org_req:: Skills required by projects are identified (outcome a)
   :id: ORG_HR_001
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.4.2, outcome a

   The organization shall identify the skills its projects need.

   **Partial, disclosed rather than closed here:** :need:`ORG_COMPETENCE_001`
   identifies the competence needed for "personnel performing
   safety-related activities" — but only that scope. No equivalent
   skill-identification exists for the other roles
   :doc:`../framework/process_metamodel` names (Contributor, Committer,
   Process Development Community, Line Manager, AI Project Assistant).

.. org_req:: Necessary human resources are provided to projects (outcome b)
   :id: ORG_HR_002
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.4.2, outcome b

   The organization shall provide the human resources its projects need.

   **Gap, disclosed rather than closed here:** no staffing or
   resourcing record exists; who is actually assigned to this repo's
   work is nowhere written down.

.. org_req:: Personnel skills are developed, maintained, or enhanced (outcome c)
   :id: ORG_HR_003
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.4.2, outcome c

   The organization shall develop, maintain, or enhance the skills of
   its personnel.

   **Partial, disclosed rather than closed here:** :need:`ORG_ASPICE_COMPETENCE_001`
   (process-assessor and QA competence, training records) and
   :need:`ORG_COMPETENCE_001` (safety personnel) both require records of
   competence development — but each is scoped to one specific role,
   and each is a requirement rather than an executed training record.
   No general skills-development activity has actually happened yet for
   either scope, and no scope exists for roles outside them.

.. org_req:: Multi-project resource conflicts are resolved (outcome d)
   :id: ORG_HR_004
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.4.2, outcome d

   The organization shall resolve conflicts arising when more than one
   project competes for the same personnel.

   **Gap, disclosed rather than closed here:** this repo has no
   visibility into resourcing across other projects (e.g.
   Test_Dashboard), so there is no process for resolving a conflict
   between them even if one arose.

Quality Management (6.2.5)
----------------------------------------

Purpose, per the standard: assure that products, services, and the
quality management process itself meet the organization's and its
projects' quality objectives, and satisfy customers. The standard
itself notes these outcomes are written to align with ISO 9001:2008
subclause 4.1.

.. org_req:: Quality management policies, objectives, and procedures are defined and implemented (outcome a)
   :id: ORG_QM_001
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.5.2, outcome a

   The organization shall define and implement quality management
   policies, objectives, and procedures.

   **Partial, disclosed rather than closed here:** :doc:`../policies/quality`
   states the policy, and :need:`ORG_ASPICE_PRM_001` /
   :need:`ORG_ASPICE_SUP1_001` define the adopted process model and the
   SUP.1 quality assurance process. Defined — yes. Implemented — the
   policy page says outright that ``Needs/quality/`` is "currently
   scaffolding only (no review or metric data has been captured yet),"
   so the defined process has no operating instance behind it yet.

.. org_req:: Quality evaluation criteria and methods are established (outcome b)
   :id: ORG_QM_002
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.5.2, outcome b

   The organization shall establish criteria and methods for evaluating
   quality.

   **Partial, disclosed rather than closed here:** :need:`ORG_ASPICE_CL_POLICY_001`
   sets up the ASPICE capability-level rating scale (0-5) as the
   intended evaluation method. The scale is defined; no project has
   actually been evaluated against it yet.

.. org_req:: Resources and information are provided to support project QA activities (outcome c)
   :id: ORG_QM_003
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.5.2, outcome c

   The organization shall provide the resources and information
   projects need to operate and monitor their own quality assurance
   activities.

   **Gap, disclosed rather than closed here:** there is no resourcing
   for QA activity to point at — no assigned QA capacity, no shared QA
   tooling beyond the CI checks already covered under
   :doc:`../../org_tools/tool_register`.

.. org_req:: Quality assurance evaluation results are gathered and analyzed (outcome d)
   :id: ORG_QM_004
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.5.2, outcome d

   The organization shall gather and analyze the results of quality
   assurance evaluations.

   **Gap, disclosed rather than closed here:** same scaffolding-only
   state noted under outcome (a) — there are no evaluation results yet
   to gather.

.. org_req:: Quality policies and procedures are improved from results (outcome e)
   :id: ORG_QM_005
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.5.2, outcome e

   The organization shall improve its quality management policies and
   procedures based on project and organizational results.

   **Gap, disclosed rather than closed here:** with no results yet
   (outcome d), there is nothing to improve from.

Knowledge Management (6.2.6)
----------------------------------------

Purpose, per the standard: build the capability and assets that let
the organization re-apply knowledge it already has — spanning
knowledge, skills, and knowledge assets, including system elements.

.. org_req:: A taxonomy for knowledge assets is identified (outcome a)
   :id: ORG_KM_001
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.6.2, outcome a

   The organization shall identify a taxonomy for organizing its
   knowledge assets.

   **Satisfied** — the ``doc/`` folder structure (``manuals/``,
   ``tutorials/``, ``reference/``, ``release_notes/``, ``errata/``),
   named in :doc:`../framework/process_metamodel`, is itself a taxonomy
   for knowledge assets. This outcome asks for a taxonomy to be
   identified, not populated — populating it is outcomes (b) and (c)
   below.

.. org_req:: Knowledge, skills, and knowledge assets are developed or acquired (outcome b)
   :id: ORG_KM_002
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.6.2, outcome b

   The organization shall develop or acquire the knowledge, skills, and
   knowledge assets its taxonomy identifies a need for.

   **Partial, disclosed rather than closed here:** some of the
   taxonomy's folders hold real content, and other capture points named
   in :doc:`../framework/process_metamodel` are populated too —
   ``management/risk/``, ``management/problem/`` (both migrated to real
   needs this session), and ``test/test-reports/``. But three of the
   five ``doc/`` folders — ``manuals/``, ``tutorials/``, ``reference/``
   — hold nothing but a ``.gitkeep``.

.. org_req:: Knowledge, skills, and knowledge assets are available (outcome c)
   :id: ORG_KM_003
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.6.2, outcome c

   The organization shall make the knowledge, skills, and knowledge
   assets it holds available for reuse.

   **Partial, disclosed rather than closed here:** the same split as
   outcome (b) applies — available where content exists
   (``management/risk/``, ``management/problem/``,
   ``test/test-reports/``), not available where the folder is still
   just a placeholder (``manuals/``, ``tutorials/``, ``reference/``).

.. org_req:: Knowledge management usage data is gathered and analyzed (outcome d)
   :id: ORG_KM_004
   :status: draft
   :standard: ISO/IEC/IEEE 15288 clause 6.2.6.2, outcome d

   The organization shall gather and analyze data on how its knowledge
   assets are actually used.

   **Gap, disclosed rather than closed here:** nothing tracks who
   re-uses which knowledge asset, or how often — there is no usage data
   to analyze.
