Platform-Level FMEA
=======================

Failure modes for the elements that currently carry a safety chain.
Diagnostics is excluded below because it has no safety chain yet (see the
Dependent Failure Analysis in this same folder).

.. list-table::
   :header-rows: 1

   * - Failure mode
     - Effect
     - Cause
     - Current mitigation
     - Detection
     - Linked need
   * - Stale/cached authorization token accepted as valid
     - Message delivered to a subscriber that is no longer authorized,
       violating ``sg_001``
     - ``UNIT_A_001`` (Proxy Serialization Unit) deserializes a token
       without re-checking session validity
     - ``tsr_001`` requires the proxy layer to reject delivery on an
       unvalidated token
     - Not specified — no test or monitoring need currently references
       this failure mode
     - ``tsr_001``
   * - Subscriber authorization check skipped under load/error path
     - Same as above
     - ``fsr_001``'s check is bypassed by an error-handling code path not
       covered by any current design need
     - None documented
     - None documented
     - ``fsr_001``

Coverage by module
---------------------

.. list-table::
   :header-rows: 1

   * - Module
     - FMEA coverage
   * - Communication (``comp_a_001``)
     - Partial — two failure modes identified, neither has a documented
       detection mechanism
   * - Diagnostics (``comp_z_001``)
     - Not analyzed — see Dependent Failure Analysis for why

This FMEA is a starting point, not a completed analysis: both entries above
have "None documented" or unspecified detection, which is itself a gap that
should be closed before this is treated as evidence of a mitigated design.
