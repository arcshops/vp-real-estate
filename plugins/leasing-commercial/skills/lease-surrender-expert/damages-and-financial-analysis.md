# Surrender Damages & Financial Analysis

Reference companion to `SKILL.md`. NPV frameworks, scenario walkthroughs, and key metrics for evaluating surrender vs. enforcing the lease.

## Landlord's Financial Analysis

Compare two scenarios.

### Scenario A: Enforce Lease
- Collect rent for remaining term
- Less: vacancy costs if tenant defaults
- Less: legal costs to enforce
- Less: time value of delayed collections
- Plus: keep security deposit
- Plus: potential damages claim

### Scenario B: Accept Surrender
- Receive security deposit (keep or apply to arrears)
- Plus: arrears payment plan (discounted to present value)
- Plus: re-leasing opportunity (may be higher rent)
- Less: vacancy period (estimate)
- Less: leasing costs (TI, commission, free rent)
- Less: lost rent during vacancy
- Plus: avoid legal costs and time
- Plus: improved landlord-tenant relationship

### Net Present Value Calculation

```
NPV(Surrender) = Security Deposit
               + PV(Arrears Payments)
               + PV(New Lease Revenue - Vacancy - Leasing Costs)
               - PV(Lost Rent from Original Lease)
               + Avoided Legal Costs

If NPV(Surrender) > NPV(Enforce Lease), accept surrender.
```

## Tenant's Financial Analysis

Compare two scenarios.

### Scenario A: Continue Lease
- Pay rent for remaining term
- Plus: operating costs
- Plus: potential default damages if can't pay
- Plus: legal costs if landlord sues
- Less: utility of space (if still needed)
- Risk: business failure, bankruptcy

### Scenario B: Surrender
- Forfeit security deposit
- Pay arrears (on payment plan)
- Pay restoration costs
- Pay moving costs
- Plus: avoid future rent obligations
- Plus: opportunity to downsize or relocate
- Plus: avoid default and credit damage
- Plus: clean break

### Net Present Value Calculation

```
NPV(Surrender) = - Security Deposit
                - PV(Arrears Payments)
                - Restoration Costs
                - Moving Costs
                + PV(Avoided Future Rent)
                + PV(Avoided Operating Costs)
                + Avoided Default Damages
                + Avoided Legal Costs
                + Value of Clean Break

If NPV(Surrender) > NPV(Continue Lease), surrender makes sense.
```

## Key Metrics

1. **Breakeven New Rent**: What rent must landlord achieve on re-lease to break even?
2. **Breakeven Vacancy**: How long can space sit vacant before landlord is worse off?
3. **Tenant Savings**: How much does tenant save in PV terms by surrendering?
4. **Landlord Opportunity Cost**: What is landlord giving up by accepting surrender?

## Landlord Considerations

### Negotiating Points (Landlord Perspective)

1. **Security deposit retention**
   - Goal: Retain entire deposit as consideration for early surrender
   - Justification: Landlord loses guaranteed income stream, incurs re-leasing costs
   - Fallback: Apply to arrears, refund balance

2. **All leasehold improvements transfer**
   - Goal: Own all improvements without compensation
   - Justification: Improvements are landlord's property at lease end anyway
   - Watch for: Specialized improvements that may need removal

3. **Additional rent reconciliation**
   - Goal: Include "to be determined" amounts in tenant's obligations
   - Justification: Tenant owes for full occupancy period
   - Risk: May owe tenant refund if overestimated

4. **Broad tenant release**
   - Goal: Full release from all claims
   - Justification: Clean break, no future litigation
   - Watch for: Don't release tenant from post-surrender obligations

5. **Strong holdover penalties**
   - Goal: 150-200% penalty rent, plus indemnity
   - Justification: Landlord may have new tenant waiting
   - Risk: May be challenged as penalty clause (aim for liquidated damages)

6. **Access rights before surrender**
   - Goal: Unrestricted access for showings and construction
   - Justification: Need to secure new tenant
   - Fallback: Reasonable access, don't materially interrupt business

7. **No consideration to tenant**
   - Goal: Tenant gets nothing except release from future obligations
   - Justification: Tenant is getting benefit of early termination
   - Reality: May need to offer inducement if landlord needs the space

8. **Title clearance**
   - Goal: Tenant removes all caveats/notices immediately
   - Power of attorney: Can do it ourselves if tenant fails
   - Indemnity: Tenant pays all costs

9. **Personal guarantee continuation**
   - Goal: Guarantor remains liable for arrears and survival provisions
   - Justification: Guarantee covers all lease obligations
   - Watch for: Guarantee may terminate with lease

10. **As-is acceptance OR restoration**
    - Option A: Take premises as-is (if landlord will renovate anyway)
    - Option B: Require full restoration per lease (if re-leasing as-is)
    - Hybrid: Specify which improvements stay/go

### Risks for Landlord

1. **Re-leasing risk**: May not find new tenant quickly or at same rate
2. **Vacancy costs**: Must pay full operating costs during vacancy
3. **Leasing costs**: Commission, TI, free rent for new tenant
4. **Market risk**: Rents may have declined since original lease
5. **Tenant default on payment plan**: May have to chase arrears anyway
6. **Condition issues**: Premises may be in poor condition, costly to repair
7. **Environmental issues**: May discover contamination after tenant leaves
8. **Holdover**: Tenant may not vacate on time, delaying new tenant
9. **Additional rent reconciliation**: May owe tenant significant refund
10. **Lost leverage**: Once lease surrendered, can't use it as leverage

### Due Diligence (Landlord)

