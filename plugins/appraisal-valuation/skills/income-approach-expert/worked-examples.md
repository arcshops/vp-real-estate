# Worked Examples: Income Approach Valuations

Full walkthroughs of income approach valuations by land use type. Use alongside `SKILL.md` after establishing market rent and cap rate. Each example shows NOI build, capitalization, sensitivity, and reconciliation with sales comparison.

---

## Example 1: Telecom Ground Lease (Cellular Tower)

**Subject**: Ground lease parcel for cellular tower
- Signed lease with major carrier: $35,000/year
- 20-year term with 2 × 5-year renewal options
- 2% annual escalation
- Carrier maintains tower structure

### Market rent analysis
- Comparable 1: Similar site, same carrier — $32,000/year
- Comparable 2: Shared tower site (more risk) — $28,000/year
- **Conclusion**: Market rent = $34,000/year (accounts for less restrictive operator profile vs. Comp 1)

### Operating expenses
- Property taxes: $1,500/year (rural location)
- Insurance: $600/year
- Maintenance: $800/year
- **Total OpEx**: $2,900/year

### NOI
```
NOI = $34,000 − $2,900 = $31,100/year
```

### Cap rate selection
- Extracted from 2 comparable sales of ground leases: 6.2%, 6.0%
- **Conclusion**: 6.0%

### Land value
```
$31,100 ÷ 0.060 = $518,333
```

### Sensitivity (±0.5% cap rate)
- At 5.5%: $565,455
- At 6.5%: $478,462
- **Value range**: $478,000-$565,000 (most likely $518,000)

### Unique characteristics of telecom sites
- **Stable income**: Multi-decade leases, creditworthy major carriers (Verizon, AT&T, Bell, etc.)
- **Renewal certainty**: Carriers renew because infrastructure already sunk
- **Limited tenant pool**: Few operators, reduces competition for rent
- **Capital improvements**: Carrier builds/maintains towers (landlord receives improved asset post-lease)
- **Location specificity**: Site value tied to network coverage needs (not easily relocated)

---

## Example 2: Agricultural Land (80-Acre Class 2)

**Subject**: 80-acre Class 2 agricultural land

### Market rent analysis
- County extension survey: $240/acre for similar Class 2 land
- Comparable lease 1: $235/acre fixed
- Comparable lease 2: $280/acre (formula: 50% upside commodity participation)
- **Conclusion**: Market rent = $245/acre (conservative, mostly fixed, modest upside potential)

### Per-acre NOI
- Gross rent: $245/acre
- Landlord maintenance (fencing, drainage): $15/acre/year
- Property tax estimate: $10/acre/year
- Management: $5/acre/year
- **Per-acre NOI**: $245 − $30 = $215/acre

### Cap rate selection
- Agricultural land extraction (3 recent sales): 2.8%, 3.1%, 2.9% (range 2.8-3.1%)
- **BUT**: Sales extraction likely reflects capital appreciation expectations
- **Income approach cap rate** (NOI-only): 4.5% (conservative)

### Per-acre value
```
$215/acre ÷ 0.045 = $4,778/acre
```

### Total land value (80 acres)
```
$4,778 × 80 = $382,222
```

### Sales comparison check
- Recent sales: $2,500/acre, $2,600/acre, $2,450/acre
- Average: $2,517/acre
- **Sales value** (80 acres): $2,517 × 80 = $201,360

### Reconciliation
- Income approach (4.5% cap): $382,222
- Sales comparison: $201,360
- Difference: 90% (significant difference indicates different buyer motivations)
- Sales comparison reflects transaction prices (includes capital appreciation expectations, investment activity)
- Income approach (4.5% cap) implies expecting only NOI return, not capital appreciation
- **Reconciled value**: $290,000 (blend, assumes 3% annual appreciation + 4.5% NOI yield)

### Alternative smaller-case agricultural example (80-acre Class 1)

- Market rent: $260/acre/year
- Property size: 80 acres
- Vacancy/non-rent years: 5%
- Effective gross income: $260 × 80 × 0.95 = $19,760/year
- OpEx: property tax $800 + maintenance $1,200 + management $500 = $2,500/year
- NOI: $19,760 − $2,500 = $17,260/year
- At 7.5% cap rate: $17,260 ÷ 0.075 = **$230,133 (~$2,877/acre)**

### Unique characteristics of agricultural land
- **Commodity price exposure**: Rent tied to (or indexed to) crop prices, weather
- **Annual renewal**: Most ag leases year-to-year with renewal
- **Multiple buyer pool**: Higher transaction volume, more market comparables
- **Capital appreciation**: Land value typically exceeds NOI yield (expect 2-4% cap rates)
- **Government programs**: Crop insurance, commodity payments, conservation programs

---

## Example 3: Ground Lease (Shopping Center, 25-Year Remaining)

**Subject**: Fee simple interest in land under 25-year shopping center lease

### Lease terms
- Annual rent: $50,000 (fixed, no escalation)
- Remaining term: 25 years
- Tenant: Established retail operator (good credit)
- Upon expiration: Fee owner regains clear possession of land

### Fee interest formula
```
Fee Value = [Interim Rent ÷ Cap Rate] + [Reversion Value ÷ (1 + Cap Rate)^n]
```

### Interim rent capitalization
- Cap rate: 5.5% (lower risk, contractual rent)
- Value of interim rent stream: $50,000 ÷ 0.055 = $909,091

