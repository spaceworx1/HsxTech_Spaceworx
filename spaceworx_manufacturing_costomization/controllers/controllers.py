# -*- coding: utf-8 -*-
# from odoo import http


# class SpaceworxManufacturingCostomization(http.Controller):
#     @http.route('/spaceworx_manufacturing_costomization/spaceworx_manufacturing_costomization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spaceworx_manufacturing_costomization/spaceworx_manufacturing_costomization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('spaceworx_manufacturing_costomization.listing', {
#             'root': '/spaceworx_manufacturing_costomization/spaceworx_manufacturing_costomization',
#             'objects': http.request.env['spaceworx_manufacturing_costomization.spaceworx_manufacturing_costomization'].search([]),
#         })

#     @http.route('/spaceworx_manufacturing_costomization/spaceworx_manufacturing_costomization/objects/<model("spaceworx_manufacturing_costomization.spaceworx_manufacturing_costomization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spaceworx_manufacturing_costomization.object', {
#             'object': obj
#         })

