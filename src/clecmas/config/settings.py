from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="CLECMAS_")

    env: str = "local"
    app_name: str = "clecmas"
    debug: bool = False
    ai_enabled: bool = False


settings = Settings()
