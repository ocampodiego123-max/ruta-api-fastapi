from fastapi import FastAPI
from rutas_equipos import router
from base_datos import inicializar_bd
from contextlib import asynccontextmanager
from configuracion import config



@asynccontextmanager
async def lifespan(app:FastAPI):
    inicializar_bd()
    yield


app = FastAPI(lifespan=lifespan, debug=config.ENTORNO == "desarrollo")

app.include_router(router) 



@app.get("/")
def inicio():
    return {"message": "Mi primera API esta funcionando"}

