from odoo import models, api


class CompanyReport(models.Model):
    _inherit = 'ir.actions.report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Fetch the current company ID from the context
        company_id = self.env.context.get('company_id')
        if not company_id:
            company_id = self.env.user.company_id.id

        # Get the company record
        company = self.env['res.company'].browse(company_id)

        # Fetch the report template associated with the company
        report_template = company.invoice_report_template_id
        if not report_template:
            # Fallback to a default template if not set
            report_template = self.env['ir.actions.report'].search([('report_type', '=', 'qweb-pdf')], limit=1)

        # Set the appropriate report template dynamically
        if report_template:
            self.report_name = report_template.report_name

        # Call the super method to generate report values
        return super(CompanyReport, self)._get_report_values(docids, data)