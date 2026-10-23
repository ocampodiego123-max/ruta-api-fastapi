import sqlite3
from pathlib import Path
from configuracion import config

RUTA_BD = Path(__file__).resolve().parent / "equipos.db"


def conexion_bd():

    conexion = sqlite3.connect(config.BASE_DATOS)

    cursor = conexion.cursor()

    return conexion, cursor


def inicializar_bd():

    conexion, cursor = conexion_bd()

    try:
        cursor.execute ("""CREATE TABLE IF NOT EXISTS equipos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            tipo TEXT NOT NULL,
                            estado TEXT NOT NULL)""")
                        
        
        conexion.commit()

    finally:
        conexion.close()
