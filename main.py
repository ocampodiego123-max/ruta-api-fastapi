from fastapi import FastAPI, HTTPException
from rutas_equipos import router


app = FastAPI()

app.include_router(router)


@app.get("/")
def inicio():
    return {"message": "Mi primera API esta funcionando"}









        



