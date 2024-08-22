import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_PATH = Path(__file__).parent.parent
conf_file = os.getenv("CONFIG_FILE") or ".docker/.env"
conf_path = BASE_PATH / conf_file

load_dotenv(conf_path)


class RedisConf(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="REDIS_", extra="ignore", case_sensitive=False, env_file=conf_path)
    host: str
    port: int = 6379
    encoding: str = "utf-8"
    decode_responses: bool = True
    db: int = 0
    cache_expire_time: int = 60
    max_connections: int = 300

    @property
    def dns(self):
        return f"redis://{self.host}:{self.port}/{self.db}"


class PostgresConf(BaseSettings, case_sensitive=False):
    model_config = SettingsConfigDict(env_prefix="POSTGRES_", extra="ignore", case_sensitive=False, env_file=conf_path)
    host: str
    port: int = 5432
    user: str = "postgres"
    password: str = "postgres"
    db: str = "lexicom"
    echo: bool = False

    echo_pool: bool = False
    pool_pre_ping: bool = True
    max_overflow: int = 20
    pool_timeout: int = 30
    pool_size: int = 30

    @property
    def dns(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class ApiConf(BaseSettings, case_sensitive=False):
    model_config = SettingsConfigDict(env_prefix="API_", extra="ignore", case_sensitive=False, env_file=conf_path)
    host: str
    port: int = 8080
    debug: bool = False


class Conf(BaseModel):
    api: ApiConf
    redis: RedisConf
    postgres: PostgresConf


def conf() -> Conf:
    conf = Conf(api=ApiConf(), redis=RedisConf(), postgres=PostgresConf())
    return conf
