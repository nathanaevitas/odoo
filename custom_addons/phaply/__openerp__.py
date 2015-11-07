# -*- coding: utf-8 -*-
{
    'name': "Phap Ly",

    'summary': """
        Module quan ly cong viec va ho so mang phap ly.""",

    'description': """
        Module quan ly cong viec va ho so mang phap ly
    """,

    'author': "To Am Xinh",
    'website': "http://www.toamxinh.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Legal',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}