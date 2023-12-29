# -*- coding: utf-8 -*-
# from odoo import http


# class SmartDtp(http.Controller):
#     @http.route('/smart_dtp/smart_dtp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_dtp/smart_dtp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_dtp.listing', {
#             'root': '/smart_dtp/smart_dtp',
#             'objects': http.request.env['smart_dtp.smart_dtp'].search([]),
#         })

#     @http.route('/smart_dtp/smart_dtp/objects/<model("smart_dtp.smart_dtp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_dtp.object', {
#             'object': obj
#         })
