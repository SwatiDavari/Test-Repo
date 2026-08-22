Operational Needs
==================

.. note::
   Previously described degraded operation for an interrupted OTA update
   — Test_Dashboard's scope. Rewritten around this repo's real service-
   discovery dependency.

.. eng_need:: Controlled operation when service discovery is degraded
   :id: need_ops_001
   :kind: need
   :domain: operational
   :lifecycle_stage: stakeholder_needs
   :version: 1.0.0
   :status: proposed
   :derives_from: need_disc_001

   The platform needs to remain in a controlled, diagnosable state if the
   service-discovery registry (``comp_z_001``) becomes unavailable or
   stale, rather than leaving dependent application instances unable to
   communicate at all. This is the same open dependency this repo's
   dependent-failure analysis already flags between Communication and
   Diagnostics (see ``Needs/safety/analyses/dependent-failure-analysis``).
