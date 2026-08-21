# Case TC_UNIT_Z_001: Service registry advertise/lookup/withdraw (unit)

Covers: UNIT_Z_001

Verifies, at the unit level and in isolation (no process boundary, no
network, no timeout), that the in-memory service registry makes an
advertised service instance visible to a lookup by service type, keeps
multiple instances of the same service type visible side by side, and
removes an instance from subsequent lookups once it is withdrawn.

This replaces the previous copy of `communication`'s
`case_a_001.md` (`Covers: UNIT_A_001`, a publish/subscribe
dispatch case unrelated to this module), which had been carried over
unchanged under this unit-test folder. The feature-level case for
service discovery still lives at the root `integration test/` — this
one is scoped to the unit alone.
