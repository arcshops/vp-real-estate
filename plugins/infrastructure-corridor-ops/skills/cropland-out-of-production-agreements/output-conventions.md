# Cropland Compensation Output Conventions

Standard structure, filename convention, and tone guidance for compensation analysis deliverables. Linked from `SKILL.md`.

## Filename & Location

Save deliverables to `$CLAUDE_PROJECT_DIR/Reports/` with Eastern Time timestamp prefix.

**Filename format**: `YYYY-MM-DD_HHMMSS_[farm_name]_cropland_compensation_analysis.md`

**Get timestamp**: `TZ='America/New_York' date '+%Y-%m-%d_%H%M%S'`

## Standard Deliverable Sections

1. **Executive Summary** — Three-model comparison table and recommendation
2. **Farm & Infrastructure Summary** — Acreage, crop type, land value, tower count, voltage, ROW dimensions, lifespan
3. **Compensation Models Detailed Analysis** — Ontario, Alberta, Farmer Required (full math for each)
4. **Comparative Analysis** — Shortfall ($/%), multiplier, exceeds-needs analysis
5. **Sensitivity Analysis** — Discount rate, crop prices, tower count, breakeven, scenario tables
6. **Risk Assessment & Non-Financial Considerations** — Intergenerational equity, farm value impact, precedent
7. **Negotiation Strategy** — Three-tier counter-offer, walk-away threshold, tactics, sequencing
8. **Conclusion & Final Recommendation**
9. **Appendices** — Calculation methodology, data sources, supporting files, assumptions/limitations

## Professional Tone Guidance

This analysis **ADVOCATES for the farmer** — it is not neutral.

**Use evidence-backed advocacy language**:
- Terms like "inadequate", "shortfall", "uncompensated burden", "cost externalization" are appropriate
- Every claim must be backed by a number, a precedent (Alberta case law, OFA position, gas pipeline practice), or documented operational data
- Frame from farmer perspective; quantify everything — turn qualitative complaints into dollar figures
- Emphasize intergenerational impacts: perpetual easement = perpetual burden = requires perpetual compensation

**Avoid**:
- Neutral "on the one hand / on the other hand" framing that gives the utility's position equal weight
- Hedging language ("possibly inadequate", "may be unfair") — be definitive when the numbers support it
- Generic complaints not tied to dollar figures
- Treating Ontario's lower NPV as favorable (see NPV convention in `calculator-reference.md`)
