# Cropland Calculator Reference

Full input schema, validation rules, output structure, and conventions for `cropland_calculator.py`. Linked from `SKILL.md`.

## JSON Input Schema

```json
{
  "farm_details": {
    "total_acres": 250,
    "crop_type": "Cash crops (corn/soybeans rotation)",
    "land_value_per_acre": 35000,
    "net_income_per_acre": 600
  },
  "infrastructure": {
    "type": "Transmission line",
    "voltage": "500kV",
    "utility": "Hydro One",
    "tower_count": 16,
    "row_width_m": 80,
    "crossing_length_km": 2.0,
    "lifespan_years": 50,
    "tower_classification": {
      "cultivated": 14,
      "uncultivated": 0,
      "headlands": 2
    }
  },
  "compensation_offer": {
    "one_time_easement": 21000,
    "theoretical_profit_6yr": 12000,
    "total_one_time": 33000,
    "notes": "Ontario Hydro One standard offer"
  },
  "ongoing_impacts": {
    "headland_radius_m": 12.5,
    "headland_productivity_loss_pct": 40,
    "aerial_spray_restriction": true,
    "ground_spray_cost_per_ha": 550,
    "aerial_spray_cost_per_ha": 100,
    "precision_ag_interference": true,
    "gps_interference_width_m": 100,
    "overlap_pct": 7,
    "input_costs_per_ha": 800,
    "labor_increase_pct": 10,
    "hourly_labor_cost": 50,
    "weed_control_per_tower": 50,
    "equipment_damage_probability_pct": 2,
    "average_damage_cost": 5000
  },
  "financial_parameters": {
    "discount_rate_pct": 5.0,
    "npv_horizon_years": 50
  }
}
```

## Data Validation Rules

**Consistency checks**:
- `tower_classification` cultivated + uncultivated + headlands must equal `tower_count`
- `total_one_time` must equal `one_time_easement` + `theoretical_profit_6yr`
- `npv_horizon_years` should align with `lifespan_years`

**Reasonableness ranges** (flag if outside):
- Land value: $10,000-$60,000/acre
- Net income: $200-$1,200/acre
- Tower count: 1-50
- Headland productivity loss: 20-70%
- Labor increase: 5-30%
- Equipment damage probability: 1-5% per tower per year
- Discount rate: 3-7% (5% institutional default)

**Conditional fields**:
- If `aerial_spray_restriction = true`, both spray cost fields required
- If `precision_ag_interference = true`, GPS interference fields required

## Calculator Output (results.json)

For each model: total one-time, annual ongoing, NPV total over horizon.

**Comparison metrics**:
- Ontario vs Farmer Required shortfall ($ and % uncompensated)
- Alberta vs Ontario delta ($ and multiplier, typically 6-20×)
- Alberta vs Farmer Required (Alberta typically EXCEEDS actual needs - useful negotiation benchmark)

**Sensitivity analysis** (±20% on each):
- Discount rate (3% → 7%)
- Crop prices / net income per acre
- Tower count

**Breakeven analysis**: Discount rate at which Ontario offer equals Farmer Required (typically unrealistic — proves Ontario inadequate at any reasonable rate).

## NPV Convention (CRITICAL)

NPV in this skill represents **total cost to farmer over infrastructure lifespan**, NOT compensation paid.

- Higher NPV = more compensation REQUIRED to offset costs
- Lower NPV = less compensation required
- Ontario lower NPV is NOT "better" — it means Ontario compensates LESS and leaves more burden uncompensated

**Common misreading to avoid**: Treating Ontario's lower NPV as favorable. It is the shortfall that defines inadequacy.

## Annuity Factor Reference

```
Annuity Factor = (1 - (1 + r)^-n) / r

50 years @ 5% = 18.26
50 years @ 3% = 25.73
50 years @ 7% = 13.80
40 years @ 5% = 17.16
80 years @ 5% = 19.60
```

Used to capitalize annual compensation into one-time equivalent (or convert one-time offer into annual equivalent).
