# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner_inherit(models.Model):
    _name = 'res.partner'
    
    _inherit = 'res.partner'
    
    design = fields.Boolean(string='Thiet ke')
    construct = fields.Boolean(string='Thi cong')
    partner = fields.Many2one(string='Co hoi hop tac', comodel_name='phaply.cohoi')
    
    #hoso = fields.Many2many(string="Ho so", comodel_name='phaply2.hoso', relation='hosophaply_rel', column1='hoso_id', column2='name')
    docs = fields.One2many(comodel_name='phaply.hoso', inverse_name='customer')
    
class cohoihoptac(models.Model):
    _name = 'phaply.cohoi'
    
    name = fields.Char(string='Co hoi hop tac')
    