from __future__ import annotations
import aiohttp
import asyncio
from typing import Optional


API_KEY = None

class ReqConfig:
    internal: Optional[ReqConfig] = None
    def __init__(self, api_key, requests_per_minute):

        self.api_key = api_key
        self.lock = asyncio.Semaphore(requests_per_minute)

    @classmethod
    def create(cls, api_key, requests_per_minute = 5):
        if ReqConfig is None:
            ReqConfig.internal = cls(api_key, requests_per_minute)
        return ReqConfig.internal

class Requests:

    async def lock(self):
        pass
