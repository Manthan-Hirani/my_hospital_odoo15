from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    # mail_patient_ids = fields.One2many('mail.patient.wizard', string="Mail to Patient")
    # today_date = fields.Date(string="Today's Date")
    age = fields.Integer(string="Age", tracking=True, compute="_compute_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    email = fields.Char(string="Email", tracking=True)
    # mail_id = fields.Many2one('mail.patient.wizard', string="Mail")
    # state = fields.Selection([
    #     ('draft', 'Draft'),
    #     ('under_observation', 'Under Observation'),
    #     ('done', 'Done')], string="Status", default='draft', required=True)

    # @api.onchange('date_of_birth')
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year - (
                        (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 1

    @api.model
    def test_cron_job(self):
        print("ABCD")
