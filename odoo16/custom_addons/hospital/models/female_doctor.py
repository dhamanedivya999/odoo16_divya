from odoo import api, fields, models,_

class HospitalFemaleDoctor(models.Model):
    _name = "hospital.female.doctor"
    _inherit = 'mail.thread'
    _description = "Female Doctor Records"
    _rec_name = "name"

    name = fields.Char(string='Name',required = True, tracking = True)
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],
                              string="Gender", tracking=True)
    ref = fields.Char(string="Reference", required=True)
    age = fields.Integer(string='Age')
    doctor_id = fields.Many2one('hospital.doctor',string='Doctor')

    @api.onchange('doctor_id')
    def onchange_patient_id(self):
        self.ref = self.doctor_id.ref
