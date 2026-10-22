import sqlite3

def conexion_bd():

    conexion = sqlite3.connect("equipos.db")

    cursor = conexion.cursor()

    cursor.execute ("""CREATE TABLE IF NOT EXISTS equipos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    estado TEXT NOT NULL)""")
                   

    conexion.commit()

    return conexion, cursor

