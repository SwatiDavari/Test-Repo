Communication Manager -- Unit Design
======================================

Register of unit-level (``unit``) design for the Communication module --
one file per module. The entries below are the first real content in this
register: AUTOSAR Adaptive Platform Communication Management SWS
requirements (``AUTOSAR_AP_SWS_CommunicationManagement.pdf``, AP R23-11),
scoped to SOME/IP network binding and the core, binding-agnostic ara::com
API, converted 1:1 (222 of them) plus 10 compressed representative entries
covering the granular wire-format/per-field-type clusters that were too
numerous to convert individually (see the note on
``SOME/IP Payload Serialization and Method/Field Handling (compressed
reference)`` below).

Each ``unit::`` need's ``:satisfies:`` points at one of the new topic-level
``comp::`` entries in :doc:`../index` (``COMP_COM_PARADIGM_001``-``COMP_COM_SERDES_001``), not
at ``COMP_A_001``-``COMP_COM_IPC_001`` -- those remain the eclipse-score-derived
IPC/Communication-Manager architecture, a separate part of this module.

.. note::
   ``UNIT_A_001`` is intentionally **not** defined here. It is already
   referenced narratively elsewhere in this repo (``needs_types_definition.rst``'s
   ASIL table, ``functionalsafety/analyses/fmea.rst``) as the proxy-layer
   serialization/session-handling unit in the safety chain
   ``SG_001`` -> ``FSR_001`` -> ``TSR_001`` -> ``COMP_A_001`` -> ``UNIT_A_001``.
   That is a distinct scope (the IPC/shared-memory Communication Manager) from
   this AUTOSAR SOME/IP conversion, and giving it a real definition is left
   for whoever does that safety-chain work, not decided here. This register's
   own new content starts at ``UNIT_COM_PARADIGM_001``.

.. unit:: Active subscriber
   :id: UNIT_COM_PARADIGM_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_PARADIGM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12002

   The active subscriber shall be an adaptive application that has invoked the Subscribe
   method of the respective: - Trigger class (see [SWS_CM_00723]) or - Field or Event class
   (see [SWS_CM_00141]) and has not canceled the subscription by invoking the Unsubscribe
   method of the respective: - Trigger class (see [SWS_CM_00810]) or - Field or Event class
   (see [SWS_CM_00151])

.. unit:: Active subscriber when SOME/IP Network binding is used
   :id: UNIT_COM_PARADIGM_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_PARADIGM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12003

   In addition to [SWS_CM_12002], if SOME/IP Network binding is used to provide services
   for an application, the active subscriber shall be an adaptive application for which the
   SOME/IP services subscription has not yet expired when the TTL contained in the
   respective SOME/IP SubscribeEventgroup message has been exceeded (see [SWS_CM_00205]).

.. unit:: Service interface version evaluation for backwardscompatibility
   :id: UNIT_COM_PARADIGM_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_PARADIGM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_99003

   The version of ServiceInterfaceDeployment shall be evaluated by the Service Discovery in
   terms of backwards-compatibility based on the used network binding for service
   connection.

.. unit:: SOME/IP Compliance
   :id: UNIT_COM_SOMEIP_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SOMEIP_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10000

   The SOME/IP network binding shall implement the SOME/IP Protocol and the SOME/IP Service
   Discovery Protocol defined in [4] and [6].

.. unit:: Payload Byte order definition
   :id: UNIT_COM_SOMEIP_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SOMEIP_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10172

   The byte order of the parameters inside the payload shall be defined according to
   [PRS_SOMEIP_00369] by byteOrder of ApSomeipTransformationProps.

.. unit:: Session handling state
   :id: UNIT_COM_SOMEIP_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SOMEIP_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10240

   In case of normal (i.e., non Fire and Forget) method calls or getters and setters of
   Fields (i.e., in case of SOME/IP messages of type REQUEST, RESPONSE, and ERROR) or if
   segmentation of SOME/IP messages needs to be performed (i.e. [SWS_CM_10454] and
   [SWS_CM_10455] and [SWS_CM_10456] apply and [SWS_CM_10457] does not apply) the Session
   handling shall be Active. Otherwise, the Session handling shall be Inactive.

.. unit:: Static service connection
   :id: UNIT_COM_SOMEIP_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SOMEIP_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_02201

   The static connection of services which are bound to SOME/IP protocols shall be
   preformed by statically pre-configured application end-points as described in the
   TPS_ManifestSpecification for a ProvidedSomeipServiceInstance by [TPS_MANI_03312],
   [TPS_MANI_03313] and for a RequiredSomeipServiceInstance by [TPS_MANI_03314],
   [TPS_MANI_03315], [TPS_MANI_03316].

.. unit:: Service Discovery is bypassed by static service connection
   :id: UNIT_COM_SOMEIP_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SOMEIP_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_02202

   The service discovery protocols are bypassed in case of a static service connection.c ()

.. unit:: Service versioning is not checked at runtime in case of a static service connection
   :id: UNIT_COM_SOMEIP_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SOMEIP_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_02203

   Service versions are not checked at run-time in case of a static service connection
   since the Service Discovery has been bypassed.c() Note: ara::com language APIs are
   agnostic to static service connection. 7.4.1.2 Service Discovery 7.4.1.2.1 Start of
   service discovery protocol

.. unit:: Handling of an ServiceInterface that does not contain any events, methods, or fields
   :id: UNIT_COM_SOMEIP_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SOMEIP_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10458

   If a SomeipServiceInterfaceDeployment is defined for a ServiceInterface that does not
   contain any events, methods, or fields and a ProvidedSomeipServiceInstance is defined in
   the ServiceInstanceManifest that points to the SomeipServiceInterfaceDeployment in the
   role serviceInterface then: - the ServiceInterface shall be offered over SOME/IP as
   defined by [SWS_CM_00203] which means that the Endpoint Option shall include the IP-
   Address, Port Number and Protocol as defined by the ProvidedSomeipServiceInstance - the
   Server shall not create a UDP/TCP socket and shall not bind any socket to the configured
   server address

.. unit:: Start of service discovery protocol on Server side
   :id: UNIT_COM_SD_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00201

   The registration of a new offered service which is bound to SOME/IP by invoking the
   OfferService method (see [SWS_CM_00101]) of the ServiceSkeleton class shall trigger the
   start of the initial wait phase of the SOME/IP service discovery protocol after link up
   according to [PRS_SOMEIPSD_00133].

.. unit:: Start of service discovery protocol on Client side
   :id: UNIT_COM_SD_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00209

   When invoking the FindService methods (see [SWS_CM_00122] and [SWS_CM_00622]) or the
   StartFindService methods (see [SWS_CM_00123] and [SWS_CM_00623]) of the ServiceProxy
   class, such a search request shall be considered as issuing an internal service request
   as used in [PRS_SOMEIPSD_00435]. FindService shall not wait for offer messages, but only
   check information available within the local AP-instance (StartFindService shall also
   not wait for offer messages as it only registers a handler).c (RS_CM_00204, RS_CM_00102,
   RS_SOMEIPSD_00024, RS_SOMEIPSD_00008) Note: The result of a FindService call depends on
   the already received offers, hence multiple calls might be necessary to find a service
   instance at all. Also, the number of found service instances might vary for subsequent
   calls of FindService. Note for [SWS_CM_00201] and [SWS_CM_00209]: See also
   [PRS_SOMEIPSD_00395], [PRS_SOMEIPSD_00397], [PRS_SOMEIPSD_00399], [PRS_SOMEIPSD_00416],
   [PRS_SOMEIPSD_00435], [PRS_SOMEIPSD_00752], [PRS_SOMEIPSD_00133], [PRS_SOMEIPSD_00805]
   and [PRS_SOMEIPSD_00751]. The different phases of SOME/IP Service Discovery on the
   Client side are configured in the Manifest in the SomeipSdClientServiceInstanceConfig
   referenced in RequiredSomeipServiceInstance element in the role sdClientConfig. The
   configuration is described in more detail in TPS_ManifestSpecification by -
   [TPS_MANI_03026] (Initial Wait Phase), - [TPS_MANI_03027] (Repetition Phase). The
   corresponding timing parameters for these phases are configured via InitialSdDelayConfig
   in the role initialFindBehavior, and RequestResponseDelay in the role
   requestResponseDelay. The sharing of timers is described in [TPS_MANI_03231]. 7.4.1.2.2
   FindService message

.. unit:: Periodic link state monitoring
   :id: UNIT_COM_SD_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11374

   The SOME/IP network binding shall periodically monitor and obtain the current link state
   of the underlying network interfaces. Note: This information is required since the
   behavior of SOME/IP service discovery is influenced by the current link state as well as
   by changes in the link state

.. unit:: SOME/IP FindService message
   :id: UNIT_COM_SD_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00202

   The fields in the SOME/IP FindService message shall be as follows: - The Type field and
   the TTL field shall be set to values suitable for a FindService entry, which means that
   – The Type field shall be set to FindService (see [PRS_SOMEIPSD_00351] for numerical
   value) – TTL for FindService messages shall not be used, and the value may be set to an
   arbitrary value. The field is only defined in the protocol for backward compatibility. -
   The Service ID field shall be set to a value derived from the Manifest where the
   SomeipServiceInterfaceDeployment element defines the serviceInterfaceId. - The Instance
   ID shall be set to a value derived from the Manifest where the
   RequiredSomeipServiceInstance element defines the requiredServiceInstanceId for the
   SomeipServiceInterfaceDeployment that is referenced by the RequiredSomeipServiceInstance
   in the role serviceInterfaceDeployment. If the requiredServiceInstanceId is set to "ALL"
   then 0xFFFF shall be used. - The Major Version field of the
   RequiredSomeipServiceInstance that is searched shall be set to a value derived from the
   Manifest where the SomeipServiceVersion element that is aggregated by the
   SomeipServiceInterfaceDeployment in the role serviceInterfaceVersion defines the
   majorVersion. - The Minor Version field of the RequiredSomeipServiceInstance that is
   searched shall be set to a value derived from the Manifest from the requiredMinorVersion
   attribute in the RequiredSomeipServiceInstance. – If versionDrivenFindBehavior is set to
   minimumMinorVersion then the Minor Version Field shall be set to 0xFFFF FFFF and all
   found services with a minor version smaller than the requiredMinorVersion shall not be
   considered for service discovery. – If versionDrivenFindBehavior is set to
   exactOrAnyMinorVersion then the Minor Version Field shall be set with the
   requiredMinorVersion. – If the minorVersion is set to "ALL", then the Minor Version
   Field shall be set to 0xFFFF FFFF. - Configuration Option shall be used in the find
   message if at least one capabilityRecord is defined in the RequiredSomeipServiceInstance
   element. The content of the Configuration Option shall be derived from the key/value
   pairs defined in each capabilityRecord.

.. unit:: Version blocklist
   :id: UNIT_COM_SD_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10202

   The service connection of a RequiredSomeipServiceInstance with a certain
   SomeipServiceVersion shall not be considered for service discovery for this instance if
   this SomeipServiceVersion is listed inside a
   RequiredSomeipServiceInstance.blocklistedVersion.c (RS_CM_00701) 7.4.1.2.3 OfferService
   message

.. unit:: SOME/IP OfferService message
   :id: UNIT_COM_SD_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00203

   The fields in the SOME/IP OfferService message shall be as follows: - The Type field and
   the TTL field shall be set to values suitable for a OfferService entry, which means that
   – The Type field shall be set to OfferService (see [PRS_SOMEIPSD_00356] for numerical
   value). – The TTL field shall be set to a value derived from the Manifest where the
   SomeipSdServerServiceInstanceConfig element that is referenced by the
   ProvidedSomeipServiceInstance in the role sdServerConfig defines the
   serviceOfferTimeToLive. - The Service ID field shall be set to a value derived from the
   Manifest where the SomeipServiceInterfaceDeployment element defines the
   serviceInterfaceId. - The Instance ID shall be set to a value derived from the Manifest
   where the ProvidedSomeipServiceInstance element defines the serviceInstanceId for the
   SomeipServiceInterfaceDeployment that is referenced by the ProvidedSomeipServiceInstance
   in the role serviceInterfaceDeployment. - Major Version field of the
   SomeipServiceInterfaceDeployment that is offered shall be set to a value derived from
   the Manifest where the SomeipServiceVersion element that is aggregated by the
   SomeipServiceInterfaceDeployment in the role serviceInterfaceVersion defines the
   majorVersion. - Minor Version field of the SomeipServiceInterfaceDeployment that is
   offered shall be set to a value derived from the Manifest where the SomeipServiceVersion
   element that is aggregated by the SomeipServiceInterfaceDeployment in the role
   serviceInterfaceVersion defines the minorVersion. - The Endpoint Option(s) shall be set
   in the following way: – An IPv4 Endpoint Option shall be used if the Machine to which
   the ProvidedSomeipServiceInstance is mapped with the ServiceInstanceToMachineMapping
   provides an EthernetCommunicationConnector that refers to a NetworkEndpoint in the role
   unicastNetworkEndpoint where an IPv4 Address is configured in the Ipv4Configuration
   element. – An IPv6 Endpoint Option shall be used if the Machine to which the
   ProvidedSomeipServiceInstance is mapped with the ServiceInstanceToMachineMapping
   provides an EthernetCommunicationConnector that refers to a NetworkEndpoint in the role
   unicastNetworkEndpoint where an IPv6 Address is configured in the Ipv6Configuration
   element. – The Transport Layer Protocol used in the IPv4 Endpoint option and/or IPv6
   Endpoint option shall be derived from the Manifest where the
   SomeipServiceInstanceToMachineMapping element that maps the
   ProvidedSomeipServiceInstance to an EthernetCommunicationConnector of a Machine defines
   the transport protocol and the port number. ∗ UDP shall be used if
   SomeipServiceInstanceToMachineMapping. udpPort is configured. ∗ TCP shall be used
   ifSomeipServiceInstanceToMachineMapping. tcpPort is configured. In case the port number
   (SomeipServiceInstanceToMachineMapping.udpPort or
   SomeipServiceInstanceToMachineMapping.tcpPort) is configured to 0, an ephemeral port
   shall be used. If the port number is configured to a value different from 0 exactly that
   value shall be used.

.. unit:: Cyclic interval of OfferService messages
   :id: UNIT_COM_SD_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11373

   If attribute SomeipSdServerServiceInstanceConfig.offerCyclicDelay is configured in
   SomeipSdServerServiceInstanceConfig and is greater than 0, in the Main Phase an
   OfferService entry shall be sent cyclically with an interval defined by configuration
   item SomeipSdServerServiceInstanceConfig.offerCyclicDelay. If
   SomeipSdServerServiceInstanceConfig.offerCyclicDelay is 0, no OfferService entries shall
   be sent in Main Phase for this Server Service Instance.c() 7.4.1.2.4 StopOfferService
   message

.. unit:: Service Discovery Endpoint Options
   :id: UNIT_COM_SD_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12019

   The SOME/IP-SD implementation shall support [PRS_SOMEIPSD_00547], [PRS_SOMEIPSD_00650],
   [PRS_SOMEIPSD_00651], [PRS_SOMEIPSD_00548], [PRS_SOMEIPSD_00549], [PRS_SOMEIPSD_00550],
   [PRS_SOMEIPSD_00551], [PRS_SOMEIPSD_00552], [PRS_SOMEIPSD_00856], [PRS_SOMEIPSD_00857],
   [PRS_SOMEIPSD_00854] in case of IPv4. [PRS_SOMEIPSD_00554], [PRS_SOMEIPSD_00654],
   [PRS_SOMEIPSD_00555], [PRS_SOMEIPSD_00556], [PRS_SOMEIPSD_00557], [PRS_SOMEIPSD_00558],
   [PRS_SOMEIPSD_00559], [PRS_SOMEIPSD_00837], [PRS_SOMEIPSD_00859], [PRS_SOMEIPSD_00860],
   [PRS_SOMEIPSD_00855] in case of IPv6.

