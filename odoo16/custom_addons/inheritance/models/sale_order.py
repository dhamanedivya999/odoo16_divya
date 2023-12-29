from odoo import api, fields, models, _


class SaleOrder(models.Model):
    # _name = "inheritance.invoiceorder"
    _inherit = "account.move"
    sale_desc = fields.Char(string='Sale Description')