from fastapi import FastAPI

import asyncio
from functools import lru_cache

from . import config
from . import kafka

app = FastAPI()


@lru_cache
def get_settings():
    return config.Settings()


asyncio.create_task(kafka.consume())
asyncio.create_task(kafka.producer())
