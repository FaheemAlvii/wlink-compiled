{
    'name': 'Whatsapp Messaging for most apps',
    'description':'static/description/index.html',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '17.0.1.0',
    'price':'0'
    'currency':'usd',
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
