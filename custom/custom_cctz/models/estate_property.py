from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property Application"
    _order = "id desc"

    name = fields.Char()
   

            

