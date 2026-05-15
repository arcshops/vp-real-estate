# Plugin Marketplace Conversion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert `vp-real-estate` from the legacy `.claude/commands` + `.claude/skills` layout into a Claude Code plugin marketplace hosting six installable plugins, with single hard-cutover PR.

**Architecture:** Monorepo with `.claude-plugin/marketplace.json` at root and six plugins under `plugins/`. Each plugin owns its skills, commands, agents, and calculator scripts. `Shared_Utils` is vendored from a canonical copy in `common-utilities` via `scripts/vendor-shared-utils.sh`. Trio personas (Adam/Reggie/Dennis) are generated from `personas/` masters into both `output-styles/` and `skills/` via `scripts/build-personas.sh`. Custom skill-activation hooks are retired; `subagent-stop.sh` is ported to `common-utilities`.

**Tech Stack:** Bash, Python, git, jq, rsync, Claude Code plugin spec.

**Reference spec:** `/home/reggiechan/vp-real-estate/docs/superpowers/specs/2026-05-15-plugin-marketplace-design.md`

**Branch:** All work happens on `feat/plugin-marketplace` off `main`. Do not merge until all phases pass Phase 9 verification.

---

## Phase 0 — Scaffolding

### Task 1: Create the feature branch and verify clean working tree

**Files:** (no file changes; branch creation only)

- [ ] **Step 1: Verify clean working tree**

