{
    'name': "Asset management",
    'summary': '',
    'author': "Remco Huijdts",
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'depends': ['base', 'hr'],
    'data': [
        'security/security_groups.xml',
        "security/ir.model.access.csv",
        'views/menu.xml',
        'views/category_view.xml',
        'views/device_view.xml',
        'views/asset_view.xml',
        'reports/reports.xml',
        'reports/templates.xml',
        'views/option_view.xml',
        'views/loan_agreement_view.xml'
    ],
}
