from odoo import fields, api, models, _ 


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    pre_sale_id = fields.Many2one('res.users', string='Pre-Sales Person')

