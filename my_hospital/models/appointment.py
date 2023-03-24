from odoo import api, fields, models
from odoo.exceptions import UserError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one('hospital.patient', string="Patient", tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", tracking=True)
    gender = fields.Selection(related="patient_id.gender", tracking=True)
    age = fields.Integer(related="patient_id.age", string="Age", trcking=True)
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today, tracking=True)
    prescription = fields.Html(string="Prescription", tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled')], string="Status", default='draft', required=True, tracking=True)

    # pharmacy_ids = fields.One2many('appointment.pharmacy', 'appointment_id', string="Pharmacy")

    def cancel_btn(self):
        self.state = "cancel"

    # def action_send_mail(self):
    #     template = self.env.ref('my_hospital.report_patient_cards').id
    #     for rec in self:
    #         template.send_mail(rec)
    #     print("Email Sent")

    # def action_send_mail(self):
    #     template_id = self.env.ref('my_hospital.report_patient_cards')
    #     template = self.env['mail.template'].browse(template_id)
    #     template.send_mail(self.id, force_send=True)

# class AppointmentPharmacy(models.Model):
#     _name = "appointment.pharmacy"
#     _description = "Appointment Pharmacy"
#
#     patient_id = fields.Many2one('hospital.patient', string="Patient")
#     age = fields.Integer(related="patient_id.age", string="Age")
#     email = fields.Char(related="patient_id.email", string="Email")
#     gender = fields.Selection(related="patient_id.gender", string="Gender")
#     date_of_birth = fields.Date(related="patient_id.date_of_birth", string="Date of Birth")
#     appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
