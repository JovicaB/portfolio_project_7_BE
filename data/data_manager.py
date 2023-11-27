import json
from collections import Counter


STOCKS_DATA = 'data/stocks.json'


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


class StocksDataManager:
    def __init__(self) -> None:
        self.stocks_data = JSONData(STOCKS_DATA)

    def get_ticker_symbols(self):
        tickers = [ticker[0] for ticker in self.stocks_data.read_json('top_tech_companies').values()]
        return tickers
    
    def ticker_symbol_generator(self):
        for ticker in self.get_ticker_symbols():
            yield ticker
    
    def get_countries(self):
        companies = [ticker[1] for ticker in self.stocks_data.read_json('top_tech_companies').values()]
        return list(set(companies))
    
    def get_country_counts(self):
        companies = [ticker[1] for ticker in self.stocks_data.read_json('top_tech_companies').values()]
        country_counts = Counter(companies)
        return country_counts
    
    def get_country(self, ticker):
        for value in self.stocks_data.read_json('top_tech_companies').values():
            if value[0] == ticker:
                return value[1]
            
    def get_company_name(self, ticker):
        for key, value in self.stocks_data.read_json('top_tech_companies').items():
            if value[0] == ticker:
                return key


# class JSONDataStockManager:
    
