# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner_inherit(models.Model):
    _inherit = 'res.partner'
     
    design = fields.Boolean(string='Thiet ke')
    construct = fields.Boolean(string='Thi cong')
    legal = fields.Boolean(string='Phap ly')
    partner = fields.Many2one(string='Co hoi hop tac', comodel_name='phaply.cohoi')
    
    partner_create_date = fields.Date(string='Ngay tao', default=fields.Date.today, store=True)
    
    #hoso = fields.Many2many(string="Ho so", comodel_name='phaply2.hoso', relation='hosophaply_rel', column1='hoso_id', column2='name')
    docs = fields.One2many(comodel_name='phaply.hoso', inverse_name='customer')
    
    _order = 'partner_create_date desc'
    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(display_name)',
         "Ma ho so bi trung"),
        ('mobile_unique',
         'UNIQUE(mobile)',
         "SDT bi trung"),
        ('email_unique',
         'UNIQUE(email)',
         "Ma ho so bi trung"),
    ]
    
class cohoihoptac(models.Model):
    _name = 'phaply.cohoi'
    
    name = fields.Char(string='Co hoi hop tac')
    
class quanhuyen(models.Model):
    _name = 'phaply.quanhuyen'
    
    name = fields.Char(string='Quan huyen')
    
class service(models.Model):
    _name = 'phaply.service'
    
    name = fields.Char(string='Dich vu')
    
    hoso_ids = fields.One2many(string='Ho so', comodel_name='phaply.hoso', inverse_name='service')
    
    hoso_count = fields.Integer(
        string="Ho so count", compute='_get_hoso_count', store=True)
    
    @api.depends('hoso_ids')
    def _get_hoso_count(self):
        for r in self:
            r.hoso_count = len(r.hoso_ids)