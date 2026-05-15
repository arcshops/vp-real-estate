# Cap Rate Tables and Build-Up Components

Reference tables for cap rate selection across income-producing land types. Use alongside `SKILL.md` when justifying capitalization rate selection.

---

## Cap Rates by Property Type

### Telecom Sites

| Site Type | Cap Rate Range | Notes |
|-----------|---------------|-------|
| **Ground lease sites** | 5.5%-7.0% | Stable, creditworthy major-carrier operators |
| **Rooftop sites** | 6.0%-7.5% | Higher risk of carrier relocation |
| **Co-location (shared tower)** | 7.0%-8.5% | Multiple operators, variable occupancy |

### Agricultural Land (reflecting commodity risk)

| Rent Structure | Cap Rate Range | Notes |
|----------------|---------------|-------|
| **Non-indexed fixed rent** | 3.5%-5.0% | Lowest cap rate; predictable cash flow |
| **Partially indexed rent** | 4.0%-6.0% | Base + commodity participation |
| **Fully commodity-indexed rent** | 5.5%-8.0% | Landlord bears commodity risk, demands higher yield |

**Note**: Sales extraction often yields 2-4% cap rates for ag land because purchase prices include capital appreciation expectations beyond NOI yield. Income approach cap rates should reflect NOI-only return; use 4-5% for fixed-rent ag land when extraction shows 2-3%.

### Agricultural Rent Levels by Soil Class

**Row crops** (corn, soybeans, small grains):

| Soil Class | Quality | Rent Range |
|-----------|---------|-----------|
| Class 1 | Prime agricultural | $250-$350/acre/year |
| Class 2 | Good agricultural | $200-$280/acre/year |
| Class 3 | Fair agricultural | $150-$220/acre/year |

**Pasture/hay**:

| Type | Rent Range |
|------|-----------|
| Improved pasture | $100-$150/acre/year |
| Native/marginal pasture | $50-$100/acre/year |

**Formula-based adjustments**:
- **Commodity indexation**: Rent = corn price × conversion factor
  - Example: Rent = Corn Price ÷ 2 (if corn $6/bu, rent = $3/acre — extremely low, reflects commodity risk)
  - More realistic: Base rent + 50% of commodity upside (e.g., $180 base + 50% of upside above $4/bu)

### Ground Leases (Fee Simple Under Long-Term Lease)

| Stream | Typical Cap Rate | Notes |
|--------|------------------|-------|
| Interim contractual rent | 5.0%-6.0% | Lower risk, contractual stream |
| Reversion (long-dated) | 6.5%-8.0% | Higher uncertainty, projection risk |

---

## Band of Investment Components

**Formula**: `Cap Rate = (LTV% × Debt Yield) + (Equity% × Equity Yield)`

**Typical structure for income-producing land**:

| Component | Typical Range |
|-----------|--------------|
| Loan-to-Value | 50%-75% |
| Debt Yield (mortgage rate) | 4%-6% |
| Equity Yield (required return) | 8%-12% |

**Sample assumptions by use**:

| Use | LTV | Debt Yield | Equity Yield | Resulting Cap Rate |
|-----|-----|-----------|--------------|-------------------|
| Telecom ground lease | 60% | 5.5% | 10% | 7.3% |
| Agricultural land | 50% | 6% | 9% | 7.5% |
| Stabilized urban ground lease | 65% | 5.0% | 9% | 6.4% |

---

## Build-Up Method Components

**Formula**: `Cap Rate = Risk-Free Rate + Liquidity Premium + Inflation Premium + Business Risk Premium`

### Risk-free rate
- Government bond yield (10-year Treasury / Canada Bond) matched to holding period
- Example baseline: 4.5%

### Liquidity premium

| Asset Class | Premium |
|------------|---------|
| Telecom sites (multiple operators) | 1.0%-1.5% |
| Stabilized commercial ground lease | 1.5%-2.0% |
| Agricultural land (limited buyers) | 2.0%-3.0% |

### Inflation premium

| Rent Structure | Premium |
|----------------|---------|
| Agricultural land w/ formula-based rent adjustments | 0.5%-1.0% |
| Fixed-rate telecom leases | 1.5%-2.5% |
| Long-dated fixed ground lease | 2.0%-3.0% |

### Business / operational risk

| Use | Premium |
|-----|---------|
| Telecom sites (creditworthy national carriers) | 0.5%-1.0% |
| Stabilized retail ground lease | 1.0%-1.5% |
| Agricultural land (commodity, weather, policy risk) | 2.0%-3.0% |

### Build-up examples

**Telecom ground lease**:
```
Risk-free rate:                 4.5%
Liquidity premium:            + 1.0%
Inflation premium:            + 1.5%
Business risk:                + 0.5%
─────────────────────────────────────
Cap Rate:                     = 7.5%
```

**Agricultural land**:
```
Risk-free rate:                 4.5%
Liquidity premium:            + 2.5%
Inflation premium:            + 1.0%
Business risk:                + 2.5%
─────────────────────────────────────
Cap Rate:                     = 10.5%
```

---

## Market Extraction Reference

**Principle**: Cap Rate = NOI ÷ Sale Price from arm's-length transactions.

**Reliability ranking** (best to worst):
1. **Market extraction** from 3+ recent arm's-length transactions in same use class
2. **Band of investment** when financing terms well-documented
3. **Build-up method** when extraction unavailable; defensible but more subjective

**Example extraction set (telecom)**:

| Transaction | Sale Price | NOI | Cap Rate |
|-------------|-----------|-----|----------|
| Comp 1 | $500,000 | $30,000 | 6.0% |
| Comp 2 | $480,000 | $28,000 | 5.8% |
| Comp 3 | $550,000 | $32,500 | 5.9% |
| **Market range** | — | — | **5.8%-6.0%** |

Conclusion: **5.9% midpoint**.
