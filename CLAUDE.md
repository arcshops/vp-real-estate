# CLAUDE.md

Commercial real estate lease analysis toolkit: abstraction, financial analysis, and rental yield curves.

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
│   └── common-utilities/                          # 4 skills + 3 persona skills, 3 output styles, canonical shared_utils, subagent-stop hook
├── scripts/                                       # vendor-shared-utils.sh, build-personas.sh, sync-all.sh
├── docs/superpowers/specs/                        # design specs
├── docs/superpowers/plans/                        # implementation plans
├── Reports/                                       # user-generated outputs
├── Sample_Inputs/, Sample_Outputs/                # documentation samples
└── README.md, CLAUDE.md, etc.
```

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

## File Naming: Reports Folder

**CRITICAL**: All files in `Reports/` MUST use timestamp prefix:

**Format**: `YYYY-MM-DD_HHMMSS_[filename].md` (Eastern Time)

**Example**: `2025-10-31_143022_lease_abstract_acme_corp.md`

## Slash Commands (23 total)

Commands are namespaced under their owning plugin (prefix: `/<plugin>:`). Most follow **PDF → JSON → Python → Report** automated workflow.

### leasing-commercial (15)

**Abstraction**
- `/leasing-commercial:abstract-lease` - Extract lease terms using 25-section template
- `/leasing-commercial:critical-dates` - Extract timeline and critical dates

**Financial Analysis**
- `/leasing-commercial:effective-rent` - NER, NPV, breakeven (Ponzi Rental Rate)
- `/leasing-commercial:renewal-economics` - Renewal vs. relocation NPV analysis
- `/leasing-commercial:tenant-credit` - Credit scoring and risk assessment
- `/leasing-commercial:option-value` - Real options valuation (Black-Scholes)
- `/leasing-commercial:rollover-analysis` - Portfolio lease expiry analysis
- `/leasing-commercial:rental-variance` - Rental variance decomposition by rate, area, and term
- `/leasing-commercial:relative-valuation` - MCDA competitive positioning with 25 variables, personas, and filters
- `/leasing-commercial:extract-mls` - Extract MLS data to professionally formatted Excel

**Accounting**
- `/leasing-commercial:ifrs16-calculation` - IFRS 16/ASC 842 lease accounting

**Compliance**
- `/leasing-commercial:default-analysis` - Default provisions and cure periods
- `/leasing-commercial:estoppel-certificate` - Estoppel generation
- `/leasing-commercial:notice-generator` - Generate lease notices
- `/leasing-commercial:work-letter` - Generate work letter from TI provisions

### appraisal-valuation (3)
- `/appraisal-valuation:comparable-sales-analysis` - Comparable sales DCA + MCDA adjustment grid
- `/appraisal-valuation:easement-valuation` - Easement compensation (percentage-of-fee, income capitalization, before/after)
- `/appraisal-valuation:mcda-sales-comparison` - MCDA ordinal ranking for fee simple valuation

### expropriation-law (2)
- `/expropriation-law:expropriation-compensation` - Full statutory compensation analysis under OEA
- `/expropriation-law:partial-taking-analysis` - Severance damages + injurious affection on partial takings

### common-utilities (3)
- `/common-utilities:convert-to-pdf` - Convert markdown files to PDF
- `/common-utilities:git-delete-comments` - Git operations utility
- `/common-utilities:git-delete` - Git operations utility

### Migration from v2.x

Many v2 commands were folded into related skills (which auto-activate via native discovery) or dropped entirely. To migrate workflows that referenced these:

| v2 command | v3 successor |
|---|---|
| `/recommendation-memo` | `commercial-lease-expert` skill |
| `/assignment-consent` | `consent-to-assignment-expert` skill |
| `/insurance-audit` | `lease-compliance-auditor` skill |
| `/compare-amendment`, `/compare-offers`, `/compare-precedent`, `/lease-vs-lease` | `lease-comparison-expert` skill |
| `/market-comparison`, `/environmental-compliance` | dropped (functionality redistributed across skills) |
| `/cropland-compensation-analysis` | `cropland-out-of-production-agreements` skill |
| `/location-overview`, `/right-of-way-analysis`, `/utility-conflict-analysis` | `right-of-way-expert` skill |
| `/transit-station-scoring` | `transit-station-site-acquisition-strategy` skill |
| `/expropriation-timeline` | `expropriation-timeline-expert` skill |
| `/injurious-affection-analysis`, `/settlement-analysis` | dropped (functionality in `injurious-affection-assessment` / `settlement-analysis-expert` skills) |
| `/income-approach-land` | `income-approach-expert` skill |
| `/cost-approach-infrastructure` | `cost-approach-expert` skill |
| `/title-analysis` | `title-expert` skill |
| `/environmental-due-diligence` | `environmental-due-diligence-expert` skill |
| `/negotiation-strategy` | `negotiation-expert-infrastructure` skill |
| `/board-memo`, `/briefing-note` | dropped |

**See**: `plugins/*/commands/` for detailed documentation

## Specialized Skills (23 total)

Skills are **automatically invoked** through Claude Code's native skill discovery - when your request matches a skill's description or you read relevant documents, Claude automatically loads the expertise. No manual invocation required. Skills live under `plugins/<name>/skills/`.

### Core Lease Agreements
- **commercial-lease-expert** - General lease negotiation, net lease structures, deal structuring

### Financial Analysis (NEW - 3 skills)
- **effective-rent-analyzer** - NER, NPV, breakeven analysis using Ponzi Rental Rate framework
- **tenant-credit-analyst** - Creditworthiness assessment, DSCR analysis, security structuring
- **lease-abstraction-specialist** - 25-section lease abstraction, critical dates extraction

### Compliance & Process (NEW - 3 skills)
- **lease-compliance-auditor** - Insurance, environmental, use clause, covenant compliance
- **default-and-remedies-advisor** - Default analysis, cure periods, damages calculation
- **lease-comparison-expert** - Amendment analysis, competing offers, precedent deviation

### Investment & Portfolio (NEW - 2 skills)
- **portfolio-strategy-advisor** - Lease rollover, expiry cliff analysis, renewal prioritization
- **real-options-valuation-expert** - Black-Scholes valuation of renewal/expansion/termination options

### Security & Protection
- **indemnity-expert** - Indemnity agreements, bankruptcy-proof provisions
- **non-disturbance-expert** - SNDA agreements, foreclosure protection

### Lease Modifications & Transfers
- **consent-to-assignment-expert** - Assignment consent, privity analysis
- **consent-to-sublease-expert** - Sublease consent, three-party structures
- **share-transfer-consent-expert** - Change of control, corporate restructuring
- **lease-surrender-expert** - Early termination, mutual release

### Preliminary & Ancillary Agreements
- **offer-to-lease-expert** - Offers to lease, LOIs, term sheets
- **waiver-agreement-expert** - Conditional waivers, counter-offers
- **temporary-license-expert** - Short-term licenses (1 day - 3 months)
- **storage-agreement-expert** - Storage lockers, ancillary space

### Specialized Licenses
- **telecom-licensing-expert** - Carrier access, CRTC compliance

### Dispute Resolution
- **lease-arbitration-expert** - Arbitration agreements, rent determination

### Negotiation & Objection Handling
- **negotiation-expert** - Evidence-based persuasion, calibrated questions, accusation audits
- **objection-handling-expert** - Objection analysis, response strategies, value-creating solutions

## Intelligent Skill Activation

Skills activate automatically via Claude Code's native skill discovery. When your request matches a skill's description, Claude loads the relevant expertise from the appropriate plugin without any manual configuration.

### How It Works

Claude Code scans skill descriptions in `plugins/<name>/skills/*/SKILL.md` at session start and activates matching skills based on your questions and the documents you're reading. No hook system required.

### Benefits

- **Proactive Expertise**: Skills load automatically when relevant
- **Native Discovery**: Uses Claude Code's built-in mechanism — no custom hooks needed
- **Context-Aware**: Right skills at the right time
- **No Memorization**: Don't need to remember which skills exist

### Maintenance

**Adding New Skills:**
```bash
# 1. Create skill directory in the appropriate plugin
mkdir -p plugins/<plugin-name>/skills/new-skill-name/
# 2. Create SKILL.md with description, triggers, and content
# 3. Skill is immediately discoverable — no rule regeneration needed
```

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

# Skills activate automatically based on your questions
# Example: "How do I negotiate rent with a difficult tenant?"
# → negotiation-expert skill loads automatically
# Example: "Review this assignment consent agreement"
# → consent-to-assignment-expert skill loads automatically

# Convert DOCX to markdown
markitdown document.docx -o output.md
```

