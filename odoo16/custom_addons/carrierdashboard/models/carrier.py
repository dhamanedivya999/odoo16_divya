from odoo import api, fields, models, _


class CarrierDashboard(models.Model):
    _name = "carrierdashboard.carrier"
    _inherit = 'mail.thread'
    _description = "carrier Records"
    _rec_name = "orderid"

    From = fields.Char(string='From')
    to = fields.Char(string='To', required=True, tracking=True)
    ref = fields.Char(string='reference', default=lambda self: _('Orders'))
    orderid = fields.Char(string='order ID', default=lambda self: _('New'))
    product = fields.Char(string='Product', required=True, tracking=True)
    quantity = fields.Integer(string="Quantity", tracking=True)
    description = fields.Text(string="Description", tracking=True)
    # orders = fields.Char(string='Orders', required=True, tracking=True)
    mode = fields.Selection([('road', 'Road'), ('ship', 'Ship'), ('air', 'Air'), ('rail', 'Rail')],
                            string="Mode of Transport", tracking=True)
    image = fields.Binary(string="Image")
    vehicletype = fields.Char(string='Vehicle Type')
    vehiclenumber = fields.Integer(string='Vehicle Number', default=False)
    drivername = fields.Char(string='Driver Name')
    drivercontact = fields.Integer(string="Diver Contact Number")
    carriername = fields.Char(string='Carrier Name')
    trackingnumber = fields.Integer(string='Tracking Number')
    state = fields.Selection([
        ('pending', 'Pending'),
        ('all', 'All'),
        ('in transit', 'In Transit'),
        ('delivered', 'Delivered')

    ], default="pending", string="Status")
    date = fields.Date(string='Date')
    location = fields.Char(string='Current Location')
    # modeoftransport = fields.Char(string='Mode of Transport')
    remark = fields.Char(string="Remark")

    tracking_ids = fields.One2many('tracking.details', 'carrier_id', string='Tracking ID')

    documents = fields.Many2many('ir.attachment', string="Upload Document")
    document_name = fields.Char(string="File Name")
    nameofcertificate = fields.Char(string="Name of Certificate")

    # carrier_dashboard_lines = fields.One2many('tracking.details','carrier_id',string='Carrier Dashboard Lines')

    # files = fields.Many2many('ir.attachment', string='Files')

    def action_save(self):
        print('saved!')

    def action_test(self):
        for rec in self:
            rec.state = 'all'

    def action_t(self):
        for rec in self:
            rec.state = 'pending'

    def action_te(self):
        for rec in self:
            rec.state = 'in transit'

    def action_tes(self):
        for rec in self:
            rec.state = 'deliverd'

    @api.model
    def create(self, vals_list):
        if vals_list.get('orderid', 'New') == 'New':
            vals_list['orderid'] = self.env['ir.sequence'].next_by_code('carrierdashboard.carrier') or 'New'
            result = super(CarrierDashboard, self).create(vals_list)
            return result


class TrackingDetails(models.Model):
    _name = "tracking.details"
    _inherit = 'mail.thread'
    _description = "tracking details Records"

    name = fields.Char(string="Carrier name")
    # name = fields.Char(related="carrier_id.name")
    date = fields.Date(string="Date")
    location = fields.Char(string="location")
    trackingnumber = fields.Integer(string='Tracking ID')
    remark = fields.Char(string="remark")

    mode = fields.Selection([('road', 'Road'), ('ship', 'Ship'), ('air', 'Air'), ('rail', 'Rail')],
                            string="Mode of Transport", tracking=True)
    # mode = fields.Char(related="carrier_id.mode")
    # location = fields.Char(string="Location")

    carrier_id = fields.Many2one('carrierdashboard.carrier', string="Carrier Id")

# date = fields.Date(related='carrier_id.date')
# location = fields.Char(related='carrier_id.location')
# mode = fields.Char(related='carrier_id.mode')
# carriername = fields.Char(related='carrier_id.carriername')
# trackingnumber = fields.Integer(related='carrier_id.trackingnumber')
# remark = fields.Char(related='carrier_id.remark')
# carrier_id = fields.Many2one('carrierdashboard.carrier',string="carrierdashboard id")


# date = fields.Date(related='carrier_id.date')
# location = fields.Char(related='carrier_id.location')
# mode = fields.Char(related='carrier_id.mode')
# carriername = fields.Char(related='carrier_id.carriername')
# trackingnumber = fields.Integer(related='carrier_id.trackingnumber')
# remark = fields.Char(related='carrier_id.remark')
# carrier_id = fields.Many2one('carrierdashboard.carrier',string="carrierdashboard id")
# qty = fields.Integer(string="qty")
