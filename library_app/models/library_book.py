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


class Book(odoo.models.Model):
    _name = 'library.book'
    _description = 'Book'
    name = odoo.fields.Char(string='Title',
                            required=True)
    isbn = odoo.fields.Char(string='ISBN')
    active = odoo.fields.Boolean(string='Active?',
                                 default=True)
    date_published = odoo.fields.Date()
    image = odoo.fields.Binary(string='Cover')
    publisher_id = odoo.fields.Many2one(comodel_name='res.partner',
                                        string='Publisher')
    author_ids = odoo.fields.Many2many(comodel_name='res.partner',
                                       string='Authors')
