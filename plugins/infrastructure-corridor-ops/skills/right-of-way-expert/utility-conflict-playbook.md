# Utility Conflict Playbook

Detailed reference for the **Utility Conflict Analysis Framework** in `SKILL.md`. The skill file holds the phase skeleton and one canonical example per phase; this playbook holds the full worked examples, cost tables, coordination scripts, and best-practice expansions.

## Phase 1 — Worked Examples for Geometric Conflict Detection

### Horizontal Conflicts (side-by-side at same elevation)

**Detection Criteria:**
- Utility centerline within ROW boundary: Direct conflict
- Utility within 5m of ROW edge: High risk (contact during excavation)
- Utility within 5-15m of ROW edge: Medium risk (special handling)

**Example — 115kV transmission corridor, 45m width, Station 0+000 to 0+500:**

```
1. Gas pipeline runs parallel, 8m from proposed ROW edge
   → HIGH RISK: Within 5m of edge
   → Requires relocation or increased clearance

2. Telecom cable in same area, 3m from proposed ROW centerline
   → DIRECT CONFLICT: Within ROW boundary
   → Mandatory relocation

3. Water main 12m from proposed ROW edge
   → MEDIUM RISK: 5-15m zone
   → Requires coordination, potential clearance agreement

4. Fiber optic line 25m from proposed ROW edge
   → LOW RISK: Beyond 15m buffer
   → Standard notification required
```

### Vertical Conflicts (stacked or crossing)

**Detection Criteria:**
- Utility crossing ROW perpendicular: Overhead vs. underground clearance issues
- Stacked utilities (one above another): Conflicts during relocation work
- Utilities at different elevations in ROW: Grade separation coordination

**Example — LRT corridor profile at Station 2+150:**

```
- Proposed LRT track elevation: +5.0m (at-grade)
- Existing hydro line: +8.5m elevation (overhead clearance 3.5m — ACCEPTABLE)
- Gas pipeline: -2.1m depth (crosses LRT perpendicular)
  → CROSSING CONFLICT: Gas must bridge over or under LRT
  → Design alternative required, cost implications
- Sewer main: -3.5m depth (parallel, adjacent to proposed corridor)
  → VERTICAL CONFLICT: Potential interference with LRT foundation
  → 2m horizontal separation required, may require local relocation
```

### Utility Locate Sources

**Ontario Call Before You Dig (811):** 1-800-400-2255. Submits request to registered operators; returns digital locate marks and utility maps in 5-10 business days.

**Direct utility contacts:**
- Hydro One — transmission line maps, voltage, tower locations, guy wire anchors
- Enbridge Gas — pipeline maps, pressure class, valve/regulator stations
- Toronto Hydro / municipal utilities — local distribution lines, transformers, vaults
- Bell / Rogers / telecom — cable routes, fiber paths, splice locations
- Municipalities / conservation authorities — sewer mains, water mains, drainage

Locate drawings typically show utility location to ±0.3m accuracy with depth, type, specifications (voltage, diameter, pressure class), and asset reference numbers.

## Phase 2 — Relocation Design Options by Utility Type

### Hydro (Transmission Line)

**Standards:** NESC (North American Electric Safety Code), CSA C22.1, Hydro One Engineering Standards.

| Option | Description | Pros | Cons | Cost |
|---|---|---|---|---|
| New parallel route | Relocate 50-300m to alternative alignment | Clean separation, no ongoing conflicts | Longer spans, higher tower costs, environmental | $500K-$2M/km |
| Underground burial | Overhead to underground cable, 1.0-1.5m depth | Eliminates visual impact, free above-ground ROW | Very high cost, thermal limits, hard to maintain | $2-$5M+/km |
| Clearance agreement | Maintain location with increased clearance zone | Minimal relocation, low cost | Limits above-ground development | $10K-$50K |

### Gas Pipeline

