# -*- coding: utf-8 -*-

from openerp import models, fields, api

class nguoithuly(models.Model):
    _name = 'phaply.nguoithuly'
    
    name = fields.Char(string='Nguoi thu ly')
    
    type = fields.Char(string='Loai dich vu')
    costperdoc = fields.Float(string='Tien / Ho So')
    advantage = fields.Text(string='Thuan loi')
    disadvantage = fields.Text(string='Kho khan')
    district = fields.Many2one(string='Khu vuc', comodel_name='res.country.state')