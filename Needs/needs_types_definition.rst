Needs Type Definitions
========================

This (``Needs/``) Sphinx project registers eight Sphinx-Needs directives in
``conf.py``'s ``needs_types``. Every ``.. sys::``, ``.. feat::``,
``.. eng_need::``, etc. in this project's content only renders and links
because it's registered here — an unregistered directive fails the build
with ``Unknown directive type`` (this happened for real: ``eng_need`` was
used in ``business-needs.rst``/``operational-needs.rst``/
``stakeholder-needs.rst`` before it was registered, and broke the build
until it was added below).

ASPICE / ISO 15288 requirements chain
-----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 15 15 55 15

   * - Directive
     - ID prefix
     - Standard mapping
     - Color
   * - ``sys``
     - ``SYS_``
     - ASPICE SYS.2 / ISO 15288 System Requirements Definition
     - ``#BFD8D2``
   * - ``feat``
     - ``FEAT_``
     - ASPICE SWE.1 / ISO 15288 Requirements Definition
     - ``#FEDCD2``
   * - ``comp``
     - ``COMP_``
     - ASPICE SWE.2 / ISO 15288 Architecture Definition
     - ``#DF744A``
   * - ``unit``
     - ``UNIT_``
     - ASPICE SWE.3 / ISO 15288 Design Definition
     - ``#DCB239``

ISO 26262 functional safety chain
-------------------------------------

Layered onto the same needs graph so a safety requirement can link
straight into the ``sys``/``feat``/``comp``/``unit`` chain above — not
covered by ASPICE or ISO 15288 on their own.

.. list-table::
   :header-rows: 1
   :widths: 15 15 55 15

   * - Directive
     - ID prefix
     - Standard mapping
     - Color
   * - ``sg``
     - ``SG_``
     - Safety Goal — ISO 26262-3 clause 6 (HARA)
     - ``#B71C1C``
   * - ``fsr``
     - ``FSR_``
     - Functional Safety Requirement — ISO 26262-3 clause 8
     - ``#D32F2F``
   * - ``tsr``
     - ``TSR_``
     - Technical Safety Requirement — ISO 26262-4 clause 6 / ISO 26262-6
     - ``#E57373``

Pre-requirements input layer
---------------------------------

Upstream of ``sys`` — raw stakeholder/business/operational needs that
system requirements are elicited from. Not part of the ASPICE/ISO 15288
requirements-definition chain itself.

.. list-table::
   :header-rows: 1
   :widths: 15 15 55 15

   * - Directive
     - ID prefix
     - Standard mapping
     - Color
   * - ``eng_need``
     - ``NEED_``
     - Stakeholder / Business / Operational Need (``stakeholder-needs.rst``,
       ``business-needs.rst``, ``operational-needs.rst``)
     - ``#8E9AAF``

Extra fields
--------------

Registered in ``needs_fields`` alongside the types above:

- ``standard`` — the standard/clause this need satisfies.
- ``derives_from`` — the upstream need ID or external standard clause this
  requirement derives from. Kept as free text, not a real Sphinx-Needs
  link — same rationale as the root project's ``conf.py``: a real link
  type would fail the dead-link gate on any citation without a matching
  need, even though every ``derives_from`` usage inside ``Needs/`` today
  happens to cite a real ``eng_need`` ID.
- ``kind`` — need classification used by ``eng_need``, e.g. ``need``.
- ``domain`` — requirement/need domain, e.g. ``functional``,
  ``operational``, ``business``.
- ``lifecycle_stage`` — lifecycle stage this need belongs to, e.g.
  ``stakeholder_needs``.

Where the ID format comes from
---------------------------------

``needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"`` enforces the
``PREFIX_rest`` shape for every need ID in this project — the same shape
each prefix column above defines per type. ``needs_id_required = True``
and ``needs_report_dead_links = True`` mean a missing ID, or a
``:links:`` field pointing at an ID that doesn't exist, fails the build
(``-W``) rather than just warning.

Not this project's types
---------------------------

The root project (one level up) is a **separate** Sphinx project with its
own ``conf.py`` and its own single need type (``org_req``) — see
``../needs_types_definition.rst``, built independently from the repo
root. See ``../STANDARDS.md`` for the full folder-to-standard crosswalk
across both projects.
