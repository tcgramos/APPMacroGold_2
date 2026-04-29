from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    app_name: str = 'APPMacroGold API'
    api_prefix: str = '/api/v1'

    postgres_url: str = 'postgresql+psycopg://postgres:postgres@db:5432/appmacro'
    redis_url: str = 'redis://redis:6379/0'

    symbols: list[str] = [
        'XAUUSD', 'DXY', 'US10Y', 'BCOM', 'XAGUSD', 'COPPER', 'XPTUSD', 'FEDFUNDS'
    ]


settings = Settings()
