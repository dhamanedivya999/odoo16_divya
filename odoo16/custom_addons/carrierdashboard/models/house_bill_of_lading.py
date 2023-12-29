from odoo import fields, models, api, _


class HouseBillOfLading(models.Model):
    _name = "sale.housebilloflading"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'sale House Bill Of Lading Records'

    shipper_id = fields.Many2one('res.users', string="shipper", help='Reference from Res.Users records')
    pages = fields.Char(string="pages")  # list of pages for ex : 1 of 1
    shipper_reference_id = fields.Many2one('sale.order', string="shipper's reference",
                                           help='Reference from Sales Order records')
    bill_of_lading_number = fields.Char(string="bill of lading number")  # hardcode its value as BL12152023
    carriers_reference = fields.Char(
        string="carrier's reference")  # this is Tracking reference from delivery page additional info tab
    unique_consignment_reference = fields.Char(string="unique consignment reference")  # keep it blank
    # consignee_id = fields.Many2one('res.partner', string="consignee", help='Reference from Res.Partner records')
    # consignee_id = fields.Many2one(
    #     comodel_name='res.partner',
    #     string="consignee",
    #     required=True, readonly=False, change_default=True, index=True,
    #     tracking=1)
    consignee = fields.Char(string="consignee")
    #                         related="shipper_reference_id.partner_id")  # this is customer from sales.order
    carrier_name = fields.Char(string="carrier name")  # carrier name from delivery page additional info tab
    place_of_receipt = fields.Char(string="place of receipt")  # hardcode as : Kenya
    vessel_aircraft = fields.Char(string="vessel / aircraft")  # keep it blank
    voyage_no = fields.Char(string="voyage no")  # keep it blank
    port_of_loading = fields.Char(string="port of loading")  # hardcode as : Lamu, Kenya
    port_of_discharge = fields.Char(string="port of discharge")  # hardcode as : The Hauge, Netherland
    place_of_delivery = fields.Char(string="place of delivery")  # hardcode as : The Hauge, Netherland
    final_destination = fields.Char(string="final destination")  # hardcode as : The Hauge, Netherland
    order_id = fields.Char(string="order ID")  # this is sales order no
    no_of_packages = fields.Char(string="no of packages")  # keep it blank
    product_name = fields.Char(string="product name")  # this is name of product inside sale.order notebook section
    lot_no = fields.Char(string="lot no.")  # keep it blank
    net_weight_kg = fields.Char(string="net weight(kg)")  # weight from product/inventory
    gross_weight_kg = fields.Char(string="gross weight(kg)")  # weight from product/inventory
    volume_m3 = fields.Char(string="volume (m³)")  # volume from product/inventory
    consignment_total = fields.Char(string="consignment total")  # same value as in gross wt, net wt, volume
    container_nos = fields.Char(string="container no(s)")  # keep it blank
    container_type = fields.Char(string="container type")  # keep it blank
    cargo_weight_kg = fields.Char(string="cargo weight(kg)")  # keep it blank
    original_bills_of_lading = fields.Char(string="no. of original bills of lading")  # hardcode as : 1
    incoterms_2020 = fields.Char(string="incoterms® 2020")  # keep it blank
    payable_at = fields.Char(string="payable at")  # keep it blank
    freight_charges = fields.Char(string="freight charges")  # keep it blank
    shipped_on_board_date = fields.Char(string="shipped on board date")  # keep it blank
    place_and_date_of_issue = fields.Char(string="place and date of issue")  # ?
    signatory_company = fields.Char(string="signatory company")  # hardcode as : East Africa Trade
    name_of_authorized_signatory = fields.Char(
        string="name of authorized signatory")  # this is exporter or user who is sending
    signature = fields.Binary(string="signature")  # hardcode the signature

    # ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # vals['ref'] = self.env['ir.sequence'].next_by_code('farmer.crop')
            vals['bill_of_lading_number'] = "BL12152023"
            vals['place_of_receipt'] = "Kenya"
            vals['port_of_loading'] = "Lamu, Kenya"
            vals['port_of_discharge'] = "The Hauge, Netherland"
            vals['place_of_delivery'] = "The Hauge, Netherland"
            vals['final_destination'] = "The Hauge, Netherland"
            vals['original_bills_of_lading'] = "1"
            vals['signatory_company'] = "East Africa Trade"
            vals['pages'] = "1 of 1"
        return super(HouseBillOfLading, self).create(vals_list)

    @api.onchange('shipper_reference_id')
    def onchange_shipper_reference_id(self):
        if self.shipper_reference_id:
            self.order_id = self.shipper_reference_id.name
            self.consignee = self.shipper_reference_id.partner_id.name
        else:
            self.order_id = ''
            self.consignee = ''

        for records in self:
            sale_order_lines = self.env['sale.order.line'].search([('order_id', '=', records.order_id)], limit=1)
            stock_pickings = self.env['stock.picking'].search([('sale_id', '=', records.order_id)])
            if stock_pickings:
                stock_picking_id = stock_pickings[0].id
                stock_move_lines = self.env['stock.move.line'].search([('picking_id','=',stock_picking_id)])
                records.carrier_name = stock_pickings[0].carrier_id.name
                records.carriers_reference = stock_pickings[0].carrier_tracking_ref
                records.net_weight_kg = stock_pickings[0].weight
                records.gross_weight_kg = stock_pickings[0].weight
                records.lot_no = stock_move_lines[0].lot_id.name
            else:
                records.carrier_name = ''
                records.carriers_reference = ''
                records.net_weight_kg = ''
                records.gross_weight_kg = ''
                records.lot_no = ''

            if sale_order_lines:
                records.product_name = sale_order_lines[0].name
            else:
                records.product_name = ''

    @api.onchange('shipper_id')
    def onchange_shipper_id(self):
        if self.shipper_id:
            self.name_of_authorized_signatory = self.shipper_id.name
        else:
            self.name_of_authorized_signatory = ''

    # def _compute_helper(self):
    #     for records in self:
    #         purchase_order_lines = self.env['purchase.order.line'].search([('order_id', '=', records.id)],limit=1)
    #         if purchase_order_lines:
    #             records.open_quantity = purchase_order_lines[0].open_quantity
    #         else:
    #             records.open_quantity = 0

    # @api.onchange('carrier_name')
    # def onchange_carrier_name(self):
    #     if
