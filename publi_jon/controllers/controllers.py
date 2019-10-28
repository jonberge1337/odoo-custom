# -*- coding: utf-8 -*-
from odoo import http

# class PubliJon(http.Controller):
#     @http.route('/publi_jon/publi_jon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/publi_jon/publi_jon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('publi_jon.listing', {
#             'root': '/publi_jon/publi_jon',
#             'objects': http.request.env['publi_jon.publi_jon'].search([]),
#         })

#     @http.route('/publi_jon/publi_jon/objects/<model("publi_jon.publi_jon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('publi_jon.object', {
#             'object': obj
#         })