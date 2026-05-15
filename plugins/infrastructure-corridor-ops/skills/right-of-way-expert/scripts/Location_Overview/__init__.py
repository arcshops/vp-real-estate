"""
Location Overview Module

Generates comprehensive location overviews for Ontario properties, suitable for
inclusion in CUSPAP-compliant appraisal reports. Hosted by the
`right-of-way-expert` skill, which auto-loads on relevant location/zoning/
appraisal-research questions.

Features:
- Dual input support: 9-digit Ontario PIN or municipal address
- Multi-source integration: Ontario GeoHub, Toronto Open Data, Overpass API
- Provincial plan detection: Greenbelt, Growth Plan, Oak Ridges Moraine
- Zoning analysis: designation, permitted uses, Official Plan policies
- Neighbourhood analysis: amenities, transit, surrounding uses
- CUSPAP compliance: formatted per appraisal report standards

Usage:
    python3 -m Location_Overview.main "<PIN|address>"
    python3 -m Location_Overview.main "100 Queen Street West, Toronto"
    python3 -m Location_Overview.main 123456789
"""

__version__ = "1.0.0"
__author__ = "Lease Abstract Toolkit"

from .main import location_overview, LocationOverviewResult

__all__ = ["location_overview", "LocationOverviewResult", "__version__"]
