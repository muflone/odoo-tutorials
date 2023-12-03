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

{
    'name': "Library Book Borrowing",
    'description': """Members can borrow books from the library.""",
    'author': "Muflone",
    'application': False,
    'installable': True,

    'version': '0.1',
    'license': 'GPL-3',
    'website': 'https://github.com/muflone/odoo-tutorials',
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': ['library_member', 'mail'],

    # dependant files
    'data': [
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/checkout_view.xml',
        'views/checkout_stage_view.xml',
        'views/checkout_massmessage_wizard_view.xml',
        'data/library_checkout_stage.xml',
    ],
}
