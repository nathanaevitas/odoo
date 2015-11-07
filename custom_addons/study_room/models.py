# -*- coding: utf-8 -*-

from openerp import models, fields, api

class study_room(models.Model):
    _name = 'study.room'
    
    @api.one
    @api.depends('student_ids')
    def _get_no_of_students(self):
        self.no_of_students = len(self.student_ids)
    
    name = fields.Char(string="Name", required=True)
    teacher_ids = fields.Many2many(string="Teachers", comodel_name="hr.employee", relation="room_teacher_rel", column1="room_id", column2="teacher_id")
    student_ids = fields.One2many(string="Students", comodel_name="students.students", inverse_name="room_id")
    no_of_students = fields.Integer(string="Number of Students", compute="_get_no_of_students", store=True, help="This field show the number of students")
    
    @api.one
    @api.constrains('no_of_students')
    def _check_no_of_students(self):
        if self.no_of_students > 2:
            raise Warning('You cannot add more than 2 student!')