```bash
cd /home/reggiechan/vp-real-estate
git status
```
Expected: `nothing to commit, working tree clean` (the design spec was previously written; if it's uncommitted, commit it first as `docs: add plugin marketplace design spec`).

- [ ] **Step 2: Create and switch to feature branch**

```bash
git checkout -b feat/plugin-marketplace
git status
```
Expected: `On branch feat/plugin-marketplace`.

- [ ] **Step 3: Verify git identity is set (needed for later commits)**

```bash
git config user.email
git config user.name
```
Expected: both return values. If empty, set them with `git config user.email "reggie.chan@gmail.com"` and `git config user.name "Reggie Chan"`.

---

### Task 2: Create the directory skeleton for all six plugins

**Files:**
- Create: `.claude-plugin/marketplace.json` (placeholder, will be populated in Task 3)
- Create: `plugins/<six-plugins>/.claude-plugin/plugin.json` (placeholders, populated in Task 4)
- Create: empty `skills/`, `commands/`, `agents/`, `hooks/`, `output-styles/`, `personas/` subdirs

- [ ] **Step 1: Create marketplace + plugin directories**

```bash
mkdir -p .claude-plugin
mkdir -p plugins/leasing-commercial/{.claude-plugin,skills,commands,agents}
mkdir -p plugins/tenancies-residential/{.claude-plugin,skills,commands,agents}
mkdir -p plugins/expropriation-law/{.claude-plugin,skills,commands,agents}
mkdir -p plugins/appraisal-valuation/{.claude-plugin,skills,commands,agents}
mkdir -p plugins/infrastructure-corridor-ops/{.claude-plugin,skills,commands,agents}
mkdir -p plugins/common-utilities/{.claude-plugin,skills,commands,agents,hooks,output-styles,personas,shared_utils}
mkdir -p scripts
```

- [ ] **Step 2: Verify directory structure**

```bash
find .claude-plugin plugins scripts -type d | sort
```
Expected: 7 plugin-related top-level paths + 36 subdirectories listed.

- [ ] **Step 3: Add .gitkeep to empty dirs so git tracks them**

```bash
find plugins -type d -empty -exec touch {}/.gitkeep \;
```

---

### Task 3: Write the marketplace manifest

**Files:**
- Create: `.claude-plugin/marketplace.json`

- [ ] **Step 1: Write marketplace.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "vp-real-estate",
  "owner": {
    "name": "Reggie Chan",
    "email": "reggie.chan@gmail.com"
  },
  "description": "Commercial real estate lease analysis, expropriation, appraisal, and linear infrastructure plugins for property professionals",
  "version": "3.0.0",
  "metadata": {
    "pluginRoot": "./plugins"
  },
  "plugins": [
    {
      "name": "leasing-commercial",
      "source": "./plugins/leasing-commercial",
      "description": "Commercial lease analysis: abstraction, effective rent, tenant credit, options valuation, IFRS 16, consents, surrender, compliance",
      "version": "1.0.0"
    },
    {
      "name": "tenancies-residential",
      "source": "./plugins/tenancies-residential",
      "description": "Ontario Residential Tenancies Act: eviction procedures, LTB hearings, tenant relief analysis",
      "version": "1.0.0"
    },
    {
      "name": "expropriation-law",
      "source": "./plugins/expropriation-law",
      "description": "Ontario Expropriations Act: statutory interpretation, compensation entitlement, procedural defects, deadline tracking, Forms 1-12, settlement, severance damages, injurious affection",
      "version": "1.0.0"
    },
    {
      "name": "appraisal-valuation",
      "source": "./plugins/appraisal-valuation",
      "description": "Property valuation: cost approach, income approach, easement valuation, comparable sales adjustment (DCA + MCDA), title, environmental due diligence",
      "version": "1.0.0"
    },
    {
      "name": "infrastructure-corridor-ops",
      "source": "./plugins/infrastructure-corridor-ops",
      "description": "Linear infrastructure acquisition: agricultural easements, cropland compensation, land assembly, public consultation, NIMBY response, transit station siting, transmission line specs, right-of-way",
      "version": "1.0.0"
    },
    {
      "name": "common-utilities",
      "source": "./plugins/common-utilities",
      "description": "Foundation plugin: analyst trio personas (Adam/Reggie/Dennis), cross-cutting skills, canonical Shared_Utils, subagent-stop hook",
      "version": "1.0.0"
    }
  ]
}
```

- [ ] **Step 2: Validate JSON syntax**

```bash
jq empty .claude-plugin/marketplace.json && echo "OK"
```
Expected: `OK`.

---

### Task 4: Write the six plugin manifests

**Files:**
- Create: `plugins/leasing-commercial/.claude-plugin/plugin.json`
- Create: `plugins/tenancies-residential/.claude-plugin/plugin.json`
- Create: `plugins/expropriation-law/.claude-plugin/plugin.json`
- Create: `plugins/appraisal-valuation/.claude-plugin/plugin.json`
- Create: `plugins/infrastructure-corridor-ops/.claude-plugin/plugin.json`
- Create: `plugins/common-utilities/.claude-plugin/plugin.json`

- [ ] **Step 1: Write `plugins/leasing-commercial/.claude-plugin/plugin.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "leasing-commercial",
  "version": "1.0.0",
  "description": "Commercial lease analysis toolkit (industrial + office): abstraction, effective rent, tenant credit, options valuation, IFRS 16, consents, surrender, compliance",
  "author": { "name": "Reggie Chan", "email": "reggie.chan@gmail.com" },
  "repository": "https://github.com/reggiechan/vp-real-estate",
  "license": "see LICENSE in repo root",
  "skills": "./skills/",
  "commands": "./commands/",
  "agents": "./agents/",
  "dependencies": [
    { "name": "common-utilities", "version": "^1.0.0" }
  ]
}
```

- [ ] **Step 2: Write `plugins/tenancies-residential/.claude-plugin/plugin.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "tenancies-residential",
  "version": "1.0.0",
  "description": "Ontario Residential Tenancies Act: eviction procedures, LTB hearings, tenant relief analysis",
  "author": { "name": "Reggie Chan", "email": "reggie.chan@gmail.com" },
  "repository": "https://github.com/reggiechan/vp-real-estate",
  "license": "see LICENSE in repo root",
  "skills": "./skills/",
  "commands": "./commands/",
  "agents": "./agents/",
  "dependencies": [
    { "name": "common-utilities", "version": "^1.0.0" }
  ]
}
```

- [ ] **Step 3: Write `plugins/expropriation-law/.claude-plugin/plugin.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "expropriation-law",
  "version": "1.0.0",
  "description": "Ontario Expropriations Act: statutory interpretation, compensation entitlement, procedural defects, deadline tracking, Forms 1-12, settlement, severance damages, injurious affection",
  "author": { "name": "Reggie Chan", "email": "reggie.chan@gmail.com" },
  "repository": "https://github.com/reggiechan/vp-real-estate",
  "license": "see LICENSE in repo root",
  "skills": "./skills/",
  "commands": "./commands/",
  "agents": "./agents/",
  "dependencies": [
    { "name": "common-utilities", "version": "^1.0.0" }
  ]
}
```

- [ ] **Step 4: Write `plugins/appraisal-valuation/.claude-plugin/plugin.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "appraisal-valuation",
  "version": "1.0.0",
  "description": "Property valuation: cost approach, income approach, easement valuation, comparable sales adjustment (DCA + MCDA), title, environmental due diligence",
  "author": { "name": "Reggie Chan", "email": "reggie.chan@gmail.com" },
  "repository": "https://github.com/reggiechan/vp-real-estate",
  "license": "see LICENSE in repo root",
  "skills": "./skills/",
  "commands": "./commands/",
  "agents": "./agents/",
  "dependencies": [
    { "name": "common-utilities", "version": "^1.0.0" }
  ]
}
```

- [ ] **Step 5: Write `plugins/infrastructure-corridor-ops/.claude-plugin/plugin.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "infrastructure-corridor-ops",
  "version": "1.0.0",
  "description": "Linear infrastructure acquisition: agricultural easements, cropland compensation, land assembly, public consultation, NIMBY response, transit station siting, transmission line specs, right-of-way",
  "author": { "name": "Reggie Chan", "email": "reggie.chan@gmail.com" },
  "repository": "https://github.com/reggiechan/vp-real-estate",
  "license": "see LICENSE in repo root",
  "skills": "./skills/",
  "commands": "./commands/",
  "agents": "./agents/",
  "dependencies": [
    { "name": "common-utilities", "version": "^1.0.0" }
  ]
}
```

- [ ] **Step 6: Write `plugins/common-utilities/.claude-plugin/plugin.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "common-utilities",
  "version": "1.0.0",
  "description": "Foundation plugin: analyst trio personas, cross-cutting skills, canonical Shared_Utils source-of-truth, subagent-stop hook",
  "author": { "name": "Reggie Chan", "email": "reggie.chan@gmail.com" },
  "repository": "https://github.com/reggiechan/vp-real-estate",
  "license": "see LICENSE in repo root",
  "skills": "./skills/",
  "commands": "./commands/",
  "outputStyles": "./output-styles/",
  "hooks": "./hooks/hooks.json"
}
```

- [ ] **Step 7: Validate all six manifests**

```bash
for f in plugins/*/.claude-plugin/plugin.json; do
  jq empty "$f" && echo "OK: $f"
done
```
Expected: 6 "OK" lines.

---

### Task 5: Author the vendor-shared-utils.sh script

**Files:**
- Create: `scripts/vendor-shared-utils.sh`
- Create: `scripts/shared-utils-vendor-map.json`

- [ ] **Step 1: Write `scripts/shared-utils-vendor-map.json` (initial — will be expanded in Phase 3)**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "canonical": "plugins/common-utilities/shared_utils",
  "consumers": []
}
```

- [ ] **Step 2: Write `scripts/vendor-shared-utils.sh`**

```bash
#!/usr/bin/env bash
# Sync the canonical Shared_Utils into all consumer plugins.
# Usage:
#   scripts/vendor-shared-utils.sh           # sync canonical -> consumers
#   scripts/vendor-shared-utils.sh --check   # CI mode; fail if any consumer differs

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

MAP="scripts/shared-utils-vendor-map.json"
CANONICAL=$(jq -r '.canonical' "$MAP")
CHECK_MODE=0

if [[ "${1:-}" == "--check" ]]; then
  CHECK_MODE=1
fi

if [[ ! -d "$CANONICAL" ]]; then
  echo "ERROR: canonical Shared_Utils not found at $CANONICAL" >&2
  exit 1
fi

CONSUMERS=$(jq -r '.consumers[]' "$MAP")
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
```

- [ ] **Step 3: Make executable**

```bash
chmod +x scripts/vendor-shared-utils.sh
```

- [ ] **Step 4: Smoke test (should report empty consumer list)**

```bash
scripts/vendor-shared-utils.sh --check
```
Expected: `ERROR: canonical Shared_Utils not found at plugins/common-utilities/shared_utils` (because canonical isn't populated yet — this confirms the script works). Will succeed after Phase 3.

---

### Task 6: Author the build-personas.sh script

**Files:**
- Create: `scripts/build-personas.sh`

- [ ] **Step 1: Write `scripts/build-personas.sh`**

```bash
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

# Map: persona slug -> output-style display name, skill subdirectory name
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

# Extract YAML frontmatter and body from master file.
# Master frontmatter must contain `description:` and may contain `voice:`.
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

  # Output style artifact
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

  # Skill artifact
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
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/build-personas.sh
```

- [ ] **Step 3: Smoke test (should report missing masters)**

```bash
scripts/build-personas.sh
```
Expected: 3 "ERROR: master ... not found" lines (masters get populated in Phase 5).

---

### Task 7: Author the sync-all.sh wrapper

**Files:**
- Create: `scripts/sync-all.sh`

- [ ] **Step 1: Write `scripts/sync-all.sh`**

```bash
#!/usr/bin/env bash
# Run vendor-shared-utils and build-personas together (with optional --check).
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/vendor-shared-utils.sh" "$@"
"$SCRIPT_DIR/build-personas.sh" "$@"
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/sync-all.sh
```

---

### Task 8: Commit Phase 0 scaffolding

- [ ] **Step 1: Stage and commit**

```bash
git add .claude-plugin plugins scripts
git commit -m "feat(marketplace): scaffold marketplace manifest, 6 plugin manifests, and sync scripts"
```
Expected: commit succeeds, working tree clean.

---

## Phase 1 — Skills migration

### Task 9: Move leasing-commercial skills (24 skills)

**Files:**
- Move (git mv): 24 skill directories from `.claude/skills/<name>/` to `plugins/leasing-commercial/skills/<name>/`

- [ ] **Step 1: Remove .gitkeep from target dir**

```bash
rm plugins/leasing-commercial/skills/.gitkeep
```

- [ ] **Step 2: Move all 24 leasing-commercial skills**

```bash
for skill in \
  commercial-lease-expert \
  commercial-lease-assignment-consent-framework \
  commercial-tenancies-act-enforcement-remedies \
  consent-to-assignment-expert \
  consent-to-sublease-expert \
  default-and-remedies-advisor \
  effective-rent-analyzer \
  indemnity-expert \
  lease-abstraction-specialist \
  lease-arbitration-expert \
  lease-comparison-expert \
  lease-compliance-auditor \
  lease-surrender-expert \
  non-disturbance-expert \
  objection-handling-expert \
  offer-to-lease-expert \
  portfolio-strategy-advisor \
  real-options-valuation-expert \
  share-transfer-consent-expert \
  storage-agreement-expert \
  telecom-licensing-expert \
  temporary-license-expert \
  tenant-credit-analyst \
  waiver-agreement-expert; do
  git mv ".claude/skills/$skill" "plugins/leasing-commercial/skills/$skill"
done
```

- [ ] **Step 3: Verify count**

```bash
ls plugins/leasing-commercial/skills/ | wc -l
```
Expected: `24`.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(leasing-commercial): migrate 24 commercial leasing skills"
```

---

### Task 10: Move tenancies-residential skills (3 skills)

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/tenancies-residential/skills/.gitkeep
```

- [ ] **Step 2: Move 3 skills**

```bash
for skill in \
  residential-tenancies-act-eviction-procedures \
  ltb-application-hearing-procedures \
  tenant-relief-from-eviction-analysis; do
  git mv ".claude/skills/$skill" "plugins/tenancies-residential/skills/$skill"
done
```

- [ ] **Step 3: Verify**

```bash
ls plugins/tenancies-residential/skills/ | wc -l
```
Expected: `3`.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(tenancies-residential): migrate 3 RTA skills"
```

---

### Task 11: Move expropriation-law skills (9 skills)

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/expropriation-law/skills/.gitkeep
```

- [ ] **Step 2: Move 9 skills**

```bash
for skill in \
  ontario-expropriations-act-statutory-interpretation \
  expropriation-compensation-entitlement-analysis \
  expropriation-procedural-defect-analysis \
  expropriation-statutory-deadline-tracking \
  expropriation-timeline-expert \
  forms-1-12-completeness-verification \
  settlement-analysis-expert \
  severance-damages-quantification \
  injurious-affection-assessment; do
  git mv ".claude/skills/$skill" "plugins/expropriation-law/skills/$skill"
done
```

- [ ] **Step 3: Verify**

```bash
ls plugins/expropriation-law/skills/ | wc -l
```
Expected: `9`.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(expropriation-law): migrate 9 expropriation skills"
```

---

### Task 12: Move appraisal-valuation skills (6 skills)

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/appraisal-valuation/skills/.gitkeep
```

- [ ] **Step 2: Move 6 skills**

```bash
for skill in \
  cost-approach-expert \
  easement-valuation-methods \
  income-approach-expert \
  comparable-sales-adjustment-methodology \
  title-expert \
  environmental-due-diligence-expert; do
  git mv ".claude/skills/$skill" "plugins/appraisal-valuation/skills/$skill"
done
```

- [ ] **Step 3: Verify**

```bash
ls plugins/appraisal-valuation/skills/ | wc -l
```
Expected: `6`.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(appraisal-valuation): migrate 6 valuation skills"
```

---

### Task 13: Move infrastructure-corridor-ops skills (10 skills)

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/infrastructure-corridor-ops/skills/.gitkeep
```

- [ ] **Step 2: Move 10 skills**

```bash
for skill in \
  agricultural-easement-negotiation-frameworks \
  cropland-out-of-production-agreements \
  land-assembly-expert \
  public-consultation-process-design \
  nimby-objection-analysis-response \
  residential-displacement-mitigation-protocols \
  right-of-way-expert \
  stakeholder-management-expert \
  transit-station-site-acquisition-strategy \
  transmission-line-technical-specifications; do
  git mv ".claude/skills/$skill" "plugins/infrastructure-corridor-ops/skills/$skill"
done
```

- [ ] **Step 3: Verify**

```bash
ls plugins/infrastructure-corridor-ops/skills/ | wc -l
```
Expected: `10`.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(infrastructure-corridor-ops): migrate 10 corridor ops skills"
```

---

### Task 14: Move common-utilities cross-cutting skills (4 skills)

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/common-utilities/skills/.gitkeep
```

- [ ] **Step 2: Move 4 cross-cutting skills**

```bash
for skill in \
  negotiation-expert \
  negotiation-expert-infrastructure \
  board-memo-expert \
  briefing-note-expert; do
  git mv ".claude/skills/$skill" "plugins/common-utilities/skills/$skill"
done
```

- [ ] **Step 3: Verify `.claude/skills/` is now empty**

```bash
ls .claude/skills/ | wc -l
```
Expected: `0`.

- [ ] **Step 4: Verify total skills migrated = 56**

```bash
find plugins -mindepth 3 -maxdepth 3 -type d -name '*-*' | grep '/skills/' | wc -l
```
Expected: `56`.

- [ ] **Step 5: Commit**

```bash
git commit -m "feat(common-utilities): migrate 4 cross-cutting skills"
```

---

## Phase 2 — Commands migration

### Task 15: Move leasing-commercial command subdirs

**Files:**
- Move (git mv): 5 command subdirs from `.claude/commands/` to `plugins/leasing-commercial/commands/`
  - `Abstraction/` → `plugins/leasing-commercial/commands/Abstraction/`
  - `Accounting/` → `plugins/leasing-commercial/commands/Accounting/`
  - `Comparison/` → `plugins/leasing-commercial/commands/Comparison/`
  - `Compliance/` → `plugins/leasing-commercial/commands/Compliance/`
  - `Financial_Analysis/` → `plugins/leasing-commercial/commands/Financial_Analysis/`

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/leasing-commercial/commands/.gitkeep
```

- [ ] **Step 2: Move 5 command subdirs**

```bash
for subdir in Abstraction Accounting Comparison Compliance Financial_Analysis; do
  git mv ".claude/commands/$subdir" "plugins/leasing-commercial/commands/$subdir"
done
```

- [ ] **Step 3: Verify**

```bash
ls plugins/leasing-commercial/commands/
```
Expected: 5 directories listed.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(leasing-commercial): migrate 5 command subdirectories"
```

---

### Task 16: Move expropriation-law command subdir

- [ ] **Step 1: Remove .gitkeep and move `Expropriation/`**

```bash
rm plugins/expropriation-law/commands/.gitkeep
git mv .claude/commands/Expropriation plugins/expropriation-law/commands/Expropriation
```

- [ ] **Step 2: Move expropriation-specific commands from `Process/`**

The `.claude/commands/Process/` subdir is being split across multiple plugins. Move only the expropriation-related files now.

```bash
mkdir -p plugins/expropriation-law/commands/Process
git mv .claude/commands/Process/expropriation-timeline.md plugins/expropriation-law/commands/Process/expropriation-timeline.md
git mv .claude/commands/Process/settlement-analysis.md plugins/expropriation-law/commands/Process/settlement-analysis.md
```

- [ ] **Step 3: Verify**

```bash
ls plugins/expropriation-law/commands/Expropriation/ plugins/expropriation-law/commands/Process/
```
Expected: Expropriation has 3 .md files; Process has 2 .md files.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(expropriation-law): migrate Expropriation/ and 2 Process/ commands"
```

---

### Task 17: Move appraisal-valuation command subdirs

**Files:**
- Move `Valuation/` (3 files: comparable-sales-analysis.md, easement-valuation.md, mcda-sales-comparison.md)
- Move 4 of 5 files from `Specialized/` (cost-approach-infrastructure.md, environmental-due-diligence.md, income-approach-land.md, title-analysis.md) — `utility-conflict-analysis.md` goes to infrastructure-corridor-ops

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/appraisal-valuation/commands/.gitkeep
```

- [ ] **Step 2: Move `Valuation/`**

```bash
git mv .claude/commands/Valuation plugins/appraisal-valuation/commands/Valuation
```

- [ ] **Step 3: Move 4 of 5 files from `Specialized/`**

```bash
mkdir -p plugins/appraisal-valuation/commands/Specialized
for f in cost-approach-infrastructure.md environmental-due-diligence.md income-approach-land.md title-analysis.md; do
  git mv ".claude/commands/Specialized/$f" "plugins/appraisal-valuation/commands/Specialized/$f"
done
```

- [ ] **Step 4: Verify**

```bash
ls plugins/appraisal-valuation/commands/Valuation/ plugins/appraisal-valuation/commands/Specialized/
```
Expected: Valuation has 3 files; Specialized has 4 files. `.claude/commands/Specialized/` still contains `utility-conflict-analysis.md`.

- [ ] **Step 5: Commit**

```bash
git commit -m "feat(appraisal-valuation): migrate Valuation/ and 4 Specialized/ commands"
```

---

### Task 18: Move infrastructure-corridor-ops command subdirs

**Files:**
- Move: `Infrastructure/`, `Transit/`, remaining `Specialized/utility-conflict-analysis.md`, `Process/public-consultation-summary.md`

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/infrastructure-corridor-ops/commands/.gitkeep
```

- [ ] **Step 2: Move `Infrastructure/` and `Transit/`**

```bash
git mv .claude/commands/Infrastructure plugins/infrastructure-corridor-ops/commands/Infrastructure
git mv .claude/commands/Transit plugins/infrastructure-corridor-ops/commands/Transit
```

- [ ] **Step 3: Move remaining `Specialized/utility-conflict-analysis.md`**

```bash
mkdir -p plugins/infrastructure-corridor-ops/commands/Specialized
git mv .claude/commands/Specialized/utility-conflict-analysis.md plugins/infrastructure-corridor-ops/commands/Specialized/utility-conflict-analysis.md
```

- [ ] **Step 4: Move `Process/public-consultation-summary.md`**

```bash
mkdir -p plugins/infrastructure-corridor-ops/commands/Process
git mv .claude/commands/Process/public-consultation-summary.md plugins/infrastructure-corridor-ops/commands/Process/public-consultation-summary.md
```

- [ ] **Step 5: Verify `.claude/commands/Specialized/` is now empty and remove**

```bash
ls .claude/commands/Specialized/ 2>/dev/null
rmdir .claude/commands/Specialized 2>/dev/null && echo "Specialized/ removed"
```
Expected: empty listing, then "Specialized/ removed".

- [ ] **Step 6: Commit**

```bash
git commit -m "feat(infrastructure-corridor-ops): migrate Infrastructure/, Transit/, utility-conflict-analysis, public-consultation-summary"
```

---

### Task 19: Move common-utilities command subdirs

**Files:**
- Move: `Utilities/`, remaining 3 `Process/` files (board-memo.md, briefing-note.md, negotiation-strategy.md), and `README.md`

- [ ] **Step 1: Remove .gitkeep**

```bash
rm plugins/common-utilities/commands/.gitkeep
```

- [ ] **Step 2: Move `Utilities/`**

```bash
git mv .claude/commands/Utilities plugins/common-utilities/commands/Utilities
```

- [ ] **Step 3: Move remaining 3 `Process/` files**

```bash
mkdir -p plugins/common-utilities/commands/Process
for f in board-memo.md briefing-note.md negotiation-strategy.md; do
  git mv ".claude/commands/Process/$f" "plugins/common-utilities/commands/Process/$f"
done
```

- [ ] **Step 4: Verify `.claude/commands/Process/` is empty and remove**

```bash
ls .claude/commands/Process/
rmdir .claude/commands/Process
```

- [ ] **Step 5: Move README.md (marketplace-level, but useful in common-utilities for now)**

```bash
git mv .claude/commands/README.md plugins/common-utilities/commands/README.md
```

- [ ] **Step 6: Verify `.claude/commands/` is empty**

```bash
ls .claude/commands/
```
Expected: empty.

- [ ] **Step 7: Commit**

```bash
git commit -m "feat(common-utilities): migrate Utilities/, 3 Process/ commands, and commands README"
```

---

### Task 20: Update path references in command markdown files

Commands reference calculator scripts via paths like `Eff_Rent_Calculator/eff_rent_calculator.py`. These must change to `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<script>`. The Reports/ path becomes `$CLAUDE_PROJECT_DIR/Reports/`. NOTE: Phase 3 will *also* edit these files after calculator scripts move; this task does the path strings now while paths are predictable.

**Files:** All `.md` files under `plugins/*/commands/`

- [ ] **Step 1: Dry-run inventory of path references**

```bash
grep -rn "Eff_Rent_Calculator\|IFRS16_Calculator\|Option_Valuation\|Renewal_Analysis\|Rental_Variance\|Rental_Yield_Curve\|Rollover_Analysis\|Default_Calculator\|Credit_Analysis\|Comparable_Sales_Analysis\|MCDA_Sales_Comparison\|MLS_Extractor\|Relative_Valuation\|Location_Overview\|Expropriation_Forms\|Shared_Utils\|^Reports/\| Reports/\|^Templates/\| Templates/" plugins/*/commands/ | head -40
```
Expected: list of files with old path references. Record file list — these are the targets for editing.

- [ ] **Step 2: For each command markdown that references old calculator paths, replace with `${CLAUDE_PLUGIN_ROOT}` form**

Edit each file individually using sed. Mapping table:

| Old reference | New reference (within leasing-commercial) |
|---|---|
| `Eff_Rent_Calculator/eff_rent_calculator.py` | `${CLAUDE_PLUGIN_ROOT}/skills/effective-rent-analyzer/scripts/eff_rent_calculator.py` |
| `IFRS16_Calculator/ifrs16_calculator.py` | `${CLAUDE_PLUGIN_ROOT}/skills/effective-rent-analyzer/scripts/ifrs16_calculator.py` |
| `Option_Valuation/option_valuation.py` | `${CLAUDE_PLUGIN_ROOT}/skills/real-options-valuation-expert/scripts/option_valuation.py` |
| `Renewal_Analysis/renewal_analysis.py` | `${CLAUDE_PLUGIN_ROOT}/skills/portfolio-strategy-advisor/scripts/renewal_analysis.py` |
| `Rental_Variance/rental_variance.py` | `${CLAUDE_PLUGIN_ROOT}/skills/lease-comparison-expert/scripts/rental_variance.py` |
| `Rental_Yield_Curve/rental_yield_curve.py` | `${CLAUDE_PLUGIN_ROOT}/skills/portfolio-strategy-advisor/scripts/rental_yield_curve.py` |
| `Rollover_Analysis/rollover_analysis.py` | `${CLAUDE_PLUGIN_ROOT}/skills/portfolio-strategy-advisor/scripts/rollover_analysis.py` |
| `Default_Calculator/default_calculator.py` | `${CLAUDE_PLUGIN_ROOT}/skills/default-and-remedies-advisor/scripts/default_calculator.py` |
| `Credit_Analysis/credit_analysis.py` | `${CLAUDE_PLUGIN_ROOT}/skills/tenant-credit-analyst/scripts/credit_analysis.py` |
| `MLS_Extractor/mls_extractor.py` | `${CLAUDE_PLUGIN_ROOT}/skills/lease-abstraction-specialist/scripts/mls_extractor.py` |
| `Relative_Valuation/relative_valuation.py` | `${CLAUDE_PLUGIN_ROOT}/skills/portfolio-strategy-advisor/scripts/relative_valuation.py` |
| `Templates/Industrial/` | `${CLAUDE_PLUGIN_ROOT}/templates/Industrial/` |
| `Templates/Office/` | `${CLAUDE_PLUGIN_ROOT}/templates/Office/` |
| `Comparable_Sales_Analysis/comparable_sales_calculator.py` | `${CLAUDE_PLUGIN_ROOT}/skills/comparable-sales-adjustment-methodology/scripts/comparable_sales_calculator.py` |
| `MCDA_Sales_Comparison/mcda_calculator.py` | `${CLAUDE_PLUGIN_ROOT}/skills/comparable-sales-adjustment-methodology/scripts/mcda_calculator.py` |
| `Location_Overview/location_overview.py` | `${CLAUDE_PLUGIN_ROOT}/skills/right-of-way-expert/scripts/location_overview.py` |
| `Expropriation_Forms/forms_validator.py` | `${CLAUDE_PLUGIN_ROOT}/skills/forms-1-12-completeness-verification/scripts/forms_validator.py` |
| `Reports/` (when used as output dir) | `$CLAUDE_PROJECT_DIR/Reports/` |

Use sed to apply changes per file:

```bash
# Example for one file — repeat for each affected file
sed -i 's|Eff_Rent_Calculator/eff_rent_calculator\.py|${CLAUDE_PLUGIN_ROOT}/skills/effective-rent-analyzer/scripts/eff_rent_calculator.py|g' plugins/leasing-commercial/commands/Financial_Analysis/effective-rent.md
```

For the full set, write a one-shot edit script:

```bash
cat > /tmp/apply-path-edits.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
cd /home/reggiechan/vp-real-estate

declare -A REPLACEMENTS=(
  ["Eff_Rent_Calculator/eff_rent_calculator.py"]='${CLAUDE_PLUGIN_ROOT}/skills/effective-rent-analyzer/scripts/eff_rent_calculator.py'
  ["IFRS16_Calculator/ifrs16_calculator.py"]='${CLAUDE_PLUGIN_ROOT}/skills/effective-rent-analyzer/scripts/ifrs16_calculator.py'
  ["Option_Valuation/option_valuation.py"]='${CLAUDE_PLUGIN_ROOT}/skills/real-options-valuation-expert/scripts/option_valuation.py'
  ["Renewal_Analysis/renewal_analysis.py"]='${CLAUDE_PLUGIN_ROOT}/skills/portfolio-strategy-advisor/scripts/renewal_analysis.py'
  ["Rental_Variance/rental_variance.py"]='${CLAUDE_PLUGIN_ROOT}/skills/lease-comparison-expert/scripts/rental_variance.py'
  ["Rental_Yield_Curve/rental_yield_curve.py"]='${CLAUDE_PLUGIN_ROOT}/skills/portfolio-strategy-advisor/scripts/rental_yield_curve.py'
  ["Rollover_Analysis/rollover_analysis.py"]='${CLAUDE_PLUGIN_ROOT}/skills/portfolio-strategy-advisor/scripts/rollover_analysis.py'
  ["Default_Calculator/default_calculator.py"]='${CLAUDE_PLUGIN_ROOT}/skills/default-and-remedies-advisor/scripts/default_calculator.py'
  ["Credit_Analysis/credit_analysis.py"]='${CLAUDE_PLUGIN_ROOT}/skills/tenant-credit-analyst/scripts/credit_analysis.py'
  ["MLS_Extractor/mls_extractor.py"]='${CLAUDE_PLUGIN_ROOT}/skills/lease-abstraction-specialist/scripts/mls_extractor.py'
  ["Relative_Valuation/relative_valuation.py"]='${CLAUDE_PLUGIN_ROOT}/skills/portfolio-strategy-advisor/scripts/relative_valuation.py'
  ["Comparable_Sales_Analysis/comparable_sales_calculator.py"]='${CLAUDE_PLUGIN_ROOT}/skills/comparable-sales-adjustment-methodology/scripts/comparable_sales_calculator.py'
  ["MCDA_Sales_Comparison/mcda_calculator.py"]='${CLAUDE_PLUGIN_ROOT}/skills/comparable-sales-adjustment-methodology/scripts/mcda_calculator.py'
  ["Location_Overview/location_overview.py"]='${CLAUDE_PLUGIN_ROOT}/skills/right-of-way-expert/scripts/location_overview.py'
  ["Expropriation_Forms/forms_validator.py"]='${CLAUDE_PLUGIN_ROOT}/skills/forms-1-12-completeness-verification/scripts/forms_validator.py'
)

for old in "${!REPLACEMENTS[@]}"; do
  new="${REPLACEMENTS[$old]}"
  old_escaped=$(printf '%s\n' "$old" | sed 's:[][\\/.^$*]:\\&:g')
  new_escaped=$(printf '%s\n' "$new" | sed 's:[\\/&]:\\&:g')
  grep -rl "$old" plugins/*/commands/ 2>/dev/null | while read -r f; do
    sed -i "s|$old_escaped|$new_escaped|g" "$f"
    echo "edited: $f (replaced $old)"
  done
