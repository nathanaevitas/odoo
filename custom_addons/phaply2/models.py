# -*- coding: utf-8 -*-

from openerp import models, fields, api

class phaply2(models.Model):
    _name = 'res.partner'
    
    _inherit = 'res.partner'
    
    thietke = fields.Boolean(string='Thiet ke')
    thicong = fields.Boolean(string='Thi cong')
    cohoihoptac = fields.Many2one(string='Co hoi hop tac', comodel_name='phaply2.cohoi')
    
    hoso = fields.Many2many(string="Ho so", comodel_name='phaply2.hoso', relation='hosophaply_rel', column1='hoso_id', column2='name')
    
class cohoihoptac(models.Model):
    _name = 'phaply2.cohoi'
    
    name = fields.Char(string='Co hoi hop tac')