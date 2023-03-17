from odoo import api, fields, models


class MailPatientWizard(models.Model):
    _name = "mail.patient.wizard"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Mail Patient Wizard"

    # appointment_id = fields.Many2one('hospital.appointment', string="Appointment", tracking=True)
    # select_fields = fields.Many2many("ir.model.fields", string="Select Fields")
    # select_fields = fields.Many2one("hospital.patient", string="Select Fields")
    # select_1 = fields.Many2many(related="selected_fields.name", tracking=True)
    # select_ids = fields.One2many('hospital.patient', 'mail_id', string="Select Fields")
    select_ids = fields.Many2one('hospital.patient', string="Select Fields")
    # patient_id = fields.Many2one('hospital.patient', string="Patient")
    # age = fields.Integer(related="patient_id.age", string="Age")
    # email = fields.Char(related="patient_id.email", string="Email")
    # gender = fields.Selection(related="patient_id.gender", string="Gender")
    # date_of_birth = fields.Date(related="patient_id.date_of_birth", string="Date of Birth")
    reason_send = fields.Text(string="Reason", tracking=True)

    def send_btn(self):
        print(self.select_ids)
