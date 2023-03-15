from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Doctor"

    image = fields.Image(string="Image", tracking=True)
    name = fields.Char(string="Name", tracking=True)
    experience = fields.Integer(string="Experience", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    expertise = fields.Char(string="Expertise", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