**Standards:** CSA Z662 (Oil and Gas Pipeline), Ontario Utility Commission regulation, Enbridge Engineering Standards.

| Option | Description | Pros | Cons | Cost |
|---|---|---|---|---|
| Parallel relocation | New alignment within 20-50m | Moderate cost, uses existing ROW access | Coordination with adjacent properties | $300K-$800K/km |
| Grade separation | Cross under ROW in protected casing, 20-50m | Minimal horizontal relocation | Complex design, cathodic protection mods | $400K-$1M |
| Directional drill | Bore at 2-3m depth | No surface disruption, clean separation | Expensive, depth limits, hard to locate later | $600K-$1.5M |

### Telecom / Water / Sewer

**Standards:** CSA B411 (Underground Pipe and Cable), local municipality standards, operator-specific standards.

**Telecom cable:**
- Route around ROW (1-5 km diversion): $50K-$200K
- Underground casing crossing: $100K-$300K
- Aerial route to parallel distribution: $30K-$100K

**Water main:**
- Parallel relocation at utility easement: $200K-$500K/km
- Grade separation under ROW in casing: $300K-$700K
- Pressure main (smaller diameter, elevated): $100K-$300K/km

**Sewer main:**
- Gravity line relocation parallel to ROW: $400K-$1M/km
- Grade separation with drop structure: $500K-$1.2M
- Pressure/vacuum main conversion: $200K-$600K/km

## Phase 3 — Detailed Cost Tables

### Transmission Line Relocation (per km)

| Voltage | New parallel route | Underground | Clearance agreement |
|---|---|---|---|
| 69kV | $600K-$900K | $2.5M-$3.5M | $20K-$40K |
| 115kV | $800K-$1.2M | $3M-$4.5M | $30K-$60K |
| 230kV | $1.2M-$1.8M | $4M-$6M | $50K-$100K |
| 500kV | $2M-$3M | $6M-$10M | $100K-$200K |

**Cost components per km:**
```
Surveying & Engineering:        $30K-$60K
ROW Land Costs:                 $50K-$300K (highly variable)
Tower/Pole Manufacturing:       $200K-$600K (voltage-dependent)
Conductor & Cable:              $100K-$400K (voltage-dependent)
Construction Labor:             $300K-$800K (voltage-dependent)
Environmental Mitigation:       $50K-$200K (site-dependent)
Restoration/Landscaping:        $30K-$100K
TOTAL:                          $760K-$2.5M per km
```

### Natural Gas Pipeline Relocation (per km)

| Pressure Class | Diameter | Parallel | Cased crossing | Directional drill |
|---|---|---|---|---|
| Low pressure | 100-150mm | $200K-$350K | $250K-$450K | $400K-$700K |
| Medium pressure | 200-300mm | $350K-$600K | $400K-$700K | $600K-$1M |
| High pressure | 400mm+ | $600K-$1M | $600K-$1.2M | $1M-$1.8M |

**Cost components per km:**
```
Surveying & Engineering:        $20K-$50K
Land/Easement Costs:            $30K-$150K
Pipe Materials & Fittings:      $150K-$400K (diameter-dependent)
Construction Labor:             $200K-$600K
Valve/Regulator Relocation:     $50K-$200K (if required)
Pressure Testing:               $30K-$100K
Cathodic Protection:            $50K-$150K
Restoration:                    $20K-$80K
TOTAL:                          $550K-$1.73M per km
```

### Telecom Cable Relocation

| Cable Type | Route Option | Unit Cost | Typical Length | Total |
|---|---|---|---|---|
| Copper cable | Aerial route | $50-100/m | 3-8 km | $150K-$800K |
| Fiber optic | Underground duct | $80-150/m | 3-8 km | $240K-$1.2M |
| Joint trench | Shared utility trench | $100-200/m | 3-8 km | $300K-$1.6M |
| Casing crossing | Underground casing | $300-600/m | 50-100m | $15K-$60K |

