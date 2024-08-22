import dataclasses
from abc import ABC, abstractmethod
from typing import Any

from fastapi import Request
from redis.asyncio import Redis

from src.conf import conf

conf = conf()


class AbstractCache(ABC):
    @abstractmethod
    async def get(self, name: str) -> Any | None:
        raise NotImplementedError

    @abstractmethod
    async def set(self, name: str, value: Any, expire: int = conf.redis.cache_expire_time) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, name: str) -> None:
        raise NotImplementedError


@dataclasses.dataclass
class RedisCache(AbstractCache):
    cache: Redis = None

    async def get(self, name: str) -> Any | None:
        data = await self.cache.get(name=name)
        return data if data else None

    async def set(self, name: str, value: Any, expire: int = conf.redis.cache_expire_time) -> None:
        data = value
        await self.cache.set(name=name, value=data, ex=expire)

    async def delete(self, name: str) -> None:
        await self.cache.delete(name)


cache: AbstractCache | None = None


async def get_cache(request: Request) -> RedisCache:
    global cache
    if cache is None:
        cache = RedisCache(cache=request.app.state.redis_instance)
    return cache
