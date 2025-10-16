from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # POSTGRES_HOST: str
    # POSTGRES_PORT: int
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_DATABASE: str

    POSTGRES_HOST:str ="127.0.0.1"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "admin"
    POSTGRES_DATABASE: str = "noc_pro"

    PROJECT_TITLE: str = "NOC"
    MAX_FILE_SIZE: int = 2097152  # 2MB
    MIN_FILE_SIZE: int = 1250  # 10KB

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")


settings = Settings()

