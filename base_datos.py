import psycopg
from configuracion import config


def conexion_bd():

    conexion = psycopg.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD.get_secret_value(),
        sslmode="require"
    )

    cursor = conexion.cursor()

    return conexion, cursor


def inicializar_bd():

    conexion, cursor = conexion_bd()

    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS equipos (
                        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        tipo VARCHAR(50) NOT NULL,
                        estado VARCHAR(30) NOT NULL)""")
        conexion.commit()

    finally:
        conexion.close()
