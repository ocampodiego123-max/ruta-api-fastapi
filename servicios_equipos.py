from base_datos import conexion_bd
import sqlite3


def registrar_equipo(nombre, tipo, estado):

    conexion, cursor = conexion_bd()
    
    try:
        cursor.execute("""INSERT INTO equipos (nombre, tipo, estado) VALUES (?, ?, ?)""", (nombre, tipo, estado))

        conexion.commit()

        equipo_creado = {"id":cursor.lastrowid, "nombre":nombre, "tipo":tipo, "estado":estado}
        
        return equipo_creado 

    except sqlite3.Error:
        conexion.rollback()
        raise

    finally:
        conexion.close()


def obtener_equipo_servicios(equipo_id):

    conexion, cursor = conexion_bd()
    
    try:
        cursor.execute("""SELECT id, nombre, tipo, estado FROM equipos WHERE id = ?""", (equipo_id,))

        fila = cursor.fetchone()

        if fila:
            equipo = {"id":fila[0], "nombre":fila[1], "tipo":fila[2], "estado":fila[3]}
            return equipo
        else:
            return None

    finally:
        conexion.close()


def listar_equipos_servicios():

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


def eliminar_equipo_servicios(equipo_id):

    conexion, cursor = conexion_bd()

    try:
        cursor.execute("""DELETE FROM equipos WHERE id = ?""",(equipo_id,))

        if cursor.rowcount > 0:
            conexion.commit()
            return {"mensaje": "Equipo eliminado correctamente"}

        return None
    
    except sqlite3.Error:
        conexion.rollback()
        raise
    
    finally:
        conexion.close()


def actualizar_estado_servicios(equipo_id, estado):

    conexion, cursor = conexion_bd()

    try:
        cursor.execute("""UPDATE equipos SET estado = ? WHERE id = ?""",(estado, equipo_id))

        if cursor.rowcount > 0:
            conexion.commit()
            return {"mensaje": "Estado actualizado correctamente"}
        
        return None

    except sqlite3.Error:
        conexion.rollback()
        raise

    finally:
        conexion.close()