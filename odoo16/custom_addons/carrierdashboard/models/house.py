from odoo import fields, models, api, _


class SalesHouseBillOfLading(models.Model):
    _inherit = "stock.picking"
    _description = 'sale House Bill Of Lading Records'

    shipper = fields.Char(string="shipper", help='Reference from Res.Users records')  # this is exporter
    pages = fields.Char(string="pages")  # list of pages for ex : 1 of 1
    bill_of_lading_number = fields.Char(string="bill of lading number",
                                        default=lambda self: _('New'))  # hardcode its value as BL12152023
    carriers_reference = fields.Char(
        string="carrier's reference")  # this is Tracking reference from delivery page additional info tab
    unique_consignment_reference = fields.Char(string="unique consignment reference")  # keep it blank

    consignee = fields.Char(string="consignee")  # this is customer from sale.order
    carrier_name = fields.Char(string="carrier name")  # carrier name from delivery page additional info tab
    place_of_receipt = fields.Char(string="place of receipt")  # hardcode as : Kenya
    vessel_aircraft = fields.Char(string="vessel / aircraft")  # keep it blank
    voyage_no = fields.Char(string="voyage no")  # keep it blank
    port_of_loading = fields.Char(string="port of loading")  # hardcode as : Lamu, Kenya
    port_of_discharge = fields.Char(string="port of discharge")  # hardcode as : The Hauge, Netherland
    place_of_delivery = fields.Char(string="place of delivery")  # hardcode as : The Hauge, Netherland
    final_destination = fields.Char(string="final destination")  # hardcode as : The Hauge, Netherland
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
    signature = fields.Char(string="signature")  # hardcode the signature

    # below code is added recently
    document_name = fields.Char(string='Document Name', help='Input placeholder for document')
    image = fields.Binary('Upload Signature', attachment=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['place_of_receipt'] = "Kenya"
            vals['port_of_loading'] = "Lamu, Kenya"
            vals['port_of_discharge'] = "The Hauge, Netherland"
            vals['place_of_delivery'] = "The Hauge, Netherland"
            vals['final_destination'] = "The Hauge, Netherland"
            vals['original_bills_of_lading'] = "1"
            vals['signatory_company'] = "East Africa Trade"
            vals['pages'] = "1 of 1"
            vals['bill_of_lading_number'] = self.env['ir.sequence'].next_by_code('stock.picking')

        record = super(SalesHouseBillOfLading, self).create(vals_list)
        record.sales_helper()
        return record

    def sales_helper(self):
        for records in self:
            sale_orders = self.env['sale.order'].search([('name', '=', records.origin)])

            id_of_stock_move_line = records.id
            print(id_of_stock_move_line)
            # print("Picking ID:", records.id)
            # print("Origin:", records.origin)

            # stock_move_lines = self.env['stock.move.line'].search([('picking_id', '=', records.id)]),('lot_id','!=',False)]
            stock_move_lines = self.env['stock.move.line'].search(
                [('picking_id', '=', records.id), ('lot_id', '!=', False)], order='id desc', limit=1)
            print("below stock move line")
            print("IDs of stock move lines associated with this picking:", stock_move_lines.ids)

            print("Lot IDs of stock move lines associated with this picking:", stock_move_lines.mapped('lot_id.id'))

            if stock_move_lines:
                print("inside stock_move_lines")
                records.lot_no = stock_move_lines.lot_id.name
                print("this is lot no ---->  ", records.lot_no)
            else:
                print("inside else of stock move lines")
                print("value of stock_move_lines --> ", stock_move_lines)
                records.lot_no = ''

            if sale_orders:
                id_of_sale_order = sale_orders[0].id
                print(id_of_sale_order)
                print("inside sale_orders")
                records.shipper = sale_orders[0].user_id.name
                print("this is shipper i.e. exporter --> ", records.shipper)
                records.name_of_authorized_signatory = sale_orders[0].user_id.name
                sale_order_lines = self.env['sale.order.line'].search([('order_id', '=', id_of_sale_order)])
                if sale_order_lines:
                    print("inside if of sale_order_lines")
                    # print(sale_order_lines.name)
                    len_of_pol = len(sale_order_lines)
                    for i in range(len_of_pol):
                        print(i)
                        records.product_name = sale_order_lines[0].name
                        print(records.product_name)
                else:
                    print("inside else of sale_order_lines")
                    records.product_name = ''
            else:
                print("in else of sale_orders")
                records.shipper = ''
                records.name_of_authorized_signatory = ''

                # stock_picking_id = stock_pickings[0].id
            print("this is record.id ---> ", records.id)
            print("this is sale_id ---> ", records.sale_id)
            print("this is origin ---> ", records.origin)

            # stock_move_lines = self.env['stock.move.line'].search([('picking_id', '=', records.id)])
            # id_of_stock_move_line = records.id
            # print(id_of_stock_move_line)
            # stock_move_lines = self.env['stock.move.line'].search([('picking_id', '=', 104)])
            # print("below stock move line")
            # if stock_move_lines:
            #     print("inside stock_move_lines")
            #     records.lot_no = stock_move_lines[0].lot_id.name
            #     print("this is lot no ---->  ", records.lot_no)
            # else:
            #     print("inside else of stock move lines")
            #     print("value of stock_move_lines --> ",stock_move_lines)
            #     records.lot_no = ''

            # records.carrier_name = records.carrier_id.name
            # print("this is carrier name --> ", records.carrier_name)
            # records.carriers_reference = records.carrier_tracking_ref
            # print("this is carrier reference --> ", records.carriers_reference)
            # records.net_weight_kg = records.weight
            # print("this is net_weight_kg --> ", records.net_weight_kg)
            # records.gross_weight_kg = records.weight
            # print("this is gross_weight_kg --> ", records.gross_weight_kg)