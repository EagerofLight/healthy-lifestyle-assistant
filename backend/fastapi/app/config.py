from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str = "test"
    POSTGRES_PASSWORD: str = "test"
    POSTGRES_DB: str = "hla_management_development"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    class Config:
        env_file = ".env" # alternative get setting from .env

settings = Settings() # init instance