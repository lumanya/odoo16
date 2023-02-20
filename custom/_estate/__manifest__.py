# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'ESTATE',
    'version': '1.2',
  
  
    'summary': 'Track leads and close opportunities',
    'description': "Real estate module",
   
    'depends': [
        'base',
       
    ],
    'data': [
       'security/ir.model.access.csv',
       'views/estate_property_views.xml',
       'views/estate_menus.xml'

    ],
  
    'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False
}