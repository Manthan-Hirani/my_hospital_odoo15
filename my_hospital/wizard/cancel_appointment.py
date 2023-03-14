from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment", tracking=True)
    reason_cansel = fields.Char(string="Reason", tracking=True)

    def action_cancel(self):
        self.appointment_id.state = "cancel"
        print("Cancel appointment", self.appointment_id.state)

