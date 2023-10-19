import sys
import os
import pytest
import responses
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from  SimilarProducts import SimilarProducts  

class TestSimilarProducts:
    @responses.activate
    def test_extract_keywords(self):
        # Mocking the API response
        responses.add(
            responses.POST, 
            'https://api.apilayer.com/keyword',
            json={'result': [{'text': 'keyword1'}, {'text': 'keyword2'}]},
            status=200
        )

        # Instantiating the class and call the method
        sp = SimilarProducts()
        keywords = sp.extract_keywords("some product description")

        
        assert keywords == ['keyword1', 'keyword2']

    @responses.activate
    def test_search_for_similar_products(self):
        
        responses.add(
            responses.POST, 
            'https://api.apilayer.com/keyword',
            json={'result': [{'text': 'keyword1'}, {'text': 'keyword2'}]},
            status=200
        )

        # replicating the API response for Google Custom Search
        responses.add(
            responses.GET, 
            'https://www.googleapis.com/customsearch/v1',
            json={'items': [{'title': 'Product 1', 'link': 'http://link-to-product1', 'snippet': 'Description 1'}]},
            status=200
        )

        
        sp = SimilarProducts()
        products = sp.search_for_similar_products("some product name")

        
        assert products == [{'title': 'Product 1', 'link': 'http://link-to-product1', 'snippet': 'Description 1'}]

    # Add more method tests as needed...

# To run the test, you would use the command:
# pytest test_similar_products.py

