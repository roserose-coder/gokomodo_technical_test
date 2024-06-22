from odoo import api, models, fields

class AccountTaxInherit(models.Model):
    _inherit = "account.tax"

    x_business_model =fields.Many2one('business.model',string ="Business Model",required=True)