import logging
from fastapi import FastAPI, Request
from rutas_equipos import router
from base_datos import inicializar_bd
from contextlib import asynccontextmanager
from configuracion import config
from starlette.responses import JSONResponse


@asynccontextmanager
async def lifespan(app:FastAPI):
    inicializar_bd()
    yield


app = FastAPI(lifespan=lifespan, debug=config.ENTORNO == "desarrollo")

app.include_router(router) 


nivel_log = logging.INFO if config.ENTORNO == "desarrollo" else logging.WARNING

logging.basicConfig(level=nivel_log)
logging.info("API iniciada en modo desarrollo")

@app.exception_handler(Exception)
async def manejar_error_general(request: Request, exc: Exception):
    logging.exception("Error inesperado en la API")

    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"}
    )


@app.get("/")
def inicio():
    return {"message": "Mi primera API esta funcionando"}