### Water Main Relocation

| Pipe Size | Material | Parallel | Cased Crossing |
|---|---|---|---|
| 150mm | Ductile iron | $250-350/m | $400-600/m |
| 200mm | Ductile iron | $300-450/m | $500-750/m |
| 300mm+ | Ductile iron | $400-600/m | $600-1000/m |

### Sewer Main Relocation

| Pipe Size | Type | Gravity Line | Pressure Main |
|---|---|---|---|
| 200mm | Standard | $200-350/m | $300-500/m |
| 300mm | Standard | $250-450/m | $350-600/m |
| 375mm+ | Standard | $350-600/m | $400-800/m |

## Phase 4 — Coordination Timeline (multi-utility corridor)

```
PHASE 1: UTILITY IDENTIFICATION & DESIGN (Months 0-3)
├─ Week 1-2: Issue 811 Locate Request (receive maps 5-10 days)
├─ Week 2-4: Direct Utility Coordination
│  ├─ Hydro One (transmission)
│  ├─ Enbridge (pipeline)
│  ├─ Bell/Rogers (telecom)
│  └─ Municipality (water/sewer)
├─ Month 1-2: Relocation Design (route alternatives, grade separation, alignment, gravity/pressure)
└─ Month 2-3: Engineering & Permits (designs, estimates, regulatory applications)

PHASE 2: EASEMENT & REGULATORY APPROVALS (Months 3-6)
├─ Month 3-4: ROW acquisition / relocation agreements
├─ Month 4-5: Environmental, municipal, Utility Commission, conservation authority approvals
└─ Month 5-6: Design finalization incorporating approval conditions

PHASE 3: UTILITY RELOCATION EXECUTION (Months 6-12)
├─ CRITICAL PATH — Transmission Line
│  ├─ Month 6-7: Land acquisition for new route
│  ├─ Month 7-9: New line construction
│  ├─ Month 9-10: Testing & commissioning
│  ├─ Month 10-11: De-energize and remove old line
│  └─ CRITICAL: 2-3 week closure window for switchover
├─ PARALLEL — Gas Pipeline (preconstruction → directional drilling/casing → pressure testing → switchover)
├─ PARALLEL — Water Main (preconstruction → construction → testing/connection)
├─ PARALLEL — Sewer (preconstruction → construction → testing/connection)
└─ PARALLEL — Telecom (route prep → cable installation → testing/activation)

PHASE 4: MAIN PROJECT CONSTRUCTION (Month 12+)
├─ Dependent on all utility relocations complete
└─ Utility companies on standby for emergency support
```

**Critical path elements:**

1. **Transmission line switchover** — multi-day de-energization window, only available in low-demand seasons (spring/fall), 2-3 month lead time. **Delay risk: ±3-4 months** if missed.
2. **Gas pipeline pressure testing** — regulatory inspection, 2-4 week approval. **Delay risk: ±2-3 months**.
3. **Municipal permits** — road crossings 4-8 weeks, excavation 2-4 weeks. **Delay risk: ±1-2 months**.
4. **Environmental approvals** — species at risk 3-6 months, conservation authority 4-8 weeks. **Delay risk: ±3-6 months**.

**Dependency chain:**

```
Project Start (Month 0)
    ↓
Utility Locates (Week 2) → Utility Meetings (Week 4)
    ↓
Relocation Design (Month 2) → Permits & Easements (Month 4)
    ↓
Hydro Switchover* (Month 10, 2-week window)
    ↓
Gas Pressure Test (Month 11, 1 week)
    ↓
All Utilities Clear (Month 11)
    ↓
Main Project Start (Month 12)

*If switchover window missed → 3-4 month delay; backup windows Month 13, 16
```

## Phase 5 — Utility Owner Coordination Details

### Hydro One (Transmission)

**Stakeholders:** Transmission System Operator (route planning, voltage studies); System Operations (switchover planning); Project Management; Engineering Standards.

