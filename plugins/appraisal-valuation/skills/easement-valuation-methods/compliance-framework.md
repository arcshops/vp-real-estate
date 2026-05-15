# Professional Standards Compliance Framework

Deep dive on USPAP / CUSPAP / Yellow Book / IVS requirements, reconciliation methodology, and adjustment hierarchy. Summarized in `SKILL.md`; this file is the authoritative reference.

## Applicable Standards

| Standard | Scope |
|----------|-------|
| **USPAP 2024** | Uniform Standards of Professional Appraisal Practice — USA |
| **CUSPAP 2024** | Canadian Uniform Standards of Professional Appraisal Practice |
| **Yellow Book (UASFLA)** | Uniform Appraisal Standards for Federal Land Acquisitions |
| **IVS 2022** | International Valuation Standards — IVS 105 Valuation Approaches |

## Key Principles

- **Before-and-After Method**: Preferred approach for partial takings and easements — value of entire property before easement minus value after easement.
- **Scope of Work**: Each assignment requires appropriate scope development based on complexity, intended use, and jurisdictional requirements.
- **Highest and Best Use**: Analyze both Before and After conditions to measure true impact of easement restrictions.
- **Reconciliation**: Weight approaches based on data quality and reliability, **not** simple averaging.
- **Market Extraction**: When possible, extract easement percentages empirically from paired sales rather than relying solely on published ranges.

## Adjustment Hierarchy for Comparable Sales

Apply in sequence — earlier adjustments are cleaner (closer to "all else equal"):

1. **Property rights** — fee simple vs. leasehold vs. life estate
2. **Financing terms** — cash equivalent adjustment for seller financing
3. **Conditions of sale** — arm's length, market exposure time, motivation
4. **Market conditions / time** — trend analysis, quarterly price indices
5. **Location** — micro-market differences, accessibility, development potential
6. **Physical characteristics** — size, shape, topography, soil class, drainage, services
7. **Easement characteristics** — type, width, restrictions, permanence, operator

**Quantification methods**:
- Paired sales analysis (isolation of single variable)
- Regression analysis (statistical modeling with multiple variables)
- Market interviews (surveying buyers/sellers on perception)
- Professional judgment (when insufficient market data — document reasoning)

For a fully worked adjustment grid, see `worked-examples.md` §3.

## Reconciliation of Multiple Approaches

**USPAP / CUSPAP requirement**: appraisers must reconcile different approaches through **reasoned analysis**, not simple averaging. Reconciliation requires professional judgment to weight approaches based on data quality, reliability, and appropriateness to the specific easement.

### Step 1 — Review Each Approach

Evaluate each approach used:
- **Data quality and quantity** — how many comparables? How similar to subject? Arm's length?
- **Reliability of assumptions** — cap rates market-supported? Percentage ranges validated? Adjustments reasonable?
- **Appropriateness to easement type** — income approach strong for telecom sites; weak for non-revenue easements.
- **Market participant behavior** — which approach would buyers/sellers actually use in negotiations?

### Step 2 — Assign Weights

**Percentage of Fee Method**:
- Strong when: comparable easement sales exist; market-extracted percentages validated by multiple transactions; voltage / product type well-supported.
- Weak when: limited easement sale data; wide range in published percentages; subject easement has unique characteristics.

