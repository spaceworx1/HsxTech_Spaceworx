# -*- coding: utf-8 -*-
{
    'name': "Spaceworx Schedular for quotation",

    'summary': "This Module create schedular action to send email each week to the customer before its quotation expired",

    'description': """
This Module create schedular action to send email each week to the customer before its quotation expired
    """,

    'author': "HSxTech",
    'website': "https://www.hsxtech.net",

    'category': 'sale',
    'version': '17.0.0.1',
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/sale_order_cron.xml',
        'views/sale_order.xml',
        'views/templates.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False
}