**Meeting cadence:**
- Month 1: Initial coordination
- Month 2: Route alternatives review (3-4 options)
- Month 3: Preferred route selection
- Months 4-5: Monthly design reviews
- Month 6: Switchover planning (3-month advance)
- Months 7-10: Bi-weekly construction monitoring
- Months 10-11: Weekly pre-commissioning, daily during switchover

**Key documents:** Relocation Agreement (MOU on cost sharing/timeline), design drawings, cost estimate with shared responsibility matrix, switchover plan with safety protocols.

**Cost allocation:** Utility typically covers new line construction; project covers design, ROW, restoration. Typical split: project 40% / utility 60%.

### Enbridge Gas Pipeline

**Stakeholders:** System Planning, Engineering Design, Operations (interruption planning, supply continuity), Project Management.

**Meeting cadence:**
- Month 1: Locate processing (811)
- Month 2: Relocation options coordination
- Month 3: Design approval
- Month 4: Utility Commission permits
- Months 5-6: Construction planning
- Months 7-10: Monthly progress
- Month 11: Weekly pressure testing/commissioning

**Key documents:** locate info, relocation agreement, directional drill / casing design drawings, environmental assessment (if applicable), pressure test procedure.

**Cost allocation:** Utility typically 50-75% of relocation; project covers design and ROW. Negotiated case by case.

### Municipal Utilities (Water, Sewer)

**Stakeholders:** Water Systems Operations, Wastewater Management, Capital Planning, Engineering Services.

**Meeting cadence:** Month 1 locates → Month 2 coordination → Month 3 design review → Month 4 permits → Months 5-6 construction planning → Months 7-10 monthly construction → Month 11 testing.

**Key documents:** locate drawings, relocation agreement, environmental assessment if required, gravity flow analysis (sewer), hydraulic analysis (water if flow changes).

**Cost allocation:** Project typically covers 75-100%. Some jurisdictions require full project funding.

### Bell / Rogers Telecommunications

**Stakeholders:** Outside Plant Engineering, Network Operations, Capital Planning.

**Meeting cadence:** Month 1 locate → Months 2-3 relocation planning → Month 4 design approval → Month 6 construction scheduling → Months 7-9 cable installation → Month 10 testing/activation.

**Key documents:** locate info, relocation agreement, construction coordination plan.

**Cost allocation:** Project typically covers 50-100%. Minimal regulatory oversight.

## Phase 6 — Risk Assessment Tables

### Schedule Risk

| Risk Factor | Probability | Impact | Mitigation |
|---|---|---|---|
| Transmission switchover window missed | Medium (30%) | 3-4 months | Schedule 2-3 backup windows |
| Gas pressure test failure | Low (10%) | 4-6 weeks | Early pre-testing, 2-week buffer |
| Environmental survey required | Medium (40%) | 3-6 months | Conduct early if species at risk possible |
| Municipal permit delays | Low (15%) | 4-8 weeks | Submit early, pre-coordinate |
| Utility design disagreement | Low (10%) | 2-3 months | Engage utility early, multiple options |
| Unexpected ground conditions | Low (15%) | 2-4 weeks | Geotechnical investigation, contingency |
| Regulatory approval delays | Low (10%) | 2-4 weeks | Track processing times, escalation plan |

### Budget Risk

| Risk Factor | Base | Upside | Mitigation |
|---|---|---|---|
| Transmission line relocation | $1.5M-$3M/km | +30-50% | 2-3 design alternatives, negotiate utility share |
| Gas pipeline relocation | $800K-$1.5M/km | +20-40% | Early geotech, test directional feasibility |
| Water/Sewer relocation | $400K-$1M/km | +20-30% | Identify obstructions early, standard materials |
| Telecom relocation | $200K-$800K/km | +10-20% | Minimal contingency |
| Design & Engineering | +10% base | +50% overrun | Scope definition, design reviews, change mgmt |
| Contingency Buffer | +15% of total | varies | Track and reallocate unused contingency |

