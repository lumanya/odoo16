from odoo import fields, api, models, _ 


class CrmLead(models.Model):
    _inherit = 'crm.lead'
   
    pre_sale_id = fields.Many2one('res.users', string='Pre-Sales Person')
    account_manager = fields.Many2one('res.users', string='Account Manager')
    source = fields.Many2one('res.users', string='Source')
    business_unit = fields.Many2one('crm.team', string="Business Unit")
    account_type_id = fields.Many2one('account.type', string='Account Type')
    purchase_time_frame_id = fields.Many2one('purchase.time', string="Purchase Time Frame")
    payment_terms_id = fields.Many2one('payment.terms', string="Payment Terms")
    status_id = fields.Many2one('crm.status', string="status")
    cc_margin = fields.Integer(string="CC Margin")
    tender_status = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No')
    ], string="Tender Status")
    renewable_subscription = fields.Selection([
        ('None', 'None'),
        ('First Time Opportunity With Subscription', 'First Time Opportunity With Subscription'),
        ('Re-occuring Opportunity With Subscription', 'Re-occuring Opportunity With Subscription')
    ], string="Renewable Subscription")
    cc_care = fields.Selection([
        ('None', 'None'),
        ('Breake and Fix', 'Break and Fix'),
        ('Install', 'Install'),
        ('Remote', 'Remote'),
        ('Managed', 'Managed')
    ])
    

