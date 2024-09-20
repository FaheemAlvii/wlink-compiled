{
    'name': 'Qr Whatsapp POS Receipts',
    'author': 'WLink',
    'description': 'static/description/index.html',
    'license': 'LGPL-3',
    'version': '16.0.1.0.0',
    'website':'https://wlink.geektechsol.com',
    'images': ['static/description/banner.png',],
    'depends': ['gts_whatsapp', 'gts_contacts_whatsapp', 'point_of_sale', 'account'],
    # gts_contacts_whatsapp to re-use the messaging menu.
    'data': [
        'security/ir.model.access.csv',

        # 'views/pos.xml',
        'wizard/select_connection.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'gts_whatsapp_pos/static/src/scss/whatsapp_pos.scss',
            'gts_whatsapp_pos/static/src/xml/pos_whatsapp.xml',
            'gts_whatsapp_pos/static/src/js/ReceiptScreen.js',
        ]
    },

    'installable': True,
    'application': False
}
