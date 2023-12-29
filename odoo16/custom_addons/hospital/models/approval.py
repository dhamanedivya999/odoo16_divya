from odoo import api, fields, models,_

class HospitalApproval(models.Model):
    _name = "hospital.approval"
    _inherit = 'mail.thread'
    _description = "Approval Records"

    name = fields.Char(string='Name', required=True, tracking=True)