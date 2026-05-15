#!/usr/bin/env bash
# Run vendor-shared-utils and build-personas together (with optional --check).
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/vendor-shared-utils.sh" "$@"
"$SCRIPT_DIR/build-personas.sh" "$@"
