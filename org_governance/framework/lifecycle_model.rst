Lifecycle Model
==================

The "Lifecycle Model" element of Organizational Process Definition — the
one piece of that breakdown with no other page to live on. It states, in
one place, which lifecycle this organization actually runs: the two
chains already built into ``Needs/`` and the milestones already stubbed
in :doc:`../../management/planning/project-plan`, tied together as a
single model rather than left as separate, unconnected artifacts.

Engineering lifecycle
------------------------

Requirements and design flow through four ASPICE stages, each a distinct
need type in ``Needs/conf.py``:

1. **System Requirements** (``sys``, ASPICE SYS.2) — ``Needs/sys/``
2. **Feature / Software Requirements** (``feat``, ASPICE SWE.1) — one
   folder per module, e.g. ``Needs/Communication/feature/``
3. **Component / Software Architecture** (``comp``, ASPICE SWE.2) — e.g.
   ``Needs/Communication/component/``
4. **Unit / Detailed Design** (``unit``, ASPICE SWE.3) — e.g.
   ``Needs/Communication/unit design/``

Each stage links to the one above it via the built-in ``:links:`` field;
see :doc:`templates/index` for the exact form each stage takes.

Safety lifecycle
-------------------

Layered onto the same needs graph for safety-related modules, per
ISO 26262:

1. **Safety Goal** (``sg``, ISO 26262-3 clause 6 — HARA) — ``Needs/safety/analyses``
2. **Functional Safety Requirement** (``fsr``, ISO 26262-3 clause 8)
3. **Technical Safety Requirement** (``tsr``, ISO 26262-4 clause 6 / ISO 26262-6)

Project milestones
---------------------

The engineering and safety lifecycles above converge at the milestones
in :doc:`../../management/planning/project-plan`: architecture freeze
(component design complete), feature complete, release candidate, and
release.

Tailoring
-----------

A project may tailor how it moves through this lifecycle — e.g.
combining milestones, or skipping the safety lifecycle for a module with
no safety relevance — but may not skip a stage's underlying ASPICE
activity. Deviations are recorded in
:doc:`../../management/exceptions/exceptions`, per the ``tailors``
relationship in :doc:`process_metamodel`.

This lifecycle is assembled from ASPICE and ISO 26262 directly; it is
not adopted from any single external project's lifecycle definition.
