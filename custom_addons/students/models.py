# -*- coding: utf-8 -*-

from openerp import models, fields, api

class students(models.Model):
    """
    This class will create a new table in DB with the same and replace the '.' with '_'
    """
    _name = 'students.students'
    
    def _set_is_active(self):
        return True
    
    name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    
    gender = fields.Selection([('m', 'Male'), ('f', 'Female')], string='Gender', default='m')
    is_active = fields.Boolean(string='Active', default=_set_is_active)
    birth_date = fields.Date(string='Birth Date', default=fields.Date.today())
    room_id = fields.Many2one(string='Study Room', comodel_name='study.room')
    
    _sql_constraints = [('unique_email', 'unique(email)', 'This email is already exist!')]