# Location Overview Playbook

Detailed reference for the **Location Overview Generator** in `SKILL.md`. The skill file holds the workflow skeleton (CLI usage, three-phase overview, save convention); this playbook holds the full research-query templates, CUSPAP narrative structure, and quality criteria.

## Phase 2 — Deep Web Research

Skip this phase when speed matters. Otherwise, supplement Phase 1 API data with `WebSearch` and `WebFetch` across five research domains.

### 1. Municipal Planning

Look for active applications, Committee of Adjustment decisions, Site Plan Approval status, development permits.

```
"[address]" site:toronto.ca planning application
"[address]" zoning amendment OR minor variance
"[address]" committee of adjustment
"[address]" site plan approval
```

### 2. Heritage

Register listings, heritage impact assessments, Heritage Conservation District studies.

```
"[address]" heritage designation Ontario
"[address]" site:heritagetrust.on.ca
"[address]" Part IV OR Part V heritage
"[neighbourhood]" heritage conservation district
```

### 3. Environmental

Conservation authority permits, Records of Site Condition, contamination history.

```
"[address]" record of site condition
"[address]" site:trca.ca OR site:cvc.ca
"[address]" brownfield OR contamination
"[address]" floodplain OR regulated area
```

### 4. Development Activity

Recent/proposed developments, building permits, neighbourhood trends.

```
"[address]" site:urbantoronto.ca OR site:skyrisecities.com
"[neighbourhood]" development pipeline [current year]
"[address]" building permit
"[neighbourhood]" intensification
```

### 5. Market Context

Area market trends, comparable values, notable transactions.

```
"[neighbourhood]" real estate market [current year]
"[address]" recent sale OR sold
"[neighbourhood]" comparable sales
"[neighbourhood]" market trends commercial OR residential
```

### Municipality-Specific Anchor Domains

- **Toronto** — `site:toronto.ca/city-government/planning-development`, `site:app.toronto.ca/DevelopmentApplications`
- **Ottawa** — `site:ottawa.ca/en/planning-development-and-construction`, `site:devapps.ottawa.ca`
- **Mississauga** — `site:mississauga.ca/services-and-programs/building-and-renovating/planning-and-development`
- **Other** — general searches with municipality name + "planning department"; check for an online development tracker.

## Phase 3 — Narrative Synthesis (CUSPAP Structure)

Combine API output and web findings into flowing prose suitable for direct paste into an appraisal report. Do **not** emit tables or bullet lists in the final narrative.

The narrative must follow CUSPAP location description conventions and cover all ten sections in order:

### 1. Property Identification (1 paragraph)

Civic address, legal description if available, coordinates, municipality, ward, neighbourhood.

### 2. Regional Context (1-2 paragraphs)

Municipality's role in the GTA/province, population, economic character, subject's position within it.

### 3. Neighbourhood Description (2-3 paragraphs)

Immediate character, land use mix, building typology, streetscape. Reference the building/development by name, developer, year built, style if known. Cite the applicable Secondary Plan area.

### 4. Transportation & Accessibility (1-2 paragraphs)

Subway, bus, GO Transit, major road access, walkability, cycling. Quantify distances to key transit nodes.

### 5. Amenities & Services (1-2 paragraphs)

Schools, shopping, healthcare, recreation, employment. Cite specific amenities by name and distance where impactful.

### 6. Planning Framework (2-3 paragraphs)

Official Plan designation, zoning, Secondary Plan policies, what is permitted, Provincial Plan status (Greenbelt, Growth Plan, etc.).

### 7. Development Activity (1-2 paragraphs)

Recent, ongoing, proposed projects by name, scale, status. Neighbourhood trend (intensification, stability, decline).

### 8. Environmental Considerations (1 paragraph)

Floodplain status, conservation authority jurisdiction, heritage designations, brownfield/contamination status.

### 9. Market Context (1 paragraph)

Comparable values, market trends, demand drivers.

### 10. Conclusion (1 paragraph)

Location strengths and limitations relevant to value or marketability.

## Quality Criteria

- **Prose, not tables** — final output reads like an appraisal report section, not a data dump.
- **Specificity over generality** — name the building, the developer, the Secondary Plan, the transit station, the conservation authority; quantify distances.
- **Attribute findings** — note when a fact came from API data vs. web research so a reviewer can verify.
- **Flag uncertainty** — explicitly note when planning application status, environmental clearance, or assessment data could not be confirmed and recommend verification.
- **Respect the limits** — PIN-to-address resolution via OnLand/Teranet is not available; MPAC assessment data requires a paid subscription; web-sourced planning status may be stale.

## Output Conventions

Save the final narrative to:

```
$CLAUDE_PROJECT_DIR/Reports/YYYY-MM-DD_HHMMSS_location_overview_narrative_[address_slug].md
```

Present to the user:
- The full narrative text in chat
- The saved file path
- The list of data sources used (API + web)
- Verification recommendations for any uncertain items
