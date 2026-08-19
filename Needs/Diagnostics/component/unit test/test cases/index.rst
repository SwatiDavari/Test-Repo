Unit Test Cases — diagnostics
================================

.. note::
   This folder previously contained a byte-for-byte copy of
   ``communication``'s unit-test content (``TC_UNIT_A_001``, referencing
   ``UNIT_A_001`` and ``feat_a_001.rst``) — a leftover from copying the
   folder structure across modules that was never updated for
   diagnostics. Rewritten to actually cover this module's unit-level
   design, ``UNIT_Z_001`` — and, this pass, converted from a plain prose
   "Covers: UNIT_Z_001" line into a real ``tc`` need below, so the link
   to ``UNIT_Z_001`` is dead-link-checked instead of just narrative text.

.. tc:: Service registry advertise/lookup/withdraw — unit
   :id: TC_UNIT_Z_001
   :version: 1.0.0
   :status: draft
   :verifies: UNIT_Z_001

   Unit-level verification (no process boundary, no network, no
   timeout): given a registry constructed with no advertised instances,
   confirm that advertising a service instance makes it visible to a
   lookup by service type, that a second instance advertised for the
   same service type is returned alongside the first (not replacing
   it), and that withdrawing an instance removes it from subsequent
   lookups. See :doc:`../../../feature/feat_z_001` for the corresponding
   end-to-end (feature-level) verification of service discovery across a
   real runtime, which belongs in ``integration test/`` at the root, not
   here.

Owner: diagnostics module owner. Status: draft — no automated test
implementation is wired up yet under ``source/`` for this case.