done
EOF
chmod +x /tmp/apply-path-edits.sh
/tmp/apply-path-edits.sh
```

- [ ] **Step 3: Replace `Reports/` output references with `$CLAUDE_PROJECT_DIR/Reports/`**

```bash
grep -rln '\bReports/' plugins/*/commands/ 2>/dev/null | while read -r f; do
  sed -i 's|\([^/]\|^\)Reports/|\1$CLAUDE_PROJECT_DIR/Reports/|g' "$f"
  echo "Reports path updated: $f"
done
```

- [ ] **Step 4: Verify no remaining old-style references**

```bash
grep -rn "Eff_Rent_Calculator\|IFRS16_Calculator\|Option_Valuation\|Renewal_Analysis\|Rental_Variance\|Rental_Yield_Curve\|Rollover_Analysis\|Default_Calculator\|Credit_Analysis\|Comparable_Sales_Analysis\|MCDA_Sales_Comparison\|MLS_Extractor\|Relative_Valuation\|Location_Overview\|Expropriation_Forms" plugins/*/commands/ | grep -v CLAUDE_PLUGIN_ROOT
```
Expected: no output (all references now use `${CLAUDE_PLUGIN_ROOT}`).

- [ ] **Step 5: Commit**

```bash
git add plugins/*/commands/
git commit -m "refactor(commands): convert calculator paths to \${CLAUDE_PLUGIN_ROOT} and \$CLAUDE_PROJECT_DIR/Reports/"
```

---

## Phase 3 — Calculator + Shared_Utils consolidation

### Task 21: Move canonical Shared_Utils into common-utilities

**Files:**
- Move: `Shared_Utils/` → `plugins/common-utilities/shared_utils/`

- [ ] **Step 1: Remove the empty shared_utils placeholder dir created in Phase 0**

```bash
rmdir plugins/common-utilities/shared_utils 2>/dev/null || true
```

- [ ] **Step 2: Move Shared_Utils as canonical**

```bash
git mv Shared_Utils plugins/common-utilities/shared_utils
```

- [ ] **Step 3: Verify**

```bash
ls plugins/common-utilities/shared_utils/
```
Expected: `__init__.py`, `financial_utils.py`, `land_assembly_utils.py`, `negotiation_utils.py`, `report_utils.py`, `risk_utils.py`, `schemas`, `stakeholder_utils.py`, `timeline_utils.py`, `README_FINANCIAL_UTILS.md`.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(common-utilities): relocate canonical Shared_Utils to plugin"
```

---

### Task 22: Move leasing-commercial calculators into their owning skills' scripts/

**Files:** Move 11 calculator folders into 7 skill directories inside `plugins/leasing-commercial/skills/<skill>/scripts/`

| Source folder | Destination |
|---|---|
| `Eff_Rent_Calculator/` | `plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/` |
| `IFRS16_Calculator/` | `plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/` (alongside Eff_Rent) |
| `Option_Valuation/` | `plugins/leasing-commercial/skills/real-options-valuation-expert/scripts/` |
| `Renewal_Analysis/` | `plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/` |
| `Rental_Variance/` | `plugins/leasing-commercial/skills/lease-comparison-expert/scripts/` |
| `Rental_Yield_Curve/` | `plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/` (alongside Renewal_Analysis) |
| `Rollover_Analysis/` | `plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/` (alongside Renewal_Analysis) |
| `Default_Calculator/` | `plugins/leasing-commercial/skills/default-and-remedies-advisor/scripts/` |
| `Credit_Analysis/` | `plugins/leasing-commercial/skills/tenant-credit-analyst/scripts/` |
| `MLS_Extractor/` | `plugins/leasing-commercial/skills/lease-abstraction-specialist/scripts/` |
| `Relative_Valuation/` | `plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/` (alongside others) |

- [ ] **Step 1: Move each calculator folder (using `git mv` to preserve history)**

```bash
mkdir -p plugins/leasing-commercial/skills/effective-rent-analyzer/scripts
mkdir -p plugins/leasing-commercial/skills/real-options-valuation-expert/scripts
mkdir -p plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts
mkdir -p plugins/leasing-commercial/skills/lease-comparison-expert/scripts
mkdir -p plugins/leasing-commercial/skills/default-and-remedies-advisor/scripts
mkdir -p plugins/leasing-commercial/skills/tenant-credit-analyst/scripts
mkdir -p plugins/leasing-commercial/skills/lease-abstraction-specialist/scripts

# Move Eff_Rent_Calculator contents into the effective-rent-analyzer/scripts/ dir
# (use the calculator dir's files at the top level of scripts/, not nested)
git mv Eff_Rent_Calculator/* plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/
rmdir Eff_Rent_Calculator

# Move IFRS16_Calculator alongside
git mv IFRS16_Calculator/* plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/
rmdir IFRS16_Calculator

# Move Option_Valuation
git mv Option_Valuation/* plugins/leasing-commercial/skills/real-options-valuation-expert/scripts/
rmdir Option_Valuation

# Move Renewal_Analysis, Rental_Yield_Curve, Rollover_Analysis, Relative_Valuation into portfolio-strategy-advisor/scripts/
git mv Renewal_Analysis/* plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/
rmdir Renewal_Analysis
git mv Rental_Yield_Curve/* plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/
rmdir Rental_Yield_Curve
git mv Rollover_Analysis/* plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/
rmdir Rollover_Analysis
git mv Relative_Valuation/* plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/
rmdir Relative_Valuation

# Move Rental_Variance
git mv Rental_Variance/* plugins/leasing-commercial/skills/lease-comparison-expert/scripts/
rmdir Rental_Variance

# Move Default_Calculator
git mv Default_Calculator/* plugins/leasing-commercial/skills/default-and-remedies-advisor/scripts/
rmdir Default_Calculator

# Move Credit_Analysis
git mv Credit_Analysis/* plugins/leasing-commercial/skills/tenant-credit-analyst/scripts/
rmdir Credit_Analysis

# Move MLS_Extractor
git mv MLS_Extractor/* plugins/leasing-commercial/skills/lease-abstraction-specialist/scripts/
rmdir MLS_Extractor
```

- [ ] **Step 2: Verify all 11 source folders are gone**

```bash
ls Eff_Rent_Calculator IFRS16_Calculator Option_Valuation Renewal_Analysis Rental_Variance Rental_Yield_Curve Rollover_Analysis Default_Calculator Credit_Analysis MLS_Extractor Relative_Valuation 2>&1
```
Expected: 11 "No such file or directory" errors (confirms all moved).

- [ ] **Step 3: Verify destination structure**

```bash
for skill in effective-rent-analyzer real-options-valuation-expert portfolio-strategy-advisor lease-comparison-expert default-and-remedies-advisor tenant-credit-analyst lease-abstraction-specialist; do
  echo "=== $skill ==="
  ls plugins/leasing-commercial/skills/$skill/scripts/ | head -10
done
```
Expected: each skill's scripts/ dir contains the moved files.

- [ ] **Step 4: Commit**

```bash
git commit -m "feat(leasing-commercial): move 11 calculator folders into skill scripts/ directories"
```

---

### Task 23: Move appraisal-valuation, expropriation, infrastructure calculators

**Files:** Move 4 calculator folders into their respective skills' scripts/

| Source | Destination |
|---|---|
| `Comparable_Sales_Analysis/` | `plugins/appraisal-valuation/skills/comparable-sales-adjustment-methodology/scripts/` |
| `MCDA_Sales_Comparison/` | `plugins/appraisal-valuation/skills/comparable-sales-adjustment-methodology/scripts/` (alongside) |
| `Expropriation_Forms/` | `plugins/expropriation-law/skills/forms-1-12-completeness-verification/scripts/` |
| `Location_Overview/` | `plugins/infrastructure-corridor-ops/skills/right-of-way-expert/scripts/` |

- [ ] **Step 1: Create scripts/ destinations and move**

```bash
mkdir -p plugins/appraisal-valuation/skills/comparable-sales-adjustment-methodology/scripts
mkdir -p plugins/expropriation-law/skills/forms-1-12-completeness-verification/scripts
mkdir -p plugins/infrastructure-corridor-ops/skills/right-of-way-expert/scripts

git mv Comparable_Sales_Analysis/* plugins/appraisal-valuation/skills/comparable-sales-adjustment-methodology/scripts/
rmdir Comparable_Sales_Analysis
git mv MCDA_Sales_Comparison/* plugins/appraisal-valuation/skills/comparable-sales-adjustment-methodology/scripts/
rmdir MCDA_Sales_Comparison

git mv Expropriation_Forms/* plugins/expropriation-law/skills/forms-1-12-completeness-verification/scripts/
rmdir Expropriation_Forms

git mv Location_Overview/* plugins/infrastructure-corridor-ops/skills/right-of-way-expert/scripts/
rmdir Location_Overview
```

- [ ] **Step 2: Verify source folders are gone**

```bash
ls Comparable_Sales_Analysis MCDA_Sales_Comparison Expropriation_Forms Location_Overview 2>&1
```
Expected: 4 "No such file or directory" errors.

- [ ] **Step 3: Commit**

```bash
git commit -m "feat: move appraisal, expropriation, and infrastructure calculators into skill scripts/"
```

---

### Task 24: Move Templates into leasing-commercial

**Files:** `Templates/` → `plugins/leasing-commercial/templates/`

- [ ] **Step 1: Move templates**

```bash
git mv Templates plugins/leasing-commercial/templates
```

- [ ] **Step 2: Verify**

```bash
ls plugins/leasing-commercial/templates/
```
Expected: `Industrial`, `Office` (or whatever subdirs existed).

- [ ] **Step 3: Commit**

```bash
git commit -m "feat(leasing-commercial): move lease templates into plugin"
```

---

### Task 25: Build the Shared_Utils vendor consumer manifest

**Files:**
- Modify: `scripts/shared-utils-vendor-map.json`

- [ ] **Step 1: Identify all Shared_Utils consumers**

```bash
grep -rln 'from Shared_Utils\|import Shared_Utils' plugins/ --include='*.py' 2>/dev/null | grep -v __pycache__ | sort
```
Expected: ~24 files. Record the unique scripts/ directories (the parent of each script that imports Shared_Utils). The vendor map's consumer entries are the `scripts/shared_utils/` paths within each consuming skill.

- [ ] **Step 2: Generate the consumer list**

```bash
grep -rln 'from Shared_Utils\|import Shared_Utils' plugins/ --include='*.py' 2>/dev/null \
  | grep -v __pycache__ \
  | xargs -I{} dirname {} \
  | sort -u \
  | while read -r d; do
      # Walk up to find the skill directory (the one containing SKILL.md)
      cur="$d"
      while [[ "$cur" != "plugins" && "$cur" != "/" ]]; do
        if [[ -f "$cur/SKILL.md" ]]; then
          echo "$cur/scripts/shared_utils"
          break
        fi
        cur=$(dirname "$cur")
      done
    done | sort -u
```
Expected: ~10-15 consumer paths (one per consuming skill that has Shared_Utils-importing code).

- [ ] **Step 3: Write the resulting consumer list into the vendor map**

Use the output from Step 2 to populate `scripts/shared-utils-vendor-map.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "canonical": "plugins/common-utilities/shared_utils",
  "consumers": [
    "plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/shared_utils",
    "plugins/leasing-commercial/skills/tenant-credit-analyst/scripts/shared_utils",
    "plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/shared_utils",
    "plugins/appraisal-valuation/skills/comparable-sales-adjustment-methodology/scripts/shared_utils",
    "plugins/appraisal-valuation/skills/cost-approach-expert/scripts/shared_utils",
    "plugins/appraisal-valuation/skills/income-approach-expert/scripts/shared_utils",
    "plugins/appraisal-valuation/skills/title-expert/scripts/shared_utils",
    "plugins/appraisal-valuation/skills/environmental-due-diligence-expert/scripts/shared_utils",
    "plugins/infrastructure-corridor-ops/skills/right-of-way-expert/scripts/shared_utils",
    "plugins/infrastructure-corridor-ops/skills/stakeholder-management-expert/scripts/shared_utils",
    "plugins/common-utilities/skills/briefing-note-expert/scripts/shared_utils",
    "plugins/common-utilities/skills/negotiation-expert-infrastructure/scripts/shared_utils"
  ]
}
```

NOTE: This list is from the spec's pre-migration estimate. Reconcile against Step 2's actual output and adjust before continuing. If Step 2 produces additional or different consumers, use that authoritative list.

- [ ] **Step 4: Validate JSON**

```bash
jq empty scripts/shared-utils-vendor-map.json && echo OK
```

- [ ] **Step 5: Commit**

```bash
git add scripts/shared-utils-vendor-map.json
git commit -m "feat(scripts): populate shared-utils vendor consumer map"
```

---

### Task 26: Run vendor-shared-utils.sh to populate consumer copies

- [ ] **Step 1: Run vendoring**

```bash
scripts/vendor-shared-utils.sh
```
Expected: one "vendored: ..." line per consumer (matching the list in vendor-map.json).

- [ ] **Step 2: Verify each consumer has a shared_utils/ subdirectory**

```bash
jq -r '.consumers[]' scripts/shared-utils-vendor-map.json | while read -r path; do
  if [[ -f "$path/financial_utils.py" ]]; then
    echo "OK: $path"
  else
    echo "MISSING: $path"
  fi
done
```
Expected: all "OK" lines.

- [ ] **Step 3: Run check mode to confirm no drift**

```bash
scripts/vendor-shared-utils.sh --check
```
Expected: "All vendored copies match canonical."

- [ ] **Step 4: Commit vendored copies**

```bash
git add plugins/*/skills/*/scripts/shared_utils/
git commit -m "feat: vendor Shared_Utils into all consuming plugin skills"
```

---

### Task 27: Rewrite Python imports from Shared_Utils to shared_utils

**Files:** All `.py` files under `plugins/` that import `Shared_Utils.*`

- [ ] **Step 1: Inventory remaining imports**

```bash
grep -rln 'from Shared_Utils\|import Shared_Utils' plugins/ --include='*.py' 2>/dev/null | grep -v __pycache__
```
Expected: same files as before vendoring (vendoring didn't change the importing files).

- [ ] **Step 2: Apply search-and-replace across all consuming Python files**

```bash
grep -rln 'from Shared_Utils\|import Shared_Utils' plugins/ --include='*.py' 2>/dev/null \
  | grep -v __pycache__ \
  | while read -r f; do
      sed -i \
        -e 's|from Shared_Utils\.|from shared_utils.|g' \
        -e 's|from Shared_Utils import|from shared_utils import|g' \
        -e 's|import Shared_Utils|import shared_utils|g' \
        "$f"
      echo "rewrote imports in: $f"
    done
```

- [ ] **Step 3: Verify no Shared_Utils references remain**

```bash
grep -rn 'Shared_Utils' plugins/ --include='*.py' 2>/dev/null | grep -v __pycache__ | grep -v 'shared_utils'
```
Expected: no output (case-sensitive grep finds no remaining capitalized Shared_Utils).

- [ ] **Step 4: Commit**

```bash
git add plugins/*/skills/
git commit -m "refactor: rewrite Shared_Utils imports to lowercase shared_utils across all consuming scripts"
```

---

### Task 28: Smoke test calculator imports

Verify the import refactor didn't break anything before continuing. Run one Python import per consumer to confirm.

- [ ] **Step 1: Test effective-rent-analyzer imports**

```bash
cd plugins/leasing-commercial/skills/effective-rent-analyzer/scripts
python3 -c "from shared_utils.financial_utils import npv; print('OK: npv loaded from', npv.__module__)"
cd -
```
Expected: `OK: npv loaded from shared_utils.financial_utils` (or whatever submodule npv lives in).

- [ ] **Step 2: Test 3 more consumers**

```bash
for path in \
  plugins/leasing-commercial/skills/tenant-credit-analyst/scripts \
  plugins/appraisal-valuation/skills/comparable-sales-adjustment-methodology/scripts \
  plugins/expropriation-law/skills/forms-1-12-completeness-verification/scripts; do
  if [[ -d "$path/shared_utils" ]]; then
    (cd "$path" && python3 -c "import shared_utils; print('OK: $path')") || echo "FAIL: $path"
  fi
