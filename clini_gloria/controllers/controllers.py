# -*- coding: utf-8 -*-
from odoo import http

# class CliniGloria(http.Controller):
#     @http.route('/clini_gloria/clini_gloria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clini_gloria/clini_gloria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clini_gloria.listing', {
#             'root': '/clini_gloria/clini_gloria',
#             'objects': http.request.env['clini_gloria.clini_gloria'].search([]),
#         })

#     @http.route('/clini_gloria/clini_gloria/objects/<model("clini_gloria.clini_gloria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clini_gloria.object', {
#             'object': obj
#         })