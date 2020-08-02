{
    'name': 'Reporte Personalizado HCS',
    'version': '13.0.1.0.0',
    'category': '',
    'sequence': 22,
    'author': 'HC Sinergia',
    'license': 'AGPL-3',
    'summary': '',
    'depends': [
        'web',
        'account',
        'l10n_ar',
        'l10n_ar_afipws',
    ],
    'data': [
        'views/report_templates.xml',
        'views/report_invoice.xml',
    ],
    'installable': True,
}
