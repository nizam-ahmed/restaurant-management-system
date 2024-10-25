# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Restaurant Management System',
    'version': '1.0.0',
    'summary': 'Restaurant Project',
    'sequence': 1,
    'description': """
    This module is used for training.
    """,
    'module_type': 'official',
    'author': 'Nizam',
    'company': 'Pyworx',
    'website': 'www.pyworx.in',
    'category': 'Customization',
    'depends': [
        'base'
    ],
    'data': [
        'views/restaurant.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}