# Copyright 2020 Camptocamp (https://www.camptocamp.com)
# Copyright 2021 ACSONE SA/NV (http://www.acsone.eu)
# @author Simone Orsi <simahawk@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Shopfloor example",
    "summary": "Show how to customize the Shopfloor app frontend.",
    "version": "14.0.1.0.0",
    "author": "Camptocamp, ACSONE, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/wms",
    "category": "Hidden",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "shopfloor_base",
        "shopfloor_mobile_base",
        "shopfloor_mobile_base_auth_user",
        "shopfloor_mobile_base_auth_api_key",
    ],
    # fmt: off
    "demo": [
        "demo/shopfloor_scenario_demo.xml",
        "demo/shopfloor_profile_demo.xml",
        "demo/shopfloor_menu_demo.xml",
        "demo/shopfloor_app_demo.xml",
    ],
    # fmt: on
    "data": ["templates/assets.xml"],
    "post_init_hook": "post_init_hook",
}
