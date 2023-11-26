##
#     Project: Odoo Tutorials
# Description: Odoo Tutorials
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2023 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import odoo


class Checkout(odoo.models.Model):
    @odoo.api.model
    def _default_stage(self):
        Stage = self.env['library.checkout.stage']
        return Stage.search(args=[],
                            limit=1)

    @odoo.api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search(args=[],
                             order=order)

    @odoo.api.onchange('member_id')
    def _onchange_member_id(self):
        today = odoo.fields.Date.today()
        if self.request_date != today:
            self.request_date = today
            return {
                'warning': {
                    'title': 'Changed Request Date',
                    'message': 'Request date was changed to today.'
                }
            }

    _name = 'library.checkout'
    _description = 'Checkout request'
    member_id = odoo.fields.Many2one(comodel_name='library.member',
                                     required=True)
    user_id = odoo.fields.Many2one(comodel_name='res.users',
                                   string='Librarian',
                                   default=lambda s: s.env.uid)
    request_date = odoo.fields.Date(default=lambda s: odoo.fields.Date.today())
    line_ids = odoo.fields.One2many(comodel_name='library.checkout.line',
                                    inverse_name='checkout_id',
                                    string='Borrowed Books')
    stage_id = odoo.fields.Many2one(comodel_name='library.checkout.stage',
                                    default=_default_stage,
                                    group_expand='_group_expand_stage_id')
    state = odoo.fields.Selection(related='stage_id.state')
