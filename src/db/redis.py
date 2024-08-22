import dataclasses

import redis.asyncio as aioredis

from src.conf import conf

conf = conf()


@dataclasses.dataclass
class RedisServer:
    redis: aioredis.Redis = None

    @classmethod
    async def connect(cls):
        if cls.redis is None:
            try:
                cls.redis = aioredis.Redis.from_url(
                    url=conf.redis.dns,
                    encoding=conf.redis.encoding,
                    decode_responses=conf.redis.decode_responses,
                    db=conf.redis.db,
                    max_connections=conf.redis.max_connections,
                )
                await cls.redis.ping()
            except aioredis.RedisError as e:
                raise e
        return cls.redis

    @classmethod
    async def close(cls):
        if cls.redis is not None:
            await cls.redis.aclose()
