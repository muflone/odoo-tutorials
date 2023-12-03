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

import logging

import odoo


class CheckoutMassMessage(odoo.models.TransientModel):
    _name = 'library.checkout.massmessage'
    _description = 'Send message to Borrowers'
    checkout_ids = odoo.fields.Many2many(comodel_name='library.checkout',
                                         string='Checkouts')
    message_subject = odoo.fields.Char(string='Subject',
                                       required=True)
    message_body = odoo.fields.Html(string='Message',
                                    required=True)

    @odoo.api.model
    def default_get(self, fields_names):
        defaults = super().default_get(fields_names)
        defaults['checkout_ids'] = self.env.context.get('active_ids')
        return defaults

    @odoo.api.multi
    def button_send(self):
        self.ensure_one()
        logger = logging.getLogger(__name__)
        if not self.checkout_ids:
            raise odoo.exceptions.UserError(
                'Please select at least one checkout')
        if not self.message_body or self.message_body == '<p><br></p>':
            raise odoo.exceptions.UserError(
                'Wite a message body to send')
        for checkout in self.checkout_ids:
            checkout.message_post(body=self.message_body,
                                  subject=self.message_subject,
                                  subtype='mail.mt_comment')
            logger.debug(
                'Message on %d to followers: %s',
                checkout.id,
                checkout.message_follower_ids)
        return True