.. unit:: SOME/IP StopOffer message
   :id: UNIT_COM_SD_009
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00204

   The fields in the SOME/IP StopOffer message shall be as follows: - The Type field and
   the TTL field shall be set to values suitable for a StopOffer entry, which means that –
   The Type field shall be set to OfferService (see [PRS_SOMEIPSD_00356] for numerical
   value) – The TTL fields shall be set to 0x000000 (see [PRS_SOMEIPSD_00364]) - The
   Service ID field shall be set to the same value as in the OfferService message. - The
   Instance ID field shall be set to the same value as in the OfferService message. - The
   Major Version field shall be set to the same value as in the OfferService message. - The
   Minor Version field shall be set to the same value as in the OfferService message. -
   IPv4 Endpoint Option shall be set to the same value as in the OfferService message. -
   IPv6 Endpoint Option shall be set to the same value as in the OfferService message. -
   Configuration Option shall be set to the same value as in the OfferService message.

.. unit:: Content of SOME/IP SubscribeEventgroup message
   :id: UNIT_COM_SD_010
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00205

   The fields in the SOME/IP SubscribeEventgroup message shall be as follows: - The Type
   field and the TTL field shall be set to values suitable for a SubscribeEventgroup entry,
   which means that – The Type field shall be set to SubscribeEventgroup (see
   [PRS_SOMEIPSD_00386] for numerical value) – The TTL field shall be set to a value
   derived from Manifest, where the RequiredSomeipServiceInstance element aggregates the
   SomeipRequiredEventGroup in the role requiredEventGroup. The SomeipRequiredEventGroup
   aggregates the sdClientEventGroupTimingConfig where the timeToLive is defined. - The
   Service ID shall be taken from the offer message. - The Instance ID shall be taken from
   the offer message. - Major Version shall be derived from the offer message. - The
   Eventgroup ID field shall be derived from Manifest where the
   RequiredSomeipServiceInstance element aggregates the SomeipRequiredEventGroup in the
   role requiredEventGroup. The SomeipRequiredEventGroup contains the eventGroup reference
   to the SomeipEventGroup where the eventGroupId is defined. - IPv4 Endpoint Option shall
   be sent if the offer message contains an IPv4 Endpoint Option. In this case the IPv4
   Address sent in the IPv4 Endpoint Option of the SubscribeEventgroup message is
   configured in the Manifest where the RequiredSomeipServiceInstance element is mapped
   with the ServiceInstanceToMachineMapping to an EthernetCommunicationConnector of a
   Machine. The EthernetCommunicationConnector refers to a NetworkEndpoint in the role
   unicastNetworkEndpoint where an IPv4 Address is configured in theIpv4Configuration
   element. - IPv6 Endpoint Option shall be sent if the offer message contains an IPv6
   Endpoint Option. In this case the IPv6 Address sent in the IPv6 Endpoint Option of the
   SubscribeEventgroup message is configured in the Manifest where the
   RequiredSomeipServiceInstance element is mapped with the ServiceInstanceToMachineMapping
   to an EthernetCommunicationConnector of a Machine. The EthernetCommunicationConnector
   refers to a NetworkEndpoint in the role unicastNetworkEndpoint where an IPv6 Address is
   configured in theIpv6Configuration element. - The Transport Layer Protocol used in the
   IPv4 Endpoint option and/or IPv6 Endpoint option shall be derived from the Manifest
   where the SomeipEventGroup points either to SomeipEventDeployments where the
   transportProtocol is set to udp or to tcp. The SomeipServiceInstanceToMachineMapping
   element that maps the RequiredSomeipServiceInstance to an EthernetCommunicationConnector
   of a Machine the transport protocol and the port number. – The UDP port shall be derived
   from SomeipServiceInstanceToMachineMapping.udpPort. In case the port number
   (SomeipServiceInstanceToMachineMapping.udpPort) is configured to 0, an ephemeral port
   shall be used. If the port number is configured to a value different from 0 exactly that
   value shall be used. – The TCP port shall be derived from
   SomeipServiceInstanceToMachineMapping.tcpPort. In case the port number
   (SomeipServiceInstanceToMachineMapping.tcpPort) is configured to 0, an ephemeral port
   shall be used. If the port number is configured to a value different from 0 exactly that
   value shall be used. - The InitialDataRequested flag shall be set to 1 for fields and to
   0 for events. - Reserved shall be set to 0. - Counter shall be set to 0.

.. unit:: SOME/IP SubscribeEventgroupAck message
   :id: UNIT_COM_SD_011
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00206

   The fields in the SOME/IP SubscribeEventgroupAck message shall be as follows: - The Type
   field and the TTL field shall be set to values suitable for a SubscribeEventgroupAck
   entry, which means that – The Type field shall be set to SubscribeEventgroupAck (see
   [PRS_SOMEIPSD_00391] for numerical value) – The TTL field shall be set to the same value
   as in the SubscribeEventgroup message that is answered by this SubscribeEventgroupAck
   message (see [PRS_SOMEIPSD_00391]) - The Service ID field shall be set to the same value
   as in the SubscribeEventgroup message that is answered by this SubscribeEventgroupAck
   message. - The Instance ID field shall be set to the same value as in the
   SubscribeEventgroup message that is answered by this SubscribeEventgroupAck message. -
   The Major Version field shall be set to the same value as in the SubscribeEventgroup
   message that is answered by this SubscribeEventgroupAck message. - The Eventgroup ID
   field shall be set to the same value as in the SubscribeEventgroup message that is
   answered by this SubscribeEventgroupAck message. - The Multicast Option(s) shall be set
   in the following way – An IPv4 Multicast Option shall be derived from the Manifest if a
   multicastThreshold with a value greater 0 is defined for the SomeipProvidedEventGroup
   and a ipv4MulticastIpAddress is defined for the same SomeipProvidedEventGroup. – An IPv6
   Multicast Option shall be derived from the Manifest if a multicastThreshold with a value
   greater 0 is defined for the SomeipProvidedEventGroup and a ipv6MulticastIpAddress is
   defined for the same SomeipProvidedEventGroup. – The Transport Layer Protocol shall be
   set to UDP. Only UDP is supported as transport layer protocol in the IPv4 Multicast
   Option and/or IPv6 Multicast Option. – The UDP Port shall be derived from the the
   Manifest where the ProvidedSomeipServiceInstance that aggregates the
   SomeipProvidedEventGroup has the eventMulticastUdpPort defined. - The
   InitialDataRequested flag shall be set to 1 for fields and to 0 for events. - Reserved
   shall be set to 0. - Counter shall be set to 0.

.. unit:: SOME/IP SubscribeEventgroupNack message
   :id: UNIT_COM_SD_012
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00208

   The fields in the SOME/IP SubscribeEventgroupNack message shall be as follows: - The
   Type field and the TTL field shall be set to values suitable for a
   SubscribeEventgroupNack entry, which means that – The type field shall be set to
   SubscribeEventgroupAck (see [PRS_SOMEIPSD_00394] for numerical value) – The TTL field
   shall be set to 0x000000 (see [PRS_SOMEIPSD_00394]) - The Service ID field shall be set
   to the same value as in the SubscribeEventgroup message that is answered by this
   SubscribeEventgroupNack message. - The Instance ID field shall be set to the same value
   as in the SubscribeEventgroup message that is answered by this SubscribeEventgroupNack
   message. - The Major Version field shall be set to the same value as in the
   SubscribeEventgroup message that is answered by this SubscribeEventgroupNack message. -
   The Eventgroup ID field shall be set to the same value as in the SubscribeEventgroup
   message that is answered by this SubscribeEventgroupNack message. - The
   InitialDataRequested flag shall be set to 1 for fields and to 0 for events. - Reserved
   shall be set to 0. - Counter shall be set to 0.

.. unit:: Sending SOME/IP SubscribeEventgroup messages - initial
   :id: UNIT_COM_SD_013
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10377

   The subscription to at least one Event (ServiceInterface.event) of an Eventgroup
   (SomeipEventGroup) by invoking the Subscribe method (see [SWS_CM_00141]) of the specific
   Event class of the ServiceProxy class shall cause the sending of a SOME/IP
   SubscribeEventgroup messages in case there is no active subscription for the particular
   Eventgroup (either because there was no previous subscription to this particular
   Eventgroup or the TTL of every received SubscribeGroupAck message (see [SWS_CM_00206])
   for the particular Eventgroup has already expired). The subscription to at least one
   Event of an Eventgroup by invoking the Subscribe method (see [SWS_CM_00141]) of the
   specific Event class of the ServiceProxy class shall not cause the sending of a SOME/IP
   SubscribeEventgroup messages in case there is an active subscription for the particular
   Eventgroup (because there was some previous subscription to this particular Eventgroup
   and the TTL of at least one received SubscribeGroupAck message (see [SWS_CM_00206]) for
   the particular Eventgroup has not yet expired). The client shall explicitly request
   Initial Events for Field notifier according to [PRS_SOMEIPSD_00703] and
   [PRS_SOMEIPSD_00811].

.. unit:: Sending SOME/IP SubscribeEventgroup messages - renewal
   :id: UNIT_COM_SD_014
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10381

   Upon reception of an OfferService message, a SubscribeEventgroup message shall be sent
   to refresh/renew the active subscription to the particular Eventgroup if the TTL of an
   active subscription for a particular Eventgroup has not yet expired and there is at
   least one active subscription for an Event of this Eventgroup.

.. unit:: Content of SOME/IP StopSubscribeEventgroup message
   :id: UNIT_COM_SD_015
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00207

   The fields in the SOME/IP StopSubscribeEventgroup message shall be as follows: - The
   Type field and the TTL field shall be set to values suitable for a
   StopSubscribeEventgroup entry, which means that – The Type field shall be set to
   SubscribeEventgroup (see [PRS_SOMEIPSD_00386] for numerical value) – The TTL field shall
   be set to 0x000000 (see [PRS_SOMEIPSD_00389]) - The Service ID field shall be set to the
   same value as in the SubscribeEventgroup message. - The Instance ID field shall be set
   to the same value as in the SubscribeEventgroup message. - The Major Version field shall
   be set to the same value as in the SubscribeEventgroup message. - The Eventgroup ID
   field shall be set to the same value as in the SubscribeEventgroup message. - IPv4
   Endpoint Option shall be set to the same value as in the SubscribeEventgroup message. -
   IPv6 Endpoint Option shall be set to the same value as in the SubscribeEventgroup
   message. - The InitialDataRequested flag shall be set to 1 for fields and to 0 for
   events. - Reserved shall be set to 0. - Counter shall be set to 0.

.. unit:: Sending SOME/IP StopSubscribeEventgroup messages
   :id: UNIT_COM_SD_016
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10378

   Stopping the subscription of an Event (ServiceInterface.event) of an Eventgroup
   (SomeipEventGroup) by invoking the Unsubscribe method (see [SWS_CM_00151]) of the
   specific Event class of the ServiceProxy class shall not cause the sending of a SOME/IP
   StopSubscribeEventgroup message if there are still active subscriptions for other Events
   of the same Eventgroup. Stopping the subscription of the last Event of an Eventgroup by
   invoking the Unsubscribe method (see [SWS_CM_00151]) of the specific Event class of the
   ServiceProxy class shall cause the sending of a SOME/IP StopSubscribeEventgroup message.

.. unit:: Link loss on Client side
   :id: UNIT_COM_SD_017
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11375

   In case the SOME/IP network binding detects a link loss on the client side, the SOME/IP
   service discovery shall react according to [PRS_SOMEIPSD_00752] (i.e., re-enter the
   initial wait phase once the link is up again and the service is still requested).

.. unit:: Link loss on Server side
   :id: UNIT_COM_SD_018
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SD_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11376

   In case the SOME/IP network binding detects a link loss on the server side, the SOME/IP
   service discovery shall react according to [PRS_SOMEIPSD_00751] (i.e., re-enter the
   initial wait phase once the link is up again and the service is still requested).c()
   7.4.1.3 Accumulation of SOME/IP messages

.. unit:: Data accumulation for UDP data transmission
   :id: UNIT_COM_MSGCTX_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_MSGCTX_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10387

   To allow for the transmission of multiple SOME/IP event, method request and method
   response messages within a single UDP datagram, data accumulation for UDP data
   transmission shall be supported.

.. unit:: Enabling of data accumulation for UDP data transmission
   :id: UNIT_COM_MSGCTX_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_MSGCTX_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10388

   Data accumulation for UDP data transmission over the udpPort and unicastNetworkEndpoint
   defined on the EthernetCommunicationConnector that is referenced by a
   SomeipServiceInstanceToMachineMapping shall be enabled if the attribute
   SomeipServiceInstanceToMachineMapping.udpCollectionBufferSizeThreshold is set to a
   value. In this case all event and method messages that are configured for data
   accumulation shall be aggregated in a buffer until a transmission trigger (see
   [SWS_CM_10389] and [SWS_CM_10390]) arrives and the data transmission starts.

.. unit:: Configuration of a data accumulation on a ProvidedSomeipServiceInstance for transmission over UDP
   :id: UNIT_COM_MSGCTX_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_MSGCTX_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10389

   For a ProvidedSomeipServiceInstance all method responses and events for which the
   udpCollectionTrigger is set to never shall be aggregated in a buffer until a trigger
   arrives that starts the data transmission. The following trigger options shall be
   supported: - a SOME/IP message needs to be transmitted for which the
   udpCollectionTrigger is set to always. - the udpCollectionBufferTimeout is reached for
   one of the SOME/IP message already aggregated in the buffer. - the buffer size defined
   by the attribute udpCollectionBufferSizeThreshold is reached. - adding the method
   response or event to the buffer would lead to a message larger than the maximum possible
   size (e.g. MTU size). In this case the actual buffer shall be triggered before handling
   the new event or method response.

.. unit:: Configuration of a data accumulation on a RequiredSomeipServiceInstance for transmission over UDP
   :id: UNIT_COM_MSGCTX_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_MSGCTX_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10390

   For a RequiredSomeipServiceInstance all method requests for which the
   udpCollectionTrigger is set to never shall be aggregated in a buffer until a trigger
   arrives that starts the data transmission. The following trigger options shall be
   supported: - a SOME/IP message needs to be transmitted for which the
   udpCollectionTrigger is set to always. - the udpCollectionBufferTimeout is reached for
   one of the SOME/IP message already aggregated in the buffer. - the buffer size defined
   by the attribute udpCollectionBufferSizeThreshold is reached. - adding the method
   request or event to the buffer would lead to a message larger than the maximum possible
   size (e.g. MTU size). In this case the actual buffer shall be triggered before handling
   the new event or method response.

.. unit:: Selecting elements of the ServiceInterface for SecOC transmission
   :id: UNIT_COM_MSGCTX_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_MSGCTX_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11270

   It is possible to define which elements of the ServiceInterface of the particular
   AdaptivePlatformServiceInstance shall be securedby SecOC. The selection of
   ServiceInterface elements is done by the ServiceInterfaceElementSecureComConfigthat is
   aggregated by AdaptivePlatformServiceInstance. The following configuration in the
   ServiceInterfaceElementSecureComConfig is applicable: - Methods The roles methodCall and
   methodReturn identify the method(s) that shall be sprotected by SecOC with the
   configuration settings that are available in the ServiceInterfaceElementSecureComConfig
   element. - Events The role event identifies the event(s) that shall be protected by
   SecOC with the configuration settings that are availble in the
   ServiceInterfaceElementSecureComConfig element. - Fields The roles fieldNotifier,
   getterCall, getterReturn, setterCall and setterReturn identify the field content that
   shall be protected by SecOC with the configuration settings that are available in the
   ServiceInterfaceElementSecureComConfig element.

