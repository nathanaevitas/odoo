# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hoso(models.Model):
    _name = 'phaply.hoso'
    
    create_date_only = fields.Date(string='Ngay tao', default=fields.Date.today)

    name = fields.Char(string='Ma ho so', required=True)
    
    customer = fields.Many2one(string='Khach hang', comodel_name='res.partner', domain=[('customer','=',1)])
    phone = fields.Char(string='SDT', related='customer.mobile', required=True)
    request = fields.Text(string='Yeu cau KH')
    deadline = fields.Date(string='Ngay hen tra')
    
    service = fields.Many2one(string='Dich vu', comodel_name='phaply.service')
    cost = fields.Float(string='Phi dich vu')
    paid = fields.Float(string='Da ung')
    
    address = fields.Char(string='Dia chi', related='customer.street')
    ward = fields.Char(string='Xa / Phuong')
    district = fields.Many2one(string='Quan / Huyen', related='customer.state_id', store=True)
    
    emloyee = fields.Many2one(string='Nguoi lam HS', comodel_name='res.users')
    responsible_id = fields.Many2one(string='Nguoi thu ly', comodel_name='res.users')
    
    day_reception = fields.Date(string='Ngay tiep nhan')
    date_start = fields.Date(string='Ngay bien nhan')
    date_end = fields.Date(string='Ngay giao HS')
    
    feedback = fields.Text(string='Phan hoi')
    reason = fields.Text(string='Ly do')
    
    note = fields.Text(string='Ghi chu')
    
    doc_id = fields.Many2one(string='Ho so', comodel_name='res.partner')
    
    partner_paid = fields.One2many(string='Thu chi doi tac', comodel_name='phaply.doitacdv', inverse_name='hoso_id')
    
    due_date_from = fields.Date(string="Due date from")
    due_date_to = fields.Date(string="Due date to")
    
    
    #@api.onchange('customer','service')
    #def _auto_generate_id(self):
    #    for record in self:
    #        self.name= "%s-%s" % (self.customer, self.service)
    
    state = fields.Selection([
        ('new', "Nhan lam"),
        ('working', "Dang lam"),
        ('fail', "That bai"),
        ('done', "Da xong"),
    ])

    @api.multi
    def action_new(self):
        self.state = 'new'

    @api.multi
    def action_working(self):
        self.state = 'working'

    @api.multi
    def action_fail(self):
        self.state = 'fail'
        
    @api.multi
    def action_done(self):
        self.state = 'done'
        
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Ma ho so bi trung"),
    ]

    _order = 'create_date_only desc'
        