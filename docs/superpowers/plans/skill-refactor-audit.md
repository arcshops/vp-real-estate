# Skill Refactor Audit — 2026-05-15

Audit of all 59 SKILL.md files across 6 plugins against current Claude Code SKILL.md spec, CSO standards, and post-marketplace consistency.

## Verdict roll-up

| Plugin | OK | MINOR | NEEDS_REWORK | Total |
|---|---|---|---|---|
| appraisal-valuation | 0 | 0 | 6 | 6 |
| common-utilities | 0 | 3 | 4 | 7 |
| expropriation-law | 0 | 0 | 9 | 9 |
| infrastructure-corridor-ops | 0 | 1 | 9 | 10 |
| leasing-commercial | 0 | 7 | 17 | 24 |
| tenancies-residential | 0 | 0 | 3 | 3 |
| **TOTAL** | **0** | **11** | **48** | **59** |

## Systemic findings

### 1. Obsolete frontmatter fields (56/59 skills)
Every "expert" skill carries `tags`, `capability`, `proactive: true`. Current spec accepts only `name` and `description`. `capability` duplicates `description` and pushes `comparable-sales-adjustment-methodology` and `cost-approach-expert` over the 1024-char cap.

### 2. Persona skills missing `name` field (3 skills)
`adam-analyst`, `dennis-advisor`, `reggie-vp` have only `description` in frontmatter.

### 3. Obsolete `tools:` field (2 skills)
`common-utilities/negotiation-expert` and `leasing-commercial/objection-handling-expert` carry an agent-style `tools:` line.

### 4. Descriptions describe instead of trigger (59/59 skills)
Zero descriptions lead with "Use when...". Dominant pattern: `Expert in <topic>. Use when <buried trigger>. Key terms include <keyword dump>.`

### 5. Body boilerplate (most skills)
- Opening `You are an expert in...` narrative
- `## Granular Focus` "subset of X's capabilities" meta-scaffold
- Closing `This skill activates when you:` block duplicating description

## Cluster findings

### Body bloat (token efficiency)
| Skill | Words | Note |
|---|---|---|
| `right-of-way-expert` | 6,719 | Absorbed 3 workflows — structural issue |
| `environmental-due-diligence-expert` | 5,793 | Extract cost tables |
| `lease-surrender-expert` | 5,544 | Outlier vs ~2k peer baseline |
| `easement-valuation-methods` | 4,909 | Move v2.1 changelog out of body |
| `title-expert` | 4,805 | |
| `cost-approach-expert` | 4,781 | Frontmatter over cap |
| `income-approach-expert` | 4,523 | |
| `share-transfer-consent-expert` | 4,521 | |
| `cropland-out-of-production-agreements` | 4,083 | Case studies → reference files |

### Stale references
- `common-utilities/negotiation-expert` — slash commands without `/leasing-commercial:` namespace
- `expropriation-law/expropriation-timeline-expert` — references `.claude/skills/...` path; should be `plugins/expropriation-law/skills/...`
- `infrastructure-corridor-ops/land-assembly-expert` — "Related Skills" cross-plugin links to verify
- `infrastructure-corridor-ops/stakeholder-management-expert` — stale `Version`, `Author`, `Future Enhancements` sections

### Content issues
- `tenancies-residential/residential-tenancies-act-eviction-procedures` — s.57 cap is $35K, not "$25K+"
- `leasing-commercial/lease-abstraction-specialist` — body says "24 sections", DDD reference says "25 sections"
- `expropriation-law/injurious-affection-assessment` ↔ `severance-damages-quantification` — substantive overlap on partial-taking valuation
- `infrastructure-corridor-ops/right-of-way-expert` — 3 stacked workflows, no decision-table routing

### Merge integrations status
- ✅ `commercial-lease-expert` ← `/recommendation-memo` — clean
- ✅ `lease-abstraction-specialist` ← `lease_abstraction_ddd.md` — clean
- ✅ `cropland-out-of-production-agreements` ← `/cropland-compensation-analysis` — clean
- ⚠️ `right-of-way-expert` ← `/location-overview` — scope blurred, needs decision-table or re-split

## Refactor passes

### Pass 1 — Frontmatter cleanup (mechanical)
- Strip `tags`, `capability`, `proactive` from 56 files
- Strip `tools:` from 2 files
- Add `name:` to 3 persona skills

### Pass 2 — Description rewrites (per-skill judgment)
Rewrite 59 descriptions to lead with "Use when..." third-person, ≤500 chars, with concrete triggers.

### Pass 3 — Body boilerplate sweep
- Remove "You are an expert in..." openers
- Remove "Granular Focus / subset of X's capabilities" meta-scaffold
- Remove trailing "This skill activates when you:" duplicate blocks
- Remove "Version History", "Author", "Future Enhancements" sections (infra-corridor-ops)

### Pass 4 — Content/structural fixes (deferred)
- Fix $25K→$35K cap in RTA-eviction
- Reconcile 24 vs 25 sections in lease-abstraction-specialist
- Update stale path in expropriation-timeline-expert
- Update un-namespaced slash-command refs in negotiation-expert
- Decide on right-of-way-expert split or decision-table
- Decide on injurious-affection ↔ severance-damages overlap
- Trim bloated skills

## Execution log

- 2026-05-15: Audit complete. Passes 1+2+3 executed in parallel (6 plugin agents). Pass 4 surgical fixes done (section count, scope-boundary cross-refs, right-of-way dedup). Pass 4 body trim done (9 parallel agents). 11 residual Granular Focus blocks the Pass 3 agents missed were swept in a follow-up.

Commits on `feat/plugin-marketplace`:
- `e2b7a29` — Pass 1+2+3: align all 59 SKILL.md files with current spec
- `0e32c2f` — Pass 4 surgical: reconcile cross-references, dedup duplicated content
- `96465ca` — Pass 4 trim: 9 bloated skills extracted to sibling reference files

Final state: 59 spec-compliant SKILL.md files; 9 trimmed to 1,500-1,900 words with ~28 new sibling reference files carrying the deep content. All four obsolete frontmatter fields (`tags`, `capability`, `proactive`, `tools`) are gone; all descriptions lead with "Use when..."; no residual Granular Focus blocks.
