from odoo import api, fields, models,_

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = "Doctor Records"
    _rec_name = "name"

    name = fields.Char(string='Name',required = True, tracking = True)
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],
                              string="Gender", tracking=True)
    ref = fields.Char(string="Reference", required=True)
    age = fields.Integer(string='Age')
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High')
    ], string="Priority")
    state = fields.Selection([
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected')

    ], default='pending', string="Status", required=True)

    active = fields.Boolean(default = True)
# name get function
    def name_get(self):
        res = []
        for rec in self:
          res.append((rec.id, f'{rec.ref} - {rec.name}'))
        return res