**Specific budget risks:**

```
Transmission Line ($1.8M/km base):
├─ Rock excavation: +20-30% if bedrock encountered ($360K-$540K)
├─ Environmental mitigation (sensitive area): +10-15% ($180K-$270K)
├─ ROW acquisition premium (urban): +50-100% ($900K-$1.8M)
└─ Utility escalation: +5-10% annually ($90K-$180K)

Gas Pipeline ($1M/km base):
├─ High-pressure crossing complexity: +20-30% ($200K-$300K)
├─ Cathodic protection relocation: +15-25% ($150K-$250K)
├─ Directional drill technical issues: +30-50% ($300K-$500K)
└─ Regulatory inspection delays: +10-15% ($100K-$150K)
```

### Risk Mitigation Strategies

1. **Early Utility Engagement** (saves 2-3 months) — initial contact Month 0, share route within 2 weeks, get feasibility feedback within 4 weeks. Identifies show-stoppers before detailed estimates.
2. **Multiple Design Options** — Option A direct relocation (high cost, fast); Option B cased crossing (medium); Option C parallel distant (low cost, slower). Flexibility if first option becomes prohibitively expensive.
3. **Geotechnical Investigation** — bore holes along preferred route; test directional drilling feasibility. Early cost $50K-$100K; saves $200K-$500K+ in overruns. ROI 4:1 to 10:1.
4. **Regulatory Pre-Coordination** — meet conservation authority Month 1 not Month 4; run species at risk survey in parallel with engineering. Permit package complete by Month 4 instead of Month 6.
5. **Contingency Planning** — identify backup switchover windows at 3-month intervals (primary Month 10; backups Month 13, 16).

## Best Practices Expansions

### 1. Early Utility Engagement (Month 0-1)

Schedule kickoff meeting with each utility within 2 weeks of route decision. Share preliminary GPS/map. Request feasibility feedback. Identify red flags (e.g., "transmission line cannot be moved"). Document constraints in writing.

**Key questions per utility:**
1. What conflicts exist between proposed ROW and your assets?
2. Can conflicting assets be relocated? What are the options?
3. Estimated cost for each relocation option?
4. Estimated timeline for relocation?
5. What regulatory approvals are required?
6. What is your preferred relocation approach?

### 2. Systematic Conflict Documentation

| Item | Utility | Location | Type | Priority | Option A | Option B | Option C | Recommended |
|---|---|---|---|---|---|---|---|---|
| 1 | Hydro One 115kV | km 0.8 | Direct | CRITICAL | Parallel $1.2M, 10mo | Underground $4.5M, 12mo | Clearance $30K | Parallel |
| 2 | Enbridge Gas | km 1.5 | Crossing | HIGH | Casing $850K, 8mo | Directional $1.2M, 9mo | — | Casing |
| 3 | Water main | km 2.1 | Parallel | HIGH | Relocation $450K, 6mo | Cased crossing $550K, 7mo | — | Relocation |

Tracks accountability, cost, timeline, and decisions.

### 3. Design-Phase Coordination (Months 2-4)

Weekly meetings (not quarterly). Share drawings immediately on completion. Address utility comments within 1 week. Obtain formal utility approval on final design. Deliverables: Utility Coordination Report, Cost Allocation Matrix, Schedule Integration Matrix, Risk Register.

### 4. Timeline Integration

```
Month 0:   Locates ordered (Wk 2), kickoff meetings (Wk 4)
Month 1-2: Relocation design + utility feedback
Month 3-4: Permits, relocation agreements signed
Month 5:   Procurement (long-lead towers, pipe)
Month 6-10: Parallel construction (Hydro, Gas, Water/Sewer, Telecom)
Month 10-11: Critical switchover period (hydro de-energize 2-3 days, gas pressure test 1-2 weeks, water/sewer connect 1-2 weeks)
Month 12:  Main project construction begins
```

