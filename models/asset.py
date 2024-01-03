from odoo import models, fields, api


class Asset(models.Model):
    _name = 'am.asset'
    _description = 'Asset Model'
    _rec_name = 'device_id'
    device_id = fields.Many2one('am.device', string='Apparaat')
    employee_id = fields.Many2one('hr.employee', string='Huidige medewerker')
    loan_agreement_id = fields.Many2one(
        'am.loan_agreement', string='Gekoppeld aan gebruikersovereenkomst')
    serial = fields.Char(string='Serienummer')
    options = fields.Many2many('am.option', string='Opties')
    imei_number = fields.Char(string='IMEI nummer')
    phone_number = fields.Char(string='Telefoon nummer')
    nb_number = fields.Char(string='NB nummer')
    remarks = fields.Html(string='Opmerkingen')
    category_name = fields.Char(
        string='Apparaat categorie', related='device_id.category_id.name')
    options_str = fields.Char()
    
    def action_create_loan_agreement(self):
        loan_agreement = self.env['am.loan_agreement'].create({"employee_id": self.get_employee_from_user().id})
        for asset in self.browse(self.env.context['active_ids']):
            self.env['am.loan_agreement_line'].create(
                {'loan_agreement_id': loan_agreement.id, 'asset_id': asset.id})
            asset.write({'employee_id': loan_agreement.employee_id})
            asset.write({'loan_agreement_id': loan_agreement.id})
            asset.write({'options_str': self._compute_option_str(asset)})
        return {
            'name': self.display_name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'am.loan_agreement',
            'res_id': loan_agreement.id,
        }  
        
    def _compute_option_str(self,asset):
        if asset.options:
            return ', '.join([option.name for option in asset.options])        
        return ''
    
    @api.model
    def get_employee_from_user(self):
        current_user_id = self.env.uid
        employee_model = self.env['hr.employee']
        employee = employee_model.search([('user_id', '=', current_user_id)], limit=1)
        return employee        
        