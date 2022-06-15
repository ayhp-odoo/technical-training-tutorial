# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
  _name = 'odoo.mission'
  _description = 'Spaceship mission info'

  name = fields.Char(string='Mission\'s Name',required=True)
  launch_date = fields.Date(
    required=True,
    default=fields.Date.today
  )
  comeback_date = fields.Date(required=True)

  ship_id = fields.Many2one(
    comodel_name='odoo.spaceship',
    string='Spaceship',
    ondelete='cascade',
    required=True  
  )

  tripulation_ids = fields.Many2many(comodel_name='res.partner', string='Tripulation')

