# -*- Encoding: utf-8 -*-
{
  'name': 'Odoo Spaceship Travel',
  'summary': '''App to organize the logistics''',
  'description': '''
    An module to plan and help Odoo get to Moon
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Logistcs',
  'version': '0.1',
  'depends': ['base'],
  'data': [
    'views/spaceship_menu_items.xml',
    'views/speceship_views.xml',
    'security/spaceship_security.xml',
    'security/ir.model.access.csv'
  ],
  'demo': [
    'demo/spaceship_demo.xml'
  ],
}
