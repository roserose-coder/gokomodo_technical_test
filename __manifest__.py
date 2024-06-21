{
    'name': 'Business Model Tax and Name',
    'version': '1.1',
    'sequence': 1,
    'description': "Create selection of Taxes based on its Business model",
    'depends': [
        'base',
        'account',
        'sale_management'

    ],
    'data': [
       # 'security/ir.model.access.csv',
        'data/business_model_data.xml',
        'views/sale.xml',
        'views/account.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}