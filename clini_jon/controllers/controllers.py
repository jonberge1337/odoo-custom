# -*- coding: utf-8 -*-
from odoo import http

# class CliniJon(http.Controller):
#     @http.route('/clini_jon/clini_jon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clini_jon/clini_jon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clini_jon.listing', {
#             'root': '/clini_jon/clini_jon',
#             'objects': http.request.env['clini_jon.clini_jon'].search([]),
#         })

#     @http.route('/clini_jon/clini_jon/objects/<model("clini_jon.clini_jon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clini_jon.object', {
#             'object': obj
#         })