.. unit:: Conditions for sending of a SOME/IP event message
   :id: UNIT_COM_EVTTRIG_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10287

   The sending of a SOME/IP event message shall be requested by invoking the Send method of
   the respective Event class (see [SWS_CM_00162] and [SWS_CM_90437]) - If there is static
   service connection according to [SWS_CM_02201] - If there is at least one active
   subscriber and the offer of the service containing the event has not been stopped
   (either because the TTL contained in the SOME/IP OfferService message (see
   [SWS_CM_00203]) has expired or because the StopOfferService method (see [SWS_CM_00111])
   of the ServiceSkeleton class has been called).

.. unit:: Transport protocol for sending of a SOME/IP event message
   :id: UNIT_COM_EVTTRIG_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10288

   The SOME/IP event message shall be transmitted using the transport protocol defined via
   the SomeipServiceInterfaceDeployment.eventDeployment. transportProtocol attribute (see
   [TPS_MANI_03050]).

.. unit:: Source of a SOME/IP event message
   :id: UNIT_COM_EVTTRIG_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10289

   The SOME/IP event message shall use the unicast IP address and port taken from the
   IPv4/v6 Endpoint Option (see [PRS_SOMEIPSD_00307] and [PRS_SOMEIPSD_00315]) of the
   SOME/IP OfferService message ([SWS_CM_00203]) or the server address which has been
   statically pre-configured by the static service connection according to [SWS_CM_02201]
   as source address and source port for the transmission.

.. unit:: Destination of a SOME/IP event message
   :id: UNIT_COM_EVTTRIG_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10290

   The SOME/IP event message shall use the multicast IP address and the port taken from the
   IPv4/v6 Multicast Option (see [PRS_SOMEIPSD_00326] and [PRS_SOMEIPSD_00333]) of the
   SOME/IP SubscribeEventgroupAck message (see [SWS_CM_00206]) or the client address which
   has been statically pre-configured by the static service connection according to
   [SWS_CM_02201] as destination address and destination port for the transmission if the
   threshold defined by the multicastThreshold attribute of the SomeipProvidedEventGroup
   that is aggregated by the ProvidedSomeipServiceInstance in the role eventGroup in the
   Manifest has been reached (see [PRS_SOMEIPSD_00134]). The SOME/IP event message shall
   use the unicast IP address and the port taken from the IPv4/v6 Endpoint Option (see
   [PRS_SOMEIPSD_00307] and [PRS_SOMEIPSD_00315]) of the SOME/IP SubscribeEventgroup
   message ([SWS_CM_00205]) as destination address and destination port for the
   transmission if this threshold has not been reached (see [PRS_SOMEIPSD_00134]). In case
   multiple Endpoint Options have been contained in the SOME/IP SubscribeEventgroup
   message, the one matching the selected transport protocol (see [SWS_CM_10289]) shall be
   used.

.. unit:: Content of the SOME/IP event message
   :id: UNIT_COM_EVTTRIG_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10291

   The entries in the SOME/IP event message shall be as follows: - The Service ID (see
   [PRS_SOMEIP_00245]) shall be derived from the Manifest where the
   SomeipServiceInterfaceDeployment element defines the serviceInterfaceId. - The Method ID
   (see [PRS_SOMEIP_00245]) shall be derived from the Manifest where the
   SomeipServiceInterfaceDeployment element defines the eventDeployment.eventId by adding
   0x8000 to the eventDeployment. eventId. - The Length (see [PRS_SOMEIP_00042]) shall be
   set to the length of the serialized payload in units of bytes incremented by 8 (second
   part of the SOME/IP header that is covered by the Length) - The Client ID (see
   [PRS_SOMEIP_00702]) is unused for event messages (according to [PRS_SOMEIP_00702]) and
   thus shall be set to 0x0000. - In case of inactive Session Handling, see [SWS_CM_10240],
   the Session ID (see [PRS_SOMEIP_00703]) is unused for event messages and thus shall be
   set to 0x0000 (see [PRS_SOMEIP_00932]) and [PRS_SOMEIP_00925]). In case of active
   Session Handling, see [SWS_CM_10240], the Session ID is used for event messages and thus
   shall be incremented (with proper wrap around) upon every transmission of an event
   message (see [PRS_SOMEIP_00933], [PRS_SOMEIP_00934], [PRS_SOMEIP_00521], and
   [PRS_SOMEIP_00925]). - The Protocol Version (see [PRS_SOMEIP_00052]) shall be set to
   0x01. - The Interface Version (see [PRS_SOMEIP_00053]) shall be derived from the
   Manifest where the SomeipServiceInterfaceDeployment element defines the
   serviceInterfaceVersion.majorVersion. - The Message Type (see [PRS_SOMEIP_00055]) shall
   be set to NOTIFICATION (0x02). - The Return Code (see [PRS_SOMEIP_00058] and
   [PRS_SOMEIP_00191]) is unused for event messages and thus (according to
   [PRS_SOMEIP_00925]) shall be set to E_OK (0x00). - The Payload shall contain the
   serialized payload (i.e., the serialized VariableDataPrototype composed by the
   ServiceInterface in role event) according to the SOME/IP serialization rules.

.. unit:: Checks for a received SOME/IP event message
   :id: UNIT_COM_EVTTRIG_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10292

   Upon reception of a SOME/IP event message the following checks shall be conducted: -
   Verify that the Protocol Version (see [PRS_SOMEIP_00052]) is set to 0x01. - Use the
   Length (see [PRS_SOMEIP_00042]) being larger than 8 in combination with the Message type
   (see [PRS_SOMEIP_00055]) being set to NOTIFICATION to determine that the received
   SOME/IP message is actually an event. - Use the Service ID (see [PRS_SOMEIP_00245]) and
   the serviceInterfaceId attribute of the SomeipServiceInterfaceDeployment element in the
   Manifest to determine the right ServiceInterface. - Verify that the Method ID (see
   [PRS_SOMEIP_00245]) matches 0x8000 + the eventId attribute of one of the
   SomeipEventDeployments of the SomeipServiceInterfaceDeployment. - Verify that the Client
   ID (see [PRS_SOMEIP_00702]) is set to 0x0000. - Verify that the Interface Version (see
   [PRS_SOMEIP_00053]) matches SomeipServiceInterfaceDeployment.serviceInterfaceVersion.
   majorVersion. - Verify that the Return Code (see [PRS_SOMEIP_00058] and
   [PRS_SOMEIP_00191]) is set to E_OK (0x00). If any of the above checks fails the received
   SOME/IP event message shall be discarded and and the incident shall be logged (if
   logging is enabled for the ara::com implementation).

.. unit:: Identifying the right event
   :id: UNIT_COM_EVTTRIG_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10293

   Using the Service ID (see [PRS_SOMEIP_00245]) and the serviceInterfaceId attribute of
   the SomeipServiceInterfaceDeployment element as well as the Method ID (see
   [PRS_SOMEIP_00245]) and 0x8000 + the eventId attribute of the SomeipEventDeployments of
   the SomeipServiceInterfaceDeployment, the right event shall be identified.

.. unit:: Deserializing the payload
   :id: UNIT_COM_EVTTRIG_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10294

   Based on the event determined according to [SWS_CM_10293] the Payload of the SOME/IP
   event message (i.e., the serialized VariableDataPrototype composed by the
   ServiceInterface in role event) shall be deserialized according to the SOME/IP
   serialization rules.

.. unit:: Providing the received event data
   :id: UNIT_COM_EVTTRIG_009
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10295

   The deserialized payload containing the event data shall be provided via the
   GetNewSamples (see [SWS_CM_00701]) method of the respective Event class for the event
   determined according to [SWS_CM_10293].

.. unit:: Invoke receive handler
   :id: UNIT_COM_EVTTRIG_010
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10296

   In case a receive handler was registered using the SetReceiveHandler method (see
   [SWS_CM_00181]) of the respective Event class for the event determined according to
   [SWS_CM_10293] this registered receive handler shall be invoked when the corresponding
   Event is received.

.. unit:: Silently discarding SOME/IP event messages for unsubscribed events
   :id: UNIT_COM_EVTTRIG_011
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10379

   If the event identified according to [SWS_CM_10293] does not have an active subscription
   because the Subscribe method (see [SWS_CM_00141]) of the specific Event class of the
   ServiceProxy class has not been called, or the Unsubscribe method (see [SWS_CM_00151])
   of the specific Event class of the ServiceProxy class has been called, or the TTL of the
   SOME/IP SubscribeEventgroup message (see [SWS_CM_00205]) has expired, and if there is no
   static service connection according to [SWS_CM_02201], the received SOME/IP event
   message shall be silently discarded (i.e., [SWS_CM_10294], [SWS_CM_10295], and the
   receive handler shall not be invoked).

.. unit:: Conditions for sending of a SOME/IP trigger
   :id: UNIT_COM_EVTTRIG_012
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10511

   The sending of a SOME/IP trigger shall be requested by invoking the Send method of the
   respective Trigger class (see [SWS_CM_00721]). The SOME/IP trigger shall be sent if at
   least one of the following conditions is fulfilled: - If there is static service
   connection according to [SWS_CM_02201] - If there is at least one active subscriber and
   the offer of the service containing the trigger has not been stopped (either because the
   TTL contained in the SOME/IP OfferService message (see [SWS_CM_00203]) has expired or
   because the StopOfferService method (see [SWS_CM_00111]) of the ServiceSkeleton class
   has been called).

.. unit:: Content of the SOME/IP trigger
   :id: UNIT_COM_EVTTRIG_013
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10512

   The entries in the SOME/IP trigger shall be as follows: - The Service ID (see
   [PRS_SOMEIP_00245]) shall be derived from the Manifest where the
   SomeipServiceInterfaceDeployment element defines the serviceInterfaceId. - The Method ID
   (see [PRS_SOMEIP_00245]) shall be derived from the Manifest where the
   SomeipServiceInterfaceDeployment element defines the eventDeployment.eventId by adding
   0x8000 to the eventDeployment. eventId. - The Length (see [PRS_SOMEIP_00042]) shall be
   set to 8 - The Client ID (see [PRS_SOMEIP_00702]) is unused for triggers (according to
   [PRS_SOMEIP_00702]) and thus shall be set to 0x0000. - In case of inactive Session
   Handling, see [SWS_CM_10240], the Session ID (see [PRS_SOMEIP_00703]) is unused for
   triggers and thus shall be set to 0x0000 (see [PRS_SOMEIP_00932]) and
   [PRS_SOMEIP_00925]). In case of active Session Handling, see [SWS_CM_10240], the Session
   ID is used for triggers and thus shall be incremented (with proper wrap around) upon
   every transmission of an trigger (see [PRS_SOMEIP_00933], [PRS_SOMEIP_00934],
   [PRS_SOMEIP_00521], and [PRS_SOMEIP_00925]). - The Protocol Version (see
   [PRS_SOMEIP_00051]) shall be set to 0x01. - The Interface Version (see
   [PRS_SOMEIP_00053]) shall be derived from the Manifest where the
   SomeipServiceInterfaceDeployment element defines the
   serviceInterfaceVersion.majorVersion. - The Message Type (see [PRS_SOMEIP_00055]) shall
   be set to NOTIFICATION (0x02). - The Return Code (see [PRS_SOMEIP_00058] and
   [PRS_SOMEIP_00191]) is unused for triggers and thus (according to [PRS_SOMEIP_00925])
   shall be set to E_OK (0x00).

.. unit:: Checks for a received SOME/IP trigger
   :id: UNIT_COM_EVTTRIG_014
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10513

   Upon reception of a SOME/IP trigger the following checks shall be conducted: - Verify
   that the Protocol Version (see [PRS_SOMEIP_00052]) is set to 0x01. - Use the Length (see
   [PRS_SOMEIP_00042]) being equal to 8 in combination with the Message type (see
   [PRS_SOMEIP_00055]) being set to NOTIFICATION to determine that the received SOME/IP
   message is actually a trigger. - Use the Service ID (see [PRS_SOMEIP_00245]) and the
   serviceInterfaceId attribute of the SomeipServiceInterfaceDeployment element in the
   Manifest to determine the right ServiceInterface. - Verify that the Method ID (see
   [PRS_SOMEIP_00245]) matches 0x8000 + the eventId attribute of one of the
   SomeipEventDeployments of the SomeipServiceInterfaceDeployment. - Verify that the Client
   ID (see [PRS_SOMEIP_00702]) is set to 0x0000. - Verify that the Interface Version (see
   [PRS_SOMEIP_00053]) matches SomeipServiceInterfaceDeployment.serviceInterfaceVersion.
   majorVersion. - Verify that the Return Code (see [PRS_SOMEIP_00058] and
   [PRS_SOMEIP_00191]) is set to E_OK (0x00). If any of the above checks fails the received
   SOME/IP trigger shall be discarded and and the incident shall be logged (if logging is
   enabled for the ara::com implementation).

.. unit:: Identifying the right trigger
   :id: UNIT_COM_EVTTRIG_015
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10514

   Using the Service ID (see [PRS_SOMEIP_00245]) and the serviceInterfaceId attribute of
   the SomeipServiceInterfaceDeployment element as well as the Method ID (see
   [PRS_SOMEIP_00245]) and 0x8000 + the eventId attribute of the SomeipEventDeployments of
   the SomeipServiceInterfaceDeployment, the right trigger shall be identified.

.. unit:: Silently discarding SOME/IP triggers for unsubscribed triggers
   :id: UNIT_COM_EVTTRIG_016
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10515

   If the trigger identified according to [SWS_CM_10514] does not have an active
   subscription, the received SOME/IP trigger shall be silently discarded (i.e.,
   [SWS_CM_00226], and [SWS_CM_00249] shall not be performed).

.. unit:: Invoke receive handler
   :id: UNIT_COM_EVTTRIG_017
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10516

   In case a receive handler was registered using the SetReceiveHandler method (see
   [SWS_CM_00249]) of the respective Trigger class for the trigger determined according to
   [SWS_CM_10514] this registered receive handler shall be invoked when the corresponding
   Trigger is received.

.. unit:: Failures in sending a SOME/IP trigger
   :id: UNIT_COM_EVTTRIG_018
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_EVTTRIG_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10517

   If the sending of the SOME/IP trigger fails locally (due to a network error which is
   notified to the ara::com implementation), the ara::com implementation shall return
   kNetworkBindingFailure in the Result of the Send() method of the respective Trigger
   class (see [SWS_CM_00721]).

.. unit:: IAM Module Instantiation
   :id: UNIT_COM_IAM_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10492

   If no IamModuleInstantiation is defined on the Machine, CM shall perform no access
   control, i.e., no access to any service shall be restricted because of missing
   ComGrants.

.. unit:: Local Access Control Activation
   :id: UNIT_COM_IAM_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10493

   If IamModuleInstantiation.localComAccessControlEnabled is defined and is set to false,
   CM shall perform no local access control, i.e., no access to any service from a local
   Process shall be restricted because of missing ComGrants. If IamModuleInstantiation is
   defined on the Machine and IamModuleInstantiation.localComAccessControlEnabled is not
   defined or is set to true, CM shall perform local access control.

