{
    'name': 'Carrier',
    'author':'Divya',
    'website':'www.odoo.com',
    'summary':'Odoo 16 development',
    'license':'LGPL-3',
    'depends':['purchase','sale','account'],
     'data':[
        'security/ir.model.access.csv',
         'data/sequence.xml',
        'views/menu.xml',
        'views/carrier.xml',
         'views/purchaseorder.xml',
         'views/sales.xml',
         'views/notebook.xml',
         'views/vendor.xml',
         'views/vendoredit.xml',
         'views/productqnty.xml',
         'views/purchasetree.xml',
         'views/house_bill_of_lading.xml',
         'report/house_bill_of_lading_template.xml',
         'report/stock_report_picking.xml',
         'report/report.xml',

         # 'views/custommodel.xml',

    ]
}