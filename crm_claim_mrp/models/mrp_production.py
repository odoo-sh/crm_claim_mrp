# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    claim_id = fields.Many2one('crm.claim', readonly=True, string='Return')
