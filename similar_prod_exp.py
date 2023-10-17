import requests
import json

def search_for_similar_products(product_name):
    # Extract main keywords from product name
    keywords = "airfryer"  # refine this to make it more specific if needed

    # Your actual Google API key and Custom Search Engine ID
    api_key = "AIzaSyBME0fKEa6lrpYhZOEXZ-I-n0X6PPIv8H0"
    custom_search_engine_id = "326742dad9a9a4cb1"

    # Preferred sites for individual product listings
    preferred_sites = "https://www.bestbuy.com"  # replace with your preferred websites

    # Constructing the URL for the Custom Search Engine API
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={custom_search_engine_id}&q={keywords}&siteSearch={preferred_sites}"

    # Make the API request
    response = requests.get(url)

    # If the request was successful, process the JSON data
    if response.status_code == 200:
        results = json.loads(response.text)

        # Debugging output
        print(f"Response JSON: {json.dumps(results, indent=2)}")

        similar_products = []

        for item in results.get('items', []):
            product_info = {
                'title': item['title'],
                'link': item['link'],
                'snippet': item.get('snippet')
            }
            similar_products.append(product_info)

        return similar_products
    else:
        return f"Error: {response.status_code}, Response: {response.content}"

# Function to display products
def display_similar_products(products):
    if products:
        for index, product in enumerate(products, start=1):
            print(f"Product {index}:")
            print(f"Title: {product['title']}")
            print(f"Link: {product['link']}")
            print(f"Description: {product['snippet']}\n")
    else:
        print("No products found.")

# Main product name
main_product = "LG - NeoChef 2.0 Cu. Ft. Countertop Microwave with Sensor Cooking and EasyClean - Black Stainless Steel"

# Search for similar products
products = search_for_similar_products(main_product)
if isinstance(products, list):
    display_similar_products(products)
else:
    print(products)  # print the error message if it's not a list
