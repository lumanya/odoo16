from odoo import fields, api, models, _   


class MarketCategory(models.Model):
    _name = 'market.category'

    name = fields.Char(required=True)
   