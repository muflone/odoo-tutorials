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
import odoo.exceptions


class Book(odoo.models.Model):
    _name = 'library.book'
    _description = 'Book'
    _order = 'date_published desc, name asc'

    @odoo.api.multi
    def _check_isbn(self):
        """
        Check the Book ISBN

        :return:
        """
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            # Basic check for 13 digits ISBN
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check
        else:
            return False

    # String fields
    name = odoo.fields.Char(string='Title',
                            required=True)
    isbn = odoo.fields.Char(string='ISBN',
                            size=13)
    book_type = odoo.fields.Selection(selection=[('paper', 'Paperback'),
                                                 ('hard', 'Hardcover'),
                                                 ('electronic', 'Electronic'),
                                                 ('other', 'Other')],
                                      string='Type')
    notes = odoo.fields.Text(string='Internal notes')
    descr = odoo.fields.Html(string='Description')
    # Numeric fields
    copies = odoo.fields.Integer(default=1)
    avg_rating = odoo.fields.Float(string='Average rating',
                                   digits=(3, 2))
    price = odoo.fields.Monetary(string='Price',
                                 currency_field='currency_id')
    currency_id = odoo.fields.Many2many(comodel_name='res.currency')
    # Date and time fields
    date_published = odoo.fields.Date()
    last_borrow_date = odoo.fields.Datetime(
        string='Last Borrowed on',
        default=lambda self: odoo.fields.Datetime.now())
    # Other fields
    active = odoo.fields.Boolean(string='Active?',
                                 default=True)
    image = odoo.fields.Binary(string='Cover')
    # Relational fields
    publisher_id = odoo.fields.Many2one(comodel_name='res.partner',
                                        string='Publisher')
    author_ids = odoo.fields.Many2many(comodel_name='res.partner',
                                       string='Authors')

    @odoo.api.multi
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise odoo.exceptions.Warning('Missing ISBN for {BOOK}'.format(
                    BOOK=book.name))
            elif not book._check_isbn():
                raise odoo.exceptions.Warning(
                    'Invalid ISBN {ISBN} for {BOOK}'.format(ISBN=book.isbn,
                                                            BOOK=book.name))
        return True
