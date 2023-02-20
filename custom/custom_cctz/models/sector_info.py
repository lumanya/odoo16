from odoo import fields, models, api


class SectorInfo(models.Model):
    _name = 'sector.info'
    _description = "Sector Info"

    name = fields.Char(required=True)
    full_name = fields.Char()

    