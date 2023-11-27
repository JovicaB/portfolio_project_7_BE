import asyncio
import time
from data.data_manager import StocksDataManager
from utilities.utilities import DateManager
import yfinance as yf


class StockDataProcessor:
    def __init__(self) -> None:
        self.ticker_processor = StocksDataManager()
        self.current_date = DateManager().todays_date_str()
        self.current_day_data = {self.current_date: {}}

    def get_stock_value(self, ticker):
        ticker_object = yf.Ticker(ticker)
        price = ticker_object.info['currentPrice']
        return price

    async def generate_stock_prices(self):
        tickers = self.ticker_processor.get_ticker_symbols()
        data_dict = {}

        async def process_ticker(ticker):
            price = self.get_stock_value(ticker)
            data_dict[ticker] = price

        for ticker in tickers:
            await process_ticker(ticker)

        self.current_day_data[self.current_date] = data_dict
        return self.current_day_data
