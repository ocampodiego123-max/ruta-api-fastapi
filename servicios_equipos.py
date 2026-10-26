from base_datos import conexion_bd
import psycopg


def registrar_equipo(nombre, tipo, estado):

    conexion, cursor = conexion_bd()
    
    try:
        cursor.execute("""INSERT INTO equipos (nombre, tipo, estado) VALUES (%s, %s, %s) RETURNING id""", (nombre, tipo, estado))

        fila = cursor.fetchone()
        if fila is None:
            raise RuntimeError("No se pudo obtener el ID del equipo creado")

        nuevo_id = fila[0]

        conexion.commit()

        equipo_creado = {"id":nuevo_id, "nombre":nombre, "tipo":tipo, "estado":estado}
        
        return equipo_creado 

    except psycopg.Error:
        conexion.rollback()
        raise

    finally:
        conexion.close()


def obtener_equipo_servicios(equipo_id):

    conexion, cursor = conexion_bd()
    
    try:
        cursor.execute("""SELECT id, nombre, tipo, estado FROM equipos WHERE id = %s""", (equipo_id,))

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
        cursor.execute("""DELETE FROM equipos WHERE id = %s""",(equipo_id,))

        if cursor.rowcount > 0:
            conexion.commit()
            return {"mensaje": "Equipo eliminado correctamente"}

        return None
    
    except psycopg.Error:
        conexion.rollback()
        raise
    
    finally:
        conexion.close()


def actualizar_estado_servicios(equipo_id, estado):

    conexion, cursor = conexion_bd()

    try:
        cursor.execute("""UPDATE equipos SET estado = %s WHERE id = %s""",(estado, equipo_id))

        if cursor.rowcount > 0:
            conexion.commit()
            return {"mensaje": "Estado actualizado correctamente"}
        
        return None

    except psycopg.Error:
        conexion.rollback()
        raise

    finally:
        conexion.close()