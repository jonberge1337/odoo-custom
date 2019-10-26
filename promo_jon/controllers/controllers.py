# -*- coding: utf-8 -*-
from odoo import http

# class PromoJon(http.Controller):
#     @http.route('/promo_jon/promo_jon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/promo_jon/promo_jon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('promo_jon.listing', {
#             'root': '/promo_jon/promo_jon',
#             'objects': http.request.env['promo_jon.promo_jon'].search([]),
#         })

#     @http.route('/promo_jon/promo_jon/objects/<model("promo_jon.promo_jon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('promo_jon.object', {
#             'object': obj
#         })