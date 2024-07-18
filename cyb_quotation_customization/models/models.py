from odoo import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    html_field = fields.Html(string='Quotation Details',sanitize=False)


    @api.onchange('sale_order_template_id')
    def update_html_data(self):
        for rec in self:
            if rec.sale_order_template_id:
                rec.html_field = rec.sale_order_template_id.html_field


class SaleOrder(models.Model):
    _inherit = 'sale.order.template'

    html_field = fields.Html(string='Quotation Details',sanitize=False)


