# -*- coding: utf-8 -*-
from odoo import http

# class OngJon(http.Controller):
#     @http.route('/ong_jon/ong_jon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ong_jon/ong_jon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ong_jon.listing', {
#             'root': '/ong_jon/ong_jon',
#             'objects': http.request.env['ong_jon.ong_jon'].search([]),
#         })

#     @http.route('/ong_jon/ong_jon/objects/<model("ong_jon.ong_jon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ong_jon.object', {
#             'object': obj
#         })