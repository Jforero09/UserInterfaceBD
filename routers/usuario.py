from fastapi import APIRouter, HTTPException
from database import get_connection
from model import Usuario,UsuarioSinConsecuser
from datetime import datetime

router = APIRouter(prefix="/usuario",tags=["Usuario"])

@router.post("/")
def insertar_usuario(usuario: Usuario):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        #Valida si el usuario ya esta registrado
        cursor.execute("SELECT 1 FROM usuario WHERE CONCECUSER = :1", (usuario.concecuser,))
        if cursor.fetchone():
         raise HTTPException(status_code=409, detail="El usuario ya está registrado")


        cursor.execute("""
            INSERT INTO usuario (CONCECUSER, CODUBICA, NOMBRE, APELLIDO, USER, FECHAREGISTRO, EMAIL, CELULAR)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
        """, (
            usuario.concecuser, usuario.codubica, usuario.nombre, usuario.apellido,
            usuario.user, usuario.fecharegistro, usuario.email, usuario.celular
        ))
        conn.commit()
        return {"mensaje": "Usuario insertado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/sin_id")
def insertar_usuario_sinconsec(usuario: UsuarioSinConsecuser):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Valida si el usuario ya está registrado (por correo, user, etc., pero no por CONCECUSER)
        cursor.execute("SELECT 1 FROM usuario WHERE email = :1", (usuario.email,))
        if cursor.fetchone():
            raise HTTPException(status_code=409, detail="El usuario ya está registrado")
        
        username=usuario.nombre

        cursor.execute("""
            INSERT INTO usuario (CODUBICA, NOMBRE, APELLIDO, USERNAME, FECHAREGISTRO, EMAIL, CELULAR)
            VALUES (:1, :2, :3, :4, :5, :6, :7)
        """, (
            usuario.codubica, usuario.nombre, usuario.apellido,
            username,datetime.now(), usuario.email, usuario.celular
        ))

        conn.commit()

        # Obtener el valor generado de CONCECUSER
        cursor.execute("SELECT consecuser_seq.CURRVAL FROM dual")
        consecuser = cursor.fetchone()[0]

        return {
            "mensaje": "Usuario insertado correctamente",
            "consecuser": consecuser
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()




@router.get("/")
def mostrar_usuarios():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario")
        columnas = [col[0].lower() for col in cursor.description]
        filas = cursor.fetchall()
        return [dict(zip(columnas, fila)) for fila in filas]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
