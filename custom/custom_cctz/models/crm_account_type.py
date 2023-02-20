from odoo import fields, models, api


class SectorInfo(models.Model):
    _name = 'account.type'
    _description = "Account Type"

    name = fields.Char(required=True)
