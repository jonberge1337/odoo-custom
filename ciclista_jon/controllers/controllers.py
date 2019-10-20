# -*- coding: utf-8 -*-
from odoo import http

# class CiclistaJon(http.Controller):
#     @http.route('/ciclista_jon/ciclista_jon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ciclista_jon/ciclista_jon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ciclista_jon.listing', {
#             'root': '/ciclista_jon/ciclista_jon',
#             'objects': http.request.env['ciclista_jon.ciclista_jon'].search([]),
#         })

#     @http.route('/ciclista_jon/ciclista_jon/objects/<model("ciclista_jon.ciclista_jon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ciclista_jon.object', {
#             'object': obj
#         })