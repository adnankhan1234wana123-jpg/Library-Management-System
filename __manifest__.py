{
    'name': 'My Library',
    'version': '17.0.1.0.0',
    'category': 'Productivity',
    'summary': 'Manage library books',
    'description': 'A simple module to manage library books.',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}