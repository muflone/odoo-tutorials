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

from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):
    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref(xml_id='base.user_admin')
        self.env = self.env(user=user_admin)
        self.Book = self.env['library.book']
        self.book = self.Book.create({
            'name': 'Odoo tutorial',
            'isbn': '879-1-78439-279-6'})
        return result

    def test_create(self):
        """Test Books are active by default"""
        self.assertEqual(self.book.active, True)

    def test_check_isbn(self):
        """Check valid ISBN"""
        self.assertTrue(self.book._check_isbn)
