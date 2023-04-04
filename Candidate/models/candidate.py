from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date
import re


class RecruitmentCandidate(models.Model):
    _name = "recruitment.candidate"
    # _inherit = "['hr.applicant.category']"
    _description = "Recruitment Candidate"

    name = fields.Char(string="Candidate Name", required=True)
    email = fields.Char(string="Email", required=True)
    mobile = fields.Char(string="Mobile", required=True)
    degree = fields.Selection(
        [('graduate', 'Graduate'),
         ('bachelor_degree ', 'Permanante Employee'),
         ('master_degree', 'Master Degree'),
         ('doctoral_degree', 'Doctoral Degree')], string="Degree")
    applied_job = fields.Char(string="Applied Job")
    current_company = fields.Char(string="Current Company")
    current_city = fields.Char(string="Current City")
    skills = fields.Many2many(comodel_name="hr.applicant.category", required=True)
    current_salary = fields.Integer(string="Current Salary")
    expected_salary = fields.Integer(string="Expected Salary")
    referred_by = fields.Many2one(comodel_name="res.users", string="Referred By")
    experience_in_months = fields.Integer(string="Experience in Months")
    current_experience = fields.Integer(string="Current Experience")
    # current_experience = fields.Integer(string="Current Experience", compute="_compute_current_experience")

    @api.constrains('mobile', 'email')
    def validation(self):
        for rec in self:
            # print(rec.mobile)
            regex_mobile = "^\d{10}$"
            regex_mail = ""
            check_mobile = re.findall(regex_mobile, rec.mobile)
            check_mail = re.findall(regex_mail, rec.mail)
            # print(check_mobile)
            if not check_mobile:
                raise ValidationError(_("Enter valid 10 digit mobile number"))
            if not check_mail:
                raise ValidationError(_("Enter valid Email"))

    # @api.depends('experience_in_months')
    # def _compute_current_experience(self):
    #     pass

