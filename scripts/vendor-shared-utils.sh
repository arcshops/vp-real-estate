#!/usr/bin/env bash
# Sync the canonical Shared_Utils into all consumer plugins.
# Usage:
#   scripts/vendor-shared-utils.sh           # sync canonical -> consumers
#   scripts/vendor-shared-utils.sh --check   # CI mode; fail if any consumer differs

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

MAP="scripts/shared-utils-vendor-map.json"
CANONICAL=$(python3 -c "import sys,json; print(json.load(open(sys.argv[1]))['canonical'])" "$MAP")
CHECK_MODE=0

if [[ "${1:-}" == "--check" ]]; then
  CHECK_MODE=1
fi

if [[ ! -d "$CANONICAL" ]]; then
  echo "ERROR: canonical Shared_Utils not found at $CANONICAL" >&2
  exit 1
fi

CONSUMERS=$(python3 -c "import sys,json; print('\n'.join(json.load(open(sys.argv[1])).get('consumers', [])))" "$MAP")
EXIT_CODE=0

while IFS= read -r consumer; do
  [[ -z "$consumer" ]] && continue
  parent_dir=$(dirname "$consumer")
  mkdir -p "$parent_dir"

  if [[ $CHECK_MODE -eq 1 ]]; then
    if ! diff -rq "$CANONICAL" "$consumer" > /dev/null 2>&1; then
      echo "DRIFT: $consumer differs from canonical $CANONICAL" >&2
      EXIT_CODE=1
    fi
  else
    rsync -a --delete "$CANONICAL/" "$consumer/"
    echo "vendored: $consumer"
  fi
done <<< "$CONSUMERS"

if [[ $CHECK_MODE -eq 1 && $EXIT_CODE -eq 0 ]]; then
  echo "All vendored copies match canonical."
fi

exit $EXIT_CODE
