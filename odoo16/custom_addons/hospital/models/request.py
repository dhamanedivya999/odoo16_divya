from odoo import api, fields, models,_

class HospitalRequest(models.Model):
    _name = "hospital.request"
    _inherit = 'mail.thread'
    _description = "Request Records"

    name = fields.Char(string='Name', required=True, tracking=True)