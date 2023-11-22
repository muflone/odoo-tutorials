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
    _sql_constraints = [
        ('library_book_name_date_eq',
         'UNIQUE (name, date_published)',
         'Book title and publication date must be unique'),
        ('library_book_check_date',
         'CHECK (date_published <= current_date)',
         'Publication date must not be in the future')
    ]

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
    publisher_country_id = odoo.fields.Many2one(
        comodel_name='res.country',
        string='Publisher Country',
        compute='_compute_publisher_country',
        inverse='_inverse_publisher_country',
        search='_search_publisher_country')
    publisher_country_related = odoo.fields.Many2one(
        comodel_name='res.country',
        string='Publisher Country (related)',
        related='publisher_id.country_id',
        readonly=False)
    author_ids = odoo.fields.Many2many(comodel_name='res.partner',
                                       string='Authors')
    category_id = odoo.fields.Many2one(comodel_name='library.book.category',
                                       string='Category')

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

    @odoo.api.depends('publisher_id.country_id')
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    def _inverse_publisher_country(self):
        for book in self:
            book.publisher_id.country_id = book.publisher_country_id

    def _search_publisher_country(self, operator, value):
        return [('publisher_id.country_id', operator, value)]
