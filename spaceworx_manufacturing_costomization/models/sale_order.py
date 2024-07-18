from odoo import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for rec in self:
            for mrp in self.mrp_production_ids:
                mrp.customer_name = rec.partner_id.id
                mrp.project_name = rec.client_order_ref
        return res

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        for rec in self:
            if self.mrp_production_ids:
                for mrp in self.mrp_production_ids:
                    mrp.customer_name = rec.partner_id.id
                    mrp.project_name = rec.client_order_ref
        return res
