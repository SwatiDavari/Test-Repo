Dependent Failure Analysis
=============================

Scope
-----

ISO 26262-9 clause 7 requires checking whether elements that are treated
as independent in the safety concept actually share a common cause of
failure. Two modules currently exist under ``Needs/``:

.. list-table::
   :header-rows: 1

   * - Module
     - Safety-relevant?
     - Chain
   * - Communication (``comp_a_001``)
     - Yes
     - ``sg_001`` -> ``fsr_001`` -> ``tsr_001`` -> ``comp_a_001`` -> ``UNIT_A_001``
   * - Diagnostics (``comp_z_001``)
     - Not yet assessed
     - No ``sg``/``fsr``/``tsr`` need currently links to it

Open finding — shared runtime resources between comp_a_001 and comp_z_001
----------------------------------------------------------------------------

``tsr_001`` requires the Communication Manager's proxy layer (``comp_a_001``)
to reject delivery to any subscriber whose authorization token has not been
validated. ``comp_z_001`` (Service Discovery) advertises and looks up the
same service instances that the proxy layer delivers messages to.

If both components run in the same process/address space, or share the
same registry/cache used for token or instance lookups, a fault in Service
Discovery (e.g. a stale or corrupted registry entry) could cause the proxy
layer to treat an unauthorized instance as valid — defeating ``tsr_001``
without ``tsr_001`` itself being violated in isolation. This has not been
confirmed either way; it depends on the actual process/memory architecture,
which is not yet documented anywhere in this repo.

**This open finding is not resolved.** Until it is, this analysis should be
treated as incomplete rather than as a cleared safety case.

Diagnostics — not yet assessed
----------------------------------

``comp_z_001`` / ``feat_z_001`` / ``unit_z_001`` have no Safety Goal, FSR,
or TSR pointing at them. Before this DFA can be considered complete, someone
needs to confirm whether Diagnostics is safety-relevant at all (in which
case it needs its own ``sg``/``fsr``/``tsr`` chain) or whether it's out of
scope (in which case that should be stated explicitly here, the way
Test_Dashboard's Logging feature states "no safety/security relevance
identified").

Summary
--------

.. list-table::
   :header-rows: 1

   * - Item
     - Status
   * - Communication vs. Diagnostics shared-resource risk
     - Open — not resolved
   * - Diagnostics safety relevance
     - Not assessed
   * - Overall DFA status
     - Incomplete
