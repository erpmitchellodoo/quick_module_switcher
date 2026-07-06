# -*- coding: utf-8 -*-

{
    "name": "Quick Module Switcher",
    "version": "17.0.1.0.0",
    "category": "Productivity",
    "summary": "User-configurable backend shortcuts for switching Odoo apps",
    "description": """
Adds a quick-switch dropdown to the Odoo backend header.

Each user can select the applications shown in the dropdown from their Odoo
preferences. Only applications visible to that user are displayed.
    """,
    "author": "Mitchel Admin",
    "maintainer": "Mitchel Admin",
    "support": "erpmitchellodoo@gmail.com",
    "depends": ["web"],
    "data": ["views/res_users_views.xml"],
    "assets": {
        "web.assets_backend": [
            "quick_module_switcher/static/src/js/quick_module_switcher.js",
            "quick_module_switcher/static/src/xml/quick_module_switcher.xml",
            "quick_module_switcher/static/src/scss/quick_module_switcher.scss",
        ],
    },
    "license": "LGPL-3",
    "images": ["static/description/banner.png"],
    "installable": True,
    "auto_install": False,
    "application": False,
}
