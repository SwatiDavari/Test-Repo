Proxy Serialization Unit
==========================

.. unit:: Proxy Serialization Unit
   :id: UNIT_A_001
   :version: 1.0.0
   :status: proposed
   :asil: ASIL B
   :satisfies: COMP_A_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5

   Implements serialization and deserialization of messages within the
   proxy layer.

.. note::
   Implementation: ``source/c/include/communication/serializer.h`` +
   ``source/c/src/communication/serializer.c`` (``serializer_encode`` /
   ``serializer_decode``), unit-tested by
   ``source/c/tests/communication/test_serializer.c`` (wired into CTest
   via ``source/c/tests/CMakeLists.txt``). Compiled and run directly
   (``gcc -std=c11 -I include tests/communication/test_serializer.c
   src/communication/serializer.c``) to confirm it actually builds and
   the round-trip/truncation/empty-payload assertions pass — this is not
   just a file sitting in the tree.

   ``source/c/include/communication/router.h`` /
   ``router.c`` (``router_add(int, int)``) are unrelated placeholder code
   sharing this module's name — not part of this unit's implementation.
