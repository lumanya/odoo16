from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'
    _order = 'name asc'
    name = fields.Char(string='Tag', required=True)
    color = fields.Integer(string="Color")
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
        'tag name must be unique')
    ]