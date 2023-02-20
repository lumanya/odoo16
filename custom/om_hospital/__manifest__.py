# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hopstila Management',
    'version': '1.0',
  
    'license': 'LGPL-3',
    'summary': 'Hostiptal Management Module',
    'description': "Manage Patient out and in",
    'sequence': -100,
    'depends': [   
       'sale',
       'mail',
    ],
    'data': [  
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient.xml',
        'views/sale.xml',
        'views/appointment.xml'
        
    ],
  
    'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False
}