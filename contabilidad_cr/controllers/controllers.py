# -*- coding: utf-8 -*-
from odoo import http

# class ContabilidadCr(http.Controller):
#     @http.route('/contabilidad_cr/contabilidad_cr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contabilidad_cr/contabilidad_cr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contabilidad_cr.listing', {
#             'root': '/contabilidad_cr/contabilidad_cr',
#             'objects': http.request.env['contabilidad_cr.contabilidad_cr'].search([]),
#         })

#     @http.route('/contabilidad_cr/contabilidad_cr/objects/<model("contabilidad_cr.contabilidad_cr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contabilidad_cr.object', {
#             'object': obj
#         })