{
    'name': 'Whatsapp Messaging for Contacts',
    'description': "Adds whatsapp messaging functionality to the 'Contacts' app.",
    'author': 'Muhammad Ahmad',
    'license': 'LGPL-3',
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