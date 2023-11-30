import asyncio
from database.database_module import DatabaseManager
from utilities.json_stocks_manager import JSONStocksDataExtractor
from utilities.json_stocks_manager import JSONStocksDayDataSetter
from utilities.json_stocks_manager import JSONStocksDayDataValidator
import yfinance as yf


class StockPriceGatherer:
    """class for
    """
    def __init__(self) -> None:
        self.ticker_processor = JSONStocksDataExtractor()

    def get_stock_price(self, ticker):
        ticker_object = yf.Ticker(ticker)
        price = ticker_object.info['currentPrice']
        return price

    async def generate_stock_prices(self):
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
        self.price_generator = StockPriceGatherer()
        self.json_data = JSONStocksDayDataSetter()

    async def generate_stocks_prices(self):
        result = await self.price_generator.generate_stock_prices()
        return result
    

    def set_stocks_data(self):
        self.json_set_data.set_new_day_date()
        generate_prices = asyncio.run(self.generate_stocks_prices())
        self.json_set_data.set_new_day_data(generate_prices)

        if self.json_data_validate.validate_day_data('P'):
            print('sa calculate difference i copy, clear and save difference data to database')

        # self.json_data.set_new_day_date()
        # price_data = asyncio.run(self.generate_stocks_prices())

    # print(class_instance.set_new_day_date())
# data = {'tickers': ["AMZN", "AAPL"], 'prices': [155, 157]}
# print(class_instance.set_new_day_data(data))
# print(class_instance.clear_new_day_data())
# print(class_instance.copy_new_day_data_to_previous())

class_instance = StocksDataGenerator()

# generate_prices = asyncio.run(class_instance.generate_stocks_prices())
# print(generate_prices)
print(class_instance.set_stocks_data())





    # async def temp(self):
    #     result = await self.generate_stock_prices()
    #     return result

## USAGE
# class_instance = StockPriceGatherer()

# stocks_price_generator = asyncio.run(class_instance.generate_stock_prices())
# print(stocks_price_generator)








# #     @staticmethod
# #     def price_difference(old_price, new_price):
# #         return (new_price - old_price) / old_price


# # 1. generate yfinance data for 100 stocks
# # 2. populate current_day_prices.json
# # 3. check if last_day_prices.json has data otherwise just copy current_day_prices.json -> last_day_prices.json
# # 4. if last_day_prices.json has data:
#     # - create JSON string with difference in prices % and save current date and JSON data to DB
#     # - copy current_day_prices.json -> last_day_prices.json
#     # - clear current_day_prices.json
#     # - wait 24 hours for new day data