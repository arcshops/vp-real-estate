---
name: lease-compliance-auditor
description: Use when auditing tenant insurance certificates against CGL and property requirements, verifying environmental compliance obligations, checking use clause adherence, monitoring covenant breaches, or producing a compliance red-flag report with notice and cure timing.
---

# Lease Compliance Auditor

## Overview

**Lease Compliance** = Ongoing verification that all parties fulfill their contractual obligations under the lease.

**Purpose**:
- Prevent defaults and disputes
- Maintain insurance/environmental protection
- Preserve lease enforceability
- Protect property value
- Support litigation defense

**Key Categories**:
1. Insurance compliance
2. Environmental compliance
3. Use clause compliance
4. Financial covenant compliance
5. Administrative compliance (reporting, notices)

## Core Concepts

### Insurance Compliance

**Required Coverages** (Typical):
- **Commercial General Liability (CGL)**: $2M-$5M per occurrence
- **Property Insurance**: Replacement cost of tenant improvements
- **Business Interruption**: 12 months minimum
- **Additional Insured**: Landlord as additional insured on CGL
- **Waiver of Subrogation**: Mutual waiver

**Annual Requirements**:
- Certificate of Insurance delivered 30 days before expiry
- Policy must name landlord as additional insured
- 30-day notice of cancellation clause
- Coverage limits maintained throughout term

**Red Flags**:
- Expired certificates
- Insufficient coverage limits
- Landlord not named as additional insured
- No waiver of subrogation

### Environmental Compliance

**Tenant Obligations**:
- No hazardous materials storage (except approved)
- Obtain environmental permits
- Comply with all environmental laws
- No soil/groundwater contamination
- Phase I/II reports (if required)

**Landlord Monitoring**:
- Annual environmental questionnaire
- Site inspections
- Review permits and manifests
- Monitor waste disposal practices

**Red Flags**:
- Unauthorized hazmat storage
- Missing permits
- Environmental violations/fines
- Visible contamination

### Use Clause Compliance

**Permitted Use Verification**:
- Tenant operates only within permitted use
- No prohibited activities
- Zoning compliance maintained
- Municipal business license current

**Red Flags**:
- Business type change without consent
- Operating outside permitted hours
- Zoning violations
- Nuisance complaints

## Methodology

### Step 1: Establish Compliance Checklist

**Extract from lease**:
- All tenant obligations
- All landlord obligations
- Notice requirements
- Delivery deadlines
- Performance standards

**Create tracking matrix**:
```
Obligation | Frequency | Deadline | Status | Last Verified
```

### Step 2: Insurance Audit

**Annual Process**:
1. Request certificate 60 days before expiry (allow time for corrections)
2. Verify coverage limits match lease requirements
3. Confirm landlord named as additional insured
4. Check waiver of subrogation included
5. Verify 30-day cancellation notice provision
6. Maintain copies in lease file

**Non-Compliance Action**:
- Send notice to cure (10 days)
- If not cured, landlord may obtain insurance and charge tenant
- Potential default if persistent non-compliance

### Step 3: Financial Covenant Monitoring

**If lease requires**:
- Annual financial statements (120 days after year-end)
- Maintain minimum DSCR (e.g., 1.25)
- Maintain minimum net worth
- Maximum debt-to-equity ratio

**Verification**:
1. Receive financial statements
2. Calculate ratios
3. Compare to covenant thresholds
4. Document compliance or breach

**Breach Action**:
- Notice to tenant
- May trigger additional security requirement
- Potential default if material breach

### Step 4: Site Inspection

**Periodic inspections** (quarterly/annually):
- Verify permitted use
- Check property condition
- Observe alterations/improvements
- Environmental observations
- Signage compliance
- Parking compliance

**Document findings** and follow up on violations

### Step 5: Notice & Reporting Compliance

**Track**:
- Annual financial statements delivered
- Insurance certificates delivered
- Option notices delivered timely
- Environmental reports submitted
- Audit rights exercised

**Maintain documentation** for dispute resolution

## Red Flags

### Insurance Non-Compliance

**Expired Certificate**:
- Coverage lapsed
- **Action**: Immediate notice to cure, obtain landlord's policy if not cured

**Insufficient Limits**:
- $2M CGL required, $1M provided
- **Action**: Notice to cure, increase limits

**Landlord Not Additional Insured**:
- Policy doesn't name landlord
- **Action**: Request endorsement, reject certificate until corrected

### Environmental Violations

**Hazmat Storage Without Approval**:
- Tenant storing chemicals not disclosed
- **Action**: Immediate notice, require removal or approval process

**Environmental Fines**:
- Municipal violation notice issued
- **Action**: Demand proof of remediation, may trigger indemnity claim

**No Permits**:
- Operating without required environmental permits
- **Action**: Notice to obtain, potential lease default

