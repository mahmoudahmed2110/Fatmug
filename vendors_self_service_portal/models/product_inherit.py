# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'
    _description = 'Product Vendor Forcast'

    vendor_forcasts_ids = fields.One2many('vendor.forcast', 'product_id', string='Vendors Forcasts')


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product template Vendor Forcast '

    vendor_forcasts_ids = fields.One2many('vendor.forcast', 'product_tmpl_id', string='Vendors Forcasts')
