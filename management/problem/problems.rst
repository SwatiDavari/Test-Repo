Problems
========

Problem reports, tracked as ``problem`` needs — migrated in-place from
``problem-register.yml`` (same id, same field values).

.. problem:: Cybersecurity authentication unit tests not yet implemented
   :id: PRB_001
   :status: open
   :affected_needs: SWR_OTA_SEC_005, SWR_DIAG_SEC_002

.. needtable::
   :types: problem
   :columns: id, title, status, affected_needs
   :style: table

``affected_needs`` is kept as free text, not a real ``:links:`` —
``SWR_OTA_SEC_005`` and ``SWR_DIAG_SEC_002`` don't resolve to any actual
need in this repo. They're the same illustrative ``PROD_X`` placeholder
ids already used elsewhere (see ``test/test-strategy/`` and
``org_verification/iso29119/strategy/``), so registering this field as a
dead-link-checked link would fail the build.
