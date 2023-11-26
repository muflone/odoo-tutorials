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


class CheckoutStage(odoo.models.Model):
    _name = 'library.checkout.stage'
    _description = 'Checkout Stage'
    _order = 'sequence, name'

    name = odoo.fields.Char(string='Stage name')
    sequence = odoo.fields.Integer(default=10,
                                   string='Stage ordering')
    fold = odoo.fields.Boolean()
    active = odoo.fields.Boolean(default=True)
    state = odoo.fields.Selection(selection=[('new', 'New'),
                                             ('open', 'Borrowed'),
                                             ('done', 'Returned'),
                                             ('cancel', 'Cancelled')],
                                  default='new')
