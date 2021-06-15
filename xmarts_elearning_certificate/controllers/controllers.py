# -*- coding: utf-8 -*-
# from odoo import http


# class XmartsElearningCertificate(http.Controller):
#     @http.route('/xmarts_elearning_certificate/xmarts_elearning_certificate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xmarts_elearning_certificate/xmarts_elearning_certificate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xmarts_elearning_certificate.listing', {
#             'root': '/xmarts_elearning_certificate/xmarts_elearning_certificate',
#             'objects': http.request.env['xmarts_elearning_certificate.xmarts_elearning_certificate'].search([]),
#         })

#     @http.route('/xmarts_elearning_certificate/xmarts_elearning_certificate/objects/<model("xmarts_elearning_certificate.xmarts_elearning_certificate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xmarts_elearning_certificate.object', {
#             'object': obj
#         })
