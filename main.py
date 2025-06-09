from fastapi import FastAPI;
from routers import usuario,ubicacion,tipoubica


app = FastAPI(title="API OracleBD")

@app.get("/")

async def root():
    return {"message":"hello world"}

app.include_router(usuario.router)
app.include_router(ubicacion.router)
app.include_router(tipoubica.router)
