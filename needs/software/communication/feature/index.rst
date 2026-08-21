Communication Module — Features
===================================

Register of feature-level (``feat``) requirements for the Communication
module — one file per module, not one file per feature. Add new
Communication features here as additional ``.. feat::`` directives.

.. feat:: Publish-Subscribe Messaging
   :id: FEAT_A_001
   :version: 1.0.0
   :status: proposed
   :satisfies: SYS_MSGDISC_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3

   The communication component shall support publish-subscribe messaging
   between adaptive application instances.

.. note::
   58 further requirements, converted from the eclipse-score
   ``docs/features/communication/`` reference supplied for this
   conversion, are registered in :doc:`requirements/index` rather than
   here — the detailed register this module's own toctree entry below
   already points at, kept separate from this file's single illustrative
   example: 49 top-level Communication requirements, grouped by topic
   (``FEAT_COM_ARCH_001``-``003`` architecture style, ``FEAT_COM_IFC_001``-``012``
   interfaces, ``FEAT_COM_SAFETY_001``-``006`` safety properties,
   ``FEAT_COM_PERF_001``-``012`` performance/shared-memory behavior,
   ``FEAT_COM_BINDING_001``-``008`` language/binding support,
   ``FEAT_COM_VM_001``-``002`` VM data sharing, ``FEAT_COM_DEPLOY_001``
   deployment config, ``FEAT_COM_TRACE_001`` tracing, and
   ``FEAT_COM_ACL_001``-``004`` access control); plus 4 IPC sub-feature
   requirements (``FEAT_COM_IPC_001``–``FEAT_COM_IPC_004``), and 5 SOME/IP
   Gateway requirements (``FEAT_COM_SOMEIP_001``–``FEAT_COM_SOMEIP_005``).

.. toctree::
   :maxdepth: 1

   requirements/index
