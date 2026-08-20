#!/usr/bin/env bash
# tools/bump_governance.sh
#
# Deliberately adopt a new qorix-governance version in this product repo.
# This is the "one-line PR diff" the whole 50-product architecture depends
# on: three places must always agree on which governance version this
# product is audited against, and this script is what keeps them in sync
# instead of relying on someone remembering to edit all three by hand:
#
#   1. .qik/governance.lock   — the version this repo is pinned to
#   2. MODULE.bazel           — bazel_dep(qorix_governance, "<version>")
#   3. needs/_external_needs/org_needs.json — refetched at the new version
#
# Usage: tools/bump_governance.sh 1.5.0

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK_FILE="${REPO_ROOT}/.qik/governance.lock"
MODULE_FILE="${REPO_ROOT}/MODULE.bazel"

NEW_VERSION="${1:-}"
if [[ -z "${NEW_VERSION}" ]]; then
  echo "usage: $0 <new-version>   e.g. $0 1.5.0" >&2
  exit 2
fi
if [[ ! "${NEW_VERSION}" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "error: '${NEW_VERSION}' doesn't look like semver (X.Y.Z)" >&2
  exit 2
fi

OLD_VERSION=""
if [[ -f "${LOCK_FILE}" ]]; then
  OLD_VERSION="$(grep -E '^version\s*=' "${LOCK_FILE}" | head -n1 | sed -E 's/^version\s*=\s*"?([^"[:space:]]+)"?.*/\1/' || true)"
fi

echo "-- bumping qorix-governance: ${OLD_VERSION:-<none>} -> ${NEW_VERSION}"

mkdir -p "$(dirname "${LOCK_FILE}")"
cat > "${LOCK_FILE}" <<EOF
# Pinned qorix-governance version this product is audited against.
# Updated only by tools/bump_governance.sh — never hand-edit the version
# without also re-running this script, or MODULE.bazel and
# needs/_external_needs/org_needs.json will silently disagree with it.
version = "${NEW_VERSION}"
EOF
echo "-- wrote ${LOCK_FILE}"

if [[ -f "${MODULE_FILE}" ]]; then
  if grep -q 'bazel_dep(module_name = "qorix_governance"' "${MODULE_FILE}"; then
    sed -i -E "s/(bazel_dep\(module_name = \"qorix_governance\", version = \")[^\"]*(\"\))/\1${NEW_VERSION}\2/" "${MODULE_FILE}"
    echo "-- updated bazel_dep version in ${MODULE_FILE}"
  else
    echo "warning: no qorix_governance bazel_dep() found in ${MODULE_FILE} — add one manually:" >&2
    echo "  bazel_dep(module_name = \"qorix_governance\", version = \"${NEW_VERSION}\")" >&2
  fi
else
  echo "warning: ${MODULE_FILE} not found — skipping Bazel pin update" >&2
fi

echo "-- refetching needs.json at the new version"
"${REPO_ROOT}/tools/fetch_external_needs.sh" --version "${NEW_VERSION}"

cat <<EOF

Done. Review before committing:
  git diff -- .qik/governance.lock MODULE.bazel

Then run tools/build_needs.sh to confirm nothing under needs/ now points at
a governance id that changed or was removed in v${NEW_VERSION}.
EOF
