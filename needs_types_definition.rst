Needs Type Definitions
========================

This (root) Sphinx project registers seven Sphinx-Needs directives in
``conf.py``'s ``needs_types``. Every ``.. org_req::``, ``.. tool::``, etc.
in this project's content only renders and links because it's registered
here — an unregistered directive fails the build with ``Unknown directive
type``. (This table previously listed only ``org_req``, from before the
six management-register types below were migrated in from
``*_register.yml`` files — stale, fixed here.)

.. list-table::
   :header-rows: 1
   :widths: 15 15 55 15

   * - Directive
     - ID prefix
     - Standard mapping
     - Color
   * - ``org_req``
     - ``ORG_``
     - ISO 26262 Part 2 / ISO/SAE 21434 Clause 5 / ASPICE org-level /
       ISO 29119 org-level / ISO/IEC/IEEE 15288 clause 6.2
     - ``#B8003D``
   * - ``risk``
     - ``RISK_``
     - Organizational or Project Risk (from ``risk-register.yml``)
     - ``#B71C1C``
   * - ``problem``
     - ``PRB_``
     - Problem Report (from ``problem-register.yml``)
     - ``#D32F2F``
   * - ``change``
     - ``CR_``
     - Change Request (from ``change-register.yml``)
     - ``#5C6BC0``
   * - ``exception``
     - ``EXC_``
     - Tailoring Exception — deviation from the org-level process
     - ``#8E24AA``
   * - ``tool``
     - ``TOOL_``
     - Qualified Tool — ASPICE SUP.8/SUP.9 (from ``tool_register.yml``)
     - ``#00838F``
   * - ``infra``
     - ``INFRA_``
     - Infrastructure Element — ISO/IEC/IEEE 15288 clause 6.2.2(b)
     - ``#455A64``

Extra fields
--------------

Two free-text fields are registered in ``needs_fields`` alongside the type
above:

- ``standard`` — the standard/clause this need satisfies.
- ``derives_from`` — the upstream ID or external standard clause this
  requirement derives from. Kept as free text rather than a real
  Sphinx-Needs link, because org-level content cites both real need IDs
  (e.g. ``ORG_SMS_001``) and bare standard-clause references
  (e.g. ``ISO26262_2_5_4_2_1``) that have no matching need — a real link
  type would fail the dead-link gate (``needs_report_dead_links``) on
  every clause citation.

Status and version
---------------------

``needs_statuses`` is defined once here and kept identical in
``Needs/conf.py`` — sphinx-needs' status list is global, not per-type, so
it has to be. Combines the qik document-maturity states with the
issue-lifecycle states this project's own ``risk``/``problem``/``change``
types use (``open`` is the one real example today, in
``management/problem/problems.rst``). Full table and rationale in
``Needs/needs_types_definition.rst``'s "Status and version" section — not
repeated twice here.

``:version:`` on ``org_req`` now carries ``1.0.0`` as a content baseline,
same meaning as on the requirement-shaped types in ``Needs/``. Left
untouched on ``risk``/``problem``/``change``/``exception``/``infra``
(issue-register entries, not versioned requirement text) and on ``tool``
(where ``version`` already means the tool's own pinned version — see
``organisation/tools/tool_register.rst``, not touched by this addition).

Where the ID format comes from
---------------------------------

``needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"`` enforces the
``PREFIX_rest`` shape for every need ID in this project — the same shape
the prefix column above defines per type.

Not this project's types
---------------------------

``Needs/`` is a **separate** Sphinx project with its own ``conf.py`` and
its own eight need types (``sys``/``feat``/``comp``/``unit``,
``sg``/``fsr``/``tsr``, ``eng_need``) — see
``Needs/needs_types_definition.rst``, built independently from inside
``Needs/``. See ``STANDARDS.md`` for the full folder-to-standard crosswalk
across both projects.
