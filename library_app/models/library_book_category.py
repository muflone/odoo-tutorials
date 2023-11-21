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


class BookCategory(odoo.models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'
    _parent_store = True
    _parent_name = 'parent_id'

    name = odoo.fields.Char(required=True,
                            translate=True)
    active = odoo.fields.Boolean(string='Active?',
                                 default=True)
    # Hierarchy fields
    parent_id = odoo.fields.Many2one(comodel_name='library.book.category',
                                     string='Parent Category',
                                     ondelete='restrict')
    # This is used to save the full path when _parent_store is set
    parent_path = odoo.fields.Char(index=True)
    # Children relationship
    child_ids = odoo.fields.One2many(comodel_name='library.book.category',
                                     inverse_name='parent_id',
                                     string='Subcategories')
    # Reference fields
    highlighted_id = odoo.fields.Reference(
        selection=[('library.book', 'Book'),
                   ('res.partner', 'Author')],
        string='Category Highlight')
