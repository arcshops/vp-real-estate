# Depreciation — Worked Examples

Detailed worked examples for the three categories of depreciation (physical, functional, external) and full reconciled examples for transmission towers and telecom ground stations.

---

## 1. Physical Depreciation

### Age/Life Method

**Formula**: `Physical Depreciation % = (Effective Age / Total Economic Life) × 100%`

Where:

- **Effective Age** — How old the asset appears to be based on condition (may differ from chronological age)
- **Total Economic Life** — Total years the asset remains physically and functionally useful

**Example — Transmission Tower**

- Chronological age: 15 years
- Effective age: 13 years (well-maintained, minor corrosion)
- Economic life: 40 years
- Physical depreciation % = (13 / 40) × 100% = **32.5%**
- Physical depreciation $ = $240,000 RCN × 32.5% = **$78,000**

### Observed Condition Method

Direct observation of deterioration factors, used to supplement the age/life method.

**Structural Integrity**
- Excellent: No visible damage, cosmetic only = 0%
- Good: Minor surface corrosion, no structural impact = –5% to –10%
- Fair: Moderate corrosion, some structural concern = –15% to –25%
- Poor: Significant deterioration, repair needed = –30% to –50%

**Corrosion Assessment**
- None/minimal = 0%
- Light surface rust (cosmetic) = –3% to –8%
- Moderate pitting (reduced cross-section) = –10% to –20%
- Heavy/advanced (structural weakness) = –25% to –40%

**Paint and Protective Coating**
- Excellent (recently applied, protective) = 0%
- Good (weathered but protective) = –2% to –5%
- Fair (peeling, loss of protection) = –8% to –15%
- Poor (minimal protection remaining) = –15% to –25%

**Hardware and Connections**
- Excellent = 0%
- Good (minor loose bolts) = –2% to –4%
- Fair (rust on bolts, some loose connections) = –5% to –10%
- Poor (extensive corrosion) = –15% to –25%

**Example — Telecom Tower with Observed Condition**

- Age/life method: 35% physical depreciation
- Observed condition adjustment:
  - Structural integrity (good): –8%
  - Corrosion (light surface): –5%
  - Paint (fair, peeling): –10%
  - Hardware (good): –3%
- Total observed adjustment: –26%
- Blended physical depreciation: ~**32%** (age/life with condition-based fine-tuning)

---

## 2. Functional Obsolescence

### Capacity Issues

**Excess Capacity** (asset oversized for current needs)
- Example: Substation with 200MVA capacity, only 120MVA utilized
- Adjustment: Typically –5% to –20% depending on market for excess capacity

**Inadequate Capacity** (asset undersized, limiting growth)
- Formula: `Upgrade Cost / (1 + Discount Rate)^Years to Upgrade`

**Example — Transmission Tower at Capacity Limit**

- Current tower: 230kV, 400A capacity
- Current load: 340A (85% utilization)
- Planned load in 5 years: 450A (exceeds capacity)
- Cost to upgrade tower height/replace: $150,000
- Discount rate: 6%
- Present value cost: $150,000 / (1.06)^5 = **$112,164**
- Functional obsolescence from inadequate capacity: **–$112,164**

### Design Efficiency

- **Outdated safety systems** (no modern fall-arrest): –$8,000 to –$15,000
- **Operational efficiency** (substation control building without HVAC): –$25,000
- **Maintenance accessibility** (requires extensive disassembly): –10% to –25% of components

**Example — Telecom Site Design Inefficiency**

- Ground shelter lacks proper grounding and surge protection
- Upgrade cost for modern protection: $12,000
- Reduced equipment lifespan due to inadequate protection
- Functional obsolescence: **–$12,000 + lost efficiency = –$18,000 total**

### Operational Deficiencies

- **Environmental/regulatory non-compliance** (e.g., no secondary containment for transformer oil): –$15,000 to –$30,000
- **Reliability and availability** (aging control system, single point of failure): –$30,000 to –$50,000
- **Monitoring and control limitations** (no SCADA): –5% to –10%

---

## 3. External Obsolescence

### Market Conditions

- **High demand markets** (transmission constraint relief): +5% to +15%
- **Declining demand markets**: –10% to –20%
- **Grid modernization / renewable integration**: +5% to +10%
- **Stranded asset risk** (distributed generation): –5% to –15%
- **Telecom market saturation**: –10% to –20%

### Regulatory Changes

- **Climbing/fall-protection retrofits**: –5% to –15%
- **SF6 insulation phase-out** in switchgear: –$30,000 to –$100,000 for large substations
- **Legacy non-compliant configurations**: –10% to –20%

### Economic Factors

- **Coal plant retirements** (tower serving retired plant): –20% to –40%
- **Renewable energy growth**: +10% to +20%
- **High interest rates** (deferred maintenance): –5% to –10%
- **HVDC technology displacing AC**: –15% to –25%
- **Smart grid integration**: +5% to +10%

**Example — External Obsolescence Impact**

- Base RCN after physical/functional: $280,000
- Energy transition impact (coal plant closure nearby): –$40,000 (–14%)
- New grid regulations requiring upgrades: –$15,000 (–5%)
- Total external obsolescence: **–$55,000 (–19.6%)**

---

## 4. Full Depreciated Replacement Cost — Transmission Tower

**Formula**: `DRC = RCN – Physical Depreciation – Functional Obsolescence – External Obsolescence`

**Step-by-step**

1. **Replacement Cost New**: $240,000
2. **Physical Depreciation**:
   - Age/life method: 32.5% = $78,000
   - Observed condition adjustment: –3% = $7,200
   - Total physical: **$85,200**
