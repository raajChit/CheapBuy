"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper_Walmart import WebScrapper_Walmart
import sys
sys.path.append('../')


def test_walmart_scrapper():

    description = 'Brita Longlast Water Filter Replacement Reduces Lead 2 Count'
    t = WebScrapper_Walmart(description)
    t.start()
    t.join()
    assert t.result is not None
