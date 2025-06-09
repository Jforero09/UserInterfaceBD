from fastapi import APIRouter, HTTPException
from database import get_connection
from model import Ubicacion

router = APIRouter(prefix="/ubicacion", tags=["Ubicacion"])

@router.post("/")
def insertar_ubicacion(ubicacion: Ubicacion):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ubicacion (CODUBICA, CODTIPOUBICA, UBI_CODUBICA, NOMUBICA)
            VALUES (:1, :2, :3, :4)
        """, (
            ubicacion.codubica,
            ubicacion.codtipoubica,
            ubicacion.ubi_codubica,
            ubicacion.nomubica
        ))
        conn.commit()
        return {"mensaje": "Ubicación insertada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

        
@router.get("/")
def mostrar_ubicaciones():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ubicacion")
        columnas = [col[0].lower() for col in cursor.description]
        filas = cursor.fetchall()
        return [dict(zip(columnas, fila)) for fila in filas]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar: {str(e)}")
    finally:
        cursor.close()
        conn.close()