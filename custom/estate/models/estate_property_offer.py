from odoo import models, fields, api, exceptions

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection([
        ('Accepted', 'Accepted'),
        ('Refused', 'Refused')
    ], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    
    def action_accepted(self):
        """set state to accepted"""
        for record in self:
            record.status = 'Accepted'            
        return True
    
    def action_refused(self):
        """set Refused status"""
        for record in self:
            record.status = 'Refused'
        return True
    
    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0)',
         'The price must be postive')
    ]

    @api.model 
    def create(self, vals):
        property_obj = self.env['estate.property'].browse(vals['property_id'])
        property_obj.state = 'Offer Received'
        existing_offer = self.search([('property_id', '=', vals['property_id'])], limit=1).price
        if vals['price'] < existing_offer:
            raise exceptions.ValidationError('This offer is lower than existing offer')
        return super().create(vals)
    