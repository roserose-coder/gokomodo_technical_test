from odoo import api, models, fields

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    x_business_model =fields.Many2one('business.model')