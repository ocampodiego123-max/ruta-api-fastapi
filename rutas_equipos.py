from fastapi import APIRouter, HTTPException
import sqlite3
from modelos import CrearEquipo, EquipoRespuesta, MensajeRespuesta, ActualizarEstado
from servicios_equipos import registrar_equipo, obtener_equipo_servicios, listar_equipos_servicios, eliminar_equipo_servicios, actualizar_estado_servicios


router = APIRouter()


@router.get("/prueba")
def probar_router():
    return {"mensaje":"Router funcionando"}


@router.get("/equipos", response_model=list[EquipoRespuesta])
def listar_equipos():

    resultado = listar_equipos_servicios()

    return resultado



@router.get("/equipos/{equipo_id}", response_model=EquipoRespuesta)
def obtener_equipo(equipo_id: int):

    resultado = obtener_equipo_servicios(equipo_id)

    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontró el equipo")
    return resultado


@router.post("/equipos", status_code=201, response_model=EquipoRespuesta)
def crear_equipos(datos: CrearEquipo):

    try:
        nombre = datos.nombre
        tipo = datos.tipo
        estado = datos.estado.value

        equipo_creado = registrar_equipo(nombre, tipo, estado)

        return equipo_creado
    
    except sqlite3.Error:
        raise HTTPException(status_code=500, detail="Equipo no registrado")



@router.delete("/equipos/{equipo_id}", response_model=MensajeRespuesta)
def eliminar_equipo(equipo_id: int):

    resultado = eliminar_equipo_servicios(equipo_id)

    if resultado:
        return resultado
    else:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")



@router.patch("/equipos/{equipo_id}", response_model=MensajeRespuesta)
def actualizar_estado(equipo_id: int, datos:ActualizarEstado):

    estado = datos.estado.value
    
    resultado = actualizar_estado_servicios(equipo_id, estado)

    if resultado:
        return resultado
    else:
        raise HTTPException(status_code=404, detail="No se encontro equipo")