done
```
Expected: 3 OK lines (or the forms validator may not import shared_utils — that's fine, only checks where vendored).

- [ ] **Step 3: Run any preserved test suites in scripts/Tests/ dirs**

```bash
for tests_dir in plugins/*/skills/*/scripts/Tests; do
  if [[ -d "$tests_dir" ]]; then
    echo "=== Running tests in $tests_dir ==="
    cd "$tests_dir/.."
    python3 -m pytest Tests/ -v --tb=short 2>&1 | tail -20
    cd - > /dev/null
  fi
done
```
Expected: tests pass. If any fail, fix the import path or vendor map issue before continuing.

NOTE: If pytest is not installed, install with `pip install pytest`. If tests have non-import bugs (pre-existing), document and skip — note in the migration log.

---

## Phase 4 — Specialist sub-agents migration

### Task 29: Move 7 specialist agent files to their plugins

**Files:** Move `.claude/agents/<agent>.md` for non-trio agents.

| Agent | Destination plugin |
|---|---|
| `alexi.md` | `plugins/appraisal-valuation/agents/` |
| `anni.md` | `plugins/tenancies-residential/agents/` |
| `benji.md` | `plugins/leasing-commercial/agents/` |
| `christi.md` | `plugins/expropriation-law/agents/` |
| `katy.md` | `plugins/infrastructure-corridor-ops/agents/` |
| `shadi.md` | `plugins/infrastructure-corridor-ops/agents/` |
| `stevi.md` | `plugins/expropriation-law/agents/` |

- [ ] **Step 1: Remove .gitkeep from agents/ dirs and move specialists**

```bash
rm -f plugins/*/agents/.gitkeep
git mv .claude/agents/alexi.md plugins/appraisal-valuation/agents/alexi.md
git mv .claude/agents/anni.md plugins/tenancies-residential/agents/anni.md
git mv .claude/agents/benji.md plugins/leasing-commercial/agents/benji.md
git mv .claude/agents/christi.md plugins/expropriation-law/agents/christi.md
git mv .claude/agents/katy.md plugins/infrastructure-corridor-ops/agents/katy.md
git mv .claude/agents/shadi.md plugins/infrastructure-corridor-ops/agents/shadi.md
git mv .claude/agents/stevi.md plugins/expropriation-law/agents/stevi.md
```

- [ ] **Step 2: Verify**

```bash
ls .claude/agents/
```
Expected: only the three trio files remain (`adam.md`, `dennis.md`, `reggie-chan-vp.md`).

- [ ] **Step 3: Commit**

```bash
git commit -m "feat: migrate 7 specialist sub-agents into their domain plugins"
```

---

### Task 30: Port subagent-stop.sh to common-utilities with updated filter

**Files:**
- Move: `.claude/hooks/subagent-stop.sh` → `plugins/common-utilities/hooks/subagent-stop.sh`
- Create: `plugins/common-utilities/hooks/hooks.json`

- [ ] **Step 1: Move the hook script**

```bash
git mv .claude/hooks/subagent-stop.sh plugins/common-utilities/hooks/subagent-stop.sh
```

- [ ] **Step 2: Update the agent ID filter list (trio removed, specialists added)**

Edit `plugins/common-utilities/hooks/subagent-stop.sh` and replace the agent-id check block (currently `[[ "$AGENT_ID" == "adam" ]] || [[ "$AGENT_ID" == "reggie-chan-vp" ]] || [[ "$AGENT_ID" == "dennis" ]]`) with the seven specialist IDs:

```bash
# Check if it's one of the specialist sub-agents
if [[ "$AGENT_ID" == "alexi" ]] || \
   [[ "$AGENT_ID" == "anni" ]] || \
   [[ "$AGENT_ID" == "benji" ]] || \
   [[ "$AGENT_ID" == "christi" ]] || \
   [[ "$AGENT_ID" == "katy" ]] || \
   [[ "$AGENT_ID" == "shadi" ]] || \
   [[ "$AGENT_ID" == "stevi" ]]; then
```

The label inside the banner output should also change. Find the line `echo "📋 ${AGENT_ID^^} COMPLETE RESPONSE:"` — this stays as-is (uses `${AGENT_ID^^}` which uppercases whichever agent fired).

- [ ] **Step 3: Write `plugins/common-utilities/hooks/hooks.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "SubagentStop": [
    {
      "hooks": [
        {
          "type": "command",
          "command": "${CLAUDE_PLUGIN_ROOT}/hooks/subagent-stop.sh"
        }
      ]
    }
  ]
}
```

- [ ] **Step 4: Validate JSON**

```bash
jq empty plugins/common-utilities/hooks/hooks.json && echo OK
```

- [ ] **Step 5: Confirm script is executable**

```bash
chmod +x plugins/common-utilities/hooks/subagent-stop.sh
ls -l plugins/common-utilities/hooks/subagent-stop.sh
```
Expected: `-rwxr-xr-x ...`.

- [ ] **Step 6: Commit**

```bash
git add plugins/common-utilities/hooks/
git commit -m "feat(common-utilities): port subagent-stop hook with specialist filter list"
```

---

## Phase 5 — Trio dual-format setup

### Task 31: Author the three persona master files

**Files:**
- Create: `plugins/common-utilities/personas/dennis.md`
- Create: `plugins/common-utilities/personas/reggie.md`
- Create: `plugins/common-utilities/personas/adam.md`

Source content from the existing `.claude/agents/{dennis,reggie-chan-vp,adam}.md` files. Strip the agent-specific frontmatter (`name:`, `tools:`, `model:`) and keep the persona/voice body. Add the `description:` (and optional `voice:`) frontmatter the build script expects.

- [ ] **Step 1: Author `plugins/common-utilities/personas/dennis.md`**

Read the body content from `.claude/agents/dennis.md` (everything below the closing `---` of the agent frontmatter). Compose:

```markdown
---
description: Strategic advisor — 36+ years institutional real estate. Wisdom, not task execution.
voice: blunt, battle-tested, direct
---

You are Dennis, a seasoned real estate executive with 36+ years of institutional experience. Your role is strategic counsel, not task execution. You don't write code, build features, or analyze financials — you provide wisdom on big decisions, people management, negotiation psychology, and long-term consequences.

## Voice

- **Direct and blunt.** No political filtering. Say what you think is true.
- **Battle-tested perspective.** You've seen multiple market cycles, recessions, team dynamics, and human nature.
- **Focus on decisions, not analysis.** When users ask "should I?", give clear wisdom based on experience.
- **Emphasize human factors.** Real estate is 70% psychology, 30% spreadsheets. Never let financials override people sense.

## When to engage

You speak when users ask:
- Strategic career decisions
- Negotiation psychology and power dynamics
- People management and team building
- Work-life balance reality checks
- Long-term consequences of decisions

## When to refer elsewhere

- Detailed lease analysis → recommend the user consult Reggie
- Fast routine analyst work → recommend Adam
- Valuation or expropriation → recommend Alexi
- Compliance tracking → recommend Stevi

## Your philosophy

"Real estate is 30% spreadsheets and 70% human psychology, politics, and hard choices. The fundamentals always give you the right answer. Think things through. Make decisions as if it were your own money. And remember: Father Time is undefeated."
```

If the existing `.claude/agents/dennis.md` contains additional persona content beyond what's reproduced above, preserve it by appending to the body section.

- [ ] **Step 2: Author `plugins/common-utilities/personas/reggie.md`**

```markdown
---
description: VP of Leasing and Asset Management — CFA, FRICS, 20+ years institutional real estate. Crisis specialist, deep technical expertise.
voice: technically rigorous, brutally honest, systematic
---

You are Reggie Chan, CFA, FRICS — Vice President of Leasing and Asset Management with over 20 years of institutional commercial real estate experience.

## Credentials

- **CFA** (Chartered Financial Analyst) — investment analysis and financial modeling
- **FRICS** (Fellow of the Royal Institution of Chartered Surveyors) — senior real estate valuation
- **VP of Leasing and Asset Management** — executive-level commercial real estate
- **RICS Licensed Assessor** since 2012 — qualified to judge professional competence

## When to engage

You handle:
- Complex/distressed situations requiring deep expertise
- Fraud detection or forensic accounting
- Crisis turnarounds with compressed timelines
- Non-standard lease structures requiring framework building
- Situations needing exhaustive documentation
- Whenever someone needs you to challenge everything

## What you provide

- Domain synthesis (leasing + accounting + legal + asset management)
- Forensic mindset (follows the money, detects fraud)
- Systematic frameworks (builds comprehensive systems)
- Zero neuroticism (handles extreme pressure matter-of-factly)
- Brutal honesty (no political filtering)

## Voice

- Direct and technically precise
- No softening of bad news
- Challenge assumptions; demand evidence
- Build systematic frameworks; resist one-off thinking
- Trust the math; verify the inputs

## When to refer elsewhere

- Strategic/career/people questions → Dennis
- Fast routine work that doesn't need crisis mode → Adam
- Specialist legal or valuation work → the domain expert (Benji/Christi/Alexi)
```

- [ ] **Step 3: Author `plugins/common-utilities/personas/adam.md`**

```markdown
---
description: Senior Analyst trained by Reggie Chan. Fast execution for standard work with institutional rigor.
voice: diplomatic, efficient, politically aware
---

You are Adam, a Senior Analyst trained by Reggie Chan to handle straightforward tasks with institutional-grade rigor at exceptional speed.

## When to engage

You handle:
- Standard lease evaluations (typical terms, normal tenants)
- Routine tenant credit checks (clear financials, no fraud concerns)
- Renewal offer assessments (clear market conditions)
- Simple deal comparisons (straightforward tradeoffs)
- Professional communication to stakeholders

## What you provide

- Fast execution (80/20 analysis)
- Reggie's analytical methods applied to day-to-day work
- Diplomatic delivery (politically aware communication)
- Quantified analysis without over-engineering

## Voice

- Concise and practical
- Politically aware — softens delivery without softening substance
- Dry wit
- Defer to Reggie for complex problems, to Dennis for strategic questions

## Your role

You execute Reggie's methods on routine work so Reggie can focus on complex problems. You're the everyday analyst who gets things done fast.

## When to refer elsewhere

- Complex crisis or fraud → Reggie
- Strategic/career decisions → Dennis
- Specialist domains → the domain expert
```

- [ ] **Step 4: Verify the three masters exist**

```bash
ls plugins/common-utilities/personas/
```
Expected: `adam.md`, `dennis.md`, `reggie.md`.

- [ ] **Step 5: Commit masters**

```bash
git add plugins/common-utilities/personas/
git commit -m "feat(common-utilities): author trio persona master files (Dennis, Reggie, Adam)"
```

---

### Task 32: Generate output-styles and skill artifacts from masters

- [ ] **Step 1: Remove the placeholder output-styles dir from Phase 0**

```bash
rmdir plugins/common-utilities/output-styles 2>/dev/null || true
```

- [ ] **Step 2: Run the build script**

```bash
scripts/build-personas.sh
```
Expected: 6 "generated: ..." lines (2 per persona — output-style + skill SKILL.md).

- [ ] **Step 3: Verify artifact tree**

```bash
ls plugins/common-utilities/output-styles/
ls plugins/common-utilities/skills/ | grep -E '^(dennis-advisor|reggie-vp|adam-analyst)$'
cat plugins/common-utilities/skills/dennis-advisor/SKILL.md | head -10
cat plugins/common-utilities/output-styles/dennis.md | head -10
```
Expected: output-styles/ has 3 .md files; skills/ has 3 new persona-skill directories; SKILL.md and output-style files have correct frontmatter.

- [ ] **Step 4: Run check mode to confirm no drift**

```bash
scripts/build-personas.sh --check
```
Expected: `All generated persona artifacts match masters.`

- [ ] **Step 5: Commit generated artifacts**

```bash
git add plugins/common-utilities/output-styles/ plugins/common-utilities/skills/dennis-advisor plugins/common-utilities/skills/reggie-vp plugins/common-utilities/skills/adam-analyst
git commit -m "feat(common-utilities): generate trio output styles and skill artifacts from masters"
```

---

### Task 33: Delete the old trio agent files

The trio is no longer sub-agents — the old `.claude/agents/{adam,dennis,reggie-chan-vp}.md` files should be removed.

- [ ] **Step 1: Delete the trio agent files**

```bash
git rm .claude/agents/adam.md .claude/agents/dennis.md .claude/agents/reggie-chan-vp.md
```

- [ ] **Step 2: Verify `.claude/agents/` is empty**

```bash
ls .claude/agents/
```
Expected: empty listing.

- [ ] **Step 3: Commit**

```bash
git commit -m "feat: remove trio sub-agents (now distributed as output styles + skills)"
```

---

## Phase 6 — Hook system retirement

### Task 34: Delete custom skill-activation hooks

**Files:** Delete the entire `.claude/hooks/` directory (subagent-stop.sh was already moved to common-utilities in Phase 4; remaining contents are the skill-activation engine + tooling).

- [ ] **Step 1: Confirm subagent-stop.sh is already moved**

```bash
ls .claude/hooks/subagent-stop.sh 2>&1
```
Expected: "No such file or directory" (moved in Task 30).

- [ ] **Step 2: Inventory what remains to be deleted**

```bash
ls .claude/hooks/
```
Expected: `README.md`, `generate-skill-rules.js`, `lease-types-map.json`, `node_modules/`, `package-lock.json`, `package.json`, `pre-tool-use-skill-loader.sh`, `pre-tool-use-skill-loader.ts`, `skill-activation-prompt.sh`, `skill-activation-prompt.ts`, `skill-rules.json`.

- [ ] **Step 3: Delete the hooks directory**

```bash
git rm -rf .claude/hooks/
```

- [ ] **Step 4: Commit**

```bash
git commit -m "feat: retire custom skill-activation hooks (native discovery replaces them)"
```

---

### Task 35: Clear hook references from .claude/settings.json

**Files:**
- Modify: `.claude/settings.json`

- [ ] **Step 1: Read current settings.json**

```bash
cat .claude/settings.json
```
Expected: contains a `hooks` block with UserPromptSubmit, PreToolUse, SubagentStop entries.

- [ ] **Step 2: Remove the hooks block entirely**

Replace the entire file with:

```json
{}
```

(The settings.json file becomes effectively empty. The whole `.claude/` directory will be deleted in Phase 7; this intermediate step keeps it tidy.)

- [ ] **Step 3: Commit**

```bash
git add .claude/settings.json
git commit -m "feat: clear hook registrations from .claude/settings.json"
```

---

## Phase 7 — Repo cleanup

### Task 36: Delete the .claude directory entirely

**Files:** Delete `.claude/` (commands, skills, agents, hooks all migrated; settings.json contents cleared)

- [ ] **Step 1: Verify .claude/ is empty of migrated content**

```bash
find .claude/ -type f
```
Expected: only `.claude/settings.json` remains (containing `{}`).

- [ ] **Step 2: Remove the directory**

```bash
git rm -rf .claude/
```

- [ ] **Step 3: Verify**

```bash
ls .claude 2>&1
```
Expected: "No such file or directory".

- [ ] **Step 4: Commit**

```bash
git commit -m "feat: remove .claude/ directory (all contents migrated to plugins)"
```

---

### Task 37: Verify and prune any stale top-level dirs

**Files:** Check that all calculator-source folders are gone. Top-level dirs that must remain: `Reports/`, `Sample_Inputs/`, `Sample_Outputs/`, `Planning/`, `Research_Reports/`, `Specifications/`, `Repository_Dev_Plans/`, `User_Inputs/`, `Images/`, `docs/`, `Issues_Reports/`.

- [ ] **Step 1: List top-level directories**

```bash
ls -d */
```
Expected: 11 directories: `Images/`, `Issues_Reports/`, `Planning/`, `Reports/`, `Repository_Dev_Plans/`, `Research_Reports/`, `Sample_Inputs/`, `Sample_Outputs/`, `Specifications/`, `User_Inputs/`, `docs/`, plus `plugins/` and `scripts/`. NO `Eff_Rent_Calculator/`, `IFRS16_Calculator/`, `Shared_Utils/`, `Templates/`, etc.

- [ ] **Step 2: If any old calculator dir remains, delete it**

```bash
for dir in Eff_Rent_Calculator IFRS16_Calculator Option_Valuation Renewal_Analysis Rental_Variance Rental_Yield_Curve Rollover_Analysis Default_Calculator Credit_Analysis Comparable_Sales_Analysis MCDA_Sales_Comparison MLS_Extractor Relative_Valuation Location_Overview Expropriation_Forms Shared_Utils Templates; do
  if [[ -d "$dir" ]]; then
    git rm -rf "$dir"
    echo "removed stale: $dir"
  fi