Before accepting surrender:
- Inspect premises: Understand condition and needed repairs
- Review financials: Confirm amount of arrears
- Check market: Can we re-lease quickly and at what rate?
- Environmental: Any concerns about tenant's use? Need Phase II?
- Title search: Confirm tenant registered notice of lease/caveat
- Guarantee review: Does guarantee survive? Need release from guarantor?
- New tenant secured?: Do we have replacement tenant lined up?
- Calculate NPV: Is surrender economically better than enforcing lease?

## Tenant Considerations

### Negotiating Points (Tenant Perspective)

1. **Security deposit refund**
   - Goal: Get full refund (or application to arrears only)
   - Justification: Deposit was security for performance; we're performing by surrendering
   - Reality: Often landlord keeps as consideration for early termination

2. **Release from all future obligations**
   - Goal: Complete release from all lease obligations after surrender
   - Justification: That's the point of surrender
   - Watch for: Survival provisions (indemnities, arrears, etc.)

3. **Leasehold improvement compensation**
   - Goal: Payment for valuable improvements
   - Justification: Tenant paid for improvements, landlord benefits
   - Reality: Rarely successful unless very specialized/valuable improvements

4. **Additional rent reconciliation in tenant's favor**
   - Goal: Ensure landlord refunds overpayments promptly
   - Justification: Tenant entitled to reconciliation per original lease
   - Secure: Request holdback or payment before surrender

5. **Reasonable time to vacate**
   - Goal: 30-90 days to relocate business
   - Justification: Need time to find new space, move equipment
   - Fallback: Negotiate surrender date that gives adequate time

6. **Reduced holdover penalties**
   - Goal: 100% rent (not 150-200%)
   - Justification: Penalty clauses may be unenforceable
   - Reality: 125-150% is market standard

7. **Landlord assistance with relocation**
   - Goal: Reduced rent during notice period, moving allowance, etc.
   - Justification: Landlord benefits from early surrender
   - Reality: Only if landlord really wants the space back

8. **Minimal restoration obligations**
   - Goal: Deliver as-is or "broom clean"
   - Justification: Landlord will renovate anyway
   - Reality: Depends on landlord's plans; negotiate specifics

9. **Payment plan for arrears**
   - Goal: Extended payment terms (12-24 months)
   - Justification: Tenant is cash-strapped (that's why surrendering)
   - Reality: Landlord wants cash now; 3-12 months typical

10. **Guarantor release**
    - Goal: Release guarantor from all obligations
    - Justification: Lease is surrendering, guarantee should too
    - Reality: Landlord will want guarantee to cover arrears and survival provisions

### Risks for Tenant

1. **Arrears collection**: Landlord may still pursue arrears aggressively
2. **Additional rent**: May owe significant amounts after year-end reconciliation
3. **Improvement removal costs**: May be expensive to remove and restore
4. **Holdover penalties**: If can't vacate on time, penalties are severe
5. **Title issues**: May be costly to remove caveats (legal fees)
6. **Lost investment**: Forfeit improvements with no compensation
7. **Security deposit loss**: Forfeit entire deposit
8. **Environmental**: May be liable for environmental issues discovered later
9. **Broad indemnity**: May be liable for claims arising after surrender
10. **No leverage**: Once surrendered, can't negotiate further

### Due Diligence (Tenant)

Before agreeing to surrender:
- Financial review: Confirm exact arrears amount; dispute any errors
- Improvement inventory: What must be removed? What's the cost?
- Restoration scope: What exactly must be restored? Get specifics in writing
- Additional rent estimate: What might we owe (or be owed) in reconciliation?
- Relocation timeline: Can we realistically vacate by surrender date?
- Alternative spaces: Do we have new space secured?
- Environmental assessment: Any potential contamination from our use?
- Guarantor impact: Will guarantor be released? Need their consent?
- Tax implications: Any tax consequences of surrender and forgiveness of debt?
- Negotiate better terms: Is landlord motivated? Can we get concessions?

## Negotiation Strategy

### For Landlords

**High Leverage (Landlord Has Strong Hand):**
- Tenant is in default
- Tenant is desperate (business failing)
- Landlord has replacement tenant waiting
- Strong market (easy to re-lease)

Strategy:
- Keep security deposit
- Require full arrears payment upfront (or very short payment plan)
- Broad release from tenant
- Limited release to tenant
- Strong holdover penalties
- Extensive restoration obligations

**Low Leverage (Landlord Needs Tenant to Agree):**
- Landlord wants space for redevelopment
- Landlord has buyer who wants vacant possession
- Landlord has higher-paying tenant waiting
- Weak market (hard to re-lease)
- Tenant is in good standing

Strategy:
- Offer to refund security deposit (or apply to arrears only)
- Accept as-is condition (minimal restoration)
- Consider paying tenant to leave (buyout)
- Extended payment plan for arrears
- Mutual releases
- Help tenant with relocation costs

### For Tenants

**High Leverage (Tenant Has Strong Hand):**
- Landlord wants space for specific purpose
- Landlord has replacement tenant or buyer
- Tenant is in good standing (no arrears)
- Tenant has time on lease (landlord can't force out)

Strategy:
- Demand security deposit refund
- Negotiate buyout payment from landlord
- Minimal restoration (as-is delivery)
- Extended time to vacate
- Landlord assistance with relocation
- Mutual releases

**Low Leverage (Tenant Desperate):**
- Tenant in default (arrears)
- Tenant business failing
- Tenant needs out quickly
- Landlord not eager to accept surrender

Strategy:
- Accept security deposit forfeiture
- Negotiate payment plan for arrears
- Offer to leave improvements in good condition
- Deliver on time to avoid holdover penalties
- Get full release from future obligations
- Clean break, preserve business reputation
