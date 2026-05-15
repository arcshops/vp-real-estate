# Encumbrance Catalog: Registered Instrument Parsing

Comprehensive catalog of registered instrument types affecting Ontario real property, with parsing templates, sample registrations, and impact analyses. Companion reference to `SKILL.md` in the `title-expert` skill.

## Easements (Use Rights, Not Ownership)

**Definition**: Grant of right to use another's property for a specific purpose (utility corridor, access, drainage). Does NOT convey ownership, just the right to use.

### Key Characteristics

- **Appurtenant vs. in gross**: Appurtenant easements (benefit adjacent "dominant" property) transfer with land sale; in gross easements (personal benefit) may not transfer.
- **Exclusive vs. shared**: Exclusive easement means the grantor cannot use the corridor (e.g., sole pipeline right); shared easements permit multiple users.
- **Perpetual vs. term**: Perpetual easements run indefinitely; term easements expire (e.g., 50-year telecom easement).
- **Priority**: Earlier-registered easements rank ahead of later ones.

### Parsing a Registered Easement

```
EASEMENT (Parcel 1234567)
Date registered: June 1, 2010
Grantor: ABC Energy Corp (utility company)
Grantee: John Smith (landowner)
Description:
  - Purpose: Transmission line easement
  - Area: 2-hectare corridor, 60 meters wide
  - Restrictions: No buildings, no tree planting within corridor
  - Maintenance: ABC Energy maintains line, accesses 2x per year
  - Duration: Perpetual
  - Right of way: Exclusive to ABC Energy and their successors
```

### Impact Analysis

- **Land affected**: 2 hectares (60m × ~330m) permanently encumbered.
- **Use restrictions**: Cannot build, cannot irrigate (pivot circles), cannot plant trees.
- **Marketability**: Reduces value (agricultural land reduced to 20 hectares if originally 100 hectares).
- **Successors**: ABC Energy can transfer easement to another utility company (buyer inherits obligation).

## Restrictive Covenants (Use Restrictions)

**Definition**: Agreement restricting how owner may use property. Binds original owner AND successors in title (runs with the land).

### Key Characteristics

- **Binding on successors**: Survives property sales (encumbers the land itself).
- **Enforcement**: Can be enforced by original covenantee or assignees (e.g., neighborhood association).
- **Modification**: Persists unless (a) agreement to discharge, (b) court order, or (c) modified/discharged via Superior Court application.
- **Lapse**: Some old covenants are effectively lapsed (e.g., a 1920 covenant prohibiting business use in an area now zoned commercial is likely unenforceable).

### Common Covenant Types

**Land use restrictions**:
- "Property shall be used exclusively for single-family residential purposes"
- "No commercial use permitted"
- "Minimum lot size 1 acre"

**Building/density restrictions**:
- "Maximum 2 stories"
- "Maximum 30% lot coverage"
- "Setback minimum 50 feet from property line"

**Maintenance obligations**:
- "Property owner shall maintain boundary fence in good condition"
- "Exterior paint color shall be earth tones (brown, gray, taupe)"
- "Lawns shall be maintained (grass mowed, no weeds)"

**Special use restrictions** (developer controls):
- "No signs except real estate sale sign"
- "No trucks/commercial vehicles parked on property"
- "Architectural approval required for additions/modifications"

### Parsing a Registered Covenant

```
RESTRICTIVE COVENANT (Parcel 1234567)
Date registered: March 15, 1985
Covenantor (obligated party): Original owner
Covenantee (beneficiary): Shady Pines Development Inc. (original developer)
Covenant:
  "The property shall be used exclusively for residential purposes.
   No commercial, industrial, agricultural, or institutional use permitted.
   Any breach may result in injunction or damages."
Enforcement: Enforceable by developer and successor property owners in subdivision
Duration: Perpetual (until modified/discharged)
```

### Impact Analysis

- **Use restrictions**: Only residential use allowed (prohibits home-based business, rental of rooms, accessory dwelling unit).
- **Marketability**: Restricts buyer pool (investors wanting rental income excluded).
- **Enforceability**: Developer may no longer exist, but other property owners in subdivision could enforce.
- **Value impact**: Reduces land value if buyer needs business/mixed use.

## Liens (Payment Obligations)

**Definition**: Registered charge against property as security for debt. Holder has the right to seize and sell property if the debt is unpaid.

### Priority Order

- **First mortgage**: Ranks first (paid first from sale proceeds).
- **Second mortgage**: Ranks second (paid after first mortgage, before other liens).
- **Judgment lien**: Registered creditor judgment (low priority typically).
- **Tax lien**: Property tax arrears or income tax garnishment (often rank high).
- **Municipal lien**: Unpaid water/sewer/property tax arrears (can rank high).

### Parsing a Registered Lien

```
CHARGE/MORTGAGE (Parcel 1234567)
Rank: First Charge
Date registered: January 10, 2020
Mortgagee (lender): Royal Bank of Canada
Mortgagor (borrower): John Smith
Amount: $500,000
Maturity date: January 10, 2025
Interest rate: 5.5% annually
Terms:
  - Payment: $2,850/month principal + interest
  - Default if: Missed 2 consecutive payments, property tax arrears, breach of covenant
  - Prepayment: Allowed without penalty after 3 years
```

### Impact Analysis

- **Payment obligation**: Owner must pay the $500,000 debt (assumed by purchaser or paid from sale proceeds).
- **Default risk**: If payments missed, lender can foreclose (seize/sell property).
- **Ranks first**: Paid before other creditors, second mortgages, unsecured creditors.
- **Discharge**: Requires payoff of full $500,000 at closing (lender provides discharge document).

## Environmental Liens and Charges

**Definition**: Lien registered against property for environmental remediation costs (soil contamination, hazardous waste cleanup).

### Ontario Framework

- **Tar pond sites**: Registered under Environmental Protection Act.
- **Recordation**: Environmental liabilities and remediation requirements recorded on title.
- **Assumption**: New owner assumes environmental liability and remediation obligations.

### Parsing an Environmental Lien

```
NOTICE/CAVEAT (Parcel 1234567)
Date registered: May 1, 2015
Registration authority: Ministry of Environment, Conservation and Parks
Description:
  "Industrial property - known soil contamination.
   Phase II Environmental Site Assessment completed.
   Contaminated soil present (petroleum products, heavy metals).
   Remediation not yet completed.
   Remediation required: In-situ stabilization or soil excavation/off-site disposal.
   Estimated cost: $150,000-$300,000.
   Owner/successor responsible for remediation."
```

### Impact Analysis

- **Remediation cost**: New owner assumes $150,000-$300,000+ liability.
- **Timeline**: Remediation timeline depends on environmental regulator approval.
- **Financing impact**: Lenders may require Phase II update, environmental insurance.
- **Marketability**: Significantly reduced (industrial redevelopment buyers only).
- **Due diligence**: Environmental consultant must review Phase II report, provide remediation plan.

## Classification: Physical vs. Use vs. Payment

**Physical encumbrances** (occupy space):
- Easements: Transmission lines, pipelines, gas mains (occupy corridor)
- Underground utilities: Sewer, water, telecommunications (occupy space)
- Right of way: Utility corridors, access roads (occupy space)

**Use encumbrances** (restrict activities):
- Restrictive covenants: "Residential use only" (restricts commercial use)
- Zoning: "Low-density residential" (restricts commercial/industrial)
- Conservation easements: "No development" (restricts building)

**Payment encumbrances** (monetary obligations):
- Mortgages: Debt secured by property
- Tax liens: Unpaid property tax, income tax, HST
- Environmental liens: Remediation cost responsibility
