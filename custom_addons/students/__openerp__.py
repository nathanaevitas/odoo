# -*- coding: utf-8 -*-
{
    'name': "Students Management System",

    'summary': """
        This is just a test create a module""",

    'description': """
        Long description of module's purpose
    """,

    'author': "To Am Xinh",
    'website': "http://www.toamxinh.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
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