# Worked Examples — Easement Valuation Methods

Detailed walkthroughs for each valuation method referenced in `SKILL.md`. Use these as templates when documenting your own engagement files.

---

## 1. Income Capitalization — Agricultural Land

**Subject**: 230 kV transmission easement crossing prime farmland.

| Item | Value |
|------|-------|
| Fee simple land value | $10,000/acre (Class 1 soil) |
| Annual agricultural rent | $300/acre |
| Productivity loss from easement (towers + restricted planting) | 20% |
| Annual rent loss | $300 × 20% = $60/ac/yr |
| Capitalization rate (perpetual, low risk) | 4.5% |
| **Easement value** | **$60 ÷ 0.045 = $1,333/acre (13.3% of fee)** |

**Methodology steps**:
1. Determine annual rent for comparable agricultural land without easement.
2. Calculate percentage loss of productivity (tower footprints, restricted areas, field division).
3. Apply loss percentage to annual rent.
4. Capitalize at risk-adjusted rate.

---

## 2. Before/After vs. Take-Plus-Damages — 230 kV Across 100-Acre Farm

Two conceptual frameworks for easement valuation that are **mathematically equivalent** when properly applied.

| Component | Before-and-After | Take-Plus-Damages |
|-----------|------------------|-------------------|
| Property value before easement | $1,200,000 | — |
| Property value after easement | -$1,020,000 | — |
| Land directly encumbered (15 acres) | — | $27,000 (15% of $12K/ac fee) |
| Severance damages (field division, access impairment) | — | $153,000 |
| **Total compensation** | **$180,000** | **$180,000** |

**When to use each**:
- **Before-and-After**: Preferred in federal acquisitions (Yellow Book), Ontario expropriations, most USPAP/CUSPAP assignments — provides holistic impact analysis.
- **Take-Plus-Damages**: Useful for client communication (itemizes components clearly); required by some state jurisdictions; helpful when severance damages are complex and need separate quantification.

For severance damages quantification, see the **`severance-damages-quantification`** skill.

---

## 3. Paired Sales Extraction — Transmission Easement

**Sale 1 (no easement)**:
- 100 acres, Class 1 agricultural, highway frontage
- Sale date: June 2024
- Sale price: $1,200,000 ($12,000/acre)

**Sale 2 (with 230 kV easement)**:
- 105 acres, Class 1 agricultural, highway frontage, 230 kV easement crossing 15 acres
- Sale date: September 2024
- Sale price: $1,134,000 ($10,800/acre)

**Analysis**:
- Size adjustment: 105 vs. 100 acres (-5% on Sale 2 for being 5% larger).
- Time adjustment: 3 months later (+2% if market trending).
- After adjustments: Sale 2 → $10,600/acre.
- **Percentage difference**: ($12,000 - $10,600) ÷ $12,000 = **11.7% impact**.

**Easement-specific implied percentage**:
- Easement covers 15 acres of 105-acre parcel (14.3% of total).
- Observed total-property impact: 11.7%.
- Implied loss on affected acreage: 11.7% ÷ 14.3% = **~82% of fee** on the 15 affected acres.

### Adjustment Grid

| Characteristic | Sale 1 (Subject) | Sale 2 (Comp) | Adjustment to Sale 2 |
|----------------|------------------|---------------|----------------------|
| Sale price | — | $1,134,000 | — |
| Property rights | Fee simple | Fee simple | $0 |
| Financing | Cash | Cash | $0 |
| Conditions | Arm's length | Arm's length | $0 |
| Date of sale | Current | 3 mo ago | +2% ($22,680) |
| Location | Highway frontage | Highway frontage | $0 |
| Size | 100 acres | 105 acres | -5% (-$57,890) |
| Soil quality | Class 1 | Class 1 | $0 |
| Easement | None | 230 kV, 15 ac | TBD |
| **Adjusted price** | — | **$1,098,790** | **($10,465/ac)** |

**Easement value extraction**:
- Subject (no easement): $12,000/ac × 100 ac = $1,200,000
- Comparable adjusted: $10,465/ac × 105 ac = $1,098,790
- If comparable had no easement: $12,000/ac × 105 ac = $1,260,000
- **Easement impact**: $1,260,000 - $1,098,790 = **$161,210**
- **Percentage of fee on affected acreage**: $161,210 ÷ ($12,000 × 15 ac) = **89.6%**
- Or simplified: **12.8% of total property value** ($161,210 ÷ $1,260,000)

### Statistical Validation via Regression

When 10+ paired sales are available, fit hedonic regression to isolate easement impact:

**Model**:
```
Sale Price = β₀ + β₁(Acres) + β₂(Soil Class) + β₃(Frontage)
           + β₄(Easement Presence) + β₅(Easement Acres) + ε
```

**Variable definitions**:
- Sale Price — dependent variable
- Acres — total property size
- Soil Class — agricultural rating (1-7)
- Frontage — linear feet of highway frontage
- Easement Presence — dummy (1 if any easement, 0 otherwise)
- Easement Acres — acres affected by easement
- ε — error term

**Example output**:
- β₄ = -$15,000 (fixed discount for easement presence)
- β₅ = -$1,800/acre (each acre of easement reduces value by $1,800)
- Fee simple value: $12,000/acre
- **Implied percentage**: $1,800 ÷ $12,000 = **15% of fee**

**Statistical tests**:
- R² > 0.70 (model explains 70%+ of price variation)
- Coefficient p-value < 0.05 (95% confidence)
- Coefficient sign: negative on easement variables
- Multicollinearity: VIF < 10

