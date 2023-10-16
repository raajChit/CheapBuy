"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper_Costco import WebScrapper_Costco
import sys
sys.path.append('../')


def test_costco_scrapper():

    description = 'brita replacement filters%2c 10 pack'
    t = WebScrapper_Costco(description)

    assert t.result is not None
