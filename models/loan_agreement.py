import base64
from odoo import models, fields, api


class LoanAgreement(models.Model):
    _name = 'am.loan_agreement'
    _description = 'Loan agreement'
    _rec_name = 'rec_name'
    rec_name = fields.Char(compute='_compute_rec_name', store=True)
    employee_id = fields.Many2one('hr.employee', string='Gebruiker')
    date = fields.Date(string='Datum', default=fields.Date.today)
    remarks=fields.Html(string='Opmerkingen')
    loan_agreement_lines = fields.One2many('am.loan_agreement_line', 'loan_agreement_id', string='Loan agreement lines', ondelete='cascade' )\
        
    @api.depends('date', 'employee_id')
    def _compute_rec_name(self):
        for record in self:
            record.rec_name = (record.employee_id.name or '') + " (" + str(record.date or '') + ")"
            
    def action_send_report_by_email(self):
        loan_agreement = self.env['am.loan_agreement'].browse(self.env.context['active_ids'])
        report_obj = self.env['ir.actions.report']
        mail_obj = self.env['mail.mail']
        report = report_obj._get_report_from_name('asset_management.asset_doc')
        report_data = report._render_qweb_pdf('asset_management.asset_doc',self.env.context['active_ids'][0])
        email_values = {
            'subject': 'Report Email',
            'body_html': '<p>Attached is the report.</p>',
            'email_to': loan_agreement.employee_id.work_email,
            'attachment_ids': [(0, 0, {
                'name': 'report.pdf',
                'datas': base64.b64encode(report_data[0]),
                'type': 'binary'
            })]
        }  
        mail_obj.create(email_values).send()      
