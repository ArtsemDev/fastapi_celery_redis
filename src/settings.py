from redis.asyncio import Redis

from .types import Settings


SETTINGS = Settings()
redis = Redis.from_url(url=SETTINGS.REDIS_URL)