### Reversion value projection
- Current land value (with lease): $909,091
- Expected land appreciation: 2.5% annually for 25 years
- Multiplier: (1.025)^25 = 1.85
- Projected fee value at lease end: $909,091 × 1.85 = $1,681,818

### Discounting reversion
- Discount rate for reversion (higher risk, 25-year projection): 6.5%
- Reversion discount factor: 1 ÷ (1.065)^25 = 0.1842
- Present value of reversion: $1,681,818 × 0.1842 = $309,788

### Fee interest value
```
Fee Value = $909,091 + $309,788 = $1,218,879
```

### Unique characteristics of ground leases
- **Dual interests**: Fee owner and leaseholder have separate valuations
- **Fee interest valuation**: Reversion value + interim rent capitalized
- **Leasehold interest valuation**: Rent differential (market rent vs. lease rent) capitalized
- **Lease length**: Remaining lease term crucial (20-year vs. 99-year drives reversion materiality)
- **Renewal/reversion**: At lease end, does fee holder regain possession of improvements?

---

## Example 4: Perpetual Easement Income (Transmission Corridor)

**Subject**: Perpetual transmission easement with agricultural income loss

- Agricultural productivity loss: 20% of land value = 20% of $250/acre = $50/acre/year
- Cap rate for perpetual easement: 4.5% (very long-term, low risk)
- **Easement value**: $50 ÷ 0.045 = $1,111/acre

---

## Sensitivity Analysis Patterns

### Single-variable sensitivity (telecom base case: $32,000 rent, $5,600 OpEx, 6.0% cap → $440,000)

**Varying cap rate**:

| Cap Rate | NOI | Land Value | % Change |
|----------|-----|-----------|----------|
| 5.0% | $26,400 | $528,000 | +20.0% |
| 5.5% | $26,400 | $480,000 | +9.1% |
| 6.0% | $26,400 | $440,000 | — |
| 6.5% | $26,400 | $406,154 | -7.7% |
| 7.0% | $26,400 | $377,143 | -14.3% |

**Varying market rent**:

| Market Rent | NOI | Land Value | % Change |
|------------|-----|-----------|----------|
| $28,000 | $22,400 | $373,333 | -15.2% |
| $30,000 | $24,400 | $406,667 | -7.6% |
| $32,000 | $26,400 | $440,000 | — |
| $34,000 | $28,400 | $473,333 | +7.6% |
| $36,000 | $30,400 | $506,667 | +15.2% |

**Varying operating expense ratio**:

| OpEx Ratio | NOI | Land Value | % Change |
|-----------|-----|-----------|----------|
| 15% | $27,200 | $453,333 | +3.0% |
| 17.5% | $26,400 | $440,000 | — |
| 20% | $25,600 | $426,667 | -3.0% |
| 25% | $24,000 | $400,000 | -9.1% |

**Sensitivity ranking** (most → least impact on value):
1. Cap rate (±0.5% → ±8-10% value change)
2. Market rent (±6.3% → ±7.6% value change)
3. Operating expense ratio (±2.5 pts → ±3-9% value change)

### Multi-variable scenario (agricultural land)

**Base** (most likely):
- Market rent: $260/acre, Cap rate: 7.5% → **$230,133**

**Conservative** (commodity downturn):
- Market rent: $240/acre, Cap rate: 8.0%
- NOI: ($240 × 80 × 0.95) − $2,500 = $16,080
- Value: $16,080 ÷ 0.080 = **$201,000 (−12.6%)**

**Optimistic** (commodity recovery, improved appetite):
- Market rent: $280/acre, Cap rate: 7.0%
- NOI: ($280 × 80 × 0.95) − $2,500 = $19,840
- Value: $19,840 ÷ 0.070 = **$283,429 (+23.2%)**

| Scenario | Value | % of Base |
|----------|-------|----------|
| Conservative | $201,000 | 87% |
| Most likely | $230,133 | 100% |
| Optimistic | $283,429 | 123% |

**Range**: $201,000-$283,429. **Concluded value**: $230,000 (most likely scenario).

### Range approach (when cap rate uncertain)

If cap rate justified as 5.8%-6.2% on $30,000 NOI:
- Low cap rate (5.8%): $517,241
- High cap rate (6.2%): $483,871
- **Range**: $484,000-$517,000
- **Concluded value**: $500,000 (midpoint)

---

## Reconciliation Patterns with Sales Comparison

### Scenario 1: Income approach lower than sales comparison
- Buyers expect capital appreciation beyond NOI
- Common in: Agricultural land, developing markets, land held for speculation
- Reconciliation: If sales comparison supported by 3+ recent sales, typically more reliable

### Scenario 2: Income approach higher than sales comparison
- Market undervalues income-producing potential, or comparable sales include non-income-producing attributes
- Common in: Illiquid markets, distressed sales, special-purpose land
- Reconciliation: Investigate why comparable sales price below NOI capitalization

### Example reconciliation (80-acre Class 1 ag land)

- Income approach: $230,133 ($2,877/acre)
- Sales comparison: $215,000 ($2,688/acre, midpoint of $180K-$250K)
- Difference: +$15,133 (+7.0%)
- **Reconciled value**: $220,000 (blend of both, reflecting some capital appreciation expectation beyond NOI)
