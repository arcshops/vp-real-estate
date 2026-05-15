# Meet Reggie Chan and His Team

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/reggiechan74/vp-real-estate/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12%2B-brightgreen.svg)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/code%20style-typed-black.svg)](https://docs.python.org/3/library/typing.html)
[![GitHub Stars](https://img.shields.io/github/stars/reggiechan74/vp-real-estate?style=social)](https://github.com/reggiechan74/vp-real-estate)

**Version 3.0.0** • Released 2026-05-15

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

## The Digital Embodiment of a 20-Year Real Estate Veteran—And His Team

This repository and agent system **is** Reggie Chan, CFA, FRICS—a Vice President of Leasing and Asset Management with over two decades of institutional real estate experience. Working alongside Reggie are Adam (his senior analyst) and Dennis (his former boss and strategic advisor).

**It's like having Reggie Chan and his team work for you—for the price of a Claude Code subscription.**

You're not just getting software. You're getting:
- **Reggie Chan, CFA, FRICS** - VP of Leasing & Asset Management with 20+ years of institutional real estate experience. Handles complex problems, crisis turnarounds, fraud detection, and multi-domain synthesis. The brain behind the operation.
- **Adam** - Reggie's senior analyst and protégé. Handles routine lease analysis, credit checks, and professional communication. Fast execution for straightforward tasks.
- **Dennis** - Reggie's former boss with 36+ years of battle-tested experience. Provides strategic wisdom, negotiation psychology, and brutal honesty when you need it most.
- **Complete toolkit** - 11 financial calculators, **23+ specialized skills**, 30+ automated workflows, **Location Overview module** for appraisal research, and skills that auto-activate via Claude Code's native skill discovery

Just address "Reggie," "Adam," or "Dennis" in your messages and watch the right team member handle your request—from everyday analysis to impossible problems to strategic decisions.

---

### **TL;DR: Survive the Asset Manager's Inquisition. Get to Your Tee Time.**

Every great deal is a war fought on two fronts: one against the market, and the other against the asset manager's love of spreadsheets. You win the first war with instinct and a handshake. You win the second with this.

*   **Speak Fluent Asset Management (Without Knowing a Thing).**
    Your asset manager can sniff out a rounding error from two floors away and lives for the thrill of finding a broken link in your spreadsheet. Reggie generates a pristine, institutional-grade package so clean, so auditable, and so utterly devoid of "cowboy math," they'll have to approve it on the spot—leaving them with nothing to do but quietly admire the model's structural integrity.

*   **The Ultimate Desk Chair to Golf Cart Conversion Kit.**
    Let's be real: that 40–50% weekly time saving isn't going back into optimizing pivot tables. It's for chasing the next deal or lowering your handicap. Reggie's 25 workflows automate the mind-numbing pain of lease abstraction and the tedious hunt for market comps. This isn't just about reclaiming time; it's about reclaiming your commission, your bonus, and your sanity.

*   **Have the Answer Before They Can Even Form the Question.**
    Get ready for the lightning round of impossible questions. *"What's the three-scenario NPV on our portfolio rollover risk for Q3 2026?"* *"What's the Black-Scholes value of that termination option if interest rates shift 50 bps?"* Before, you'd stall. Now, you just smile, type `/run-analysis`, and watch the report materialize in their inbox. It’s the ultimate power move.

It's the perfect unspoken agreement. You hand them the unimpeachable, meticulously documented data they worship. So sure, they win. But you win even more on the back nine.

---

**[README for Leasing Managers](README-FOR-LEASING-MANAGERS.md)** ← Same toolkit, told the way you actually talk.

**[Why I Built This](WHY-I-BUILT-THIS.md)** ← From spreadsheet monk to deal closer. The origin story.

**[FAQ](FAQ.md)** ← The questions you're already asking.

---

## NEW: Linear Infrastructure & Property Acquisition Toolkit

Beyond commercial leasing, we've added a complete **infrastructure acquisition team** for transit corridors, utility transmission lines, highway expansion, and agricultural easements.

### The Infrastructure Quintet

| Agent | Role | Specialization |
|-------|------|----------------|
| **Alexi** | Valuation Expert (AACI) | Easement valuation, severance damages, comparable sales, before/after method |
| **Christi** | Expropriation Law | Ontario Expropriations Act, legal entitlement, settlement strategy, hearing prep |
| **Katy** | Transit Corridors | Station acquisitions, public consultation, stakeholder management |
| **Shadi** | Utility Corridors | Transmission lines, farmer negotiations, 50-100+ parcel logistics |
| **Stevi** | Compliance | Statutory deadlines, Forms 1-12 verification, procedural compliance |

### Legal Specialists

| Agent | Role | Specialization |
|-------|------|----------------|
| **Benji** | Commercial Tenancies Act | CTA interpretation, landlord remedies, lease disputes |
| **Anni** | Residential Tenancies Act | RTA/LTB procedures, eviction law, tenant rights |

### Quick Examples

```
"Alexi, value this 60m transmission line easement through farmland"

"Christi, is the owner entitled to severance damages under the OEA?"

"Katy, plan the public consultation for the new LRT station"

"Shadi, develop an acquisition strategy for 75 parcels along the corridor"

"Stevi, what statutory deadlines are we facing on this file?"
```

**[Complete Infrastructure Toolkit Guide](LINEAR_INFRASTRUCTURE.md)** ← Full documentation for the infrastructure team

---

## NEW: Location Overview Module for Appraisal Research

Automate the tedious research phase of property appraisals with the `right-of-way-expert` skill. Just ask about location/zoning/planning research for a property address and the skill auto-loads to query 11 data providers in parallel and compile zoning, planning, environmental, and neighbourhood data.

### Supported Municipalities (82% Coverage)

| Municipality | Zoning | Official Plan | Transit | Heritage | Conservation |
|--------------|--------|---------------|---------|----------|--------------|
| **Toronto** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Ottawa** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Mississauga** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Hamilton** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Other Ontario** | — | — | ✅ | ✅ | ✅ |

### Data Providers

- **Municipal**: Toronto/Ottawa/Mississauga/Hamilton Open Data (zoning, OP, secondary plans, wards)
- **Provincial**: Ontario GeoHub (Greenbelt, Oak Ridges Moraine, Niagara Escarpment, Growth Plan)
- **Environmental**: TRCA/CVC conservation areas, Brownfields ESR, Heritage registries
- **Neighbourhood**: Census demographics, GTFS transit, Overpass POI amenities
- **CUSPAP Compliance**: Built-in validator for appraisal report standards

### Quick Example

> "Generate a location overview for 100 Queen Street West, Toronto."

The `right-of-way-expert` skill auto-loads and produces a comprehensive location overview report with:
- Zoning designation and permitted uses
- Official Plan and Secondary Plan designations
- Provincial plan overlays (Greenbelt, Growth Plan, etc.)
- Surrounding land uses (N/S/E/W analysis)
- Transit accessibility and amenities
- Heritage and environmental constraints
- CUSPAP compliance score

---

## How to Work with Reggie and His Team

Simply address **"Reggie"** for most situations. For routine work, ask **"Adam"** (Reggie's analyst). For strategic wisdom, consult **"Dennis"** (Reggie's former boss).

### Reggie Chan - Your VP of Leasing & Asset Management (Primary Contact)

**Reggie is your go-to for complex lease analysis and crisis situations:**

```
"Reggie, what do you think of this renewal offer at $25/sf with 3 months free rent?"

"Reggie, this tenant's financials show declining revenue—are they hiding something?"

"Reggie, we have 6 months to turn around this distressed asset"

"Reggie, build me a framework for evaluating assignment consent requests"
```

**Reggie handles:**
- Complex/distressed situations or crisis turnarounds
- Fraud detection or forensic accounting
- Multi-domain synthesis (legal + accounting + finance + portfolio)
- Non-standard lease structures
- Situations requiring exhaustive documentation
- Deal evaluation and negotiation strategy

### Adam - Reggie's Senior Analyst (For Routine Work)

**Use Adam for straightforward tasks requiring fast execution:**

```
"Adam, analyze this renewal offer at $25/sf with 3 months free rent"

"Adam, run a basic credit check on this tenant's financials"

"Adam, prepare a professional response to this rent objection"
```

**Adam handles:**
- Standard lease evaluations with typical terms
- Routine tenant credit checks (clear financials, no red flags)
- Renewal offer assessments (market conditions clear)
- Professional communication to stakeholders
- Fast turnaround required (80/20 analysis sufficient)

### Dennis - Reggie's Former Boss (For Strategic Wisdom)

**Use Dennis for strategic guidance and reality checks:**

```
"Dennis, the tenant wants a rent reduction but won't give me financials. What do I do?"

"Dennis, should I accept this below-market renewal or push them out?"

"Dennis, how do I negotiate with someone who has all the leverage?"
```

**Dennis handles:**
- Strategic career decisions
- Negotiation psychology and power dynamics
- People management and team building
- Work-life balance reality checks
- When you need brutal honesty from someone who's seen it all

### The Natural Workflow

**Daily question → Adam handles routine work → Red flags? → Escalate to Reggie → Strategic implications? → Consult Dennis**

Reggie and his team have access to:
- **24 leasing-commercial skills (59 across the full marketplace)** for every lease, tenancy, expropriation, appraisal, and infrastructure situation (NEW: effective rent analysis, tenant credit, compliance auditing, portfolio strategy, real options valuation, and more)
- **23 slash commands** that automate everything from lease abstraction to IFRS 16 accounting
- **11 financial calculators** including NPV, effective rent, credit scoring, and Black-Scholes option valuation

You get executive-level judgment, institutional financial rigor, and 20+ years of property expertise—with the right team member for every situation.

---

## Why These Personalities Exist

### The Problem: Claude Code's Default Persona

Claude Code's default behavior tends toward being **overly diplomatic, excessively agreeable, and reluctant to challenge assumptions**. When you're making multimillion-dollar real estate decisions, the last thing you need is an AI assistant that:

- Validates every idea regardless of merit
- Sugarcoats bad news to avoid offending you
- Defaults to "sounds good!" when critical analysis is required
- Hesitates to point out when your math doesn't work
- Treats politics as more important than truth

This sycophantic tendency is dangerous in commercial real estate where **being wrong costs real money**.

### The Solution: Personality-Driven Specialization

The triumvirate agents—Reggie, Adam, and Dennis—are based on **real people** with distinct professional personas. Their personalities aren't cosmetic flourishes; they're **functional tools** designed to override Claude Code's default diplomatic drift:

**Reggie Chan** - The Forensic Analyst
- **Based on**: A real CFA/FRICS with 20+ years institutional experience
- **Personality traits** (deliberately exaggerated):
  - Political blindness (will call out flaws publicly)
  - Relentless skepticism (verifies everything twice)
  - Zero neuroticism (unfazed by pressure or conflict)
  - Compulsive quantification (every claim gets numbers)
  - Framework-building obsession (systematizes everything)
- **Why this matters**: Reggie won't tell you what you want to hear. He'll tell you what the numbers say—even if it contradicts your assumptions or embarrasses you in front of stakeholders.

**Adam** - The Diplomatic Translator
- **Based on**: Reggie's real-life senior analyst and protégé
- **Personality traits** (deliberately exaggerated):
  - Politically aware (sees organizational dynamics)
  - Dry wit (occasionally amusing, never sycophantic)
  - 80/20 pragmatism (fast execution over perfection)
  - Diplomatic delivery (translates brutal truth into professional language)
- **Why this matters**: Adam takes Reggie's unfiltered analysis and packages it for stakeholders who need their egos managed. He's politically fluent without sacrificing analytical integrity.

**Dennis** - The Brutal Realist
- **Based on**: Reggie's former boss with 36+ years executive experience
- **Personality traits** (deliberately exaggerated):
  - Blunt truth-telling (no sugarcoating ever)
  - Strategic ruthlessness (Father Time is undefeated)
  - Negotiation psychology expertise (sees power dynamics)
  - Work-life balance enforcer (will tell you when you're being an idiot)
- **Why this matters**: Dennis provides reality checks when you're about to make a career-limiting mistake or work yourself to death. He's seen every market cycle and isn't impressed by your fancy spreadsheet.

### Design Philosophy: Exaggerated But Authentic

These personalities are **based on real professional archetypes** but with certain traits deliberately amplified:

- **Reggie's political blindness** is real but exaggerated to ensure he never defaults to diplomatic evasion
- **Adam's dry humor** prevents the bland corporate-speak that plagues most AI assistants
- **Dennis's bluntness** guarantees you get unfiltered strategic wisdom, not reassuring platitudes

**The goal**: Create agents that are **recognizably human** in their strengths and limitations, forcing you (the user) to think critically about which expertise you need for each situation.

### When to Override the Default Persona

Use these agents whenever you need:
- **Brutal honesty** over reassurance (Reggie or Dennis)
- **Political translation** of harsh truths (Adam)
- **Strategic reality checks** on big decisions (Dennis)
- **Forensic skepticism** on tenant claims (Reggie)
- **Fast diplomatic execution** on routine work (Adam)

The default Claude Code persona remains available for general questions. But when real money is on the line, you want Reggie's forensic rigor, Adam's political fluency, or Dennis's battle-tested wisdom—not an AI assistant trying to make you feel good about a bad deal.

**Bottom line**: These personalities exist to **counteract AI sycophancy** by giving you access to distinct professional archetypes who won't hesitate to tell you when you're wrong. Because in commercial real estate, being liked matters less than being right.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Why These Personalities Exist](#why-these-personalities-exist)
3. [Capabilities](#capabilities)
4. [Architecture & Tech Stack](#architecture--tech-stack)
5. [Productivity Impact](#productivity-impact)
6. [Scope & Use Cases](#scope--use-cases)
7. [Roadmap](#roadmap)
8. [Project Structure](#project-structure)
9. [Compliance & Limitations](#compliance--limitations)
10. [Contributing](#contributing)
11. [License & Attribution](#license--attribution)
12. [Support](#support)

---

## Getting Started

### Requirements
- **Claude Code** - Anthropic's official CLI (required for slash-command workflows)
- Python 3.12+ (installed automatically via Claude Code)

### Installation

**Step 1: Install Claude Code**

```bash
# Install Claude Code from https://docs.claude.com/claude-code
# For most systems:
npm install -g @anthropic-ai/claude-code
```

**Step 2: Clone the Repository**

```bash
git clone https://github.com/reggiechan74/vp-real-estate.git
cd vp-real-estate
```

**Step 3: Install Dependencies via Claude Code**

Open Claude Code in the repository directory and run:

```
Install all the dependencies for this project
```

Claude Code will install:
- Python dependencies: `numpy`, `pandas`, `scipy`, `openpyxl`, `pytest`, `markitdown[docx]`
- PDF generation tools: `pandoc`, `wkhtmltopdf`
- All other required packages

**Alternative: Manual Installation**

If you prefer to install dependencies manually without Claude Code:

```bash
pip install numpy pandas scipy
pip install 'markitdown[docx]'        # document conversion
pip install openpyxl                  # Excel export for MLS extraction
pip install pytest                    # optional: run test suite

# For PDF report generation (relative valuation, etc.)
sudo apt-get install -y pandoc wkhtmltopdf  # Linux/Ubuntu
# Or: brew install pandoc wkhtmltopdf       # macOS
```

*Note: Manual installation limits you to direct calculator usage. Slash commands require Claude Code.*

### First Workflow: Abstract & Analyze

```bash
# 1. Extract lease terms into the 25-section template
/leasing-commercial:abstract-lease path/to/lease.docx

# 2. Run an effective-rent analysis on the same deal
/leasing-commercial:effective-rent path/to/lease.pdf

# 3. Extract MLS data to Excel for competitive analysis
/leasing-commercial:extract-mls path/to/mls_report.pdf --subject="2550 Stanfield"
```

Each command follows the same pipeline:
1. Extract data from PDF/DOCX
2. Generate validated JSON input
3. Execute the relevant calculator
4. Write a timestamped report into `Reports/`

### Run the Test Suite

```bash
python -m pytest plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/Eff_Rent_Calculator/Tests/ -v
```

---

## Capabilities

**What Reggie and His Team Bring to Your Operations**

Reggie's expertise is backed by a complete suite of analytical tools and specialized knowledge systems that he and his team can deploy instantly:

### Specialized Skills (24 in leasing-commercial; 59 across the full marketplace)
When you ask Reggie, Adam, or Dennis about specific situations, they automatically activate the relevant expert system. The bullets below highlight the leasing-commercial subset; the full marketplace adds residential tenancy, expropriation, appraisal, and infrastructure-corridor skills across six plugins (see `CLAUDE.md` for the cross-plugin inventory):

- **Core leasing**: Deal structuring and negotiation strategy for industrial/office leases
- **Transfers & modifications**: Assignment consent, sublease analysis, share transfers, surrenders, waivers
- **Security & protection**: Indemnity agreements, SNDA/non-disturbance negotiations
- **Ancillary agreements**: Temporary licenses, storage agreements, telecom licensing
- **Disputes**: Lease arbitration frameworks and rent determination
- **Negotiation & objection handling**: Evidence-based persuasion (calibrated questions, accusation audits, tactical empathy); systematic objection analysis and response strategies

Each skill provides checklists, negotiation angles, risk flags, and recommended language—like having a senior advisor instantly available for every situation. Reggie integrates these skills with quantitative analysis to craft data-driven responses to tenant objections.

### Reggie's Financial Toolkit (11 Analytical Engines)
These are the quantitative tools Reggie and his team use to back up their recommendations with institutional-grade analysis:
1. **Effective Rent Calculator** (`plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/Eff_Rent_Calculator/`)  
   - Inputs: rent schedule (annual $/sf), incentives (TI, cash allowances, free rent), leasing costs, REIT capital assumptions.  
   - Outputs: Net/Gross Effective Rent, NPV vs. costs, breakeven rents, Ponzi Rental Rate comparison, payback, sensitivity tables.  
   - Use Cases: Offer structuring, investment committee packages, renegotiation analysis.
2. **Rental Yield Curve** (`plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/Rental_Yield_Curve/`)  
   - Models implied termination options to build a rent term structure, forecasting market rent shifts across maturities.  
   - Supports “what-if” scenarios for escalation clauses, early termination rights, and renewal probabilities.
3. **Rental Variance Analysis** (`plugins/leasing-commercial/skills/lease-comparison-expert/scripts/Rental_Variance/`)  
   - Decomposes revenue variance into rate, area, and term components using DAYS360 methodology; reconciles budget vs. actuals with audit-ready tables.  
   - Ideal for monthly/quarterly reporting packs and leasing scorecards.
4. **Relative Valuation Engine** (`plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/Relative_Valuation/`)
   - Weighted MCDA rankings across up to 25 variables (9 core + 16 optional) with dynamic weight allocation based on data availability.
   - Core variables: rent, TMI, parking, clear height, office %, distance, building age, class, area match.
   - Optional variables: shipping doors (TL/DI), power, trailer parking, secure shipping, excess land, bay depth, lot size, HVAC, sprinkler, rail, crane, occupancy, grade-level doors, days on market, zoning.
   - **External Weights Configuration** - JSON-based weight management with 4 tenant personas (default, 3pl, manufacturing, office).
   - **Auto-Load Defaults** - Weights automatically loaded when not provided in input JSON.
   - **Complete Transparency** - All weights displayed in reports with mathematical 100% verification.
   - Outputs competitive status, pricing gap to Top 3, rent/TMI adjustment scenarios, and landscape PDF reports with professional formatting and page break controls.
5. **IFRS 16 / ASC 842 Calculator** (`plugins/leasing-commercial/skills/effective-rent-analyzer/scripts/IFRS16_Calculator/`)  
   - Generates present value of lease liabilities, ROU asset schedules, journal entries, and CSV amortization/depreciation tables.  
   - Used for monthly close, audit support, and disclosure packages.
6. **Tenant Credit Analysis** (`plugins/leasing-commercial/skills/tenant-credit-analyst/scripts/Credit_Analysis/`)  
   - Calculates 15+ ratios, produces a 100-point credit score, assigns rating band, estimates PD/LGD, and recommends security amounts.  
   - Supports underwriting, renewal risk reviews, and portfolio credit surveillance.
7. **Renewal Economics** (`plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/Renewal_Analysis/`)
   - Compares renewal vs. relocation scenarios incorporating relocation capex, downtime, IRR, payback, and blended NER.
   - Guides negotiation stance on expiring leases and capital allocation.
8. **Portfolio Rollover Calculator** (`plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/Rollover_Analysis/`)
   - Aggregates lease expiries by year/quarter with concentration risk flags (>20% HIGH, >30% CRITICAL).
   - Priority scoring (0-1 normalized) based on rent contribution, urgency, below-market status, and credit rating.
   - Three-scenario modeling (optimistic/base/pessimistic) with scenario-specific downtime and NPV discounting.
   - Use Cases: Portfolio planning, renewal prioritization, budget forecasting, expiry cliff risk management.
   - **37 tests passing** (100% coverage) including edge cases (empty portfolio, 0%/100% renewal rates).
9. **Default Damage Calculator** (`plugins/leasing-commercial/skills/default-and-remedies-advisor/scripts/Default_Calculator/`)
   - Quantifies landlord damages from tenant defaults: arrears (with interest), future rent NPV, re-letting costs, mitigation credits.
   - Business day cure period calculations with jurisdiction-aware legal framework.
   - Bankruptcy cap analysis (§502(b)(6)) for Chapter 11 scenarios.
   - Net exposure calculation after security deposits and letters of credit.
   - Use Cases: Default notices, settlement negotiations, litigation support, security adequacy reviews.
   - **32 tests passing** (100% coverage) with comprehensive METHODOLOGY.md documentation (1,850 lines).
10. **Statistical Analysis Module** (`plugins/leasing-commercial/skills/portfolio-strategy-advisor/scripts/Relative_Valuation/statistics_module.py`)
    - Supplements MCDA rankings with traditional statistical analysis (multiple linear regression, correlation, z-scores).
    - Identifies rent drivers, data quality issues, and market outliers.
    - Activated via `--stats` flag on relative valuation calculator.
    - Key Insights: Most variable factor (CV), rent predictability (R²), strongest driver, strongest correlation.
    - Use Cases: Large datasets (20+ properties), understanding rent drivers, validating MCDA results, data quality checks.
11. **Real Options Valuation Calculator** (`plugins/leasing-commercial/skills/real-options-valuation-expert/scripts/Option_Valuation/`)
    - Black-Scholes option pricing for lease flexibility (renewal, expansion, termination, purchase options).
    - Calculates option value, Greeks (Delta, Gamma, Vega, Theta, Rho), and probability in-the-money.
    - Portfolio valuation for multiple concurrent options with sensitivity analysis.
    - JSON input/output with command-line interface for automation.
    - Use Cases: Valuing embedded lease options, negotiation support, lease vs. purchase decisions, portfolio option value aggregation.
    - **36 tests passing** (100% coverage) validated against published Black-Scholes calculators.

### Reggie's Automated Workflows (23 Slash Commands)
Reggie and his team have 23 automated workflows at their disposal across the marketplace. Each slash command packages data extraction instructions, domain expertise, calculator invocation, and report formatting. The table below highlights the leasing-commercial commands (14 total: Abstraction (2), Financial Analysis (9), Accounting (1), Compliance (4)). For the cross-plugin inventory (appraisal-valuation, expropriation-law, common-utilities), see `CLAUDE.md`.

| Category | Command | Primary Output |
|----------|---------|----------------|
| Abstraction | `/leasing-commercial:abstract-lease` | 25-section lease abstract + JSON schema |
| Abstraction | `/leasing-commercial:critical-dates` | Timeline of renewals, expiries, and notice trigger dates |
| Financial Analysis | `/leasing-commercial:effective-rent` | Deal economics report with NER/GER, PRR, sensitivities |
| Financial Analysis | `/leasing-commercial:tenant-credit` | Credit memo with ratios, PD/LGD, security recommendation |
| Financial Analysis | `/leasing-commercial:rental-variance` | Budget vs. actual variance decomposition |
| Financial Analysis | `/leasing-commercial:rollover-analysis` | Portfolio expiry risk dashboard with action plan |
| Financial Analysis | `/leasing-commercial:option-value` | Real options valuation (renewal, expansion, termination) |
| Financial Analysis | `/leasing-commercial:renewal-economics` | Renewal vs. relocation recommendation matrix |
| Financial Analysis | `/leasing-commercial:relative-valuation` | Competitive ranking report and pricing adjustments |
| Financial Analysis | `/leasing-commercial:extract-mls` | Extract MLS data to professionally formatted Excel with subject property highlighting |
| Accounting | `/leasing-commercial:ifrs16-calculation` | IFRS/ASC 842 schedules and journal entries |
| Compliance | `/leasing-commercial:default-analysis` | Default and cure provisions analysis |
| Compliance | `/leasing-commercial:estoppel-certificate` | Draft estoppel certificate populated from abstract |
| Compliance | `/leasing-commercial:notice-generator` | Draft lease notices (renewal, termination, default) |
| Compliance | `/leasing-commercial:work-letter` | Work letter outline from TI provisions |

> **Tip:** Every workflow writes outputs to `Reports/` with standardized timestamps, making it easy to hand off bundles to executives, lenders, or auditors. Commands are namespaced under their plugin (e.g. `/leasing-commercial:effective-rent`). See `plugins/leasing-commercial/commands/` for arguments, required supporting documents, and validation steps. Additional commands live under the appraisal-valuation, expropriation-law, and common-utilities plugins — see `CLAUDE.md` for the full 23-command inventory.

See `plugins/leasing-commercial/commands/` for full instructions and input templates.

### Templates & Reporting
- Industrial and office 25-section abstracts (Markdown + JSON + schema).  
- Markdown reports stored in `Reports/YYYY-MM-DD_HHMMSS_[description].md`.  
- CSV exports for amortization schedules, variance breakdowns, and credit outputs.

---

## Architecture & Tech Stack

- **Language**: Python 3.12+, type hinted, modular packages.
- **Core Libraries**: NumPy, Pandas, SciPy, NumPy-Financial.
- **Testing**: Pytest with 235+ passing tests (unit + regression).
- **Workflow Pattern**: PDF → markitdown conversion → structured JSON → calculator → report.
- **Repository Layout**: Shared utilities plus dedicated folders for each calculator. See `CLAUDE.md` for a directory map and automation tooling.

---

## Productivity Impact

- Leasing managers typically spend ~60% of their week on analysis, compliance, and documentation.  
- Automated workflows + calculators cover 70–80% of that effort, unlocking an overall **40–50% reduction in total weekly workload**—often equating to two reclaimed workdays.  
- Expert skills collapse research and drafting cycles from hours to minutes, reducing dependence on senior review bottlenecks.  
- Standardized outputs (JSON, Markdown, CSV) make hand-offs to finance, legal, and executives immediate and auditable.

---

## Scope & Use Cases

### Who Uses Reggie and His Team
- **REITs & institutional investors**: full lifecycle leasing, reporting, compliance.
- **Property & asset managers**: renewals, modifications, expiry management.
- **Corporate real estate teams**: lease-vs-buy decisions, IFRS/ASC compliance.
- **Brokers & advisors**: offer preparation, market comparisons, negotiation prep.

### What Reggie and His Team Cover
- Deal structuring, LOIs, concession modeling, arbitration prep.  
- Lease drafting support: assignments, indemnities, SNDAs, surrenders, telecom, storage.  
- Financial analytics: NER/GER, NPV, IRR, variance, sensitivity, option value.  
- Accounting: IFRS 16 / ASC 842 liability and ROU asset workflows.  
- Credit risk: scoring, PD/LGD, security recommendations.  
- Lease administration: abstraction, critical dates, notices, amendment tracking.  
- Advanced analytics: term structure modelling, portfolio rollover, market benchmarking.

---

## Roadmap

Short-term priorities:
1. Comparative market analytics (automated comps ingestion and benchmarking).
2. Tenant mix optimisation and portfolio-level dashboards.
3. Expanded API integrations (Distancematrix.ai, CoStar/LoopNet) for automated data refresh.
4. Machine learning-based weight optimization from historical deal outcomes.

---

## Project Structure

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

Refer to `CLAUDE.md` for a full breakdown of plugins, commands, skills, agents, and output styles.

---

## Compliance & Limitations

- Reggie (this toolkit) is **not** legal, accounting, tax, or investment advice.  
- All outputs must be independently verified by qualified professionals.  
- Accuracy is contingent on clean inputs; garbage in → garbage out.  
- Users remain responsible for regulatory compliance, disclosure, and professional judgment.  
- Use at your own risk; see `LICENSE` for full warranty disclaimers.

---

## Contributing

Contributions are welcome—focus on calculators, workflows, templates, documentation, or tests.  
Please:
- Add or update unit tests with every change.  
- Document assumptions and limitations.  
- Follow the established directory structure and coding style.  
- Update `CHANGELOG.md` and relevant READMEs.

---

## License & Attribution

Licensed under **Apache License 2.0**. See `LICENSE` for full terms.  
Key dependencies: Python, NumPy, Pandas, SciPy, markitdown (see respective licenses).  
Academic foundations from R. Chan’s work on Ponzi Rental Rate and rental term structures.

---

## Support

**Version**: 3.0.0 (Released 2026-05-15)
**Your VP of Leasing & Asset Management**: Reggie Chan, CFA, FRICS
**Reggie's Team**: Adam (Senior Analyst) • Dennis (Strategic Advisor) • +7 Infrastructure Specialists

For issues and feature requests, open a ticket in the repository.

**Remember**: While Reggie and his team bring combined decades of institutional experience and sophisticated analytical tools, all outputs should be validated by qualified professionals. This system provides executive-level guidance and analysis—but you remain responsible for final decisions.

⚠️ Always validate model outputs before reliance on material decisions.
