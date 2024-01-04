from odoo import models, fields, api

class Device(models.Model):
    _name = 'am.device'
    _description = 'Device Model'
    _rec_name = 'rec_name'
    rec_name = fields.Char(compute='_compute_fk_label', store=False) 
    category_id = fields.Many2one('am.asset_category', string='Device category')
    brand = fields.Char(string='Brand')
    model_name = fields.Char(string='Type')
    
    @api.depends('category_id')
    def _compute_fk_label(self):
        for t in self:
            t.rec_name = f'{t.category_id.name}: {t.brand} {t.model_name}'