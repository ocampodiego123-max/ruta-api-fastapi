from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pydantic import SecretStr


class Configuracion(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env")

    ENTORNO: Literal["desarrollo","produccion"] = "desarrollo"
    API_KEY: SecretStr = SecretStr("")
    BASE_DATOS:str = "equipos.db"


config = Configuracion()
