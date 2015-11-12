# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hoso(models.Model):
    _name = 'phaply2.hoso'

    name = fields.Char(string='Ten ho so', required=True)
    tenkhachhang = fields.Many2one(string='Ten KH', comodel_name='res.partner', required=True)
    sdt = fields.Char(string='So dien thoai', related='tenkhachhang.phone', required=True)
    yeucau = fields.Text(string='Yeu cau KH')
    ngayhentra = fields.Date(string='Ngay hen tra')
    
    phidichvu = fields.Float(string='Phi dich vu')
    daung = fields.Float(string='Da ung')
    
    diachi = fields.Char(string='Dia chi')
    xaphuong = fields.Char(string='Xa / Phuong')
    quanhuyen = fields.Char(string='Quan / Huyen')
    
    nguoilam = fields.Many2one(string='Nguoi lam HS', comodel_name='hr.employee')
    ngaytiepnhan = fields.Date(string='Ngay tiep nhan')
    biennhanhs = fields.Date(string='Ngay bien nhan')
    ngaygiaohs = fields.Date(string='Ngay giao HS')
    
    phanhoi = fields.Text(string='Phan hoi')
    lydo = fields.Text(string='Ly do')
    
    ghichu= fields.Text(string='Ghi chu')
    
    hoso_id = fields.Many2one(string='Ho so', comodel_name='res.partner')