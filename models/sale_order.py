from odoo import api, models, fields

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    x_business_model =fields.Many2one('business.model',string ="Business Model")

    def name_get(self):
        result = []
        for rec in self:
            name = rec.name
            if rec.x_business_model.code:
                name = '[%s] - %s' % (rec.x_business_model.code, name)
            result.append((rec.id, name))
        return result

