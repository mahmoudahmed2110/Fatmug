# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _description = 'vendor adjustment request'

    @api.model
    def default_get(self, fields):
        team_email = super(VendorAdjustmentRequest, self).default_get(fields)
        team_email ['team_email'] = self.env['ir.config_parameter'].get_param('vendors_self_service_portal.procurement_team_email')
        return team_email


    order_id = fields.Many2one('sale.order')
    adjustment_detail = fields.Text(string="Adjustment Detail")
    comment = fields.Text(string="Comment")
    team_email = fields.Char(string="Team Email", store=True, readonly=True)

    def submit(self):
        self.env.ref("vendors_self_service_portal.vendor_email_template").send_mail(self.id, force_send=True)
        message = "Email had been sent to procurement team"
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': 'False'
            }
        }
