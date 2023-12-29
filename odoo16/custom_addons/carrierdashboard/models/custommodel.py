# from odoo import models, fields
#
# class CustomModel(models.Model):
#     _name = 'custom.model'
#     _inherit = ['purchase.order.line', 'purchase.order']  # Inherit ModelA and ModelB
#
#     # Fields to establish relationships between ModelA and ModelB
#     purchase_order_line_id = fields.Many2one('purchase.order.line', string='Model A Reference')
#     purchase_order_ids = fields.One2many('purchase.order', 'custom_model_id', string='Model B References')
#
#     # Related field to display 'field_to_show' from ModelA in ModelB
#     related_field_from_model_a = fields.Char(
#         related='purchase_order_line_id.qty_invoiced',
#         string='Field from ModelA in ModelB',
#         readonly=True
#     )
#
#     # Other fields and methods in your CustomModel
#     # ...
