# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'description': """Manage library book catalogue and lending.""",
    'author': "Muflone",
    'application': True,
    'installable': True,

    'version': '0.1',
    'license': 'GPL-3',
    'website': 'https://github.com/muflone/odoo-tutorials',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # dependant files
    'data': [
        'security/library_security.xml',
        'views/library_menu.xml',
    ],
}
