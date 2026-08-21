Functional Safety Requirements
=================================

Register of Functional Safety Requirement (``fsr``) needs, decomposed
from the safety goals in :doc:`safety_goals` — new FSRs are added here,
not as new files.

.. fsr:: Subscriber authorization check
   :id: FSR_001
   :version: 1.0.0
   :status: proposed
   :asil: ASIL B
   :links: SG_001
   :standard: ISO 26262-3 clause 8 (Functional Safety Concept)

   The communication component shall verify that a subscriber is
   authorized before delivering any message to it.
