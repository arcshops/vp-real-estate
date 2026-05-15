#!/usr/bin/env bash
# Generate output-styles/ and skills/ artifacts from personas/ masters.
# Usage:
#   scripts/build-personas.sh           # generate
#   scripts/build-personas.sh --check   # CI mode; fail if generated files would change

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

PERSONAS_DIR="plugins/common-utilities/personas"
OUTPUT_STYLES_DIR="plugins/common-utilities/output-styles"
SKILLS_DIR="plugins/common-utilities/skills"
CHECK_MODE=0

if [[ "${1:-}" == "--check" ]]; then
  CHECK_MODE=1
fi

declare -A OS_NAME=(
  [dennis]="Dennis Advisory"
  [reggie]="Reggie Chan VP"
  [adam]="Adam Analyst"
)
declare -A SKILL_DIR=(
  [dennis]="dennis-advisor"
  [reggie]="reggie-vp"
  [adam]="adam-analyst"
)

generate_for() {
  local slug="$1"
  local master="$PERSONAS_DIR/$slug.md"

  if [[ ! -f "$master" ]]; then
    echo "ERROR: master $master not found" >&2
    return 1
  fi

  local description
  description=$(awk '/^---$/{f++; next} f==1 && /^description:/{sub(/^description: */, ""); print; exit}' "$master")
  local body
  body=$(awk '/^---$/{f++; next} f==2' "$master")

  local os_file="$OUTPUT_STYLES_DIR/$slug.md"
  local os_content
  os_content=$(cat <<EOF
---
name: ${OS_NAME[$slug]}
description: $description
keep-coding-instructions: false
---

$body
EOF
)

  local skill_subdir="$SKILLS_DIR/${SKILL_DIR[$slug]}"
  local skill_file="$skill_subdir/SKILL.md"
  local skill_content
  skill_content=$(cat <<EOF
---
description: $description
---

$body
EOF
)

  if [[ $CHECK_MODE -eq 1 ]]; then
    if [[ ! -f "$os_file" ]] || ! diff <(echo "$os_content") "$os_file" > /dev/null; then
      echo "DRIFT: $os_file would change" >&2
      return 1
    fi
    if [[ ! -f "$skill_file" ]] || ! diff <(echo "$skill_content") "$skill_file" > /dev/null; then
      echo "DRIFT: $skill_file would change" >&2
      return 1
    fi
  else
    mkdir -p "$OUTPUT_STYLES_DIR" "$skill_subdir"
    echo "$os_content" > "$os_file"
    echo "$skill_content" > "$skill_file"
    echo "generated: $os_file"
    echo "generated: $skill_file"
  fi
}

EXIT_CODE=0
for slug in dennis reggie adam; do
  generate_for "$slug" || EXIT_CODE=1
done

if [[ $CHECK_MODE -eq 1 && $EXIT_CODE -eq 0 ]]; then
  echo "All generated persona artifacts match masters."
fi

exit $EXIT_CODE
