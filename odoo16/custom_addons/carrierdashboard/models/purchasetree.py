from odoo import api, fields, models, _


# from odoo.odoo.fields import One2manyfrom
# odoo import http, fields
# from werkzeug.wrappers import Response
# import json


class PurchaseTree(models.Model):
    # _name = 'carrierdashboard.productqnty'
    _inherit = 'purchase.order'

    # purchase_order_line_ids = One2many('purchase.order.line','order_id',string='Purchase Order Line Id')
    openqnty = fields.Integer(string="Opne QTY", compute='_compute_helper')
    order_id = fields.Integer(string="order id")

    # @api.depends('product_qty', 'qty_received')
    # def _compute_open_quantity(self):
    #     for rec in self:
    #         rec.openqnty = rec.product_qty - rec.qty_received
    #
    # def button_confirm(self):
    #     for rec in self:
    #         rec._compute_open_quantity()
    #
    # def _compute_helper(self):
    #     # id = self.env['purchase.order'].search([('id', '=', 1)])
    #     purchase_orders = self.env['purchase.order.line'].search([('order_id', '=', 1)])
    #     # openqnty = self.order_id.openqnty
    #     if purchase_orders:
    #         print(purchase_orders)
    #         self.openqnty = purchase_orders[0].openqnty
    #     else:
    #         self.openqnty = 0

    def _compute_helper(self):
        for record in self:
            purchase_order_line = self.env['purchase.order.line'].search([
                ('order_id', '=', record.id)
            ], limit=1)

            if purchase_order_line:
                record.openqnty = purchase_order_line[0].openqnty
            else:
                record.openqnty = 0
