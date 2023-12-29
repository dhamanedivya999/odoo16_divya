{
    'name': 'Hospital Management System',
    'author':'Divya',
    'website':'www.odoomates.tech',
    'summary':'Odoo 16 development',
    'license':'LGPL-3',
    'depends':['mail'],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
       'views/doctor.xml',
        'views/female_doctor.xml',
        'views/appointment.xml',
        'views/approval.xml',
        'views/request.xml',
    ]

}