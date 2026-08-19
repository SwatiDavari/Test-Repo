Unit Test Cases — communication
==================================

.. note::
   This folder previously contained a byte-for-byte copy of the root
   ``test/`` tree's system-level content (``TC_SYS_STARTUP_001``,
   referencing ``SYS_001`` and an OTA-firmware scenario unrelated to this
   module). Rewritten to actually cover this module's unit-level design,
   ``UNIT_A_001`` — and, this pass, converted from a plain prose
   "Covers: UNIT_A_001" line into a real ``tc`` need below, so the link
   to ``UNIT_A_001`` is dead-link-checked instead of just narrative text.

.. warning::
   Content mismatch, flagged not silently fixed: ``UNIT_A_001`` ("Proxy
   Serialization Unit") implements message serialization/deserialization
   in the proxy layer. The test case below instead describes
   publish/subscribe dispatch behavior (payload delivery to subscriber
   callbacks by topic) — that's a different unit's responsibility, not
   this one's. Either ``TC_UNIT_A_001`` needs a serialization/
   deserialization scenario, or it needs to link to whichever unit
   actually implements the dispatch routine (no such unit exists yet
   under ``needs/communication/component/unit design/``). Left as-is
   pending that decision.

.. tc:: Publish/subscribe dispatch — unit
   :id: TC_UNIT_A_001
   :version: 1.0.0
   :status: proposed
   :asil: ASIL B
   :verifies: UNIT_A_001

   Unit-level verification (no process boundary, no network, no
   timeout): given a message payload and a subscriber callback
   registered on a topic, confirm the routine delivers the exact payload
   to that callback exactly once and does not invoke callbacks
   registered on other topics. See :doc:`../../../feature/feat_a_001` for
   the corresponding end-to-end (feature-level) verification of the same
   behavior across a real timeout window, which belongs in
   ``integration test/`` at the root, not here.

Owner: communication module owner. Status: draft — no automated test
implementation is wired up yet under ``source/`` for this case.
