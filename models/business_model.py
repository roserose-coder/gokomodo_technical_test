from odoo import api, models, fields


class BusinessModel(models.Model):
    _name = "business.model"

    name = fields.Char(string="Name",required=True)
    code =fields.Char(string="Code")