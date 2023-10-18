import requests
import json
import re


def extract_keywords(text):
    url = "https://api.apilayer.com/keyword"
    payload = json.dumps({"body": text})  # Convert the dictionary to a JSON string
    headers = {
      "apikey": "CWplYejyzmZ08ppb5gJ983PSmGDypuDU",
      "Content-Type": "application/json"  # Specify the content type since we're sending JSON
    }

    response = requests.post(url, headers=headers, data=payload)  # Send a POST request

    if response.status_code == 200:
        data = response.json()
        keywords = [keyword['text'] for keyword in data.get('result', [])]  # Extracting keyword texts
        return keywords
    else:
        return None  # Handle errors as appropriate for your application

def search_for_similar_products(product_name):
    keywords_list = extract_keywords(product_name)
    if not keywords_list:
        return "Error extracting keywords."

    keywords = ' '.join(keywords_list)
    print("the keywords are", keywords)
    
    # Adding site: operators for bestbuy.com and amazon.com
    site_search_query = f"({keywords} site:bestbuy.com) OR ({keywords} site:amazon.com) OR ({keywords} site:ebay.com) OR ({keywords} site:costco.com) OR ({keywords} site:walmart.com)"

    api_key = "AIzaSyBME0fKEa6lrpYhZOEXZ-I-n0X6PPIv8H0"
    custom_search_engine_id = "326742dad9a9a4cb1"

    # including the site: operators in the query ('q') parameter
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={custom_search_engine_id}&q={site_search_query}"

    response = requests.get(url)

    if response.status_code == 200:
        results = json.loads(response.text)
        # print(f"Response JSON: {json.dumps(results, indent=2)}")
        similar_products = []

        for item in results.get('items', []):
            if len(similar_products) >= 5:
                break
            product_info = {
                'title': item['title'],
                'link': item['link'],
                'snippet': item.get('snippet')
            }
            similar_products.append(product_info)

        return similar_products
    else:
        return f"Error: {response.status_code}, Response: {response.content}"
    
def extract_product_name(url):
    # Removing the protocol (http, https) and splitting the URL into parts
    parts = url.replace("http://", "").replace("https://", "").split("/")

    
    parts = parts[1:]

    
    ignore_keywords = ["c", "kp", "www", "com", "cu.ft", "http", "https"]

   
    ignore_extensions = [".html", ".htm", ".php", ".aspx"]

    product_parts = []

    for part in parts:
        # Ignoring parts that are in our ignore list
        if part in ignore_keywords:
            continue

        # Ignoring file extensions
        if any(part.endswith(ext) for ext in ignore_extensions):
            part = part.split(".")[0]  # Remove the extension

        # Replace URL encodings and special characters, and split by "+" or "-"
        sub_parts = part.replace("%20", " ").replace("+", " ").replace("-", " ").split()

        for sub in sub_parts:
            if sub and sub not in ignore_keywords:  # Further ignoring keywords
                product_parts.append(sub)

    # Joining the remaining parts with a space
    product_name = " ".join(product_parts)

    return product_name

def display_similar_products(products):
    if products:
        for index, product in enumerate(products, start=1):
            print(f"Product {index}:")
            print(f"Title: {product['title']}")
            print(f"Link: {product['link']}")
            print(f"Description: {product['snippet']}\n")
    else:
        print("No products found.")

main_product = extract_product_name("https://www.amazon.com/Farberware-FMO11AHTBKB-1000-Watt-Microwave-Stainless/dp/B01EIZSF6I/ref=sr_1_4?crid=3HSQPUOBHFU2K&keywords=microwave&qid=1697589886&sprefix=micrwave%2Caps%2C107&sr=8-4&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc")
print("The main product is: ", main_product)
products = search_for_similar_products(main_product)
if isinstance(products, list):
    display_similar_products(products)
else:
    print(products)
