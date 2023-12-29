from odoo import models, fields, api, _


class smart_dtp(models.Model):
    _name = 'smart_dtp.smart_dtp'
    _description = 'smart_dtp.smart_dtp'
    _rec_name = "order_id"

    # name = fields.Char(string="name")
    Po_number_id = fields.Many2one('purchase.order', string="PO Number")
    price = fields.Char(string="Price")
    total_quantity = fields.Integer(string="Total Quantity")
    po_deadline = fields.Date(string="PO Deadline")
    lot_no = fields.Char(string="Lot Number")
    packer_name = fields.Char("Packer Name")
    approved_quantity = fields.Integer('Approved Quantity')
    rejected_quantity = fields.Integer("Rejected Quantity")
    Remark = fields.Char("Remark")
    image = fields.Binary(string="Image")
    order_id = fields.Char(string="Delivery Order Number", default=lambda self: _('New'))
    farmer_name = fields.Char(string="Farmer Name")
    quantity = fields.Integer(string='Quantity')
    state = fields.Selection([
        ('pending', 'Pending'),
        ('shipped to exporter', 'Shipped To Exporter'),
        ('pending with packer', 'Pending With Packer'),
        ('packer approved request', 'Packer Approved Request'),
        ('pickup confirmed', 'Pickup Confirmed'),
        ('in packaging', 'In Packaging')

    ], default="pending", string="Status")



    @api.model_create_multi
    def create(self, val_list):
        for val in val_list:
            # val['gender']='male'
            val['order_id'] = self.env['ir.sequence'].next_by_code('smart_dtp.smart_dtp')
        return super(smart_dtp, self).create(val_list)


    def open_form(self):
        return {
            'res_model': 'purchase.order',
            'res_id': self.Po_number_id.id,
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('purchase.purchase_order_form').id
        }

    @api.onchange('Po_number_id')
    def onchange_Po_number_id(self):
        if self.Po_number_id:

            self.farmer_name = self.Po_number_id.partner_id.name
            self.po_deadline = self.Po_number_id.date_order
            # self.total_quantity = self.Po_number_id.product_qty.name

        else:
            self.farmer_name = ''
            # self.total_quantity =''

        for record in self:

            purchase_order_line = self.env['purchase.order.line'].search([
                ('order_id', '=', record.Po_number_id.name)
            ])

            if purchase_order_line:
                # print('yes')
                record.total_quantity = purchase_order_line[0].product_qty
                record.price = purchase_order_line[0].price_unit
                # print('yes')
            else:
                # print('no')
                record.total_quantity = 0
                record.price = 0

                # print('no')

# class Purchase(models.Model):
#     _inherit = 'purchase.order'
#
#     def open_form(self):
#         return {
#             'res_model': 'purchase.order',
#             'res_id': self.name.id,
#             'type': 'ir.actions.act_window',
#             'view_mode': 'form',
#             'view_id': self.env.ref('purchase.purchase_order_form').id
#         }
