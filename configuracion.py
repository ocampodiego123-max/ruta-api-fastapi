from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pydantic import SecretStr


class Configuracion(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env")

    ENTORNO: Literal["desarrollo","produccion"] = "desarrollo"
    API_KEY: SecretStr = SecretStr("")
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: SecretStr = SecretStr("")
    ADMIN_USUARIO: str
    ADMIN_PASSWORD_HASH: SecretStr
    SESSION_SECRET: SecretStr


config = Configuracion()
