#!/usr/bin/env bash
# tools/fetch_external_needs.sh
#
# Pull the central qorix-governance repo's published needs.json at the
# version pinned in .qik/governance.lock, and place it where needs/conf.py's
# needs_external_needs expects it: needs/_external_needs/org_needs.json.
#
# This is the cross-repo generalization of the mechanism test_repo already
# runs *inside one repo* (root project's org_req needs exported into
# Needs/_external_needs/org_needs.json, per the existing ci-needs.yml job)
# — same idea, just fetching a GitHub Release asset from a separate repo
# instead of building a local Sphinx project first.
#
# Requires: gh (GitHub CLI), authenticated with read access to
# qorix/qorix-governance.
#
# Usage: tools/fetch_external_needs.sh [--version X.Y.Z]
#   Without --version, reads the pinned version from .qik/governance.lock.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK_FILE="${REPO_ROOT}/.qik/governance.lock"
DEST_DIR="${REPO_ROOT}/needs/_external_needs"
DEST_FILE="${DEST_DIR}/org_needs.json"
GOVERNANCE_REPO="qorix/qorix-governance"
VERSION=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --version) VERSION="$2"; shift 2 ;;
    --repo) GOVERNANCE_REPO="$2"; shift 2 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

if [[ -z "${VERSION}" ]]; then
  if [[ ! -f "${LOCK_FILE}" ]]; then
    echo "error: no --version given and ${LOCK_FILE} does not exist" >&2
    exit 1
  fi
  VERSION="$(grep -E '^version\s*=' "${LOCK_FILE}" | head -n1 | sed -E 's/^version\s*=\s*"?([^"[:space:]]+)"?.*/\1/')"
  if [[ -z "${VERSION}" ]]; then
    echo "error: could not parse a version out of ${LOCK_FILE}" >&2
    echo "       expected a line like: version = \"1.4.0\"" >&2
    exit 1
  fi
fi

echo "-- fetching ${GOVERNANCE_REPO} @ v${VERSION} needs.json"

if ! command -v gh >/dev/null 2>&1; then
  echo "error: gh (GitHub CLI) is required — https://cli.github.com/" >&2
  exit 1
fi

mkdir -p "${DEST_DIR}"
TMP_FILE="$(mktemp)"
trap 'rm -f "${TMP_FILE}"' EXIT

if ! gh release download "v${VERSION}" \
      --repo "${GOVERNANCE_REPO}" \
      --pattern "needs.json" \
      --output "${TMP_FILE}" \
      --clobber; then
  echo "error: could not download needs.json for v${VERSION} from ${GOVERNANCE_REPO}" >&2
  echo "       check that the release/tag exists and gh is authenticated" >&2
  exit 1
fi

python3 -c "import json,sys; json.load(open(sys.argv[1]))" "${TMP_FILE}" \
  || { echo "error: downloaded file is not valid JSON" >&2; exit 1; }

mv "${TMP_FILE}" "${DEST_FILE}"
trap - EXIT

echo "-- wrote ${DEST_FILE} (governance v${VERSION})"
echo "   .gitignore should exclude needs/_external_needs/ — this file is"
echo "   fetched at build time, never committed."
