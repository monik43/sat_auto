# -*- coding: utf-8 -*-
from odoo import http

# class SatAuto(http.Controller):
#     @http.route('/sat_auto/sat_auto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sat_auto/sat_auto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sat_auto.listing', {
#             'root': '/sat_auto/sat_auto',
#             'objects': http.request.env['sat_auto.sat_auto'].search([]),
#         })

#     @http.route('/sat_auto/sat_auto/objects/<model("sat_auto.sat_auto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sat_auto.object', {
#             'object': obj
#         })