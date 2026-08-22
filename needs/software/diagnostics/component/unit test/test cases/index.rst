Unit Test Cases — diagnostics
================================

.. note::
   Covers this module's unit-level design, ``unit_z_001``, via a real
   ``tc`` need below rather than free-text prose, so the link is
   dead-link-checked.

.. tc:: Service registry advertise/lookup/withdraw — unit
   :id: tc_unit_z_001
   :version: 1.0.0
   :status: proposed
   :verifies: unit_z_001

   Unit-level verification (no process boundary, no network, no
   timeout): given a registry constructed with no advertised instances,
   confirm that advertising a service instance makes it visible to a
   lookup by service type, that a second instance advertised for the
   same service type is returned alongside the first (not replacing
   it), and that withdrawing an instance removes it from subsequent
   lookups. See :doc:`../../../feature/index` for the corresponding
   end-to-end (feature-level) verification of service discovery across a
   real runtime, which belongs in ``testing/`` at the root, not
   here.

Owner: diagnostics module owner. Status: draft — no automated test
implementation is wired up yet under ``source/`` for this case.
