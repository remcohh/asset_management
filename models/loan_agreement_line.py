from odoo import models, fields, api

class LoanAgreementLine(models.Model):
    _name = 'am.loan_agreement_line'
    _description = 'Loan agreement line'
    _inherits={'am.asset': 'asset_id'}
    _rec_name = 'asset_id'
    loan_agreement_id = fields.Many2one('am.loan_agreement', string='Loan agreement')
    asset_id = fields.Many2one('am.asset', string='Configuration')
