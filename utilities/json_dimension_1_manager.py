### FINISHED
import shutil
from collections import Counter
from date_utilities import DateManager
from json_manager import JSONDataManager


STOCKS_DATA = 'data/stocks.json'


class JSONStocksDataExtractor:
    def __init__(self) -> None:
        self.json_stock_file = STOCKS_DATA
        self.stocks_data = JSONDataManager(self.json_stock_file)
        self.main_json_key = 'top_tech_companies'


    def get_ticker_symbols(self) -> list:
        """Retrieves the list of 100 ticker symbols from stocks.json file

        Returns:
            list: list of 100 ticker symbols
        """
        tickers = [ticker[0] for ticker in self.stocks_data.read_json(
            self.main_json_key).values()]
        return tickers

    def get_countries(self) -> list:
        """Retrieves the list of countries from 100 ticker symbol companies from stocks.json file

        Returns:
            list: list of countries with no duplicates
        """
        companies = [ticker[1] for ticker in self.stocks_data.read_json(
            self.main_json_key).values()]
        return list(set(companies))

    def get_country_occurrences(self):
        """Retrieves dictionary of countries (keys) with counter as a value

        Returns:
            dict: dictionary of countries (keys) with counter as a value
        """
        companies = [ticker[1] for ticker in self.stocks_data.read_json(
            self.main_json_key).values()]
        country_counts = Counter(companies)
        return country_counts

    def get_country(self, ticker: str) -> str:
        """Get country of a company by providing its ticker symbol

        Args:
            ticker (str): ticker symbol

        Returns:
            str: country name
        """
        for value in self.stocks_data.read_json(self.main_json_key).values():
            if value[0] == ticker:
                return value[1]
        return f' Incorrect ticker symbol {ticker}'

    def get_company_name(self, ticker: str):
        """Get name of the company by providing company's ticker symbol

        Args:
            ticker (str): ticker symbol

        Returns:
            str: company name
        """
        for key, value in self.stocks_data.read_json(self.main_json_key).items():
            if value[0] == ticker:
                return key
        return f' Incorrect ticker symbol {ticker}'
