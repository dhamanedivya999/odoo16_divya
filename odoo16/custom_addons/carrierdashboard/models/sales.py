from odoo import api, fields, models, _


class Sales(models.Model):
    _name = "carrierdashboard.sales"
    # _inherit = ["sale.order","mail.activity.mixin"]
    _description = "sales Records"