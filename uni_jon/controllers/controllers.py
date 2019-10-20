# -*- coding: utf-8 -*-
from odoo import http

# class UniJon(http.Controller):
#     @http.route('/uni_jon/uni_jon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uni_jon/uni_jon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('uni_jon.listing', {
#             'root': '/uni_jon/uni_jon',
#             'objects': http.request.env['uni_jon.uni_jon'].search([]),
#         })

#     @http.route('/uni_jon/uni_jon/objects/<model("uni_jon.uni_jon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uni_jon.object', {
#             'object': obj
#         })