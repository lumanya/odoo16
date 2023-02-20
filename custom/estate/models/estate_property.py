from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property Application"
    _order = "id desc"

    default_date = datetime.now() + timedelta(days=90)
   
    user_id = fields.Many2one('res.users')
    offer_ids = fields.Many2many('estate.property.offer')
    tag_ids = fields.Many2many('estate.property.tag')
    salesperson_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', copy=False, string='Buyer')
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=default_date)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    gardern_orientation = fields.Selection(
        [
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West')
        ]
    )
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        [
        ('New', 'New'),
        ('Offer Received', 'Offer Received'),
        ('Offer Accepted', 'Offer Accepted'),
        ('Sold', 'Sold'),
        ('Cancelled', 'Cancelled')
        ], default='New'
    )
    total_area = fields.Float(compute="_compute_total")
    best_price = fields.Float()

    @api.depends('garden_area', 'living_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    def action_set_sold(self):
        """ method to set sold status"""
        for record in self:
            if record.state != "Cancelled":
                record.state = "Sold"
            else:
                raise UserError('Cant Set sold Cancelled Property')
        return True
    def action_set_cancelled(self):
        """Method that set state cancelled"""
        for record in self:
            if record.state != 'Sold':
                record.state = "Cancelled"
            else:
                raise UserError('Cant Cancle Sold property')
        return True
    
    _sql_constraints = [
        ('check_postive_numer', 'CHECK(selling_price >= 0)',
        'The Selling Price must be postive')
    ]
    _sql_constraints = [
        ('check_postive_numer', 'CHECK(expected_price >= 0)',
        'The Expected Price must be postive')
    ]

    @api.ondelete(at_uninstall=False)
    def _unlink_except_state_New_Cancelled(self):
        for record in self:
            if record.state not in ('New', 'Cancelled'):
                raise UserError("You can't delete the record")
            
   

            

