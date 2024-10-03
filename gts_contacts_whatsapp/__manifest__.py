{
    'name': 'Qr Whatsapp in Contacts app',
    'description':'static/description/index.html',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '16.0.1.0',
    'website':'https://wlink.geektechsol.com',
    'images': ['static/description/banner.png',],
    'depends': ['gts_whatsapp', 'contacts', 'sale'],
    'data': [
        'security/ir.model.access.csv',

        'wizard/message_menu.xml',

        'views/menu.xml'
    ],
    'installable': True,
    'application': False
}