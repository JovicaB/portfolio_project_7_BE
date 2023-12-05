from abc import ABC, abstractmethod
import re
import requests
from bs4 import BeautifulSoup
from utilities.json_ads_manager import JSONAdsDataExtractor


class WebScraperInterface(ABC):
    @abstractmethod
    def scrape(self):
        """Abstract method for web scraping."""
        pass

class JobAdsCounterInterface(ABC):
    @abstractmethod
    def job_ads_count(self):
        """Abstract method to be implemented by subclasses."""
        pass

class JobAdsCounter(JobAdsCounterInterface, WebScraperInterface):
    def __init__(self, country_key):
        self.country_key = country_key

    def scrape(self):
        """Implement web scraping logic for the specific job ads web site."""
        pass

    def job_ads_count(self):
        """Implement counting logic based on the scraped data (regex)."""
        pass


class LinkedInJobAdsCounter(JobAdsCounter):
    def __init__(self, country_key):
        self.json_reader = JSONAdsDataExtractor()
        self.url = self.json_reader.get_ads_website(country_key)
        super().__init__(country_key)

    def scrape(self):
        pass
        # response = requests.get(self.url)
        # if response.status_code == 200:
        #     soup = BeautifulSoup(response.text, 'html.parser')

        #     posao_element = soup.find(string=element_to_find)

        #     if posao_element:
        #         parent_element = posao_element.find_parent()
        #         next_element = parent_element.find_next()

        #         if next_element:
        #             result_text = next_element.get_text(strip=True)
        #             return result_text
        # else:
        #     return None

    def job_ads_count(self):
        pass
        # scrape_result = self.scrape(self.word_to_search)

        # if scrape_result:
        #     result = re.search(r'\b(\d+)\b', scrape_result)
        #     if result:
        #         extracted_number = result.group(1)
        #         return extracted_number
        #     else:
        #         return None



class_instance = LinkedInJobAdsCounter('Serbia')
print(class_instance.scrape())