Needs Type Definitions
========================

This (root) Sphinx project registers a single Sphinx-Needs directive in
``conf.py``'s ``needs_types``. Every ``.. org_req::`` in this project's
content only renders and links because it's registered here — an
unregistered directive fails the build with ``Unknown directive type``.

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
       ISO 29119 org-level
     - ``#B8003D``

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
