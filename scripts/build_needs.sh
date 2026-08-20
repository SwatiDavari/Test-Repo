#!/usr/bin/env bash
# scripts/build_needs.sh
#
# Build needs/'s Sphinx-needs traceability graph: HTML docs for humans,
# needs.json for machines (tools/check_broken_links.py,
# tools/check_orphan_needs.py, the ci-needs.yml CI job).
#
# Assumes needs/_external_needs/org_needs.json has already been generated
# (see scripts/fetch_external_needs.sh) — the root project's org_req/risk/
# problem/change/exception/tool/infra needs that needs/'s :links: fields
# cite by ID must be present before the build, or every link to one of those
# ids will resolve as broken (see needs/conf.py's needs_external_needs).
#
# Usage: scripts/build_needs.sh [--venv PATH]

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
  echo "         Run scripts/fetch_external_needs.sh first, or every link" >&2
  echo "         to a root-project (org_req/risk/problem/...) id will" >&2
  echo "         build as broken." >&2
fi

if [[ ! -d "${VENV_DIR}" ]]; then
  echo "-- creating venv at ${VENV_DIR}"
  python3 -m venv "${VENV_DIR}"
fi
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

echo "-- installing needs/requirements.txt"
pip install --quiet -r "${NEEDS_DIR}/requirements.txt"

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
