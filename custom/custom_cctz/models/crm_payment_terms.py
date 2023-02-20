from odoo import fields, models, api


class PaymentTerms(models.Model):
    _name = 'payment.terms'
    _description = "Purchase Time Frame"

    name = fields.Char(required=True)