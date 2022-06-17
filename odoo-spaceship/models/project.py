# -*- Encoding: utf-8 -*-

from pkg_resources import require
from odoo import models, fields, api

class Project(models.Model):
  _inherit = 'project.project'

  name = fields.Char(required=True)
  description = fields.Text(required=True)
  mission_id = fields.Many2one(
    comodel_name='odoo.mission',
    string='Mission'
  )