**Income Capitalization Approach**:
- Strong when: revenue-generating easements (telecom, agricultural rent loss clearly measurable); reliable cap rates; perpetual duration.
- Weak when: non-income easements (access rights don't generate revenue); speculative income assumptions; uncertain duration.

**Before/After Comparison (paired sales)**:
- Strong when: excellent paired sales available (truly comparable, only difference is easement); reliable adjustments; statistical validation.
- Weak when: limited paired sales; significant adjustments required (introduces uncertainty); wide variation in extracted percentages.

### Example Weighting — 230 kV Transmission Easement, Agricultural Land

| Approach | Weight | Reasoning |
|----------|--------|-----------|
| Percentage of fee | 40% | Market-extracted percentage (15-20%) validated by 8 comparable transmission easement sales; voltage-specific data strong. |
| Income capitalization | 30% | Agricultural rent analysis reasonable ($300/ac → 20% loss → $60/yr → cap at 4.5% = $1,333/ac); perpetual easement supports capitalization. |
| Before/after paired sales | 30% | One excellent paired sale available (extracted 17% impact); adjustments minor, but single data point limits weight. |

### Step 3 — Range and Consistency Test

- All approaches should produce reasonably consistent results (within 20-25%).
- If wide divergence (>25%), **revisit assumptions** before proceeding.
- Outliers may indicate:
  - Data errors (incorrect sale price, easement area miscalculated)
  - Methodology errors (wrong cap rate, improper adjustments)
  - Subject easement has unique characteristics not captured in comparables

### Step 4 — Select Final Reconciled Value

Final value may be:
- **Weighted average** of approaches (most common when all approaches reliable)
- **Within range but not average** (if one approach clearly more reliable, favor that result)
- **At one end of range** (if market data strongly supports upper or lower end)

Document reasoning for final selection — explain why you selected that specific value within the range.

### Step 5 — Sensitivity Analysis

Test impact of key assumption changes on final value:
- Cap rate ±1% — if 4.5% cap, test 3.5% and 5.5%
- Percentage of fee ±5% — if 15%, test 10% and 20%
- Time adjustments ±2% — if 3% annual appreciation, test 1% and 5%

**Assess impact**: if ±1% cap rate changes value by ±22%, cap rate is highly sensitive — ensure rate is well-supported.

Document range of reasonable values based on sensitivity testing — provides confidence band around reconciled value.

For a complete worked reconciliation example, see `worked-examples.md` §5.

## Related Skills Integration

This skill focuses specifically on **easement valuation methodology**. For comprehensive infrastructure acquisition analysis, integrate with related skills covering adjacent components of total compensation.

### Valuation Components and Technical Methodology

**`comparable-sales-adjustment-methodology`** — Before/After Market Extraction Technical Rigor
- Provides 6-stage adjustment hierarchy (property rights → financing → conditions → time → location → physical).
- Includes 49 physical characteristic adjustments with statistical validation.
- Ensures USPAP/CUSPAP compliance for adjustment quantification.

**`severance-damages-quantification`** — Damages to Remainder Parcel
- Quantifies severance damages: access loss ($/linear foot by road class, time-distance modeling); shape irregularity (geometric efficiency ratios, buildable area reduction); farm operation disruption (field division, equipment access, irrigation impacts).
- Used as "Plus Damages" component in take-plus-damages framework.

**`injurious-affection-assessment`** — Construction and Proximity Impact Damages
- Noise modeling (dBA levels, distance attenuation, receptor sensitivity, rent reduction).
- Dust/air quality (PM2.5/PM10 thresholds, cleaning costs, health impacts).
- Vibration damage (structural vs. cosmetic thresholds).
- Traffic disruption (detour costs, business losses, time-distance modeling).
- Add to TCE valuation for construction period; or separate claim for adjacent properties affected by permanent easement operations.

### Agricultural Land Context

**`agricultural-easement-negotiation-frameworks`** — Farm Operation Psychology and Negotiation
- Farm operation impact assessment (crop cycles, livestock movement, precision agriculture disruption).
- Multi-generational farm psychology (succession planning, emotional attachment, legacy concerns).
- Compensation structure design (one-time vs. recurring, mitigation works vs. cash, future crop loss provisions).

**`cropland-out-of-production-agreements`** — Annual Compensation Alternative
- Ongoing productivity impacts: headlands loss from farming around towers; precision agriculture disruption (GPS-guided automated equipment); field division efficiency losses.
- Per-structure annual payment models (Ontario vs. Alberta approaches).
- Analyzes whether annual payment structure preferred by landowner.

### Legal and Entitlement Framework

**`expropriation-compensation-entitlement-analysis`** — Legal Framework for Compensability
- Market value framework (valuation date, highest and best use, special purchaser exclusion rules).
- Disturbance damages legal tests (causation, reasonableness, foreseeability, but-for test).
- Injurious affection framework (Antrim four-part test for construction vs. permanent impacts).
- Business losses compensability (goodwill generally not compensable).
- **Run first**: ensures valuation methodology aligns with statutory entitlement — prevents valuing components that aren't legally compensable.

### Specialized Infrastructure Analysis

**`right-of-way-expert`** — Corridor-Specific Technical Specifications
- ROW width calculations by voltage/product/mode.
- Access road requirements (permanent vs. temporary, width standards).
- Tower/structure spacing and footprint requirements.
- Maintenance access frequency and restrictions.
- Informs easement area quantification and access frequency assumptions.

**`cost-approach-expert`** and **`income-approach-expert`** — Easement-Holder Perspective
- Cost approach: reproduction/replacement cost of easement rights, installation costs, engineering estimates.
- Income approach: present value of avoided costs vs. alternative routes; revenue generation capability.
- When value to holder exceeds loss to landowner, may inform negotiation range or allocation methodologies.
