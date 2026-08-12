Changes
=======

Change requests, tracked as ``change`` needs — migrated in-place from
``change-register.yml`` (same id, same field values).

.. change:: Migrate repository to enterprise component-centric filesystem
   :id: CR_001
   :status: approved
   :affected_needs: SYSR_OTA_010, SYSR_DIAG_010, SYSR_LOG_010

.. needtable::
   :types: change
   :columns: id, title, status, affected_needs
   :style: table

``affected_needs`` is kept as free text, not a real ``:links:``, for the
same reason as on :doc:`../problem/problems` — these ids are illustrative
placeholders, not real needs in this repo.
