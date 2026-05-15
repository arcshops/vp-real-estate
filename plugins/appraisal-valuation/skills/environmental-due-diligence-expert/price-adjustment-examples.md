# Price Adjustment & Use Case Examples

Worked examples of acquisition price adjustments for environmental risk across low-, medium-, and high-severity scenarios.

## Price Adjustment Framework

### Price Adjustment Formula
```
Adjusted Price = Base Price - Environmental Cost + Timing Adjustment

Where:
  Base Price = Contract purchase price
  Environmental Cost = (Remediation + Professional Services) × Risk Factor
  Timing Adjustment = Cost of delay to project timeline
```

### Environmental Discount Calculation

**Step 1: Estimate Cleanup Cost** (using Cost Estimation Framework)
- Expected scenario: $X
- Conservative scenario: $Y
- Use Expected cost minus contingency for negotiation

**Step 2: Calculate Risk Factor**
- Site complexity (regulatory approval ease)
- Cleanup technology feasibility
- Remediation timeline impact
- Factor: 0.8 to 1.25 (0.8 = high confidence, 1.25 = high uncertainty)

**Step 3: Calculate Environmental Discount**
```
Environmental Discount = Estimated Cost × Risk Factor × Discount Rate

Discount Rate:
  - 85% (for low risk, straightforward cleanup): Discount 85% of cost
  - 75% (for medium risk, some complexity): Discount 75% of cost
  - 65% (for high risk, regulatory uncertainty): Discount 65% of cost

Rationale: Buyer should discount cleanup costs because:
  - Estimates may be overstated (early-stage assumptions)
  - Buyer may have operational synergies (in-house expertise)
  - Buyer can phase cleanup over time (cost of capital savings)
  - Certainty premium worth something
```

## Worked Examples

### Example 1: Low Risk Petroleum Site
```
Phase II Result: Petroleum contamination, 2,000 cy soil,
                 Tier 1 standard applies

Cleanup Estimate:
  - Phase II already completed: $0
  - Excavation/Disposal: $350,000
  - Professional Services: $20,000
  - Post-Rem Sampling: $10,000
  Expected Cost: $380,000

Risk Factor: 0.95 (low uncertainty, straightforward excavation)
Risk-Adjusted Cost: $380,000 × 0.95 = $361,000

Discount Rate: 85% (low regulatory complexity)
Environmental Discount: $361,000 × 0.85 = $306,850

Price Adjustment: REDUCE PRICE BY $306,850

Negotiation Range:
  - Buyer's opening: Reduce by $400,000
  - Seller's opening: Reduce by $200,000
  - Likely outcome: Reduce by $300,000-$350,000
```

### Example 2: Medium Risk with Tier 2 Analysis Required
```
Phase II Result: Petroleum + metals, groundwater exceedance,
                 Tier 2 Risk Assessment required

Cleanup Estimate:
  - Phase II completed: $0
  - Risk Assessment: $30,000
  - Remediation (expected): $600,000 (phased over 18 months)
  - Long-term monitoring: $30,000/year × 5 years = $150,000
  - Professional Services: $50,000
  Expected Cost: $830,000

Additional considerations:
  - 12-month MOE approval timeline
  - Project delay: 12 months
  - Cost of delay (delay to development): $500,000+

Total Environmental Impact: $1,330,000

Risk Factor: 1.1 (medium uncertainty, regulatory approval needed)
Risk-Adjusted Cost: $830,000 × 1.1 = $913,000

Discount Rate: 75% (medium regulatory complexity)
Environmental Discount: $913,000 × 0.75 = $684,750

PLUS Delay Cost (present value, 12 months at 5% WACC): $50,000

Total Price Adjustment: REDUCE PRICE BY $734,750

Negotiation Range:
  - Buyer's opening: Reduce by $900,000
  - Seller's counter: Reduce by $400,000
  - Likely outcome: Reduce by $650,000-$800,000
```

### Example 3: High Risk — Seller Remediation Required
```
Phase II Result: SEVERE: Heavy metals (lead >5,000 mg/kg),
                 Groundwater exceed by 100x, adjacent property impact

Cleanup Estimate:
  - Phase II, Risk Assessment, regulatory coordination: $75,000
  - Remediation (conservative): $2,000,000
  - Long-term monitoring (10 years): $200,000
  - Potential third-party claims: $500,000 (uncertain)
  Expected Cost: $2,775,000

Risk Factor: 1.3 (high uncertainty, regulatory action likely)
Risk-Adjusted Cost: $2,775,000 × 1.3 = $3,607,500

This exceeds typical discount rate thresholds.

Negotiation Options:
  Option 1: Reduce Price: $2.5-3.0M (not fully covering risk)
  Option 2: Seller Remediation: Seller remediates pre-closing,
            Buyer receives clean property with RSC
  Option 3: Post-Closing Holdback: Buyer retains $3-4M escrow
            for remediation, Seller guarantees completion
  Option 4: REJECT: Contamination too severe/risky

Recommendation: OPTIONS 2 or 3 (transfer risk back to seller)
```

