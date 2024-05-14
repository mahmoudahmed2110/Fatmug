# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order Adjustment Request'

    adjustments_request_ids = fields.One2many('vendor.adjustment.request', 'order_id', string='Adjustment Requests')
