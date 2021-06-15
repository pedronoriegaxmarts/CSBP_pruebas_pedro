# -*- coding: utf-8 -*-
{
    'name': "xmarts_elearning_certificate",

    'summary': """
        """,

    'description': """
        Creación de certificado para CSBP y envio automatico del certificado al correo 
        de los participantes que han concluir cursos
    """,

    'author': "Xmarts-Marlene Núñez Barrios",
    'website': "http://www.yourcompany.com",
    'images': [
        'static/src/img/csbp.png',
        'static/src/img/conecta.png',
        'static/src/img/experience.png',
        'static/src/img/fondo_conecta.png',
    ],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Elearning',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website_slides','mail', 'website_sale','sign','contacts','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/certificate_templates.xml',
        'views/cron_certificate_email_send.xml',
        'views/inherit_slide_channel.xml',
        'views/certificate_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
