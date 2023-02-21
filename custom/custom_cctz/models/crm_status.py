from odoo import fields, models, api, _    


class CrmStatus(models.Model):
    _name = 'crm.status'
    _description = 'CRM status'

    name = fields.Char(string="Status", required=True)
