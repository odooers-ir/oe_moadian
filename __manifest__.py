# -*- coding: utf-8 -*-
{
    "author": "odooers.ir",
    "website": "https://www.odooers.ir/",
    "name": "Tax Moadian System",
    "category": "Accounting",
    "depends": ["account"],
    "data": [
        'views/res_company.xml',
        'views/product_template.xml',
        'views/product_product.xml',
        'views/account_move.xml',
        'views/res_partner.xml',
       
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
