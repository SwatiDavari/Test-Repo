Organizational Requirements Overview
========================================

This page renders live traceability for every ``org_req`` need registered
in this (root) Sphinx project — the four organization-level standard files
under ``org_governance/`` and ``org_verification/iso29119/``. Product-level
traceability (system/feature/component/unit, safety chain) is a separate
build under ``Needs/`` — see its own ``needs_overview``-equivalent on
``Needs/index``.

All organizational requirements
------------------------------------

.. needtable::
   :columns: id, title, status, standard, derives_from

Unlinked (orphan) requirements — traceability gate check
--------------------------------------------------------------

.. needtable::
   :filter: len(links) == 0 and len(links_back) == 0
   :columns: id, title, standard

.. note::
   ``derives_from`` is a free-text field here (not a checked link — see
   ``conf.py``), so it won't appear in the orphan filter above even where
   it cites an upstream ID or standard clause. That's a known limitation
   of treating it as free text rather than a real link type; see the
   ``derives_from`` rationale in this project's ``conf.py`` and in
   ``Needs/conf.py``.
