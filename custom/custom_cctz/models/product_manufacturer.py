from odoo import fields, models, api


class Manufacturer(models.Model):
    _name = 'manufacturer'
    _description = "Product Manufacturer"

    name = fields.Char(required=True)
