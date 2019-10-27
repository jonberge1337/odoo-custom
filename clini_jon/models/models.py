# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class clini_jon(models.Model):
#     _name  =  'clini_jon.clini_jon'

#     name  =  fields.Char()
#     value  =  fields.Integer()
#     value2  =  fields.Float(compute="_value_pc", store=True)
#     description  =  fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2  =  float(self.value) / 100

class doctor_clini_jon(models.Model):
    _name = "doctor.clini_jon"
    _rec_name = "codigo"

    codigo = fields.Char(string="Código Médico", required=True, help="El código es alfanumérico", size=20)
    nombre = fields.Char(string="Nombre", size=20)
    especialidad = fields.Selection(string="Especialidad", required=True, selection=[("familia", 'Medicina de familia'), ("trauma", 'Traumatología'), ("nefro", 'Nefrología'), ("pediatra", 'Pediatría'), ("cardio", 'Cardiología')])
    sus_tratamientos = fields.One2many(string="Atenciones/Tratamiento", comodel_name="historial.clini_jon", inverse_name="doctor")

class unidad_clini_jon(models.Model):
    _name = "unidad.clini_jon"
    _rec_name = "id"

    idUnidad = fields.Selection(string="Identificador Unidad", required=True, selection=[("familia", 'Medicina de familia'), ("trauma", 'Traumatología'), ("nefro", 'Nefrología'), ("pediatra", 'Pediatría'), ("cardio", 'Cardiología')])
    nombre = fields.Char(string="Nombre Completo Unidad", size=100, help="Escriba si es necesario especificar algo más aparte del identificador")
    planta = fields.Integer(string="Número de planta")

class paciente_clini_jon(models.Model):
    _name = "paciente.clini_jon"
    _rec_name = "ss"

    ss = fields.Char(string="Número de S.S.", size=12, required=True)
    nombre = fields.Char(string="Nombre del paciente", size=20)
    edad = fields.Integer(string="Edad del paciente")
    fechaIngreso = fields.Date(string="Fecha de ingreso")
    unidad = fields.Many2one(string="Unidad de ingreso", comodel_name="unidad.clini_jon")
    sus_ingresos = fields.One2many(string="Ingresos", comodel_name="historial.clini_jon", inverse_name="paciente")
class historial_clini_jon(models.Model):
    _name = "historial.clini_jon"

    sintoma = fields.Char(string="Síntomas", size=100)
    tratamiento = fields.Text(string="Tratamiento")
    fechaInicio = fields.Date(string="Fecha inicio tratamiento")
    fechaFin = fields.Date(string="Fecha final tratamiento")
    doctor = fields.Many2one(string="Médico asignado", comodel_name="doctor.clini_jon")
    paciente = fields.Many2one(string="Paciente", comodel_name="paciente.clini_jon")