### Use Clause Violations

**Operating Outside Permitted Use**:
- Office tenant subletting to manufacturing
- **Action**: Cease and desist, require consent for use change

**Zoning Violation**:
- City issues zoning violation notice
- **Action**: Demand immediate compliance, tenant indemnifies landlord

### Financial Covenant Breach

**DSCR Below Threshold**:
- Lease requires 1.25, tenant at 1.1
- **Action**: Require additional security deposit or guarantee

**Late Financial Statements**:
- Due 120 days after year-end, not received
- **Action**: Notice to deliver, potential default

## Integration with Slash Commands

This skill is automatically loaded when:
- User mentions: compliance, insurance audit, environmental compliance, use clause, covenant
- Reading files: Insurance certificates, environmental reports, compliance documents

**Related Commands**:
- `/default-analysis <lease-path>` - Assess compliance violations as defaults

Insurance audits and environmental compliance reviews are handled directly by this skill — just ask in natural language.

## Examples

### Example 1: Annual Insurance Audit

**Lease Requirements**:
- CGL: $5M per occurrence
- Property: Replacement cost
- Business Interruption: 12 months
- Additional Insured: Landlord
- Waiver of Subrogation: Yes

**Certificate Received**:
- CGL: $2M per occurrence ❌
- Property: Actual cash value ❌
- Business Interruption: 6 months ❌
- Additional Insured: Not shown ❌
- Waiver of Subrogation: Not shown ❌

**Audit Result**:
```
INSURANCE COMPLIANCE AUDIT - FAIL

Deficiencies:
1. CGL coverage insufficient ($2M vs. $5M required)
2. Property insurance on ACV basis (replacement cost required)
3. Business interruption insufficient (6 months vs. 12 required)
4. Landlord not shown as additional insured
5. Waiver of subrogation not shown

Action Required:
- Reject certificate
- Issue notice to cure within 10 days
- Provide corrected certificate meeting all lease requirements
- If not cured, Landlord may obtain insurance and charge Tenant

Status: NON-COMPLIANT
```

### Example 2: Use Clause Violation

**Lease Permitted Use**: "General office purposes only"

**Site Inspection Findings**:
- Tenant operating gym/fitness studio
- Equipment observed: treadmills, weights, showers
- Signage: "ABC Fitness - Personal Training"

**Compliance Assessment**:
```
USE CLAUSE COMPLIANCE AUDIT - VIOLATION

Permitted Use: General office purposes
Actual Use: Fitness studio / personal training

Violation: Material change in use without landlord consent

Concerns:
- Increased liability (fitness injuries)
- Increased building insurance premiums
- Higher wear/tear (showers, equipment)
- Parking impact (clients vs. office workers)
- Potential zoning violation (may require fitness license)

Action Required:
1. Cease and desist notice
2. Require tenant to:
   a) Cease fitness operations, OR
   b) Request formal consent to use change
3. If consent considered:
   - Amend permitted use clause
   - Increase insurance requirements
   - Charge higher rent (fitness use = higher value)
   - Obtain zoning confirmation

Status: VIOLATION - Immediate action required
```

---

## Insurance Audit Workflow

**Invocation**: Ask in natural language, e.g. "Audit the insurance compliance for this lease against the attached certificate."

### Step 1: Extract Lease Insurance Requirements

For each required insurance type, extract:

**Commercial General Liability (CGL):**
- Per-occurrence and annual aggregate limits
- Required coverages (bodily injury, property damage, personal injury)
- Additional insureds (landlord, property manager, lender)
- Cross-liability/severability of interests clause
- Contractual liability coverage

