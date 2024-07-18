from odoo import models, fields
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_reminder = fields.Boolean(default=True, string="Send Quotation Reminder")

    def action_send_mail(self):
        template = self.env.ref('sale.quotation_reminder')
        template.send_mail(self.id, force_send=True)

    def action_send_quotation_on_expiry(self):
        today = fields.Date.today()

        quotations = self.env['sale.order'].search([
            ('state', '=', 'sent'),
            ('is_reminder', '=', True),
            ('validity_date', '>=', today)
        ])
        for quot in quotations:
            date_order = quot.date_order.date() if quot.date_order else today
            days_since_order = (today - date_order).days
            if days_since_order % 7 == 0:
                quot.action_send_mail()
