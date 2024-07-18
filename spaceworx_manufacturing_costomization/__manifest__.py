# -*- coding: utf-8 -*-
{
    'name': "SpaceWorx MO Customizations",

    'summary': "This addons add cutomer name and project name(Customer Reference) from sale order on manufacturing order",

    'description': """
This addons add cutomer name and project name(Customer Reference) from sale order on manufacturing ordere
    """,

    'author': "Ali Hassan",
    'website': "https://www.hsxtech.net",

    'category': 'sale, manufacturing',
    'version': '17.0.0.1',

    'depends': ['base','sale_management','mrp'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_production.xml',
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}

