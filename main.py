from fastapi import FastAPI;
from routers import usuario,ubicacion,tipoubica
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="API OracleBD")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")

async def root():
    return {"message":"hello world"}

app.include_router(usuario.router)
app.include_router(ubicacion.router)
app.include_router(tipoubica.router)
