# -*- coding: utf-8 -*-
from openerp import http

# class Phaply(http.Controller):
#     @http.route('/phaply/phaply/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phaply/phaply/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phaply.listing', {
#             'root': '/phaply/phaply',
#             'objects': http.request.env['phaply.phaply'].search([]),
#         })

#     @http.route('/phaply/phaply/objects/<model("phaply.phaply"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phaply.object', {
#             'object': obj
#         })