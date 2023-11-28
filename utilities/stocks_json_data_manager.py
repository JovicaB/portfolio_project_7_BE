import json
from collections import Counter
from utilities import DateManager


STOCKS_DATA = 'data/stocks.json'
CURRENT_DAY_DATA = 'data/current_day_prices.json'
LAST_DAY_DATA = 'data/last_day_prices.json'


class JSONData:
    def __init__(self, filename) -> None:
        self.filename = filename

    def read_json(self, key=None):
        """
        Read data from the JSON file based on a specified key.

        This method reads the JSON file, retrieves the value associated with the provided key, and returns it.
        If no key is provided, return 1. If the key is not found, return 1. If the key is found, return 2.

        Parameters:
        - key (str, optional): The key used to retrieve the data from the JSON file.

        Returns:
        The value associated with the specified key in the JSON file if the key is present, else 1.

        Example:
        >>> json_data = JSONData("data.json")
        >>> result = json_data.read_json("my_key")
        >>> print(result)

        """
        try:
            with open(self.filename, 'r') as json_file:
                data = json.load(json_file)

                if key is not None and key in data:
                    result = data[key]
                    return result
                else:
                    return data

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data from {self.filename}: {e}")
            return None

    def write_json(self, keys, value):
        """
        Write data to the JSON file using a specified set of keys.

        This method reads the JSON file, modifies the value associated with the specified set of keys, and updates the JSON file with the new data.

        Parameters:
        - keys (list): A list of keys to navigate through the JSON structure to locate the target value.
        - value: The new value to be written to the JSON file.

        Returns:
        A message indicating the successful update of the JSON file.

        Example:
        >>> json_data = JSONData("data.json")
        >>> result = json_data.write_json(["my", "nested", "key"], "new_value")
        >>> print(result)

        """
        try:
            with open(self.filename, 'r+') as json_file:
                data = json.load(json_file)
                nested_dict = data
                for key in keys[:-1]:
                    nested_dict = nested_dict.setdefault(key, {})
                nested_dict[keys[-1]] = value
                json_file.seek(0)
                json.dump(data, json_file, indent=4)
                json_file.truncate()
            return f"'{'/'.join(keys)}' updated in the JSON file"
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading or writing data: {e}")
            return None


class JSONStocksDataManager:
    def __init__(self) -> None:
        self.stocks_data = JSONData(STOCKS_DATA)

    def get_ticker_symbols(self) -> list:
        """Retrieves the list of 100 ticker symbols from stocks.json

        Returns:
            list: list of 100 ticker symbols
        """
        tickers = [ticker[0] for ticker in self.stocks_data.read_json(
            'top_tech_companies').values()]
        return tickers

    def ticker_symbol_generator(self):
        """Ticker symbol generator: 100 ticker symbols from stocks.json

        Yields:
            _type_: _description_
        """
        for ticker in self.get_ticker_symbols():
            yield ticker

    def get_countries(self) -> list:
        companies = [ticker[1] for ticker in self.stocks_data.read_json(
            'top_tech_companies').values()]
        return list(set(companies))

    def get_country_counts(self):
        companies = [ticker[1] for ticker in self.stocks_data.read_json(
            'top_tech_companies').values()]
        country_counts = Counter(companies)
        return country_counts

    def get_country(self, ticker: str) -> str:
        for value in self.stocks_data.read_json('top_tech_companies').values():
            if value[0] == ticker:
                return value[1]

    def get_company_name(self, ticker: str):
        for key, value in self.stocks_data.read_json('top_tech_companies').items():
            if value[0] == ticker:
                return key


class JSONStocksDayDataManager:
    def __init__(self) -> None:
        self.currentday_data = JSONData(CURRENT_DAY_DATA)
        self.lastday_data = JSONData(LAST_DAY_DATA)

    def get_todays_date(self):
        result = DateManager().todays_date_str()
        return result

    def set_new_currentday(self):
        json_data = self.currentday_data.read_json()
        # set new main key
        todays_date = self.get_todays_date()
        main_key = list(json_data.keys())[0]
        self.currentday_data.write_json(main_key, todays_date)
        return main_key

    def copy_currentday_to_lastday(self):
        pass

    def validate_day_data(self):
        pass


# day_manager = JSONStocksDayDataManager()
# print(day_manager.get_todays_date())

# data = {'28-11-2023': {'AMZN': 147.73, '2353.TW': 34.8}}

# class JSONDataStockManager:

todays_date = JSONStocksDayDataManager().set_new_currentday()
print(todays_date)
