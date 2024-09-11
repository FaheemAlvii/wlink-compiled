{
    'name': 'Whatsapp Messaging for POS',
    'description':'static/description/index.html',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '17.0.1.0',   
    'depends': ['gts_whatsapp', 'gts_contacts_whatsapp', 'point_of_sale', 'account'],
    'images': ['static/description/pos_connection3.jpg'],
    # gts_contacts_whatsapp to re-use the messaging menu.
    'data': [
        # TODO: Security and icon
        'security/ir.model.access.csv',

        # 'views/pos.xml',
        'wizard/select_connection.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'gts_whatsapp_pos/static/src/scss/whatsapp_pos.scss',
            'gts_whatsapp_pos/static/src/xml/pos_whatsapp.xml',
            'gts_whatsapp_pos/static/src/js/ReceiptScreen.js',
        ]
    },

    'installable': True,
    'application': False
}