**Validation steps**:
1. Run regression on paired-sales dataset.
2. Check R², coefficient significance and signs.
3. Extract percentage from β₅.
4. Compare to published percentage-of-fee ranges (10-25% for transmission).
5. Reconcile against income capitalization approach.
6. Document methodology and confidence level.

---

## 4. Temporary Construction Easement (TCE)

### 4a. Fair Market Rental Method — Agricultural TCE

- 5 acres affected for 180 days (6 months)
- Annual crop rent for comparable land: $300/ac/yr
- Rental calculation: 5 ac × $300 × (180/365) = **$740**
- Crop loss (spring seeding disrupted, full season lost): **$1,500**
- Restoration (topsoil replacement, re-leveling, re-seeding): **$3,000**
- **Total TCE compensation: $5,240**

### 4b. Rate-of-Return Method — Industrial TCE

**Formula**:
```
TCE Value = (Affected Fee Simple Value × Annual Rate × Days/365)
          + Physical Damage Restoration Costs
          + Business/Operational Losses
```

- 2 acres for 90 days (pipeline construction staging area)
- Fee simple value: $200,000/ac → $400,000 for 2 ac
- Annual rate: 10% (industry standard)
- Rental value: $400,000 × 10% × (90/365) = **$9,863**
- Site restoration (grading, asphalt repair, landscaping): **$15,000**
- Business interruption (forklift access to warehouse blocked): **$8,000**
- **Total TCE compensation: $32,863**

### 4c. Duration-Based Adjustments

**Short-duration (<30 days)**:
- Daily rate may exceed prorated annual rate due to fixed setup/disruption costs.
- Minimum compensation often applies regardless of duration.
- Example: $500-$2,000/day for industrial site access.

**Medium-duration (3-12 months)**:
- Standard prorated calculation using annual rate.
- Most common for pipeline construction, transmission installation.
- Restoration typically feasible and expected.

**Long-duration (1-3 years)**:
- May approach permanent easement value if restoration uncertain.
- Consider option to convert to permanent easement.
- Apply annual escalation (typically 2-4%/yr).

**3-year TCE with 3% escalation example**:
- Year 1: $400,000 × 10% = $40,000
- Year 2: $400,000 × 10% × 1.03 = $41,200
- Year 3: $400,000 × 10% × 1.03² = $42,436
- **Total: $123,636** (vs. $120,000 without escalation)

### 4d. Additional Compensation Components

**Physical damage and restoration**:
- Soil compaction from heavy equipment (remediation required)
- Vegetation removal and restoration (trees, shrubs, turf)
- Drainage disruption repair (culverts, ditching, grading)
- Fencing replacement (temporary removal for access)
- Pavement/hardscape repair (asphalt, concrete, interlocking)

**Business and operational losses**:
- Lost production during construction period
- Equipment relocation costs
- Alternative access costs (longer routes, detours)
- Customer/employee inconvenience
- Inventory disruption (cannot receive/ship goods normally)

For noise/dust/vibration/traffic impacts during construction, see **`injurious-affection-assessment`** skill.

---

## 5. Reconciliation — 230 kV Easement, 15 Acres Class 1 Agricultural

| Approach | Calculation | Indicated Value |
|----------|-------------|-----------------|
| **Percentage of fee** | 15 ac × $12,000/ac × 15% (market-extracted) | $27,000 |
| **Income capitalization** | 15 ac × $60/ac annual loss ÷ 4.5% cap | $20,000 |
| **Before/after paired sales** | One paired-sale analysis (adjusted) | $24,000 |

**Weighting**:

| Approach | Weight | Weighted |
|----------|--------|----------|
| Percentage of fee | 40% | $10,800 |
| Income cap | 30% | $6,000 |
| Before/after | 30% | $7,200 |
| **Weighted average** | | **$24,000** |

**Range**: $20,000 (low) — $27,000 (high)

**Reasoning**: Percentage-of-fee given highest weight due to strong market data (8 comparable easement sales). Income approach lower due to conservative cap rate (4.5% may be too high for perpetual government easement; 4.0% more appropriate, which would yield $22,500). Before/after provides good mid-range support. Final value favors upper end ($25,000-$27,000) due to market evidence supporting 15-18% percentage of fee for 230 kV easements on prime agricultural land.

**Sensitivity check**:
- Cap rate at 4.0%: Income approach → $22,500 (closer to consensus)
- Percentage at 18%: Percentage-of-fee → $32,400 (upper limit)
- Reasonable range accounting for sensitivity: **$22,000 - $32,000**
- **Final reconciliation within validated range: $25,000**

---

## 6. Comprehensive Transmission Line Acquisition Workflow

Sequence for a full transmission easement engagement, integrating related skills:

1. **Legal entitlement** (`expropriation-compensation-entitlement-analysis`) — confirm statutory authority and compensable components.
2. **Technical specifications** (`right-of-way-expert`) — define easement area, access requirements, restrictions.
3. **Permanent easement valuation** (this skill) — percentage of fee, income capitalization, before/after.
4. **Severance damages** (`severance-damages-quantification`) — access loss, field division impacts to the 85-acre remainder.
5. **TCE valuation** (this skill, §4) — value 6-month construction easement using rate-of-return method.
6. **Construction impacts** (`injurious-affection-assessment`) — noise, dust, vibration during installation.
7. **Agricultural impacts** (`cropland-out-of-production-agreements`) — annual compensation vs. lump-sum for ongoing tower impacts.
8. **Negotiation strategy** (`agricultural-easement-negotiation-frameworks`) — structure offer considering farm succession and compensation preferences.
9. **Reconciliation** (this skill, §5) — final compensation package integrating all components.

**Total Compensation** = Permanent Easement Value + Severance Damages + TCE Value + Construction Impacts ± Negotiated Adjustments
