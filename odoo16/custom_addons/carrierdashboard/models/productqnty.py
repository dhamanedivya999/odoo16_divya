from odoo import api, fields, models, _


class ProductQnty(models.Model):
    _inherit = ['purchase.order.line']

    openqnty = fields.Integer(string="OpenQuantity",compute ="_compute_open_quantity")
    # order_id = fields.Many2one('purchase.order')



    @api.depends('product_qty', 'qty_received')
    def _compute_open_quantity(self):
        for rec in self:
            rec.openqnty = rec.product_qty - rec.qty_received

    def button_confirm(self):
        for rec in self:
            rec._compute_open_quantity()