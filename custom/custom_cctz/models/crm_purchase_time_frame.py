from odoo import fields, models, api


class PurchaseTimeFrame(models.Model):
    _name = 'purchase.time'
    _description = "Purchase Time Frame"

    name = fields.Char(required=True)