3. **Functional Obsolescence**:
   - Inadequate capacity (upgrade need): $45,000
   - Design deficiency (safety systems): $8,000
   - Total functional: **$53,000**
4. **External Obsolescence**:
   - Grid modernization impact: –$12,000
   - Energy transition impact: –$20,000
   - Total external: **–$32,000**
5. **Total Depreciation**: $85,200 + $53,000 + $32,000 = **$170,200**
6. **Depreciated Replacement Cost**: $240,000 – $170,200 = **$69,800**

### Depreciation Schedule

| Component               | RCN      | Physical | Functional | External | Net Value |
| ----------------------- | -------- | -------- | ---------- | -------- | --------- |
| Steel structure         | $85,000  | $28,900  | $0         | $5,100   | $51,000   |
| Insulators/hardware     | $15,000  | $5,100   | $0         | $900     | $9,000    |
| Foundation              | $25,000  | $8,500   | $8,000     | $1,500   | $7,000    |
| Grounding system        | $8,000   | $2,700   | $0         | $480     | $4,820    |
| Climbing/access         | $3,000   | $1,000   | $8,000     | $180     | –$6,180*  |
| Labor/overhead/profit   | $104,000 | $39,100  | $37,000    | $18,840  | $9,060    |
| **TOTALS**              | **$240,000** | **$85,200** | **$53,000** | **$32,000** | **$69,800** |

*Negative component values indicate concentrated obsolescence in access systems; rolled into overall value conclusion.

---

## 5. Full Worked Example — 69kV Lattice Transmission Tower (Ontario)

**Asset**: H-frame lattice tower, 120ft height, 1998 construction, moderate corrosion. **Valuation date**: November 17, 2025.

```
REPLACEMENT COST NEW ESTIMATION:
  Materials (structure, insulators, grounding):    $130,000
  Labor (fabrication, erection, testing):           $95,000
  Overhead (15%):                                    $33,750
  Profit (12%):                                      $27,000
  TOTAL RCN:                                        $285,750

PHYSICAL DEPRECIATION:
  Effective age: 27 years
  Economic life: 45 years
  Age/life method: 27/45 = 60% depreciation
  Physical depreciation amount:                     $171,450
  Observed condition adjustment (moderate corrosion): +5%
  Condition-adjusted physical depreciation:         $180,038

FUNCTIONAL OBSOLESCENCE:
  Modern climbing safety systems (deficient):       –$10,000
  TOTAL FUNCTIONAL:                                 $10,000

EXTERNAL OBSOLESCENCE:
  Grid modernization impact:                         –$5,000
  Renewable energy integration (positive):           +$8,000
  NET EXTERNAL:                                     +$3,000

DEPRECIATED REPLACEMENT COST:
  $285,750 – $180,038 – $10,000 + $3,000 = $98,712

MARKET APPROACH VALIDATION:
  Comparable 1: Similar 69kV tower, 2023 sale: $95,000
  Comparable 2: Nearby 69kV tower, 2024 sale: $110,000
  Adjusted range: $95,000 – $110,000

  Reconciliation: Cost approach ($98,712) within market range
                  Cost approach reconciles to: $102,000
```

**Final Value Conclusion**: $100,000–$105,000 (cost approach primary, market approach confirmatory)

---

## 6. Full Worked Example — Telecom Ground Station with Tower Lease

**Asset**: 100ft monopole tower with ground shelter and equipment, 8 years old. **Valuation date**: November 17, 2025.

```
REPLACEMENT COST NEW ESTIMATION:
  Tower structure (monopole):                       $85,000
  Foundation & concrete:                            $18,000
  Ground shelter & HVAC:                            $35,000
  Antennas & transmission equipment:                $50,000
  Power systems (generator, batteries):             $20,000
  Site infrastructure (road, fencing):              $12,000
  Cables, conduit, grounding:                       $15,000
  Labor & installation (25%):                       $80,950
  Overhead (15%):                                   $51,195
  Profit (12%):                                     $40,956
  TOTAL RCN:                                       $408,101

PHYSICAL DEPRECIATION:
  Effective age: 8 years; Economic life: 35 years
  Age/life method: 8/35 = 22.9%
  Tower structure depreciation (22.9%):             $19,465
  Equipment depreciation:
    - Antennas/transmission (15yr life): 53% = $26,500
    - Power systems (12yr life): 67% = $13,400
    - Controls (10yr life): 80% = $5,000
  Total physical depreciation:                      $64,365

FUNCTIONAL OBSOLESCENCE:
  Equipment technological obsolescence:             –$15,000
  Shelter climate control improvements:             –$8,000
  TOTAL FUNCTIONAL:                                 –$23,000

EXTERNAL OBSOLESCENCE:
  Telecom market saturation:                        –$30,000
  Technology transition (small cell networks):      –$15,000
  TOTAL EXTERNAL:                                   –$45,000

DEPRECIATED REPLACEMENT COST:
  $408,101 – $64,365 – $23,000 – $45,000 = $275,736

MARKET APPROACH VALIDATION:
  Tower lease comparable: $15,000/year × 8% cap rate = $187,500
  Add: Ground equipment and shelter value: +$50,000
  Market approach estimate: $237,500

  Blended value (60% market, 40% cost):
    $237,500 × 0.60 + $275,736 × 0.40 = $252,394
```

**Final Value Conclusion**: $250,000 (market approach weighted higher due to income data; cost approach provides upper bound).
