from odoo import api, fields, models, _


class VendorEdit(models.Model):
    # _name = "inheritance.invoiceorder"
    _inherit = "res.partner"
    # packer_assi = fields.Char(string='Packer Assignment')
    packer_assi = fields.Selection([
        ('yes','Yes'),
        ('no','No'),
    ], default='no', string="packer_assi")