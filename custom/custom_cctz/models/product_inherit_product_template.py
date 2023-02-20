from odoo import fields, api, models, _   


class InheritProductTemplate(models.Model):
    _inherit = 'product.template'

    part_number = fields.Char(string="Part Number")
    business_unit_id = fields.Many2one('crm.team', string="Business Unit")
    manufacturer_id = fields.Many2one('manufacturer', string="Manufacturer")