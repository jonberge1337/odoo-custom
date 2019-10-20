# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ciclista_ciclista_jon(models.Model):
    _name = "ciclista.ciclista_jon"

    nombre = fields.Char(string="Nombre del Ciclista", size=20, required=True)
    nacion = fields.Char(string="Nación", size=20)
    fnac = fields.Date(string="Fecha de Nacimiento")
    ganador = fields.One2Many(comodel_name="prueba.ciclista_jon", inverse_name="ganador")

class equipo_ciclista_jon(models.Model):
    _name = "equipo.ciclista_jon"

    nombre = fields.Char(string="Nombre del Equipo", size=20, required=True)
    nacion = fields.Char(string="Nación", size=20)
    direct = fields.Char(string="Director", size=20)
    
class prueba_ciclista_jon(models.Model):
    _name = "prueba.ciclista_jon"

    nombre = fields.Char(string="Nombre de la prueba", size=10, required=True)
    aino = fields.Date(string="Año de Edición")
    etapas = fields.Integer(string="Nº de Etapas", size=2)
    km = fields.Integer(string="Kilómetros")
    ganador = fields.Many2one(comodel_name="ciclista.ciclista_jon")

class participacion_ciclista_jon(models.Model):
    _name = "participacion.ciclista_jon"

    nombrep = fields.Many2one(comodel_name="prueba.ciclista_jon")
    nombree = fields.Many2One(comodel_name="equipo.ciclista_jon")
    puesto = fields.Integer()

class plantilla_ciclista_jon(models.Model):
    nombrec = fields.Char(string="Nombre Ciclista")
    nombree = fields.Char(string="Nombre del equipo")
    inicio = fields.Date(string="Inicio")
    fin = fields.Date(string="Final")
    
