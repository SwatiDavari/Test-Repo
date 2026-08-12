Product Verification Strategy
================================

.. note::
   This file previously described verification against
   ``SYSR_*``-prefixed requirements (e.g. ``SYSR_OTA_010``) that don't
   exist anywhere in this repo — Test_Dashboard-era content, byte-
   identical to
   ``organisation/verification/iso29119/strategy/product-verification-strategy.rst``
   (which is itself the wrong place for product-specific content — see
   that file's own note). Rewritten below as this project's actual
   tailoring of the organizational template (``ORG_TESTSTRATEGY_001`` /
   :doc:`../../organisation/verification/iso29119/strategy/product-verification-strategy`)
   against Qorix Engineering Processes' real requirements.

Product verification exercises ``SYS_001`` (inter-application
communication and service discovery) and its two features —
``FEAT_A_001`` (publish-subscribe messaging) and ``FEAT_Z_001``
(service discovery) — end to end against a built product image,
independent of any single component's internal structure. Test design
follows equivalence partitioning and boundary analysis per the
ISO 29119-informed test information model, tailoring the system-level
entry/exit criteria and defect classification scheme defined in the
organizational template.
