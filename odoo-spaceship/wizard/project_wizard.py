# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProjectWizard(models.TransientModel):
    _name = 'project.wizard'
    _description = "Wizard quick project in mission"
    
    def _default_mission(self):
        return self.env['odoo.mission'].browse(self._context.get('active_id'))
        
    name = fields.Char(required=True)
    description = fields.Char(required=True)
    mission_id = fields.Many2one(comodel_name='odoo.mission', string='Mission',required = True,default= _default_mission)

    def create_project_mission(self):
      pass