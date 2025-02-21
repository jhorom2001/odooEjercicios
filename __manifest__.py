{
    'name': 'Modulo Prueba',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Este es un módulo de prueba para Odoo.',
    'author': 'Jhonatan Romero',
    'website': 'https://tu-sitio-web.com',
    'depends': ['base'],  # Dependencia del módulo base
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'demo':[
        'demo/demo.xml'
    ],
    'installable': True,  # Hace que el módulo sea instalable
    'auto_install': False,  # No se instala automáticamente
    'application': True,  # Marca este módulo como una aplicación
}

