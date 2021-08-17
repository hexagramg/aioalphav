from __future__ import annotations
import aiohttp
import asyncio
from typing import Optional
from time import monotonic
from functools import wraps
import aiohttp.web as aioweb
import logging

class Config:
    internal: Optional[Config] = None
    def __init__(self, api_key, requests_per_minute, retries):

        self.api_key = api_key
        self.lock = requests_per_minute
        self.retries = retries

    @classmethod
    def create(cls, api_key, requests_per_minute=5, retries = 3):
        if Config.internal is None:
            Config.internal = cls(api_key, requests_per_minute, retries)
        return Config.internal

class Limit:
    """
    alpha vantage has plans that require having limiters per minute on requests
    here is the decorator class that returns wrapper on call
    """
    def __init__(self, wait_time=60):
        self.num_calls = 0
        self.time_reset = 0
        self.timer = monotonic
        self.wait = wait_time

    def _diff(self):
        return  self.time_reset - self.timer()

    def _update(self):
        self.time_reset = self.timer() + self.wait
        self.num_calls = 0

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            while True:
                if self._diff() < 0:
                    self._update()
                    logging.debug(f'updated time:{args}{kwargs}')
                if self.num_calls < Config.internal.lock:
                    self.num_calls += 1
                    logging.debug(f'passed {self.num_calls} limit {args}{kwargs}')
                    break
                else:
                    d = self._diff()
                    logging.debug(f'waiting {d} limit {args}{kwargs}')
                    await asyncio.sleep(self._diff())

            return await func(*args, **kwargs)
        return wrapper



class Requests:

    @staticmethod
    def url_from_params(params:dict):
        base = 'https://www.alphavantage.co/query?'
        params['apikey'] = Config.internal.api_key
        postfix = [f'{key}={item}' for key, item in params.items()]
        base += '&'.join(postfix)
        return base

    @staticmethod
    async def get_json(params:dict):
        url = Requests.url_from_params(params)
        return await Requests._get(url, json=True)

    @staticmethod
    async def get_text(params:dict):
        url = Requests.url_from_params(params)
        return await Requests._get(url)

    @staticmethod
    @Limit()
    async def _get(url, json=False):
        async with aiohttp.ClientSession() as session:
            retries = Config.internal.retries
            while retries:
                async with session.get(url) as response:
                    try:
                        if json:
                            result = await response.json()
                        else:
                            result = await response.text()

                    except aioweb.HTTPError as e:
                        retries -= 1
                        if not retries:
                            raise e
                    else:
                        break
        return result





