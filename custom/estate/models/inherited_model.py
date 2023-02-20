from odoo import fields, models, api, _ 

class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'user_id', domain=[('state', 'in', ['New','Offer Received', 'Offer Accepted'])])
    
    