done
```
Expected: no output (all were removed during Phase 3 moves).

- [ ] **Step 3: Commit if anything was removed**

```bash
if ! git diff --cached --quiet; then
  git commit -m "feat: prune stale top-level calculator folders"
fi
```

---

## Phase 8 — Documentation updates

### Task 38: Update README.md to describe the plugin marketplace

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Read existing README.md to identify sections to update**

```bash
head -50 README.md
grep -n '^#\|^##' README.md | head -30
```
Record the section structure.

- [ ] **Step 2: Replace the install/structure sections**

Replace the section currently describing the `.claude/commands` and calculator folders with a new "Installation" section near the top:

```markdown
## Installation

This repository is a Claude Code plugin marketplace. To install:

```bash
# Add the marketplace
/plugin marketplace add reggiechan/vp-real-estate

# Install the plugins you need
/plugin install leasing-commercial@vp-real-estate
/plugin install common-utilities@vp-real-estate    # foundation plugin — recommended

# Optional plugins for specialized domains
/plugin install tenancies-residential@vp-real-estate
/plugin install expropriation-law@vp-real-estate
/plugin install appraisal-valuation@vp-real-estate
/plugin install infrastructure-corridor-ops@vp-real-estate
```

## Plugins

| Plugin | Purpose |
|---|---|
| **common-utilities** | Foundation: trio personas (Adam/Reggie/Dennis), shared utilities, cross-cutting skills |
| **leasing-commercial** | Commercial lease analysis: abstraction, effective rent, tenant credit, options, IFRS 16, consents, compliance |
| **tenancies-residential** | Ontario RTA: eviction procedures, LTB hearings |
| **expropriation-law** | Ontario Expropriations Act: compensation, forms, deadlines, settlement |
| **appraisal-valuation** | Cost approach, income approach, easement valuation, comparable sales, environmental DD |
| **infrastructure-corridor-ops** | Linear infrastructure acquisition: easements, land assembly, public consultation, transit, transmission |

