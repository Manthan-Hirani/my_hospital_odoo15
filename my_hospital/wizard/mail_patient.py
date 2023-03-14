from odoo import api, fields, models


class MailPatient(models.TransientModel):
    _name = "mail.patient.wizard"
    _description = "Mail Patient Wizard"

    # appointment_id = fields.Many2one('hospital.appointment', string="Appointment", tracking=True)
    select_fields = fields.Many2many("ir.model.fields", string="Select Fields")
    # select_fields = fields.Many2one("hospital.patient", string="Select Fields")
    # select_1 = fields.Many2many(related="selected_fields.name", tracking=True)
    reason_send = fields.Char(string="Reason", tracking=True)

    def action_send(self):
        print(self.select_fields)
