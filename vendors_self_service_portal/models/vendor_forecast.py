# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class VendorForcast(models.Model):
    _name = 'vendor.forcast'
    _description = 'Vendor Forcast'

    product_id = fields.Many2one("product.product")
    product_tmpl_id = fields.Many2one(related="product_id.product_tmpl_id", string="Product")
    expected_quantity = fields.Integer(string="Expected Quantity")
    forecast_date = fields.Date(string="Forcast Date")


    def action_report_forcast(self):
        return self.env.ref('vendors_self_service_portal.vendor_forcast_report').report_action(self)

    def _get_report_base_filename(self):
        return self.product_id.name