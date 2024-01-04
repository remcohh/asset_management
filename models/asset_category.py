from odoo import models, fields

class AssetCategory(models.Model):
    _name = 'am.asset_category'
    _description = 'Device category'
    name = fields.Char('Name', required=True)
    