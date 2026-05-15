# Plugin Marketplace Design — vp-real-estate v3.0.0

**Date:** 2026-05-15
**Author:** Reggie Chan (with Claude Code brainstorming)
**Status:** Approved by user; pending implementation plan
**Target release:** v3.0.0 (breaking change)

## Purpose

Convert the `vp-real-estate` repository from a legacy `.claude/commands/` + `.claude/skills/` layout into an official Claude Code plugin marketplace hosting six installable plugins. The migration consolidates ~25 top-level calculator/script folders with their corresponding skills, replaces the custom skill-activation hook system with native skill auto-discovery, and reorganizes the analyst trio (Adam/Reggie/Dennis) from ephemeral sub-agents into persistent personas via dual-format output styles and skills.

## Goals

- Conform to Claude Code's official plugin and marketplace specification (`code.claude.com/docs/en/plugins.md`, `plugins-reference.md`, `plugin-marketplaces.md`)
- Enable selective installation: a residential tenancies practitioner can install just `tenancies-residential` without dragging in expropriation infrastructure
- Solve the "fresh Dennis every time" problem — the trio becomes session-persistent rather than ephemeral
- Retire ~1,000 lines of custom hook infrastructure now redundant with native skill discovery
- Bundle calculator scripts with the skills that drive them, using `${CLAUDE_PLUGIN_ROOT}` for path resolution

## Non-goals

- Publishing to a public plugin registry (when/if Anthropic launches one)
- Per-plugin CI/CD pipelines
- Backwards compatibility with the legacy `.claude/` layout (hard cutover, by user decision)
- New skills, commands, or calculators during migration (feature freeze on main during the migration window)
- Republishing `Shared_Utils` as a PyPI package (deferred; vendoring is preferred for solo-maintained, slow-evolving utilities consumed by non-developer users)

---

## Architecture

### Repository topology

Monorepo: marketplace manifest plus all six plugins live in this single repository, matching the `obra/superpowers-marketplace` pattern.

```
vp-real-estate/
├── .claude-plugin/
│   └── marketplace.json                # marketplace manifest
├── plugins/
│   ├── leasing-commercial/
│   ├── tenancies-residential/
│   ├── expropriation-law/
│   ├── appraisal-valuation/
│   ├── infrastructure-corridor-ops/
│   └── common-utilities/
├── scripts/
│   ├── vendor-shared-utils.sh          # syncs canonical Shared_Utils into consumer plugins
│   ├── shared-utils-vendor-map.json    # consumer manifest
│   ├── build-personas.sh               # generates output-styles + skills from persona masters
│   └── sync-all.sh                     # convenience wrapper for both
├── docs/superpowers/specs/             # design docs (this file)
├── Reports/                            # user-generated outputs (not part of any plugin)
├── Sample_Inputs/, Sample_Outputs/     # documentation samples (stay top-level)
├── Planning/, Research_Reports/, Specifications/, Repository_Dev_Plans/, User_Inputs/, Images/
├── README.md, CLAUDE.md, CHANGELOG.md, LICENSE, VERSION, requirements.txt, FAQ.md
└── .gitignore
```

User installation flow:

```bash
/plugin marketplace add reggiechan/vp-real-estate
/plugin install leasing-commercial@vp-real-estate
/plugin install common-utilities@vp-real-estate    # auto-prompted as dependency
```

### Plugin partitioning

