from odoo import api, fields, models, _


class NoteBook(models.Model):
    _inherit = 'sale.order'
    _description = 'CarrierDashboard sales records'

    custom_field = fields.Char(string='Custom Field')
    sale_description = fields.Char(string='Sale Description')
    documents = fields.Many2many('ir.attachment', string="Upload Document")
    document_name = fields.Char(string="File Name")
    tracking_number_ids = fields.One2many('sales.carrier.details', 'tracking_number_id')

    tag_ids = fields.One2many('sales.carrier.details', 'carrier_id')

    class SalesCarrierDetails(models.Model):
        _name = "sales.carrier.details"
        _description = 'Sales Carrier Details'

        date = fields.Date(string="Date")
        current_location = fields.Char(string="Current Location")
        mode = fields.Selection([('road', 'Road'), ('ship', 'Ship'), ('air', 'Air'), ('rail', 'Rail')],
                                string="Mode Of Transport")
        carrier_name = fields.Char(string="Carrier Name")
        remark = fields.Char(string="Remark")
        color = fields.Char(string="color")

        carrier_id = fields.Many2one('sale.order', string="Carrier Id")

        vehicle_type = fields.Char(string="Vehicle Type")
        vehicle_no = fields.Char(string="Vehicle No")
        driver_name = fields.Char(string="Driver Name")
        driver_contact_number = fields.Char(string="Driver Contact Number")
        # carrier_name = fields.Char(string="Carrier Name")
        tracking_number_id = fields.Many2one('sale.order', string="Tracking Number")
