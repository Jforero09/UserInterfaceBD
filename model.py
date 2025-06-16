from pydantic import BaseModel,EmailStr
from datetime import date
from typing import Optional
from datetime import datetime

class Ubicacion(BaseModel):
    codubica: str          # VARCHAR2(4), NOT NULL
    codtipoubica: str      # VARCHAR2(3), NOT NULL
    ubi_codubica: Optional[str] = None  # VARCHAR2(4), nullable
    nomubica: str          # VARCHAR2(30), NOT NULL

    class Config:
        from_attributes = True


class TipoUbica(BaseModel):
    codtipoubica: str
    desctipoubica: str

    class Config:
        from_attributes = True

class Usuario(BaseModel):
    concecuser: str  # VARCHAR2(5)
    codubica: str   # VARCHAR2(4)
    nombre: str     # VARCHAR2(25)
    apellido: str   # VARCHAR2(25)
    user: str       # VARCHAR2(6)
    fecharegistro: date
    email: EmailStr  # Validación automática de email
    celular: str    # VARCHAR2(16)

    class Config:
        from_attributes = True



class UsuarioSinConsecuser(BaseModel):
    codubica: str
    nombre: str
    apellido: str
    email: str
    celular: str

    class Config:
         from_attributes = True