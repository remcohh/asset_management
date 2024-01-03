from odoo import models, fields, api

class Option(models.Model):
    _name = 'am.option'
    _description = 'Option'
    name = fields.Char(string="Optie")
