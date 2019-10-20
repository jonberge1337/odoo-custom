# -*- coding: utf-8 -*-

from odoo import models, fields, api

class producto_internet_jon(models.Model):
    _name = 'producto.internet_jon'

    codigo = fields.Char(required=True, size=15, required=True)
    nombre = fields.Char(string="Nombre", size=25)
    descripcion = fields.Char(string="Descripción", size=40)
    foto = fields.Binary()
    pertenece = fields.Many2one(comodel_name="lote.internet_jon", string="pertenece al lote")

class lote_internet_jon(models.Model):
    _name = "lote.internet_jon"

    catnum = fields.Integer(string="Número de catalogo", required=True)
    salida = fields.Float(string="Precio de salida", digits=2)
    desc = fields.Char(string="Descripción", size=50)
    tiempo = fields.Datetime(string="Fecha")
    productos = fields.One2many(comodel_name="producto.inverse_name", inverse_name="producto")



class cliente_internet_jon(models.Model):
    _name = "cliente.internet_jon"

    usuario = fields.Char(string="Usuario", required=True, size=15)
    nombre = fields.Char(string="Nombre", 20)
    clave = fields.Char(string="Contraseña", size=50)
    email = fields.Char(string="Email", size=50)
    


class puja_internet_jon(models.Model):
    _name = "puja.internet_jon"

    usuario = fields.Many2one(comodel_name="cliente.internet_jon")
    catnum = fields.Many2one(comodel_name="lote.internet_jon")
    dia = fields.Date()
    hora = fields.Datetime()
    cantidad = fields.Float(string="Cantidad pujado", digits=2)
