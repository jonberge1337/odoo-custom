# -*- coding: utf-8 -*-
from odoo import http

# class Cebanc(http.Controller):
#     @http.route('/cebanc/cebanc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cebanc/cebanc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cebanc.listing', {
#             'root': '/cebanc/cebanc',
#             'objects': http.request.env['cebanc.cebanc'].search([]),
#         })

#     @http.route('/cebanc/cebanc/objects/<model("cebanc.cebanc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cebanc.object', {
#             'object': obj
#         })