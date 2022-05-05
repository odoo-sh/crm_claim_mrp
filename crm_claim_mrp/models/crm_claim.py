# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    mrp_count = fields.Integer(
        string='Manufacturing Orders',
        compute='_compute_claims_count',
    )

    def _set_claim_fields_count(self, model_list, field_list):
        if isinstance(model_list, list) and isinstance(field_list, list):
            model_list.append('mrp.production')
            field_list.append('mrp_count')
        return super()._set_claim_fields_count(model_list, field_list)

    def action_view_production(self):
        action = self.env["ir.actions.act_window"]._for_xml_id('mrp.mrp_production_action')
        claim_ids = sum([claim.ids for claim in self], [])
        production = self.env['mrp.production'].search([('claim_id', 'in', claim_ids)])
        context = {
            'default_partner_id': self.partner_id.id,
            'default_claim_id': self.id,
        }
        if len(production) == 1:
            form = self.env.ref('mrp.mrp_production_form_view', False)
            form_id = form.id if form else False
            action['views'] = [(form_id, 'form')]
            action['res_id'] = production[0].id
        else:
            action['domain'] = [('id', 'in', production.ids)]
        action['context'] = context
        return action