Use `Edit` tool to make this replacement precisely. Identify the existing section by its header and replace through to the next major heading.

- [ ] **Step 3: Update the "Quick Start Examples" section**

The current section shows usage like `/abstract-lease path/to/lease.docx`. Update to plugin-namespaced form:

```markdown
## Quick Start Examples

```bash
# Lease abstraction (after installing leasing-commercial)
/leasing-commercial:abstract-lease path/to/lease.docx

# Financial analysis
/leasing-commercial:effective-rent path/to/lease.pdf
/leasing-commercial:tenant-credit path/to/financials.pdf

# IFRS 16 accounting
/leasing-commercial:ifrs16-calculation path/to/lease.pdf 5.5

# Adopt a persona for the session (after installing common-utilities)
# Run /config -> select Output Style -> pick "Dennis Advisory"

# Or invoke a persona by name in the current session
# Just say: "Dennis, what do you think about this acquisition?"
```

Identify the existing Quick Start section by its header, replace through to the next major heading.

- [ ] **Step 4: Commit README updates**

```bash
git add README.md
git commit -m "docs: rewrite README.md for plugin marketplace v3.0.0"
```

---

### Task 39: Update CLAUDE.md to describe new layout

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Replace the "Structure" section**

Identify the section that begins with `## Structure` and the tree diagram of the old `.claude/commands/` + calculator folders. Replace the tree with:

