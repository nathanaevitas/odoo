# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hoso(models.Model):
    _name = 'phaply.hoso'

    name = fields.Char(string='Ten ho so', required=True)
    customer = fields.Many2one(string='Khach hang', comodel_name='res.partner', required=True)
    phone = fields.Char(string='So dien thoai', related='customer.phone', required=True)
    request = fields.Text(string='Yeu cau KH')
    deadline = fields.Date(string='Ngay hen tra')
    
    cost = fields.Float(string='Phi dich vu')
    paid = fields.Float(string='Da ung')
    
    address = fields.Char(string='Dia chi')
    ward = fields.Char(string='Xa / Phuong')
    district = fields.Char(string='Quan / Huyen')
    
    emloyee = fields.Many2one(string='Nguoi lam HS', comodel_name='hr.employee',
        domain=['&', ('active', '=', True),
                     ('department_id.name', '=', "Phap Ly")])
    day_reception = fields.Date(string='Ngay tiep nhan')
    date_start = fields.Date(string='Ngay bien nhan')
    date_end = fields.Date(string='Ngay giao HS')
    
    feedback = fields.Text(string='Phan hoi')
    reason = fields.Text(string='Ly do')
    
    note = fields.Text(string='Ghi chu')
    
    doc_id = fields.Many2one(string='Ho so', comodel_name='res.partner')
    
    state = fields.Selection([
        ('new', "Moi nhan"),
        ('working', "Dang lam"),
        ('done', "Da xong"),
    ])

    @api.multi
    def action_new(self):
        self.state = 'new'

    @api.multi
    def action_working(self):
        self.state = 'working'

    @api.multi
    def action_done(self):
        self.state = 'done'
