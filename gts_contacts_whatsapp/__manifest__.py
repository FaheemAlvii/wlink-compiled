{
    'name': 'Whatsapp Messaging for Contacts',
    'description': 'static/description/index.html',
    'author': 'WLink',
    'license': 'LGPL-3',
    'price':'0',
    'currency':'usd',
    'version': '17.0.1.0',
    'depends': ['gts_whatsapp', 'contacts', 'sale'],
    'data': [
        'security/ir.model.access.csv',

        'wizard/message_menu.xml',

        'views/menu.xml'
    ],
    'installable': True,
    'application': False
}
