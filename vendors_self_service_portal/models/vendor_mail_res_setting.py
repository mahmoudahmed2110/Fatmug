# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    procurement_team_email = fields.Char(
        string="Procurement Team Email", config_parameter='vendors_self_service_portal.procurement_team_email', readonly=False)



