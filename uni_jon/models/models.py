# -*- coding: utf-8 -*-

from odoo import models, fields, api

class persona_uni_jon(models.Model):
    _name = 'persona.uni_jon'

    pid = fields.Char(string="Identificador", size=10, required=True, help="E,P: estudiante,profesor")
    nombre = fields.Char(string="Nombre", size=20)
    tlfno = fields.Char(string="Telefono", size=9)
    directorio = fields.Char(string="Direccion", size=70)
    email = fields.Char(size=40)

class profesor_uni_jon(models.Model):
    _name = "profesor.uni_jon"

    ded = fields.Selection(string="Dedicacion", selection=[("Completa", 1), ("Parcial", 2), ("Colaboracion", 3)], size=40)
    imparte_en = fields.Many2many(comodel_name="centro.uni_jon", relation="uniProfe", colum1="idprofe", colum2="idcentro")

class centro_uni_jon(models.Model):
    _name = "centro.uni_jon"
    _rec_nombre = "nombrec"

    nombrec = fields.Char(string="Nombre centro", required=True, size=40)
    sus_alumnos = fields.One2many(comodel_name="alumno.uni_jon", inverse_name="su_centro", string="Alumnos matriculados")
    claustro = fields.Many2many(comodel_name="profesor.uni_jon", relation="uniProfe", colum1="idcentro", colum2="idprofe")

class alumno_uni_jon(models.Model):
    _name = "alumno.uni_jon"

    exp = fields.Char(string="Expediente", required=True, size=40)
    titulacion = fields.Char(string="Titulacion", size=40)
    su_centro = fields.Many2one(comodel_name="centro.uni_jon", string="Estudia") 

class personal_uni_jon(models.Model):
    _name = "personal.uni_jon"

    unidad = fields.Char(string="Unidad",required=True, size=15)
    categoria = fields.Char(string="Categoria", size=30)
