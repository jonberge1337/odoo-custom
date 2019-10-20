# -*- coding: utf-8 -*-
from odoo import http

# class InternetJon(http.Controller):
#     @http.route('/internet_jon/internet_jon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/internet_jon/internet_jon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('internet_jon.listing', {
#             'root': '/internet_jon/internet_jon',
#             'objects': http.request.env['internet_jon.internet_jon'].search([]),
#         })

#     @http.route('/internet_jon/internet_jon/objects/<model("internet_jon.internet_jon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('internet_jon.object', {
#             'object': obj
#         })