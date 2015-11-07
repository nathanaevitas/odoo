# -*- coding: utf-8 -*-
from openerp import http

# class StudyRoom(http.Controller):
#     @http.route('/study_room/study_room/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/study_room/study_room/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('study_room.listing', {
#             'root': '/study_room/study_room',
#             'objects': http.request.env['study_room.study_room'].search([]),
#         })

#     @http.route('/study_room/study_room/objects/<model("study_room.study_room"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('study_room.object', {
#             'object': obj
#         })