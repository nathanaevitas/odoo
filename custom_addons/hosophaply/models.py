# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hosophaply(models.Model):
    _name = 'hosophaply.hosophaply'

    name = fields.Char(string='Ten ho so')
    tenkhachhang = fields.Char(string='Ten KH')
    sdt = fields.Integer(string='So dien thoai')
    yeucau = fields.Text(string='Yeu cau KH')
    ngayhentra = fields.Date(string='Ngay hen tra')
    
    phidichvu = fields.Float(string='Phi dich vu')
    daung = fields.Float(string='Da ung')
    
    diachi = fields.Char(string='Dia chi')
    xaphuong = fields.Char(string='Xa / Phuong')
    quanhuyen = fields.Char(string='Quan / Huyen')
    
    nguoilam = fields.Char(string='Nguoi lam HS')
    ngaytiepnhan = fields.Date(string='Ngay tiep nhan')
    biennhanhs = fields.Date(string='Ngay bien nhan')
    ngaygiaohs = fields.Date(string='Ngay giao HS')
    
    phanhoi = fields.Text(sring='Phan hoi')
    lydo = fields.Text(string='Ly do')
    
    ghichu= fields.Text(string='Ghi chu')
    
    