# -*- coding: utf-8 -*-
{
    'name': "Vendor Self-Service Portal",

    'summary': """
        Vendor Self-Service Portal module for Fatmug Designs""",

    'description': """
        Vendor Self-Service Portal is designed to assess your ability to implement key features in Odoo while
        maintaining a manageable scope suitable for a short time frame.    """,

    'author': "Fatmug-Eng-Mahmoud-Rafat",
    'website': "https://www.fatmugcompany.com",

    'category': 'web',
    'version': '0.1',

    'depends': ['base', 'sale', 'sale_management', 'portal'],

    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/vendor_forcast.xml',
        'views/vendor_adjustment_request.xml',
        'views/sale_order_inherit_view.xml',
        'views/product_inherit_view.xml',
        'views/vendors_res_config_settings.xml',
        'wizard/adjustment_request_submission.xml',
        'data/vendor_email_template.xml',
        'report/vendor_forcast_template.xml',
        'report/report.xml',
        'views/portal_templates.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'installable': True,
}
