import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from source.utils.url_shortener import shorten_url
from webdriver_manager.chrome import ChromeDriverManager

# Set working directory path
sys.path.append('../')


class WebScraper_Target:
    """
    Main class used to scrape results from Target.com

    ...

    Attributes
    ----------
    description : str
        description of the product

    Methods
    -------
    run:
        Threaded method to execute subclasses
    get_driver:
        Returns Chrome Driver
    get_url_target:
        Returns Target.com URL
    scrape_target:
        Returns scraped results
    """

    def __init__(self, description):
        """
        Parameters
        ----------
        description : str
            description of the product
        """
        # Initialize class variables
        self.description = description
        self.result = {}

    def run(self):
        """ 
        Returns final result
        """
        self.driver = self.get_driver()
        try:
            # Get results from scraping function
            results = self.scrape_target()
            # Condition to check whether results are available or not
            if len(results) == 0:
                print('Target.com results empty')
                self.result = {}
            else:
                item = results[0]
                # Find the 'a' tag containing the required item
                atag = item.find("a", {"class": "product-title-link"})
                # Extract description from the 'a' tag
                self.result['description'] = atag.text
                # Get the URL for the product page
                self.result['url'] = atag['href']
                self.result['url'] = shorten_url(self.result['url'])  # short URL is not applied currently
                # Find the element containing the price of the item
                price_element = item.find("div", {"class": "price"})
                # Find the price of the item
                self.result['price'] = price_element.find("span", {"class": "sr-only"}).text
                # Assign the site as Target.com to the result
                self.result['site'] = 'Target.com'
        except Exception as e:
            print('Target.com results exception', e)
            self.result = {}
        return self.result

    def get_driver(self):
        """ 
        Returns Chrome Driver
        """
        # Prepare driver for scraping
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(
            options=options, executable_path=ChromeDriverManager().install())
        return driver

    def get_url_target(self):
        """ 
        Returns Target.com URL for the search query
        """
        # Prepare URL for the given description
        template = 'https://www.target.com/s?search={}'
        search_term = self.description.replace(' ', '+')
        return template.format(search_term)

    def scrape_target(self):
        """ 
        Returns scraped results from Target.com
        """
        results = []
        try:
            # Call the function to get the URL
            url = self.get_url_target()
            self.driver.get(url)
            # Use BeautifulSoup to scrape the webpage
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all('div', {'class': 'search-result-gridview-items'})
        except Exception as e:
            print('Error scraping Target.com:', e)
            results = []
        return results
