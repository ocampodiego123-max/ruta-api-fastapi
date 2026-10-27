from fastapi import Request, HTTPException
from pwdlib import PasswordHash
from configuracion import config
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import timedelta, datetime, timezone


router_auth = APIRouter()

class DatosLogin(BaseModel):

    usuario: str
    contrasena: str


Password_hash = PasswordHash.recommended()

def verificar_credenciales(usuario: str, contrasena:str) -> bool:

    usuario_correcto = usuario == config.ADMIN_USUARIO

    contrasena_correcta = Password_hash.verify(contrasena, config.ADMIN_PASSWORD_HASH.get_secret_value())

    return usuario_correcto and contrasena_correcta


def obtener_usuario_sesion(request: Request) -> str:

    usuario = request.session.get("usuario")
    hora_inicio_sesion = request.session.get("inicio_sesion")

    if usuario != config.ADMIN_USUARIO or not hora_inicio_sesion:
        raise HTTPException(status_code=401, detail="Debes iniciar sesion")

    hora_actual = datetime.now(timezone.utc)
    numero_hora_actual = hora_actual.timestamp()

    if numero_hora_actual - hora_inicio_sesion >= 1800:
        request.session.clear()
        raise HTTPException(status_code=401, detail="Tiempo de inicio de sesion agotado")

    return usuario



@router_auth.post("/login")
def iniciar_sesion(datos: DatosLogin, request: Request):

    if not verificar_credenciales(datos.usuario, datos.contrasena):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

    hora_actual = datetime.now(timezone.utc)
    numero_hora_actual = hora_actual.timestamp()

    request.session["usuario"] = datos.usuario
    request.session["inicio_sesion"] = numero_hora_actual

    return {"Mensaje": "inicio de sesión exitoso"}



@router_auth.post("/logout")
def cerrar_sesion(request: Request):

    request.session.clear()

    return {"mensaje": "Sesión cerrada correctamente"}



@router_auth.get("/sesion")
def validar_sesion(request: Request):

    return obtener_usuario_sesion(request)
    



