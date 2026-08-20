Component Integration Test Cases — Service Discovery Architecture
=====================================================================

.. note::
   This is a newly-added artifact — component-integration verification
   previously didn't exist for this module at all; the chain jumped
   straight from unit test (``TC_UNIT_Z_001``) to the root-level
   system/feature test in ``integration test/``.

.. itc:: Registry wiring — registry unit inside the component
   :id: ITC_COMP_Z_001_001
   :version: 1.0.0
   :status: proposed
   :verifies: COMP_Z_001

   Verifies that ``UNIT_Z_001`` (the in-memory service registry) is
   correctly wired into ``COMP_Z_001``'s registry/listener/query
   decomposition: a service instance advertised through the registry
   unit is actually observable through the component's listener and
   query interfaces, not just within the registry unit in isolation.
   This is below full system integration — no other component, no
   network — it only verifies this component's own internal wiring.

   Status: draft. No automated test implementation exists yet, and (see
   ``UNIT_Z_001``'s own ``implementation`` field) there is no real
   implementation behind the registry unit to test against yet either —
   this test case documents the intended verification, not a result.
