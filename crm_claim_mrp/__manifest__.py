# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Crm Claim MRP",
    "summary": """
        Module adds MRP functionality to crm claims.""",
    "version": "15.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        "crm_claim",
        "mrp",
    ],
    "data": [
        "views/mrp_production_views.xml",
        "views/crm_claim_views.xml",
    ],
}
