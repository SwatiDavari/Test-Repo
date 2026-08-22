Diagnostics Manager — Component Integration Test Cases
===========================================================

Register of component-integration test case (``itc``) needs for the
Diagnostics module — below full system integration (no other component,
no network); each entry verifies a component's own internal wiring.
Add new integration test cases here as additional ``.. itc::``
directives.

.. itc:: Registry wiring — registry unit inside the component
   :id: itc_comp_z_001_001
   :version: 1.0.0
   :status: proposed
   :verifies: comp_z_001

   Verifies that ``unit_z_001`` (the in-memory service registry) is
   correctly wired into ``comp_z_001``'s registry/listener/query
   decomposition: a service instance advertised through the registry
   unit is actually observable through the component's listener and
   query interfaces, not just within the registry unit in isolation.

   Status: draft. No automated test implementation exists yet, and (see
   ``unit_z_001``'s own ``implementation`` field) there is no real
   implementation behind the registry unit to test against yet either —
   this test case documents the intended verification, not a result.