## Extended Use Cases

### Use Case 1: Phase I ESA Review — Petroleum Service Station

**Scenario**: Buyer acquiring 15,000 sf service station property. Phase I ESA completed shows property was service station for 40 years (1970-2010), no prior Phase II, petroleum staining noted in parking lot.

**Analysis**:
```
Phase I Finding: REC identified (historical petroleum use, visible staining)
Risk Level: MEDIUM (petroleum service station, but closed >10 years)

Phase II Recommended: YES
Likely Finding: Soil petroleum contamination, probably <5,000 cy

Estimated Cleanup:
  - Phase II ESA: $6,000
  - Soil sampling (20 borings): $10,000
  - Excavation/disposal (3,000 cy @ $75): $225,000
  - Professional services: $25,000
  - Post-rem sampling: $8,000
  Total: $274,000

Risk Factor: 0.95 (petroleum straightforward to remediate)
Risk-Adjusted Cost: $260,300

Discount Rate: 85% (Tier 1 standard, no regulatory complexity)
Environmental Discount: $221,255

RECOMMENDATION:
  1. Make offer conditional on Phase II ESA
  2. Use Phase II results to finalize price
  3. If Phase II confirms estimate, reduce price by $200,000-$250,000
  4. If Phase II worse than expected, re-negotiate or withdraw
  5. Request seller indemnity for 3 years, $25K threshold
```

### Use Case 2: Phase II ESA Analysis — Manufacturing Property

**Scenario**: Buyer acquiring 50,000 sf former manufacturing facility. Phase I shows REC (manufacturing 1950-2000). Phase II completed shows soil metals exceedance (lead 1,200 mg/kg vs. 500 standard), no groundwater exceedance, contamination deep (8-15 feet). Tier 1 standard applies.

**Analysis**:
```
Phase II Finding:
  - Soil metals exceedance, Tier 1 applies
  - Estimated 8,000 cy contaminated soil (8-15 feet depth)
  - Lead concentration 2-3x standard
  - Deep contamination = lower exposure risk

Cleanup Approach: Excavation (soil removal) most cost-effective

Estimated Cleanup:
  - Excavation (8,000 cy @ $40): $320,000
  - Disposal (8,000 cy @ $90): $720,000
  - Backfill (8,000 cy @ $20): $160,000
  - Professional services: $40,000
  - Post-rem sampling: $15,000
  - Contingency (20%): $251,000
  Total: $1,506,000

Tier 2 Required: NO (Tier 1 applies)
Timeline: 6-9 months (straightforward excavation)

Risk Factor: 1.0 (clear path, well-understood metals remediation)
Risk-Adjusted Cost: $1,506,000

Discount Rate: 85% (no regulatory complexity beyond standard approval)
Environmental Discount: $1,280,100

RECOMMENDATION:
  1. Reduce offer price by $1,200,000-$1,350,000
  2. Request 5-year seller indemnity capped at $500,000
  3. Holdback $400,000 in escrow until remediation complete
  4. Require post-closing Phase I to confirm no additional contamination
  5. Negotiate timeline: Seller to complete remediation within 9 months
```

### Use Case 3: Tier 2 Risk Assessment — Chlorinated Solvent Contamination

**Scenario**: Buyer acquiring 20,000 sf former electronics manufacturing facility. Phase II shows TCE (trichloroethylene) in groundwater at 50 µg/L (standard: 5 µg/L, 10x exceedance). Property near municipal water source, 500 meters down-gradient.

