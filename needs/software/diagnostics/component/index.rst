Diagnostics Manager — Component
=================================

Register of component-level (``comp``) design for the Diagnostics
module — one file per module, not one file per component.

.. comp:: Service Discovery Architecture
   :id: comp_z_001
   :version: 1.0.0
   :status: proposed
   :satisfies: feat_z_001
   :standard: ASPICE SWE.2 / ISO 15288 6.4.4

   Defines the structural decomposition of service discovery into
   registry, listener, and query interfaces.

.. note::
   **2026-08-22:** ``requirements/index`` removed from the toctree below.
   It was a byte-for-byte copy of
   ``software/communication/component/requirements/index.rst`` — same
   title ("Communication Module — Feature Requirements"), same 49
   ``FEAT_COM_*`` IDs — duplicating those IDs in this build (sphinx-needs
   does not allow the same ``:id:`` defined twice) rather than describing
   anything about Diagnostics/service discovery. Moved to ``_to_delete/``
   at the repo root pending manual delete rather than deleted outright.
   Diagnostics does not currently have a detailed feature-requirements
   register of its own beyond ``feat_z_001`` above — flagged here as a
   real gap, not filled with placeholder content.

.. toctree::
   :maxdepth: 1

   integration_test_cases
   unit design/units
   unit test/index
