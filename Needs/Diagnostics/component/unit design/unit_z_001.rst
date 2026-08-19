Service Registry Unit
========================

.. unit:: Service Registry Unit
   :id: UNIT_Z_001
   :version: 1.0.0
   :status: approved
   :satisfies: COMP_Z_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5

   Implements the in-memory registry of advertised service instances.

.. note::
   Implementation: ``source/c/include/diagnostics/registry.h`` +
   ``source/c/src/diagnostics/registry.c`` (``registry_advertise`` /
   ``registry_lookup`` / ``registry_withdraw``), unit-tested by
   ``source/c/tests/diagnostics/test_registry.c`` (wired into CTest via
   ``source/c/tests/CMakeLists.txt``), mirroring
   ``PROC_UNIT_Z_001``/``TC_UNIT_Z_001`` step by step: advertise S1,
   lookup returns S1; advertise S2 for the same service type, lookup
   returns both side by side; withdraw S1, lookup returns exactly S2.
   Compiled and run directly (``gcc -std=c11 -I include
   tests/diagnostics/test_registry.c src/diagnostics/registry.c``) to
   confirm it actually builds and every assertion passes.

   This was the first ``source/`` content for the ``diagnostics`` module
   in any language — the ``source/c/include/diagnostics/``,
   ``source/c/src/diagnostics/``, and ``source/c/tests/diagnostics/``
   folders were created for it.
