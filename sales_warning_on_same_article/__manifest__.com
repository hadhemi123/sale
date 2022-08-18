# -*- coding: utf-8 -*-
{
    'name': "sale warning double article",

    'summary': """
        In Odoo 14, the user can add the same product in the same quotation more than one time,
        this module aims to notify the user of the duplication and the price unit of the first duplication
        of the product. 
        
        """,

    'description': """
         Notify the user of the product duplication in the same quotation
         how to use?
         - Install this module in your Odoo enviroment.
         - The warning will show up in case of duplication of products in the same quotation
    """,

    'author': "Hadhemi Jaballah",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
