from odoo import api, fields, models, _   


class CustomerType(models.Model):
    _name = "customer.type"

    name = fields.Char(required=True)
    