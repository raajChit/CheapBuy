"""
To check if
fetch_desc_bestbuy in FetchDescription
works properly
"""

from source.web_scrappers.FetchDescription import FetchDescription
import sys
sys.path.append('./')


def test_fetch_description_bestbuy():
    link = "https://www.bestbuy.com/site/dyson-outsize-total-clean-cordless-vacuum-nickel-red/6451332.p?skuId=6451332"
    fd = FetchDescription(link)
    assert fd.fetch_desc_bestbuy() == "dyson outsize total clean cordless vacuum nickel red"


"""
link = "https://www.bestbuy.com/site/dyson-outsize-total-clean-cordless-vacuum-nickel-red/6451332.p?skuId=6451332"
fd = FetchDescription(link)
print(fd.fetch_desc_bestbuy())
"""
