# -*- coding: utf-8 -*-
from odoo import http

# class InterAlumno(http.Controller):
#     @http.route('/inter_alumno/inter_alumno/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inter_alumno/inter_alumno/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inter_alumno.listing', {
#             'root': '/inter_alumno/inter_alumno',
#             'objects': http.request.env['inter_alumno.inter_alumno'].search([]),
#         })

#     @http.route('/inter_alumno/inter_alumno/objects/<model("inter_alumno.inter_alumno"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inter_alumno.object', {
#             'object': obj
#         })