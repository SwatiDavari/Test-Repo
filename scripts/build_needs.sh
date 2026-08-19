#!/usr/bin/env bash
# tools/build_needs.sh
#
# Build this product's Sphinx-needs traceability graph: HTML docs for humans,
# needs.json for machines (qik axon, tools/check_broken_links.py, the
# needs-gate.yml CI job).
#
# Assumes needs/_external_needs/org_needs.json has already been fetched
# (see tools/fetch_external_needs.sh) — the central governance content this
# product cites by ID must be present before the build, or every :links:
# field pointing at a governance id will resolve as broken.
#
# Usage: tools/build_needs.sh [--venv PATH]

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NEEDS_DIR="${REPO_ROOT}/needs"
VENV_DIR="${REPO_ROOT}/.venv"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --venv) VENV_DIR="$2"; shift 2 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

if [[ ! -d "${NEEDS_DIR}" ]]; then
  echo "error: ${NEEDS_DIR} does not exist" >&2
  exit 1
fi

if [[ ! -f "${NEEDS_DIR}/_external_needs/org_needs.json" ]]; then
  echo "warning: needs/_external_needs/org_needs.json is missing." >&2
  echo "         Run tools/fetch_external_needs.sh first, or every link" >&2
  echo "         to a central-governance id will build as broken." >&2
fi

if [[ ! -d "${VENV_DIR}" ]]; then
  echo "-- creating venv at ${VENV_DIR}"
  python3 -m venv "${VENV_DIR}"
fi
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

echo "-- installing needs/requirements-docs.txt"
pip install --quiet -r "${NEEDS_DIR}/requirements-docs.txt"

echo "-- building HTML (warnings as errors)"
sphinx-build -b html -W "${NEEDS_DIR}" "${NEEDS_DIR}/_build/html"

echo "-- building needs.json"
sphinx-build -b needs "${NEEDS_DIR}" "${NEEDS_DIR}/_build/needs"

NEEDS_JSON="${NEEDS_DIR}/_build/needs/needs.json"
if [[ -f "${NEEDS_JSON}" ]]; then
  COUNT=$(python3 -c "
import json
d = json.load(open('${NEEDS_JSON}'))
v = d.get('versions', {})
cur = d.get('current_version', '')
needs = (v.get(cur) or next(iter(v.values()), {})).get('needs', {})
print(len(needs))
")
  echo "-- done: ${COUNT} need(s) in ${NEEDS_JSON}"
else
  echo "error: expected ${NEEDS_JSON} was not produced" >&2
  exit 1
fi