## Templates

**Industrial**: `plugins/leasing-commercial/templates/Industrial/` (ANSI/BOMA Z65.2-2012 Method A)
**Office**: `plugins/leasing-commercial/templates/Office/` (ANSI/BOMA Office Buildings Standard)

Each has: `*_template.md`, `*_template.json`, `*_schema.json`

## JSON Schema Standards

When creating JSON schema validation documents (not data templates), follow these requirements:

**Schema Version**: Use JSON Schema **Draft 2020-12** or **Draft-07**
- Specify `"$schema"` at document root
- Draft 2020-12: `"$schema": "https://json-schema.org/draft/2020-12/schema"`
- Draft-07: `"$schema": "http://json-schema.org/draft-07/schema#"`

**Required Elements**:
1. **Object Structure**: Define `type`, `properties`, `additionalProperties`
2. **Type Definitions**: Specify data types for all fields (string, number, integer, boolean, array, object)
3. **Required Properties**: List mandatory fields in `required` array
4. **Validation Rules**: Add constraints appropriate to field type:
   - Numbers: `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`
   - Strings: `minLength`, `maxLength`, `pattern`, `format`, `enum`
   - Arrays: `minItems`, `maxItems`, `uniqueItems`
   - Objects: `minProperties`, `maxProperties`

**Example Structure**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/schemas/my-schema.json",
  "title": "Schema Title",
  "description": "Schema description",
  "type": "object",
  "required": ["field1", "field2"],
  "properties": {
    "field1": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "description": "Field description"
    }
  },
  "additionalProperties": false
}
```

**Naming Convention**: Use `*_schema.json` suffix for validation schemas, `*_template.json` for data templates

## Key Lease Provisions

**Net Lease**: Tenant pays base rent + proportionate share of opex/taxes/mgmt fees
**Proportionate Share**: Rentable Area ÷ Total Building Area
**Standard Schedules**: A-J (Legal, Plan, Work, Deposit, Environmental, Rules, Special Provisions, Indemnity, PAD, LC)
**Schedule G**: Special Provisions - often contains critical custom terms that override standard provisions

**Typical Values**:
- Management fees: 5% (multi-tenant), 3% (single/landlord), 2.75% (single/tenant)
- Default cure: 5-10 days (rent), 15-30 days (covenants)
- Insurance: $2M-$5M CGL, replacement cost property, 12mo business interruption

## Reference

`plugins/leasing-commercial/templates/Industrial/` and `plugins/leasing-commercial/templates/Office/` - Lease template scaffolding (ANSI/BOMA aligned)

`plugins/leasing-commercial/commands/` - All slash command definitions (namespaced under `leasing-commercial`)

`plugins/common-utilities/personas/` - Master persona files for Adam, Reggie, and Dennis (source of truth for output styles and skills)
