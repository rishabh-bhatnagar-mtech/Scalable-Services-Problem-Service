import pathlib

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    def get_database_url(self) -> str:
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    print(f"{pathlib.Path(__file__).resolve().parent.parent.parent}/deployments/.env", )

    model_config = ConfigDict(extra='allow')


def get_settings(env_file_path: str = None) -> Settings:
    if env_file_path is None:
        env_file_path = f"{pathlib.Path(__file__).resolve().parent.parent.parent}/deployments/.env"
    settings = Settings(_env_file=env_file_path)
    return settings
