# -*- coding: utf-8 -*-

from openerp import models, fields, api

class phaply(models.Model):
    """
    This class will create a new table in DB with the same and replace the '.' with '_'
    """
    _name = 'phaply.phaply'
    
    name = fields.Many2one(string='Ten KH', comodel_name='res.partner', required=True)
    ngaysinh = fields.Date(string='Ngay sinh')
    gioitinh = fields.Selection([('m', 'Nam'), ('f', 'Nu')], string='Gioi tinh')
    
    quan = fields.Char(string='Quan')
    ngaytiepnhan = fields.Datetime(string='Ngay gio tiep nhan')
    email = fields.Char(string='Email', store=True, readonly=True, related='name.email')
    phone = fields.Char(string='Mobile', store=True, readonly=True, related='name.mobile')
    nguon = fields.Many2one(string='Nguon', comodel_name='phaply.nguon')
    
    dv_thietke = fields.Boolean(string='Da co thiet ke')
    dv_thicong = fields.Boolean(string='Da co thi cong')
    dv_doitac = fields.Many2one(string='Doi tac', comodel_name='phaply.doitac')
    
    dichvu = fields.Many2one(string='Dich vu', comodel_name='phaply.dichvu')
    phutrach = fields.Many2one(string='Nguoi phu trach', comodel_name='hr.employee')
    
    trangthai = fields.Selection([('d', 'Dang deal'), ('y', 'Da chot'), ('n', 'Khong duoc')], string='Trang thai')
    
    hoatdong = fields.Many2many(string='Hoat dong', comodel_name='hoatdongpl.hoatdongpl', relation='hoatdong_pl_rel', column1='hoatdong_id', column2='phutrach')
    hoso = fields.Many2many(string="Ho so", comodel_name='hosophaply.hoso', relation='hosophaply_rel', column1='hoso_id', column2='name')
    
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
    
class doitac(models.Model):
    """
    Dich vu phap ly
    """
    _name = 'phaply.doitac'
    
    name = fields.Char(string='Doi tac')
    doitac_id = fields.One2many(string='Doi tac ID', comodel_name='phaply.phaply', inverse_name='dv_doitac')