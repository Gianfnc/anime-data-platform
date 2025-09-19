from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str # Sem valor padrão!

settings = Settings()