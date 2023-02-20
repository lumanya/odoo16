from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'This is the module that shows real estate property'

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedroams = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    gardern_area = fields.Integer()
    gardern_orientation = fields.Selection([
        ('Upright', 'Upright'),
        ('potrait', 'potratit'),
    ])

