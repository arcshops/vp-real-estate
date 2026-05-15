# Easement Compensation Tables by Corridor Type

Detailed base-percentage tables and adjustment factors for each specialized calculator. Used by the calculators in this skill directory (`hydro_easement_calculator.py`, `rail_easement_calculator.py`, `pipeline_easement_calculator.py`). Values are MARKET-ALIGNED based on IRWA standards (25-50% range), professional research, and documented market evidence.

## 1. Hydro / Utility Transmission Easements

**Calculator**: `hydro_easement_calculator.py`
**Required parameter**: `voltage_kv`
**Default reconciliation weights**: 50% percentage of fee / 30% income cap / 20% before-after
**Use for**: Overhead transmission lines, hydro corridors, electrical utility easements
**Research basis**: IRWA 25-50% permanent easement range, EMF perception studies

### Voltage-Based Base Percentages (25-40% range)

| Voltage | Base % | Typical Range |
|---------|--------|---------------|
| 500 kV  | 37.5%  | 35-40% |
| 230 kV  | 35.0%  | 32-38% |
| 115 kV  | 32.0%  | 28-36% |
| 69 kV   | 28.0%  | 25-31% |
| <69 kV  | 25.0%  | minimum market range |

### Domain-Specific Adjustments

| Factor | Adjustment | Notes |
|--------|------------|-------|
| EMF concern (230 kV) | +4% | Research supports +3-5% public perception |
| EMF concern (500 kV) | +5% | |
| Tower placement | +1% per tower (max +5%) | Permanent structural impact |
| Vegetation management | +2.5% | Ongoing restrictions |
| Access road | +2% | Permanent land take |
| Building proximity (<50 m, ≥230 kV) | +4% | Marketability impact |

### Legacy Voltage/Width Ranges (Percentage of Fee Method)

For non-calculator quick reference, historical published ranges are:

| Voltage | Width | % of Fee |
|---------|-------|----------|
| 69 kV   | 20-30 m  | 10-15% |
| 115 kV  | 30-40 m  | 12-18% |
| 230 kV  | 45-60 m  | 15-20% |
| 500 kV  | 80-100 m | 20-25% |

Note: Legacy ranges (10-25%) reflect older market studies; calculator base percentages (25-40%) reflect modern IRWA-aligned market evidence including EMF perception research.

---

## 2. Rail / Transit Corridor Easements

**Calculator**: `rail_easement_calculator.py`
**Required parameter**: `rail_type`
**Optional parameter**: `rail_alignment` (defaults to `at_grade`)
**Default reconciliation weights**: 50% percentage of fee / 20% income cap / 30% before-after
**Use for**: Rail corridors, transit alignments, elevated guideways, subway tunnels
**Research basis**: Rail vibration studies (44% exceed limits), noise impact analysis, subsurface market evidence

### Rail Type Base Percentages (28-40% range)

| Rail Type | Base % | Typical Range | Drivers |
|-----------|--------|---------------|---------|
| Heavy rail freight   | 40.0% | 38-45% | Hazmat, vibration, safety |
| Heavy rail passenger | 38.0% | 35-42% | High frequency, noise |
| Subway surface       | 37.0% | 35-40% | Very frequent service |
| Light rail           | 35.0% | 32-38% | Moderate impact |
| Bus rapid transit    | 28.0% | 25-32% | Lower impact |

### Domain-Specific Adjustments

| Factor | Adjustment | Notes |
|--------|------------|-------|
| Alignment: elevated | +3% | Visual / noise propagation |
| Alignment: at-grade | baseline | |
| Alignment: trench | -3% | Reduced surface impact |
| Alignment: subway / tunnel | -8% | Subsurface only |
| Train frequency 20-50/day | +3% | "Significantly negative impact" |
| Train frequency >50/day | +5% | |
| Grade crossing safety | +1% per crossing (max +3%) | |
| Vibration <30 m (heavy rail) | +5% | Documented price depreciation |
| Vibration <50 m (any rail) | +3% | |
| No noise barriers | +4% | 31% of projects exceed noise limits |
| Extended hours (≥20 h/day) | +2.5% | Sleep disruption |

---

## 3. Pipeline Corridor Easements

**Calculator**: `pipeline_easement_calculator.py`
**Required parameter**: `pipeline_type`
**Default reconciliation weights**: 45% percentage of fee / 30% income cap / 25% before-after
**Use for**: Pipeline easements, subsurface corridors, utility ROW
**Research basis**: IRWA 61.4% weighted impact for 16" pipeline, subsurface market evidence (typical -50%)

### Pipeline Type Base Percentages (25-40% range)

| Pipeline Type | Base % | Typical Range | Drivers |
|---------------|--------|---------------|---------|
| Crude oil transmission     | 38.0% | 35-42% | Environmental risk |
| Natural gas transmission   | 35.0% | 32-39% | Explosion risk |
| Natural gas distribution   | 28.0% | 25-32% | Lower pressure |
| Water transmission         | 26.0% | 25-29% | Lower risk |
| Sewer                      | 25.0% | minimum market range | Gravity flow |

