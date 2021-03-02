# -*- coding: utf-8 -*-

from odoo import models, fields, api

class helpdeskticket(models.Model):
    _inherit = 'helpdesk.ticket'

class mrprepair(models.Model):
    _inherit = 'mrp.repair'

    @api.model
    def default_get(self,fields):
        res = super(mrprepair,self).default_get(fields)
        res.update({
            'x_sn': self.env.helpdesk.ticket.x_sn or False
        })
        return res