from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # database
    POSTGRES_USER: str = "test"
    POSTGRES_PASSWORD: str = "test"
    POSTGRES_DB: str = "hla_management_development"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    
    # open ai
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"
    OPENAI_API_KEY: str = ""

    # nutrition
    USDA_API_KEY: str = ""
    CALORIENINJAS_API_KEY: str = ""

    # search
    SERPER_API_KEY: str = ""

    class Config:
        env_file = ".env" # alternative get setting from .env

settings = Settings() # init instance