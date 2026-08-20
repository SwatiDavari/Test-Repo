Qorix Engineering Processes
===========================

This is the root-level documentation project for Qorix Engineering Processes. It covers
organizational governance and project process; the product traceability
graph (system/feature/component/unit requirements, safety chain) lives in
``needs/`` as a **separate** Sphinx project — build it independently from
inside ``needs/`` (``sphinx-build -b html . _build``). See ``STANDARDS.md``
for how each folder maps onto ASPICE / ISO 15288 / ISO 26262 / ISO 29119
terminology. Published documentation lives under ``doc/`` (``manuals/``,
``tutorials/``, ``reference/``, ``release_notes/``, ``errata/`` — see
``doc/README.md``); it's plain Markdown, not part of this Sphinx build.

.. note::
   Every toctree below lists its pages flat, one level deep, even where a
   page has children of its own (e.g. each per-standard organizational
   requirements page under "Organizational Governance"). This project
   uses the Furo theme, whose sidebar always renders at full depth
   regardless of a toctree's ``:maxdepth:`` — confirmed by reading
   ``furo/__init__.py``'s ``_compute_navigation_tree``, which calls
   ``toctree(maxdepth=-1, ...)`` unconditionally. The only way to avoid
   multi-level expandable nesting in the sidebar is to not declare that
   nesting in a toctree at all, so child pages are listed here directly
   and each parent page links to its children in prose instead (see the
   note in ``organisation/governance/index.rst``).

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   getting_started

.. toctree::
   :maxdepth: 1
   :caption: Organizational Governance

   organisation/governance/index
   organisation/governance/aspice/index
   organisation/governance/aspice/org_aspice_requirements
   organisation/governance/cybersecurity/index
   organisation/governance/cybersecurity/org_cybsec_requirements
   organisation/governance/functionalsafety/index
   organisation/governance/functionalsafety/org_fusa_requirements
   organisation/governance/quality/index
   organisation/governance/quality/org_quality_requirements
   organisation/governance/systemslifecycle/index
   organisation/governance/systemslifecycle/org_project_enabling_requirements
   organisation/governance/systemslifecycle/infra_register
   organisation/governance/policies/safety
   organisation/governance/policies/cybersecurity
   organisation/governance/policies/quality
   organisation/governance/framework/index
   organisation/governance/framework/architecture
   organisation/governance/framework/process_metamodel
   organisation/governance/framework/lifecycle_model
   organisation/governance/framework/templates/index
   organisation/testing/iso29119/index
   organisation/testing/iso29119/organizational_requirements
   organisation/testing/iso29119/strategy/product-verification-strategy
   organisation/tools/index
   organisation/tools/policy
   organisation/tools/tool_qualification_requirements
   organisation/tools/tool_register

.. toctree::
   :maxdepth: 1
   :caption: Enterprise Strategy

   organisation/strategy/index
   organisation/strategy/strategy
   organisation/strategy/roadmap

.. toctree::
   :maxdepth: 1
   :caption: Common Framework

   organisation/common_framework/index
   organisation/common_framework/core lib/error_handling/index
   organisation/common_framework/core lib/error_handling/overview
   organisation/common_framework/core lib/error_handling/error_classification
   organisation/common_framework/core lib/error_handling/exception_management
   organisation/common_framework/core lib/error_handling/fault_recovery
   organisation/common_framework/core lib/error_handling/logging_integration
   organisation/common_framework/core lib/error_handling/examples

.. toctree::
   :maxdepth: 1
   :caption: Project Management

   management/planning/project-plan
   management/change/changes
   management/problem/problems
   management/risk/risks
   management/exceptions/exceptions

.. toctree::
   :maxdepth: 1
   :caption: Verification

   integration test/index
   integration test/test strategy/product-verification-strategy
   integration test/test cases/index
   integration test/test reports/product-verification-report

.. toctree::
   :maxdepth: 1
   :caption: Decision Records

   decision records/decision_register

.. toctree::
   :maxdepth: 1
   :caption: Traceability (organizational requirements only)

   needs_types_definition
