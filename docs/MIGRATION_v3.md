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
- `Research_Reports/`, `Specifications/`, `Repository_Dev_Plans/`, `User_Inputs/`, `Images/`, `Issues_Reports/` — repo-level docs

## What was deleted

- Entire `.claude/` directory
- Top-level calculator folders (now bundled inside owning plugin's skill `scripts/` dirs)
- Top-level `Shared_Utils/` (now at `plugins/common-utilities/shared_utils/`)
- Top-level `Templates/` (now at `plugins/leasing-commercial/templates/`)
- Custom skill-activation hooks (replaced by native discovery)

## Calculator subdirectory layout

Each calculator preserved its original folder name when migrating into a skill's `scripts/` directory. E.g., `Eff_Rent_Calculator/` files are now at `plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/Eff_Rent_Calculator/`. This was a pragmatic choice during Phase 3 migration to avoid filename collisions (multiple calculators had `README.md`, `__init__.py`, `Tests/` etc.).

Command markdown files reference these paths via `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<Calculator_Subdir>/<file>`.
