from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    REDIS_URL: RedisDsn

    class Config:
        env_file = '.env'
