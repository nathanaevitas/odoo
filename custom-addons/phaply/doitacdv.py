# -*- coding: utf-8 -*-

from openerp import models, fields, api

class doitacdv(models.Model):
    _name = 'phaply.doitacdv'
    
    name = fields.Many2one(string='Ten doi tac', comodel_name='phaply.tendoitac')
    mobile = fields.Char(string='SDT', related='name.mobile')
    type = fields.Many2one(string='Hang muc chi', comodel_name='phaply.hangmucdt')
    cost = fields.Float(string='Chi phi')
    
    hoso_id = fields.Many2one(string='Ho so ID', comodel_name='phaply.hoso')
    
class tendoitac(models.Model):
    _name = 'phaply.tendoitac'
    
    name = fields.Char(string='Ten doi tac')
    mobile = fields.Char(string='SDT')
    service = fields.Many2one(string='Dich vu', comodel_name='phaply.service')
    district = fields.Many2one(string='Quan', comodel_name='res.country.state')
    type = fields.Many2one(string='Hang muc chi', comodel_name='phaply.hangmucdt')
    cost = fields.Float(string='Chi phi trung binh')


class hangmucdt(models.Model):
    _name = 'phaply.hangmucdt'
    
    name = fields.Char(string='Hang muc')