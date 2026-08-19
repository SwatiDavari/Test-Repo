# tools/

Repo-level automation for a product built on the combined test_repo +
qorix-ik-main structure. Everything here is language-agnostic and operates
on the whole repo — it stays out of `source/<lang>/`, which is product
implementation code only (see the earlier note on why `scripts/` merges
into `tools/` rather than living under `source/`).

| Script | Purpose | Typical caller |
|---|---|---|
| `fetch_external_needs.sh` | Pull the central `qorix-governance` repo's `needs.json` at the version pinned in `.qik/governance.lock`. | `needs-gate.yml`, before every build |
| `build_needs.sh` | Build this product's `needs/` Sphinx-needs project — HTML for humans, `needs.json` for tooling. | `needs-gate.yml`, `docs.yml` |
| `check_broken_links.py` | Hard gate: fail if any need links to an id that doesn't exist — the general form of test_repo's disclosed `SYS_001` dead-link defect. Also asserts a required HEAD-of-the-V anchor exists via `--require`. | `needs-gate.yml` |
| `check_orphan_needs.py` | Carried over from test_repo unchanged — fails if any need has no incoming or outgoing link at all. Complementary to `check_broken_links.py` (orphan = no links; broken = a link to nothing). | `needs-gate.yml` |
| `bump_governance.sh` | Deliberately adopt a new `qorix-governance` version: updates `.qik/governance.lock`, `MODULE.bazel`'s `bazel_dep()`, and refetches `needs.json` — the one-line-PR-diff mechanism the 50-product architecture depends on. | run by hand, reviewed in a PR |
| `install_claude_settings.py` | Scaffold/verify `.mcp.json` and `.claude/settings.json`. Does not write the hook scripts or agent persona files themselves — those come from `qik upgrade`. | first-time repo setup, `--check` in CI |

## Suggested `needs-gate.yml` wiring

```yaml
name: Needs gate
on: [push, pull_request]
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: gh auth setup-git   # or however this org authenticates gh in CI
        env: { GH_TOKEN: ${{ secrets.GITHUB_TOKEN }} }
      - run: tools/fetch_external_needs.sh
      - run: tools/build_needs.sh
      - run: python tools/check_broken_links.py needs/_build/needs/needs.json --require SYS_001
      - run: python tools/check_orphan_needs.py needs/_build/needs/needs.json
```

Every step above fails the job on a real problem — no `|| echo "::warning::..."` anywhere in this chain. That's the deliberate difference from test_repo's current `docs.yml`, whose orphan check is non-blocking today.

## Not included here

`qik axon check` / `qik cortex check` themselves aren't reimplemented — they're the actual qik binary, installed via `qorix-ik-main`'s own `scripts/install.sh` (or a released binary), and belong in a separate `cortex-gate.yml` / `bazel.yml` job. The scripts above cover the parts specific to *this* product repo's needs graph and its citation of central governance — not qik's own build.
