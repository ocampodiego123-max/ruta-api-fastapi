from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, StringConstraints
from enum import Enum
from typing import Annotated
from base_datos import conexion_bd
import sqlite3


app = FastAPI()

@app.get("/")
def inicio():
    return {"message": "Mi primera API esta funcionando"}



class EstadoEquipo(str, Enum):

    ACTIVO = "activo"
    MANTENIMIENTO = "en mantenimiento"
    FUERA_SERVICIO = "fuera de servicio"


class ActualizarEstado(BaseModel):
    
    estado: EstadoEquipo


TextoNoVacio = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class CrearEquipo(BaseModel):

    id : int
    nombre : TextoNoVacio
    tipo :TextoNoVacio
    estado : EstadoEquipo



@app.get("/equipos")
def listar_equipos():

    conexion, cursor = conexion_bd()

    try:
        cursor.execute("""SELECT id, nombre, tipo, estado FROM equipos""")
        resultado = cursor.fetchall()

        equipos = []

        for fila in resultado:
            fila = {"id":fila[0],
                    "nombre": fila[1],
                    "tipo": fila[2],
                    "estado": fila[3]
                    }
            equipos.append(fila)
        
        return equipos

    finally:
        conexion.close()



@app.get("/equipos/{equipo_id}")
def obtener_equipo(equipo_id: int):

    conexion, cursor = conexion_bd()

    try:
        cursor.execute("""SELECT id, nombre, tipo, estado FROM equipos WHERE id = ?""", (equipo_id,))

        fila = cursor.fetchone()

        if fila:
            equipo = {"id":fila[0], "nombre":fila[1], "tipo":fila[2], "estado":fila[3]}
            return equipo
        else:
            raise HTTPException(status_code=404, detail="Equipo no encontrado")

    finally:
        conexion.close()



@app.patch("/equipos/{equipo_id}")
def actualizar_estado(equipo_id: int, datos: ActualizarEstado):

    conexion, cursor = conexion_bd()

    try:
        cursor.execute("""UPDATE equipos SET estado = ? WHERE id = ?""",(datos.estado.value, equipo_id))

        if cursor.rowcount > 0:
            conexion.commit()
            return {"mensaje": "Estado actualizado correctamente"}
        else:
            raise HTTPException(status_code=404, detail="No se encontro equipo")
    finally:
        conexion.close()



@app.post("/equipos", status_code=201)
def crear_equipos(datos: CrearEquipo):

    conexion, cursor = conexion_bd()

    nombre = datos.nombre
    tipo = datos.tipo
    estado = datos.estado.value

    try:
        cursor.execute("""INSERT INTO equipos (nombre, tipo, estado) VALUES (?, ?, ?)""", (nombre, tipo, estado))

        conexion.commit()

        equipo_creado = {"id":cursor.lastrowid, "nombre":nombre, "tipo":tipo, "estado":estado}
        
        return equipo_creado 

    except sqlite3.Error:
        conexion.rollback()
        raise HTTPException(status_code=500, detail="No se pudo registrar el equipo")

    finally:
        conexion.close()



@app.delete("/equipos/{equipo_id}")
def eliminar_equipo(equipo_id: int):

    conexion, cursor = conexion_bd()

    try:
        cursor.execute("""DELETE FROM equipos WHERE id = ?""",(equipo_id,))

        if cursor.rowcount > 0:
            conexion.commit()
            return {"mensaje": "Equipo eliminado correctamente"}
        else:
            raise HTTPException(status_code=404, detail="Equipo no encontrado")
    finally:
        conexion.close()

        



