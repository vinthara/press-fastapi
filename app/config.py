from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str
    secret_key: str
    algorithm: str

    class Config:
        env_file = ".env"


settings = Settings()
