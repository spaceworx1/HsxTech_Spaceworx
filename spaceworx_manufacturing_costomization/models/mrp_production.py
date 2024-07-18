from odoo import models, api, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    customer_name = fields.Many2one('res.partner', string="Customer Name", readonly=True, store=True)
    project_name = fields.Char(string="Project Name", readonly=True, store=True)
