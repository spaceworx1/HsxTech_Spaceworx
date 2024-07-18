# -*- coding: utf-8 -*-
# from odoo import http


# class SpaceworxQuotationSchedular(http.Controller):
#     @http.route('/spaceworx_quotation_schedular/spaceworx_quotation_schedular', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spaceworx_quotation_schedular/spaceworx_quotation_schedular/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('spaceworx_quotation_schedular.listing', {
#             'root': '/spaceworx_quotation_schedular/spaceworx_quotation_schedular',
#             'objects': http.request.env['spaceworx_quotation_schedular.spaceworx_quotation_schedular'].search([]),
#         })

#     @http.route('/spaceworx_quotation_schedular/spaceworx_quotation_schedular/objects/<model("spaceworx_quotation_schedular.spaceworx_quotation_schedular"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spaceworx_quotation_schedular.object', {
#             'object': obj
#         })

