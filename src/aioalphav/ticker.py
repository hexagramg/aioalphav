import asyncio
from aioalphav.requests_base import Requests


class Ticker:
    def __init__(self, ticker: str):
        self.ticker = ticker

    async def time_series_daily(self, outputsize='compact'):
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': self.ticker,
            'outputsize': outputsize,
        }
        return await Requests.get_json(params)