# -*- Encoding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SpaceShip(models.Model):
  _name = 'odoo.spaceship'
  _description = 'Spaceship info'

  name = fields.Char(string='Ship\'s Name', required=True)
  ship_width = fields.Float( string='Ship\'s Width',required=True)
  ship_height = fields.Float( string='Ship\'s Height',required=True)
  fuel_type = fields.Selection(
    string='Ship\'s Fuel Type',
    required=True,
    selection=[
      ('solid','Solid'),
      ('liquid','Liquid')
    ],
  )
  ship_type = fields.Selection(
    string='Ship\'s Type',
    required=True,
    selection=[
      ('flipper','Flipper'),
      ('glide_symmetric_spaceship','Glide symmetric spaceship'),
      ('non_monotonic_spaceship','Non-monotonic spaceship'),
      ('knightship','Knightship')
    ],
  )
  number_passengers = fields.Integer(string='Number of Passengers',required=True)
  active = fields.Boolean(default=True)

  @api.constrains('ship_width')
  def _check_ship_width(self):
    for record in self:
      if record.ship_width > record.ship_height:
        raise UserError('The width of the ship should not be larger than the height')