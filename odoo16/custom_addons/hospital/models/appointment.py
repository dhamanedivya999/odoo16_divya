from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Appointments Records"

    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_time = fields.Datetime(string="appointment time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    state = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')

    ], default="pending",string="Status")

    def action_test(self):
        print('Button Clicked!!')
        return{
            'effect':{
            'fadeout':'slow',
            'message':'Click Successful',
            'type':'rainbow_man',
         }
        }
    # availability_start = fields.Datetime(string='Availability Start', required=False)
    # availability_end = fields.Datetime(string='Availability End', required=False)
    # check_date = fields.Datetime(string='Check Date', required=False)
    # appointment_date = fields.Datetime(string='Appointment Date', required=False)
    #
    # availability_start = fields.Datetime(string='Availability Start', required=False)
    # availability_end = fields.Datetime(string='Availability End', required=False)
    # is_available = fields.Boolean(string='Is Available', compute='_compute_is_available', store=True)


# @api.depends('check_date')
# def _compute_is_available(self, doctor_id, check_date):
#     doctor = self.env['res.partner'].browse(doctor_id)
#     doctor_availability = self.env['hospital.appointment'].search([
#         ('doctor_id', '=', doctor_id),
#         ('availability_start', '<=', check_date),
#         ('availability_end', '>=', check_date)
#     ])
#     if doctor_availability:
#         appointments = self.env['hospital.appointment'].search([
#             ('doctor_id', '=', doctor_id),
#             ('appointment_date', '=', check_date)
#         ])
#         if appointments:
#             # Doctor is not available at this time due to an appointment
#             self.env.user.notify_warning(
#                 title='Doctor Not Available',
#                 message='Doctor is not available at this time due to an appointment.'
#             )
#         else:
#             # Doctor is available at this time for an appointment
#             self.env.user.notify_info(
#                 title='Doctor Available',
#                 message='Doctor is available at this time for an appointment.'
#             )
#     else:
#         # Doctor is not available at this time
#         self.env.user.notify_info(
#             title='Doctor Not Available',
#             message='Doctor is not available at this time.'
#         )
