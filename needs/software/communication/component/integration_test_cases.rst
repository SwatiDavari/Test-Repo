Communication Manager — Component Integration Test Cases
=============================================================

Register of component-integration test case (``itc``) needs for the
Communication module — below full system integration (no other
component, no network); each entry verifies a component's own internal
wiring. Add new integration test cases here as additional
``.. itc::`` directives.

.. itc:: Proxy layer wiring — serialization unit inside the component
   :id: itc_comp_a_001_001
   :version: 1.0.0
   :status: proposed
   :asil: ASIL B
   :verifies: comp_a_001

   Verifies that ``UNIT_A_001`` (the proxy-layer serialization/
   deserialization routine) is correctly wired into ``comp_a_001``'s
   proxy/skeleton/binding decomposition: a message serialized by the
   proxy layer and passed through the skeleton/binding layers
   deserializes back to an identical message on the other side, with no
   data loss or corruption introduced at the layer boundaries.

   Status: draft. No automated test implementation exists yet, and (see
   ``UNIT_A_001``'s own ``implementation`` field) there is no real
   implementation behind the serialization unit to test against yet
   either — this test case documents the intended verification, not a
   result.
