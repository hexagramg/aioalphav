import aioalphav as aioav
import asyncio
import pytest
import json
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
loop = asyncio.get_event_loop()

@pytest.fixture
def ticker():
    return aioav.Ticker('nvda')


@pytest.fixture
def settings():
    with open('../k.json', 'r') as k:
        s = json.load(k)
    return s


@pytest.fixture
def config(settings):
    return aioav.Config.create(api_key=settings['api'])

@pytest.fixture
def many_tickers_func():
    return [aioav.Ticker('nvda').time_series_daily() for _ in range(10)]

def test_time_series_daily(ticker, config):
    d = loop.run_until_complete(ticker.company_overview())
    assert d is not None


def test_limit(many_tickers_func, config):
    gathering = asyncio.gather(*many_tickers_func)
    d = loop.run_until_complete(gathering)

    assert d is not None

