# Code Links Sample — `source/c` only

A working proof-of-concept: real, dead-link-checked traceability from
implementation source code back to a design need, using
[sphinx-codelinks](https://pypi.org/project/sphinx-codelinks/) (the same
`useblocks` team that builds `sphinx-needs`). Scope is deliberately limited
to `source/c` — this is a sample, not a rollout. `source/cpp`, `source/python`,
`source/rust`, and `source/typescript` are untouched.

## What changed

- `source/c/src/communication/serializer.c` — two functions each gained a
  one-line comment marker directly above their definition:

  ```c
  // @Serialize a message into wire format, IMPL_C_SERIALIZER_ENCODE, impl, [UNIT_A_001]
  size_t serializer_encode(...) { ... }

  // @Deserialize a message from wire format, IMPL_C_SERIALIZER_DECODE, impl, [UNIT_A_001]
  int serializer_decode(...) { ... }
  ```

  `source/c/include/communication/serializer.h` still carries its original
  prose comment ("Implements UNIT_A_001...") — untouched. The marker is an
  addition, not a replacement of the header comment.

- `needs/conf.py` — added `version = "1.0"` / `release = "1.0"`. Sphinx-needs'
  `needs_external_needs` requires a non-empty `current_version` in the
  *source* project's exported `needs.json` before another project can import
  it. `needs/` never set one, so its own needs.json had an empty
  `current_version` and this sample's import failed outright with
  `NeedsExternalException("No version defined...")`. This is a real,
  necessary fix to `needs/conf.py` itself, independent of this sample —
  without it, nothing can ever import `needs/`'s own needs.json.
  `needs/`'s own `-W` build still passes with 0 warnings after this change.

- `codelinks_sample/` (new folder) — `conf.py`, `codelinks.toml`, `index.rst`,
  this README. A **third, independent Sphinx project**, alongside the
  existing root project and `needs/`.

## Why a third, separate Sphinx project

`sphinx-codelinks` 1.4.0 — the only version published on PyPI — requires
Python **>=3.12**. `.github/workflows/docs.yml` pins the root project's CI
build to Python **3.11** (documented, deliberate tool-qualification state,
per `ORG_TOOLCFG_001` / `TOOL_SPHINX_ROOT` in
`organisation/tools/tool_register.rst` — not an oversight). Adding
`sphinx_codelinks` to root `conf.py`'s `extensions` list would make the real
CI's Sphinx import fail on every build, immediately.

Keeping this as an isolated project with its own `conf.py` — the same
pattern the repo already uses to keep `needs/` separate from the root
project — means this sample builds and is verified for real, on Python
3.12, without touching or being able to break anything that runs in CI
today.

## How it works

`codelinks_sample/codelinks.toml` tells sphinx-codelinks to scan
`source/c` for one-line comment markers
(`// @<title>, <id>, <type>, [<links>]`). `codelinks_sample/index.rst`'s
`.. src-trace:: :project: source_c :directory: .` directive runs that scan
at build time and calls sphinx-needs' `add_need()` for each marker found —
these are real needs (type `impl`), not documentation text. Because
`codelinks_sample/conf.py` also imports `needs/`'s exported `needs.json` via
`needs_external_needs`, each `impl` need's `:links: UNIT_A_001` is checked
against a real external need at build time — sphinx-needs will report a
dead link (`needs_report_dead_links = True`) if `UNIT_A_001` is ever renamed
or removed, exactly like every other cross-need link in this repo.

## How to build and verify it locally

Requires Python 3.12 (not the CI's 3.11 — see above):

```bash
python3.12 -m venv /tmp/codelinks_venv
/tmp/codelinks_venv/bin/pip install sphinx sphinx-needs sphinx_codelinks furo

# needs/'s needs.json must exist first — this sample imports it:
cd needs && /tmp/codelinks_venv/bin/python -m sphinx -b needs . _build/needsjson

cd ../codelinks_sample && /tmp/codelinks_venv/bin/python -m sphinx -b html . _build/html -W
```

Verified output: `codelinks [source_c]: 2 files, 2 markers`, and the built
`needs.json` shows `IMPL_C_SERIALIZER_ENCODE` / `IMPL_C_SERIALIZER_DECODE`
each with `"links": ["UNIT_A_001"]`.

## Known gaps (disclosed, not fixed)

- **One remaining build warning, sandbox-only.** A `-W` build in the sandbox
  this sample was developed in reports:
  `WARNING: git root is not found in the parent of .../source/c
  [codelinks.git_root]`. sphinx-codelinks auto-discovers `git_root` by
  walking up from `src_dir` looking for a real `.git` directory. This
  sandbox mirror of the repo has no `.git` at all (`git status` here
  reports "fatal: not a git repository"). On the real device, `test_repo`
  is an actual git checkout, so the same auto-discovery will find
  `test_repo/.git` and this warning will not occur there — confirmed by
  reading `sphinx_codelinks/analyse/utils.py:locate_git_root`, not assumed.
  Deliberately left as auto-discovery (no hardcoded `git_root` in
  `codelinks.toml`) rather than forced, because hardcoding it here traded
  this one warning for two different ones (`codelinks.git_config` /
  `codelinks.git_head`), since those two also require a real `.git` to read
  from — see the comment in `codelinks.toml` for the full trace. **Please
  rebuild on the real device to confirm 0 warnings there** before treating
  this sample as fully clean.

- **`UNIT_A_001.rst` references a unit test that does not exist on disk.**
  While staging `source/c` for this sample, `source/c/tests/` was found not
  to exist at all on the real device (checked via a full recursive listing).
  `needs/communication/unit design/unit_a_001.rst` (`UNIT_A_001`) states this
  unit is verified by a compiled-and-run `test_serializer.c`. That test file
  — and the `tests/` directory it would live in — is not there. This is a
  pre-existing gap in the repo, unrelated to and not introduced by this
  sample; it's surfaced here because it was discovered while working in this
  exact area of the tree, not because this sample depends on it.

## What full production adoption would additionally require

This sample proves the mechanism for two functions in one file. Rolling it
out for real would need, at minimum: comment markers added across all of
`source/c` (not just `serializer.c`), then repeated for `source/cpp`,
`source/python`, `source/rust`, `source/typescript` (each with its own
`comment_type` in `codelinks.toml` — `cpp` covers C/C++ headers already used
here); a CI job pinned to Python 3.12 to run this build (separate from the
root project's 3.11-pinned job, unless/until that pin is revisited); a step
to export `needs/`'s `needs.json` before this project builds (it's a build
artifact, not committed, same as `needs/`'s own import of root's needs);
and a decision on whether `codelinks_sample/` merges into `needs/` itself
(one project, native + imported), or stays a fourth standalone project
permanently. None of that is done here — this is a sample, not a rollout.
