from odoo import models, fields

class AssetCategory(models.Model):
    _name = 'am.asset_category'
    _description = 'Apparaat categorie'
    name = fields.Char('Name', required=True)
    