# -*- encoding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Mission(models.Model):
  _name = 'odoo.mission'
  _description = 'Spaceship mission info'

  name = fields.Char(string='Mission\'s Name',required=True)
  launch_date = fields.Date(
    required=True,
    default=fields.Date.today
  )
  comeback_date = fields.Date(required=True)
  amount_fuel = fields.Float(string='Amount of fuel necessary',required=True)
  engines = fields.Integer(string='Number of engines',required=True)

  ship_id = fields.Many2one(
    comodel_name='odoo.spaceship',
    string='Spaceship',
    ondelete='cascade',
    required=True  
  )

  tripulation_ids = fields.Many2many(comodel_name='res.partner', string='Tripulation')

  project_ids = fields.One2many(
    comodel_name='project.project',
    inverse_name='mission_id',
    string='Projects'
  )

  @api.constrains('tripulation_ids')
  def _check_amount_tripulation(self):
    for record in self:
      if len(record.tripulation_ids) > record.ship_id.number_passengers:
        raise UserError("Cannot set a larger tripulation than spaceship's amount of passengers")
