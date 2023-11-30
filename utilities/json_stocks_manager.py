### FINISHED
import shutil
from collections import Counter
from date_utilities import DateManager
from json_manager import JSONDataManager


STOCKS_DATA = 'data/stocks.json'
CURRENT_DAY_DATA = 'data/current_day_prices.json'
LAST_DAY_DATA = 'data/last_day_prices.json'


class JSONStocksDataExtractor:
    def __init__(self) -> None:
        self.stocks_data = JSONDataManager(STOCKS_DATA)
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

    def get_country_counts(self):
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

## USAGE
# class_instance = JSONStocksDataExtractor()

# print(class_instance.get_ticker_symbols())
# print(class_instance.get_countries())
# print(class_instance.get_country_counts())
# print(class_instance.get_country('AAPL'))
# print(class_instance.get_company_name('AAPL'))


class JSONStocksDayDataValidator:
    def __init__(self) -> None:
        self.current_data = JSONDataManager(CURRENT_DAY_DATA)
        self.previous_data = JSONDataManager(LAST_DAY_DATA)

    def validate_day_data(self, day_code: str) -> bool:
        """Validates the availability of data for a specific day.

        Args:
            day_code (str): "T": today, "P": previous day

        Returns:
            bool: True if data is populated completely, False if any data is missing

        Usage:
            validator_instance = JSONStocksDayDataValidator()
            validator = validator_instance.validate_day_data("P")
            print(validator)
        """
        if day_code == "T":
            prices_data = self.current_data.read_json('prices')
        elif day_code == "P":
            prices_data = self.previous_data.read_json('prices')
        else:
            return "Wrong data key entered"

        for value in prices_data.values():
            if value is None:
                return False

        return True


## USAGE
# class_instance = JSONStocksDayDataValidator()

# print(class_instance.validate_day_data('T'))
# print(class_instance.validate_day_data('P'))


class JSONStocksDayDataSetter:
    def __init__(self) -> None:
        self.current_data = JSONDataManager(CURRENT_DAY_DATA)
        self.previous_data = JSONDataManager(LAST_DAY_DATA)
        self.tickers = JSONStocksDataExtractor().get_ticker_symbols()

    def set_new_day_date(self):
        """Set today's date into current_day_prices.json, key: current_date

        Returns:
           Confirmation message
        """
        key = ["current_date"]
        value = DateManager().todays_date_str()

        self.current_data.write_json(key, value)
        return "New date set"

    def set_new_day_data(self, stock_data):
        key = ["prices"]

        keys = stock_data['tickers']
        values = stock_data['prices']
        data_storage = {key:value for key,value in zip(keys, values)}

        self.current_data.write_json(key, data_storage)
        return 'Current day data stored'

    def clear_new_day_data(self):
        #date
        key = ["current_date"]
        self.current_data.write_json(key, None)

        #ticker prices
        key = ["prices"]
        tickers = self.tickers
        for ticker in tickers:
            keys = ["prices", ticker]
            value = None

            self.current_data.write_json(keys, value)

        return "Current day data cleared"

    def copy_new_day_data_to_previous(self):

        try:
            shutil.copyfile(CURRENT_DAY_DATA, LAST_DAY_DATA)

            return "Data last day's data copy to last_day_prices.json"
        except FileNotFoundError as e:
            print(f"Error copying data: {e}")
            return None
        
    def get_stocks_data(self):
        day_data = {
            'tickers': self.tickers,
            'current_day_prices': None,
            'previous_day_prices': None
        }

        day_data['current_day_prices'] = [price for price in self.current_data.read_json('prices').values()]
        day_data['previous_day_prices'] = [price for price in self.previous_data.read_json('prices').values()]

        return day_data
    

## USAGE
class_instance = JSONStocksDayDataSetter()

# print(class_instance.set_new_day_date())
# data = {'tickers': ["AMZN", "AAPL"], 'prices': [155, 157]}
# print(class_instance.set_new_day_data(data))
# print(class_instance.clear_new_day_data())
# print(class_instance.copy_new_day_data_to_previous())
# print(class_instance.get_stocks_data())

