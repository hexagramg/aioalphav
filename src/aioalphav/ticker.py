import asyncio
from aioalphav.requests_base import Requests
from functools import wraps


class Ticker:
    def __init__(self, ticker: str):
        self.ticker = ticker

    def _init_params(self) -> dict:
        return {
            'symbol': self.ticker
        }

    async def time_series_intraday(self, interval, adjusted = True, outputsize = 'compact'):
        params:dict = self._init_params()
        params['function'] = 'TIME_SERIES_INTRADAY'
        params['interval'] = interval
        params['adjusted'] = adjusted
        params['outputsize'] = outputsize
        return await Requests.get_json(params)

    async def time_series_daily(self, outputsize='compact'):
        params = self._init_params()
        params['function'] = 'TIME_SERIES_DAILY'
        params['outputsize'] = outputsize
        return await Requests.get_json(params)

    async def time_series_daily_adjusted(self, outputsize='compact'):
        params = self._init_params()
        params['function'] = 'TIME_SERIES_DAILY_ADJUSTED'
        params['outputsize'] = outputsize
        return await Requests.get_json(params)

    async def time_series_weekly(self):
        params = self._init_params()
        params['function'] = 'TIME_SERIES_WEEKLY'
        return await Requests.get_json(params)

    async def time_series_weekly_adjusted(self):
        params = self._init_params()
        params['function'] = 'TIME_SERIES_WEEKLY_ADJUSTED'
        return await Requests.get_json(params)

    async def time_series_monthly(self):
        params = self._init_params()
        params['function'] = 'TIME_SERIES_MONTHLY'
        return await Requests.get_json(params)

    async def time_series_monthly_adjusted(self):
        params = self._init_params()
        params['function'] = 'TIME_SERIES_MONTHLY_ADJUSTED'
        return await Requests.get_json(params)

    async def quote_endpoint(self):
        params = self._init_params()
        params['function'] = 'GLOBAL_QUOTE'
        return await Requests.get_json(params)

    async def search_endpoint(self):
        params = self._init_params()
        params['function'] = 'SYMBOL_SEARCH'
        return await Requests.get_json(params)

    async def company_overview(self):
        params = self._init_params()
        params['function'] = 'OVERVIEW'
        return await Requests.get_json(params)

    async def earnings(self):
        params = self._init_params()
        params['function'] = 'EARNINGS'
        return await Requests.get_json(params)

    async def income_statement(self):
        params = self._init_params()
        params['function'] = 'INCOME_STATEMENT'
        return await Requests.get_json(params)

    async def balance_sheet(self):
        params = self._init_params()
        params['function'] = 'BALANCE_SHEET'
        return await Requests.get_json(params)

    async def cash_flow(self):
        params = self._init_params()
        params['function'] = 'CASH_FLOW'
        return await Requests.get_json(params)

    async def listing_delisting_status(self, state = 'active'):
        params = self._init_params()
        params['function'] = 'LISTING_STATUS'
        params['state'] = state
        return await Requests.get_json(params)

    async def earnings_calendar(self):
        params = {
            'function': 'EARNINGS_CALENDAR'
        }
        return await Requests.get_json(params)

    async def ipo_calendar(self):
        params = {
            'function': 'IPO_CALENDAR'
        }
        return await Requests.get_json(params)