Stakeholder Needs
=================

.. note::
   This file previously described OTA/diagnostics/logging needs for a
   product named "product-x" — Test_Dashboard's scope, not this repo's.
   The real features in Qorix Engineering Processes are Communication (publish-subscribe
   messaging, ``FEAT_A_001``) and Diagnostics (service discovery,
   ``FEAT_Z_001``), both under the shared system requirement ``SYS_MSGDISC_001``.
   Rewritten below to actually describe this product.

.. eng_need:: Reliable, authorized inter-application messaging
   :id: NEED_COMM_001
   :kind: need
   :domain: functional
   :lifecycle_stage: stakeholder_needs
   :version: 1.0.0
   :status: proposed
   :tags: communication

   Application developers need adaptive application instances to exchange
   messages reliably over a publish-subscribe channel, with delivery
   restricted to instances that are authorized subscribers.

.. eng_need:: Runtime discovery of available services
   :id: NEED_DISC_001
   :kind: need
   :domain: functional
   :lifecycle_stage: stakeholder_needs
   :version: 1.0.0
   :status: proposed
   :tags: diagnostics

   Application developers need adaptive application instances to discover
   available service instances at runtime, without a fixed, build-time
   wiring of endpoints.

.. eng_need:: Freedom from unintended actuation via message spoofing
   :id: NEED_SAFE_001
   :kind: need
   :domain: safety
   :lifecycle_stage: stakeholder_needs
   :version: 1.0.0
   :status: proposed
   :tags: safety
   :derives_from: SG_001

   Vehicle stakeholders need assurance that no application instance can
   trigger unintended actuation by receiving a message it was never an
   authorized subscriber for — the stakeholder-level statement of what
   ``SG_001`` (Prevent Unauthorized Message Delivery) formalizes as a
   safety goal.
