from odoo import api, fields, models, _


class SalesOrder(models.Model):
    _name = "inheritance.salesorder"
    # _inherit = "account.move"