# Third-Party Notices

*** DRAFT — NOT YET REVIEWED BY LEGAL/IP COUNSEL ***

This file is a technical inventory, not a legal clearance. It lists the
third-party software this repository's own manifests, build scripts, and
CI workflows explicitly name — compiled by reading those files directly
(`conf.py`, `needs/requirements.txt`, `source/*/package.json` /
`pyproject.toml` / `Cargo.toml` / `CMakeLists.txt`, `.github/workflows/*`)
and checking each package's own published license metadata, not from
memory. It has not been reviewed by Legal/IP and should be treated the
same way `LICENSE` (repo root) already asks readers to treat that file:
as a draft, pending confirmation, not a binding statement of this
repository's licensing position.

## Scope and a real limitation

This list covers **direct** dependencies — the packages named outright in
this repo's own configuration. None of those packages have their versions
pinned here (`needs/requirements.txt` lists bare names; `package.json`
uses caret ranges; `pyproject.toml`'s dev extras are unpinned), so the
exact set of **transitive** dependencies each one pulls in — and their
exact versions — isn't fixed or reproducible from this repository alone,
and isn't enumerated below. As one concrete example: `sphinx-needs` alone
pulls in `requests`, `requests-file`, `jsonschema-rs`, `minijinja`,
`sphinx-data-viewer`, and `sphinxcontrib-jquery` as its own runtime
dependencies, and `sphinxcontrib-jquery` bundles an actual copy of jQuery
that ends up copied into the published docs site's static assets. `furo`
similarly pulls in `beautifulsoup4`, `pygments`, `accessible-pygments`, and
`sphinx-basic-ng`. Sphinx itself pulls in `docutils`, `Jinja2`, `Pygments`,
`Babel`, `alabaster`, `imagesize`, `snowballstemmer`, and `packaging`.
Each of those is itself a real, separately-licensed open-source project
(overwhelmingly BSD/MIT/Apache-2.0 in this specific dependency graph, per a
spot check run while compiling this file — none GPL) — they're named here
so the gap is visible, not fixed, since a byte-accurate transitive list
requires a pinned lockfile and a license-scanning tool (e.g. `pip-licenses`,
`license-checker` for npm, `cargo-license` for Rust) run against it in CI,
re-run on every dependency bump. Hand-maintaining a 40+ package transitive
list by prose would go stale immediately and give a false sense of
completeness; this file doesn't attempt that.

## Documentation build & publishing

These are installed by `.github/workflows/docs.yml` and `conf.py` /
`needs/conf.py`, and their output (rendered HTML, theme CSS/JS, generated
diagrams) is what actually gets published to the GitHub Pages site — the
strongest case for "incorporated," since end users viewing the docs
receive these components' generated assets directly.

| Component | License | Role |
|---|---|---|
| Sphinx | BSD-2-Clause | Documentation build engine |
| sphinx-needs | MIT | Requirements/traceability (needs graph, `needtable`, `needflow`) |
| furo | MIT | HTML theme for both Sphinx projects |
| sphinxcontrib-plantuml | BSD | Renders `.. uml::` diagrams via PlantUML |
| Pillow | MIT-CMU | Image handling used by the Sphinx/PlantUML pipeline |
| PlantUML (`plantuml`, apt) | Multi-licensed — EPL-1.0, LGPL-2.1+, GPL-2+, AGPL-3+, Apache-2.0, BSD-2-Clause, or Expat (MIT), per the packager's choice of any one; confirmed from the installed package's own `copyright` file | Diagram rendering engine invoked by sphinxcontrib-plantuml |
| Graphviz (`graphviz`, apt) | Primarily EPL-1.0, with some MIT/X11 and zlib-style components | Layout engine used by `needflow`/PlantUML |
| OpenJDK JRE (`default-jre-headless`, apt) | GPL-2.0 with Classpath Exception (primary); some bundled components under BSD/LGPL/MIT | Required to run the PlantUML `.jar` |

Verified versions at the time this file was written (root project's
Python 3.11 CI environment): Sphinx 9.0.4, sphinx-needs 8.3.1, furo
2025.12.19, sphinxcontrib-plantuml 0.31, Pillow 12.2.0, PlantUML
1:1.2020.2+ds-3ubuntu1.1, Graphviz 2.42.2-9ubuntu0.1, OpenJDK 21.0.10 —
these will drift as CI's `pip install` / `apt-get install` steps resolve
newer releases over time; this file is not re-generated automatically.

## Per-language development and test tooling

Named in each `source/<language>/` sub-project's own manifest. None of
these ship inside that sub-project's own build output — `pyproject.toml`'s
runtime `dependencies` list is empty, and every TypeScript package below
is a `devDependency` — they only run during local development, linting,
and test execution.

| Component | License | Sub-project |
|---|---|---|
| pytest | MIT | `source/python` (test framework) |
| pytest-cov | MIT | `source/python` (coverage plugin) |
| ruff | MIT | `source/python` (lint/format) |
| TypeScript | Apache-2.0 | `source/typescript` |
| ESLint | MIT | `source/typescript` |
| @eslint/js | MIT | `source/typescript` |
| typescript-eslint | MIT | `source/typescript` |
| Vitest | MIT | `source/typescript` (test runner) |
| @vitest/coverage-v8 | MIT | `source/typescript` (coverage) |

`source/rust`'s only crate (`crates/example_crate`) declares zero
dependencies in its `Cargo.toml`. `source/c` and `source/cpp` link only
the C/C++ standard library per their `CMakeLists.txt` — no third-party
libraries are declared in either.

## Build/CI orchestration (invoked remotely, not incorporated into this repository)

These run as external CI infrastructure — nothing about them is copied
into this repository's tree or into any published output. Listed for
completeness against `LICENSE`'s broad "may incorporate third-party...
components" language, not because they meet the stricter "included in
this repository" bar the rest of this file uses.

| Component | License | Role |
|---|---|---|
| CMake | BSD-3-Clause | Build system for `source/c`, `source/cpp` (`cmake_minimum_required`) |
| Bazel | Apache-2.0 (one bundled file, `src/main/cpp/util/md5.cc`, separately carries the RSA Data Security MD5 license) | Multi-language build/test orchestration (`ci.yml`) |
| GitHub Actions — `actions/checkout`, `actions/setup-python`, `actions/upload-pages-artifact`, `actions/deploy-pages`, `actions/upload-artifact` | MIT (GitHub's first-party `actions/*` org is consistently MIT-licensed; spot-verified against `actions/checkout`) | CI steps across all three workflows |
| `bazel-contrib/setup-bazel` (GitHub Action) | MIT | Installs Bazel in `ci.yml` |

## What this file does not cover

- Any content under `needs/` or `organisation/` itself — those are this
  organization's own requirements and process documentation, not
  third-party material.
- Fonts, icons, or other embedded assets — none were found vendored into
  this repository as of this writing (`doc/` contains no `.css`/`.js`/
  font files of its own).
- A full transitive dependency closure — see "Scope and a real
  limitation" above.

Questions about permitted use, redistribution, or licensing should go to
Legal/IP (see `LICENSE`'s own contact placeholder), not to this file's
listed components' upstream maintainers.
