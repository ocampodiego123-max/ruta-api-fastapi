import logging
from fastapi import FastAPI, Request
from rutas_equipos import router
from base_datos import inicializar_bd
from contextlib import asynccontextmanager
from configuracion import config
from starlette.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from autenticacion import router_auth
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app:FastAPI):
    inicializar_bd()
    yield


app = FastAPI(lifespan=lifespan, debug=config.ENTORNO == "desarrollo")


app.add_middleware(
    SessionMiddleware,
    secret_key=config.SESSION_SECRET.get_secret_value(),
    session_cookie="inventario_session",
    max_age=None,
    same_site="none",
    https_only=config.ENTORNO == "produccion",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ruta-api-frontend.onrender.com",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type"],
)

app.include_router(router_auth)
app.include_router(router) 


nivel_log = logging.INFO if config.ENTORNO == "desarrollo" else logging.WARNING

logging.basicConfig(level=nivel_log)

@app.exception_handler(Exception)
async def manejar_error_general(request: Request, exc: Exception):
    logging.exception("Error inesperado en la API")

    return JSONResponse(status_code=500, content={"detail": "Error interno del servidor"})


@app.get("/")
def inicio():
    return {"message": "Mi primera API esta funcionando"}