.. unit:: Remote Access Control Activation
   :id: UNIT_COM_IAM_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10494

   If IamModuleInstantiation.remoteAccessControlEnabled is defined and is set to false, CM
   shall perform no remote access control, i.e., no access to any service from a remote
   subject shall be restricted because of missing ComGrants. If IamModuleInstantiation is
   defined on the Machine and IamModuleInstantiation.remoteAccessControlEnabled is not
   defined or is set to true, CM shall perform remote access control.

.. unit:: Local access control on receiving triggers
   :id: UNIT_COM_IAM_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10539

   If a Process subscribes to a trigger of a service interface, but there exists no
   ComTriggerGrant that - does not reference any remote subject in the role remoteSubject
   and - references the requested RequiredApServiceInstance in the role serviceInstance and
   the RequiredApServiceInstance is referenced by a ServiceInstanceToPortPrototypeMapping
   in the role serviceInstance and the ServiceInstanceToPortPrototypeMapping references the
   requesting Process in the role process, - references the subscribed trigger in the role
   serviceDeployment, then Communication Management shall drop the request and
   ComErrc::kGrantEnforcementError shall be returned by the Subscribe() method of the
   respective Trigger class.

.. unit:: Local access control on providing service instances
   :id: UNIT_COM_IAM_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10542

   If a Process requests to provide a service instance or any element thereof, but there
   exists no ComOfferServiceGrant that - does not reference any remote subject in the role
   remoteSubject and - references the requested ProvidedApServiceInstance in the role
   serviceInstance and the ProvidedApServiceInstance is referenced by a
   ServiceInstanceToPortPrototypeMapping in the role serviceInstance and the
   ServiceInstanceToPortPrototypeMapping references the requesting Process in the role
   process, then Communication Management shall drop the request.

.. unit:: Local access control on executing methods
   :id: UNIT_COM_IAM_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90001

   If a Process executes a method of a service interface, but there exists no
   ComMethodGrant that - does not reference any remote subject in the role remoteSubject
   and - references the requested RequiredApServiceInstance in the role serviceInstance and
   the RequiredApServiceInstance is referenced by a ServiceInstanceToPortPrototypeMapping
   in the role serviceInstance and the ServiceInstanceToPortPrototypeMapping references the
   requesting Process in the role process, - references the requested method in the role
   serviceDeployment, then Communication Management shall drop the request and
   ComErrc::kGrantEnforcementError shall be returned in the Future of the operator().

.. unit:: Local access control on receiving events
   :id: UNIT_COM_IAM_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90003

   If a Process subscribes to an event of a service interface, but there exists no
   ComEventGrant that - does not reference any remote subject in the role remoteSubject and
   - references the requested RequiredApServiceInstance in the role serviceInstance and the
   RequiredApServiceInstance is referenced by a ServiceInstanceToPortPrototypeMapping in
   the role serviceInstance and the ServiceInstanceToPortPrototypeMapping references the
   requesting Process in the role process, - references the subscribed event in the role
   serviceDeployment, then Communication Management shall drop the request and
   ComErrc::kGrantEnforcementError shall be returned by the Subscribe() method of the
   respective Event class.

.. unit:: Local access control on service discovery
   :id: UNIT_COM_IAM_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAM_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90006

   If a Process requests to find a service, but there exists no ComGrant that - does not
   reference any remote subject in the role remoteSubject and - references the requested
   RequiredApServiceInstance in the role serviceInstance and the RequiredApServiceInstance
   is referenced by a ServiceInstanceToPortPrototypeMapping in the role serviceInstance and
   the ServiceInstanceToPortPrototypeMapping references the requesting Process in the role
   process, then Communication Management shall drop the request and - the constructor of
   the ServiceProxy class shall throw an exception (see [SWS_CM_00131]), or - the named
   constructor function Create() of the ServiceProxy class (see [SWS_CM_10438]) shall
   return the error code ComErrc::kGrantEnforcementError.

.. unit:: TLS-based Authentication
   :id: UNIT_COM_IAMREMOTE_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10495

   Communication Management shall associate remote subjects communicating via an
   established (D)TLS connection to a TlsIamRemoteSubject according to [TPS_MANI_03240].

.. unit:: IP and IPsec-based Authentication
   :id: UNIT_COM_IAMREMOTE_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10496

   Communication Management shall associate remote subjects communicating via IP to an
   IPSecIamRemoteSubject or an IpIamRemoteSubject according to [TPS_MANI_03242] and
   [TPS_MANI_03244].

.. unit:: Authentication Failure
   :id: UNIT_COM_IAMREMOTE_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10497

   If IamModuleInstantiation. remoteAccessControlEnabled is set to true and a remote
   subject cannot be authenticated, Communication Management shall silently drop all
   messages from this remote subject.

.. unit:: Remote access control on executing methods
   :id: UNIT_COM_IAMREMOTE_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10498

   If a remote subject requests the execution of a method of a service interface, but there
   exists no ComMethodGrant that - references the requesting remote subject in the role
   remoteSubject and - references a ProvidedApServiceInstance in the role serviceInstance
   and - references the requested method in the role serviceDeployment, then Communication
   Management shall drop the request.

.. unit:: Remote access control on consuming events
   :id: UNIT_COM_IAMREMOTE_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10501

   If a remote subject subscribes to an event of a service interface, but there exists no
   ComEventGrant that - references the subscribing remote subject in the role remoteSubject
   and - references a ProvidedApServiceInstance in the role serviceInstance and -
   references the subscribed event in the role serviceDeployment, then Communication
   Management shall drop the subscription request.

.. unit:: Remote access control on consuming field notifiers
   :id: UNIT_COM_IAMREMOTE_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10505

   If a remote subject subscribes to a field notifier , but there exists no ComFieldGrant
   that - references the subscribing remote subject in the role remoteSubject and -
   references a ProvidedApServiceInstance in the role serviceInstance and - references the
   event in the role serviceDeployment, then Communication Management shall drop the the
   subscription request.

.. unit:: Remote access control on calling field setters
   :id: UNIT_COM_IAMREMOTE_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10506

   If a remote subject requests the execution of a set method of a field, but there exists
   no ComFieldGrant that - has the parameter ComFieldGrant.role set to setter or
   getterSetter and - references the requesting remote subject in the role remoteSubject
   and - references a ProvidedApServiceInstance in the role serviceInstance and -
   references the event in the role serviceDeployment, then Communication Management shall
   drop the request.

.. unit:: Remote access control on calling field getters
   :id: UNIT_COM_IAMREMOTE_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10507

   If a remote subject requests the execution of a get method of a field, but there exists
   no ComFieldGrant that - has the parameter ComFieldGrant.role set to getter or
   getterSetter and - references the requesting remote subject in the role remoteSubject
   and - references a ProvidedApServiceInstance in the role serviceInstance and -
   references the event in the role serviceDeployment, then Communication Management shall
   drop the request.

.. unit:: Remote access control on consuming triggers
   :id: UNIT_COM_IAMREMOTE_009
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10541

   If a remote subject subscribes to an trigger of a service interface, but there exists no
   ComTriggerGrant that - references the subscribing remote subject in the role
   remoteSubject and - references a ProvidedApServiceInstance in the role serviceInstance
   and - references the ServiceEventDeployment in the role serviceDeployment that in turn
   references the subscribed trigger. then Communication Management shall drop the
   subscription request.

.. unit:: Remote access control on providing service instances
   :id: UNIT_COM_IAMREMOTE_010
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_IAMREMOTE_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10543

   If a remote subject provides a service instance or any element thereof, but there exists
   no ComOfferServiceGrant that - references the providing remote subject in the role
   remoteSubject and - references the provided RequiredApServiceInstance in the role
   serviceInstance, then Communication Management shall drop all requests to and from this
   service instance.

.. unit:: Secure UDP and TCP channel creation for TLS, DTLS and SecOC
   :id: UNIT_COM_SECCHAN_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECCHAN_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90101

   The Communication Management software shall create secure UDP channels according to the
   input for all SecureComProps referenced by ServiceInstanceToMachineMapping in the role
   secureComPropsForUdp. The Communication Management software shall create secure TCP
   channels according to the input for all SecureComProps referenced by
   ServiceInstanceToMachineMapping in the role secureComPropsForTcp. Secure channels may be
   shared by multiple AdaptivePlatformServiceInstances by multiplexing the communication,
   i.e. by referencing the same SecureComProps in the same role.

.. unit:: Using secure TLS, DTLS and SecOC channels
   :id: UNIT_COM_SECCHAN_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECCHAN_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90102

   All communication triggered by a Skeleton or Proxy shall be sent via the respective
   secure channel according to the configuration input. In the configuration the
   appropriate secure channel is identified by examining the references to SecureComProps
   of ServiceInstanceToMachineMapping for the AdaptivePlatformServiceInstance that is
   mapped to an EthernetCommunicationConnector of a Machine by this
   ServiceInstanceToMachineMapping.

.. unit:: Secure TLS and DTLS channel creation in the DDS Network Binding
   :id: UNIT_COM_SECCHAN_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECCHAN_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90201

   Secure channels shall be created as specified in [SWS_CM_90101].

.. unit:: Using TLS and DTLS secure channels in the DDS Network Binding
   :id: UNIT_COM_SECCHAN_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECCHAN_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90202

   Secure channels shall be used as specified in [SWS_CM_90102].c (RS_CM_00801,
   RS_CM_00803) 7.5.2.2 DDS Security DDS Security, as defined in [26], is a complementary
   standard to DDS, providing transport-independent security measures (authentication,
   secrecy, non-repudiation, integrity, access control and logging) without requiring
   changes to application logic. Mapping DDS Service Interface and Instance Deployment
   models, as well as IAM Communications Grant models, to DDS QoS policies, and DDS
   Security certificate, governance and permission files is defined by [29].

.. unit:: IPsec secure channel between communication nodes
   :id: UNIT_COM_SECCHAN_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECCHAN_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90117

   An IPsec secure channel shall be created and used if an AdaptivePlatformServiceInstance
   is mapped by ServiceInstanceToMachineMapping to an EthernetCommunicationConnector that
   points with the unicastNetworkEndpoint to a NetworkEndpoint that aggregates an
   IPSecConfig. The IPSecRules in the IPSecConfig define security associations between the
   NetworkEndpoint that aggregates this IPSecConfig and remote nodes that are defined by
   the referenced remoteIpAddress.

