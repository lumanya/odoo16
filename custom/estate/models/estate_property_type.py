from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'Estate Property Type'
    _order = "name asc"
    
    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence')
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
        'Property type name must be unique')
    ]