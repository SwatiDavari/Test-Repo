Platform-Level Safety Analyses
=================================

Analyses that look across module boundaries rather than at a single
Safety Goal chain. These sit alongside the safety-goal/FSR/TSR registers
(``../safety_goals``, ``../functional_safety_requirements``,
``../technical_safety_requirements``) because they reference the same
real component and unit IDs, but they
don't themselves derive a new Safety Goal — they test whether the existing
one (``SG_001``) actually holds once modules are combined.

.. toctree::
   :maxdepth: 1

   dependent-failure-analysis
   fmea
