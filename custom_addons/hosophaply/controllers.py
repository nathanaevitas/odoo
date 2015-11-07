# -*- coding: utf-8 -*-
from openerp import http

# class Hosophaply(http.Controller):
#     @http.route('/hosophaply/hosophaply/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hosophaply/hosophaply/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hosophaply.listing', {
#             'root': '/hosophaply/hosophaply',
#             'objects': http.request.env['hosophaply.hosophaply'].search([]),
#         })

#     @http.route('/hosophaply/hosophaply/objects/<model("hosophaply.hosophaply"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hosophaply.object', {
#             'object': obj
#         })