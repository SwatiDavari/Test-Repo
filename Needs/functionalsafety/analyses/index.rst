Platform-Level Safety Analyses
=================================

Analyses that look across module boundaries rather than at a single
Safety Goal chain. These sit alongside ``sg_001`` / ``fsr_001`` / ``tsr_001``
because they reference the same real component and unit IDs, but they
don't themselves derive a new Safety Goal — they test whether the existing
one (``SG_001``) actually holds once modules are combined.

.. toctree::
   :maxdepth: 1

   dependent-failure-analysis
   fmea
