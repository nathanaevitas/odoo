# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hoatdongpl(models.Model):
    _name = 'hoatdongpl.hoatdongpl'
    
    name = fields.Char(string='Ten hoat dong')
    loai = fields.Many2one(string='Loai hoat dong', comodel_name='hoatdongpl.loai')
    ngaygio = fields.Datetime(string='Ngay gio')
    ketqua = fields.Many2one(string='Ket qua', comodel_name='hoatdongpl.ketqua')
    ghichu = fields.Text(string='Ghi chu')
    hoatdong_id = fields.Many2one(string='Hoat dong', comodel_name='phaply.phaply')
    
class loaihoatdong(models.Model):
    _name = 'hoatdongpl.loai'
    
    name = fields.Char(string='Loai hoat dong')
    loaihoatdong_id = fields.One2many(string='Hoat dong ID', comodel_name='hoatdongpl.hoatdongpl', inverse_name='loai')
    
class ketquahd(models.Model):
    _name = 'hoatdongpl.ketqua'
    
    name = fields.Char(string='Ten ket qua')
    ketqua_id = fields.One2many(string='Ket qua ID', comodel_name='hoatdongpl.hoatdongpl', inverse_name='ketqua')