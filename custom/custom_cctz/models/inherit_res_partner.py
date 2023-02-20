from odoo import fields, api, models, _   


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    vrn_number = fields.Char(string="VRN Number")
    account_manager_id = fields.Many2one('res.users')
    sector_id = fields.Many2one('sector.info', string='Sector')
    market_category_id = fields.Many2one('market.category', string="Market Category")
    customer_type_id = fields.Many2one('customer.type', string="Customer Type")
    