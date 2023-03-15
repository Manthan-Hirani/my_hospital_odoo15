from odoo import api, fields, models


class HospitalTags(models.Model):
    _name = "hospital.tags"
    # _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Tags"
    _rec_name = "tag_name"

    tag_name = fields.Selection([
        ('vip', 'VIP'),
        ('master', 'Master'),
        ('kid', 'Kid')], string="Tag Name")
    color1 = fields.Integer(string="Color 1")
    color2 = fields.Char(string="Color 2")
