from fastapi import APIRouter, HTTPException
from database import get_connection
from model import TipoUbica

router = APIRouter(prefix="/tipoubica", tags=["Tipo Ubicacion"])

@router.post("/")
def insertar_tipo_ubicacion(tipo: TipoUbica):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tipoubica (CODTIPOUBICA, DESCTIPOUBICA)
            VALUES (:1, :2)
        """, (
            tipo.codtipoubica,
            tipo.desctipoubica
        ))
        conn.commit()
        return {"mensaje": "Tipo de ubicación insertado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al insertar: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.get("/")
def listar_tipo_ubicacion():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tipoubica")
        columnas = [col[0].lower() for col in cursor.description]
        filas = cursor.fetchall()
        return [dict(zip(columnas, fila)) for fila in filas]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar: {str(e)}")
    finally:
        cursor.close()
        conn.close()
