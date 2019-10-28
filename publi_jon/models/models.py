# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class publi_jon(models.Model):
#     _name = 'publi_jon.publi_jon'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class revista_publi_jon(models.Model):
    _name = "revista.publi_jon"

    issn = fields.Char(string="Numero de identificación", required=True, size=20)
    numero = fields.Integer(string="Numero")
    titulo = fields.Char(string="Titulo", size=40)
    año = fields.Date(string="Año")

class articulo_publi_jon(models.Model):
    _name = "articulo.publi_jon"

    titulo = fields.Char(string="Titulo", size=30, required=True)
    inicio = fields.Date(string="Pagina de inicio")
    fin = fields.Date(string="Pagina final")
    relacion = fields.Many2one(string="Publicados", comodel_name="revista.publi_jon")
    
class escrito_publi_jon(models.Model):
    _name = "escrito.publi_jon"

    titulo = fields.Many2one(comodel_name="articulo.publi_jon")
    nombre = fields.Many2one(comodel_name="autor.publi_jon")
    posicion = fields.Integer()


class autor_publi_jon(models.Model):
    _name = "autor.publi_jon"

    nombre = fields.Char(string="Nombre", required=True, size=20)
    email = fields.Char(string="Email", size=40)
    adscrip = fields.Char(string="Adscripción", size=40)


