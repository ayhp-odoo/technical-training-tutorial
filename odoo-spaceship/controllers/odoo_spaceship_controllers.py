# -*- coding: utf-8 -*- 

from odoo import http

class OdooSpaceship(http.Controller):
  @http.route('/odoo-spaceship/', auth='public',website=True)
  def index(self, **kw):
    return "Hello world!"

  @http.route('/odoo-spaceship/missions/', auth='public',website=True)
  def missions(self, **kw):
    missions = http.request.env['odoo.mission'].search([])
    return http.request.render('odoo-spaceship.missions_website', {
      'missions': missions
    })