**Property Insurance (Tenant's Improvements):**
- Coverage type (replacement cost vs. actual cash value)
- Perils covered (all-risk vs. named perils)
- Deductible limits; loss payee requirements

**Business Interruption / Rent Insurance:**
- Minimum coverage period (months); minimum amount (X months' rent)
- Landlord as loss payee

**Other Required Insurance:**
- Automobile liability, pollution/environmental liability
- Boiler and machinery / equipment breakdown
- Workers compensation; umbrella/excess liability

**Policy Requirements:**
- Insurance company A.M. Best rating (A- minimum)
- Primary and non-contributory
- Waiver of subrogation in favor of landlord
- Maximum deductible threshold

**Certificate Requirements:**
- Certificate holder (landlord name/address)
- Delivery timeline (before occupancy, annually, 30 days before renewal)
- Notice of cancellation period (30 days minimum)
- Form: ACORD 25 or equivalent

### Step 2: Insurance Requirements Matrix

| Insurance Type | Required? | Minimum Limits | Additional Insured | Special Requirements |
|----------------|-----------|----------------|-------------------|---------------------|
| CGL | Yes | $X,XXX,XXX per occ / $X,XXX,XXX aggregate | Landlord, PM | Cross-liability, contractual |
| Property | Yes | Replacement cost | Landlord as loss payee | All-risk, max $X deductible |
| Business Interruption | Yes | 12 months rent | Landlord as loss payee | Covers rent obligation |
| Umbrella | ? | - | - | |
| Auto Liability | If applicable | $X,XXX,XXX | - | |
| Boiler & Machinery | If applicable | $XXX,XXX | Landlord | If equipment on premises |

### Step 3: Review ACORD 25 Certificate (if provided)

Extract and verify:
- Insurer name and A.M. Best rating
- Policy numbers and effective/expiration dates
- Coverage limits (per occurrence, aggregate)
- Certificate holder (correct landlord name/address?)
- Additional insured endorsement listed?
- Waiver of subrogation shown?
- Notice of cancellation period

**Required vs. Actual Comparison Table:**

| Requirement | Lease Requires | Actual Policy | Compliant? | Gap/Issue |
|-------------|----------------|---------------|------------|-----------|
| CGL Per Occurrence | $2,000,000 | $X | ✓/✗ | |
| CGL Aggregate | $5,000,000 | $X | ✓/✗ | |
| Additional Insured | Landlord | Listed/Not listed | ✓/✗ | |
| Property Coverage | $X | $X | ✓/✗ | |
| Biz Interruption | 12 months | X months | ✓/✗ | |
| Waiver of Subrogation | Required | Shown/Not shown | ✓/✗ | |
| Notice Period | 30 days | X days | ✓/✗ | |
| A.M. Best Rating | A- minimum | [Rating] | ✓/✗ | |

### Step 4: Non-Compliance Classification

**Critical (Immediate Action):**
- No insurance certificate on file
- Insurance has expired
- Landlord not listed as additional insured
- Coverage limits below requirements
- No waiver of subrogation
- Insurer rating below A-

**Material (Require Correction):**
- Amounts slightly below requirements
- Missing specific coverage types
- Deductible exceeds permitted amount
- Certificate holder information incorrect
- Notice period less than required

**Administrative (Low Priority):**
- Certificate not on ACORD 25 form
- Minor clerical errors

### Step 5: Calculate Insurance Gap Exposure

For each deficiency, estimate landlord's exposure:

**Inadequate Liability Limits:**
```
Required: $2,000,000 per occurrence
Actual: $1,000,000
Gap: $1,000,000
Exposure: If tenant causes $2M claim, landlord potentially liable for $1M shortfall
```

**Missing Business Interruption:**
```
Required: 12 months rent
Actual: 0 months
Gap: $XXX,XXX (12 months × monthly rent)
Exposure: If fire/casualty, tenant may default on rent; landlord loses gap before re-leasing
```

### Step 6: Action Plan for Non-Compliance

**Immediate (Critical Deficiencies):**
1. Send notice of insurance deficiency (10-day cure period)
2. Reject non-compliant certificate
3. If not cured: landlord may obtain insurance and charge tenant as additional rent
4. Persistent non-compliance = notice of default

**If Not Cured:**
- Purchase insurance on tenant's behalf (if lease permits), charge cost to tenant
- Issue notice of default
- Consider lease termination if material breach

### Step 7: Insurance Tracking Schedule (Compliant Tenants)

| Tenant | Policy Type | Expiry Date | Renewal Reminder | Certificate Due | Status |
|--------|-------------|-------------|------------------|-----------------|--------|
| [Name] | CGL | YYYY-MM-DD | 90 days before | 30 days before | Current/Expiring/Expired |
| [Name] | Property | YYYY-MM-DD | 90 days before | 30 days before | Current/Expiring/Expired |

**Automated reminder timeline:**
- 90 days before expiry: Notify tenant renewal approaching
- 60 days before: Request renewed certificate
- 30 days before: Follow up if not received
- 15 days before: Escalate to management
- 7 days before: Prepare default notice
- Day of expiry: If not renewed, issue default notice

### Output Report

Save to `Reports/YYYY-MM-DD_HHMMSS_[tenant]_insurance_audit.md`

Report includes:
- Summary of lease requirements
- Analysis of actual coverage (if certificates provided)
- Compliance status (compliant / non-compliant)
- List of all gaps and deficiencies
- Estimated exposure for each gap
- Corrective action requirements with deadlines
- Template notice to tenant demanding compliance

### Example Usage

> "Audit insurance compliance for `/path/to/lease_abstract.md` against `/path/to/insurance_certificate.pdf`."

---

**Skill Version:** 1.0
**Last Updated:** November 13, 2025
**Related Skills:** commercial-lease-expert, default-and-remedies-advisor, lease-abstraction-specialist
**Related Commands:** /default-analysis (insurance and environmental compliance reviews are handled by this skill)
