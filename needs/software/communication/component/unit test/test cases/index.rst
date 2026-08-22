Unit Test Cases — communication
==================================

.. note::
   Covers this module's unit-level design via a real ``tc`` need below
   rather than free-text prose, so the link is dead-link-checked.

.. note::
   **2026-08-21: resolved the content mismatch flagged below (kept for
   history).** Added ``unit_com_evttrig_019`` ("Topic-scoped event
   dispatch isolation") to
   ``needs/software/communication/component/unit design/units.rst`` to
   cover the dispatch/isolation behavior this test case actually
   verifies, and retargeted ``:verifies:`` at it. The old link target,
   ``UNIT_A_001``, no longer exists anywhere in this project — a stale
   ID left over from before ``units.rst`` was consolidated into its
   current ``UNIT_COM_*`` scheme; it was never redefined post-reorg,
   which is what made the outgoing link permanently unresolvable rather
   than just semantically off.

   *Original note, now resolved*: ``UNIT_A_001`` ("Proxy Serialization
   Unit") implemented message serialization/deserialization in the
   proxy layer. This test case instead describes publish/subscribe
   dispatch behavior (payload delivery to subscriber callbacks by
   topic) — a different unit's responsibility, not that one's. Either
   this test case needed a serialization/deserialization scenario
   instead, or it needed to link to whichever unit actually implements
   the dispatch routine (no such unit existed yet). Resolved via the
   latter.

.. tc:: Publish/subscribe dispatch — unit
   :id: tc_unit_a_001
   :version: 1.0.0
   :status: proposed
   :asil: ASIL B
   :verifies: unit_com_evttrig_019

   Unit-level verification (no process boundary, no network, no
   timeout): given a message payload and a subscriber callback
   registered on a topic, confirm the routine delivers the exact payload
   to that callback exactly once and does not invoke callbacks
   registered on other topics. See :doc:`../../../feature/index` for
   the corresponding end-to-end (feature-level) verification of the same
   behavior across a real timeout window, which belongs in
   ``testing/`` at the root, not here.

Owner: communication module owner. Status: draft — no automated test
implementation is wired up yet under ``source/`` for this case.
