# Copyright (C) 2014-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Multi Company - Product Module',
    'version': '12.0.1.0.1',
    'category': 'Multi Company',
    'summary': 'Handle Multi company for Product Module',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'multi_company_base',
        'product',
    ],
    'data': [
        'views/view_product_template.xml',
        'views/view_product_pricelist.xml',
        'views/view_product_pricelist_item.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
    ],
    'installable': True,
}
