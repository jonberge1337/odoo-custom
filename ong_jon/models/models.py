# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class ong_jon(models.Model):
#     _name = 'ong_jon.ong_jon'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class sede_ong_jon(models.Model):
    _name = 'sede.ong_jon'

    id = fields.Integer(string="ID", required=True)
    ciudad = fields.Char(string="Ciudad", size=40)
    pais = fields.Char(string="Pais", size=40)
    direccion = fields.Char(string="Dirección", size=50)
    tfno = fields.Char(string="Telefono", size=12)
    director = fields.Char(string="Nombre del director", size=40)

class proyecto_ong_jon(models.Model):
    _name = 'proyecto.ong_jon'

    cod = fields.Char(string="Código", size=20, required=True)
    titulo = fields.Char(string="Titulo", size=40)
    inicio = fields.Date(string="Fecha de inicio")
    fin = fields.Date(string="Fecha final")
    presup = fields.Float(string="Presupuesto asignado", digits=2)
    resp = fields.Char(string="Nombre del responsable", size=40)

class actuacion_ong_jon(models.Model):
    _name = 'actuacion.ong_jon'

    cod = fields.Many2one(comodel_name="proyecto.ong_jon", string="Código del proyecto")
    idpon = fields.Many2one(comodel_name="poblacio.ong_jon", string="Código de la población")
    inversion = fields.Float(string="Inversion", digits=2)
    descrip = fields.Char(string="Descripción", size=50)

class poblacion_ong_jon(models.Model):
    _name = 'poblacion.ong_jon'

    idpob = fields.Integer(string="ID de la polación")
    nombre = fields.Char(string="Nombre", size=40)
    pais = fields.Char(string="Pais", size=40)
    habitantes = fields.Integer()


