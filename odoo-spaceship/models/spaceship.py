# -*- Encoding: utf-8 -*-

from odoo import models, fields, api

class SpaceShip(models.Model):
  _name = 'odoo.spaceship'
  _description = 'Spaceship info'

  name = fields.Char(string='Ship\'s Nanme', required=True)
  captain = fields.Char(string='Captain\'s name',required=True)
  ship_dimensions = fields.Float(string='Ship\'s Dimensions',required=True)
  fuel_type = fields.Selection(
    string='Ship\'s Fuel Type',
    required=True,
    selection=[
      ('solid','Solid'),
      ('liquid','Liquid')
    ]
  )
  ship_type = fields.Selection(
    string='Ship\'s Type',
    required=True,
    selection=[
      ('flipper','Flipper'),
      ('glide_symmetric_spaceship','Glide symmetric spaceship'),
      ('non_monotonic_spaceship','Non-monotonic spaceship'),
      ('knightship','Knightship')
    ]
  )
  number_passengers = fields.Integer(string='Number of Passengers',required=True)