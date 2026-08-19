Communication Manager — Component
=======================================

.. note::
   This file previously contained a byte-identical duplicate of
   ``Needs/Communication/feature/index.rst`` — the same orphaned
   ``FEAT_DIAGNOSTICS_001`` stub. Replaced with real content and wired
   into :doc:`../index`.

.. toctree::
   :maxdepth: 1

   comp_a_001
   requirements/index
   itc_comp_a_001
   unit design/unit_a_001
   unit test/index

.. note::
   ``unit design/`` and ``unit test/`` are wired in from here, not the
   module-level ``../index.rst`` — matching
   ``diagnostics/component/index.rst``'s layout and its own note on the
   same point. ``../index.rst`` previously (and incorrectly) tried to
   reference them one level too shallow; fixed there, added here,
   verified with a real ``-W`` build.