```markdown
## Structure

```
vp-real-estate/                                    # plugin marketplace root
├── .claude-plugin/marketplace.json                # marketplace manifest
├── plugins/
│   ├── leasing-commercial/                        # 24 skills, 5 command subdirs, 1 agent (benji)
│   ├── tenancies-residential/                     # 3 skills, 1 agent (anni)
│   ├── expropriation-law/                         # 9 skills, 2 agents (christi, stevi)
│   ├── appraisal-valuation/                       # 6 skills, 1 agent (alexi)
│   ├── infrastructure-corridor-ops/               # 10 skills, 2 agents (katy, shadi)
│   └── common-utilities/                          # 4 skills, 3 persona skills, 3 output styles, canonical Shared_Utils, hook
├── scripts/                                       # vendor-shared-utils.sh, build-personas.sh, sync-all.sh
├── docs/superpowers/specs/                        # design specs
├── docs/superpowers/plans/                        # implementation plans
├── Reports/                                       # user-generated outputs
├── Sample_Inputs/, Sample_Outputs/                # documentation samples
└── README.md, CLAUDE.md, etc.
```
```

- [ ] **Step 2: Replace the "Meet Your Team: The Triumvirate" section to describe dual format**

Find the section heading `## Meet Your Team: The Triumvirate` and rewrite as follows (substitute into the file via the Edit tool):

```markdown
## Meet Your Team: The Triumvirate

The trio (Adam, Reggie, Dennis) is available in two formats via the `common-utilities` plugin:

### Session-level persona via output styles

For deep immersion in one persona for an entire session:

```bash
/config → Output style → pick "Dennis Advisory" / "Reggie Chan VP" / "Adam Analyst"
```

The selected persona's voice and worldview shape the entire session. They remember everything from turn 1. Persists across session restarts via `.claude/settings.local.json`.

### In-conversation invocation via skills

For quick consultation while in a different output style:

> "Adam, sanity-check this calculation."
> "Reggie, what am I missing in this lease?"
> "Dennis, should I take this acquisition?"

The corresponding skill (`adam-analyst`, `reggie-vp`, `dennis-advisor`) auto-loads via native skill discovery and shapes that response. Useful when you're in a coding session but want one quick consultation without switching modes.

### Specialists are sub-agents

The domain specialists remain as Claude Code sub-agents (Task tool, fresh context per invocation):

- **alexi** (appraisal-valuation) — Expropriation appraisal expert, AACI
- **anni** (tenancies-residential) — Ontario RTA specialist
- **benji** (leasing-commercial) — Commercial Tenancies Act specialist
- **christi** (expropriation-law) — Expropriation law specialist
- **katy** (infrastructure-corridor-ops) — Transit corridor specialist
- **shadi** (infrastructure-corridor-ops) — Utility transmission corridor specialist
- **stevi** (expropriation-law) — Compliance enforcer & deadline watchdog

Specialists are dispatch-oriented: they receive a focused task, return a written brief, and don't carry state between invocations. The `SubagentStop` hook in `common-utilities` ensures their full transcripts surface without main-thread re-summarization.
```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: rewrite CLAUDE.md Structure and Triumvirate sections for plugin layout"
```

---

### Task 40: Update CHANGELOG.md with v3.0.0 entry

**Files:**
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Add v3.0.0 entry at the top of CHANGELOG.md**

Insert immediately after the title line (or at the very top if no title):

```markdown
## [3.0.0] — 2026-05-15

### BREAKING — Conversion to Claude Code plugin marketplace

The entire repository has been restructured as a Claude Code plugin marketplace. The legacy `.claude/commands/` and `.claude/skills/` layout has been removed and replaced with six installable plugins under `plugins/`. Users must now install plugins via `/plugin marketplace add reggiechan/vp-real-estate` followed by `/plugin install <plugin-name>@vp-real-estate`. See README.md for full instructions.

### Added

- Plugin marketplace at `.claude-plugin/marketplace.json` listing six plugins
- `plugins/common-utilities/` foundation plugin: 4 cross-cutting skills, 3 generated persona skills (Adam/Reggie/Dennis), 3 output styles, canonical Shared_Utils, subagent-stop hook
- `plugins/leasing-commercial/` (24 skills, 5 command subdirs, 11 calculator scripts bundled, agent: benji)
- `plugins/tenancies-residential/` (3 RTA skills, agent: anni)
- `plugins/expropriation-law/` (9 skills, 2 command subdirs, 1 calculator bundled, agents: christi, stevi)
- `plugins/appraisal-valuation/` (6 valuation skills, 2 command subdirs, 2 calculators bundled, agent: alexi)
- `plugins/infrastructure-corridor-ops/` (10 skills, 4 command subdirs, 1 calculator bundled, agents: katy, shadi)
- `scripts/vendor-shared-utils.sh` — syncs canonical Shared_Utils into consuming plugins
- `scripts/build-personas.sh` — generates output styles + skill artifacts from `personas/` masters
- `scripts/sync-all.sh` — wrapper for both sync scripts

### Changed

- Slash commands are now namespaced under their plugin (`/leasing-commercial:effective-rent`, etc.)
- Calculator paths now use `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<script>` instead of top-level folders
- Python imports converted from `Shared_Utils.*` to lowercase `shared_utils.*`
- Output files now write to `$CLAUDE_PROJECT_DIR/Reports/` instead of repo-relative `Reports/`
- Analyst trio (Adam/Reggie/Dennis) reimplemented as output styles + skills instead of sub-agents — solves the "fresh persona every invocation" problem

### Removed

- `.claude/` directory in its entirety
- Top-level calculator folders: Eff_Rent_Calculator, IFRS16_Calculator, Option_Valuation, Renewal_Analysis, Rental_Variance, Rental_Yield_Curve, Rollover_Analysis, Default_Calculator, Credit_Analysis, Comparable_Sales_Analysis, MCDA_Sales_Comparison, MLS_Extractor, Relative_Valuation, Location_Overview, Expropriation_Forms
- Top-level `Shared_Utils/` (now canonical at `plugins/common-utilities/shared_utils/`)
- Top-level `Templates/` (now at `plugins/leasing-commercial/templates/`)
- Custom skill-activation hook system (`pre-tool-use-skill-loader.{sh,ts}`, `skill-activation-prompt.{sh,ts}`, `generate-skill-rules.js`, `skill-rules.json`, `lease-types-map.json`) — replaced by native Claude Code skill auto-discovery
```

- [ ] **Step 2: Commit**

```bash
git add CHANGELOG.md
git commit -m "docs(changelog): add v3.0.0 entry for plugin marketplace conversion"
```

---

### Task 41: Update VERSION file

**Files:**
- Modify: `VERSION`

- [ ] **Step 1: Set version to 3.0.0**

```bash
echo "3.0.0" > VERSION
cat VERSION
```
Expected: `3.0.0`.

- [ ] **Step 2: Commit**

```bash
git add VERSION
git commit -m "chore: bump VERSION to 3.0.0"
```

---

### Task 42: Write migration notes for future-you

**Files:**
- Create: `docs/MIGRATION_v3.md`

- [ ] **Step 1: Write `docs/MIGRATION_v3.md`**

```markdown
# Migration to v3.0.0 — Plugin Marketplace Conversion

**Date:** 2026-05-15

## What changed

This repository was converted from a legacy `.claude/commands/` + `.claude/skills/` layout into a Claude Code plugin marketplace. The conversion was driven by:

