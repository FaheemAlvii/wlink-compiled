{
    'name': 'Qr Whatsapp POS Receipts',
    'author': 'WLink',
    'description': 'static/description/index.html',
    'license': 'LGPL-3',
    'version': '16.0.1.0.0',
    'website':'https://wlink.geektechsol.com',
    'images': ['static/description/banner.png',],
    'depends': ['gts_whatsapp', 'gts_contacts_whatsapp', 'point_of_sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/select_connection.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'gts_whatsapp_pos/static/src/scss/style.scss',
            'gts_whatsapp_pos/static/src/xml/receipt.xml',
            'gts_whatsapp_pos/static/src/js/receipt.js',
            # 'gts_whatsapp_pos/static/src/xml/payment.xml',
            # 'gts_whatsapp_pos/static/src/js/payment.js',
        ]
    },
    'installable': True,
    'application': False
}