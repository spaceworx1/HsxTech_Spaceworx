import binascii
import json

from odoo import fields, http, _
from odoo.http import request
from odoo.addons.sale.controllers.portal import CustomerPortal as CustomerPortal


class QuotationPortal(CustomerPortal):
    @http.route('/my/orders/update_quantity', type='json', auth="user", methods=['POST'], website=True)
    def update_quotation_lines(self, updates=None, **post):
        new_val = json.loads(request.httprequest.data)
        if new_val.get('updates'):
            SaleOrderLine = http.request.env['sale.order.line']
            lines = new_val['updates']
            for line in lines:
                order_line = SaleOrderLine.browse(int(line['line_id']))
                if order_line.order_id.id == int(line['order_id']) and order_line.order_id.state in ['draft','sent']:
                    qty = line.get('new_qty')
                    product_name = line.get('product_name')
                    order_line.product_uom_qty = float(qty)
                    # order_line.name = product_name
                    order_line.product_id = int(line.get('product_id'))
            return {'success': True}

