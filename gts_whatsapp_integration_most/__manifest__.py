{
    'name': 'Qr WhatsApp Document Send',
    'description':'static/description/index.html',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '16.0.1.0',
    'website':'https://wlink.geektechsol.com',
    'images': ['static/description/banner.png',],
    'depends': ['gts_whatsapp', 'stock', 'purchase', 'account', 'sale', 'gts_contacts_whatsapp'],  # gts_contacts_whatsapp to re-use the messaging menu.
    'data': [
        'security/ir.model.access.csv',

        'models/inventory_message_menu/inventory_message_menu.xml',

        'views/sale.xml',
        'views/inventory.xml',
        'views/invoice.xml',
        'views/purchase.xml',
    ],
    'installable': True,
    'application': False
}
