Qorix Engineering Processes
===========================

This is the root-level documentation project for Qorix Engineering Processes. It covers
organizational governance and project process; the product traceability
graph (system/feature/component/unit requirements, safety chain) lives in
``Needs/`` as a **separate** Sphinx project — build it independently from
inside ``Needs/`` (``sphinx-build -b html . _build``). See ``STANDARDS.md``
for how each folder maps onto ASPICE / ISO 15288 / ISO 26262 / ISO 29119
terminology. Published documentation lives under ``doc/`` (``manuals/``,
``tutorials/``, ``reference/``, ``release_notes/``, ``errata/`` — see
``doc/README.md``); it's plain Markdown, not part of this Sphinx build.

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   getting_started

.. toctree::
   :maxdepth: 2
   :caption: Organizational Governance

   org_governance/index
   org_governance/framework/index
   org_verification/iso29119/index
   org_tools/index

.. toctree::
   :maxdepth: 1
   :caption: Enterprise Strategy

   org_strategy/index

.. toctree::
   :maxdepth: 2
   :caption: Common Framework

   org_common_framework/index

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

   test/index

.. toctree::
   :maxdepth: 1
   :caption: Traceability (organizational requirements only)

   needs_types_definition
   needs_overview