.. unit:: Transport of Service communication over an IPsec security association
   :id: UNIT_COM_SECCHAN_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECCHAN_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90118

   If a communication connection is established between a Service Provider and Service
   Requester and the configured transport layer connection matches the defined security
   association then the IP packets exchanged between the Service Provider and Service
   Requester will be protected by IPsec. In other words it means that if the IPsec security
   association defined by - the local Address (IP Address defined by the
   networkEndpointAddress, Port and Protocol defined by localPortRangeStart and
   localPortRangeEnd - the remote Address (IP Address defined by the remoteIpAddress, Port
   and Protocol defined by remotePortRangeStart or remotePortRangeEnd) equals the settings
   defined by - the ServiceInstanceToMachineMapping for the ProvidedApServiceInstance and -
   the ServiceInstanceToMachineMapping for the RequiredApServiceInstance and - this network
   connection is established then the IP packets between the two nodes will be protected
   according to the configuration that is also defined in the IPSecRule.

.. unit:: MACsec secure channel between communication nodes and MACsec security association
   :id: UNIT_COM_SECCHAN_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECCHAN_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_99040

   A MACsec secure channel and secure association shall be created and used according to
   the requirements and constraints specified in [SWS_CM_90117] and [SWS_CM_90118].

.. unit:: SecOC secure channel behavior
   :id: UNIT_COM_SECTRANS_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11271

   Whenever a SecOC secure channel interaction is detected (based on the configuration
   options of [SWS_CM_90108], [SWS_CM_90115], [SWS_CM_90109], [SWS_CM_90116], and
   [SWS_CM_90110]) the SecOC functionality shall be applied according to: - sending
   according to [SWS_CM_11274], [SWS_CM_11275] - reception according to [SWS_CM_11276],
   [SWS_CM_11277]

.. unit:: Lifecycle management of FVM
   :id: UNIT_COM_SECTRANS_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11272

   The lifecycle of an SecOC FreshnessValueManager implementation shall be managed by
   ara::com.c (RS_CM_00801) [SWS_CM_11273]{DRAFT} Initialization of the FVM d - The SecOC
   FreshnessValueManager implementation shall be initialized by calling Freshness Value
   Management Library API ara::com:: secoc::FVM::Initialize.

.. unit:: SecOC secure channel sending
   :id: UNIT_COM_SECTRANS_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11274

   If a message is configured to be SecOC sent, the message shall be secured according to
   [30] and following steps shall be performed: - the message shall be handled as Authentic
   message by the Communication Management - the message Authentication shall be performed
   in the order of operations after the E2E protection calculations - if the
   ServiceInterfaceElementSecureComConfig has an attribute freshnessValueId defined, the
   Communication Management shall call the Freshness Value Mananement Library API
   ara::com::secoc:: FVM::GetTxFreshness with the freshnessValueId - calculate the MAC
   using the Authentic message ([PRS_SecOc_00200] see [30]), (optionally the Freshness
   Value), and the dataId - if the attribute authInfoTxLength is defined, the Authenticator
   ([PRS_SecOc_00210] see [30]) shall be truncated - if the attribute
   freshnessValueTxLength is defined, the Freshness Value shall be truncated
   ([PRS_SecOc_00201] see [30]) - combine the Authentic message, (truncated) Freshness
   Value, and (truncated) Authenticator ([PRS_SecOc_00211] see [30]) - continue in the
   Communication Management with the send processing The details for the construction of
   secure message are described in: [PRS_SecOc_00103], [PRS_SecOc_00105],
   [PRS_SecOc_00200], [PRS_SecOc_00207], [PRS_SecOc_00208], [PRS_SecOc_00209],
   [PRS_SecOc_00210], [PRS_SecOc_00211], [PRS_SecOc_00212] (see [30])

.. unit:: SecOC secure message build attempts
   :id: UNIT_COM_SECTRANS_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11275

   For every message to be sent and secured with SecOC [30] an Authentication Build
   Counter([PRS_SecOc_00202] see [30]) shall be maintained: - the Authentication Build
   Counter shall be set to 0 if the operation was successful. - if the query of the
   freshness value ara::com::secoc::FVM::GetTxFreshness return a recoverable error
   kFVNotAvailable, or an error occurs during calculation of the Authenticator, the
   Authentication Build Counter is incremented and the process of securing the message will
   be retried in an implementation specific manner. - if the Authentication Build Counter
   has reached the SecOC implementation specific threshold
   SecOCAuthenticationBuildAttempts([PRS_SecOc_00206] see [30]), the message shall be
   discarded and the incident shall be logged (if logging is enabled for the ara::com
   implementation). The process is described in: [PRS_SecOc_00201], [PRS_SecOc_00202],
   [PRS_SecOc_00203], [PRS_SecOc_00204], [PRS_SecOc_00205], [PRS_SecOc_00206] (see [30])

.. unit:: SecOC secure channel reception
   :id: UNIT_COM_SECTRANS_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11276

   If a message is configured to be SecOC received and the attribute securedRxVerification
   is set to true or is not defined, then the message shall be verified according to [30]
   and following steps shall be performed: - the message shall be handled as Secured
   message by the Communication Management - if the attribute freshnessValueTxLength is
   defined, the Freshness Value will be calculated by calling the Freshness Value
   Mananement Library API ara::com::secoc::FVM::GetRxFreshness with SecOCFreshnessValueID
   equals to defined freshnessValueId and with the SecOCTruncatedFreshnessValue equals to
   the extracted Truncated Freshness Value([PRS_SecOc_00317] see [30]) from the Secured
   message, otherwise the Freshness Value([PRS_SecOc_00316] see [30]) shall be extracted
   from the Secured message itself - if the attribute authInfoTxLength is defined, the
   Truncated Authenticator([PRS_SecOc_00315] see [30]) shall be extracted from the Secured
   message, otherwise the Authenticator([PRS_SecOc_00317] see [30]) shall be extracted from
   the Secured message - verify the message by calculating the MAC using the Secured
   message, optionally the Freshness Value([PRS_SecOc_00300], and comparing the result with
   received Truncated Authenticator([PRS_SecOc_00315] and continue in the Communication
   Management with the receive processing - the message authentication procedure is done
   before E2E checks The details for the verification of secure message are described in:
   [PRS_SecOc_00103], [PRS_SecOc_00300], [PRS_SecOc_00313], [PRS_SecOc_00314],
   [PRS_SecOc_00315], [PRS_SecOc_00316], [PRS_SecOc_00317], [PRS_SecOc_00318],
   [PRS_SecOc_00330] (see [30])

.. unit:: SecOC secure message verification attempts
   :id: UNIT_COM_SECTRANS_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11277

   For every message received and secured with SecOc, an Authentication Build
   Counter([PRS_SecOc_00301] shall be maintained: - the Authentication Build Counter shall
   be set to 0 if the operation was successful. - if the query of the freshness value
   Freshness Value Mananement Library API ara::com::secoc::FVM::GetRxFreshness returns a
   recoverable error kFVNotAvailable, or an error occurs during calculation of the
   Authenticator, the Authentication Build Counter shall be incremented and the process of
   message verification will be retried in an implementation specific manner. - if the
   counter has reached the parameter authenticationRetries([PRS_SecOc_00307] see [30]), the
   message shall be discarded and the incident shall be logged (if logging is enabled for
   the ara::com implementation). - if the calculation of the
   Authenticator([PRS_SecOc_00315] was successful but the verification failed for the
   parameter authenticationRetries([PRS_SecOc_00306] see [30]), the message shall be
   discarded and the incident shall be logged (if logging is enabled for the ara::com
   implementation). The process is described in: [PRS_SecOc_00301], [PRS_SecOc_00302],
   [PRS_SecOc_00303], [PRS_SecOc_00304], [PRS_SecOc_00305], [PRS_SecOc_00306],
   [PRS_SecOc_00307], [PRS_SecOc_00308], [PRS_SecOc_00309], [PRS_SecOc_00310],
   [PRS_SecOc_00311], [PRS_SecOc_00312] (see [30])

.. unit:: SecOC verification results
   :id: UNIT_COM_SECTRANS_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11278

   Communication Management shall make each verification result (VerificationStatusResult)
   accessible via the VerificationStatus service.

.. unit:: SecOc override the verification result
   :id: UNIT_COM_SECTRANS_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11279

   Communication Management shall allow the configuration of SecOC behavior via the
   VerifyStatusOverride or VerifyStatusOverride methods. The overwrite options are defined
   by OverrideStatus. The configuration is available per dataID in the case of
   VerificationStatusConfigurationByDataId service or per freshnessID in the case of
   VerificationStatusConfigurationByFreshnessId service.c (RS_CM_00801) 7.5.2.3.2 Signal
   based network binding The SOME/IP Message Header as shown in figure 7.19 is divided into
   two parts: Part I containing the Message ID and the Length and Part II containing
   Request ID, Protocol Version, Interface Version, Message Type and Return Code (SOME/IP
   Protocol Specification [4]). In case of signal-service-translation only a partial header
   is used, namely the Part I. In figure 7.22 the handling of the Header Part I, the signal
   based payload, and the SecOC part is illustrated. Signal based Serialized Payload x y z
   Payload covered by SecOC Signal based Serialized Payload SecOC SecOC (truncated)
   (truncated) x y z Freshness Authenticator Payload covered by SOME/IP Length SOME/IP
   Signal based Serialized Payload SecOC SecOC Msg Header (truncated) (truncated) Part I x
   y z Freshness Authenticator Figure 7.22: Payload covered by SecOC and Signal2Service
   transport

.. unit:: SecOC secure channel reception bypass
   :id: UNIT_COM_SECTRANS_009
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_11372

   If a message is configured to be SecOC received and the attribute securedRxVerification
   is set to false, then - the message shall be handled as Secured message without
   verification by the Communication Management - the Authentic message part shall be
   extracted and processed - the VerificationStatus shall be set to
   VerificationStatusResult. kSecOcNoVerification

.. unit:: SecOC secure channel for methods using reliable transport
   :id: UNIT_COM_SECTRANS_010
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90108

   A SecOC secure channel shall be created and used if: - A SecOcSecureComProps instance is
   referenced in the role secureComPropsForTcp by a ServiceInstanceToMachineMapping and a
   Method of the AdaptivePlatformServiceInstance is selected for transmission over the
   secured channel by the ServiceInterfaceElementSecureComConfig and this Method of the
   AdaptivePlatformServiceInstance is configured for transmission over “tcp” by
   transportProtocol in the associated SomeipMethodDeployment.

.. unit:: SecOC secure channel for events and triggers using reliable transport
   :id: UNIT_COM_SECTRANS_011
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90109

   A SecOC secure channel shall be created and used if: - A SecOcSecureComProps instance is
   referenced in the role secureComPropsForTcp by a ServiceInstanceToMachineMapping and an
   event or trigger of the AdaptivePlatformServiceInstance is selected for transmission
   over the secured channel by the ServiceInterfaceElementSecureComConfig and this event or
   trigger of the AdaptivePlatformServiceInstance is configured for transmission over “tcp”
   by transportProtocol in the associated SomeipEventDeployment.

.. unit:: SecOC secure channel for fields
   :id: UNIT_COM_SECTRANS_012
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90110

   The requirements [SWS_CM_90108], [SWS_CM_90109], [SWS_CM_90115], [SWS_CM_90116] apply to
   fields in the same manner, since fields are a composition of methods and events.c
   (RS_CM_00801)

.. unit:: SecOC secure channel for methods using unreliable transport
   :id: UNIT_COM_SECTRANS_013
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90115

   A SecOC secure channel shall be created and used if: - A SecOcSecureComProps instance is
   referenced in the role secureComPropsForUdp by a ServiceInstanceToMachineMapping and a
   Method of the AdaptivePlatformServiceInstance is selected for transmission over the
   secured channel by the ServiceInterfaceElementSecureComConfig and this Method of the
   AdaptivePlatformServiceInstance is configured for transmission over “udp” by
   transportProtocol in the associated SomeipMethodDeployment.

.. unit:: SecOC secure channel for events and triggers using unreliable transport
   :id: UNIT_COM_SECTRANS_014
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90116

   A SecOC secure channel shall be created and used if: - A SecOcSecureComProps instance is
   referenced in the role secureComPropsForUdp by a ServiceInstanceToMachineMapping and an
   event or trigger of the AdaptivePlatformServiceInstance is selected for transmission
   over the secured channel by the ServiceInterfaceElementSecureComConfig and this event or
   trigger of the AdaptivePlatformServiceInstance is configured for transmission over “udp”
   by transportProtocol in the associated SomeipEventDeployment.

.. unit:: TLS secure channel for ServiceInterface content using reliable transport
   :id: UNIT_COM_SECTRANS_015
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90103

   A TLS secure channel shall be created and used if a TlsSecureComProps instance is
   referenced in the role secureComPropsForTcp by a ServiceInstanceToMachineMapping. All
   content of the ServiceInterface that is referenced by the
   AdaptivePlatformServiceInstance that in turn is referenced by the
   ServiceInstanceToMachineMapping that is configured for transmission over “tcp” in the
   ServiceInterfaceDeployment is selected for transmission over the TLS secured channel.

.. unit:: DTLS secure channel for ServiceInterface content using unreliable transport
   :id: UNIT_COM_SECTRANS_016
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90104

   A DTLS secure channel shall be created and used if a TlsSecureComProps instance is
   referenced in the role secureComPropsForUdp by a ServiceInstanceToMachineMapping. All
   content of the ServiceInterface that is referenced by the
   AdaptivePlatformServiceInstance that in turn is referenced by the
   ServiceInstanceToMachineMapping that is configured for transmission over “udp” in the
   ServiceInterfaceDeployment is selected for transmission over the TLS secured channel.

.. unit:: Behavior of a ServiceProxy over TLS before successful completion of the handshake
   :id: UNIT_COM_SECTRANS_017
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90111

   The communication channel is ready as soon as the TLS handshake is completed. Therefore,
   the future returned by the following methods shall only be satisfied after the handshake
   has finished and once the communication was successful: - the function call operator
   (operator()) of the respective Method class (see [SWS_CM_00196]) - the Set() method of
   the respective Field class (see [SWS_CM_00113]) - the Get() method of the respective
   Field class (see [SWS_CM_00112]) If the handshake fails, the error code
   ComErrc::kPeerIsUnreachable shall be returned in the Future of the respective methods
   (operator(), Set(), Get()). The error shall be logged.

.. unit:: Behavior of a ServiceProxy over DTLS before successful completion of the handshake
   :id: UNIT_COM_SECTRANS_018
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90112

   The communication channel is ready as soon as the DTLS handshake is completed. Before
   completion the middleware shall drop all requests as if the remote peer is unreachable.

.. unit:: Behavior of a ServiceSkeleton over TLS before successful completion of the handshake
   :id: UNIT_COM_SECTRANS_019
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90113

   The communication channel is ready as soon as the TLS handshake is completed. Therefore,
   [SWS_CM_10287] and [SWS_CM_10319] shall be extended to checking whether the TLS
   handshake did successfully finish. Therefore, as if the proxy was not connected, the
   invocation of the following methods shall not result in sending any data: - the Send()
   method of the respective Event class (see [SWS_CM_00162]) - the Send() method of the
   respective Trigger class (see [SWS_CM_00721]) - the Update() method of the respective
   Field class (see [SWS_CM_00119])

.. unit:: Behavior of a ServiceSkeleton over DTLS before successful completion of the handshake
   :id: UNIT_COM_SECTRANS_020
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90114

   The communication channel is ready as soon as the TLS handshake is completed. Therefore,
   [SWS_CM_10287] and [SWS_CM_10319] shall be extended to checking whether the TLS
   handshake did successfully finish. Therefore, as if the proxy was not connected, the
   invocation of the following methods shall not result in sending any data: - the Send()
   method of the respective Event class (see [SWS_CM_00162]) - the Send() method of the
   respective Trigger class (see [SWS_CM_00721]) - the Update() method of the respective
   Field class (see [SWS_CM_00119])

.. unit:: Behavior of a creating ServiceProxy over TLS or DTLS
   :id: UNIT_COM_SECTRANS_021
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90119

   The instantiation according to [SWS_CM_00131] shall trigger the asynchronous handshake.

.. unit:: TLS server role of a Skeleton
   :id: UNIT_COM_SECTRANS_022
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SECTRANS_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90121

   The TLS secure channel shall be associated with the respective Skeleton and the
   implementation shall act as a TLS server, if the AdaptivePlatformServiceInstance
   referenced in - [SWS_CM_90103] - [SWS_CM_90104] is a ProvidedApServiceInstance.

.. unit:: E2E event protection properties and profile configuration
   :id: UNIT_COM_E2E_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2E_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90402

   An E2E-protected Event shall have its options configured in End2EndEventProtectionProps
   and E2EProfileConfiguration.

.. unit:: Requirements of E2E_protect and E2E_check
   :id: UNIT_COM_E2E_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2E_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90433

   The E2E functions mentioned in this section using the names E2E_protect and E2E_check
   shall meet the requirements on E2E protection as defined in [9] and comply with the E2E
   protection protocol specification of [7] (especially [PRS_E2E_00323]).

.. unit:: E2E-protected Methods Request Message Protection
   :id: UNIT_COM_E2E_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2E_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10462

   For E2E-protected Methods, E2E protection of the request message shall be performed
   within the context of the operator() of the Method class (see [SWS_CM_00196]) of the
   respective service method.

.. unit:: E2E checking of the method request in ServiceSkeleton (message reception)
   :id: UNIT_COM_E2E_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2E_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10466

   For E2E-protected Method requests, E2E checking shall be performed within the context of
   the message reception within the ServiceSkeleton if the MethodCallProcessingMode is set
   to kEventSingleThread.

.. unit:: Wrong Method Call Processing Mode Error for ServiceSkeleton named constructor
   :id: UNIT_COM_E2E_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2E_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10467

   In case a MethodCallProcessingMode of kEvent has been passed to the named constructor of
   the ServiceSkeleton for a service using E2E-protected methods (see [SWS_CM_10436] or
   [SWS_CM_10435]), an error code ComErrc:kWrongMethodCallProcessingMode shall be returned
   in the Result of the named constructor Create(). If logging is enabled, the error shall
   be logged.

.. unit:: E2E checking of the method request in ServiceSkeleton (ProcessNextMethodCall)
   :id: UNIT_COM_E2E_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2E_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10468

   For E2E-protected Method requests, E2E checking shall be performed within the context of
   ProcessNextMethodCall within the ServiceSkeleton if the MethodCallProcessingMode is set
   to kPoll.

.. unit:: E2E protection of method response message performed after the method or E2E error handler execution
   :id: UNIT_COM_E2E_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2E_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90481

   For E2E-protected Methods, E2E protection of the response message shall be performed
   after the execution of the service method (in case of a successful E2E_check according
   to [SWS_CM_90480]) or after the execution of the E2E error handler (in case of a failed
   E2E check according to [SWS_CM_90480]).

.. unit:: E2E checking of the method response in the ServiceProxy
   :id: UNIT_COM_E2E_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2E_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90471

   For E2E-protected Method responses, E2E checking shall be performed within the context
   of the message reception within the ServiceProxy.

.. unit:: E2E protection of events in Send
   :id: UNIT_COM_E2EEVT_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00046

   For E2E-protected Events, E2E protection shall be performed within the context of Send.

.. unit:: E2E_protect for event serialized data
   :id: UNIT_COM_E2EEVT_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90401

   For E2Eprotected Events, E2E_protect shall be invoked on the to be protected serialized
   data (passed as argument serializedData to E2E_protect) according to [PRS_E2E_00323].

.. unit:: Argument dataID in E2E_protect for events
   :id: UNIT_COM_E2EEVT_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90403

   For E2Eprotected Events, the End2EndEventProtectionProps.dataId shall be passed as
   argument dataID to E2E_protect.

.. unit:: E2E protection header for events
   :id: UNIT_COM_E2EEVT_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90404

   For E2E-protected Events, in case of SOME/IP serialization the E2E protection header
   shall be added to the message. If the protocol specification of the respective network
   binding imposes restrictions on the placement of the E2E protection header (e.g.,
   [PRS_SOMEIP_00941] in case of SOME/IP network binding), then these restrictions shall be
   honored.c (RS_E2E_08540) 7.6.1.3 Subscriber - GetNewSamples

.. unit:: E2E-protected events sample serialization
   :id: UNIT_COM_E2EEVT_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90430

   For E2Eprotected Events, Send shall serialize the sample and potentially add a protocol
   header according to the rules of the respective network binding (e.g., according to
   [SWS_CM_10291] in case of SOME/IP network binding), resulting in serialized data.c
   (RS_CM_00223, RS_E2E_08540) From E2E protection perspective this serialized data include
   both a non-protected part as well as the part to be protected (see [PRS_E2E_UC_00239]
   and [PRS_E2E_USE_00741]).

.. unit:: E2E checking shall be done in GetNewSamples for events
   :id: UNIT_COM_E2EEVT_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90406

   For E2E-protected Events, E2E checking shall be performed within the context of
   GetNewSamples.

.. unit:: GetNewSamples shall get all the serialized data that has not yet been fetched
   :id: UNIT_COM_E2EEVT_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90407

   For E2E-protected Events, GetNewSamples shall first get the collection of all serialized
   data that have not been fetched during the last call of this GetNewSamples function.

.. unit:: E2E Protection header removal from serialized data
   :id: UNIT_COM_E2EEVT_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00044

   For the given E2E-protected sample, the E2E protection header shall be removed from the
   serialized data.

.. unit:: Argument dataID in E2E_check for event with serialized sample
   :id: UNIT_COM_E2EEVT_009
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00045

   For the given E2E-protected sample, the End2EndEventProtectionProps.dataId shall be
   passed as argument dataID to E2E_check.

.. unit:: Processing the non-E2E-protected header of E2Eprotected sample
   :id: UNIT_COM_E2EEVT_010
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90408

   For the given E2E-protected sample, GetNewSamples shall process the non-E2E protected
   header (if any) of the sample’s serialized data.

.. unit:: E2E_check for event serialized data
   :id: UNIT_COM_E2EEVT_011
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90410

   For the given E2E-protected sample, E2E_check shall be invoked on the protected
   serialized data (passed as argument serializedData to E2E_check) according to
   [RS_E2E_08540] and [PRS_E2E_00323].

.. unit:: E2E_check for Events provides Result with SMState and ProfileCheckStatus
   :id: UNIT_COM_E2EEVT_012
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90411

   In return, for the given E2E-protected sample, E2E_check shall provide a Result
   (e2eResult according to [PRS_E2E_00322] of [7]) containing the elements SMState
   (e2eState according to [PRS_E2E_00322] of [7]) and ProfileCheckStatus (e2eStatus
   according to [PRS_E2E_00322] of [7]).

.. unit:: E2E-protected sample deserialization
   :id: UNIT_COM_E2EEVT_013
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90412

   For the given E2E-protected sample, GetNewSamples shall deserialize the resulting
   serialized data according to the rules of the respective network binding (e.g.,
   according to [SWS_CM_10294] in case of SOME/IP network binding), resulting in the
   deserialized sample.

.. unit:: GetNewSamples shall update ProfileCheckStatus in the SamplePtr and SMState in the Event class
   :id: UNIT_COM_E2EEVT_014
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90413

   For the given E2E-protected sample, GetNewSamples shall store the ProfileCheckStatus in
   the SamplePtr and shall update/overwrite the global SMState within its specific Event
   class of the specific E2E-protected Event.

.. unit:: Argument dataID in E2E_check for events without serialized sample
   :id: UNIT_COM_E2EEVT_015
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00043

   The End2EndEventProtectionProps.dataId shall be passed as argument dataID to E2E_check.

.. unit:: E2E_check invoked on a null sample
   :id: UNIT_COM_E2EEVT_016
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90415

   E2E_check shall be invoked on a null sample (i.e., a null pointer shall be passed as
   argument serializedData to E2E_check) according to [RS_E2E_08540] and [PRS_E2E_00323].c
   (RS_E2E_08540)

.. unit:: E2E_check Result on a null sample
   :id: UNIT_COM_E2EEVT_017
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90416

   In return, for the given null sample, E2E_check shall provide a Result (e2eResult
   according to [PRS_E2E_00322] of [7]) containing the elements SMState (e2eState according
   to [PRS_E2E_00322] of [7]) and ProfileCheckStatus (e2eStatus according to
   [PRS_E2E_00322] of [7]).

.. unit:: GetNewSamples shall update the SMState of specific event class
   :id: UNIT_COM_E2EEVT_018
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90417

   GetNewSamples shall update/overwrite the global SMState within its specific Event class
   of the specific E2E-protected Event.

.. unit:: GetProfileCheckStatus method of SamplePtr
   :id: UNIT_COM_E2EEVT_019
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00042

   Each SamplePtr shall provide a GetProfileCheckStatus method to access the
   ProfileCheckStatus of each sample (see [SWS_CM_90420]).

.. unit:: GetE2EStateMachineState method for Events
   :id: UNIT_COM_E2EEVT_020
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EEVT_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10475

   A GetE2EStateMachineState method shall be provided for each Event class of a specific
   ServiceProxy class.

.. unit:: E2E-protected Methods Arguments Serialization
   :id: UNIT_COM_E2EMETH_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00041

   For E2E-protected Method requests, operator() shall serialize the Method’s in and inout
   arguments and potentially add a protocol header according to the rules of the respective
   network binding (e.g., according to [SWS_CM_10301] in case of SOME/IP network binding),
   resulting in the serialized data.

.. unit:: E2E-protected Method Requests dataID Argument
   :id: UNIT_COM_E2EMETH_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10463

   For E2E-protected Method requests, the End2EndMethodProtectionProps. dataId shall be
   passed as argument dataID to E2E_protect.

.. unit:: E2E protection header according to the network binding in the method request
   :id: UNIT_COM_E2EMETH_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10464

   For E2E-protected Method requests, the E2E protection header shall be added to the
   message. If the protocol specification of the respective network binding imposes
   restrictions on the placement of the E2E protection header (e.g., [PRS_SOMEIP_00941] in
   case of SOME/IP network binding), then these restrictions shall be honored.

.. unit:: E2E-protected Methods Serialized Data Protection
   :id: UNIT_COM_E2EMETH_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90479

   For E2E-protected Method requests, E2E_protect shall be invoked on the to be protected
   serialized data (passed as argument serializedData to E2E_protect) according to
   [RS_E2E_08541], [PRS_E2E_00323], and [PRS_E2E_00828].

.. unit:: Argument sourceID for E2E_protect
   :id: UNIT_COM_E2EMETH_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90486

   For E2Eprotected Method requests using profiles P04m, P07m, P08m, or P44m, the
   End2EndMethodProtectionProps.sourceId shall be passed as argument sourceID to
   E2E_protect.

.. unit:: Argument messageType for E2E_protect
   :id: UNIT_COM_E2EMETH_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90487

   For E2Eprotected Method requests using profiles P04m, P07m, P08m, or P44m,
   STD_MESSAGETYPE_REQUEST (0) shall be passed as argument messageType to E2E_protect.

.. unit:: Argument messageResult for E2E_protect
   :id: UNIT_COM_E2EMETH_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90488

   For E2E-protected Method requests using profiles P04m, P07m, P08m, or P44m,
   STD_MESSAGERESULT_OK (0) shall be passed as argument messageResult to E2E_protect.

.. unit:: E2E Protection header removal from serialized data for method requests
   :id: UNIT_COM_E2EMETH_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00037

   For the given E2E-protected Method request, the E2E protection header shall be removed
   from the serialized data.

.. unit:: E2E_check for method request provides Result with SMState and ProfileCheckStatus
   :id: UNIT_COM_E2EMETH_009
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00038

   In return, for the given E2E-protected Method request, E2E_check shall provide a Result
   (e2eResult according to [PRS_E2E_00322] of [7]) containing the elements SMState
   (e2eState according to [PRS_E2E_00322] of [7]) and ProfileCheckStatus (e2eStatus
   according to [PRS_E2E_00322] of [7]).

.. unit:: Argument dataID in E2E_check for method requests
   :id: UNIT_COM_E2EMETH_010
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00039

   For the given E2E-protected Method request, the End2EndMethodProtectionProps.dataId
   shall be passed as argument dataID to E2E_check()).

.. unit:: Processing the non-E2E-protected header of E2Eprotected method request
   :id: UNIT_COM_E2EMETH_011
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00040

   For the given E2E-protected Method request, the nonE2E-protected header (if any) of the
   Method request’s serialized data shall be processed.

.. unit:: E2E Error Handler - Invocation Arguments
   :id: UNIT_COM_E2EMETH_012
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00047

   In case no new request message is available, E2EErrorHandler shall be called with the
   following arguments: errorCode shall be set to the kNotAvailable, dataID shall be set to
   0, and messageCounter shall be set 0.

.. unit:: E2E Error Handler - Invocation Arguments
   :id: UNIT_COM_E2EMETH_013
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10471

   In case a new request message is available, E2EErrorHandler shall be called with the
   following arguments: errorCode shall be set to the ProfileCheckStatus obtained in
   [SWS_CM_90411], dataID shall be set to End2EndMethodProtectionProps. dataId, and
   messageCounter shall be set to the E2E counter of the received request message.

.. unit:: Argument serializedData in E2E_check for method requests
   :id: UNIT_COM_E2EMETH_014
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90480

   For the given E2E-protected Method request, E2E_check() shall be invoked on the
   protected serialized data (passed as argument serializedData to E2E_check()) according
   to [RS_E2E_08541], [PRS_E2E_00323], and [PRS_E2E_00828].

.. unit:: Argument sourceID in E2E_check for method requests
   :id: UNIT_COM_E2EMETH_015
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90489

   For E2E-protected Method requests using profiles P04m, P07m, P08m, or P44m, a reference
   to a variable to store the End2EndMethodProtectionProps. sourceId to shall be passed as
   argument sourceID to E2E_check. E2E_check shall extract the E2E Source ID contained in
   the E2E protection header into this variable. This extracted sourceID shall be stored
   for later use during E2E protection of response payload (see [SWS_CM_90492]).

.. unit:: Argument messageType in E2E_check for method requests
   :id: UNIT_COM_E2EMETH_016
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90490

   For E2E-protected Method requests using profiles P04m, P07m, P08m, or P44m,
   STD_MESSAGETYPE_REQUEST (0) shall be passed as argument messageType to E2E_check.

.. unit:: Argument messageResult E2E_check for method requests
   :id: UNIT_COM_E2EMETH_017
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90491

   For E2E-protected Method requests using profiles P04m, P07m, P08m, or P44m,
   STD_MESSAGERESULT_OK (0) shall be passed as argument messageResult to E2E_check.

.. unit:: Payload of the E2E Error Response
   :id: UNIT_COM_E2EMETH_018
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00033

   The payload of this error response message shall contain an ara::core::ErrorCode of
   error domain ara::com::e2e::E2EErrorDomain. The value of this ara::core::ErrorCode shall
   be set to the corresponding error value of E2E_check according to [SWS_CM_90421]. The
   serialization of this error code and the potential adding of a protocol header shall
   take place according to the used network binding (e.g., according to [SWS_CM_10312] and
   [SWS_CM_10428] in case of SOME/IP).

.. unit:: E2E Error Response
   :id: UNIT_COM_E2EMETH_019
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10472

   In case E2E_check (according to [SWS_CM_90480]) reported an E2E error, an error response
   message according to the used network binding (e.g., [SWS_CM_10312] in case of SOME/IP)
   shall be sent to the client.

.. unit:: Payload of the Normal or Application Error Response
   :id: UNIT_COM_E2EMETH_020
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90467

   For E2E-protected Methods the Method inout and out arguments or the application error
   shall be serialized and a protocol header shall be potentially added according to the
   rules of the respective network binding (e.g., according to [SWS_CM_10312] in case of
   SOME/IP network binding), resulting in the serialized data.

.. unit:: Argument dataId in E2E_protect for methods
   :id: UNIT_COM_E2EMETH_021
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10469

   For E2E-protected Method responses, the End2EndMethodProtectionProps.dataId shall be
   passed as argument dataID to E2E_protect.

.. unit:: Argument serializedData in E2E_protect for methods
   :id: UNIT_COM_E2EMETH_022
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90468

   For E2E-protected Method responses, E2E_protect shall be invoked on the to be protected
   serialized data (passed as argument serializedData to E2E_protect) according to
   [RS_E2E_08541], [PRS_E2E_00323], and [PRS_E2E_00828].

.. unit:: E2E Counter in E2E_protect for method response
   :id: UNIT_COM_E2EMETH_023
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90469

   For E2E-protected Method responses, the E2E counter contained in the corresponding
   Method request shall be used as E2E counter in the call to E2E_protect.

.. unit:: E2E protection header according to the network binding in the method response
   :id: UNIT_COM_E2EMETH_024
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90470

   For E2E-protected Method responses, the E2E protection header shall be added to the
   message. If the protocol specification of the respective network binding imposes
   restrictions on the placement of the E2E protection header (e.g., [PRS_SOMEIP_00941] in
   case of SOME/IP network binding), then these restrictions shall be honored.

.. unit:: Argument sourceId in E2E_protect for methods
   :id: UNIT_COM_E2EMETH_025
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90492

   For E2E-protected Method responses using profiles P04m, P07m, P08m, or P44m, the stored
   sourceID (which has been extracted according to [SWS_CM_90489]) shall be passed as
   argument sourceID to E2E_protect.

.. unit:: Argument messageType in E2E_protect for methods
   :id: UNIT_COM_E2EMETH_026
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90493

   For E2E-protected Method responses using profiles P04m, P07m, P08m, or P44m,
   STD_MESSAGETYPE_RESPONSE (1) shall be passed as argument messageType to E2E_protect.

.. unit:: Argument messageResult STD_MESSAGERESULT_OK in E2E_protect for methods
   :id: UNIT_COM_E2EMETH_027
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90494

   For E2E-protected Method responses using profiles P04m, P07m, P08m, or P44m, in case of
   a normal response (i.e., neither an application error response message nor an E2E error
   response message), STD_MESSAGERESULT_OK (0) shall be passed as argument messageResult to
   E2E_protect.

.. unit:: Argument messageResult STD_MESSAGERESULT_ERROR in E2E_protect for methods
   :id: UNIT_COM_E2EMETH_028
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90495

   For E2E-protected Method responses using profiles P04m, P07m, P08m, or P44m, in case of
   an error response (i.e., either an application error response message or an E2E error
   response message), STD_MESSAGERESULT_ERROR (1) shall be passed as argument messageResult
   to E2E_protect.

.. unit:: E2E counter of method response shall match with the one in method request
   :id: UNIT_COM_E2EMETH_029
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10465

   For E2E-protected Method response, the response message shall carry the same E2E counter
   value as the request message. In case the E2E counter is different, the response message
   shall be discarded (without any further processing).

.. unit:: Processing the non-E2E-protected header of the E2Eprotected method response
   :id: UNIT_COM_E2EMETH_030
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90472

   For the given E2E-protected Method responses, the non-E2E-protected header (if any) of
   the Method response’s serialized data shall be processed.

.. unit:: Argument serialized Data in E2E_check for method response
   :id: UNIT_COM_E2EMETH_031
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90473

   For the given E2E-protected Method response, E2E_check() shall be invoked on the
   protected serialized data (passed as argument serializedData to E2E_check()) according
   to [RS_E2E_08541], [PRS_E2E_00323], and [PRS_E2E_00828].

.. unit:: Argument dataId in E2E_check for method response
   :id: UNIT_COM_E2EMETH_032
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90474

   For the given E2E-protected Method response, the End2EndMethodProtectionProps.dataId
   shall be passed as argument dataID to E2E_check()).

.. unit:: E2E protection header removal from the serialized data for method response
   :id: UNIT_COM_E2EMETH_033
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90475

   For the given E2E-protected Method response, the E2E protection header shall be removed
   from the serialized data.

.. unit:: E2E_check for method response provides Result with SMState and ProfileCheckStatus
   :id: UNIT_COM_E2EMETH_034
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90478

   In return, for the given E2E-protected Method response, E2E_check shall provide a Result
   (e2eResult according to [PRS_E2E_00322] of [7]) containing the elements SMState
   (e2eState according to [PRS_E2E_00322] of [7]) and ProfileCheckStatus (e2eStatus
   according to [PRS_E2E_00322] of [7]).

.. unit:: Update SMState of specific method class with the SMState provided in the Result of E2E_check
   :id: UNIT_COM_E2EMETH_035
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90482

   The global SMState within its specific Method class of a specific ServiceProxy class
   shall be updated/overwritten with the element SMState of the Result provided by
   E2E_check according to [SWS_CM_90478].

.. unit:: Argument sourceId in E2E_check for method response
   :id: UNIT_COM_E2EMETH_036
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90496

   For E2E-protected Method responses using profiles P04m, P07m, P08m, or P44m, the
   End2EndMethodProtectionProps.sourceId shall be passed as argument sourceID to E2E_check.

.. unit:: Argument messageType in E2E_check for methods response
   :id: UNIT_COM_E2EMETH_037
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90497

   For E2E-protected Method responses using profiles P04m, P07m, P08m, or P44m,
   STD_MESSAGETYPE_RESPONSE (1) shall be passed as argument messageType to E2E_check.

.. unit:: Argument messageResult STD_MESSAGERESULT_OK in E2E_check for method response
   :id: UNIT_COM_E2EMETH_038
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90498

   For E2Eprotected Method responses using profiles P04m, P07m, P08m, or P44m, in case of a
   normal response (i.e., neither an application error response message nor an E2E error
   response message), STD_MESSAGERESULT_OK (0) shall be passed as argument messageResult to
   E2E_check.

.. unit:: Argument messageResult STD_MESSAGERESULT_ERROR in E2E_check for method response
   :id: UNIT_COM_E2EMETH_039
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90499

   For E2E-protected Method responses using profiles P04m, P07m, P08m, or P44m, in case of
   an error response (i.e., either an application error response message or an E2E error
   response message), STD_MESSAGERESULT_ERROR (1) shall be passed as argument messageResult
   to E2E_check.

.. unit:: Handling the E2E Error Response
   :id: UNIT_COM_E2EMETH_040
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10473

   Handling of an E2E error response message (sent due to a detected E2E error in request
   according to [SWS_CM_10472]) shall be done in the same way as the reception and the
   handling of any other error response message according to the used network binding
   (e.g., according to [SWS_CM_10429] in case of SOME/IP network binding).

.. unit:: Deserialization of the data according to the network binding for method response
   :id: UNIT_COM_E2EMETH_041
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90476

   For the given E2E-protected Method response, the resulting serialized data shall be
   deserialized according to the rules of the respective network binding (e.g., according
   to [SWS_CM_10316] and [SWS_CM_10429] in case of SOME/IP network binding), resulting in
   the deserialized inout and out arguments to the Method call or in the deserialized
   application error.

.. unit:: E2E Error Return Code
   :id: UNIT_COM_E2EMETH_042
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90477

   For the given E2E-protected Method response in case of failed E2E check an
   ara::core::ErrorCode of error domain ara::com::e2e::E2EErrorDomain with value set to
   ProfileCheckStatus obtained in [SWS_CM_90478] shall be constructed according to
   [SWS_CM_90421]. This ara::core::ErrorCode shall be passed as argument in a call to
   SetError() on the ara::core::Promise.

.. unit:: GetE2EStateMachineState method shall be provided for each method class
   :id: UNIT_COM_E2EMETH_043
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90483

   A GetE2EStateMachineState method shall be provided for each Method class of a specific
   ServiceProxy class.

.. unit:: GetE2EStateMachineState method shall provide access to the SMState of the specific method class
   :id: UNIT_COM_E2EMETH_044
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_E2EMETH_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90484

   The GetE2EStateMachineState method shall provide access to the global SMState of the
   specific Method class, which was determined by the last run of E2E_check function
   invoked during the last reception of the Method response (see [SWS_CM_90482]).

.. unit:: Uniqueness of offered service on local machine
   :id: UNIT_COM_COREAPI_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00102

   Upon a call to OfferService() the Communication Management shall check the offered
   service for uniqueness on the local machine using information available to the service
   discovery. If the implementation detects a service instance duplication (i.e., a service
   with the same serviceInstanceId, serviceInterfaceId and majorVersion on the same VLAN
   (e.g.according to [constr_1723] of [5]) is already registered, the requested service
   offering shall not start, and the function shall return positively after error is
   logged.

.. unit:: Network binding where a service is offered
   :id: UNIT_COM_COREAPI_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00103

   When a new service is offered by the application, the Communication Management shall
   check over which network binding this service shall be offered. This information is
   configured in the class of ServiceInterfaceDeployment referencing the offered
   ServiceInterface in the role serviceInterface. If the class is
   SomeipServiceInterfaceDeployment then the Some/IP network binding shall handle the
   OfferService call as described in [SWS_CM_00203]. If the class is
   DdsServiceInterfaceDeployment, then the DDS network binding shall handle the
   OfferService call as described in [SWS_CM_11001]. If the class is
   UserDefinedServiceInterfaceDeployment, the Communication Management implementer is
   responsible for implementing the OfferService method in an appropriate way.

.. unit:: Network binding for StopOfferService
   :id: UNIT_COM_COREAPI_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00104

   When a service calls StopOfferService, the Communication Management shall check over
   which network binding the offered service shall be stopped. This information is
   configured in the class of ServiceInterfaceDeployment referencing the offered
   ServiceInterface in the role serviceInterface. If the class is
   SomeipServiceInterfaceDeployment then the Some/IP network binding shall handle the
   mapping of the StopOfferService method as described in [SWS_CM_00204]. If the class is
   DdsServiceInterfaceDeployment, then the DDS network binding shall handle the mapping of
   the StopOfferService as described in [SWS_CM_11005]. If the class is
   UserDefinedServiceInterfaceDeployment, the Communication Management implementer is
   responsible for implementing the StopOfferService method in an appropriate way.

.. unit:: Destruction of service proxy
   :id: UNIT_COM_COREAPI_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10446

   The destructor of each specific ServiceProxy class shall destroy the Promise instances
   corresponding to the Future instances returned by the function call operator
   (operator()) of the respective Method class (see [SWS_CM_00196]) or by the Get or Set
   method of the respective Field class (see [SWS_CM_00112] and [SWS_CM_00113]) by
   explicitly or implicitly invoking the destructor of the Promise (see [SWS_CORE_00349]).
   This in turn will make the corresponding Future ready (if this is not already the case)
   with an ara::core::ErrorCode (see [SWS_CORE_00501]) where the error domain is set to
   ara::core::FutureErrorDomain (see [SWS_CORE_00421]) and the value is set to
   broken_promise (see [SWS_CORE_00400]).

.. unit:: Call SubscriptionStateChangeHandler with kSubscriptionPending on the Proxy side
   :id: UNIT_COM_COREAPI_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00313

   The Communication Management shall call the SubscriptionStateChangeHandler on the Proxy
   side with the value kSubscriptionPending in the following cases: - the client subscribes
   to an event and the actual subscription does not happen immediately (e.g. due to a bus
   protocol) - the client is subscribed to an event and Communication Management has
   detected that the server instance is currently not available (due to restart, network
   problem or so)

.. unit:: Call SubscriptionStateChangeHandler with kSubscribed on the Proxy side
   :id: UNIT_COM_COREAPI_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00314

   The Communication Management shall call the SubscriptionStateChangeHandler on the Proxy
   side with the value kSubscribed in the following cases: - the client subscribes to an
   event and the actual subscription is established successfully - the client is subscribed
   to an event and the actual subscription is re-established again after being temporarily
   unavailable (due to restart, network problem or so)

.. unit:: Re-establishing an active subscription
   :id: UNIT_COM_COREAPI_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00315

   The Communication Management shall re-establish the actual subscription again after the
   server service being temporarily unavailable (due to restart, network problem or so).
   This shall work independently of whether a network binding is involved or not. The
   reestablishment shall also provide a possible update of binding specific connection
   properties if needed.

.. unit:: Ensure memory allocation of maxSampleCount samples
   :id: UNIT_COM_COREAPI_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00700

   The Communication Management shall ensure, that after returning from method Subscribe
   sufficient memory resources are available, so that the number of samples given in
   parameter maxSampleCount can be concurrently accessed by application layer.

.. unit:: Asynchronous nature of Subscribe()
   :id: UNIT_COM_COREAPI_009
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12006

   In order to keep application functionality robust against Network Binding configuration
   changes, applications shall assume asynchronous operation when calling Subscribe(). This
   implies not assuming success in the subscription process until GetSubscriptionState() or
   the handler set by SetSubscriptionStateChangeHandler() have reported kSubscribed, even
   if Subscribe() has returned with no error.

.. unit:: Subscription State change handler on the Proxy side
   :id: UNIT_COM_COREAPI_010
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_99035

   The handler SubscriptionStateChangeHandler defined in [SWS_CM_00311] shall be called for
   the Proxy side by the Communication Management implementation as soon as the
   subscription state of this event has changed. Handler may be overwritten during runtime.

.. unit:: Sequence of actions in GetNewSamples
   :id: UNIT_COM_COREAPI_011
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00703

   In the context of the GetNewSamples call, the Communication Management shall do the
   following steps repeatedly: - get next received event data sample from underlying
   receive buffers. - de-serialize the data, if needed. - place the de-serialized data
   sample of type SampleType in the local cache. - call user provided f with a SamplePtr
   (including ProfileCheckStatus) referencing the data sample located in local cache. until
   at least one of the following conditions is true: - maxNumberOfSamples have already been
   fetched from the underlying receive buffers within this GetNewSamples call. -
   maxSampleCount reached. I.e. the application is currently holding exactly as many
   SamplePtrs provided by this Event class instance, than it has committed in call to
   Subscribe via maxSampleCount. - no new data samples available from underlying receive
   buffers.

.. unit:: FIFO semantics
   :id: UNIT_COM_COREAPI_012
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00709

   The Communication Management shall provide buffering with FIFO semantics between sender
   and receiver of events.

.. unit:: No implicit context switches
   :id: UNIT_COM_COREAPI_013
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00710

   When no ReceiveHandler has been set at the proxy side via SetReceiverHandler(), new
   SampleData shall only be rececived by directly invoking GetNewSamples() (polling
   behaviour). Reception of new events itself shall not lead to an implicit context switch
   in the local receiver process (i.e. if only polling behavior is used). In case a
   SetReceiveHandler () is enabled, a context switch shall be enforced with the reception
   of new events to schedule/invoke the ReceiveHandler.

.. unit:: New data samples received by CM at execution time of receive handler
   :id: UNIT_COM_COREAPI_014
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12007

   In case new data samples arrive at Communication Management side during the execution of
   a user defined receive handler, Communication Management shall postpone the next call to
   receive handler until the previous call to receive handler is finished.

.. unit:: Sequence of actions in GetNewTriggers
   :id: UNIT_COM_COREAPI_015
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00227

   In the context of the GetNewTriggers (see [SWS_CM_00226]) call, the Communication
   Management shall get the number of triggers occurred since the last call of
   GetNewTriggers.

.. unit:: Synchronous behavior of method call
   :id: UNIT_COM_COREAPI_016
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00192

   To achieve synchronous behavior of the method call, the methods of ara::core::Future
   object with blocking behavior shall be used because they only return when the output of
   the method call according to [SWS_CM_00196] is available: get(), wait(), wait_for (),
   wait_until(). With the call of one of these methods and the result still pending, the
   Communication Management software is allowed to perform actions which lead to
   uncontrolled context switches from the caller point of view, e.g. an asynchronous event-
   style mechanism for a wait-on-event.

.. unit:: Asynchronous behavior of method call with polling
   :id: UNIT_COM_COREAPI_017
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00193

   To achieve asynchronous behavior of the method call with polling on the result
   availability, the non-blocking method is_ready() of ara::core::Future object shall be
   used. If is_ready() returns true, the next call of get() shall not block, but
   immediately return the valid value.

.. unit:: Cancel the method call
   :id: UNIT_COM_COREAPI_018
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00194

   The destructor of the returned ara::core::Future object shall be used by the caller to
   cancel the request after issuing a method call. Deleting the returned ara::core::Future
   object shall result in the abort of the method call and ensure that any related buffers
   are released and no result is returned to the caller.

.. unit:: Retrieving results of the method call
   :id: UNIT_COM_COREAPI_019
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00195

   The method GetResult() of the returned ara::core::Future object shall be used to
   retrieve the result of the method call as ara::core::Result. The call of the method
   GetResult() will block if there is not yet a result available and will return after the
   result has been received returning an object of the respective Output or an error. As an
   alternative, get() returns the contained object of the result from GetResult(), or
   throws the contained error as exception, respectively.

.. unit:: Asynchronous behavior of method call with notification
   :id: UNIT_COM_COREAPI_020
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00197

   To achieve asynchronous behavior of the method call with event-driven notification on
   the result availability, the non-blocking method then() of ara::core::Future object
   shall be used. It allows to register a function, which gets asynchronously called in
   case the future has a valid result.

.. unit:: Context of return checked errors
   :id: UNIT_COM_COREAPI_021
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10371

   If during processing of a method call one of the checked errors occurs, the
   corresponding ara::core:: ErrorCode shall be returned in the context of the
   ara::core::Future::GetResult()/ara::core::Future::get() call.

.. unit:: Initiate a method call
   :id: UNIT_COM_COREAPI_022
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10414

   At the point of time when the caller calls the method (see [SWS_CM_00196]), the
   Communication Management software does not know yet if the result shall be returned with
   synchronous or asynchronous behavior. Therefore the Communication Management software
   shall instantiate the ara::core::Future object to be returned to the caller, but shall
   not perform actions which lead to uncontrolled context switches from the caller point of
   view, e.g. an asynchronous event-style mechanism for a wait-on-event.

.. unit:: Aborting method calls in case of locally detected failures
   :id: UNIT_COM_COREAPI_023
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10440

   To notify the adaptive application about locally detected failures which prevent an
   issued (remote) service method call from succeeding, the ara::com implementation shall
   make the Future returned by the function call operator (operator()) of the respective
   Method class (see [SWS_CM_00196]) or by the Get or Set method of the respective Field
   class (see [SWS_CM_00112] and [SWS_CM_00113]) ready by invoking the SetError (see
   [SWS_CORE_00353]) operation of the Promise corresponding to this Future with an
   ara::core::ErrorCode (see [SWS_CORE_00501]) where the error domain is set to
   ara::com::ComErrorDomain (see [SWS_CM_11264]) and the value is set to
   kNetworkBindingFailure (see [SWS_CM_10432]) as an argument.

.. unit:: No checked errors for Fire and Forget method calls
   :id: UNIT_COM_COREAPI_024
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_90436

   There shall be no checked errors returned for Fire and Forget method calls.

.. unit:: Provision of an update notification event for a Field
   :id: UNIT_COM_COREAPI_025
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00120

   If hasNotifier is true, update notification events for the Field shall be provided as of
   the following requirements: - [SWS_CM_00141] Method to subscribe to a service event.
   This subscribe leads immediately to a service event that contains the initial field
   value send from provider side to the consumer. - [SWS_CM_00151] Method to unsubscribe
   from a service event. - [SWS_CM_00316] Method to query the subscription state. -
   [SWS_CM_00701] Method to receive a service event using polling. - [SWS_CM_00181] Method
   to enable service event trigger. - [SWS_CM_00182] Event Receive Handler call
   serialization. - [SWS_CM_00183] Method to disable service event trigger. -
   [SWS_CM_00333] Method to set a subscription state change handler. - [SWS_CM_00334]
   Method to unset a subscription state change handler. Except that the corresponding
   methods reside in the Field class instead of the Event class.

.. unit:: InstanceSpecifier translation to InstanceIdentifiers
   :id: UNIT_COM_COREAPI_026
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10452

   The Communication Management shall translate an InstancSpecifier to InstanceIdentifiers.
   Based on the match there shall be zero, 1 or multiple InstanceIdentifiers .

.. unit:: InstanceIdentifier check during the creation of service skeleton
   :id: UNIT_COM_COREAPI_027
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10410

   The Communication Management shall check the value of the InstanceIdentifier argument:
   the identifier shall be unique. If the same InstanceIdentifier is used for the creation
   of more than one skeleton instance of the same service shall be handled as violation
   according to [SWS_CORE_00003].

.. unit:: InstanceSpecifier check during the creation of service skeleton
   :id: UNIT_COM_COREAPI_028
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10450

   The Communication Management shall check the value of the InstanceSpecifier argument:
   the specifier shall be unique, using the same instance specifier for the creation of
   more than one skeleton instance of the same service shall be handled as violation
   according to [SWS_CORE_00003].

.. unit:: InstanceIdentifierContainer check during the creation of service skeleton
   :id: UNIT_COM_COREAPI_029
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10451

   The Communication Management shall check the value of the InstanceIdentifierContainer
   argument: - the container size shall be bigger than zero - the identifiers of the
   container shall be unique - the identifiers of the container shall correspond to the
   same instance specifier. If there are failing checks, and the same InstanceIdentifier is
   used for the creation of more than one skeleton instance of the same service shall be
   handled as violation according to [SWS_CORE_00003].

.. unit:: Subscription State change handler
   :id: UNIT_COM_COREAPI_030
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12012

   The handler SubscriptionStateChangeHandler defined in [SWS_CM_00311], [SWS_CM_12008] and
   [SWS_CM_12009] shall be called by the Communication Management implementation as soon as
   the subscription state of this event has changed. Handler may be overwritten during
   runtime.

.. unit:: Call SubscriptionStateChangeHandler on Skeleton side with kSubscribed
   :id: UNIT_COM_COREAPI_031
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12013

   The Communication Management shall call the SubscriptionStateChangeHandler on the
   skeleton side with the value kSubscribed whenever the number of active subscriptions to
   this event become more than 0.

.. unit:: Call SubscriptionStateChangeHandler on Skeleton side with kNotSubscribed
   :id: UNIT_COM_COREAPI_032
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12014

   The Communication Management shall call the SubscriptionStateChangeHandler on the
   skeleton side with the value kNotSubscribed whenever the number of active subscriptions
   to this event become 0.

.. unit:: Query Subscription State on Skeleton side
   :id: UNIT_COM_COREAPI_033
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12015

   GetSubscriptionState on the skeleton side shall return kSubscribed if at least one
   active subscription to this event exists and kNotSubscribed otherwise.
   kSubscriptionPending shall not be used on the Server side.

.. unit:: Re-entrancy and thread-safety GetSubscriptionState
   :id: UNIT_COM_COREAPI_034
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12016

   GetSubscriptionState (see [SWS_CM_12011]) shall be re-entrant and threadsafe for
   different Event class instances. When called re-entrant or concurrently on the same
   Event class instance, the behavior is undefined.

.. unit:: Re-entrancy and thread-safety SetSubscriptionStateChangeHandler
   :id: UNIT_COM_COREAPI_035
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12017

   SetSubscriptionStateChangeHandler [SWS_CM_12008] and [SWS_CM_12009] shall be reentrant
   and thread-safe for different Event class instances. When called re-entrant or
   concurrently on the same Event class instance, the behavior is undefined.

.. unit:: Re-entrancy and thread-safety UnsetSubscriptionStateChangeHandler
   :id: UNIT_COM_COREAPI_036
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_12018

   UnsetSubscriptionStateChangeHandler [SWS_CM_12010] shall be re-entrant and thread-safe
   for different Event class instances. When called reentrant or concurrently on the same
   Event class instance, the behavior is undefined.

.. unit:: Send event where application is responsible for the data
   :id: UNIT_COM_COREAPI_037
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_99031

   As defined in [SWS_CM_00162], the Send method of the specific Event class where the
   application is responsible for the data and the Communication Management creates a copy
   for sending shall be used whenever the application wants to work further with the data.

.. unit:: Send event where Communication Management is responsible for the data
   :id: UNIT_COM_COREAPI_038
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_99032

   As defined in [SWS_CM_90437], the Send method of the specific Event class where the
   Communication Management is responsible for the data and the application is not allowed
   to access the data after sending shall be used whenever the data is created explicitly
   for sending and no further processing is happening afterward by the application itself.
   Before sending the event, the corresponding data has to be requested from the
   Communication Management (see [SWS_CM_99033]) and filled with the respective data.c
   (RS_CM_00201)

.. unit:: Allocating data for event transfer
   :id: UNIT_COM_COREAPI_039
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_99033

   Data shall be requested by calling the Allocate method of the specific Event class as
   defined in [SWS_CM_90438]. By calling the Send method with the data, it is ensured that
   the data will be freed by the Communication Management.

.. unit:: Service method processing modes
   :id: UNIT_COM_COREAPI_040
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10411

   The following service method processing modes shall be supported: - Polling: Instead of
   calling a provided service method, the Communication Management software collects
   incoming service method invocations. The processing of each invocation is explicitly
   triggered by the implementation providing the service method using the mechanism defined
   in [SWS_CM_00199]. - Event-driven, concurrent: The Communication Management software
   activates the invoked service method when the invocation arrives. Consumer concurrent
   calls are allowed and will be processed concurrently on provider side by using different
   threads. This is the default mode. - Event-driven, sequential: The Communication
   Management software activates the invoked service method when the invocation arrives.
   Consumer concurrent calls are allowed, but will not be processed concurrently on
   provider side, by instead executing them one after the other to avoid the need of
   synchronization mechanisms in the implementation providing the service method.

.. unit:: Invoking GetHandlers
   :id: UNIT_COM_COREAPI_041
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10412

   The registered GetHandler shall be called by the implementation whenever the
   Communication Management receives a Get.

.. unit:: Ensuring the existence of valid Field values
   :id: UNIT_COM_COREAPI_042
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00128

   To ensure the existence of a valid field values upon a call to the Subscribe() method
   (see [SWS_CM_00141]) or to the Get() method (see [SWS_CM_00112]) the ara::com
   implementation shall do the following: If a service containing a Field is offered via a
   call to OfferService() (see [SWS_CM_00101]), if Update() has not been called yet and one
   or more of the following applies: - hasNotifier = true - hasGetter = true and a
   GetHandler (see [SWS_CM_00114]) has not yet been registered. Then the error code
   ComErrc::kFieldValueIsNotValid shall be returned in the result type of OfferService().
   The error shall be logged.

.. unit:: Ensuring the existence of SetHandler
   :id: UNIT_COM_COREAPI_043
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00129

   Upon a call to OfferService() in a skeleton implementation for a given service, the
   following error check shall be made: if for at least one contained Field having
   hasSetter = true no SetHandler (see [SWS_CM_00116]) has been registered yet, the error
   code ComErrc::kFieldSetHandlerNotSet shall be returned in the result type of
   OfferService(). The error shall be logged.

.. unit:: Invoking SetHandlers
   :id: UNIT_COM_COREAPI_044
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10413

   The registered SetHandler shall be called by the implementation whenever the
   Communication Management receives a Set.

.. unit:: Notify the Field value after a call to the SetHandler function
   :id: UNIT_COM_COREAPI_045
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10415

   The Communication Management implementation shall take the effective field value
   returned by the SetHandler function, and send it back to the requester as return value
   of the Set function (see [SWS_CM_00113]), and to all the other subscribed entities via
   notification (see [SWS_CM_00119]).

.. unit:: Find service handler invocation
   :id: UNIT_COM_COREAPI_046
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00124

   After calling the StartFindService method, the FindServiceHandler shall be called by the
   Communication Management software to receive the found services. By the first call, the
   FindServiceHandler shall receive the initially known matches, if there are any. In
   following, the FindServiceHandler shall be called every time the availability of any of
   the services matching the given instance criteria changes.

.. unit:: Calling stop find service for already stopped finds
   :id: UNIT_COM_COREAPI_047
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10382

   Calls to the StopFindService method using a FindServiceHandle obtained from a
   StartFindService that already has been stopped shall be silently ignored.c (RS_CM_00102)
   7.8.9 Service proxy creation For the service proxy creation C++ API reference, see
   chapter 8.1.3.12.

.. unit:: Re-establishing service connection
   :id: UNIT_COM_COREAPI_048
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_COREAPI_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10491

   In case the service becomes temporarily unavailable (due to restart, network problem or
   so), or if an error occurs while establishing a connection to the service, the error
   shall be logged, and the Communication Management shall retry to establish the
   connection once the next offer is received.

.. unit:: Event Receive Handler call serialization
   :id: UNIT_COM_APIDETAIL_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_APIDETAIL_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00182

   The Communication Management shall serialize calls to the registered EventReceiveHandler
   function as it is not guaranteed that the callback function is re-entrant.

.. unit:: GetNewSamples shall provide data samples if GetFreeSampleCount is not 0
   :id: UNIT_COM_APIDETAIL_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_APIDETAIL_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00711

   After the Communication Management has called the registered EventReceiveHandler
   function for a specific Event class instance, the next call to GetNewSamples on the same
   instance shall provide at least one data sample as long as GetFreeSampleCount is not
   already returning 0 at the point in time of the call.

.. unit:: Service Contract Version
   :id: UNIT_COM_APIDETAIL_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_APIDETAIL_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_99029

   The value of the service contract major version (serviceContractVersionMajor) shall be
   derived from the majorVersion attribute in the ServiceInterface. The value of the
   service contract minor version (serviceContractVersionMinor) shall be derived from the
   minorVersion attribute in the ServiceInterface.

.. unit:: Find Service Handle
   :id: UNIT_COM_APIDETAIL_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_APIDETAIL_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_99030

   To identify a triggered request to find a service, the StartFindService method of
   [SWS_CM_00123] shall return a FindServiceHandle which is used as parameter to cancel
   this request with StopFindService as described in [SWS_CM_00125].

.. unit:: SOME/IP method call handling (representative)
   :id: UNIT_COM_SERDES_001
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10297-SWS_CM_10441 range (29 reqs in SWS chapter 7.4.1.7)

   The SOME/IP network binding shall govern method-call request/response/fire-and-forget
   sending: the request message is sent by invoking the Method class's function-call
   operator when a static or discovered service connection exists; the transport protocol
   (UDP/TCP) is taken from the
   SomeipServiceInterfaceDeployment.methodDeployment.transportProtocol manifest attribute;
   local send failures shall be reported through the returned ara::core::Future's error
   result rather than silently dropped.

.. unit:: SOME/IP field/event message handling (representative)
   :id: UNIT_COM_SERDES_002
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10319-SWS_CM_10380 range (35 reqs in SWS chapter 7.4.1.8)

   The SOME/IP network binding shall govern event/field notification sending and reception:
   an event/field-update message is sent when the Field class's Update method is invoked or
   a configured cyclic/on-change trigger fires; UDP or multicast is selected per the
   ProvidedEventGroup's multicastThreshold configuration; a message for an event/field the
   receiver has not subscribed to (or whose subscription TTL has expired) shall be silently
   discarded.

.. unit:: SOME/IP serialization -- general rules (representative)
   :id: UNIT_COM_SERDES_003
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10034, SWS_CM_10169, SWS_CM_10259 and related (15 reqs in SWS 7.4.1.9)

   Payload serialization shall follow the data-type definitions of the service interface;
   deserialization shall tolerate and ignore trailing parameters appended to a previously-
   known parameter list (to allow rolling upgrades); serialized variable-length data shall
   be padded to its configured alignment.

.. unit:: SOME/IP serialization -- structs and enumerations (representative)
   :id: UNIT_COM_SERDES_004
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10042, SWS_CM_00252, SWS_CM_10268, SWS_CM_10361 and related (1 + 13 + 6 = 20 reqs in SWS 7.4.1.9.2-7.4.1.9.4)

   A struct shall be serialized in depth-first traversal order; an enumeration shall be
   serialized as its underlying primitive type; a struct's optional length field (size,
   byte order, and presence) is governed by the SomeipDataPrototypeTransformationProps
   manifest attributes, including the wire-type rules (4 for fixed-length, 5/6/7 for
   dynamic-length) that every deserializer shall be able to handle regardless of the
   serializer's own configuration.

.. unit:: SOME/IP serialization -- strings (representative)
   :id: UNIT_COM_SERDES_005
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10053, SWS_CM_10054, SWS_CM_10285 and related (21 reqs in SWS 7.4.1.9.5)

   Strings shall be Unicode-encoded and null-terminated; UTF-8, UTF-16BE, and UTF-16LE
   shall all be supported on the wire; the application always provides strings in UTF-8,
   and the SOME/IP binding is responsible for re-encoding to whatever wire encoding is
   configured via the manifest.

.. unit:: SOME/IP serialization -- vectors and arrays (representative)
   :id: UNIT_COM_SERDES_006
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_00270, SWS_CM_00257, SWS_CM_10256 and related (17 reqs in SWS 7.4.1.9.6)

   A vector/array's maximum element count is bounded by its allocator's configured
   capacity; its optional length field (size, presence, and byte order) is governed by the
   same
   SomeipDataPrototypeTransformationProps.someipTransformationProps.sizeOfArrayLengthField-
   style manifest attributes as structs, with a value of 0 meaning no length field is
   inserted on the wire.

.. unit:: SOME/IP serialization -- associative maps (representative)
   :id: UNIT_COM_SERDES_007
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10261, SWS_CM_10262, SWS_CM_10282 and related (11 reqs in SWS 7.4.1.9.7)

   An associative map shall be serialized as a length field followed by its key/value
   entries with no intermediate padding; the length field's presence, size, and byte order
   follow the same manifest-configured rules as vectors and structs.

.. unit:: SOME/IP serialization -- variants (representative)
   :id: UNIT_COM_SERDES_008
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10254, SWS_CM_10255, SWS_CM_10226 and related (9 reqs in SWS 7.4.1.9.8)

   A Variant shall be serialized with an optional length field (size and data type governed
   by ApSomeipTransformationProps.sizeOfUnionLengthField) followed by a type field
   identifying the active alternative and the serialized value of that alternative, padded
   per its own alignment rules.

.. unit:: SOME/IP message segmentation (representative)
   :id: UNIT_COM_SERDES_009
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- SWS_CM_10454, SWS_CM_99036, SWS_CM_10455 and related (9 reqs in SWS 7.4.1.9.9)

   An event or method-call message whose serialized payload exceeds the manifest-configured
   maximumSegmentLength (event) or maximumSegmentLengthRequest (method request) shall be
   segmented; where a separationTime is configured, segments shall be spaced accordingly.

.. unit:: SOME/IP serialization -- basic and TLV-related data types (representative)
   :id: UNIT_COM_SERDES_010
   :version: 1.0.0
   :status: draft
   :satisfies: COMP_COM_SERDES_001
   :standard: ASPICE SWE.3 / ISO 15288 6.4.5
   :derives_from: AUTOSAR_AP_SWS_CommunicationManagement (AP R23-11) -- remaining 7.4.1.9 items not covered by the categories above

   Basic (primitive) data types are serialized in their manifest-configured byte order with
   no additional framing; Tag-Length-Value (TLV) framing, where configured, layers a tag
   and length ahead of a member's serialized value to allow optional/reordered members --
   see SOME/IP Protocol Specification chapter 7.4.1.9 for the exact bit layout, not
   reproduced here.
