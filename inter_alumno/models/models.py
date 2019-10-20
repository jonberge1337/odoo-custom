# -*- coding: utf-8 -*-

from odoo import models, fields, api

class producto_inter_alumno(models.Model):
    _name = 'producto.inter_alumno'

    codigo = fields.Char(size=15)
    nombre = fields.Char(size=20)
    descripcion = fields.Text()
    lote_es = fields.Many2one(lote)

class lote_inter_alumno(models.Model)
    _name = 'lote.inter_alumno'

    catnum = fields.Integer()
    salida = fields.
    pujamax = fields.Integer()
    tiempo = fields.

class cliente_inter_alumno(models.Model)
    _name = 'cliente.inter_alumno'

    usuario = 

class puja_inter_alumno(models.Model)
    _name = ''
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
