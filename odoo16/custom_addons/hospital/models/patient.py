from odoo import (api, fields, models, _)
from odoo.odoo.exceptions import ValidationError
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = "mail.thread"
    _description = "Patient in the hospital"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    notes = fields.Text(string="Notes", tracking=True)
    gender = fields.Selection(related="doctor_id.gender")
    date_of_birth = fields.Date(string='Date Of Birth')
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
    ref = fields.Char(string='reference', default=lambda self: _('New'))
    # status = fields.Selection(related='')
    # adding many2one field
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    # adding many2many field
    tag_ids = fields.Many2many('res.partner.category', 'hospital_patient_tag_rel', 'patient_id', 'tag_id',
                               string="Tags")
    appointment_time = fields.Datetime(string="Appointment time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)

    # requester_id = fields.Many2one('res.users', string='Requester', required=True)
    # request_type = fields.Selection([
    #     ('approve', 'Approve'),
    #     ('reject', 'Reject')
    # ], string='Request Type', required=True)
    # state = fields.Char(string="state")

    state = fields.Selection([
         # ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status')

    # @api.multi
    # def action_send_for_approval(self):
    #     for rec in self:
    #         rec.status = 'pending'

    # @api.depends('name')
    # def _compute_capitalized_name(self):
    #     if self.name:
    #         self.capitalized_name = self.name.upper()
    #     else:
    #         self.capitalized_name = ' '

    # @api.constrains('is_child', 'age')
    # def _check_child_age(self):
    #     for rec in self:
    #         if rec.is_child==True and rec.age == 0:
    #             raise ValidationError(_("Age has to be recorded"))

    # @api.constrains('age')
    # def _check_child_age(self):
    #     for record in self:
    #         if not record.age:
    #             raise ValidationError("Age must be recorded for the patient.")

    @api.depends('name')
    def _compute_capitalized_name(self):
        for record in self:
            if record.name:
                record.capitalized_name = record.name.upper()
            else:
                record.capitalized_name = ''

    @api.model_create_multi
    def create(self, val_list):
        for val in val_list:
            # val['gender']='male'
            val['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(val_list)

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                rec.age = today.year - rec.date_of_birth.year
                # rec.age = age
            else:
                rec.age = 0  # Set a default age when date_of_birth is not available


