# Case Z-001: Service Discovery lookup round trip

Covers: feat_z_001

Verifies that a service instance advertised by one adaptive application
instance is discoverable via lookup by another adaptive application
instance, within the configured timeout, across a real process boundary
(unlike `needs/diagnostics/unit test/test cases/case_z_001.md`'s
`tc_unit_z_001`, which verifies the same advertise/lookup/withdraw
behavior at the unit level, in isolation, with no process boundary).

Owner: validation team. Status: draft — no automated test
implementation is wired up yet under `source/` for this case.
