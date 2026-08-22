Communication Module — Features
===================================

Register of feature-level (``feat``) requirements for the Communication
module — one file per module, not one file per feature. Add new
Communication features here as additional ``.. feat::`` directives.

.. feat:: Publish-Subscribe Messaging
   :id: feat_a_001
   :version: 1.0.0
   :status: proposed
   :satisfies: sys_msgdisc_001
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
   (``feat_com_arch_001``-``003`` architecture style, ``feat_com_ifc_001``-``012``
   interfaces, ``feat_com_safety_001``-``006`` safety properties,
   ``feat_com_perf_001``-``012`` performance/shared-memory behavior,
   ``feat_com_binding_001``-``008`` language/binding support,
   ``feat_com_vm_001``-``002`` VM data sharing, ``feat_com_deploy_001``
   deployment config, ``feat_com_trace_001`` tracing, and
   ``feat_com_acl_001``-``004`` access control); plus 4 IPC sub-feature
   requirements (``feat_com_ipc_001``–``feat_com_ipc_004``), and 5 SOME/IP
   Gateway requirements (``feat_com_someip_001``–``feat_com_someip_005``).

.. toctree::
   :maxdepth: 1

   requirements/index
