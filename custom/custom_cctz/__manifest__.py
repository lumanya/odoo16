{
    'name': 'Custom CCTZ',
    'sequence': -110,
    'summary': 'Custom odoo app as per CCTZ requirements',
    'description': """Custom odoo app as per CCTZ requirements""",
    'category': 'CRM & Sales',
    'author': 'Nathaniel Anania',
    'maintainer': 'Nathaiel Anania',
    'website': 'https://churhcycodes.co.tz',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'crm',
        'contacts',
        'mail',
        'purchase'
       
        
    ],
    'data': [
    'security/ir.model.access.csv',
    'views/crm_account_type.xml',
    'views/crm_payment_terms.xml',
    'views/crm_purchase_time_frame.xml',
    'views/crm_status.xml',
    'views/crm_inherit_crm_lead_view.xml',
    'views/product_manufacuture.xml',
    'views/product_inherit_product_template.xml',
    'views/sector_info.xml',
    'views/market_category.xml',
    'views/customer_type.xml',
    'views/inherit_res_partner.xml'
    
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'autoinstall': False,
   
    }