### Domain-Specific Adjustments

| Factor | Adjustment | Notes |
|--------|------------|-------|
| High pressure (>1000 psi) | +4% | Rupture risk |
| Very large diameter (>1000 mm) | +5% | Massive ROW impact |
| Large diameter (750-1000 mm) | +3% | Wider restrictions |
| Burial depth shallow (<1 m) | +3% | Surface restrictions |
| Burial depth deep (>3 m) | -5% | Surface use feasible |
| Access road | +2.5% | Ongoing disruption |
| Water proximity, crude oil <100 m | +4% | Environmental stigma |
| Water proximity, any product <100 m | +2% | |
| Aging (>40 years) | +2.5% | Liability concerns |
| High consequence area (Class 3/4) | +3% | Property value impact |

### Legacy Pipeline Ranges (Percentage of Fee Method)

For non-calculator quick reference:

| Product | Width | % of Fee |
|---------|-------|----------|
| Natural gas (low pressure)  | 10-15 m | 15-20% |
| Natural gas (high pressure) | 20-30 m | 20-25% |
| Petroleum products          | 30-40 m | 25-30% |
| Hazardous materials         | wider buffers | 30%+ |

---

## 4. Access Easements (Non-Calculator Reference)

**Range**: 5-15% of fee

| Use Case | % of Fee |
|----------|----------|
| Infrequent access (utility meter reading) | 5-8% |
| Regular access (shared driveway) | 8-12% |
| Exclusive access (ROW to landlocked parcel) | 12-15% |

**Adjustment factors**: width and location (wider/bisecting = higher), exclusivity (exclusive use = higher), perpetual vs. temporary, surface treatment (paved > gravel/grass).

---

## 5. Income Capitalization Reference Tables

### Agricultural Rent by Soil Class

**Row crops (corn, soybeans)**:

| Soil Class | Annual Rent | Cap Rate | Easement Value |
|------------|-------------|----------|----------------|
| Class 1 (prime) | $250-$350/ac/yr | 4-5% | $5,000-$8,750/ac |
| Class 2 (good)  | $200-$280/ac/yr | 4-5% | $4,000-$7,000/ac |
| Class 3 (fair)  | $150-$220/ac/yr | 5-6% | $2,500-$4,400/ac |

**Pasture / hay**:

| Type | Annual Rent | Cap Rate | Easement Value |
|------|-------------|----------|----------------|
| Improved pasture | $100-$150/ac/yr | 5-6% | $1,667-$3,000/ac |
| Native pasture   | $50-$100/ac/yr  | 6-7% | $714-$1,667/ac |

### Telecom Site Rental

**Urban cell tower sites**:

| Type | Monthly Rent | Cap Rate | Capitalized Value |
|------|--------------|----------|-------------------|
| Rooftop | $2,000-$5,000 | 6% | $400K-$1M |
| Ground lease (200-400 sf) | $1,500-$3,000 | 6-7% | $257K-$600K |

**Rural cell tower sites**:

| Type | Monthly Rent | Cap Rate | Capitalized Value |
|------|--------------|----------|-------------------|
| Greenfield | $500-$1,500 | 7-8% | $75K-$257K |
| Co-location (per carrier) | $300-$800 | 7-8% | $51K-$137K |

### Discount Rate Selection by Permanence and Operator

| Permanence | Government/Utility | Private Party |
|------------|--------------------|---------------|
| Perpetual (runs with land) | 4-5% | 5-6% |
| Long-term (50-99 yr) | 5-6% | 6-7% |
| Medium-term (20-49 yr) | 6-7% | 7-8% |
| Temporary (1-5 yr) | Lump-sum (not capitalized) | Lump-sum |

**Rate adjustments**:
- Add 0.5-1% for uncertain renewal
- Add 1-2% for risky operators
- Subtract 0.5% for government guarantees
- Subtract 0.5-1% for indexed annual escalations

### Temporary Construction Easement (TCE) Rates

| Annual Rate | Use Case |
|-------------|----------|
| 6%  | Conservative, government agencies (e.g. Austin, TX precedent) |
| 10% | Industry standard for private utility projects (most common) |
| 12%+ | High-disruption sites, premium locations, lengthy duration |

---

## Hybrid Calculator Architecture

**Shared core** (`easement_calculator_base.py`):
- TCE rate-of-return method
- Income capitalization (productivity loss basis)
- Before/after comparison
- Dynamic reconciliation
- Sensitivity analysis

**Domain specialization** (per-corridor calculators):
- Infrastructure-specific base percentages (tables above)
- Unique adjustment factors per industry
- Tailored reconciliation weights
- Professional standards alignment
