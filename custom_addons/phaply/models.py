# -*- coding: utf-8 -*-

from openerp import models, fields, api

class phaply(models.Model):
    """
    This class will create a new table in DB with the same and replace the '.' with '_'
    """
    _name = 'phaply.phaply'
    
    name = fields.Char(string='Ten KH')
    ngaysinh = fields.Date(string='Ngay sinh')
    gioitinh = fields.Selection([('m', 'Nam'), ('f', 'Nu')], string='Gioi tinh')
    
    quan = fields.Char(string='Quan')
    ngaytiepnhan = fields.Datetime(String='Ngay gio tiep nhan')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    nguon = fields.Many2one(string='Nguon', comodel_name='phaply.nguon')
    
    dv_thietke = fields.Boolean(string='Da co thiet ke')
    dv_thicong = fields.Boolean(string='Da co thi cong')
    dv_doitac = fields.Char(string='Doi tac')
    
    dichvu = fields.Many2one(string='Dich vu', comodel_name='phaply.dichvu')
    phutrach = fields.Many2one(string='Nguoi phu trach', comodel_name='hr.employee')
    
    da_chot = fields.Boolean(string='Da chot')
    
class nguon(models.Model):
    """
    Luu tru nguon khach hang
    """
    _name = 'phaply.nguon'
    
    name = fields.Char(string='Nguon khach hang')
    nguon_id = fields.One2many(string='Nguon ID', comodel_name='phaply.phaply', inverse_name='nguon')
    
class dichvu(models.Model):
    """
    Dich vu phap ly
    """
    _name = 'phaply.dichvu'
    
    name = fields.Char(string='Dich vu')
    dichvu_id = fields.One2many(string='Dich vu ID', comodel_name='phaply.phaply', inverse_name='dichvu')