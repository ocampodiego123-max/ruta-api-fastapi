from pydantic import BaseModel, StringConstraints
from enum import Enum
from typing import Annotated


TextoNoVacio = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

class EstadoEquipo(str, Enum):

    ACTIVO = "activo"
    MANTENIMIENTO = "en mantenimiento"
    FUERA_SERVICIO = "fuera de servicio"


class ActualizarEstado(BaseModel):
    
    estado: EstadoEquipo


class CrearEquipo(BaseModel):

    nombre : TextoNoVacio
    tipo :TextoNoVacio
    estado : EstadoEquipo


class EquipoRespuesta(BaseModel):

    id: int
    nombre: str
    tipo: str
    estado: EstadoEquipo


class MensajeRespuesta(BaseModel):

    mensaje: str 