| Plugin | Skills | Agents (sub-agents) | Commands | Bundled calculators |
|---|---|---|---|---|
| **leasing-commercial** | 24: commercial-lease-expert, lease-abstraction-specialist, effective-rent-analyzer, tenant-credit-analyst, lease-compliance-auditor, default-and-remedies-advisor, lease-comparison-expert, portfolio-strategy-advisor, real-options-valuation-expert, indemnity-expert, non-disturbance-expert, consent-to-assignment-expert, consent-to-sublease-expert, share-transfer-consent-expert, lease-surrender-expert, offer-to-lease-expert, waiver-agreement-expert, temporary-license-expert, storage-agreement-expert, telecom-licensing-expert, lease-arbitration-expert, objection-handling-expert, commercial-lease-assignment-consent-framework, commercial-tenancies-act-enforcement-remedies | benji | Abstraction/*, Accounting/ifrs16-calculation, Comparison/*, Compliance/*, Financial_Analysis/* | Eff_Rent_Calculator, IFRS16_Calculator, Option_Valuation, Renewal_Analysis, Rental_Variance, Rental_Yield_Curve, Rollover_Analysis, Default_Calculator, Credit_Analysis, Relative_Valuation, MLS_Extractor, Templates/ |
| **tenancies-residential** | 3: residential-tenancies-act-eviction-procedures, ltb-application-hearing-procedures, tenant-relief-from-eviction-analysis | anni | (none yet) | — |
| **expropriation-law** | 9: ontario-expropriations-act-statutory-interpretation, expropriation-compensation-entitlement-analysis, expropriation-procedural-defect-analysis, expropriation-statutory-deadline-tracking, expropriation-timeline-expert, forms-1-12-completeness-verification, settlement-analysis-expert, severance-damages-quantification, injurious-affection-assessment | christi, stevi | Expropriation/*, Process/expropriation-timeline, Process/settlement-analysis | Expropriation_Forms |
| **appraisal-valuation** | 6: cost-approach-expert, easement-valuation-methods, income-approach-expert, comparable-sales-adjustment-methodology, title-expert, environmental-due-diligence-expert | alexi | Valuation/*, Specialized/cost-approach-infrastructure, Specialized/environmental-due-diligence, Specialized/income-approach-land, Specialized/title-analysis | Comparable_Sales_Analysis, MCDA_Sales_Comparison |
| **infrastructure-corridor-ops** | 10: agricultural-easement-negotiation-frameworks, cropland-out-of-production-agreements, land-assembly-expert, public-consultation-process-design, nimby-objection-analysis-response, residential-displacement-mitigation-protocols, right-of-way-expert, stakeholder-management-expert, transit-station-site-acquisition-strategy, transmission-line-technical-specifications | katy, shadi | Infrastructure/*, Transit/*, Specialized/utility-conflict-analysis, Process/public-consultation-summary | Location_Overview |
| **common-utilities** | 4: negotiation-expert, negotiation-expert-infrastructure, board-memo-expert, briefing-note-expert — plus 3 generated trio skills (dennis-advisor, reggie-vp, adam-analyst) | (none — trio is not sub-agents) | Utilities/*, Process/board-memo, Process/briefing-note, Process/negotiation-strategy | Shared_Utils canonical source |

Skill totals: 24 + 3 + 9 + 6 + 10 + 4 = 56 hand-authored skills (matches current `.claude/skills/` inventory). The trio's 3 generated SKILL.md files (dennis-advisor, reggie-vp, adam-analyst) in `common-utilities/skills/` are build artifacts derived from `personas/` masters, so the marketplace surfaces 59 skills total post-migration but only 56 are source-of-truth.

### Calculator and Shared_Utils strategy

Each calculator folder moves into its owning skill's `scripts/` subdirectory inside the plugin:

```
plugins/leasing-commercial/skills/effective-rent-analyzer/
├── SKILL.md
├── reference.md
└── scripts/
    ├── eff_rent_calculator.py
    ├── shared_utils/                    # vendored copy of canonical
    │   ├── __init__.py
    │   ├── financial_utils.py
    │   └── ...
    ├── baf_input_example.json
    ├── landlord_investment_parameters_schema.json
    ├── Tests/
    └── README.md
```

Path resolution in slash commands uses `${CLAUDE_PLUGIN_ROOT}` for plugin-relative references and `$CLAUDE_PROJECT_DIR` for user outputs:

```
${CLAUDE_PLUGIN_ROOT}/skills/effective-rent-analyzer/scripts/eff_rent_calculator.py
$CLAUDE_PROJECT_DIR/Reports/2026-05-15_143022_lease_abstract.md
```

Python imports become local to the vendored copy:

```python
# Before (relied on PYTHONPATH=repo root)
from Shared_Utils.financial_utils import npv, irr

# After (vendored)
from shared_utils.financial_utils import npv, irr
```

**Vendoring workflow.** Canonical `Shared_Utils` lives at `plugins/common-utilities/shared_utils/`. The `scripts/vendor-shared-utils.sh` script reads `scripts/shared-utils-vendor-map.json` (listing consumer skills) and rsync-copies the canonical directory into each consumer's `scripts/shared_utils/`. A `--check` mode runs in CI to fail on drift.

**Consumer manifest sketch:**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "canonical": "plugins/common-utilities/shared_utils",
  "consumers": [
    "plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/shared_utils",
    "plugins/leasing-commercial/skills/tenant-credit-analyst/scripts/shared_utils",
    "plugins/appraisal-valuation/skills/comparable-sales-adjustment-methodology/scripts/shared_utils",
    "plugins/expropriation-law/skills/settlement-analysis-expert/scripts/shared_utils"
  ]
}
```

The exact consumer list is finalized during Phase 3 of migration after running `grep -r 'from Shared_Utils' plugins/` against the migrated tree.

### Sub-agents (specialists)

Seven domain specialists remain as sub-agents in their owning plugins. Each is a single markdown file with persona/instructions, no shared infrastructure.

```
plugins/leasing-commercial/agents/benji.md
plugins/tenancies-residential/agents/anni.md
plugins/expropriation-law/agents/{christi,stevi}.md
plugins/appraisal-valuation/agents/alexi.md
plugins/infrastructure-corridor-ops/agents/{katy,shadi}.md
```

Specialists are dispatch-oriented: they receive a focused task (legal opinion, appraisal, deadline check) and return a written brief. Ephemeral context is appropriate for this usage pattern.

### Trio personas (Adam, Reggie, Dennis)

The trio is not implemented as sub-agents. Sub-agents spawn ephemeral context windows, meaning each invocation creates a fresh persona with no memory of prior conversation — incompatible with the trio's intended role as relational colleagues (Adam = your analyst, Reggie = your VP, Dennis = your strategic advisor).

The trio ships in dual format:

- **Output style** — for session-level immersion. User runs `/config` → picks an output style → entire session is configured with that persona's system prompt. Persists across sessions via `.claude/settings.local.json`'s `outputStyle` field.
- **Skill** — for in-conversation invocation. While the user is in a different output style, addressing "Dennis, ..." auto-loads the skill, which injects the persona into the main context for that turn and forward.

Both formats are generated from a single master file per persona by `scripts/build-personas.sh`.

```
plugins/common-utilities/
├── personas/                            # SOURCE OF TRUTH
│   ├── dennis.md
│   ├── reggie.md
│   └── adam.md
├── output-styles/                       # GENERATED — do not hand-edit
│   ├── dennis.md
│   ├── reggie.md
│   └── adam.md
└── skills/                              # GENERATED — do not hand-edit (for trio dirs)
    ├── dennis-advisor/SKILL.md
    ├── reggie-vp/SKILL.md
    └── adam-analyst/SKILL.md
```

Master file shape:

```markdown
---
description: Strategic advisor — 36+ years institutional real estate. Wisdom, not task execution.
voice: blunt, battle-tested, direct
---

You are Dennis, a seasoned real estate executive...

## Voice
- Direct and blunt. No political filtering.
...
```

The build script reads each master and writes two artifacts with format-specific frontmatter prepended:

- `output-styles/dennis.md` — adds `name: Dennis Advisory`, copies `description:`, adds `keep-coding-instructions: false`
- `skills/dennis-advisor/SKILL.md` — copies `description:` only (skills tolerate other fields but minimal frontmatter avoids future strictness)

CI runs `scripts/build-personas.sh --check` to fail on drift between master and generated outputs.

### Hook system

The legacy custom hooks at `.claude/hooks/` are retired:

- `skill-activation-prompt.{sh,ts}` — DELETE. Native skill auto-discovery via `description:` frontmatter replaces it.
- `pre-tool-use-skill-loader.{sh,ts}` — DELETE. Same reason; native discovery handles document-type-triggered skill loading.
- `generate-skill-rules.js` + `skill-rules.json` + `lease-types-map.json` — DELETE. Auto-generated artifacts no longer needed.
- `node_modules/`, `package.json`, `package-lock.json` — DELETE.
- `subagent-stop.sh` — **KEEP**, moved to `plugins/common-utilities/hooks/subagent-stop.sh`. Filter list updates from `adam|reggie-chan-vp|dennis` to the seven specialist agent names. Registered via `plugins/common-utilities/hooks/hooks.json`:

```json
{
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

The `hooks` block in `.claude/settings.json` is fully removed (becomes empty file, then deleted along with the rest of `.claude/`).

### Manifest examples

**`.claude-plugin/marketplace.json`:**

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

**`plugins/leasing-commercial/.claude-plugin/plugin.json` (representative):**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "name": "leasing-commercial",
  "version": "1.0.0",
  "description": "Commercial lease analysis toolkit (industrial + office)",
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

**`plugins/common-utilities/.claude-plugin/plugin.json`:**

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

Versioning: all six plugins ship at v1.0.0 at cutover (they are new artifacts; plugins did not exist before this migration). Bump rules: MAJOR for breaking input-schema or interface changes, MINOR for new skills/commands/agents, PATCH for bug fixes. The marketplace manifest's own `version` field tracks the repo's release lineage (v3.0.0 at cutover, reflecting that this is the third major repository iteration after the original calculator-folder layout and the v2.x `.claude/`-based layout). The top-level `VERSION` file becomes the marketplace version (3.0.0).

---

## Migration sequencing (hard cutover)

Single feature branch `feat/plugin-marketplace` off `main`. One PR. Total estimated effort 6–7 working days; Phase 3 is the time risk.

| Phase | Description | Effort |
|---|---|---|
| 0 | Branch + scaffolding (manifests, empty plugin dirs, sync scripts) | ½ day |
| 1 | Skills migration (`git mv` 56 skills into owning plugins) | 1 day |
| 2 | Commands migration (move 13 subdirs, update path references to `${CLAUDE_PLUGIN_ROOT}` and `$CLAUDE_PROJECT_DIR`) | ½ day |
| 3 | Calculator + Shared_Utils consolidation (move ~25 folders into skill scripts/, vendor Shared_Utils, fix Python imports, run existing tests) | 2 days |
| 4 | Specialist sub-agents migration (move 7 agent files, update subagent-stop.sh filter, port hook to common-utilities) | ½ day |
| 5 | Trio dual-format setup (author 3 personas/ masters, write build-personas.sh, generate artifacts) | 1 day |
| 6 | Hook system retirement (delete skill-activation hooks, clear settings.json hook blocks) | ¼ day |
| 7 | Repo cleanup (delete `.claude/`, top-level calculator folders, Shared_Utils, Templates) | ½ day |
| 8 | Documentation updates (README, CLAUDE.md, MIGRATION_v3.md, CHANGELOG) | ½ day |
| 9 | Local install validation (smoke test all 6 plugins via `claude --plugin-dir`) | 1 day |
| 10 | PR, merge, tag v3.0.0 | ¼ day |

### Files preserved at repo root post-migration

`Reports/`, `Sample_Inputs/`, `Sample_Outputs/`, `Planning/`, `Research_Reports/`, `Specifications/`, `Repository_Dev_Plans/`, `User_Inputs/`, `Images/`, `docs/`, `README.md`, `README-FOR-LEASING-MANAGERS.md`, `CLAUDE.md`, `CHANGELOG.md`, `LICENSE`, `VERSION`, `requirements.txt`, `FAQ.md`, `IMPLEMENTATION_GUIDE.md`, `LINEAR_INFRASTRUCTURE.md`, `OEA_COMPLIANCE.md`, `Staff_Meeting.md`, `WHY-I-BUILT-THIS.md`, `readme_style.css`, `.gitignore`.

### Files deleted at repo root post-migration

`.claude/` (entire tree), `Comparable_Sales_Analysis/`, `Credit_Analysis/`, `Default_Calculator/`, `Eff_Rent_Calculator/`, `Expropriation_Forms/`, `IFRS16_Calculator/`, `Location_Overview/`, `MCDA_Sales_Comparison/`, `MLS_Extractor/`, `Option_Valuation/`, `Relative_Valuation/`, `Renewal_Analysis/`, `Rental_Variance/`, `Rental_Yield_Curve/`, `Rollover_Analysis/`, `Shared_Utils/`, `Templates/`.

### Rollback plan

`main` is untouched until merge. If post-merge smoke testing reveals breakage:
1. Revert the merge commit on `main`
2. Re-open the PR for fixes
3. Users who installed the marketplace before revert see plugins disappear on next `/plugin marketplace update` — no data loss (their `Reports/` and `User_Inputs/` are in their project directory, not in plugin caches)

### Verification checklist (Phase 9)

For each of six plugins:
- [ ] `claude --plugin-dir ./plugins/<name>` loads without manifest errors
- [ ] At least one slash command invokes successfully and produces expected output
- [ ] At least one skill auto-discovers when relevant keywords appear
- [ ] Calculator script resolves paths via `${CLAUDE_PLUGIN_ROOT}` and imports `shared_utils.*` successfully
- [ ] `vendor-shared-utils.sh --check` passes
- [ ] `build-personas.sh --check` passes
- [ ] Existing calculator tests pass (Eff_Rent_Calculator/Tests, MCDA validation, etc.)
- [ ] For common-utilities: `/config` lists Dennis/Reggie/Adam output styles; selecting one persists across session restart
- [ ] For common-utilities: SubagentStop hook fires when a specialist sub-agent completes

---

## Open questions and assumptions

1. **Agent namespacing inside plugins.** Skills get namespaced as `/<plugin>:<skill>` when shipped via plugins. Whether sub-agents get similarly namespaced when invoked via the Task tool (e.g., `subagent_type: "leasing-commercial:benji"` vs just `"benji"`) is not explicitly covered in the docs. Verified during Phase 9; if namespacing applies, the plan adds a one-time search-replace across slash commands that reference agents.

2. **Plugin install behavior for hooks.** The docs confirm `${CLAUDE_PLUGIN_ROOT}` resolves correctly for hook scripts inside installed plugins. Behavior verified during Phase 9 smoke test.

3. **Output style auto-discovery.** Plugin-shipped output styles appear in `/config` picker. Whether they require explicit `force-for-plugin` or are picked up by enumeration is verified during Phase 9. Default is no `force-for-plugin` (user opt-in).

4. **Cross-plugin dependency resolution.** Domain plugins declare `common-utilities` as a dependency via `plugin.json`. When a user installs `leasing-commercial`, Claude Code should prompt to also install `common-utilities`. Exact prompt UX verified during Phase 9; documented in README install instructions.

5. **Vendored Shared_Utils consumers.** Final consumer list determined by `grep -r 'from Shared_Utils' plugins/` during Phase 3. Pre-migration estimate is 6 calculators across 4 plugins; actual count may differ.

---

## Out of scope (deferred to future work)

- Publishing to a public plugin registry once Anthropic launches one
- Per-plugin GitHub Actions CI/CD
- Automated version bump tooling
- Republishing `Shared_Utils` as a true pip-installable package (the vendoring approach is sufficient for current scale and audience; revisit if `Shared_Utils` grows beyond ~200KB or gains external consumers)
- Adding new skills, commands, or calculators during the migration window (post-merge work)
- Adding output-style variants for the seven domain specialists (current scope is trio only)
- Splitting plugins out into separate repositories (topology is hybrid-ready — marketplace.json supports both relative and GitHub `source` fields, so individual plugins can extract later if they grow enough to justify it)
