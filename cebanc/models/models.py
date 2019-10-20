# -*- coding: utf-8 -*-

from odoo import models, fields, api

class alumnosCebanc(models.Model):
    _name = 'alumnos.cebanc'

    name = fields.Char(required=True, string="Nombre", size=35)
    edad = fields.Integer()
    nota = fields.Float(string="Nota media", digits=(2,2))
    description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
