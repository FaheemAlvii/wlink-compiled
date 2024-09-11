{
    'name': 'Whatsapp API Handler',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '17.0.1.0',
    'depends': ['mail'],
    'price': 20,
    'currency': 'USD',
    'description':'static/description/index.html',
    'data': [
        'security/ir.model.access.csv',
        'views/connections.xml',
        'wizard/login_menu.xml',

        'views/menu.xml'
    ],
    'installable': True,
}
