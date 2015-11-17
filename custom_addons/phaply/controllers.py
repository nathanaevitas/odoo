# -*- coding: utf-8 -*-
from openerp import http

# class Phaply2(http.Controller):
#     @http.route('/phaply2/phaply2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phaply2/phaply2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phaply2.listing', {
#             'root': '/phaply2/phaply2',
#             'objects': http.request.env['phaply2.phaply2'].search([]),
#         })

#     @http.route('/phaply2/phaply2/objects/<model("phaply2.phaply2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phaply2.object', {
#             'object': obj
#         })