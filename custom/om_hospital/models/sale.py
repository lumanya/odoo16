from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_description = fields.Char(string='Sale Description')