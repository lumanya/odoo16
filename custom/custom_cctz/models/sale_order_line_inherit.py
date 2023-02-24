from odoo import fields, models, api, _    


class SaleOderLineInherit(models.Model):
    _inherit = 'sale.order.line'
      