from odoo import fields, models, api, _

class HostipatlPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = 'hospital patient management'
    
    name = fields.Char(string='Name', tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,                            
                           index=True, default=lambda self: _('New'))            
                            
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection(
        [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),    
        ], default='male', string='Gender', tracking=True
    )
    note = fields.Text(string='Description', tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Responsible", tracking=True)

    @api.model
    def create(self, values):
        if not values.get('note'):
            values['note'] = 'New Patient'
        if values.get('reference', ('New')) == _('New'):
            values['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        result = super(HostipatlPatient, self).create(values)        
        return result
        
       