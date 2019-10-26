# -*- coding: utf-8 -*-

from odoo import models, fields, api

class promocion_promo_jon(models.Model):
    _name = 'promocion.promo_jon'

    codigop = fields.Char(string="Codigo", required=True)
    nombre = fields.Char(string="Nombre", size=20)
    poblacion = fields.Char(string="Poblacion", size=30)
    plano = fields.Binary()

class contrado_promo_jon(models.Model):
    _name = "contrato.promo_jon"

    nombre = fields.Many2one(comodel_name="empresa.promo_jon")
    codigo = fields.Many2one(comodel_name="promocion.promo_jon")
    importe = fields.Float(string="Importe", digits=2)

class empresa_promo_jon(models.Model):
    _name = "empresa.promo_jon"

    nombre = fields.Char(string="Nombre", required=True, size=40)
    tipo = fields.Char(string="Tipo", size=10)
    dir = fields.Char(string="Dirección", size=20)
    tfno = fields.Char(string="Teléfono", size=12)
    fax = fields.Char(string="Fax", size=12)
    email = fields.Char(string="Email", size=12)

class vivienda_promo_jon(models.Model):
    _name = "vivienda.promo_jon"

    id = fields.Char(string="ID", required=True)
    superficie = fields.Integer(string="Superficie")
    hab = fields.Integer(string="Nº de Habitaciones")
    baños = fields.Integer(string="Nº de Baños")
    plano = fields.Binary(string="Plano de la Vivienda")
    terraza = fields.Boolean(string="Terraza")
    jardin = fields.Boolean(string="Jardín")
    piscina = fields.Boolean(string="Piscina")
    garaje = fields.Boolean(string="Garaje")
    codigo = fields.Many2one(comodel_name="promocion.promo_jon", string="Promocion")

