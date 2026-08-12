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
   * - Communication (``COMP_A_001``)
     - Yes
     - ``SG_001`` -> ``FSR_001`` -> ``TSR_001`` -> ``COMP_A_001`` -> ``UNIT_A_001``
   * - Diagnostics (``COMP_Z_001``)
     - Not yet assessed
     - No ``sg``/``fsr``/``tsr`` need currently links to it

Open finding — shared runtime resources between COMP_A_001 and COMP_Z_001
----------------------------------------------------------------------------

``TSR_001`` requires the Communication Manager's proxy layer (``COMP_A_001``)
to reject delivery to any subscriber whose authorization token has not been
validated. ``COMP_Z_001`` (Service Discovery) advertises and looks up the
same service instances that the proxy layer delivers messages to.

If both components run in the same process/address space, or share the
same registry/cache used for token or instance lookups, a fault in Service
Discovery (e.g. a stale or corrupted registry entry) could cause the proxy
layer to treat an unauthorized instance as valid — defeating ``TSR_001``
without ``TSR_001`` itself being violated in isolation. This has not been
confirmed either way; it depends on the actual process/memory architecture,
which is not yet documented anywhere in this repo.

**This open finding is not resolved.** Until it is, this analysis should be
treated as incomplete rather than as a cleared safety case.

Diagnostics — not yet assessed
----------------------------------

``COMP_Z_001`` / ``FEAT_Z_001`` / ``UNIT_Z_001`` have no Safety Goal, FSR,
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
