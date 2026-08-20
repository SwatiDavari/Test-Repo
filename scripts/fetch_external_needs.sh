#!/usr/bin/env bash
# scripts/fetch_external_needs.sh
#
# Export this repo's own root-project needs (org_req, risk, problem, change,
# exception, tool, infra) and place the result where needs/conf.py's
# needs_external_needs expects it: needs/_external_needs/org_needs.json.
# This is the exact mechanism the real "Export organisation/governance/
# needs.json" step of .github/workflows/ci-needs.yml already runs inline —
# pulled out here as a standalone, reusable script instead of living only
# as YAML, so it can be run locally too.
#
# There is no separate "governance" repo to fetch from: the root project
# (this same repo, built from repo root) is the org_req source of truth.
# needs/ imports its exported needs.json as external-need citations so
# needs/'s own :links: fields can point at a real, checked org_req id
# instead of unenforced free-text — see needs/conf.py's own comment on
# needs_external_needs for the mechanics.
#
# Requires the root project's own doc-build dependencies (see
# .github/workflows/ci-needs.yml's "Install root-project deps" step):
#   pip install sphinx sphinx-needs sphinxcontrib-plantuml Pillow
#   apt-get install -y default-jre-headless graphviz plantuml
# Not installed by this script — it assumes the environment already has
# them (matching how ci-needs.yml itself separates the two steps).
#
# Usage: scripts/fetch_external_needs.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST_DIR="${REPO_ROOT}/needs/_external_needs"
DEST_FILE="${DEST_DIR}/org_needs.json"
BUILD_DIR="${REPO_ROOT}/_build/org_needs"

cd "${REPO_ROOT}"

echo "-- building root project's needs export (org_req, risk, problem, change, exception, tool, infra)"
sphinx-build -b needs . "${BUILD_DIR}"

if [[ ! -f "${BUILD_DIR}/needs.json" ]]; then
  echo "error: expected ${BUILD_DIR}/needs.json was not produced" >&2
  exit 1
fi

mkdir -p "${DEST_DIR}"
cp "${BUILD_DIR}/needs.json" "${DEST_FILE}"

echo "-- wrote ${DEST_FILE}"
echo "   needs/_external_needs/ is CI-generated, never committed — matches"
echo "   needs/conf.py's own comment on needs_external_needs. Re-run this"
echo "   any time root-project needs change before building needs/."
