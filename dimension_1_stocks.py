import asyncio
from database.database_module import DatabaseManager
from utilities.data_utilities import DataUtilities
from utilities.json_stocks_manager import JSONStocksDataExtractor
from utilities.json_stocks_manager import JSONStocksDayDataSetter
from utilities.json_stocks_manager import JSONStocksDayDataValidator
import yfinance as yf


class GetStockPrices:
    def __init__(self) -> None:
        self.ticker_processor = JSONStocksDataExtractor()

    def get_stock_price(self, ticker: str) -> float:
        """Get stock price for ticker_symbol argument

        Args:
            ticker (str): Company ticker symbol

        Returns:
            float: Current price of a compeny stock
        """
        ticker_object = yf.Ticker(ticker)
        price = ticker_object.info['currentPrice']
        return price

    async def generate_stock_prices(self) -> dict:
        """Async method that retrieves prices for 100 companies, next ticker iteration is after previous ticker price is processed

        Returns:
            dict: 2 keys: 'ticker' : with value that is list of tickers,
                          'prices' : list of prices for provides ticker symbols
        """
        tickers = self.ticker_processor.get_ticker_symbols()
        data_dict = {'tickers': tickers,
                     'prices': []}
        prices = []

        async def process_ticker(ticker):
            price = self.get_stock_price(ticker)
            prices.append(price)

        for ticker in tickers:
            await process_ticker(ticker)

        data_dict['prices'] = prices
        return data_dict


class StocksDataGenerator:
    def __init__(self) -> None:
        self.json_data_validate = JSONStocksDayDataValidator()
        self.json_set_data = JSONStocksDayDataSetter()
        self.price_generator = GetStockPrices()
        self.data_utilities = DataUtilities()
        self.database_manager = DatabaseManager()

    async def generate_stocks_prices(self):
        """Instance of GetStockPrices class and use of async generate_stock_prices method

        Returns:
            dict: 2 keys: 'ticker' : with value that is list of tickers,
                          'prices' : list of prices for provides ticker symbols
        """
        result = await self.price_generator.generate_stock_prices()
        return result
    
    def set_stocks_data(self):
        """ Daily routine for stock price retireval and saver of that data

        Returns:
            confirmation message
        """

        # set DB data
        todays_date = self.json_set_data.set_new_day_date()
        price_difference_data = {
            'tickers': None, 
            'difference_in_prices': None
        }
        
        # retrieve stocks prices
        generate_prices = asyncio.run(self.generate_stocks_prices())

        # set jsnon current day data
        self.json_set_data.set_new_day_data(generate_prices)

        # checks if previous day has data, if not it means it is first iteration 
        if self.json_data_validate.validate_day_data('P'):
            # creates data for difference calculation and DB
            stock_price_values = self.json_set_data.get_stocks_data()

            # set ticker symbols into price_difference_data
            price_difference_data['tickers'] = stock_price_values['tickers']

            # current and previous day data for difference calculation
            current_prices = stock_price_values['current_day_prices']
            previous_prices = stock_price_values['previous_day_prices']
            difference = [self.data_utilities.calculate_difference(new_value, old_value) for new_value, old_value in zip(current_prices, previous_prices)]
            price_difference_data['difference_in_prices'] = difference

            db_data = (todays_date, price_difference_data)
            sql_query = "INSERT INTO stocks_data (data_date, stocks_data) " \
                    "VALUES (%s, %s)"
            self.database_manager.save_data(sql_query, db_data)

            # copy current day data to previous day
            self.json_set_data.copy_new_day_data_to_previous()

            # clear json current day data
            self.json_set_data.clear_new_day_data()

            return f"Data is saved for {todays_date}"
          

class_instance = StocksDataGenerator()
print(class_instance.set_stocks_data())