**Analysis**:
```
Phase II Finding:
  - Groundwater exceedance (TCE 10x standard)
  - Proximity to water source (HIGH RISK)
  - Potential third-party impact (neighbors, water utility)

Tier 2 Analysis Required: YES
Regulatory Complexity: HIGH
Risk Level: HIGH

Phase II Result:
  - Soil exceedance (TCE, vinyl chloride breakdown products)
  - Groundwater plume extent estimated (10+ acre plume)
  - Vapor intrusion testing required

Risk Assessment Scope:
  - Human health exposure assessment
  - Groundwater pathway analysis (migration to water source)
  - Vapor intrusion modeling
  - Recommended remediation (likely in-situ treatment, 10+ years)

Timeline:
  - Risk Assessment preparation: 8-10 weeks
  - MOE review period: 12-16 weeks
  - Remediation approval: 4-8 weeks
  - Remediation startup: 6-12 months
  - Remediation duration: 5-15 years (pump & treat)
  Total MOE approval: 12-24 months

Cleanup Cost Estimate (Conservative):
  - Risk Assessment: $40,000
  - Site pilot studies (treatability): $50,000
  - Remediation system installation: $300,000
  - Remediation operation (10 years @ $40K/year): $400,000
  - Monitoring (10 years @ $30K/year): $300,000
  - Professional oversight: $75,000
  Total: $1,165,000

Risk-Adjusted Cost: $1,165,000 × 1.3 = $1,514,500

Discount Rate: 65% (high regulatory complexity, third-party impact)
Environmental Discount: $984,425

Additional Risk:
  - Potential third-party claims (water utility, neighbors)
  - Regulatory enforcement risk (MOE action)
  - Long-term operational risk (24-year monitoring commitment)

RECOMMENDATION:
  Option 1 - Price Reduction + Indemnity:
    - Reduce price by $1,000,000
    - 7-year seller indemnity, $2,000,000 cap, $50,000 threshold
    - 7-year cost-cap insurance policy ($500,000 excess)
    - Buyer retains remediation risk
    Risk to Buyer: Moderate

  Option 2 - Seller Remediation + Hold Back:
    - Reduce price by $600,000
    - Seller responsible for Tier 2 approval and remediation startup
    - Buyer retains long-term monitoring (10-year commitment)
    - $1,500,000 escrow for remediation costs
    Risk to Buyer: Lower

  Option 3 - REJECT or Renegotiate:
    - Environmental risk too high for this property use
    - TCE groundwater near water source = regulatory scrutiny
    - 15-year remediation timeline = long-term liability
    - Consider alternative acquisition
    Recommendation: Unless strong project fundamentals, AVOID
```

### Use Case 4: HREC — Former Dry Cleaner

**Scenario**: 5,000 sf retail/office space, formerly dry cleaning business 1980-1995, now general office use. Phase I shows dry cleaning history and prior solvent contamination reports (1990s).

**Phase I Findings**:
- Historical REC: Dry cleaning operations (historical use, business closed 1995)
- Prior site records: Spill report 1992 (petroleum, cleaned up)
- No current evidence of contamination
- Prior Phase II ESA from 1995 (not available, original lender requirement)
- No subsequent violations or reports
- **Result: HREC IDENTIFIED (no current REC)**

**Analysis**:
```
Environmental Risk Level: LOW-MEDIUM
Phase II ESA Required: Recommended (data gap — 1995 Phase II not available)

Cost for Phase II ESA:
  - New Phase II ESA (4 borings, soil/groundwater): $8,000

Likely Result: Non-exceedance or minor exceedance
  - If non-exceedance: Proceed, minimal adjustment
  - If minor (< 2x standard): Excavate ~500 cy, cost ~$50-75K

Estimated Price Impact: $0-$50,000 discount
Timeline Impact: 4-8 weeks for Phase II, no delay to occupancy

Recommendation:
  1. Commission Phase II ESA as due diligence
  2. If non-exceedance: No price adjustment
  3. If minor exceedance: Reduce price by $40,000-$60,000
  4. If significant exceedance: Re-evaluate, may require Tier 2
  5. Historical dry cleaning = typical REC, should resolve easily
```

## Integration with Settlement & Expropriation

### Settlement Analysis Example
```
Phase II shows significant contamination, cleanup estimate $1.5M
Seller disputes cost estimate, claims $500K sufficient

Options:
  1. Accept $500K adjustment (vs. $1.5M estimated)
  2. Seller provides indemnity capped at $750K
  3. Use escrow approach with phased release

Settlement Analysis:
  - Probability seller's estimate correct: 20%
  - Probability buyer's estimate correct: 60%
  - Probability intermediate ($900K): 20%

  Expected outcome: (0.20 × $500K) + (0.60 × $1.5M) + (0.20 × $900K)
                  = $100K + $900K + $180K = $1.18M discount
```

### Expropriation Compensation Example
```
Expropriation/Negotiation Scenario:
  - Market value (uncontaminated): $5,000,000
  - Contamination cleanup cost: $1,500,000
  - Risk adjustment (75% of cost): $1,125,000

  Adjusted fair market value = $5,000,000 - $1,125,000 = $3,875,000

  Compensation to owner limited to $3,875,000
```
