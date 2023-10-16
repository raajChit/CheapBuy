"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper_Ebay import WebScrapper_Ebay
import sys
sys.path.append('../')


def test_ebay_scrapper():

    description = '3x Brita Longlast Water Filter Replacement  - NEW Sealed'
    t = WebScrapper_Ebay(description)
    
    assert t.result == {'description': '3x Brita Longlast Water Filter Replacement  - NEW Sealed',
                        'url': 'https://tinyurl.com/yg7pognr',
                        'price': '$20.00',
                        'site': 'ebay'}
