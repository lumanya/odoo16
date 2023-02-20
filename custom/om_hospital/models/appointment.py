from odoo import fields, models, api, _

class HostipatlAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = 'hospital appointment'
    
    
    name = fields.Char(string='Order name', required=True, copy=False, readonly=True,                            
                           index=True, default=lambda self: _('New'))            
   
    note = fields.Text(string='Description', tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Responsible", tracking=True)

    @api.model
    def create(self, values):
        if not values.get('note'):
            values['note'] = 'New Patient'
        if values.get('name', ('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        result = super(HostipatlAppointment, self).create(values)        
        return result
        
       