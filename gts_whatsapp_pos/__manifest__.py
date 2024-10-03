{
    'name': 'Qr Whatsapp POS Receipts',
    'description':'static/description/index.html',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '17.0.1.0',
    'depends': ['gts_whatsapp', 'gts_contacts_whatsapp', 'point_of_sale', 'account'],
    'images': ['static/description/banner_pos.png'],
    'website':'https://wlink.geektechsol.com',
    'data': [
        'security/ir.model.access.csv',
        'wizard/select_connection.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
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