1. **Distributability** — users can now install only the plugins they need (a residential tenancies lawyer doesn't need expropriation infrastructure)
2. **Modularity** — each domain is independently versioned and updatable
3. **Native skill discovery** — Claude Code's official mechanism replaces the custom skill-activation hook system

## Repository structure (after)

- `.claude-plugin/marketplace.json` — marketplace manifest listing six plugins
- `plugins/<name>/` — six self-contained plugins, each with its own skills, commands, agents, calculators
- `scripts/vendor-shared-utils.sh` — sync canonical Shared_Utils into consumer plugins
- `scripts/build-personas.sh` — generate trio output styles + skills from masters in `plugins/common-utilities/personas/`
- `scripts/sync-all.sh` — runs both

## How to install plugins for development

```bash
# In a sibling test directory
claude --plugin-dir /home/reggiechan/vp-real-estate/plugins/leasing-commercial
```

## How users install

```bash
/plugin marketplace add reggiechan/vp-real-estate
/plugin install <plugin-name>@vp-real-estate
```

## Editing personas (trio)

1. Edit master file at `plugins/common-utilities/personas/<dennis|reggie|adam>.md`
2. Run `scripts/build-personas.sh` to regenerate output-style + skill artifacts
3. Commit both master and generated files

## Editing Shared_Utils

1. Edit canonical at `plugins/common-utilities/shared_utils/<file>.py`
2. Run `scripts/vendor-shared-utils.sh` to sync into consumer plugins
3. Commit canonical + all vendored copies

## Pre-commit hygiene

Before committing changes that touch Shared_Utils or persona masters, run:

```bash
scripts/sync-all.sh
git add -A
git commit -m "..."
```

If you want a CI guard, run:

```bash
scripts/sync-all.sh --check
```

This fails if any generated/vendored artifact drifted from its master/canonical.

## Pre-existing top-level dirs preserved

- `Reports/` — user output dir (commands write here via `$CLAUDE_PROJECT_DIR/Reports/`)
- `Sample_Inputs/`, `Sample_Outputs/` — documentation examples
- `Planning/`, `Research_Reports/`, `Specifications/`, `Repository_Dev_Plans/`, `User_Inputs/`, `Images/`, `Issues_Reports/` — repo-level docs

## What was deleted

- Entire `.claude/` directory
- Top-level calculator folders (now bundled inside owning plugin's skill `scripts/` dirs)
- Top-level `Shared_Utils/` (now at `plugins/common-utilities/shared_utils/`)
- Top-level `Templates/` (now at `plugins/leasing-commercial/templates/`)
- Custom skill-activation hooks (replaced by native discovery)
```

- [ ] **Step 2: Commit**

```bash
git add docs/MIGRATION_v3.md
git commit -m "docs: add MIGRATION_v3 notes for plugin marketplace conversion"
```

---

### Task 43: Update README-FOR-LEASING-MANAGERS.md

**Files:**
- Modify: `README-FOR-LEASING-MANAGERS.md`

- [ ] **Step 1: Identify and update install instructions**

```bash
grep -n 'git clone\|cd vp-real-estate\|/abstract-lease\|/effective-rent' README-FOR-LEASING-MANAGERS.md | head -20
```
Record lines that show old-style commands.

- [ ] **Step 2: Add a "Installation via Plugin" section near the top**

Find the appropriate location (likely after the title/intro, before the first usage example) and insert:

```markdown
## Installation

The fastest way to use these tools is via the Claude Code plugin marketplace:

```bash
/plugin marketplace add reggiechan/vp-real-estate
/plugin install leasing-commercial@vp-real-estate
/plugin install common-utilities@vp-real-estate
```

Then invoke commands with the plugin namespace, e.g. `/leasing-commercial:abstract-lease path/to/lease.pdf`.

If you prefer to clone the repo directly for development, see CLAUDE.md.
```

- [ ] **Step 3: Update usage examples that show un-namespaced commands**

Search for `/abstract-lease`, `/effective-rent`, etc. and prefix with `leasing-commercial:`:

```bash
sed -i \
  -e 's|/abstract-lease |/leasing-commercial:abstract-lease |g' \
  -e 's|/effective-rent |/leasing-commercial:effective-rent |g' \
  -e 's|/tenant-credit |/leasing-commercial:tenant-credit |g' \
  -e 's|/ifrs16-calculation |/leasing-commercial:ifrs16-calculation |g' \
  -e 's|/renewal-economics |/leasing-commercial:renewal-economics |g' \
  -e 's|/option-value |/leasing-commercial:option-value |g' \
  README-FOR-LEASING-MANAGERS.md
```

- [ ] **Step 4: Commit**

```bash
git add README-FOR-LEASING-MANAGERS.md
git commit -m "docs(leasing-managers): update install instructions and command namespaces for v3.0.0"
```

---

## Phase 9 — Local install validation

### Task 44: Validate marketplace manifest loads

- [ ] **Step 1: Verify marketplace.json is well-formed**

```bash
jq -e '.plugins | length == 6' .claude-plugin/marketplace.json && echo "marketplace lists 6 plugins"
jq -r '.plugins[].name' .claude-plugin/marketplace.json
```
Expected: "marketplace lists 6 plugins" and the six plugin names.

- [ ] **Step 2: Verify all plugin sources resolve**

```bash
jq -r '.plugins[] | .name + " " + .source' .claude-plugin/marketplace.json | while read -r name path; do
  if [[ -f "$path/.claude-plugin/plugin.json" ]]; then
    echo "OK: $name -> $path"
  else
    echo "MISSING: $name -> $path/.claude-plugin/plugin.json"
  fi
done
```
Expected: 6 OK lines.

---

### Task 45: Test plugin loading for each of six plugins

For each plugin, install locally via `claude --plugin-dir` and smoke test at least one capability.

- [ ] **Step 1: Test common-utilities loads**

```bash
cd /tmp && mkdir -p plugin-test-common && cd plugin-test-common
claude --plugin-dir /home/reggiechan/vp-real-estate/plugins/common-utilities --help 2>&1 | head -20
cd -
```
Expected: claude launches without manifest errors.

- [ ] **Step 2: Test leasing-commercial loads**

```bash
cd /tmp && mkdir -p plugin-test-leasing && cd plugin-test-leasing
claude --plugin-dir /home/reggiechan/vp-real-estate/plugins/leasing-commercial --help 2>&1 | head -20
cd -
```
Expected: no manifest parse errors.

- [ ] **Step 3-6: Test remaining four plugins similarly**

```bash
for p in tenancies-residential expropriation-law appraisal-valuation infrastructure-corridor-ops; do
  echo "=== Testing $p ==="
  cd /tmp && mkdir -p plugin-test-$p && cd plugin-test-$p
  claude --plugin-dir /home/reggiechan/vp-real-estate/plugins/$p --help 2>&1 | head -5
  cd -
done
```
Expected: each plugin loads without manifest errors.

---

### Task 46: Test ${CLAUDE_PLUGIN_ROOT} resolution in commands

The slash commands reference `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<script>`. Confirm Claude Code resolves this correctly.

- [ ] **Step 1: Inspect a representative command file**

```bash
cat plugins/leasing-commercial/commands/Financial_Analysis/effective-rent.md | head -30
```
Verify it references `${CLAUDE_PLUGIN_ROOT}/skills/effective-rent-analyzer/scripts/eff_rent_calculator.py` (or similar).

- [ ] **Step 2: Test by invoking the command in a Claude Code session with the plugin loaded**

In a separate Claude Code terminal:

```bash
cd /tmp/plugin-test-leasing
claude --plugin-dir /home/reggiechan/vp-real-estate/plugins/leasing-commercial
# Inside Claude Code:
# /leasing-commercial:effective-rent /home/reggiechan/vp-real-estate/Sample_Inputs/<some_sample_lease.json>
```

Verify the command resolves the script path and runs the calculator. If the calculator imports work and produce output, the path resolution is correct.

NOTE: This is an interactive test. If you cannot run an interactive Claude Code session as part of the plan, mark this as a manual verification step and continue.

---

### Task 47: Verify sync scripts pass --check mode

- [ ] **Step 1: Run sync-all.sh --check**

```bash
cd /home/reggiechan/vp-real-estate
scripts/sync-all.sh --check
```
Expected: "All vendored copies match canonical." AND "All generated persona artifacts match masters."

---

### Task 48: Verify output styles appear in /config picker

- [ ] **Step 1: Confirm 3 output style files exist**

```bash
ls plugins/common-utilities/output-styles/
```
Expected: `adam.md`, `dennis.md`, `reggie.md`.

- [ ] **Step 2: Confirm frontmatter is correct**

```bash
head -5 plugins/common-utilities/output-styles/dennis.md
```
Expected:
```
---
name: Dennis Advisory
description: Strategic advisor — 36+ years institutional real estate. Wisdom, not task execution.
keep-coding-instructions: false
---
```

- [ ] **Step 3: Manual verification**

In a Claude Code session with `common-utilities` loaded, run `/config` → Output style → verify "Dennis Advisory", "Reggie Chan VP", "Adam Analyst" appear in the picker. Select one and confirm the session adopts that persona's voice.

---

### Task 49: Verify subagent-stop hook fires for specialists

- [ ] **Step 1: Confirm hook is registered**

```bash
cat plugins/common-utilities/hooks/hooks.json
```
Expected: SubagentStop block referencing `${CLAUDE_PLUGIN_ROOT}/hooks/subagent-stop.sh`.

- [ ] **Step 2: Confirm filter list contains specialists, not trio**

```bash
grep 'AGENT_ID ==' plugins/common-utilities/hooks/subagent-stop.sh
```
Expected: lines referencing alexi, anni, benji, christi, katy, shadi, stevi (not adam, dennis, reggie-chan-vp).

- [ ] **Step 3: Manual verification (interactive)**

In a Claude Code session with `expropriation-law` and `common-utilities` loaded, invoke the `christi` sub-agent on a test task. Verify the `📋 CHRISTI COMPLETE RESPONSE:` banner appears at end of sub-agent completion.

---

### Task 50: Run all preserved calculator test suites end-to-end

- [ ] **Step 1: Run each scripts/Tests/ directory**

```bash
for tests_dir in plugins/*/skills/*/scripts/Tests; do
  if [[ -d "$tests_dir" ]]; then
    scripts_dir=$(dirname "$tests_dir")
    echo "=== $scripts_dir ==="
    (cd "$scripts_dir" && python3 -m pytest Tests/ --tb=short 2>&1) | tail -10
  fi
done
```
Expected: tests pass. Document any failures and address before PR.

---

## Phase 10 — PR, merge, tag

### Task 51: Verify branch is ready for merge

- [ ] **Step 1: Verify working tree is clean**

```bash
git status
```
Expected: `nothing to commit, working tree clean` on `feat/plugin-marketplace`.

- [ ] **Step 2: Verify all phases committed**

```bash
git log main..HEAD --oneline | wc -l
git log main..HEAD --oneline | head -30
```
Expected: ~40+ commits spanning the 10 phases.

- [ ] **Step 3: Verify diff summary makes sense**

```bash
git diff main --stat | tail -20
```
Expected: many files moved (rename detection should be high), `.claude/` deleted, `plugins/` added, scripts added, docs updated.

---

### Task 52: Open pull request

- [ ] **Step 1: Push the branch**

```bash
git push -u origin feat/plugin-marketplace
```

- [ ] **Step 2: Create PR using gh**

```bash
gh pr create --title "v3.0.0: convert repo to plugin marketplace" --body "$(cat <<'EOF'
## Summary

Converts the repository from the legacy `.claude/commands/` + `.claude/skills/` layout into a Claude Code plugin marketplace hosting six installable plugins.

- **Six plugins** under `plugins/`: leasing-commercial, tenancies-residential, expropriation-law, appraisal-valuation, infrastructure-corridor-ops, common-utilities
- **All ~25 calculator folders** bundled into their owning skill's `scripts/` directory; paths resolved via `${CLAUDE_PLUGIN_ROOT}`
- **Shared_Utils vendored** per consuming plugin via `scripts/vendor-shared-utils.sh` from canonical at `plugins/common-utilities/shared_utils/`
- **Trio personas** (Adam/Reggie/Dennis) reimplemented as output styles + skills generated from `personas/` masters via `scripts/build-personas.sh` — solves the "fresh Dennis every invocation" problem
- **Specialist sub-agents** (Alexi/Anni/Benji/Christi/Katy/Shadi/Stevi) distributed to their owning plugins
- **Custom skill-activation hooks retired** (~1k lines deleted); `subagent-stop.sh` ported to `common-utilities` with updated filter list
- **Hard cutover**: `.claude/` directory deleted entirely

See `docs/superpowers/specs/2026-05-15-plugin-marketplace-design.md` for the full design and `docs/MIGRATION_v3.md` for upgrade notes.

## Breaking changes

- Slash commands are namespaced: `/abstract-lease` → `/leasing-commercial:abstract-lease`
- Users must reinstall via `/plugin marketplace add reggiechan/vp-real-estate` + `/plugin install <plugin>@vp-real-estate`
- Python imports: `Shared_Utils.*` → `shared_utils.*`
- Output paths: `Reports/` → `$CLAUDE_PROJECT_DIR/Reports/`

## Test plan

- [ ] Each of six plugins loads via `claude --plugin-dir`
- [ ] `${CLAUDE_PLUGIN_ROOT}` resolves correctly in slash command path references
- [ ] Vendored Shared_Utils imports successfully from at least 4 consumer skills
- [ ] All preserved calculator test suites (`scripts/Tests/`) pass
- [ ] `sync-all.sh --check` passes (no vendor or persona drift)
- [ ] Output styles (Dennis Advisory, Reggie Chan VP, Adam Analyst) appear in `/config` picker
- [ ] Persona skill invocation ("Adam, ...") loads correct skill via native discovery
- [ ] SubagentStop hook banner fires when specialist sub-agent completes

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

- [ ] **Step 3: Capture PR URL**

The output of `gh pr create` includes the PR URL. Record it for the user.

---

### Task 53: Merge and tag v3.0.0 (manual review gate)

This step requires user approval to merge. Once approved:

- [ ] **Step 1: After PR review and approval, merge**

```bash
gh pr merge feat/plugin-marketplace --squash --delete-branch
```

- [ ] **Step 2: Pull main and tag**

```bash
git checkout main
git pull origin main
git tag -a v3.0.0 -m "v3.0.0: Plugin marketplace conversion"
git push origin v3.0.0
```

- [ ] **Step 3: Verify tag**

```bash
git tag | grep v3.0.0
```
Expected: `v3.0.0`.

---

## Self-Review

After writing this plan, here is the consistency check against the spec:

**Spec coverage:**
- [x] Marketplace topology — Tasks 1-4
- [x] Plugin partitioning (24/3/9/6/10/4 skills) — Tasks 9-14
- [x] Command migration with namespacing — Tasks 15-20
- [x] Calculator + Shared_Utils consolidation — Tasks 21-28
- [x] Specialist sub-agent migration — Task 29
- [x] subagent-stop.sh port with updated filter — Task 30
- [x] Trio persona masters + dual format generation — Tasks 31-33
- [x] Custom skill-activation hook retirement — Tasks 34-35
- [x] Repo cleanup — Tasks 36-37
- [x] Documentation updates (README, CLAUDE.md, CHANGELOG, VERSION, MIGRATION_v3, README-FOR-LEASING-MANAGERS) — Tasks 38-43
- [x] Local install validation across six plugins — Tasks 44-50
- [x] PR + merge + tag — Tasks 51-53

**Type/naming consistency:**
- `${CLAUDE_PLUGIN_ROOT}` used uniformly (not `$CLAUDE_PLUGIN_ROOT` without braces) throughout commands and hooks.json
- `$CLAUDE_PROJECT_DIR` used uniformly for user outputs
- `shared_utils` (lowercase) used consistently for Python imports; `Shared_Utils` (capitalized) appears only in pre-migration grep patterns and is removed in Task 27
- Skill names match the partitioning table from the spec

**Known assumptions documented in spec:**
- Agent namespacing inside plugins — verified in Task 49 (manual)
- `${CLAUDE_PLUGIN_ROOT}` resolution in hooks — verified in Task 46
- Output style auto-discovery — verified in Task 48
- Cross-plugin dependency resolution — verified during installation; documented in README

**Risks called out:**
- Phase 3 (calculator + Shared_Utils) is the time risk; Task 28 smoke tests are the early-warning system
- Task 25 Step 3 notes that the vendor map list is initial-estimate and Step 2 must reconcile against actual grep output before continuing
- Tasks 46, 48, 49 involve interactive verification that cannot be fully automated; flagged in task body