**Never** start main project construction before all utilities are fully relocated and tested.

### 5. Cost Estimation Contingencies

```
Direct Relocation Cost Estimate:        $5.0M
Contingencies:
├─ Design refinement (5%):               $250K
├─ Unforeseen ground conditions (10%):   $500K
├─ Utility scope changes (10%):          $500K
├─ Regulatory requirement changes (5%):  $250K
├─ Inflation adjustment (3% over 2 yrs): $150K
└─ Risk Reserve (10%):                   $500K
Total Estimated Budget:                  $7.15M (43% contingency)
```

Typical contingency range 25-50%. 40%+ justifiable for high-risk items (transmission switchover, directional drilling).

### 6. Utility Owner Relationship Management

- Single point of contact on your team
- Respond within 24 hours to utility requests
- Monthly status updates (weekly during construction)
- Acknowledge concerns promptly; offer flexibility where utility has good reason
- Invite utility reps to site visits and project meetings
- Celebrate milestones (successful switchover, passed pressure test)

Trust built early translates to smoother execution and fewer disputes.

## Cost Calculator Input Example

The `/right-of-way-analysis` slash command integrates utility conflict detection with cost estimation. Sample invocations:

```bash
# Transmission line relocation analysis
/right-of-way-analysis "115kV transmission, 40m width, 2.5km length" "Preferred route coordinates and property details"

# Pipeline crossing conflict
/right-of-way-analysis "36-inch natural gas pipeline, current at km 3.2, proposed crossing at km 3.5" "Casing design specs"

# Multi-utility coordination
/right-of-way-analysis "LRT corridor 3.2km with conflicts: hydro line, gas pipeline, water main, sewer, telecom" "Detailed conflict schedule"
```

Sample input file:

```json
{
  "project_name": "Highway Expansion - Utility Conflicts",
  "corridor_type": "highway_expansion",
  "corridor_specifications": {
    "width_meters": 45.0,
    "length_meters": 2500.0,
    "alignment": "North-South corridor through suburban area"
  },
  "utility_conflicts": [
    {
      "utility_type": "transmission_line",
      "operator": "Hydro One",
      "voltage_kv": 115.0,
      "conflict_type": "direct_conflict",
      "conflict_location_km": 0.8,
      "distance_from_row_m": -5.0,
      "priority": "critical",
      "relocation_options": [
        {"option_name": "Parallel relocation 100m west", "estimated_cost": 1200000, "timeline_months": 10, "risk_level": "medium"},
        {"option_name": "Underground burial (3 km section)", "estimated_cost": 4500000, "timeline_months": 12, "risk_level": "high"}
      ]
    },
    {
      "utility_type": "gas_pipeline",
      "operator": "Enbridge Gas",
      "product": "natural_gas",
      "pressure_class": "high_pressure",
      "conflict_type": "perpendicular_crossing",
      "conflict_location_km": 1.5,
      "distance_from_row_m": 3.0,
      "priority": "high",
      "relocation_options": [
        {"option_name": "Cased crossing (75m span)", "estimated_cost": 850000, "timeline_months": 8, "risk_level": "medium"}
      ]
    },
    {
      "utility_type": "water_main",
      "operator": "Municipality of X",
      "diameter_mm": 300,
      "conflict_type": "parallel_overlap",
      "conflict_location_km": 2.1,
      "distance_from_row_m": 2.0,
      "priority": "high",
      "relocation_options": [
        {"option_name": "Parallel relocation to south", "estimated_cost": 450000, "timeline_months": 6, "risk_level": "low"}
      ]
    }
  ],
  "coordination": {
    "project_start_month": 0,
    "target_construction_start_month": 12,
    "parallel_relocation_possible": true,
    "critical_path_item": "transmission_line_switchover",
    "critical_path_duration_months": 10
  }
}
```
