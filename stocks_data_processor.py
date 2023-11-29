import asyncio
from utilities.date_utilities import DateManager
from utilities.stocks_json_data_manager import JSONStocksDataExtractor
from utilities.stocks_json_data_manager import JSONStocksDayDataValidator
from utilities.stocks_json_data_manager import JSONStocksDayDataSetter
from database.database_module import DatabaseManager
# import yfinance as yf


# class StockPriceProcessor:
#     """class for
#     """
#     def __init__(self) -> None:
#         pass
#         self.ticker_processor = JSONStocksDataManager()
#         # self.current_date = DateManager().todays_date_str()
#         # self.current_day_data = {self.current_date: {}}

#     def get_stock_price(self, ticker):
#         ticker_object = yf.Ticker(ticker)
#         price = ticker_object.info['currentPrice']
#         return price

#     async def generate_stock_prices(self):
#         tickers = self.ticker_processor.get_ticker_symbols()
#         data_dict = {}

#         async def process_ticker(ticker):
#             price = self.get_stock_price(ticker)
#             data_dict[ticker] = price

#         for ticker in tickers:
#             await process_ticker(ticker)

#         # self.current_day_data[self.current_date] = data_dict
#         # return self.current_day_data

#     async def temp(self):
#         result = await self.generate_stock_prices()
#         return result

# # Example usage:
# stocks_data = asyncio.run(StockPriceProcessor().generate_stock_prices())
# print(stocks_data)



# # class StockDataGenerator:
# #     def __init__(self) -> None:
# #         json_processor = JSONStocksDayDataManager()

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