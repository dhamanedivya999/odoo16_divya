from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _name = "carrierdashboard.purchaseorder"
    _inherit = ["purchase.order","mail.activity.mixin"]
    _description = "puchaseorder Records"
    # _rec_name = "orderid"

    name = fields.Char(string="name")
