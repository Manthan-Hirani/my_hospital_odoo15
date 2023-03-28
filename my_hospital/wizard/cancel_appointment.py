from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment", tracking=True, domain=[('state', '=', 'draft')])
    reason_cansel = fields.Char(string="Reason", tracking=True)

    def action_cancel(self):
        today = date.today()
        if self.appointment_id.booking_date == today:
            raise ValidationError(_("You can't cancel today's appointment"))
        else:
            self.appointment_id.state = "cancel"


